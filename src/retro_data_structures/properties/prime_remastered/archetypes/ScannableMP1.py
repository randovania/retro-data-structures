# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing
import uuid

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime_remastered.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ScannableMP1Json(typing_extensions.TypedDict):
        scan_file: str
        unk_bool: bool


def _from_json_scan_file(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _to_json_scan_file(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


@dataclasses.dataclass()
class ScannableMP1(BaseProperty):
    scan_file: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0x1A73E2B4,
                original_name="Scan File",
                from_json=_from_json_scan_file,
                to_json=_to_json_scan_file,
            ),
        },
    )
    unk_bool: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x05264039, original_name="Unk Bool"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.LITTLE_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 2:
            return None

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x1A73E2B4
        scan_file = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x05264039
        unk_bool = structs.LITTLE_bool_.unpack(data.read(1))[0]

        return cls(scan_file, unk_bool)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x01\x00")  # 1 properties
        num_properties_written = 1

        data.write(b"\xb4\xe2s\x1a")  # 0x1a73e2b4
        data.write(b"\x10\x00")  # size
        data.write(self.scan_file.bytes_le)

        if self.unk_bool != default_override.get("unk_bool", False):
            num_properties_written += 1
            data.write(b"9@&\x05")  # 0x5264039
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool))

        if num_properties_written != 1:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack("<H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScannableMP1Json", data)
        return cls(
            scan_file=uuid.UUID(json_data["scan_file"]),
            unk_bool=json_data["unk_bool"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan_file": str(self.scan_file),
            "unk_bool": self.unk_bool,
        }


def _decode_scan_file(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1A73E2B4: ("scan_file", _decode_scan_file),
    0x05264039: ("unk_bool", structs.decode_LITTLE_bool_),
}
