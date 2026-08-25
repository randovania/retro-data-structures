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

    class TweakPlayer_MiscJson(typing_extensions.TypedDict):
        eye_offset: float
        normal_turn_factor: float
        free_look_turn_factor: float
        free_look_max_x: float
        free_look_max_z: float
        free_look_speed: float
        free_look_snap_speed: float
        free_look_fade_angle: float
        free_look_min_angle: float
        free_look_centered_time: float
        free_look_dampen_factor: float
        null_analog_scales: bool
        unknown: float
        left_analog_max: float
        right_analog_max: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xB49B008E,
    0xB0291470,
    0x287892AB,
    0x79F8EF93,
    0x34304E98,
    0xBA27556F,
    0xD7D7828E,
    0xE0C431E,
    0x2C1DA0EC,
    0xE11788E4,
    0xC982754E,
    0xFB5C81A9,
    0xFB909BC3,
    0xF1F038DE,
    0x2B1F5094,
)


@dataclasses.dataclass()
class TweakPlayer_Misc(BaseProperty):
    eye_offset: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB49B008E, original_name="EyeOffset"),
        },
    )
    normal_turn_factor: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB0291470, original_name="NormalTurnFactor"),
        },
    )
    free_look_turn_factor: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x287892AB, original_name="FreeLookTurnFactor"),
        },
    )
    free_look_max_x: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x79F8EF93, original_name="FreeLookMaxX"),
        },
    )
    free_look_max_z: float = dataclasses.field(
        default=70.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x34304E98, original_name="FreeLookMaxZ"),
        },
    )
    free_look_speed: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA27556F, original_name="FreeLookSpeed"),
        },
    )
    free_look_snap_speed: float = dataclasses.field(
        default=200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7D7828E, original_name="FreeLookSnapSpeed"),
        },
    )
    free_look_fade_angle: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0E0C431E, original_name="FreeLookFadeAngle"),
        },
    )
    free_look_min_angle: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C1DA0EC, original_name="FreeLookMinAngle"),
        },
    )
    free_look_centered_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE11788E4, original_name="FreeLookCenteredTime"),
        },
    )
    free_look_dampen_factor: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC982754E, original_name="FreeLookDampenFactor"),
        },
    )
    null_analog_scales: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFB5C81A9, original_name="NullAnalogScales?"),
        },
    )
    unknown: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB909BC3, original_name="Unknown"),
        },
    )
    left_analog_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1F038DE, original_name="LeftAnalogMax"),
        },
    )
    right_analog_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B1F5094, original_name="RightAnalogMax"),
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
        if property_count != 15:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?LHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(147))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\xb4\x9b\x00\x8e")  # 0xb49b008e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.eye_offset))

        data.write(b"\xb0)\x14p")  # 0xb0291470
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.normal_turn_factor))

        data.write(b"(x\x92\xab")  # 0x287892ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_turn_factor))

        data.write(b"y\xf8\xef\x93")  # 0x79f8ef93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_max_x))

        data.write(b"40N\x98")  # 0x34304e98
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_max_z))

        data.write(b"\xba'Uo")  # 0xba27556f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_speed))

        data.write(b"\xd7\xd7\x82\x8e")  # 0xd7d7828e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_snap_speed))

        data.write(b"\x0e\x0cC\x1e")  # 0xe0c431e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_fade_angle))

        data.write(b",\x1d\xa0\xec")  # 0x2c1da0ec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_min_angle))

        data.write(b"\xe1\x17\x88\xe4")  # 0xe11788e4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_centered_time))

        data.write(b"\xc9\x82uN")  # 0xc982754e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.free_look_dampen_factor))

        data.write(b"\xfb\\\x81\xa9")  # 0xfb5c81a9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.null_analog_scales))

        data.write(b"\xfb\x90\x9b\xc3")  # 0xfb909bc3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xf1\xf08\xde")  # 0xf1f038de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.left_analog_max))

        data.write(b"+\x1fP\x94")  # 0x2b1f5094
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.right_analog_max))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_MiscJson", data)
        return cls(
            eye_offset=json_data["eye_offset"],
            normal_turn_factor=json_data["normal_turn_factor"],
            free_look_turn_factor=json_data["free_look_turn_factor"],
            free_look_max_x=json_data["free_look_max_x"],
            free_look_max_z=json_data["free_look_max_z"],
            free_look_speed=json_data["free_look_speed"],
            free_look_snap_speed=json_data["free_look_snap_speed"],
            free_look_fade_angle=json_data["free_look_fade_angle"],
            free_look_min_angle=json_data["free_look_min_angle"],
            free_look_centered_time=json_data["free_look_centered_time"],
            free_look_dampen_factor=json_data["free_look_dampen_factor"],
            null_analog_scales=json_data["null_analog_scales"],
            unknown=json_data["unknown"],
            left_analog_max=json_data["left_analog_max"],
            right_analog_max=json_data["right_analog_max"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "eye_offset": self.eye_offset,
            "normal_turn_factor": self.normal_turn_factor,
            "free_look_turn_factor": self.free_look_turn_factor,
            "free_look_max_x": self.free_look_max_x,
            "free_look_max_z": self.free_look_max_z,
            "free_look_speed": self.free_look_speed,
            "free_look_snap_speed": self.free_look_snap_speed,
            "free_look_fade_angle": self.free_look_fade_angle,
            "free_look_min_angle": self.free_look_min_angle,
            "free_look_centered_time": self.free_look_centered_time,
            "free_look_dampen_factor": self.free_look_dampen_factor,
            "null_analog_scales": self.null_analog_scales,
            "unknown": self.unknown,
            "left_analog_max": self.left_analog_max,
            "right_analog_max": self.right_analog_max,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB49B008E: ("eye_offset", structs.decode_BIG_f),
    0xB0291470: ("normal_turn_factor", structs.decode_BIG_f),
    0x287892AB: ("free_look_turn_factor", structs.decode_BIG_f),
    0x79F8EF93: ("free_look_max_x", structs.decode_BIG_f),
    0x34304E98: ("free_look_max_z", structs.decode_BIG_f),
    0xBA27556F: ("free_look_speed", structs.decode_BIG_f),
    0xD7D7828E: ("free_look_snap_speed", structs.decode_BIG_f),
    0x0E0C431E: ("free_look_fade_angle", structs.decode_BIG_f),
    0x2C1DA0EC: ("free_look_min_angle", structs.decode_BIG_f),
    0xE11788E4: ("free_look_centered_time", structs.decode_BIG_f),
    0xC982754E: ("free_look_dampen_factor", structs.decode_BIG_f),
    0xFB5C81A9: ("null_analog_scales", structs.decode_BIG_bool_),
    0xFB909BC3: ("unknown", structs.decode_BIG_f),
    0xF1F038DE: ("left_analog_max", structs.decode_BIG_f),
    0x2B1F5094: ("right_analog_max", structs.decode_BIG_f),
}
