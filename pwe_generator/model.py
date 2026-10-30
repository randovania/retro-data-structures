"""The intermediate model: what the templates of one game say, before and after merging the games."""

from __future__ import annotations

import dataclasses
import typing

from retro_data_structures.game_check import Game

GAMES = (Game.PRIME, Game.ECHOES, Game.CORRUPTION)
GAME_IDS = {"Prime": Game.PRIME, "Echoes": Game.ECHOES, "Corruption": Game.CORRUPTION}
GAME_CONST = {Game.PRIME: "PRIME", Game.ECHOES: "ECHOES", Game.CORRUPTION: "CORRUPTION"}
ID_TAGGED = (Game.ECHOES, Game.CORRUPTION)


def lit(value: typing.Any) -> str:
    """Python source of a literal, with double quotes."""
    if isinstance(value, str):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if isinstance(value, list):
        return "[" + ", ".join(lit(v) for v in value) + "]"
    return repr(value)


EnumKey = tuple[str, ...]
"""("shared", name) for enums defined in `enums/`, ("local", owner, name) for the ones of a single class."""


@dataclasses.dataclass(frozen=True)
class Codec:
    """
    A codec expression, independent of the game's naming. `kind` is the name of the codec function in
    `retro_data_structures.properties.codec`.

    - scalars, `string`, `vector`, ...: no args
    - `asset`: args are the asset types, `flag` is ignore_dependencies_mlvl
    - `enum_`, `flags_`: `ref` is the EnumKey
    - `struct`: `ref` is the struct name, `defaults` the overrides of its fields, by field name
    - `array`: `inner` is the element codec
    """

    kind: str
    args: tuple[str, ...] = ()
    flag: bool = False
    ref: typing.Any = None
    defaults: tuple[tuple[str, Value], ...] = ()
    cooks: tuple[tuple[str, str], ...] = ()
    """For structs: overrides of the cook preference of its fields, by field name."""
    inner: Codec | None = None

    def struct_refs(self) -> typing.Iterator[str]:
        if self.kind == "struct":
            yield self.ref
        if self.inner is not None:
            yield from self.inner.struct_refs()

    def enum_refs(self) -> typing.Iterator[EnumKey]:
        if self.kind in ("enum_", "flags_"):
            yield self.ref
        if self.inner is not None:
            yield from self.inner.enum_refs()
        for _, value in self.defaults:
            if value.kind in ("enum", "flags"):
                yield value.ref

    def type_key(self) -> tuple:
        """What the Python type of the values is. Two codecs with the same key hold the same type."""
        match self.kind:
            case "f32":
                return ("float",)
            case "bool_":
                return ("bool",)
            case "string":
                return ("str",)
            case "guid":
                return ("bytes",)
            case "vector":
                return ("Vector",)
            case "color":
                return ("Color",)
            case "spline":
                return ("Spline",)
            case "animation_parameters":
                return ("AnimationParameters",)
            case "enum_" | "flags_":
                return ("enum", self.ref)
            case "struct":
                return ("struct", self.ref)
            case "array":
                assert self.inner is not None
                return ("list", self.inner.type_key())
            case _:
                return ("int",)


@dataclasses.dataclass(frozen=True)
class Value:
    """
    A default value. `kind`:
    - "py": `expr` is Python source of the value; `factory` tells if it must be made again for every use.
    - "enum"/"flags": `ref` is the EnumKey and `raw` the value in the game.
    """

    kind: str
    expr: str = ""
    factory: bool = False
    ref: typing.Any = None
    raw: int = 0


@dataclasses.dataclass
class GField:
    """A field in one game."""

    game: Game
    name: str
    original_name: str | None
    locator: typing.Any
    """The property id (Echoes, Corruption), the position (Prime), or a `PrimeEditorSpec`."""
    codec: Codec
    default: Value | None
    """None if the field has no default in the template: the codec's own default."""
    cook: str = "Always"
    only_if: str | None = None
    min_count: int | None = None
    """Prime: the property is only in the data when the struct has at least this many properties."""


@dataclasses.dataclass(frozen=True)
class PrimeEditorSpec:
    name: int
    position: int | None
    rotation: int | None
    scale: int | None
    active: int | None


@dataclasses.dataclass
class GClass:
    """A class in one game."""

    game: Game
    name: str
    kind: str
    """"object" (Script/), "tweak" (Misc/) or "struct" (Structs/)."""
    fields: list[GField]
    count_issue: str | None = None
    """Prime: why the properties with a count condition are required instead of optional."""
    atomic: bool = False
    incomplete: bool = False
    modules: list[str] | None = None
    object_type: str | int | None = None
    alias_object_types: list[str | int] = dataclasses.field(default_factory=list)
    """Other object types of the same template (the last one in the game's list is `object_type`)."""


@dataclasses.dataclass
class GEnum:
    """An enum or flags defined in a game."""

    game: Game
    name: str
    kind: str
    """"enum" or "flags"."""
    values: dict[str, typing.Any]
    owners: list[str] = dataclasses.field(default_factory=list)
    """Template files that define it inline, once for each definition. Empty for enums with a file of their own."""
    key: EnumKey = ()
    base: str = ""


@dataclasses.dataclass
class GameData:
    game: Game
    classes: dict[str, GClass] = dataclasses.field(default_factory=dict)
    enums: dict[EnumKey, GEnum] = dataclasses.field(default_factory=dict)
