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
from retro_data_structures.properties.corruption.archetypes.OptionalAreaAssetTypes import OptionalAreaAssetTypes
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class OptionalAreaAssetJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        optional_area_asset_types: json_util.JsonObject
        asset: int


@dataclasses.dataclass()
class OptionalAreaAsset(BaseObjectType):
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
    optional_area_asset_types: OptionalAreaAssetTypes = dataclasses.field(
        default_factory=OptionalAreaAssetTypes,
        metadata={
            "reflection": FieldReflection[OptionalAreaAssetTypes](
                OptionalAreaAssetTypes,
                id=0x0FF44A68,
                original_name="OptionalAreaAssetTypes",
                from_json=OptionalAreaAssetTypes.from_json,
                to_json=OptionalAreaAssetTypes.to_json,
            ),
        },
    )
    asset: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0B4C13A0, original_name="Asset"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "OPAA"

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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FF44A68
        optional_area_asset_types = OptionalAreaAssetTypes.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B4C13A0
        asset = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(editor_properties, optional_area_asset_types, asset)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0f\xf4Jh")  # 0xff44a68
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.optional_area_asset_types.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0bL\x13\xa0")  # 0xb4c13a0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.asset))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("OptionalAreaAssetJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            optional_area_asset_types=OptionalAreaAssetTypes.from_json(json_data["optional_area_asset_types"]),
            asset=json_data["asset"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "optional_area_asset_types": self.optional_area_asset_types.to_json(),
            "asset": self.asset,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_optional_area_asset_types(data: typing.BinaryIO, game: Game, property_size: int) -> OptionalAreaAssetTypes:
    return OptionalAreaAssetTypes.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x0FF44A68: ("optional_area_asset_types", _decode_optional_area_asset_types),
    0x0B4C13A0: ("asset", structs.decode_BIG_Q),
}
