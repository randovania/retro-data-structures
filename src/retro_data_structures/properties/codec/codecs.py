"""
Codecs: how one value is read, written and converted to JSON, in each game.

A codec is a stateless object, shared by every field that uses it. All of its methods take the game, because the
encoding of a value can depend on it (the width of an asset id, the numbering of an enum, ...).

Codecs for simple values have a `fixed(game)` description: the value is a run of `struct` fields with a known size.
The compiled decoders and encoders of `BaseStruct` merge the fixed fields that follow each other into one
`struct.Struct`.
"""

from __future__ import annotations

import base64
import functools
import importlib
import struct
import typing

from retro_data_structures.base_resource import Dependency
from retro_data_structures.enums import merged as enum_support
from retro_data_structures.properties.codec.layout import Cook, Default

if typing.TYPE_CHECKING:
    import enum
    from collections.abc import Callable, Iterator, Mapping

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.game_check import Game


@functools.cache
def get_struct(endianness: str, fmt: str) -> struct.Struct:
    return struct.Struct(endianness + fmt)


class Fixed(typing.NamedTuple):
    """
    A value that is a run of `struct` fields of a known size. The templates are python expressions used by the
    generated code: `{0}`, `{1}`, ... are the unpacked fields, `{v}` is the value, `{c}` is the codec itself and `game`
    is the game.
    """

    fmt: str
    """The `struct` format, without endianness."""
    unpack: str
    """Expression that builds the value from the fields."""
    pack: str
    """Comma separated expressions that give the fields from the value."""

    def size(self) -> int:
        return struct.calcsize(">" + self.fmt)

    @property
    def columns(self) -> int:
        return len(struct.unpack(">" + self.fmt, bytes(self.size())))

    @property
    def is_identity(self) -> bool:
        return self.unpack == "{0}" and self.pack == "{v}"


class Codec:
    """The interface of a codec. Subclasses override what applies to them."""

    py_type: typing.Any = object
    """The type of the Python values."""
    asset_types: tuple[str, ...] | None = None
    field_metadata: Mapping[str, typing.Any] = {}  # noqa: RUF012
    """Added to the metadata of the fields that use this codec."""
    binds: bool = False
    """True if values hold structs that need to be given the game of their owner."""

    def default_for(self, game: Game) -> Default:
        raise TypeError(f"{self!r} has no default, give one to prop()")

    def fixed(self, game: Game) -> Fixed | None:
        """Description of the value if it's a run of struct fields in the game."""
        return None

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> typing.Any:
        """Read a value. `size` is the size of the property, or None if it isn't known (Prime, array elements)."""
        raise NotImplementedError

    def write(self, data: typing.BinaryIO, game: Game, value: typing.Any) -> None:
        raise NotImplementedError

    def to_json(self, value: typing.Any, game: Game) -> json_util.JsonValue:
        return value

    def from_json(self, data: json_util.JsonValue, game: Game) -> typing.Any:
        return data

    def dependencies(self, value: typing.Any, game: Game, asset_manager: AssetManager) -> Iterator[Dependency]:
        return iter(())

    def bind(self, value: typing.Any, game: Game) -> None:
        """Give the game to the structs in the value, in place."""

    def convert(self, value: typing.Any, source: Game | None, target: Game) -> typing.Any:
        """A copy of the value, for another game."""
        return value

    def equal(self, a: typing.Any, b: typing.Any) -> bool:
        """Equality used to tell if a value is a default. Doesn't take the game of structs into account."""
        return bool(a == b)

    def check_game(self, game: Game) -> None:
        """Raise if this codec doesn't work in the game."""


class _Scalar(Codec):
    def __init__(self, fmt: str, py_type: type, default: typing.Any, name: str):
        self.fmt = fmt
        self.py_type = py_type
        self._default = Default.of_value(default)
        self._name = name
        self._fixed = Fixed(fmt, "{0}", "{v}")

    def __repr__(self) -> str:
        return self._name

    def default_for(self, game: Game) -> Default:
        return self._default

    def fixed(self, game: Game) -> Fixed:
        return self._fixed

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> typing.Any:
        s = get_struct(game.struct_endianness, self.fmt)
        return s.unpack(data.read(s.size))[0]

    def write(self, data: typing.BinaryIO, game: Game, value: typing.Any) -> None:
        data.write(get_struct(game.struct_endianness, self.fmt).pack(value))


f32 = _Scalar("f", float, 0.0, "f32")
s32 = _Scalar("l", int, 0, "s32")
u32 = _Scalar("L", int, 0, "u32")
s16 = _Scalar("h", int, 0, "s16")
u16 = _Scalar("H", int, 0, "u16")
s8 = _Scalar("b", int, 0, "s8")
u8 = _Scalar("B", int, 0, "u8")
bool_ = _Scalar("?", bool, False, "bool_")


class _Sound(_Scalar):
    field_metadata: Mapping[str, typing.Any] = {"sound": True}  # noqa: RUF012

    def dependencies(self, value: int, game: Game, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(value)


sound = _Sound("l", int, 65535, "sound")
"""A sound id. It's an s32, with the audio group of the sound as a dependency."""


class _Guid(_Scalar):
    def to_json(self, value: bytes, game: Game) -> json_util.JsonValue:
        return value.hex()

    def from_json(self, data: json_util.JsonValue, game: Game) -> bytes:
        return bytes.fromhex(typing.cast("str", data))


guid = _Guid("16s", bytes, bytes(16), "guid")


class _String(Codec):
    py_type = str

    def __repr__(self) -> str:
        return "string"

    def default_for(self, game: Game) -> Default:
        return Default.of_value("")

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> str:
        if size is not None:
            return data.read(size)[:-1].decode("utf-8", "surrogateescape")

        # Without a size, the string ends with a null byte. Read ahead in blocks and go back after the terminator.
        chunks = []
        while True:
            block = data.read(64)
            end = block.find(b"\x00")
            if end >= 0:
                chunks.append(block[:end])
                data.seek(end + 1 - len(block), 1)
                return b"".join(chunks).decode("utf-8", "surrogateescape")
            if not block:
                raise EOFError("Unterminated string")
            chunks.append(block)

    def write(self, data: typing.BinaryIO, game: Game, value: str) -> None:
        data.write(value.encode("utf-8", "surrogateescape"))
        data.write(b"\x00")


string = _String()
"""A utf-8 string ending with a null byte. Its length comes from the property size, or the null byte in Prime."""


class _Asset(Codec):
    py_type = int

    def __init__(self, types: tuple[str, ...], ignore_mlvl: bool):
        self.asset_types = types
        self.ignore_mlvl = ignore_mlvl
        self._has_dependencies = not any(t in types for t in ("MLVL", "MREA"))

    def __repr__(self) -> str:
        return f"asset({', '.join(map(repr, self.asset_types or ()))})"

    @staticmethod
    def fmt_for(game: Game) -> str:
        if game.uses_asset_id_32:
            return "L"
        if game.uses_asset_id_64:
            return "Q"
        raise ValueError(f"{game.name} has no integer asset ids")

    def check_game(self, game: Game) -> None:
        self.fmt_for(game)

    def default_for(self, game: Game) -> Default:
        return Default.of_value(game.invalid_asset_id)

    def fixed(self, game: Game) -> Fixed:
        return Fixed(self.fmt_for(game), "{0}", "{v}")

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> int:
        s = get_struct(game.struct_endianness, self.fmt_for(game))
        return s.unpack(data.read(s.size))[0]

    def write(self, data: typing.BinaryIO, game: Game, value: int) -> None:
        data.write(get_struct(game.struct_endianness, self.fmt_for(game)).pack(value))

    def dependencies(self, value: int, game: Game, asset_manager: AssetManager) -> Iterator[Dependency]:
        if not self._has_dependencies:
            return
        deps = asset_manager.get_dependencies_for_asset(value)
        if self.ignore_mlvl:
            for it in deps:
                yield Dependency(it.type, it.id, True)
        else:
            yield from deps


def asset(*types: str, ignore_dependencies_mlvl: bool = False) -> Codec:
    """
    An asset id of one of the given types. It's 32 bits wide in Prime and Echoes and 64 bits in Corruption. Its
    default is the invalid asset id of the game. The assets are dependencies, unless they're MLVL or MREA.
    """
    return _Asset(types, ignore_dependencies_mlvl)


class _Enum(Codec):
    def __init__(self, cls: type[enum.Enum]):
        self.cls = cls
        self.py_type = cls
        self._decode_tables: dict[Game, dict[typing.Any, typing.Any]] = {}

    def __repr__(self) -> str:
        return f"enum_({self.cls.__name__})"

    def fixed(self, game: Game) -> Fixed:
        return Fixed("L", "{c}.decode({0}, game)", "{c}.encode({v}, game)")

    def decode(self, raw: int, game: Game) -> typing.Any:
        table = self._decode_tables.get(game)
        if table is None:
            table = self._decode_tables[game] = self._make_decode_table(game)
        try:
            return table[raw]
        except KeyError:
            return enum_support.from_game_value(self.cls, raw, game)

    def _make_decode_table(self, game: Game) -> dict[int, typing.Any]:
        """The members by stored value. Other values (unknown ones) go through `enum_support`."""
        game_values = enum_support.get_game_values(self.cls)
        if game_values is None:
            return {member.value: member for member in self.cls}
        return {value: self.cls[name] for name, value in game_values.get(game, {}).items()}

    def encode(self, value: enum.Enum | int, game: Game) -> int:
        if not isinstance(value, self.cls):
            value = self.cls(value)
        return enum_support.to_game_value(value, game)

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> typing.Any:
        return self.decode(get_struct(game.struct_endianness, "L").unpack(data.read(4))[0], game)

    def write(self, data: typing.BinaryIO, game: Game, value: typing.Any) -> None:
        data.write(get_struct(game.struct_endianness, "L").pack(self.encode(value, game)))

    def to_json(self, value: typing.Any, game: Game) -> json_util.JsonValue:
        return self.encode(value, game)

    def from_json(self, data: json_util.JsonValue, game: Game) -> typing.Any:
        return self.decode(typing.cast("int", data), game)

    def convert(self, value: typing.Any, source: Game | None, target: Game) -> typing.Any:
        self.encode(value, target)  # raises MemberNotInGame
        return value


def enum_[E: enum.Enum](cls: type[E]) -> Codec:
    """
    An enum, stored as an u32. The Python value is a member of `cls`, and the stored value is the one it has in the
    game (see `retro_data_structures.enums.merged`). There is no default: give one to `prop`.
    """
    return _Enum(cls)


class _Flags(_Enum):
    def __repr__(self) -> str:
        return f"flags_({self.cls.__name__})"

    def decode(self, raw: int, game: Game) -> typing.Any:
        return enum_support.flags_from_game_value(typing.cast("type[enum.IntFlag]", self.cls), raw, game)

    def encode(self, value: typing.Any, game: Game) -> int:
        if not isinstance(value, self.cls):
            value = self.cls(value)
        return enum_support.flags_to_game_value(value, game)


def flags_[F: enum.IntFlag](cls: type[F]) -> Codec:
    """Flags, stored as an u32. Like `enum_`, but translated bit by bit, and bits without a member are kept."""
    return _Flags(cls)


class _Struct(Codec):
    binds = True

    def __init__(self, cls: type, defaults: Mapping[str, typing.Any] | None, cooks: Mapping[str, Cook | str] | None):
        self.cls = cls
        self.py_type = cls
        self.defaults: dict[str, typing.Any] | None = dict(defaults) if defaults else None
        self.cooks: dict[str, Cook] | None = {n: Cook.parse(c) for n, c in cooks.items()} if cooks else None
        self._declarative: bool | None = None
        self._plans: dict[Game, typing.Any] = {}

    def __repr__(self) -> str:
        return f"struct({self.cls.__name__})"

    @property
    def declarative(self) -> bool:
        """True if the class is a `BaseStruct`, and not a hand-written one."""
        if self._declarative is None:
            from retro_data_structures.properties.base_property import BaseStruct

            self._declarative = issubclass(self.cls, BaseStruct)
        return self._declarative

    def default_for(self, game: Game) -> Default:
        return Default.of_factory(self.cls, key=("struct", self.cls))

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> typing.Any:
        if self.declarative:
            plan = self._plans.get(game)
            if plan is None:
                plan = self._plans[game] = self.cls._plan(game)  # type: ignore[attr-defined]
            return plan.decode(data, size, self.defaults, self.cooks)
        return self.cls.from_stream(data, game, size)  # type: ignore[attr-defined]

    def write(self, data: typing.BinaryIO, game: Game, value: typing.Any) -> None:
        if self.declarative:
            if value.__dict__.get("_game") is not game:
                value.set_game(game)
            value._plan(game).encode(value, data, self.defaults, self.cooks)
        else:
            value.to_stream(data, game)

    def to_json(self, value: typing.Any, game: Game) -> json_util.JsonValue:
        if self.declarative:
            return value._to_json_inner(game)
        return value.to_json()

    def from_json(self, data: json_util.JsonValue, game: Game) -> typing.Any:
        if self.declarative:
            return self.cls._from_json_inner(data, game)  # type: ignore[attr-defined]
        return self.cls.from_json(data)  # type: ignore[attr-defined]

    def dependencies(self, value: typing.Any, game: Game, asset_manager: AssetManager) -> Iterator[Dependency]:
        return value.dependencies_for(asset_manager)

    def bind(self, value: typing.Any, game: Game) -> None:
        if self.declarative and isinstance(value, self.cls):
            value.set_game(game)  # type: ignore[attr-defined]

    def convert(self, value: typing.Any, source: Game | None, target: Game) -> typing.Any:
        if self.declarative:
            return value.to_game(target)
        import copy

        return copy.deepcopy(value)

    def equal(self, a: typing.Any, b: typing.Any) -> bool:
        if self.declarative:
            return bool(a._values_equal(b))
        return bool(a == b)


def struct_(
    cls: type, defaults: Mapping[str, typing.Any] | None = None, cooks: Mapping[str, Cook | str] | None = None
) -> Codec:
    """
    A nested class: a `BaseStruct`, or a hand-written one like `Vector`.

    :param defaults: Overrides the defaults of some fields of the struct, by field name. They are the value of the
        fields that are missing when reading, what is written for the cook preference `Default` and what the
        fields are compared to for `OnlyIfModified`.
    :param cooks: Overrides the cook preference of some fields of the struct, by field name, for id-tagged games.
        It's a property of the field that holds the struct, because the struct is shared by many classes.
    """
    return _Struct(cls, defaults, cooks)


class _Array(Codec):
    py_type = list

    def __init__(self, element: Codec):
        self.element = element

    @property
    def binds(self) -> bool:  # type: ignore[override]
        return self.element.binds

    def __repr__(self) -> str:
        return f"array({self.element!r})"

    def default_for(self, game: Game) -> Default:
        return Default.of_factory(list, key=("array",))

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> list:
        endianness = game.struct_endianness
        (count,) = get_struct(endianness, "L").unpack(data.read(4))
        element = self.element
        fixed = element.fixed(game)
        if fixed is not None and fixed.is_identity:
            s = get_struct(endianness, f"{count}{fixed.fmt}")
            return list(s.unpack(data.read(s.size)))
        return [element.read(data, game, None) for _ in range(count)]

    def write(self, data: typing.BinaryIO, game: Game, value: list) -> None:
        data.write(get_struct(game.struct_endianness, "L").pack(len(value)))
        write = self.element.write
        for item in value:
            write(data, game, item)

    def to_json(self, value: list, game: Game) -> json_util.JsonValue:
        to_json = self.element.to_json
        return [to_json(item, game) for item in value]

    def from_json(self, data: json_util.JsonValue, game: Game) -> list:
        from_json = self.element.from_json
        return [from_json(item, game) for item in typing.cast("list", data)]

    def dependencies(self, value: list, game: Game, asset_manager: AssetManager) -> Iterator[Dependency]:
        for item in value:
            yield from self.element.dependencies(item, game, asset_manager)

    def bind(self, value: list, game: Game) -> None:
        bind = self.element.bind
        for item in value:
            bind(item, game)

    def convert(self, value: list, source: Game | None, target: Game) -> list:
        convert = self.element.convert
        return [convert(item, source, target) for item in value]

    def equal(self, a: list, b: list) -> bool:
        equal = self.element.equal
        return len(a) == len(b) and all(equal(x, y) for x, y in zip(a, b, strict=True))

    def check_game(self, game: Game) -> None:
        self.element.check_game(game)

    @property
    def asset_types(self) -> tuple[str, ...] | None:  # type: ignore[override]
        return self.element.asset_types


def array(element: Codec) -> Codec:
    """A list: an u32 with the number of elements, followed by the elements without ids or sizes."""
    return _Array(element)


class _Opaque(Codec):
    """A hand-written class like `Vector`, that knows how to read and write itself. It never has a game."""

    def __init__(
        self,
        module: str,
        name: str,
        fixed: Callable[[Game], Fixed] | None = None,
    ):
        self._module = module
        self._name = name
        self._cls: type | None = None
        self._fixed = fixed

    def __repr__(self) -> str:
        return self._name.lower()

    @property
    def cls(self) -> type:
        if self._cls is None:
            self._cls = getattr(importlib.import_module(self._module), self._name)
        return self._cls

    @property
    def py_type(self) -> type:
        return self.cls

    def default_for(self, game: Game) -> Default:
        return Default.of_factory(self.cls, key=("opaque", self._name))

    def fixed(self, game: Game) -> Fixed | None:
        return self._fixed(game) if self._fixed is not None else None

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> typing.Any:
        return self.cls.from_stream(data, game, size)  # type: ignore[attr-defined]

    def write(self, data: typing.BinaryIO, game: Game, value: typing.Any) -> None:
        value.to_stream(data, game)

    def to_json(self, value: typing.Any, game: Game) -> json_util.JsonValue:
        return value.to_json()

    def from_json(self, data: json_util.JsonValue, game: Game) -> typing.Any:
        return self.cls.from_json(data)  # type: ignore[attr-defined]

    def dependencies(self, value: typing.Any, game: Game, asset_manager: AssetManager) -> Iterator[Dependency]:
        return value.dependencies_for(asset_manager)

    def convert(self, value: typing.Any, source: Game | None, target: Game) -> typing.Any:
        import copy

        return copy.deepcopy(value)


def _vector_fixed(game: Game) -> Fixed:
    return Fixed("fff", "{c}.cls({0}, {1}, {2})", "{v}.x, {v}.y, {v}.z")


def _color_fixed(game: Game) -> Fixed:
    return Fixed("ffff", "{c}.cls({0}, {1}, {2}, {3})", "{v}.r, {v}.g, {v}.b, {v}.a")


def _animation_parameters_fixed(game: Game) -> Fixed:
    if game.uses_asset_id_32:
        return Fixed(
            "LLL",
            "{c}.cls({0}, {1}, {2})",
            "{c}.cls.encode_ancs({v}.ancs, game), {v}.character_index, {v}.initial_anim",
        )
    # Corruption only has the asset and the character index
    return Fixed("QL", "{c}.cls({0}, {1})", "{c}.cls.encode_ancs({v}.ancs, game), {v}.character_index")


vector = _Opaque("retro_data_structures.properties.core.vector", "Vector", _vector_fixed)
"""Three floats."""
color = _Opaque("retro_data_structures.properties.core.color", "Color", _color_fixed)
"""Four floats, RGBA. The default alpha is 0."""
spline = _Opaque("retro_data_structures.properties.core.spline", "Spline")
"""A Maya spline. It's always big endian."""
animation_parameters = _Opaque(
    "retro_data_structures.properties.core.AnimationParameters", "AnimationParameters", _animation_parameters_fixed
)
"""An ANCS asset id and two u32. The ANCS is a dependency, with the animation it uses."""


class Bytes(Codec):
    """Raw bytes with the size of the property. For fields the generator can't decode."""

    py_type = bytes

    def default_for(self, game: Game) -> Default:
        return Default.of_value(b"")

    def read(self, data: typing.BinaryIO, game: Game, size: int | None) -> bytes:
        if size is None:
            raise ValueError("Bytes needs a property size")
        return data.read(size)

    def write(self, data: typing.BinaryIO, game: Game, value: bytes) -> None:
        data.write(value)

    def to_json(self, value: bytes, game: Game) -> json_util.JsonValue:
        return base64.b64encode(value).decode("ascii")

    def from_json(self, data: json_util.JsonValue, game: Game) -> bytes:
        return base64.b64decode(typing.cast("str", data))


bytes_ = Bytes()
