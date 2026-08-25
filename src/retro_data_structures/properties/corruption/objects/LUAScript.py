# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class LUAScriptJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        abandoned_world: int
        phaaze_world: int
        unknown_0xed4a2787: str
        unknown_0x9facea01: str
        unknown_0xea46b664: str
        unknown_0xa1ecc54b: str


@dataclasses.dataclass()
class LUAScript(BaseObjectType):
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
    abandoned_world: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MLVL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2BF9AE74, original_name="AbandonedWorld"),
        },
    )
    phaaze_world: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["MLVL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x567A48F4, original_name="PhaazeWorld"),
        },
    )
    unknown_0xed4a2787: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xED4A2787, original_name="Unknown"),
        },
    )
    unknown_0x9facea01: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x9FACEA01, original_name="Unknown"),
        },
    )
    unknown_0xea46b664: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xEA46B664, original_name="Unknown"),
        },
    )
    unknown_0xa1ecc54b: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xA1ECC54B, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "LUAX"

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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BF9AE74
        abandoned_world = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x567A48F4
        phaaze_world = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED4A2787
        unknown_0xed4a2787 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9FACEA01
        unknown_0x9facea01 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA46B664
        unknown_0xea46b664 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1ECC54B
        unknown_0xa1ecc54b = data.read(property_size)[:-1].decode("utf-8")

        return cls(
            editor_properties,
            abandoned_world,
            phaaze_world,
            unknown_0xed4a2787,
            unknown_0x9facea01,
            unknown_0xea46b664,
            unknown_0xa1ecc54b,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x05")  # 5 properties
        num_properties_written = 5

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.abandoned_world != default_override.get("abandoned_world", default_asset_id):
            num_properties_written += 1
            data.write(b"+\xf9\xaet")  # 0x2bf9ae74
            data.write(b"\x00\x08")  # size
            data.write(structs.BIG_Q.pack(self.abandoned_world))

        if self.phaaze_world != default_override.get("phaaze_world", default_asset_id):
            num_properties_written += 1
            data.write(b"VzH\xf4")  # 0x567a48f4
            data.write(b"\x00\x08")  # size
            data.write(structs.BIG_Q.pack(self.phaaze_world))

        data.write(b"\xedJ'\x87")  # 0xed4a2787
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xed4a2787.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9f\xac\xea\x01")  # 0x9facea01
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x9facea01.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xeaF\xb6d")  # 0xea46b664
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xea46b664.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa1\xec\xc5K")  # 0xa1ecc54b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xa1ecc54b.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LUAScriptJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            abandoned_world=json_data["abandoned_world"],
            phaaze_world=json_data["phaaze_world"],
            unknown_0xed4a2787=json_data["unknown_0xed4a2787"],
            unknown_0x9facea01=json_data["unknown_0x9facea01"],
            unknown_0xea46b664=json_data["unknown_0xea46b664"],
            unknown_0xa1ecc54b=json_data["unknown_0xa1ecc54b"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "abandoned_world": self.abandoned_world,
            "phaaze_world": self.phaaze_world,
            "unknown_0xed4a2787": self.unknown_0xed4a2787,
            "unknown_0x9facea01": self.unknown_0x9facea01,
            "unknown_0xea46b664": self.unknown_0xea46b664,
            "unknown_0xa1ecc54b": self.unknown_0xa1ecc54b,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_unknown_0xed4a2787(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x9facea01(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xea46b664(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xa1ecc54b(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x2BF9AE74: ("abandoned_world", structs.decode_BIG_Q),
    0x567A48F4: ("phaaze_world", structs.decode_BIG_Q),
    0xED4A2787: ("unknown_0xed4a2787", _decode_unknown_0xed4a2787),
    0x9FACEA01: ("unknown_0x9facea01", _decode_unknown_0x9facea01),
    0xEA46B664: ("unknown_0xea46b664", _decode_unknown_0xea46b664),
    0xA1ECC54B: ("unknown_0xa1ecc54b", _decode_unknown_0xa1ecc54b),
}
