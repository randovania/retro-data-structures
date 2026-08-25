# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct7Json(typing_extensions.TypedDict):
        unknown_0x174a5ec9: float
        unknown_0x87c20643: float
        cutting_beams_chance: float
        ground_spin_chance: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x174A5EC9, 0x87C20643, 0xC0271DC6, 0x2F4C641F)


@dataclasses.dataclass()
class UnknownStruct7(BaseProperty):
    unknown_0x174a5ec9: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x174A5EC9, original_name="Unknown"),
        },
    )
    unknown_0x87c20643: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x87C20643, original_name="Unknown"),
        },
    )
    cutting_beams_chance: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC0271DC6, original_name="CuttingBeamsChance"),
        },
    )
    ground_spin_chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2F4C641F, original_name="GroundSpinChance"),
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
        if property_count != 4:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(40))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\x17J^\xc9")  # 0x174a5ec9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x174a5ec9))

        data.write(b"\x87\xc2\x06C")  # 0x87c20643
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x87c20643))

        data.write(b"\xc0'\x1d\xc6")  # 0xc0271dc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cutting_beams_chance))

        data.write(b"/Ld\x1f")  # 0x2f4c641f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ground_spin_chance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct7Json", data)
        return cls(
            unknown_0x174a5ec9=json_data["unknown_0x174a5ec9"],
            unknown_0x87c20643=json_data["unknown_0x87c20643"],
            cutting_beams_chance=json_data["cutting_beams_chance"],
            ground_spin_chance=json_data["ground_spin_chance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x174a5ec9": self.unknown_0x174a5ec9,
            "unknown_0x87c20643": self.unknown_0x87c20643,
            "cutting_beams_chance": self.cutting_beams_chance,
            "ground_spin_chance": self.ground_spin_chance,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x174A5EC9: ("unknown_0x174a5ec9", structs.decode_BIG_f),
    0x87C20643: ("unknown_0x87c20643", structs.decode_BIG_f),
    0xC0271DC6: ("cutting_beams_chance", structs.decode_BIG_f),
    0x2F4C641F: ("ground_spin_chance", structs.decode_BIG_f),
}
