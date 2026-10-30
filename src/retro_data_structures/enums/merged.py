"""
Support for enums and flags whose values are different in each game.

A merged enum is one Python class for all games. When every game gives each member the same value, it is a plain
`enum.IntEnum` or `enum.IntFlag` and nothing here is needed.

Otherwise, the Python values are canonical (the value in the newest game that has the member), and the class carries
the real value of every member in every game that has the enum:

    class Effect(enum.IntEnum):
        Normal = 0
        Fire = 1
        Ice = 2           # canonical value: the one in Corruption

        __game_values__ = {
            Game.PRIME: {"Normal": 0, "Fire": 1},
            Game.ECHOES: {"Normal": 0, "Fire": 1, "Ice": 5},
            Game.CORRUPTION: {"Normal": 0, "Fire": 1, "Ice": 2},
        }

For flags, `__game_values__` maps names to the game's mask, and the codec translates bit by bit, keeping bits that are
not named in either game as they are.

The functions here are what the `enum_` and `flags_` codecs use. A member that the game doesn't have raises
`MemberNotInGame`.
"""

from __future__ import annotations

import enum
import typing

from retro_data_structures.properties.errors import MemberNotInGame

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game

GameValues = dict["Game", dict[str, typing.Any]]


def get_game_values(enum_cls: type) -> GameValues | None:
    """The `__game_values__` of an enum class, or None when it has the same values in every game."""
    return getattr(enum_cls, "__game_values__", None)


def has_member(member: enum.Enum, game: Game) -> bool:
    """True if the member exists in the game."""
    game_values = get_game_values(type(member))
    if game_values is None:
        return True
    return member.name in game_values.get(game, ())


_reverse_cache: dict[tuple[type, Game], dict[typing.Any, enum.Enum]] = {}


def _reverse(enum_cls: type[enum.Enum], game: Game) -> dict[typing.Any, enum.Enum]:
    key = (enum_cls, game)
    result = _reverse_cache.get(key)
    if result is None:
        values = get_game_values(enum_cls)
        assert values is not None
        result = {value: enum_cls[name] for name, value in values.get(game, {}).items()}
        _reverse_cache[key] = result
    return result


def to_game_value(member: enum.Enum, game: Game) -> typing.Any:
    """The value of the member in the game. Raises MemberNotInGame."""
    game_values = get_game_values(type(member))
    if game_values is None:
        return member.value
    try:
        return game_values[game][member.name]
    except KeyError:
        raise MemberNotInGame(type(member), member.name, game) from None


def from_game_value[E: enum.Enum](enum_cls: type[E], value: typing.Any, game: Game) -> E:
    """The member that has the given value in the game."""
    if get_game_values(enum_cls) is None:
        return enum_cls(value)
    try:
        return typing.cast("E", _reverse(enum_cls, game)[value])
    except KeyError:
        result = enum_cls._missing_(value)
        if result is None:
            raise ValueError(f"{value!r} is not a valid {enum_cls.__name__} in {game.name}") from None
        return typing.cast("E", result)


class AllowUnknownValues:
    """
    Mixin for enums that must accept values they have no member for. Such a value becomes a pseudo-member named
    `Unknown_<value>`. It only supports enums with the same value in every game.

        class InventorySlotEnum(AllowUnknownValues, enum.IntEnum): ...
    """

    @classmethod
    def _missing_(cls, value: object) -> typing.Any:
        if not isinstance(value, int):
            return None
        obj: typing.Any = int.__new__(cls, value)  # type: ignore[type-var]
        obj._name_ = f"Unknown_{value}"
        obj._value_ = value
        return obj


# Flags


_flag_tables: dict[type, list[tuple[int, str]]] = {}


def _single_bit_members(flags_cls: type[enum.Flag]) -> list[tuple[int, str]]:
    result = _flag_tables.get(flags_cls)
    if result is None:
        result = [
            (member.value, name)
            for name, member in flags_cls.__members__.items()
            if member.value != 0 and member.value & (member.value - 1) == 0
        ]
        _flag_tables[flags_cls] = result
    return result


def flags_to_game_value(flags: enum.IntFlag, game: Game) -> int:
    """Translate canonical flags to the mask used by the game. Unknown bits are kept."""
    game_values = get_game_values(type(flags))
    value = int(flags)
    if game_values is None:
        return value

    result = 0
    remaining = value
    for canonical, name in _single_bit_members(type(flags)):
        if value & canonical:
            try:
                result |= game_values[game][name]
            except KeyError:
                raise MemberNotInGame(type(flags), name, game) from None
            remaining &= ~canonical
    return result | remaining


def flags_from_game_value[F: enum.IntFlag](flags_cls: type[F], value: int, game: Game) -> F:
    """Translate the mask used by the game to canonical flags. Unknown bits are kept."""
    game_values = get_game_values(flags_cls)
    if game_values is None:
        return flags_cls(value)

    result = 0
    remaining = value
    in_game = game_values.get(game, {})
    for canonical, name in _single_bit_members(flags_cls):
        game_bits = in_game.get(name)
        if game_bits and (value & game_bits) == game_bits:
            result |= canonical
            remaining &= ~game_bits
    return flags_cls(result | remaining)
