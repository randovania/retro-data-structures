# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GhorStructC import GhorStructC
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct35 import UnknownStruct35
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct36Json(typing_extensions.TypedDict):
        is_gandrayda: bool
        slip_time: float
        collision_set: str
        unknown_0xfaf186b6: str
        snap_locator: str
        unknown_struct35: json_util.JsonObject
        ghor_struct_c: json_util.JsonObject
        ball_target_extend: json_util.JsonObject
        ball_target_retract: json_util.JsonObject
        unknown_0x13d02889: str
        unknown_0x4a744859: json_util.JsonObject
        jump_distance: float
        jump_height: float
        jump_shockwave: json_util.JsonObject
        shock_wave_info: json_util.JsonObject
        move_min_range: float
        move_max_range: float
        move_desired_range: float
        move_min_distance: float
        move_desired_distance: float
        unknown_0xa31d0055: float
        unknown_0x9ae279da: float
        unknown_0xb39c84c2: float
        unknown_0x2a35593b: float


@dataclasses.dataclass()
class UnknownStruct36(BaseProperty):
    is_gandrayda: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x531A8C85, original_name="IsGandrayda"),
        },
    )
    slip_time: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9865FC0, original_name="SlipTime"),
        },
    )
    collision_set: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x9CE31FFA, original_name="CollisionSet"),
        },
    )
    unknown_0xfaf186b6: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xFAF186B6, original_name="Unknown"),
        },
    )
    snap_locator: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5D1949B5, original_name="SnapLocator"),
        },
    )
    unknown_struct35: UnknownStruct35 = dataclasses.field(
        default_factory=UnknownStruct35,
        metadata={
            "reflection": FieldReflection[UnknownStruct35](
                UnknownStruct35,
                id=0xAEC7546E,
                original_name="UnknownStruct35",
                from_json=UnknownStruct35.from_json,
                to_json=UnknownStruct35.to_json,
            ),
        },
    )
    ghor_struct_c: GhorStructC = dataclasses.field(
        default_factory=GhorStructC,
        metadata={
            "reflection": FieldReflection[GhorStructC](
                GhorStructC,
                id=0x810EC49A,
                original_name="GhorStructC",
                from_json=GhorStructC.from_json,
                to_json=GhorStructC.to_json,
            ),
        },
    )
    ball_target_extend: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x9B98F8CE,
                original_name="BallTargetExtend",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    ball_target_retract: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x3D14FB8E,
                original_name="BallTargetRetract",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    unknown_0x13d02889: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x13D02889, original_name="Unknown"),
        },
    )
    unknown_0x4a744859: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x4A744859, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    jump_distance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9B2EA489, original_name="JumpDistance"),
        },
    )
    jump_height: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD0475191, original_name="JumpHeight"),
        },
    )
    jump_shockwave: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x56C192F3,
                original_name="JumpShockwave",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0xF55A1548,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    move_min_range: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8554E360, original_name="MoveMinRange"),
        },
    )
    move_max_range: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC51B9B16, original_name="MoveMaxRange"),
        },
    )
    move_desired_range: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAFECAB12, original_name="MoveDesiredRange"),
        },
    )
    move_min_distance: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7CC59B31, original_name="MoveMinDistance"),
        },
    )
    move_desired_distance: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD6AAD996, original_name="MoveDesiredDistance"),
        },
    )
    unknown_0xa31d0055: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA31D0055, original_name="Unknown"),
        },
    )
    unknown_0x9ae279da: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9AE279DA, original_name="Unknown"),
        },
    )
    unknown_0xb39c84c2: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB39C84C2, original_name="Unknown"),
        },
    )
    unknown_0x2a35593b: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A35593B, original_name="Unknown"),
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
        if property_count != 24:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531A8C85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9865FC0
        slip_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9CE31FFA
        collision_set = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFAF186B6
        unknown_0xfaf186b6 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D1949B5
        snap_locator = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAEC7546E
        unknown_struct35 = UnknownStruct35.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x810EC49A
        ghor_struct_c = GhorStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B98F8CE
        ball_target_extend = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D14FB8E
        ball_target_retract = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13D02889
        unknown_0x13d02889 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A744859
        unknown_0x4a744859 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B2EA489
        jump_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD0475191
        jump_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56C192F3
        jump_shockwave = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF55A1548
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8554E360
        move_min_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC51B9B16
        move_max_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFECAB12
        move_desired_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CC59B31
        move_min_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6AAD996
        move_desired_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA31D0055
        unknown_0xa31d0055 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AE279DA
        unknown_0x9ae279da = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB39C84C2
        unknown_0xb39c84c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A35593B
        unknown_0x2a35593b = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            is_gandrayda,
            slip_time,
            collision_set,
            unknown_0xfaf186b6,
            snap_locator,
            unknown_struct35,
            ghor_struct_c,
            ball_target_extend,
            ball_target_retract,
            unknown_0x13d02889,
            unknown_0x4a744859,
            jump_distance,
            jump_height,
            jump_shockwave,
            shock_wave_info,
            move_min_range,
            move_max_range,
            move_desired_range,
            move_min_distance,
            move_desired_distance,
            unknown_0xa31d0055,
            unknown_0x9ae279da,
            unknown_0xb39c84c2,
            unknown_0x2a35593b,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x18")  # 24 properties

        data.write(b"S\x1a\x8c\x85")  # 0x531a8c85
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b"\xe9\x86_\xc0")  # 0xe9865fc0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.slip_time))

        data.write(b"\x9c\xe3\x1f\xfa")  # 0x9ce31ffa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.collision_set.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfa\xf1\x86\xb6")  # 0xfaf186b6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xfaf186b6.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"]\x19I\xb5")  # 0x5d1949b5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.snap_locator.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xae\xc7Tn")  # 0xaec7546e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct35.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81\x0e\xc4\x9a")  # 0x810ec49a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9b\x98\xf8\xce")  # 0x9b98f8ce
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_target_extend.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"=\x14\xfb\x8e")  # 0x3d14fb8e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_target_retract.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x13\xd0(\x89")  # 0x13d02889
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x13d02889.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"JtHY")  # 0x4a744859
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x4a744859.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9b.\xa4\x89")  # 0x9b2ea489
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.jump_distance))

        data.write(b"\xd0GQ\x91")  # 0xd0475191
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.jump_height))

        data.write(b"V\xc1\x92\xf3")  # 0x56c192f3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.jump_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf5Z\x15H")  # 0xf55a1548
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x85T\xe3`")  # 0x8554e360
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_min_range))

        data.write(b"\xc5\x1b\x9b\x16")  # 0xc51b9b16
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_max_range))

        data.write(b"\xaf\xec\xab\x12")  # 0xafecab12
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_desired_range))

        data.write(b"|\xc5\x9b1")  # 0x7cc59b31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_min_distance))

        data.write(b"\xd6\xaa\xd9\x96")  # 0xd6aad996
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_desired_distance))

        data.write(b"\xa3\x1d\x00U")  # 0xa31d0055
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa31d0055))

        data.write(b"\x9a\xe2y\xda")  # 0x9ae279da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9ae279da))

        data.write(b"\xb3\x9c\x84\xc2")  # 0xb39c84c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb39c84c2))

        data.write(b"*5Y;")  # 0x2a35593b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2a35593b))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct36Json", data)
        return cls(
            is_gandrayda=json_data["is_gandrayda"],
            slip_time=json_data["slip_time"],
            collision_set=json_data["collision_set"],
            unknown_0xfaf186b6=json_data["unknown_0xfaf186b6"],
            snap_locator=json_data["snap_locator"],
            unknown_struct35=UnknownStruct35.from_json(json_data["unknown_struct35"]),
            ghor_struct_c=GhorStructC.from_json(json_data["ghor_struct_c"]),
            ball_target_extend=Spline.from_json(json_data["ball_target_extend"]),
            ball_target_retract=Spline.from_json(json_data["ball_target_retract"]),
            unknown_0x13d02889=json_data["unknown_0x13d02889"],
            unknown_0x4a744859=Spline.from_json(json_data["unknown_0x4a744859"]),
            jump_distance=json_data["jump_distance"],
            jump_height=json_data["jump_height"],
            jump_shockwave=ShockWaveInfo.from_json(json_data["jump_shockwave"]),
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            move_min_range=json_data["move_min_range"],
            move_max_range=json_data["move_max_range"],
            move_desired_range=json_data["move_desired_range"],
            move_min_distance=json_data["move_min_distance"],
            move_desired_distance=json_data["move_desired_distance"],
            unknown_0xa31d0055=json_data["unknown_0xa31d0055"],
            unknown_0x9ae279da=json_data["unknown_0x9ae279da"],
            unknown_0xb39c84c2=json_data["unknown_0xb39c84c2"],
            unknown_0x2a35593b=json_data["unknown_0x2a35593b"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "is_gandrayda": self.is_gandrayda,
            "slip_time": self.slip_time,
            "collision_set": self.collision_set,
            "unknown_0xfaf186b6": self.unknown_0xfaf186b6,
            "snap_locator": self.snap_locator,
            "unknown_struct35": self.unknown_struct35.to_json(),
            "ghor_struct_c": self.ghor_struct_c.to_json(),
            "ball_target_extend": self.ball_target_extend.to_json(),
            "ball_target_retract": self.ball_target_retract.to_json(),
            "unknown_0x13d02889": self.unknown_0x13d02889,
            "unknown_0x4a744859": self.unknown_0x4a744859.to_json(),
            "jump_distance": self.jump_distance,
            "jump_height": self.jump_height,
            "jump_shockwave": self.jump_shockwave.to_json(),
            "shock_wave_info": self.shock_wave_info.to_json(),
            "move_min_range": self.move_min_range,
            "move_max_range": self.move_max_range,
            "move_desired_range": self.move_desired_range,
            "move_min_distance": self.move_min_distance,
            "move_desired_distance": self.move_desired_distance,
            "unknown_0xa31d0055": self.unknown_0xa31d0055,
            "unknown_0x9ae279da": self.unknown_0x9ae279da,
            "unknown_0xb39c84c2": self.unknown_0xb39c84c2,
            "unknown_0x2a35593b": self.unknown_0x2a35593b,
        }


def _decode_collision_set(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xfaf186b6(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_snap_locator(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_struct35(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct35:
    return UnknownStruct35.from_stream(data, game, property_size)


def _decode_ghor_struct_c(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructC:
    return GhorStructC.from_stream(data, game, property_size)


def _decode_ball_target_extend(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_ball_target_retract(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x13d02889(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x4a744859(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_jump_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x531A8C85: ("is_gandrayda", structs.decode_BIG_bool_),
    0xE9865FC0: ("slip_time", structs.decode_BIG_f),
    0x9CE31FFA: ("collision_set", _decode_collision_set),
    0xFAF186B6: ("unknown_0xfaf186b6", _decode_unknown_0xfaf186b6),
    0x5D1949B5: ("snap_locator", _decode_snap_locator),
    0xAEC7546E: ("unknown_struct35", _decode_unknown_struct35),
    0x810EC49A: ("ghor_struct_c", _decode_ghor_struct_c),
    0x9B98F8CE: ("ball_target_extend", _decode_ball_target_extend),
    0x3D14FB8E: ("ball_target_retract", _decode_ball_target_retract),
    0x13D02889: ("unknown_0x13d02889", _decode_unknown_0x13d02889),
    0x4A744859: ("unknown_0x4a744859", _decode_unknown_0x4a744859),
    0x9B2EA489: ("jump_distance", structs.decode_BIG_f),
    0xD0475191: ("jump_height", structs.decode_BIG_f),
    0x56C192F3: ("jump_shockwave", _decode_jump_shockwave),
    0xF55A1548: ("shock_wave_info", _decode_shock_wave_info),
    0x8554E360: ("move_min_range", structs.decode_BIG_f),
    0xC51B9B16: ("move_max_range", structs.decode_BIG_f),
    0xAFECAB12: ("move_desired_range", structs.decode_BIG_f),
    0x7CC59B31: ("move_min_distance", structs.decode_BIG_f),
    0xD6AAD996: ("move_desired_distance", structs.decode_BIG_f),
    0xA31D0055: ("unknown_0xa31d0055", structs.decode_BIG_f),
    0x9AE279DA: ("unknown_0x9ae279da", structs.decode_BIG_f),
    0xB39C84C2: ("unknown_0xb39c84c2", structs.decode_BIG_f),
    0x2A35593B: ("unknown_0x2a35593b", structs.decode_BIG_f),
}
