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

    class TweakPlayer_GrappleBeamJson(typing_extensions.TypedDict):
        travel_speed: float
        x_wave_amplitude: float
        z_wave_amplitude: float
        angle_phase_delta: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x14849367, 0x6C6E6F3C, 0x88AA6E41, 0x2AAB8DDA)


@dataclasses.dataclass()
class TweakPlayer_GrappleBeam(BaseProperty):
    travel_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14849367, original_name="Travel_Speed"),
        },
    )
    x_wave_amplitude: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C6E6F3C, original_name="X_Wave_Amplitude"),
        },
    )
    z_wave_amplitude: float = dataclasses.field(
        default=0.125,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88AA6E41, original_name="Z_Wave_Amplitude"),
        },
    )
    angle_phase_delta: float = dataclasses.field(
        default=0.875,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2AAB8DDA, original_name="Angle_Phase_Delta"),
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

        data.write(b"\x14\x84\x93g")  # 0x14849367
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.travel_speed))

        data.write(b"lno<")  # 0x6c6e6f3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.x_wave_amplitude))

        data.write(b"\x88\xaanA")  # 0x88aa6e41
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.z_wave_amplitude))

        data.write(b"*\xab\x8d\xda")  # 0x2aab8dda
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.angle_phase_delta))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_GrappleBeamJson", data)
        return cls(
            travel_speed=json_data["travel_speed"],
            x_wave_amplitude=json_data["x_wave_amplitude"],
            z_wave_amplitude=json_data["z_wave_amplitude"],
            angle_phase_delta=json_data["angle_phase_delta"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "travel_speed": self.travel_speed,
            "x_wave_amplitude": self.x_wave_amplitude,
            "z_wave_amplitude": self.z_wave_amplitude,
            "angle_phase_delta": self.angle_phase_delta,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x14849367: ("travel_speed", structs.decode_BIG_f),
    0x6C6E6F3C: ("x_wave_amplitude", structs.decode_BIG_f),
    0x88AA6E41: ("z_wave_amplitude", structs.decode_BIG_f),
    0x2AAB8DDA: ("angle_phase_delta", structs.decode_BIG_f),
}
