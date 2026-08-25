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

    class TweakBall_MovementJson(typing_extensions.TypedDict):
        forward_accel_normal: float
        forward_accel_air: float
        forward_accel_ice: float
        forward_accel_organic: float
        forward_accel_water: float
        forward_accel_lava: float
        forward_accel_phazon: float
        forward_accel_shrubbery: float
        movement_friction_normal: float
        movement_friction_air: float
        movement_friction_ice: float
        movement_friction_organic: float
        movement_friction_water: float
        movement_friction_lava: float
        movement_friction_phazon: float
        movement_friction_shrubbery: float
        forward_max_speed_normal: float
        forward_max_speed_air: float
        forward_max_speed_ice: float
        forward_max_speed_organic: float
        forward_max_speed_water: float
        forward_max_speed_lava: float
        forward_max_speed_phazon: float
        forward_max_speed_shrubbery: float
        unknown_0x85ee51ed: float
        unknown_0x6d7811f5: float
        ball_up_gravity: float
        ball_down_gravity: float
        ball_forward_braking_accel_normal: float
        ball_forward_braking_accel_air: float
        ball_forward_braking_accel_ice: float
        ball_forward_braking_accel_organic: float
        ball_forward_braking_accel_water: float
        ball_forward_braking_accel_lava: float
        ball_forward_braking_accel_phazon: float
        ball_forward_braking_accel_shrubbery: float
        ball_gravity: float
        ball_water_gravity: float
        unknown_0xeeb74968: float
        ball_boost_height: float
        unknown_0xe2bb0298: float
        minimum_alignment_speed: float
        tireness: float
        max_lean_angle: float
        tire_to_marble_threshold_speed: float
        marble_to_tire_threshold_speed: float
        force_to_lean_gain: float
        lean_tracking_gain: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x18D0B2DA,
    0x84F61AC5,
    0xEDB06C1D,
    0x56F9F2AF,
    0xD05B643F,
    0x122CE118,
    0xF848DABE,
    0x68AC6028,
    0xD4A25028,
    0x2B5CB136,
    0x421AC7EE,
    0x586137D,
    0xAECE038B,
    0x3637E815,
    0x343A384C,
    0xCAF4624,
    0xFFD4A030,
    0x59DFBCB9,
    0x3099CA61,
    0x16C1FDDB,
    0x6C648931,
    0x4B42F5A9,
    0x1F4CC854,
    0xB3408173,
    0x85EE51ED,
    0x6D7811F5,
    0xF80A0655,
    0x92F30F94,
    0xB06AC970,
    0xBB3C2629,
    0xD27A50F1,
    0x60520222,
    0xDFF9B92,
    0xBBAF8577,
    0x50F2A114,
    0x5B3C4299,
    0xD83E5EEC,
    0x9C905747,
    0xEEB74968,
    0xBD28AF6E,
    0xE2BB0298,
    0xE46FA96A,
    0x4ED87EBD,
    0xCA8EDEAB,
    0x96226D18,
    0x191F4F62,
    0x54C20211,
    0xB90A721E,
)


@dataclasses.dataclass()
class TweakBall_Movement(BaseProperty):
    forward_accel_normal: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x18D0B2DA, original_name="ForwardAccelNormal"),
        },
    )
    forward_accel_air: float = dataclasses.field(
        default=3000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x84F61AC5, original_name="ForwardAccelAir"),
        },
    )
    forward_accel_ice: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEDB06C1D, original_name="ForwardAccelIce"),
        },
    )
    forward_accel_organic: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x56F9F2AF, original_name="ForwardAccelOrganic"),
        },
    )
    forward_accel_water: float = dataclasses.field(
        default=8000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD05B643F, original_name="ForwardAccelWater"),
        },
    )
    forward_accel_lava: float = dataclasses.field(
        default=8000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x122CE118, original_name="ForwardAccelLava"),
        },
    )
    forward_accel_phazon: float = dataclasses.field(
        default=8000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF848DABE, original_name="ForwardAccelPhazon"),
        },
    )
    forward_accel_shrubbery: float = dataclasses.field(
        default=8000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x68AC6028, original_name="ForwardAccelShrubbery"),
        },
    )
    movement_friction_normal: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4A25028, original_name="MovementFrictionNormal"),
        },
    )
    movement_friction_air: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B5CB136, original_name="MovementFrictionAir"),
        },
    )
    movement_friction_ice: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x421AC7EE, original_name="MovementFrictionIce"),
        },
    )
    movement_friction_organic: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0586137D, original_name="MovementFrictionOrganic"),
        },
    )
    movement_friction_water: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAECE038B, original_name="MovementFrictionWater"),
        },
    )
    movement_friction_lava: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3637E815, original_name="MovementFrictionLava"),
        },
    )
    movement_friction_phazon: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x343A384C, original_name="MovementFrictionPhazon"),
        },
    )
    movement_friction_shrubbery: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0CAF4624, original_name="MovementFrictionShrubbery"),
        },
    )
    forward_max_speed_normal: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFFD4A030, original_name="ForwardMaxSpeedNormal"),
        },
    )
    forward_max_speed_air: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x59DFBCB9, original_name="ForwardMaxSpeedAir"),
        },
    )
    forward_max_speed_ice: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3099CA61, original_name="ForwardMaxSpeedIce"),
        },
    )
    forward_max_speed_organic: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16C1FDDB, original_name="ForwardMaxSpeedOrganic"),
        },
    )
    forward_max_speed_water: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C648931, original_name="ForwardMaxSpeedWater"),
        },
    )
    forward_max_speed_lava: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B42F5A9, original_name="ForwardMaxSpeedLava"),
        },
    )
    forward_max_speed_phazon: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1F4CC854, original_name="ForwardMaxSpeedPhazon"),
        },
    )
    forward_max_speed_shrubbery: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB3408173, original_name="ForwardMaxSpeedShrubbery"),
        },
    )
    unknown_0x85ee51ed: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x85EE51ED, original_name="Unknown"),
        },
    )
    unknown_0x6d7811f5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D7811F5, original_name="Unknown"),
        },
    )
    ball_up_gravity: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF80A0655, original_name="BallUpGravity"),
        },
    )
    ball_down_gravity: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x92F30F94, original_name="BallDownGravity"),
        },
    )
    ball_forward_braking_accel_normal: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB06AC970, original_name="BallForwardBrakingAccelNormal"),
        },
    )
    ball_forward_braking_accel_air: float = dataclasses.field(
        default=3000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBB3C2629, original_name="BallForwardBrakingAccelAir"),
        },
    )
    ball_forward_braking_accel_ice: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD27A50F1, original_name="BallForwardBrakingAccelIce"),
        },
    )
    ball_forward_braking_accel_organic: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x60520222, original_name="BallForwardBrakingAccelOrganic"),
        },
    )
    ball_forward_braking_accel_water: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0DFF9B92, original_name="BallForwardBrakingAccelWater"),
        },
    )
    ball_forward_braking_accel_lava: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBBAF8577, original_name="BallForwardBrakingAccelLava"),
        },
    )
    ball_forward_braking_accel_phazon: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50F2A114, original_name="BallForwardBrakingAccelPhazon"),
        },
    )
    ball_forward_braking_accel_shrubbery: float = dataclasses.field(
        default=12000.0,
        metadata={
            "reflection": FieldReflection[float](
                float, id=0x5B3C4299, original_name="BallForwardBrakingAccelShrubbery"
            ),
        },
    )
    ball_gravity: float = dataclasses.field(
        default=76.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD83E5EEC, original_name="BallGravity"),
        },
    )
    ball_water_gravity: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9C905747, original_name="BallWaterGravity"),
        },
    )
    unknown_0xeeb74968: float = dataclasses.field(
        default=3.200000047683716,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEEB74968, original_name="Unknown"),
        },
    )
    ball_boost_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBD28AF6E, original_name="BallBoostHeight"),
        },
    )
    unknown_0xe2bb0298: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE2BB0298, original_name="Unknown"),
        },
    )
    minimum_alignment_speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE46FA96A, original_name="MinimumAlignmentSpeed"),
        },
    )
    tireness: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4ED87EBD, original_name="Tireness"),
        },
    )
    max_lean_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCA8EDEAB, original_name="MaxLeanAngle"),
        },
    )
    tire_to_marble_threshold_speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x96226D18, original_name="TireToMarbleThresholdSpeed"),
        },
    )
    marble_to_tire_threshold_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x191F4F62, original_name="MarbleToTireThresholdSpeed"),
        },
    )
    force_to_lean_gain: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54C20211, original_name="ForceToLeanGain"),
        },
    )
    lean_tracking_gain: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB90A721E, original_name="LeanTrackingGain"),
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
        if property_count != 48:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHf"
            )

        dec = _FAST_FORMAT.unpack(data.read(480))
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
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[60],
            dec[63],
            dec[66],
            dec[69],
            dec[72],
            dec[75],
            dec[78],
            dec[81],
            dec[84],
            dec[87],
            dec[90],
            dec[93],
            dec[96],
            dec[99],
            dec[102],
            dec[105],
            dec[108],
            dec[111],
            dec[114],
            dec[117],
            dec[120],
            dec[123],
            dec[126],
            dec[129],
            dec[132],
            dec[135],
            dec[138],
            dec[141],
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
            dec[98],
            dec[101],
            dec[104],
            dec[107],
            dec[110],
            dec[113],
            dec[116],
            dec[119],
            dec[122],
            dec[125],
            dec[128],
            dec[131],
            dec[134],
            dec[137],
            dec[140],
            dec[143],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x000")  # 48 properties

        data.write(b"\x18\xd0\xb2\xda")  # 0x18d0b2da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_normal))

        data.write(b"\x84\xf6\x1a\xc5")  # 0x84f61ac5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_air))

        data.write(b"\xed\xb0l\x1d")  # 0xedb06c1d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_ice))

        data.write(b"V\xf9\xf2\xaf")  # 0x56f9f2af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_organic))

        data.write(b"\xd0[d?")  # 0xd05b643f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_water))

        data.write(b"\x12,\xe1\x18")  # 0x122ce118
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_lava))

        data.write(b"\xf8H\xda\xbe")  # 0xf848dabe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_phazon))

        data.write(b"h\xac`(")  # 0x68ac6028
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_accel_shrubbery))

        data.write(b"\xd4\xa2P(")  # 0xd4a25028
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_normal))

        data.write(b"+\\\xb16")  # 0x2b5cb136
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_air))

        data.write(b"B\x1a\xc7\xee")  # 0x421ac7ee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_ice))

        data.write(b"\x05\x86\x13}")  # 0x586137d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_organic))

        data.write(b"\xae\xce\x03\x8b")  # 0xaece038b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_water))

        data.write(b"67\xe8\x15")  # 0x3637e815
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_lava))

        data.write(b"4:8L")  # 0x343a384c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_phazon))

        data.write(b"\x0c\xafF$")  # 0xcaf4624
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_friction_shrubbery))

        data.write(b"\xff\xd4\xa00")  # 0xffd4a030
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_normal))

        data.write(b"Y\xdf\xbc\xb9")  # 0x59dfbcb9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_air))

        data.write(b"0\x99\xcaa")  # 0x3099ca61
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_ice))

        data.write(b"\x16\xc1\xfd\xdb")  # 0x16c1fddb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_organic))

        data.write(b"ld\x891")  # 0x6c648931
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_water))

        data.write(b"KB\xf5\xa9")  # 0x4b42f5a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_lava))

        data.write(b"\x1fL\xc8T")  # 0x1f4cc854
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_phazon))

        data.write(b"\xb3@\x81s")  # 0xb3408173
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_shrubbery))

        data.write(b"\x85\xeeQ\xed")  # 0x85ee51ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x85ee51ed))

        data.write(b"mx\x11\xf5")  # 0x6d7811f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6d7811f5))

        data.write(b"\xf8\n\x06U")  # 0xf80a0655
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_up_gravity))

        data.write(b"\x92\xf3\x0f\x94")  # 0x92f30f94
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_down_gravity))

        data.write(b"\xb0j\xc9p")  # 0xb06ac970
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_normal))

        data.write(b"\xbb<&)")  # 0xbb3c2629
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_air))

        data.write(b"\xd2zP\xf1")  # 0xd27a50f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_ice))

        data.write(b'`R\x02"')  # 0x60520222
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_organic))

        data.write(b"\r\xff\x9b\x92")  # 0xdff9b92
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_water))

        data.write(b"\xbb\xaf\x85w")  # 0xbbaf8577
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_lava))

        data.write(b"P\xf2\xa1\x14")  # 0x50f2a114
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_phazon))

        data.write(b"[<B\x99")  # 0x5b3c4299
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_forward_braking_accel_shrubbery))

        data.write(b"\xd8>^\xec")  # 0xd83e5eec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_gravity))

        data.write(b"\x9c\x90WG")  # 0x9c905747
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_water_gravity))

        data.write(b"\xee\xb7Ih")  # 0xeeb74968
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeeb74968))

        data.write(b"\xbd(\xafn")  # 0xbd28af6e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_boost_height))

        data.write(b"\xe2\xbb\x02\x98")  # 0xe2bb0298
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe2bb0298))

        data.write(b"\xe4o\xa9j")  # 0xe46fa96a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.minimum_alignment_speed))

        data.write(b"N\xd8~\xbd")  # 0x4ed87ebd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.tireness))

        data.write(b"\xca\x8e\xde\xab")  # 0xca8edeab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_lean_angle))

        data.write(b'\x96"m\x18')  # 0x96226d18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.tire_to_marble_threshold_speed))

        data.write(b"\x19\x1fOb")  # 0x191f4f62
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.marble_to_tire_threshold_speed))

        data.write(b"T\xc2\x02\x11")  # 0x54c20211
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.force_to_lean_gain))

        data.write(b"\xb9\nr\x1e")  # 0xb90a721e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lean_tracking_gain))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakBall_MovementJson", data)
        return cls(
            forward_accel_normal=json_data["forward_accel_normal"],
            forward_accel_air=json_data["forward_accel_air"],
            forward_accel_ice=json_data["forward_accel_ice"],
            forward_accel_organic=json_data["forward_accel_organic"],
            forward_accel_water=json_data["forward_accel_water"],
            forward_accel_lava=json_data["forward_accel_lava"],
            forward_accel_phazon=json_data["forward_accel_phazon"],
            forward_accel_shrubbery=json_data["forward_accel_shrubbery"],
            movement_friction_normal=json_data["movement_friction_normal"],
            movement_friction_air=json_data["movement_friction_air"],
            movement_friction_ice=json_data["movement_friction_ice"],
            movement_friction_organic=json_data["movement_friction_organic"],
            movement_friction_water=json_data["movement_friction_water"],
            movement_friction_lava=json_data["movement_friction_lava"],
            movement_friction_phazon=json_data["movement_friction_phazon"],
            movement_friction_shrubbery=json_data["movement_friction_shrubbery"],
            forward_max_speed_normal=json_data["forward_max_speed_normal"],
            forward_max_speed_air=json_data["forward_max_speed_air"],
            forward_max_speed_ice=json_data["forward_max_speed_ice"],
            forward_max_speed_organic=json_data["forward_max_speed_organic"],
            forward_max_speed_water=json_data["forward_max_speed_water"],
            forward_max_speed_lava=json_data["forward_max_speed_lava"],
            forward_max_speed_phazon=json_data["forward_max_speed_phazon"],
            forward_max_speed_shrubbery=json_data["forward_max_speed_shrubbery"],
            unknown_0x85ee51ed=json_data["unknown_0x85ee51ed"],
            unknown_0x6d7811f5=json_data["unknown_0x6d7811f5"],
            ball_up_gravity=json_data["ball_up_gravity"],
            ball_down_gravity=json_data["ball_down_gravity"],
            ball_forward_braking_accel_normal=json_data["ball_forward_braking_accel_normal"],
            ball_forward_braking_accel_air=json_data["ball_forward_braking_accel_air"],
            ball_forward_braking_accel_ice=json_data["ball_forward_braking_accel_ice"],
            ball_forward_braking_accel_organic=json_data["ball_forward_braking_accel_organic"],
            ball_forward_braking_accel_water=json_data["ball_forward_braking_accel_water"],
            ball_forward_braking_accel_lava=json_data["ball_forward_braking_accel_lava"],
            ball_forward_braking_accel_phazon=json_data["ball_forward_braking_accel_phazon"],
            ball_forward_braking_accel_shrubbery=json_data["ball_forward_braking_accel_shrubbery"],
            ball_gravity=json_data["ball_gravity"],
            ball_water_gravity=json_data["ball_water_gravity"],
            unknown_0xeeb74968=json_data["unknown_0xeeb74968"],
            ball_boost_height=json_data["ball_boost_height"],
            unknown_0xe2bb0298=json_data["unknown_0xe2bb0298"],
            minimum_alignment_speed=json_data["minimum_alignment_speed"],
            tireness=json_data["tireness"],
            max_lean_angle=json_data["max_lean_angle"],
            tire_to_marble_threshold_speed=json_data["tire_to_marble_threshold_speed"],
            marble_to_tire_threshold_speed=json_data["marble_to_tire_threshold_speed"],
            force_to_lean_gain=json_data["force_to_lean_gain"],
            lean_tracking_gain=json_data["lean_tracking_gain"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "forward_accel_normal": self.forward_accel_normal,
            "forward_accel_air": self.forward_accel_air,
            "forward_accel_ice": self.forward_accel_ice,
            "forward_accel_organic": self.forward_accel_organic,
            "forward_accel_water": self.forward_accel_water,
            "forward_accel_lava": self.forward_accel_lava,
            "forward_accel_phazon": self.forward_accel_phazon,
            "forward_accel_shrubbery": self.forward_accel_shrubbery,
            "movement_friction_normal": self.movement_friction_normal,
            "movement_friction_air": self.movement_friction_air,
            "movement_friction_ice": self.movement_friction_ice,
            "movement_friction_organic": self.movement_friction_organic,
            "movement_friction_water": self.movement_friction_water,
            "movement_friction_lava": self.movement_friction_lava,
            "movement_friction_phazon": self.movement_friction_phazon,
            "movement_friction_shrubbery": self.movement_friction_shrubbery,
            "forward_max_speed_normal": self.forward_max_speed_normal,
            "forward_max_speed_air": self.forward_max_speed_air,
            "forward_max_speed_ice": self.forward_max_speed_ice,
            "forward_max_speed_organic": self.forward_max_speed_organic,
            "forward_max_speed_water": self.forward_max_speed_water,
            "forward_max_speed_lava": self.forward_max_speed_lava,
            "forward_max_speed_phazon": self.forward_max_speed_phazon,
            "forward_max_speed_shrubbery": self.forward_max_speed_shrubbery,
            "unknown_0x85ee51ed": self.unknown_0x85ee51ed,
            "unknown_0x6d7811f5": self.unknown_0x6d7811f5,
            "ball_up_gravity": self.ball_up_gravity,
            "ball_down_gravity": self.ball_down_gravity,
            "ball_forward_braking_accel_normal": self.ball_forward_braking_accel_normal,
            "ball_forward_braking_accel_air": self.ball_forward_braking_accel_air,
            "ball_forward_braking_accel_ice": self.ball_forward_braking_accel_ice,
            "ball_forward_braking_accel_organic": self.ball_forward_braking_accel_organic,
            "ball_forward_braking_accel_water": self.ball_forward_braking_accel_water,
            "ball_forward_braking_accel_lava": self.ball_forward_braking_accel_lava,
            "ball_forward_braking_accel_phazon": self.ball_forward_braking_accel_phazon,
            "ball_forward_braking_accel_shrubbery": self.ball_forward_braking_accel_shrubbery,
            "ball_gravity": self.ball_gravity,
            "ball_water_gravity": self.ball_water_gravity,
            "unknown_0xeeb74968": self.unknown_0xeeb74968,
            "ball_boost_height": self.ball_boost_height,
            "unknown_0xe2bb0298": self.unknown_0xe2bb0298,
            "minimum_alignment_speed": self.minimum_alignment_speed,
            "tireness": self.tireness,
            "max_lean_angle": self.max_lean_angle,
            "tire_to_marble_threshold_speed": self.tire_to_marble_threshold_speed,
            "marble_to_tire_threshold_speed": self.marble_to_tire_threshold_speed,
            "force_to_lean_gain": self.force_to_lean_gain,
            "lean_tracking_gain": self.lean_tracking_gain,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x18D0B2DA: ("forward_accel_normal", structs.decode_BIG_f),
    0x84F61AC5: ("forward_accel_air", structs.decode_BIG_f),
    0xEDB06C1D: ("forward_accel_ice", structs.decode_BIG_f),
    0x56F9F2AF: ("forward_accel_organic", structs.decode_BIG_f),
    0xD05B643F: ("forward_accel_water", structs.decode_BIG_f),
    0x122CE118: ("forward_accel_lava", structs.decode_BIG_f),
    0xF848DABE: ("forward_accel_phazon", structs.decode_BIG_f),
    0x68AC6028: ("forward_accel_shrubbery", structs.decode_BIG_f),
    0xD4A25028: ("movement_friction_normal", structs.decode_BIG_f),
    0x2B5CB136: ("movement_friction_air", structs.decode_BIG_f),
    0x421AC7EE: ("movement_friction_ice", structs.decode_BIG_f),
    0x0586137D: ("movement_friction_organic", structs.decode_BIG_f),
    0xAECE038B: ("movement_friction_water", structs.decode_BIG_f),
    0x3637E815: ("movement_friction_lava", structs.decode_BIG_f),
    0x343A384C: ("movement_friction_phazon", structs.decode_BIG_f),
    0x0CAF4624: ("movement_friction_shrubbery", structs.decode_BIG_f),
    0xFFD4A030: ("forward_max_speed_normal", structs.decode_BIG_f),
    0x59DFBCB9: ("forward_max_speed_air", structs.decode_BIG_f),
    0x3099CA61: ("forward_max_speed_ice", structs.decode_BIG_f),
    0x16C1FDDB: ("forward_max_speed_organic", structs.decode_BIG_f),
    0x6C648931: ("forward_max_speed_water", structs.decode_BIG_f),
    0x4B42F5A9: ("forward_max_speed_lava", structs.decode_BIG_f),
    0x1F4CC854: ("forward_max_speed_phazon", structs.decode_BIG_f),
    0xB3408173: ("forward_max_speed_shrubbery", structs.decode_BIG_f),
    0x85EE51ED: ("unknown_0x85ee51ed", structs.decode_BIG_f),
    0x6D7811F5: ("unknown_0x6d7811f5", structs.decode_BIG_f),
    0xF80A0655: ("ball_up_gravity", structs.decode_BIG_f),
    0x92F30F94: ("ball_down_gravity", structs.decode_BIG_f),
    0xB06AC970: ("ball_forward_braking_accel_normal", structs.decode_BIG_f),
    0xBB3C2629: ("ball_forward_braking_accel_air", structs.decode_BIG_f),
    0xD27A50F1: ("ball_forward_braking_accel_ice", structs.decode_BIG_f),
    0x60520222: ("ball_forward_braking_accel_organic", structs.decode_BIG_f),
    0x0DFF9B92: ("ball_forward_braking_accel_water", structs.decode_BIG_f),
    0xBBAF8577: ("ball_forward_braking_accel_lava", structs.decode_BIG_f),
    0x50F2A114: ("ball_forward_braking_accel_phazon", structs.decode_BIG_f),
    0x5B3C4299: ("ball_forward_braking_accel_shrubbery", structs.decode_BIG_f),
    0xD83E5EEC: ("ball_gravity", structs.decode_BIG_f),
    0x9C905747: ("ball_water_gravity", structs.decode_BIG_f),
    0xEEB74968: ("unknown_0xeeb74968", structs.decode_BIG_f),
    0xBD28AF6E: ("ball_boost_height", structs.decode_BIG_f),
    0xE2BB0298: ("unknown_0xe2bb0298", structs.decode_BIG_f),
    0xE46FA96A: ("minimum_alignment_speed", structs.decode_BIG_f),
    0x4ED87EBD: ("tireness", structs.decode_BIG_f),
    0xCA8EDEAB: ("max_lean_angle", structs.decode_BIG_f),
    0x96226D18: ("tire_to_marble_threshold_speed", structs.decode_BIG_f),
    0x191F4F62: ("marble_to_tire_threshold_speed", structs.decode_BIG_f),
    0x54C20211: ("force_to_lean_gain", structs.decode_BIG_f),
    0xB90A721E: ("lean_tracking_gain", structs.decode_BIG_f),
}
