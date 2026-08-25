# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayer_AimStuffJson(typing_extensions.TypedDict):
        aim_min_time: float
        aim_max_time: float
        aim_max_distance: float
        aim_max_angle_left: float
        aim_max_angle_right: float
        aim_max_angle_up: float
        aim_max_angle_down: float
        aim_angle_per_second: float
        aim_threshold_distance: float
        aim_turn_angle_per_second: float
        unknown_0x54354c80: float
        aim_box_width: float
        aim_box_height: float
        aim_target_timer: float
        aim_assist_horizontal_angle: float
        aim_assist_vertical_angle: float
        unknown_0x38ee6d6e: bool
        unknown_0x9e3aceb5: bool
        unknown_0x228a8def: bool
        unknown_0x534a7b3c: bool
        unknown_0xd2dfc16a: bool
        unknown_0x60f08beb: int
        unknown_0xcca13e22: bool
        unknown_0x85437c89: float
        unknown_0x21047226: bool
        unknown_0x95f112be: float
        unknown_0xb5d9e201: bool
        unknown_0x747a79cb: float
        unknown_0x189d7017: int
        unknown_0xa065b70c: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x27C60D0A,
    0xB7B51DE0,
    0xF77D0359,
    0xDE887CCA,
    0xB4B07D5D,
    0xE5F8C567,
    0x9774749D,
    0x133F3002,
    0x96FAB602,
    0x94164A2F,
    0x54354C80,
    0x5361CE18,
    0x4B2E9260,
    0x3B9A3789,
    0x38DD0B85,
    0x1157883E,
    0x38EE6D6E,
    0x9E3ACEB5,
    0x228A8DEF,
    0x534A7B3C,
    0xD2DFC16A,
    0x60F08BEB,
    0xCCA13E22,
    0x85437C89,
    0x21047226,
    0x95F112BE,
    0xB5D9E201,
    0x747A79CB,
    0x189D7017,
    0xA065B70C,
)


@dataclasses.dataclass()
class TweakPlayer_AimStuff(BaseProperty):
    aim_min_time: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x27C60D0A, original_name="AimMinTime"),
        },
    )
    aim_max_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB7B51DE0, original_name="AimMaxTime"),
        },
    )
    aim_max_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF77D0359, original_name="AimMaxDistance"),
        },
    )
    aim_max_angle_left: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE887CCA, original_name="AimMaxAngleLeft"),
        },
    )
    aim_max_angle_right: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB4B07D5D, original_name="AimMaxAngleRight"),
        },
    )
    aim_max_angle_up: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE5F8C567, original_name="AimMaxAngleUp"),
        },
    )
    aim_max_angle_down: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9774749D, original_name="AimMaxAngleDown"),
        },
    )
    aim_angle_per_second: float = dataclasses.field(
        default=110.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x133F3002, original_name="AimAnglePerSecond"),
        },
    )
    aim_threshold_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x96FAB602, original_name="AimThresholdDistance"),
        },
    )
    aim_turn_angle_per_second: float = dataclasses.field(
        default=360.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x94164A2F, original_name="AimTurnAnglePerSecond"),
        },
    )
    unknown_0x54354c80: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54354C80, original_name="Unknown"),
        },
    )
    aim_box_width: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5361CE18, original_name="AimBoxWidth"),
        },
    )
    aim_box_height: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B2E9260, original_name="AimBoxHeight"),
        },
    )
    aim_target_timer: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3B9A3789, original_name="AimTargetTimer"),
        },
    )
    aim_assist_horizontal_angle: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38DD0B85, original_name="AimAssistHorizontalAngle"),
        },
    )
    aim_assist_vertical_angle: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1157883E, original_name="AimAssistVerticalAngle"),
        },
    )
    unknown_0x38ee6d6e: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x38EE6D6E, original_name="Unknown"),
        },
    )
    unknown_0x9e3aceb5: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9E3ACEB5, original_name="Unknown"),
        },
    )
    unknown_0x228a8def: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x228A8DEF, original_name="Unknown"),
        },
    )
    unknown_0x534a7b3c: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x534A7B3C, original_name="Unknown"),
        },
    )
    unknown_0xd2dfc16a: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xD2DFC16A, original_name="Unknown"),
        },
    )
    unknown_0x60f08beb: enums.TweakPlayer_AimStuff_UnknownEnum1Enum = dataclasses.field(
        default=enums.TweakPlayer_AimStuff_UnknownEnum1Enum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.TweakPlayer_AimStuff_UnknownEnum1Enum](
                enums.TweakPlayer_AimStuff_UnknownEnum1Enum,
                id=0x60F08BEB,
                original_name="Unknown",
                from_json=enums.TweakPlayer_AimStuff_UnknownEnum1Enum.from_json,
                to_json=enums.TweakPlayer_AimStuff_UnknownEnum1Enum.to_json,
            ),
        },
    )
    unknown_0xcca13e22: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCCA13E22, original_name="Unknown"),
        },
    )
    unknown_0x85437c89: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x85437C89, original_name="Unknown"),
        },
    )
    unknown_0x21047226: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x21047226, original_name="Unknown"),
        },
    )
    unknown_0x95f112be: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95F112BE, original_name="Unknown"),
        },
    )
    unknown_0xb5d9e201: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB5D9E201, original_name="Unknown"),
        },
    )
    unknown_0x747a79cb: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x747A79CB, original_name="Unknown"),
        },
    )
    unknown_0x189d7017: enums.TweakPlayer_AimStuff_UnknownEnum2Enum = dataclasses.field(
        default=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.Unknown2,
        metadata={
            "reflection": FieldReflection[enums.TweakPlayer_AimStuff_UnknownEnum2Enum](
                enums.TweakPlayer_AimStuff_UnknownEnum2Enum,
                id=0x189D7017,
                original_name="Unknown",
                from_json=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.from_json,
                to_json=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.to_json,
            ),
        },
    )
    unknown_0xa065b70c: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA065B70C, original_name="Unknown"),
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
        if property_count != 30:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?LH?LH?LH?LH?LHLLH?LHfLH?LHfLH?LHfLHLLH?"
            )

        dec = _FAST_FORMAT.unpack(data.read(273))
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
            enums.TweakPlayer_AimStuff_UnknownEnum1Enum(dec[65]),
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            enums.TweakPlayer_AimStuff_UnknownEnum2Enum(dec[86]),
            dec[89],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1e")  # 30 properties

        data.write(b"'\xc6\r\n")  # 0x27c60d0a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_min_time))

        data.write(b"\xb7\xb5\x1d\xe0")  # 0xb7b51de0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_max_time))

        data.write(b"\xf7}\x03Y")  # 0xf77d0359
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_max_distance))

        data.write(b"\xde\x88|\xca")  # 0xde887cca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_left))

        data.write(b"\xb4\xb0}]")  # 0xb4b07d5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_right))

        data.write(b"\xe5\xf8\xc5g")  # 0xe5f8c567
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_up))

        data.write(b"\x97tt\x9d")  # 0x9774749d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_down))

        data.write(b"\x13?0\x02")  # 0x133f3002
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_angle_per_second))

        data.write(b"\x96\xfa\xb6\x02")  # 0x96fab602
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_threshold_distance))

        data.write(b"\x94\x16J/")  # 0x94164a2f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_turn_angle_per_second))

        data.write(b"T5L\x80")  # 0x54354c80
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x54354c80))

        data.write(b"Sa\xce\x18")  # 0x5361ce18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_box_width))

        data.write(b"K.\x92`")  # 0x4b2e9260
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_box_height))

        data.write(b";\x9a7\x89")  # 0x3b9a3789
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_target_timer))

        data.write(b"8\xdd\x0b\x85")  # 0x38dd0b85
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_assist_horizontal_angle))

        data.write(b"\x11W\x88>")  # 0x1157883e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aim_assist_vertical_angle))

        data.write(b"8\xeemn")  # 0x38ee6d6e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x38ee6d6e))

        data.write(b"\x9e:\xce\xb5")  # 0x9e3aceb5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x9e3aceb5))

        data.write(b'"\x8a\x8d\xef')  # 0x228a8def
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x228a8def))

        data.write(b"SJ{<")  # 0x534a7b3c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x534a7b3c))

        data.write(b"\xd2\xdf\xc1j")  # 0xd2dfc16a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xd2dfc16a))

        data.write(b"`\xf0\x8b\xeb")  # 0x60f08beb
        data.write(b"\x00\x04")  # size
        self.unknown_0x60f08beb.to_stream(data, game)

        data.write(b'\xcc\xa1>"')  # 0xcca13e22
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xcca13e22))

        data.write(b"\x85C|\x89")  # 0x85437c89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x85437c89))

        data.write(b"!\x04r&")  # 0x21047226
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x21047226))

        data.write(b"\x95\xf1\x12\xbe")  # 0x95f112be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95f112be))

        data.write(b"\xb5\xd9\xe2\x01")  # 0xb5d9e201
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xb5d9e201))

        data.write(b"tzy\xcb")  # 0x747a79cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x747a79cb))

        data.write(b"\x18\x9dp\x17")  # 0x189d7017
        data.write(b"\x00\x04")  # size
        self.unknown_0x189d7017.to_stream(data, game)

        data.write(b"\xa0e\xb7\x0c")  # 0xa065b70c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa065b70c))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_AimStuffJson", data)
        return cls(
            aim_min_time=json_data["aim_min_time"],
            aim_max_time=json_data["aim_max_time"],
            aim_max_distance=json_data["aim_max_distance"],
            aim_max_angle_left=json_data["aim_max_angle_left"],
            aim_max_angle_right=json_data["aim_max_angle_right"],
            aim_max_angle_up=json_data["aim_max_angle_up"],
            aim_max_angle_down=json_data["aim_max_angle_down"],
            aim_angle_per_second=json_data["aim_angle_per_second"],
            aim_threshold_distance=json_data["aim_threshold_distance"],
            aim_turn_angle_per_second=json_data["aim_turn_angle_per_second"],
            unknown_0x54354c80=json_data["unknown_0x54354c80"],
            aim_box_width=json_data["aim_box_width"],
            aim_box_height=json_data["aim_box_height"],
            aim_target_timer=json_data["aim_target_timer"],
            aim_assist_horizontal_angle=json_data["aim_assist_horizontal_angle"],
            aim_assist_vertical_angle=json_data["aim_assist_vertical_angle"],
            unknown_0x38ee6d6e=json_data["unknown_0x38ee6d6e"],
            unknown_0x9e3aceb5=json_data["unknown_0x9e3aceb5"],
            unknown_0x228a8def=json_data["unknown_0x228a8def"],
            unknown_0x534a7b3c=json_data["unknown_0x534a7b3c"],
            unknown_0xd2dfc16a=json_data["unknown_0xd2dfc16a"],
            unknown_0x60f08beb=enums.TweakPlayer_AimStuff_UnknownEnum1Enum.from_json(json_data["unknown_0x60f08beb"]),
            unknown_0xcca13e22=json_data["unknown_0xcca13e22"],
            unknown_0x85437c89=json_data["unknown_0x85437c89"],
            unknown_0x21047226=json_data["unknown_0x21047226"],
            unknown_0x95f112be=json_data["unknown_0x95f112be"],
            unknown_0xb5d9e201=json_data["unknown_0xb5d9e201"],
            unknown_0x747a79cb=json_data["unknown_0x747a79cb"],
            unknown_0x189d7017=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.from_json(json_data["unknown_0x189d7017"]),
            unknown_0xa065b70c=json_data["unknown_0xa065b70c"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "aim_min_time": self.aim_min_time,
            "aim_max_time": self.aim_max_time,
            "aim_max_distance": self.aim_max_distance,
            "aim_max_angle_left": self.aim_max_angle_left,
            "aim_max_angle_right": self.aim_max_angle_right,
            "aim_max_angle_up": self.aim_max_angle_up,
            "aim_max_angle_down": self.aim_max_angle_down,
            "aim_angle_per_second": self.aim_angle_per_second,
            "aim_threshold_distance": self.aim_threshold_distance,
            "aim_turn_angle_per_second": self.aim_turn_angle_per_second,
            "unknown_0x54354c80": self.unknown_0x54354c80,
            "aim_box_width": self.aim_box_width,
            "aim_box_height": self.aim_box_height,
            "aim_target_timer": self.aim_target_timer,
            "aim_assist_horizontal_angle": self.aim_assist_horizontal_angle,
            "aim_assist_vertical_angle": self.aim_assist_vertical_angle,
            "unknown_0x38ee6d6e": self.unknown_0x38ee6d6e,
            "unknown_0x9e3aceb5": self.unknown_0x9e3aceb5,
            "unknown_0x228a8def": self.unknown_0x228a8def,
            "unknown_0x534a7b3c": self.unknown_0x534a7b3c,
            "unknown_0xd2dfc16a": self.unknown_0xd2dfc16a,
            "unknown_0x60f08beb": self.unknown_0x60f08beb.to_json(),
            "unknown_0xcca13e22": self.unknown_0xcca13e22,
            "unknown_0x85437c89": self.unknown_0x85437c89,
            "unknown_0x21047226": self.unknown_0x21047226,
            "unknown_0x95f112be": self.unknown_0x95f112be,
            "unknown_0xb5d9e201": self.unknown_0xb5d9e201,
            "unknown_0x747a79cb": self.unknown_0x747a79cb,
            "unknown_0x189d7017": self.unknown_0x189d7017.to_json(),
            "unknown_0xa065b70c": self.unknown_0xa065b70c,
        }


def _decode_unknown_0x60f08beb(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.TweakPlayer_AimStuff_UnknownEnum1Enum:
    return enums.TweakPlayer_AimStuff_UnknownEnum1Enum.from_stream(data, game)


def _decode_unknown_0x189d7017(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.TweakPlayer_AimStuff_UnknownEnum2Enum:
    return enums.TweakPlayer_AimStuff_UnknownEnum2Enum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x27C60D0A: ("aim_min_time", structs.decode_BIG_f),
    0xB7B51DE0: ("aim_max_time", structs.decode_BIG_f),
    0xF77D0359: ("aim_max_distance", structs.decode_BIG_f),
    0xDE887CCA: ("aim_max_angle_left", structs.decode_BIG_f),
    0xB4B07D5D: ("aim_max_angle_right", structs.decode_BIG_f),
    0xE5F8C567: ("aim_max_angle_up", structs.decode_BIG_f),
    0x9774749D: ("aim_max_angle_down", structs.decode_BIG_f),
    0x133F3002: ("aim_angle_per_second", structs.decode_BIG_f),
    0x96FAB602: ("aim_threshold_distance", structs.decode_BIG_f),
    0x94164A2F: ("aim_turn_angle_per_second", structs.decode_BIG_f),
    0x54354C80: ("unknown_0x54354c80", structs.decode_BIG_f),
    0x5361CE18: ("aim_box_width", structs.decode_BIG_f),
    0x4B2E9260: ("aim_box_height", structs.decode_BIG_f),
    0x3B9A3789: ("aim_target_timer", structs.decode_BIG_f),
    0x38DD0B85: ("aim_assist_horizontal_angle", structs.decode_BIG_f),
    0x1157883E: ("aim_assist_vertical_angle", structs.decode_BIG_f),
    0x38EE6D6E: ("unknown_0x38ee6d6e", structs.decode_BIG_bool_),
    0x9E3ACEB5: ("unknown_0x9e3aceb5", structs.decode_BIG_bool_),
    0x228A8DEF: ("unknown_0x228a8def", structs.decode_BIG_bool_),
    0x534A7B3C: ("unknown_0x534a7b3c", structs.decode_BIG_bool_),
    0xD2DFC16A: ("unknown_0xd2dfc16a", structs.decode_BIG_bool_),
    0x60F08BEB: ("unknown_0x60f08beb", _decode_unknown_0x60f08beb),
    0xCCA13E22: ("unknown_0xcca13e22", structs.decode_BIG_bool_),
    0x85437C89: ("unknown_0x85437c89", structs.decode_BIG_f),
    0x21047226: ("unknown_0x21047226", structs.decode_BIG_bool_),
    0x95F112BE: ("unknown_0x95f112be", structs.decode_BIG_f),
    0xB5D9E201: ("unknown_0xb5d9e201", structs.decode_BIG_bool_),
    0x747A79CB: ("unknown_0x747a79cb", structs.decode_BIG_f),
    0x189D7017: ("unknown_0x189d7017", _decode_unknown_0x189d7017),
    0xA065B70C: ("unknown_0xa065b70c", structs.decode_BIG_bool_),
}
