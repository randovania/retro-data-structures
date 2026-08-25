# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ScannableParametersJson(typing_extensions.TypedDict):
        scannable_info0: int
        max_scannable_distance: float
        priority: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xB94E9BE7, 0xFF4AE2EC, 0x42087650)


@dataclasses.dataclass()
class ScannableParameters(BaseProperty):
    scannable_info0: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB94E9BE7, original_name="ScannableInfo0"),
        },
    )
    max_scannable_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF4AE2EC, original_name="MaxScannableDistance"),
        },
    )
    priority: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42087650, original_name="Priority"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 3:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHQLHfLHl")

        dec = _FAST_FORMAT.unpack(data.read(34))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\xb9N\x9b\xe7")  # 0xb94e9be7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scannable_info0))

        data.write(b"\xffJ\xe2\xec")  # 0xff4ae2ec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_scannable_distance))

        data.write(b"B\x08vP")  # 0x42087650
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.priority))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScannableParametersJson", data)
        return cls(
            scannable_info0=json_data["scannable_info0"],
            max_scannable_distance=json_data["max_scannable_distance"],
            priority=json_data["priority"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scannable_info0": self.scannable_info0,
            "max_scannable_distance": self.max_scannable_distance,
            "priority": self.priority,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB94E9BE7: ("scannable_info0", structs.decode_BIG_Q),
    0xFF4AE2EC: ("max_scannable_distance", structs.decode_BIG_f),
    0x42087650: ("priority", structs.decode_BIG_l),
}
