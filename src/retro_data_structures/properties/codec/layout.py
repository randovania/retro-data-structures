"""`prop()` and `FieldLayout`: how a dataclass field is laid out in each game."""

from __future__ import annotations

import copy
import dataclasses
import enum
import typing

from retro_data_structures.game_check import Game
from retro_data_structures.properties.errors import UNSET

if typing.TYPE_CHECKING:
    from collections.abc import Callable, Collection, Hashable, Iterable, Mapping

    from retro_data_structures.properties.codec.codecs import Codec

ID_TAGGED_GAMES = (Game.ECHOES, Game.CORRUPTION)
"""Games whose properties are `u32 id, u16 size, value`. Prime's are positional."""


class Cook(enum.Enum):
    """What the game's editor writes for a property. Only id-tagged games use anything but ALWAYS."""

    ALWAYS = "Always"
    NEVER = "Never"
    DEFAULT = "Default"
    ONLY_IF_MODIFIED = "OnlyIfModified"

    @classmethod
    def parse(cls, value: Cook | str) -> Cook:
        return value if isinstance(value, Cook) else cls(value)


class CookMode(enum.Enum):
    """
    Which optional properties of id-tagged games an encode writes (those with `Cook.ONLY_IF_MODIFIED`).

    - `PRESERVE`: an object that was decoded remembers the property ids that were in its data, and writes exactly
      those, in the same order, plus the ones that were not there but have a non-default value now. So decoding and
      encoding without changes is byte-identical. Objects that weren't decoded (new ones, `dataclasses.replace`,
      `from_json`, `to_game`) have nothing remembered and follow the cook preferences of the fields.
    - `MINIMAL`: only the cook preferences of the fields: every optional property that equals its default is left out,
      whatever the object was read with.
    """

    PRESERVE = "preserve"
    MINIMAL = "minimal"


@dataclasses.dataclass(frozen=True)
class PrimeEditor:
    """
    The positions in Prime of the properties that make up an `EditorProperties` field.
    `prime=EDITOR_PROPERTIES` is the usual `name=0, position=1, rotation=2, scale=3` without an active flag.
    Objects that don't have a position, rotation or scale pass `None` for it: it isn't stored, and the
    `EditorProperties` keeps its default.
    """

    name: int = 0
    position: int | None = 1
    rotation: int | None = 2
    scale: int | None = 3
    active: int | None = None

    def slots(self) -> list[tuple[int, str]]:
        """(position, attribute) of each slot, sorted by position."""
        result = [
            (position, slot)
            for position, slot in (
                (self.name, "name"),
                (self.position, "position"),
                (self.rotation, "rotation"),
                (self.scale, "scale"),
                (self.active, "active"),
            )
            if position is not None
        ]
        return sorted(result)


EDITOR_PROPERTIES = PrimeEditor()


_IMMUTABLE = (int, float, str, bytes, bool, type(None), tuple, frozenset, enum.Enum)


@dataclasses.dataclass(frozen=True)
class Default:
    """
    The default of a field in one game. `key` tells whether two games have the same default: it is equal for equal
    defaults and different for different ones.
    """

    key: Hashable
    value: typing.Any = None
    factory: Callable[[], typing.Any] | None = None

    @classmethod
    def of_value(cls, value: typing.Any) -> Default:
        try:
            hash(value)
            key: Hashable = ("value", type(value), value)
        except TypeError:
            key = ("value", type(value), repr(value))
        return cls(key, value)

    @classmethod
    def of_factory(cls, factory: Callable[[], typing.Any], key: Hashable | None = None) -> Default:
        return cls(("factory", id(factory)) if key is None else key, None, factory)

    @property
    def is_mutable(self) -> bool:
        return self.factory is not None or not isinstance(self.value, _IMMUTABLE)

    def make(self) -> typing.Any:
        """A new value, never shared."""
        if self.factory is not None:
            return self.factory()
        if isinstance(self.value, _IMMUTABLE):
            return self.value
        return copy.deepcopy(self.value)


@dataclasses.dataclass(frozen=True)
class FieldLayout:
    """Where and how a field is stored in one game."""

    game: Game
    codec: Codec
    default: Default
    id: int | None = None
    """Property id, for id-tagged games."""
    position: int | PrimeEditor | None = None
    """Position, for positional games (Prime)."""
    cook: Cook = Cook.ALWAYS
    order: int | None = None
    """Id-tagged games write properties in the order of the dataclass, unless this says otherwise."""
    only_if: str | None = None
    """Name of a bool field. The property is only stored when that field is true (Prime)."""
    min_count: int | None = None
    """Prime: the property is only stored when the struct's property count is at least this. See `prop`."""
    original_name: str | None = None

    @property
    def is_virtual(self) -> bool:
        """True if the field exists in the game but its class doesn't store it: its owner does."""
        return self.id is None and self.position is None


def _per_game(
    shared: typing.Any, specific: Mapping[Game, typing.Any] | None, games: Iterable[Game]
) -> dict[Game, typing.Any]:
    result = dict.fromkeys(games, shared)
    if specific:
        for game, value in specific.items():
            if game in result:
                result[game] = value
    return result


def _as_games(games: Game | Collection[Game]) -> frozenset[Game]:
    return frozenset((games,)) if isinstance(games, Game) else frozenset(games)


def prop(  # noqa: PLR0912, PLR0915
    codec: Codec,
    *,
    id: int | None = None,
    prime: int | tuple[int, int] | PrimeEditor | None = None,
    echoes: int | None = None,
    corruption: int | None = None,
    games: Game | Collection[Game] | None = None,
    default: typing.Any = dataclasses.MISSING,
    default_factory: Callable[[], typing.Any] | None = None,
    defaults: Mapping[Game, typing.Any] | None = None,
    codecs: Mapping[Game, Codec] | None = None,
    cook: Cook | str = Cook.ALWAYS,
    cooks: Mapping[Game, Cook | str] | None = None,
    order: Mapping[Game, int] | None = None,
    only_if: str | None = None,
    asset_types: Collection[str] | None = None,
    original_name: str | None = None,
) -> typing.Any:
    """
    Declare a dataclass field that is stored in one or more games.

    :param codec: How the value is encoded, unless `codecs` says otherwise for a game.
    :param id: Property id in Echoes and Corruption.
    :param prime: Position in Prime: an int, or `EDITOR_PROPERTIES`/`PrimeEditor(...)` for an `EditorProperties` field.
        `(position, min_count)` makes the property optional: it is only in the data when the struct's property count is
        at least `min_count`. Optional properties must be the last ones of the struct, and `min_count` must be the
        number of properties up to and including it (or up to the last of those with the same `min_count`).
    :param echoes: Property id in Echoes, if it's not `id`.
    :param corruption: Property id in Corruption, if it's not `id`.
    :param games: The games that have this field. By default, the ones that have an id or position. A game with no id
        or position is "virtual": the field exists in it, but the class doesn't encode it (its owner does).
    :param default: The default in every game. If neither it nor `default_factory` is given, it's the codec's default.
        When the games have different defaults, it must be `UNSET`, and `defaults` gives the default of each game.
    :param default_factory: Like `default`, but called for each new value.
    :param defaults: The default of each game, only with `default=UNSET`. A game that isn't in it has the codec's
        default.
    :param codecs: Codecs of some games, for fields that are encoded differently in them but have the same type.
    :param cook: Cook preference in every game. See `Cook`.
    :param cooks: Cook preferences of some games.
    :param order: Position in the order in which the properties of an id-tagged game are written, for the games where
        it is not the order of the dataclass.
    :param only_if: Name of a bool field of the same class. The property only exists when that field is true.
    :param asset_types: Overrides the asset types of the codec.
    :param original_name: Name in the template, when it's not just the CamelCase of the field's name.
    :return: A `dataclasses.field`. If all games that have the field agree on its default, that's the dataclass default.
        Otherwise it's `UNSET`, which becomes the game's default when the object gets a game.
    """
    per_game_defaults = default is UNSET
    if defaults is not None and not per_game_defaults:
        raise TypeError("`defaults` needs `default=UNSET`")
    if per_game_defaults and default_factory is not None:
        raise TypeError("`default=UNSET` can't be used with `default_factory`")
    min_count: int | None = None
    if isinstance(prime, tuple):
        prime, min_count = prime
    locators: dict[Game, int | PrimeEditor | None] = {}
    if id is not None:
        locators.update(dict.fromkeys(ID_TAGGED_GAMES, id))
    if echoes is not None:
        locators[Game.ECHOES] = echoes
    if corruption is not None:
        locators[Game.CORRUPTION] = corruption
    if prime is not None:
        locators[Game.PRIME] = prime

    if games is None:
        layout_games = frozenset(locators)
    else:
        layout_games = _as_games(games)
        locators = {g: v for g, v in locators.items() if g in layout_games}
    if not layout_games:
        raise ValueError("A field must be in at least one game")

    ordered_games = sorted(layout_games, key=lambda g: g.value)
    codec_per_game = _per_game(codec, codecs, ordered_games)
    cook_per_game = {g: Cook.parse(c) for g, c in _per_game(cook, cooks, ordered_games).items()}

    layouts: dict[Game, FieldLayout] = {}
    for game in ordered_games:
        game_codec = codec_per_game[game]
        if defaults is not None and game in defaults:
            game_default = Default.of_value(defaults[game])
        elif default_factory is not None:
            game_default = Default.of_factory(default_factory)
        elif default is not dataclasses.MISSING and not per_game_defaults:
            game_default = Default.of_value(default)
        else:
            game_default = game_codec.default_for(game)

        locator = locators.get(game)
        layouts[game] = FieldLayout(
            game=game,
            codec=game_codec,
            default=game_default,
            id=locator if isinstance(locator, int) and game in ID_TAGGED_GAMES else None,
            position=locator if game == Game.PRIME else None,
            cook=cook_per_game[game],
            order=order.get(game) if order else None,
            only_if=only_if if game == Game.PRIME else None,
            min_count=min_count if game == Game.PRIME else None,
            original_name=original_name,
        )

    metadata: dict[str, typing.Any] = {"layout": layouts}
    types = asset_types if asset_types is not None else next(iter(layouts.values())).codec.asset_types
    if types is not None:
        metadata["asset_types"] = list(types)
    for layout in layouts.values():
        metadata.update(layout.codec.field_metadata)

    defaults_of_games = [layout.default for layout in layouts.values()]
    first = defaults_of_games[0]
    games_disagree = any(d.key != first.key for d in defaults_of_games)
    if games_disagree != per_game_defaults:
        if games_disagree:
            raise ValueError("The games have different defaults: pass `default=UNSET`, and `defaults` if needed")
        raise ValueError("All games have the same default, so it can't be `UNSET`")
    if games_disagree:
        return dataclasses.field(default=UNSET, metadata=metadata)
    if first.is_mutable:
        return dataclasses.field(default_factory=first.make, metadata=metadata)
    return dataclasses.field(default=first.value, metadata=metadata)


def unknown_properties() -> typing.Any:
    """
    The field of the classes that don't know all of their properties, called `unknown_properties`.
    In id-tagged games, the properties that aren't in the class are read as bytes, and written back after the others.
    """
    return dataclasses.field(default_factory=dict, metadata={"unknown_properties": True})
