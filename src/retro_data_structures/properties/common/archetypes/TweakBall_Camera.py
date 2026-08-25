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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakBall_CameraJson(typing_extensions.TypedDict):
        ball_camera_angle_per_second: float
        ball_camera_offset: json_util.JsonValue
        ball_camera_min_speed_distance: float
        ball_camera_max_speed_distance: float
        ball_camera_backwards_distance: float
        ball_camera_elevation: float
        ball_camera_spring_constant: float
        ball_camera_spring_max: float
        ball_camera_spring_tardis: float
        ball_camera_centroid_spring_constant: float
        ball_camera_centroid_spring_max: float
        ball_camera_centroid_spring_tardis: float
        ball_camera_centroid_distance_spring_constant: float
        ball_camera_centroid_distance_spring_max: float
        ball_camera_centroid_distance_spring_tardis: float
        ball_camera_look_at_spring_constant: float
        ball_camera_look_at_spring_max: float
        ball_camera_look_at_spring_tardis: float
        ball_camera_transition_time: float
        ball_camera_free_look_speed: float
        ball_camera_free_look_zoom_speed: float
        ball_camera_free_look_min_distance: float
        ball_camera_free_look_max_distance: float
        ball_camera_free_look_max_vert_angle: float
        unknown_0x144db504: float
        unknown_0xee5bea64: float
        ball_camera_chase_distance: float
        ball_camera_chase_elevation: float
        ball_camera_chase_yaw_speed: float
        ball_camera_chase_dampen_angle: float
        ball_camera_chase_angle_per_second: float
        ball_camera_chase_look_at_offset: json_util.JsonValue
        ball_camera_chase_spring_constant: float
        ball_camera_chase_spring_max: float
        ball_camera_chase_spring_tardis: float
        ball_camera_boost_distance: float
        ball_camera_boost_elevation: float
        ball_camera_boost_yaw_speed: float
        ball_camera_boost_dampen_angle: float
        ball_camera_boost_angle_per_second: float
        ball_camera_boost_look_at_offset: json_util.JsonValue
        ball_camera_boost_spring_constant: float
        ball_camera_boost_spring_max: float
        ball_camera_boost_spring_tardis: float
        ball_camera_control_distance: float
        ball_camera_look_at_min_height: float
        unknown_0x50f77df0: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x8AE409FC,
    0xC7BF307C,
    0xF88297B3,
    0xEBC77118,
    0xF52074C,
    0x31FF1A31,
    0xC54A2A64,
    0x587695FA,
    0x6617065C,
    0xDA3010AF,
    0xD2E267A2,
    0xD550ADBC,
    0xFA4AE412,
    0xD0EFEDBF,
    0x7E7391E1,
    0x6AB01E0B,
    0xF9FD14B7,
    0x46A7EBCC,
    0x6EFA8159,
    0xAE74C22F,
    0xC040D23B,
    0x16A35615,
    0x475AED48,
    0x14DE6D39,
    0x144DB504,
    0xEE5BEA64,
    0xF20BA524,
    0xD5D38CBC,
    0x5429D2AE,
    0x31BD251E,
    0x50FC4ACB,
    0xA8A86DE9,
    0x1F526953,
    0xBC5A0377,
    0x9A39CF14,
    0xE6F4443F,
    0x5FA2BAB1,
    0x40D633B5,
    0x4BA944BB,
    0xE9735BA1,
    0x416D0E9F,
    0xA6DD7839,
    0x362B357A,
    0x3CFF8C12,
    0xEE4C1F4B,
    0x9388FA50,
    0x50F77DF0,
)


@dataclasses.dataclass()
class TweakBall_Camera(BaseProperty):
    ball_camera_angle_per_second: float = dataclasses.field(
        default=1200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8AE409FC, original_name="BallCameraAnglePerSecond"),
        },
    )
    ball_camera_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xC7BF307C,
                original_name="BallCameraOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    ball_camera_min_speed_distance: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF88297B3, original_name="BallCameraMinSpeedDistance"),
        },
    )
    ball_camera_max_speed_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEBC77118, original_name="BallCameraMaxSpeedDistance"),
        },
    )
    ball_camera_backwards_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0F52074C, original_name="BallCameraBackwardsDistance"),
        },
    )
    ball_camera_elevation: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x31FF1A31, original_name="BallCameraElevation"),
        },
    )
    ball_camera_spring_constant: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC54A2A64, original_name="BallCameraSpringConstant"),
        },
    )
    ball_camera_spring_max: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0x587695FA, original_name="BallCameraSpringMax"),
        },
    )
    ball_camera_spring_tardis: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6617065C, original_name="BallCameraSpringTardis"),
        },
    )
    ball_camera_centroid_spring_constant: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0xDA3010AF, original_name="BallCameraCentroidSpringConstant"
            ),
        },
    )
    ball_camera_centroid_spring_max: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD2E267A2, original_name="BallCameraCentroidSpringMax"),
        },
    )
    ball_camera_centroid_spring_tardis: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD550ADBC, original_name="BallCameraCentroidSpringTardis"),
        },
    )
    ball_camera_centroid_distance_spring_constant: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0xFA4AE412, original_name="BallCameraCentroidDistanceSpringConstant"
            ),
        },
    )
    ball_camera_centroid_distance_spring_max: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0xD0EFEDBF, original_name="BallCameraCentroidDistanceSpringMax"
            ),
        },
    )
    ball_camera_centroid_distance_spring_tardis: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0x7E7391E1, original_name="BallCameraCentroidDistanceSpringTardis"
            ),
        },
    )
    ball_camera_look_at_spring_constant: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6AB01E0B, original_name="BallCameraLookAtSpringConstant"),
        },
    )
    ball_camera_look_at_spring_max: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF9FD14B7, original_name="BallCameraLookAtSpringMax"),
        },
    )
    ball_camera_look_at_spring_tardis: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x46A7EBCC, original_name="BallCameraLookAtSpringTardis"),
        },
    )
    ball_camera_transition_time: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6EFA8159, original_name="BallCameraTransitionTime"),
        },
    )
    ball_camera_free_look_speed: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAE74C22F, original_name="BallCameraFreeLookSpeed"),
        },
    )
    ball_camera_free_look_zoom_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC040D23B, original_name="BallCameraFreeLookZoomSpeed"),
        },
    )
    ball_camera_free_look_min_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16A35615, original_name="BallCameraFreeLookMinDistance"),
        },
    )
    ball_camera_free_look_max_distance: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x475AED48, original_name="BallCameraFreeLookMaxDistance"),
        },
    )
    ball_camera_free_look_max_vert_angle: float = dataclasses.field(
        default=89.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14DE6D39, original_name="BallCameraFreeLookMaxVertAngle"),
        },
    )
    unknown_0x144db504: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x144DB504, original_name="Unknown"),
        },
    )
    unknown_0xee5bea64: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE5BEA64, original_name="Unknown"),
        },
    )
    ball_camera_chase_distance: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF20BA524, original_name="BallCameraChaseDistance"),
        },
    )
    ball_camera_chase_elevation: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5D38CBC, original_name="BallCameraChaseElevation"),
        },
    )
    ball_camera_chase_yaw_speed: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5429D2AE, original_name="BallCameraChaseYawSpeed"),
        },
    )
    ball_camera_chase_dampen_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x31BD251E, original_name="BallCameraChaseDampenAngle"),
        },
    )
    ball_camera_chase_angle_per_second: float = dataclasses.field(
        default=1200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50FC4ACB, original_name="BallCameraChaseAnglePerSecond"),
        },
    )
    ball_camera_chase_look_at_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xA8A86DE9,
                original_name="BallCameraChaseLookAtOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    ball_camera_chase_spring_constant: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1F526953, original_name="BallCameraChaseSpringConstant"),
        },
    )
    ball_camera_chase_spring_max: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC5A0377, original_name="BallCameraChaseSpringMax"),
        },
    )
    ball_camera_chase_spring_tardis: float = dataclasses.field(
        default=5.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9A39CF14, original_name="BallCameraChaseSpringTardis"),
        },
    )
    ball_camera_boost_distance: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE6F4443F, original_name="BallCameraBoostDistance"),
        },
    )
    ball_camera_boost_elevation: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5FA2BAB1, original_name="BallCameraBoostElevation"),
        },
    )
    ball_camera_boost_yaw_speed: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x40D633B5, original_name="BallCameraBoostYawSpeed"),
        },
    )
    ball_camera_boost_dampen_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4BA944BB, original_name="BallCameraBoostDampenAngle"),
        },
    )
    ball_camera_boost_angle_per_second: float = dataclasses.field(
        default=2400.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9735BA1, original_name="BallCameraBoostAnglePerSecond"),
        },
    )
    ball_camera_boost_look_at_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x416D0E9F,
                original_name="BallCameraBoostLookAtOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    ball_camera_boost_spring_constant: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA6DD7839, original_name="BallCameraBoostSpringConstant"),
        },
    )
    ball_camera_boost_spring_max: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x362B357A, original_name="BallCameraBoostSpringMax"),
        },
    )
    ball_camera_boost_spring_tardis: float = dataclasses.field(
        default=5.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3CFF8C12, original_name="BallCameraBoostSpringTardis"),
        },
    )
    ball_camera_control_distance: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE4C1F4B, original_name="BallCameraControlDistance"),
        },
    )
    ball_camera_look_at_min_height: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9388FA50, original_name="BallCameraLookAtMinHeight"),
        },
    )
    unknown_0x50f77df0: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50F77DF0, original_name="Unknown"),
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
        if property_count != 47:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHfLHfffLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfffLHfLHfLHfLHfLHfLHfLHfLHfLHfffLHfLHfLHfLHfLHfLHf"
            )

        dec = _FAST_FORMAT.unpack(data.read(494))
        assert (
            dec[0],
            dec[3],
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
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
            dec[65],
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            dec[86],
            dec[89],
            dec[92],
            dec[95],
            dec[100],
            dec[103],
            dec[106],
            dec[109],
            dec[112],
            dec[115],
            dec[118],
            dec[121],
            dec[124],
            dec[129],
            dec[132],
            dec[135],
            dec[138],
            dec[141],
            dec[144],
        ) == _FAST_IDS
        return cls(
            dec[2],
            Vector(*dec[5:8]),
            dec[10],
            dec[13],
            dec[16],
            dec[19],
            dec[22],
            dec[25],
            dec[28],
            dec[31],
            dec[34],
            dec[37],
            dec[40],
            dec[43],
            dec[46],
            dec[49],
            dec[52],
            dec[55],
            dec[58],
            dec[61],
            dec[64],
            dec[67],
            dec[70],
            dec[73],
            dec[76],
            dec[79],
            dec[82],
            dec[85],
            dec[88],
            dec[91],
            dec[94],
            Vector(*dec[97:100]),
            dec[102],
            dec[105],
            dec[108],
            dec[111],
            dec[114],
            dec[117],
            dec[120],
            dec[123],
            Vector(*dec[126:129]),
            dec[131],
            dec[134],
            dec[137],
            dec[140],
            dec[143],
            dec[146],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00/")  # 47 properties

        data.write(b"\x8a\xe4\t\xfc")  # 0x8ae409fc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_angle_per_second))

        data.write(b"\xc7\xbf0|")  # 0xc7bf307c
        data.write(b"\x00\x0c")  # size
        self.ball_camera_offset.to_stream(data, game)

        data.write(b"\xf8\x82\x97\xb3")  # 0xf88297b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_min_speed_distance))

        data.write(b"\xeb\xc7q\x18")  # 0xebc77118
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_max_speed_distance))

        data.write(b"\x0fR\x07L")  # 0xf52074c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_backwards_distance))

        data.write(b"1\xff\x1a1")  # 0x31ff1a31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_elevation))

        data.write(b"\xc5J*d")  # 0xc54a2a64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_spring_constant))

        data.write(b"Xv\x95\xfa")  # 0x587695fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_spring_max))

        data.write(b"f\x17\x06\\")  # 0x6617065c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_spring_tardis))

        data.write(b"\xda0\x10\xaf")  # 0xda3010af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_centroid_spring_constant))

        data.write(b"\xd2\xe2g\xa2")  # 0xd2e267a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_centroid_spring_max))

        data.write(b"\xd5P\xad\xbc")  # 0xd550adbc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_centroid_spring_tardis))

        data.write(b"\xfaJ\xe4\x12")  # 0xfa4ae412
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_centroid_distance_spring_constant))

        data.write(b"\xd0\xef\xed\xbf")  # 0xd0efedbf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_centroid_distance_spring_max))

        data.write(b"~s\x91\xe1")  # 0x7e7391e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_centroid_distance_spring_tardis))

        data.write(b"j\xb0\x1e\x0b")  # 0x6ab01e0b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_look_at_spring_constant))

        data.write(b"\xf9\xfd\x14\xb7")  # 0xf9fd14b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_look_at_spring_max))

        data.write(b"F\xa7\xeb\xcc")  # 0x46a7ebcc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_look_at_spring_tardis))

        data.write(b"n\xfa\x81Y")  # 0x6efa8159
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_transition_time))

        data.write(b"\xaet\xc2/")  # 0xae74c22f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_free_look_speed))

        data.write(b"\xc0@\xd2;")  # 0xc040d23b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_free_look_zoom_speed))

        data.write(b"\x16\xa3V\x15")  # 0x16a35615
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_free_look_min_distance))

        data.write(b"GZ\xedH")  # 0x475aed48
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_free_look_max_distance))

        data.write(b"\x14\xdem9")  # 0x14de6d39
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_free_look_max_vert_angle))

        data.write(b"\x14M\xb5\x04")  # 0x144db504
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x144db504))

        data.write(b"\xee[\xead")  # 0xee5bea64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xee5bea64))

        data.write(b"\xf2\x0b\xa5$")  # 0xf20ba524
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_distance))

        data.write(b"\xd5\xd3\x8c\xbc")  # 0xd5d38cbc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_elevation))

        data.write(b"T)\xd2\xae")  # 0x5429d2ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_yaw_speed))

        data.write(b"1\xbd%\x1e")  # 0x31bd251e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_dampen_angle))

        data.write(b"P\xfcJ\xcb")  # 0x50fc4acb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_angle_per_second))

        data.write(b"\xa8\xa8m\xe9")  # 0xa8a86de9
        data.write(b"\x00\x0c")  # size
        self.ball_camera_chase_look_at_offset.to_stream(data, game)

        data.write(b"\x1fRiS")  # 0x1f526953
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_spring_constant))

        data.write(b"\xbcZ\x03w")  # 0xbc5a0377
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_spring_max))

        data.write(b"\x9a9\xcf\x14")  # 0x9a39cf14
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_chase_spring_tardis))

        data.write(b"\xe6\xf4D?")  # 0xe6f4443f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_distance))

        data.write(b"_\xa2\xba\xb1")  # 0x5fa2bab1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_elevation))

        data.write(b"@\xd63\xb5")  # 0x40d633b5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_yaw_speed))

        data.write(b"K\xa9D\xbb")  # 0x4ba944bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_dampen_angle))

        data.write(b"\xe9s[\xa1")  # 0xe9735ba1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_angle_per_second))

        data.write(b"Am\x0e\x9f")  # 0x416d0e9f
        data.write(b"\x00\x0c")  # size
        self.ball_camera_boost_look_at_offset.to_stream(data, game)

        data.write(b"\xa6\xddx9")  # 0xa6dd7839
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_spring_constant))

        data.write(b"6+5z")  # 0x362b357a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_spring_max))

        data.write(b"<\xff\x8c\x12")  # 0x3cff8c12
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_boost_spring_tardis))

        data.write(b"\xeeL\x1fK")  # 0xee4c1f4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_control_distance))

        data.write(b"\x93\x88\xfaP")  # 0x9388fa50
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_camera_look_at_min_height))

        data.write(b"P\xf7}\xf0")  # 0x50f77df0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x50f77df0))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakBall_CameraJson", data)
        return cls(
            ball_camera_angle_per_second=json_data["ball_camera_angle_per_second"],
            ball_camera_offset=Vector.from_json(json_data["ball_camera_offset"]),
            ball_camera_min_speed_distance=json_data["ball_camera_min_speed_distance"],
            ball_camera_max_speed_distance=json_data["ball_camera_max_speed_distance"],
            ball_camera_backwards_distance=json_data["ball_camera_backwards_distance"],
            ball_camera_elevation=json_data["ball_camera_elevation"],
            ball_camera_spring_constant=json_data["ball_camera_spring_constant"],
            ball_camera_spring_max=json_data["ball_camera_spring_max"],
            ball_camera_spring_tardis=json_data["ball_camera_spring_tardis"],
            ball_camera_centroid_spring_constant=json_data["ball_camera_centroid_spring_constant"],
            ball_camera_centroid_spring_max=json_data["ball_camera_centroid_spring_max"],
            ball_camera_centroid_spring_tardis=json_data["ball_camera_centroid_spring_tardis"],
            ball_camera_centroid_distance_spring_constant=json_data["ball_camera_centroid_distance_spring_constant"],
            ball_camera_centroid_distance_spring_max=json_data["ball_camera_centroid_distance_spring_max"],
            ball_camera_centroid_distance_spring_tardis=json_data["ball_camera_centroid_distance_spring_tardis"],
            ball_camera_look_at_spring_constant=json_data["ball_camera_look_at_spring_constant"],
            ball_camera_look_at_spring_max=json_data["ball_camera_look_at_spring_max"],
            ball_camera_look_at_spring_tardis=json_data["ball_camera_look_at_spring_tardis"],
            ball_camera_transition_time=json_data["ball_camera_transition_time"],
            ball_camera_free_look_speed=json_data["ball_camera_free_look_speed"],
            ball_camera_free_look_zoom_speed=json_data["ball_camera_free_look_zoom_speed"],
            ball_camera_free_look_min_distance=json_data["ball_camera_free_look_min_distance"],
            ball_camera_free_look_max_distance=json_data["ball_camera_free_look_max_distance"],
            ball_camera_free_look_max_vert_angle=json_data["ball_camera_free_look_max_vert_angle"],
            unknown_0x144db504=json_data["unknown_0x144db504"],
            unknown_0xee5bea64=json_data["unknown_0xee5bea64"],
            ball_camera_chase_distance=json_data["ball_camera_chase_distance"],
            ball_camera_chase_elevation=json_data["ball_camera_chase_elevation"],
            ball_camera_chase_yaw_speed=json_data["ball_camera_chase_yaw_speed"],
            ball_camera_chase_dampen_angle=json_data["ball_camera_chase_dampen_angle"],
            ball_camera_chase_angle_per_second=json_data["ball_camera_chase_angle_per_second"],
            ball_camera_chase_look_at_offset=Vector.from_json(json_data["ball_camera_chase_look_at_offset"]),
            ball_camera_chase_spring_constant=json_data["ball_camera_chase_spring_constant"],
            ball_camera_chase_spring_max=json_data["ball_camera_chase_spring_max"],
            ball_camera_chase_spring_tardis=json_data["ball_camera_chase_spring_tardis"],
            ball_camera_boost_distance=json_data["ball_camera_boost_distance"],
            ball_camera_boost_elevation=json_data["ball_camera_boost_elevation"],
            ball_camera_boost_yaw_speed=json_data["ball_camera_boost_yaw_speed"],
            ball_camera_boost_dampen_angle=json_data["ball_camera_boost_dampen_angle"],
            ball_camera_boost_angle_per_second=json_data["ball_camera_boost_angle_per_second"],
            ball_camera_boost_look_at_offset=Vector.from_json(json_data["ball_camera_boost_look_at_offset"]),
            ball_camera_boost_spring_constant=json_data["ball_camera_boost_spring_constant"],
            ball_camera_boost_spring_max=json_data["ball_camera_boost_spring_max"],
            ball_camera_boost_spring_tardis=json_data["ball_camera_boost_spring_tardis"],
            ball_camera_control_distance=json_data["ball_camera_control_distance"],
            ball_camera_look_at_min_height=json_data["ball_camera_look_at_min_height"],
            unknown_0x50f77df0=json_data["unknown_0x50f77df0"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "ball_camera_angle_per_second": self.ball_camera_angle_per_second,
            "ball_camera_offset": self.ball_camera_offset.to_json(),
            "ball_camera_min_speed_distance": self.ball_camera_min_speed_distance,
            "ball_camera_max_speed_distance": self.ball_camera_max_speed_distance,
            "ball_camera_backwards_distance": self.ball_camera_backwards_distance,
            "ball_camera_elevation": self.ball_camera_elevation,
            "ball_camera_spring_constant": self.ball_camera_spring_constant,
            "ball_camera_spring_max": self.ball_camera_spring_max,
            "ball_camera_spring_tardis": self.ball_camera_spring_tardis,
            "ball_camera_centroid_spring_constant": self.ball_camera_centroid_spring_constant,
            "ball_camera_centroid_spring_max": self.ball_camera_centroid_spring_max,
            "ball_camera_centroid_spring_tardis": self.ball_camera_centroid_spring_tardis,
            "ball_camera_centroid_distance_spring_constant": self.ball_camera_centroid_distance_spring_constant,
            "ball_camera_centroid_distance_spring_max": self.ball_camera_centroid_distance_spring_max,
            "ball_camera_centroid_distance_spring_tardis": self.ball_camera_centroid_distance_spring_tardis,
            "ball_camera_look_at_spring_constant": self.ball_camera_look_at_spring_constant,
            "ball_camera_look_at_spring_max": self.ball_camera_look_at_spring_max,
            "ball_camera_look_at_spring_tardis": self.ball_camera_look_at_spring_tardis,
            "ball_camera_transition_time": self.ball_camera_transition_time,
            "ball_camera_free_look_speed": self.ball_camera_free_look_speed,
            "ball_camera_free_look_zoom_speed": self.ball_camera_free_look_zoom_speed,
            "ball_camera_free_look_min_distance": self.ball_camera_free_look_min_distance,
            "ball_camera_free_look_max_distance": self.ball_camera_free_look_max_distance,
            "ball_camera_free_look_max_vert_angle": self.ball_camera_free_look_max_vert_angle,
            "unknown_0x144db504": self.unknown_0x144db504,
            "unknown_0xee5bea64": self.unknown_0xee5bea64,
            "ball_camera_chase_distance": self.ball_camera_chase_distance,
            "ball_camera_chase_elevation": self.ball_camera_chase_elevation,
            "ball_camera_chase_yaw_speed": self.ball_camera_chase_yaw_speed,
            "ball_camera_chase_dampen_angle": self.ball_camera_chase_dampen_angle,
            "ball_camera_chase_angle_per_second": self.ball_camera_chase_angle_per_second,
            "ball_camera_chase_look_at_offset": self.ball_camera_chase_look_at_offset.to_json(),
            "ball_camera_chase_spring_constant": self.ball_camera_chase_spring_constant,
            "ball_camera_chase_spring_max": self.ball_camera_chase_spring_max,
            "ball_camera_chase_spring_tardis": self.ball_camera_chase_spring_tardis,
            "ball_camera_boost_distance": self.ball_camera_boost_distance,
            "ball_camera_boost_elevation": self.ball_camera_boost_elevation,
            "ball_camera_boost_yaw_speed": self.ball_camera_boost_yaw_speed,
            "ball_camera_boost_dampen_angle": self.ball_camera_boost_dampen_angle,
            "ball_camera_boost_angle_per_second": self.ball_camera_boost_angle_per_second,
            "ball_camera_boost_look_at_offset": self.ball_camera_boost_look_at_offset.to_json(),
            "ball_camera_boost_spring_constant": self.ball_camera_boost_spring_constant,
            "ball_camera_boost_spring_max": self.ball_camera_boost_spring_max,
            "ball_camera_boost_spring_tardis": self.ball_camera_boost_spring_tardis,
            "ball_camera_control_distance": self.ball_camera_control_distance,
            "ball_camera_look_at_min_height": self.ball_camera_look_at_min_height,
            "unknown_0x50f77df0": self.unknown_0x50f77df0,
        }


def _decode_ball_camera_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_ball_camera_chase_look_at_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_ball_camera_boost_look_at_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8AE409FC: ("ball_camera_angle_per_second", structs.decode_BIG_f),
    0xC7BF307C: ("ball_camera_offset", _decode_ball_camera_offset),
    0xF88297B3: ("ball_camera_min_speed_distance", structs.decode_BIG_f),
    0xEBC77118: ("ball_camera_max_speed_distance", structs.decode_BIG_f),
    0x0F52074C: ("ball_camera_backwards_distance", structs.decode_BIG_f),
    0x31FF1A31: ("ball_camera_elevation", structs.decode_BIG_f),
    0xC54A2A64: ("ball_camera_spring_constant", structs.decode_BIG_f),
    0x587695FA: ("ball_camera_spring_max", structs.decode_BIG_f),
    0x6617065C: ("ball_camera_spring_tardis", structs.decode_BIG_f),
    0xDA3010AF: ("ball_camera_centroid_spring_constant", structs.decode_BIG_f),
    0xD2E267A2: ("ball_camera_centroid_spring_max", structs.decode_BIG_f),
    0xD550ADBC: ("ball_camera_centroid_spring_tardis", structs.decode_BIG_f),
    0xFA4AE412: ("ball_camera_centroid_distance_spring_constant", structs.decode_BIG_f),
    0xD0EFEDBF: ("ball_camera_centroid_distance_spring_max", structs.decode_BIG_f),
    0x7E7391E1: ("ball_camera_centroid_distance_spring_tardis", structs.decode_BIG_f),
    0x6AB01E0B: ("ball_camera_look_at_spring_constant", structs.decode_BIG_f),
    0xF9FD14B7: ("ball_camera_look_at_spring_max", structs.decode_BIG_f),
    0x46A7EBCC: ("ball_camera_look_at_spring_tardis", structs.decode_BIG_f),
    0x6EFA8159: ("ball_camera_transition_time", structs.decode_BIG_f),
    0xAE74C22F: ("ball_camera_free_look_speed", structs.decode_BIG_f),
    0xC040D23B: ("ball_camera_free_look_zoom_speed", structs.decode_BIG_f),
    0x16A35615: ("ball_camera_free_look_min_distance", structs.decode_BIG_f),
    0x475AED48: ("ball_camera_free_look_max_distance", structs.decode_BIG_f),
    0x14DE6D39: ("ball_camera_free_look_max_vert_angle", structs.decode_BIG_f),
    0x144DB504: ("unknown_0x144db504", structs.decode_BIG_f),
    0xEE5BEA64: ("unknown_0xee5bea64", structs.decode_BIG_f),
    0xF20BA524: ("ball_camera_chase_distance", structs.decode_BIG_f),
    0xD5D38CBC: ("ball_camera_chase_elevation", structs.decode_BIG_f),
    0x5429D2AE: ("ball_camera_chase_yaw_speed", structs.decode_BIG_f),
    0x31BD251E: ("ball_camera_chase_dampen_angle", structs.decode_BIG_f),
    0x50FC4ACB: ("ball_camera_chase_angle_per_second", structs.decode_BIG_f),
    0xA8A86DE9: ("ball_camera_chase_look_at_offset", _decode_ball_camera_chase_look_at_offset),
    0x1F526953: ("ball_camera_chase_spring_constant", structs.decode_BIG_f),
    0xBC5A0377: ("ball_camera_chase_spring_max", structs.decode_BIG_f),
    0x9A39CF14: ("ball_camera_chase_spring_tardis", structs.decode_BIG_f),
    0xE6F4443F: ("ball_camera_boost_distance", structs.decode_BIG_f),
    0x5FA2BAB1: ("ball_camera_boost_elevation", structs.decode_BIG_f),
    0x40D633B5: ("ball_camera_boost_yaw_speed", structs.decode_BIG_f),
    0x4BA944BB: ("ball_camera_boost_dampen_angle", structs.decode_BIG_f),
    0xE9735BA1: ("ball_camera_boost_angle_per_second", structs.decode_BIG_f),
    0x416D0E9F: ("ball_camera_boost_look_at_offset", _decode_ball_camera_boost_look_at_offset),
    0xA6DD7839: ("ball_camera_boost_spring_constant", structs.decode_BIG_f),
    0x362B357A: ("ball_camera_boost_spring_max", structs.decode_BIG_f),
    0x3CFF8C12: ("ball_camera_boost_spring_tardis", structs.decode_BIG_f),
    0xEE4C1F4B: ("ball_camera_control_distance", structs.decode_BIG_f),
    0x9388FA50: ("ball_camera_look_at_min_height", structs.decode_BIG_f),
    0x50F77DF0: ("unknown_0x50f77df0", structs.decode_BIG_f),
}
