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

    class TweakPlayer_ScanVisorJson(typing_extensions.TypedDict):
        scan_distance: float
        scan_retention: bool
        scan_freezes_game: bool
        scan_line_of_sight: bool
        scan_max_target_distance: float
        scan_max_lock_distance: float
        scan_camera_speed: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xB0A32E5B, 0x2A75F2B8, 0x58284BB, 0x1E54F5AE, 0xADFA90FC, 0xF4DB84A9, 0x8A7B245F)


@dataclasses.dataclass()
class TweakPlayer_ScanVisor(BaseProperty):
    scan_distance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB0A32E5B, original_name="ScanDistance"),
        },
    )
    scan_retention: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2A75F2B8, original_name="ScanRetention"),
        },
    )
    scan_freezes_game: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x058284BB, original_name="ScanFreezesGame"),
        },
    )
    scan_line_of_sight: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1E54F5AE, original_name="ScanLineOfSight"),
        },
    )
    scan_max_target_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xADFA90FC, original_name="ScanMaxTargetDistance"),
        },
    )
    scan_max_lock_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4DB84A9, original_name="ScanMaxLockDistance"),
        },
    )
    scan_camera_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A7B245F, original_name="ScanCameraSpeed"),
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
        if property_count != 7:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLH?LH?LH?LHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(61))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xb0\xa3.[")  # 0xb0a32e5b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_distance))

        data.write(b"*u\xf2\xb8")  # 0x2a75f2b8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scan_retention))

        data.write(b"\x05\x82\x84\xbb")  # 0x58284bb
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scan_freezes_game))

        data.write(b"\x1eT\xf5\xae")  # 0x1e54f5ae
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scan_line_of_sight))

        data.write(b"\xad\xfa\x90\xfc")  # 0xadfa90fc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_max_target_distance))

        data.write(b"\xf4\xdb\x84\xa9")  # 0xf4db84a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_max_lock_distance))

        data.write(b"\x8a{$_")  # 0x8a7b245f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_camera_speed))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_ScanVisorJson", data)
        return cls(
            scan_distance=json_data["scan_distance"],
            scan_retention=json_data["scan_retention"],
            scan_freezes_game=json_data["scan_freezes_game"],
            scan_line_of_sight=json_data["scan_line_of_sight"],
            scan_max_target_distance=json_data["scan_max_target_distance"],
            scan_max_lock_distance=json_data["scan_max_lock_distance"],
            scan_camera_speed=json_data["scan_camera_speed"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan_distance": self.scan_distance,
            "scan_retention": self.scan_retention,
            "scan_freezes_game": self.scan_freezes_game,
            "scan_line_of_sight": self.scan_line_of_sight,
            "scan_max_target_distance": self.scan_max_target_distance,
            "scan_max_lock_distance": self.scan_max_lock_distance,
            "scan_camera_speed": self.scan_camera_speed,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB0A32E5B: ("scan_distance", structs.decode_BIG_f),
    0x2A75F2B8: ("scan_retention", structs.decode_BIG_bool_),
    0x058284BB: ("scan_freezes_game", structs.decode_BIG_bool_),
    0x1E54F5AE: ("scan_line_of_sight", structs.decode_BIG_bool_),
    0xADFA90FC: ("scan_max_target_distance", structs.decode_BIG_f),
    0xF4DB84A9: ("scan_max_lock_distance", structs.decode_BIG_f),
    0x8A7B245F: ("scan_camera_speed", structs.decode_BIG_f),
}
