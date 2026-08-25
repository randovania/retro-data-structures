# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PlayerProxyJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        proxy_type: int
        unknown_0xd62f2d4e: bool
        unknown_0x0847909f: bool
        slave_offset: json_util.JsonValue


class ProxyType(enum.IntEnum):
    Unknown1 = 3560604011
    Unknown2 = 3638325778
    Unknown3 = 2293645153
    Unknown4 = 2459374031
    Unknown5 = 2561452093
    Unknown6 = 3823934638
    Unknown7 = 1939145129
    Unknown8 = 1377309871
    Unknown9 = 2544156382

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class PlayerProxy(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    proxy_type: ProxyType = dataclasses.field(
        default=ProxyType.Unknown1,
        metadata={
            "reflection": FieldReflection[ProxyType](
                ProxyType,
                id=0x9654AF0E,
                original_name="ProxyType",
                from_json=ProxyType.from_json,
                to_json=ProxyType.to_json,
            ),
        },
    )
    unknown_0xd62f2d4e: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xD62F2D4E, original_name="Unknown"),
        },
    )
    unknown_0x0847909f: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0847909F, original_name="Unknown"),
        },
    )
    slave_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x8927B141, original_name="SlaveOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PLPX"

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9654AF0E
        proxy_type = ProxyType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD62F2D4E
        unknown_0xd62f2d4e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0847909F
        unknown_0x0847909f = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8927B141
        slave_offset = Vector.from_stream(data, game, property_size)

        return cls(editor_properties, proxy_type, unknown_0xd62f2d4e, unknown_0x0847909f, slave_offset)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x04")  # 4 properties
        num_properties_written = 4

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x96T\xaf\x0e")  # 0x9654af0e
        data.write(b"\x00\x04")  # size
        self.proxy_type.to_stream(data, game)

        data.write(b"\xd6/-N")  # 0xd62f2d4e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xd62f2d4e))

        data.write(b"\x08G\x90\x9f")  # 0x847909f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x0847909f))

        if self.slave_offset != default_override.get("slave_offset", Vector(x=0.0, y=0.0, z=0.0)):
            num_properties_written += 1
            data.write(b"\x89'\xb1A")  # 0x8927b141
            data.write(b"\x00\x0c")  # size
            self.slave_offset.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerProxyJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            proxy_type=ProxyType.from_json(json_data["proxy_type"]),
            unknown_0xd62f2d4e=json_data["unknown_0xd62f2d4e"],
            unknown_0x0847909f=json_data["unknown_0x0847909f"],
            slave_offset=Vector.from_json(json_data["slave_offset"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "proxy_type": self.proxy_type.to_json(),
            "unknown_0xd62f2d4e": self.unknown_0xd62f2d4e,
            "unknown_0x0847909f": self.unknown_0x0847909f,
            "slave_offset": self.slave_offset.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_proxy_type(data: typing.BinaryIO, game: Game, property_size: int) -> ProxyType:
    return ProxyType.from_stream(data, game)


def _decode_slave_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x9654AF0E: ("proxy_type", _decode_proxy_type),
    0xD62F2D4E: ("unknown_0xd62f2d4e", structs.decode_BIG_bool_),
    0x0847909F: ("unknown_0x0847909f", structs.decode_BIG_bool_),
    0x8927B141: ("slave_offset", _decode_slave_offset),
}
