# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakTargeting_UnknownStruct3Json(typing_extensions.TypedDict):
        unknown_0x77feeef0: float
        unknown_0x6c68981b: json_util.JsonValue
        orbit_lock_color: json_util.JsonValue
        unknown_0x1b905dfe: json_util.JsonValue
        unknown_0x05ee18e2: json_util.JsonValue
        unknown_0x337e60a9: json_util.JsonValue
        unknown_0x4f635051: float
        unknown_0x20af6870: float
        unknown_0x0a5848fb: float
        unknown_0x01b64bdf: float
        unknown_0xd4044569: float
        unknown_0xae6c5261: float
        unknown_0x84ac3eee: json_util.JsonValue
        unknown_0x396d001e: json_util.JsonValue
        unknown_0xe8008fa5: float
        unknown_0xe9c116bf: float
        unknown_0x79f18548: float
        unknown_0x26978c4b: float
        unknown_0x9d58f885: float
        unknown_0x99c2c9af: float
        unknown_0x326905f2: float
        unknown_0x3cf144d1: float
        unknown_0x7975982c: float
        unknown_0x460b2702: float
        unknown_0x43c8a56e: json_util.JsonValue
        unknown_0x83f19d56: float
        unknown_0xa9cd091f: float
        unknown_0xe589a4f9: float
        unknown_0xd7cf6cc5: float
        unknown_0x85e956d3: float
        unknown_0xa6f2b827: float
        unknown_0xca637bcd: float
        unknown_0xf04414b3: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x77FEEEF0,
    0x6C68981B,
    0x6D5BC9C5,
    0x1B905DFE,
    0x5EE18E2,
    0x337E60A9,
    0x4F635051,
    0x20AF6870,
    0xA5848FB,
    0x1B64BDF,
    0xD4044569,
    0xAE6C5261,
    0x84AC3EEE,
    0x396D001E,
    0xE8008FA5,
    0xE9C116BF,
    0x79F18548,
    0x26978C4B,
    0x9D58F885,
    0x99C2C9AF,
    0x326905F2,
    0x3CF144D1,
    0x7975982C,
    0x460B2702,
    0x43C8A56E,
    0x83F19D56,
    0xA9CD091F,
    0xE589A4F9,
    0xD7CF6CC5,
    0x85E956D3,
    0xA6F2B827,
    0xCA637BCD,
    0xF04414B3,
)


@dataclasses.dataclass()
class TweakTargeting_UnknownStruct3(BaseProperty):
    unknown_0x77feeef0: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x77FEEEF0, original_name="Unknown"),
        },
    )
    unknown_0x6c68981b: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6C68981B, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    orbit_lock_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6D5BC9C5, original_name="OrbitLockColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x1b905dfe: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1B905DFE, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x05ee18e2: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x05EE18E2, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x337e60a9: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x337E60A9, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0x4f635051: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4F635051, original_name="Unknown"),
        },
    )
    unknown_0x20af6870: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x20AF6870, original_name="Unknown"),
        },
    )
    unknown_0x0a5848fb: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A5848FB, original_name="Unknown"),
        },
    )
    unknown_0x01b64bdf: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x01B64BDF, original_name="Unknown"),
        },
    )
    unknown_0xd4044569: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4044569, original_name="Unknown"),
        },
    )
    unknown_0xae6c5261: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAE6C5261, original_name="Unknown"),
        },
    )
    unknown_0x84ac3eee: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x84AC3EEE, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x396d001e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x396D001E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xe8008fa5: float = dataclasses.field(
        default=54.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8008FA5, original_name="Unknown"),
        },
    )
    unknown_0xe9c116bf: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9C116BF, original_name="Unknown"),
        },
    )
    unknown_0x79f18548: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x79F18548, original_name="Unknown"),
        },
    )
    unknown_0x26978c4b: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x26978C4B, original_name="Unknown"),
        },
    )
    unknown_0x9d58f885: float = dataclasses.field(
        default=0.125,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9D58F885, original_name="Unknown"),
        },
    )
    unknown_0x99c2c9af: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x99C2C9AF, original_name="Unknown"),
        },
    )
    unknown_0x326905f2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x326905F2, original_name="Unknown"),
        },
    )
    unknown_0x3cf144d1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3CF144D1, original_name="Unknown"),
        },
    )
    unknown_0x7975982c: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7975982C, original_name="Unknown"),
        },
    )
    unknown_0x460b2702: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x460B2702, original_name="Unknown"),
        },
    )
    unknown_0x43c8a56e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x43C8A56E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x83f19d56: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x83F19D56, original_name="Unknown"),
        },
    )
    unknown_0xa9cd091f: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA9CD091F, original_name="Unknown"),
        },
    )
    unknown_0xe589a4f9: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE589A4F9, original_name="Unknown"),
        },
    )
    unknown_0xd7cf6cc5: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD7CF6CC5, original_name="Unknown"),
        },
    )
    unknown_0x85e956d3: float = dataclasses.field(
        default=0.8999999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0x85E956D3, original_name="Unknown"),
        },
    )
    unknown_0xa6f2b827: float = dataclasses.field(
        default=135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA6F2B827, original_name="Unknown"),
        },
    )
    unknown_0xca637bcd: float = dataclasses.field(
        default=0.3499999940395355,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCA637BCD, original_name="Unknown"),
        },
    )
    unknown_0xf04414b3: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF04414B3, original_name="Unknown"),
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
        if property_count != 33:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHfLHffffLHffffLHffffLHffffLHfffLHfLHfLHfLHfLHfLHfLHffffLHffffLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHffffLHfLHfLHfLHfLHfLHfLHfLHf"
            )

        dec = _FAST_FORMAT.unpack(data.read(422))
        assert (
            dec[0],
            dec[3],
            dec[9],
            dec[15],
            dec[21],
            dec[27],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[56],
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
            dec[98],
            dec[101],
            dec[104],
            dec[107],
            dec[110],
            dec[113],
            dec[116],
            dec[119],
        ) == _FAST_IDS
        return cls(
            dec[2],
            Color(*dec[5:9]),
            Color(*dec[11:15]),
            Color(*dec[17:21]),
            Color(*dec[23:27]),
            Vector(*dec[29:32]),
            dec[34],
            dec[37],
            dec[40],
            dec[43],
            dec[46],
            dec[49],
            Color(*dec[52:56]),
            Color(*dec[58:62]),
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
            Color(*dec[94:98]),
            dec[100],
            dec[103],
            dec[106],
            dec[109],
            dec[112],
            dec[115],
            dec[118],
            dec[121],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00!")  # 33 properties

        data.write(b"w\xfe\xee\xf0")  # 0x77feeef0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x77feeef0))

        data.write(b"lh\x98\x1b")  # 0x6c68981b
        data.write(b"\x00\x10")  # size
        self.unknown_0x6c68981b.to_stream(data, game)

        data.write(b"m[\xc9\xc5")  # 0x6d5bc9c5
        data.write(b"\x00\x10")  # size
        self.orbit_lock_color.to_stream(data, game)

        data.write(b"\x1b\x90]\xfe")  # 0x1b905dfe
        data.write(b"\x00\x10")  # size
        self.unknown_0x1b905dfe.to_stream(data, game)

        data.write(b"\x05\xee\x18\xe2")  # 0x5ee18e2
        data.write(b"\x00\x10")  # size
        self.unknown_0x05ee18e2.to_stream(data, game)

        data.write(b"3~`\xa9")  # 0x337e60a9
        data.write(b"\x00\x0c")  # size
        self.unknown_0x337e60a9.to_stream(data, game)

        data.write(b"OcPQ")  # 0x4f635051
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f635051))

        data.write(b" \xafhp")  # 0x20af6870
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x20af6870))

        data.write(b"\nXH\xfb")  # 0xa5848fb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a5848fb))

        data.write(b"\x01\xb6K\xdf")  # 0x1b64bdf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x01b64bdf))

        data.write(b"\xd4\x04Ei")  # 0xd4044569
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd4044569))

        data.write(b"\xaelRa")  # 0xae6c5261
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xae6c5261))

        data.write(b"\x84\xac>\xee")  # 0x84ac3eee
        data.write(b"\x00\x10")  # size
        self.unknown_0x84ac3eee.to_stream(data, game)

        data.write(b"9m\x00\x1e")  # 0x396d001e
        data.write(b"\x00\x10")  # size
        self.unknown_0x396d001e.to_stream(data, game)

        data.write(b"\xe8\x00\x8f\xa5")  # 0xe8008fa5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8008fa5))

        data.write(b"\xe9\xc1\x16\xbf")  # 0xe9c116bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe9c116bf))

        data.write(b"y\xf1\x85H")  # 0x79f18548
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x79f18548))

        data.write(b"&\x97\x8cK")  # 0x26978c4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x26978c4b))

        data.write(b"\x9dX\xf8\x85")  # 0x9d58f885
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9d58f885))

        data.write(b"\x99\xc2\xc9\xaf")  # 0x99c2c9af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x99c2c9af))

        data.write(b"2i\x05\xf2")  # 0x326905f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x326905f2))

        data.write(b"<\xf1D\xd1")  # 0x3cf144d1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3cf144d1))

        data.write(b"yu\x98,")  # 0x7975982c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7975982c))

        data.write(b"F\x0b'\x02")  # 0x460b2702
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x460b2702))

        data.write(b"C\xc8\xa5n")  # 0x43c8a56e
        data.write(b"\x00\x10")  # size
        self.unknown_0x43c8a56e.to_stream(data, game)

        data.write(b"\x83\xf1\x9dV")  # 0x83f19d56
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x83f19d56))

        data.write(b"\xa9\xcd\t\x1f")  # 0xa9cd091f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa9cd091f))

        data.write(b"\xe5\x89\xa4\xf9")  # 0xe589a4f9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe589a4f9))

        data.write(b"\xd7\xcfl\xc5")  # 0xd7cf6cc5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd7cf6cc5))

        data.write(b"\x85\xe9V\xd3")  # 0x85e956d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x85e956d3))

        data.write(b"\xa6\xf2\xb8'")  # 0xa6f2b827
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa6f2b827))

        data.write(b"\xcac{\xcd")  # 0xca637bcd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xca637bcd))

        data.write(b"\xf0D\x14\xb3")  # 0xf04414b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf04414b3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_UnknownStruct3Json", data)
        return cls(
            unknown_0x77feeef0=json_data["unknown_0x77feeef0"],
            unknown_0x6c68981b=Color.from_json(json_data["unknown_0x6c68981b"]),
            orbit_lock_color=Color.from_json(json_data["orbit_lock_color"]),
            unknown_0x1b905dfe=Color.from_json(json_data["unknown_0x1b905dfe"]),
            unknown_0x05ee18e2=Color.from_json(json_data["unknown_0x05ee18e2"]),
            unknown_0x337e60a9=Vector.from_json(json_data["unknown_0x337e60a9"]),
            unknown_0x4f635051=json_data["unknown_0x4f635051"],
            unknown_0x20af6870=json_data["unknown_0x20af6870"],
            unknown_0x0a5848fb=json_data["unknown_0x0a5848fb"],
            unknown_0x01b64bdf=json_data["unknown_0x01b64bdf"],
            unknown_0xd4044569=json_data["unknown_0xd4044569"],
            unknown_0xae6c5261=json_data["unknown_0xae6c5261"],
            unknown_0x84ac3eee=Color.from_json(json_data["unknown_0x84ac3eee"]),
            unknown_0x396d001e=Color.from_json(json_data["unknown_0x396d001e"]),
            unknown_0xe8008fa5=json_data["unknown_0xe8008fa5"],
            unknown_0xe9c116bf=json_data["unknown_0xe9c116bf"],
            unknown_0x79f18548=json_data["unknown_0x79f18548"],
            unknown_0x26978c4b=json_data["unknown_0x26978c4b"],
            unknown_0x9d58f885=json_data["unknown_0x9d58f885"],
            unknown_0x99c2c9af=json_data["unknown_0x99c2c9af"],
            unknown_0x326905f2=json_data["unknown_0x326905f2"],
            unknown_0x3cf144d1=json_data["unknown_0x3cf144d1"],
            unknown_0x7975982c=json_data["unknown_0x7975982c"],
            unknown_0x460b2702=json_data["unknown_0x460b2702"],
            unknown_0x43c8a56e=Color.from_json(json_data["unknown_0x43c8a56e"]),
            unknown_0x83f19d56=json_data["unknown_0x83f19d56"],
            unknown_0xa9cd091f=json_data["unknown_0xa9cd091f"],
            unknown_0xe589a4f9=json_data["unknown_0xe589a4f9"],
            unknown_0xd7cf6cc5=json_data["unknown_0xd7cf6cc5"],
            unknown_0x85e956d3=json_data["unknown_0x85e956d3"],
            unknown_0xa6f2b827=json_data["unknown_0xa6f2b827"],
            unknown_0xca637bcd=json_data["unknown_0xca637bcd"],
            unknown_0xf04414b3=json_data["unknown_0xf04414b3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x77feeef0": self.unknown_0x77feeef0,
            "unknown_0x6c68981b": self.unknown_0x6c68981b.to_json(),
            "orbit_lock_color": self.orbit_lock_color.to_json(),
            "unknown_0x1b905dfe": self.unknown_0x1b905dfe.to_json(),
            "unknown_0x05ee18e2": self.unknown_0x05ee18e2.to_json(),
            "unknown_0x337e60a9": self.unknown_0x337e60a9.to_json(),
            "unknown_0x4f635051": self.unknown_0x4f635051,
            "unknown_0x20af6870": self.unknown_0x20af6870,
            "unknown_0x0a5848fb": self.unknown_0x0a5848fb,
            "unknown_0x01b64bdf": self.unknown_0x01b64bdf,
            "unknown_0xd4044569": self.unknown_0xd4044569,
            "unknown_0xae6c5261": self.unknown_0xae6c5261,
            "unknown_0x84ac3eee": self.unknown_0x84ac3eee.to_json(),
            "unknown_0x396d001e": self.unknown_0x396d001e.to_json(),
            "unknown_0xe8008fa5": self.unknown_0xe8008fa5,
            "unknown_0xe9c116bf": self.unknown_0xe9c116bf,
            "unknown_0x79f18548": self.unknown_0x79f18548,
            "unknown_0x26978c4b": self.unknown_0x26978c4b,
            "unknown_0x9d58f885": self.unknown_0x9d58f885,
            "unknown_0x99c2c9af": self.unknown_0x99c2c9af,
            "unknown_0x326905f2": self.unknown_0x326905f2,
            "unknown_0x3cf144d1": self.unknown_0x3cf144d1,
            "unknown_0x7975982c": self.unknown_0x7975982c,
            "unknown_0x460b2702": self.unknown_0x460b2702,
            "unknown_0x43c8a56e": self.unknown_0x43c8a56e.to_json(),
            "unknown_0x83f19d56": self.unknown_0x83f19d56,
            "unknown_0xa9cd091f": self.unknown_0xa9cd091f,
            "unknown_0xe589a4f9": self.unknown_0xe589a4f9,
            "unknown_0xd7cf6cc5": self.unknown_0xd7cf6cc5,
            "unknown_0x85e956d3": self.unknown_0x85e956d3,
            "unknown_0xa6f2b827": self.unknown_0xa6f2b827,
            "unknown_0xca637bcd": self.unknown_0xca637bcd,
            "unknown_0xf04414b3": self.unknown_0xf04414b3,
        }


def _decode_unknown_0x6c68981b(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x1b905dfe(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x05ee18e2(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x337e60a9(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0x84ac3eee(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x396d001e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x43c8a56e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x77FEEEF0: ("unknown_0x77feeef0", structs.decode_BIG_f),
    0x6C68981B: ("unknown_0x6c68981b", _decode_unknown_0x6c68981b),
    0x6D5BC9C5: ("orbit_lock_color", _decode_orbit_lock_color),
    0x1B905DFE: ("unknown_0x1b905dfe", _decode_unknown_0x1b905dfe),
    0x05EE18E2: ("unknown_0x05ee18e2", _decode_unknown_0x05ee18e2),
    0x337E60A9: ("unknown_0x337e60a9", _decode_unknown_0x337e60a9),
    0x4F635051: ("unknown_0x4f635051", structs.decode_BIG_f),
    0x20AF6870: ("unknown_0x20af6870", structs.decode_BIG_f),
    0x0A5848FB: ("unknown_0x0a5848fb", structs.decode_BIG_f),
    0x01B64BDF: ("unknown_0x01b64bdf", structs.decode_BIG_f),
    0xD4044569: ("unknown_0xd4044569", structs.decode_BIG_f),
    0xAE6C5261: ("unknown_0xae6c5261", structs.decode_BIG_f),
    0x84AC3EEE: ("unknown_0x84ac3eee", _decode_unknown_0x84ac3eee),
    0x396D001E: ("unknown_0x396d001e", _decode_unknown_0x396d001e),
    0xE8008FA5: ("unknown_0xe8008fa5", structs.decode_BIG_f),
    0xE9C116BF: ("unknown_0xe9c116bf", structs.decode_BIG_f),
    0x79F18548: ("unknown_0x79f18548", structs.decode_BIG_f),
    0x26978C4B: ("unknown_0x26978c4b", structs.decode_BIG_f),
    0x9D58F885: ("unknown_0x9d58f885", structs.decode_BIG_f),
    0x99C2C9AF: ("unknown_0x99c2c9af", structs.decode_BIG_f),
    0x326905F2: ("unknown_0x326905f2", structs.decode_BIG_f),
    0x3CF144D1: ("unknown_0x3cf144d1", structs.decode_BIG_f),
    0x7975982C: ("unknown_0x7975982c", structs.decode_BIG_f),
    0x460B2702: ("unknown_0x460b2702", structs.decode_BIG_f),
    0x43C8A56E: ("unknown_0x43c8a56e", _decode_unknown_0x43c8a56e),
    0x83F19D56: ("unknown_0x83f19d56", structs.decode_BIG_f),
    0xA9CD091F: ("unknown_0xa9cd091f", structs.decode_BIG_f),
    0xE589A4F9: ("unknown_0xe589a4f9", structs.decode_BIG_f),
    0xD7CF6CC5: ("unknown_0xd7cf6cc5", structs.decode_BIG_f),
    0x85E956D3: ("unknown_0x85e956d3", structs.decode_BIG_f),
    0xA6F2B827: ("unknown_0xa6f2b827", structs.decode_BIG_f),
    0xCA637BCD: ("unknown_0xca637bcd", structs.decode_BIG_f),
    0xF04414B3: ("unknown_0xf04414b3", structs.decode_BIG_f),
}
