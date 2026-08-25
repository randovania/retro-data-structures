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

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakGui_EchoVisorJson(typing_extensions.TypedDict):
        echo_base_color: json_util.JsonValue
        echo_outline_color: json_util.JsonValue
        echo_damage_color: json_util.JsonValue
        unknown_0xa288fe51: json_util.JsonValue
        unknown_0xf316c617: int
        unknown_0xb56d2286: float
        unknown_0xc5c2d8fc: float
        unknown_0x47d948b1: float
        unknown_0x5708b903: float
        unknown_0xafc8c571: float
        unknown_0x28bffdc5: float
        echo_ring_color: json_util.JsonValue
        unknown_0x99a65ca7: float
        unknown_0x51f19dea: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x905FA7E4,
    0x62CA2DDD,
    0xDC4C2A5F,
    0xA288FE51,
    0xF316C617,
    0xB56D2286,
    0xC5C2D8FC,
    0x47D948B1,
    0x5708B903,
    0xAFC8C571,
    0x28BFFDC5,
    0x66351D36,
    0x99A65CA7,
    0x51F19DEA,
)


@dataclasses.dataclass()
class TweakGui_EchoVisor(BaseProperty):
    echo_base_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x905FA7E4, original_name="EchoBaseColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    echo_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x62CA2DDD, original_name="EchoOutlineColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    echo_damage_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDC4C2A5F, original_name="EchoDamageColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xa288fe51: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA288FE51, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xf316c617: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF316C617, original_name="Unknown"),
        },
    )
    unknown_0xb56d2286: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB56D2286, original_name="Unknown"),
        },
    )
    unknown_0xc5c2d8fc: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC5C2D8FC, original_name="Unknown"),
        },
    )
    unknown_0x47d948b1: float = dataclasses.field(
        default=800.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47D948B1, original_name="Unknown"),
        },
    )
    unknown_0x5708b903: float = dataclasses.field(
        default=500.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5708B903, original_name="Unknown"),
        },
    )
    unknown_0xafc8c571: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAFC8C571, original_name="Unknown"),
        },
    )
    unknown_0x28bffdc5: float = dataclasses.field(
        default=0.8999999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0x28BFFDC5, original_name="Unknown"),
        },
    )
    echo_ring_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x66351D36, original_name="EchoRingColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x99a65ca7: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x99A65CA7, original_name="Unknown"),
        },
    )
    unknown_0x51f19dea: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x51F19DEA, original_name="Unknown"),
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
        if property_count != 14:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHffffLHffffLHffffLHffffLHlLHfLHfLHfLHfLHfLHfLHffffLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(200))
        assert (
            dec[0],
            dec[6],
            dec[12],
            dec[18],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[51],
            dec[54],
        ) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            Color(*dec[47:51]),
            dec[53],
            dec[56],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"\x90_\xa7\xe4")  # 0x905fa7e4
        data.write(b"\x00\x10")  # size
        self.echo_base_color.to_stream(data, game)

        data.write(b"b\xca-\xdd")  # 0x62ca2ddd
        data.write(b"\x00\x10")  # size
        self.echo_outline_color.to_stream(data, game)

        data.write(b"\xdcL*_")  # 0xdc4c2a5f
        data.write(b"\x00\x10")  # size
        self.echo_damage_color.to_stream(data, game)

        data.write(b"\xa2\x88\xfeQ")  # 0xa288fe51
        data.write(b"\x00\x10")  # size
        self.unknown_0xa288fe51.to_stream(data, game)

        data.write(b"\xf3\x16\xc6\x17")  # 0xf316c617
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xf316c617))

        data.write(b'\xb5m"\x86')  # 0xb56d2286
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb56d2286))

        data.write(b"\xc5\xc2\xd8\xfc")  # 0xc5c2d8fc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc5c2d8fc))

        data.write(b"G\xd9H\xb1")  # 0x47d948b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x47d948b1))

        data.write(b"W\x08\xb9\x03")  # 0x5708b903
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5708b903))

        data.write(b"\xaf\xc8\xc5q")  # 0xafc8c571
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xafc8c571))

        data.write(b"(\xbf\xfd\xc5")  # 0x28bffdc5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x28bffdc5))

        data.write(b"f5\x1d6")  # 0x66351d36
        data.write(b"\x00\x10")  # size
        self.echo_ring_color.to_stream(data, game)

        data.write(b"\x99\xa6\\\xa7")  # 0x99a65ca7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x99a65ca7))

        data.write(b"Q\xf1\x9d\xea")  # 0x51f19dea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x51f19dea))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_EchoVisorJson", data)
        return cls(
            echo_base_color=Color.from_json(json_data["echo_base_color"]),
            echo_outline_color=Color.from_json(json_data["echo_outline_color"]),
            echo_damage_color=Color.from_json(json_data["echo_damage_color"]),
            unknown_0xa288fe51=Color.from_json(json_data["unknown_0xa288fe51"]),
            unknown_0xf316c617=json_data["unknown_0xf316c617"],
            unknown_0xb56d2286=json_data["unknown_0xb56d2286"],
            unknown_0xc5c2d8fc=json_data["unknown_0xc5c2d8fc"],
            unknown_0x47d948b1=json_data["unknown_0x47d948b1"],
            unknown_0x5708b903=json_data["unknown_0x5708b903"],
            unknown_0xafc8c571=json_data["unknown_0xafc8c571"],
            unknown_0x28bffdc5=json_data["unknown_0x28bffdc5"],
            echo_ring_color=Color.from_json(json_data["echo_ring_color"]),
            unknown_0x99a65ca7=json_data["unknown_0x99a65ca7"],
            unknown_0x51f19dea=json_data["unknown_0x51f19dea"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "echo_base_color": self.echo_base_color.to_json(),
            "echo_outline_color": self.echo_outline_color.to_json(),
            "echo_damage_color": self.echo_damage_color.to_json(),
            "unknown_0xa288fe51": self.unknown_0xa288fe51.to_json(),
            "unknown_0xf316c617": self.unknown_0xf316c617,
            "unknown_0xb56d2286": self.unknown_0xb56d2286,
            "unknown_0xc5c2d8fc": self.unknown_0xc5c2d8fc,
            "unknown_0x47d948b1": self.unknown_0x47d948b1,
            "unknown_0x5708b903": self.unknown_0x5708b903,
            "unknown_0xafc8c571": self.unknown_0xafc8c571,
            "unknown_0x28bffdc5": self.unknown_0x28bffdc5,
            "echo_ring_color": self.echo_ring_color.to_json(),
            "unknown_0x99a65ca7": self.unknown_0x99a65ca7,
            "unknown_0x51f19dea": self.unknown_0x51f19dea,
        }


def _decode_echo_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xa288fe51(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_ring_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x905FA7E4: ("echo_base_color", _decode_echo_base_color),
    0x62CA2DDD: ("echo_outline_color", _decode_echo_outline_color),
    0xDC4C2A5F: ("echo_damage_color", _decode_echo_damage_color),
    0xA288FE51: ("unknown_0xa288fe51", _decode_unknown_0xa288fe51),
    0xF316C617: ("unknown_0xf316c617", structs.decode_BIG_l),
    0xB56D2286: ("unknown_0xb56d2286", structs.decode_BIG_f),
    0xC5C2D8FC: ("unknown_0xc5c2d8fc", structs.decode_BIG_f),
    0x47D948B1: ("unknown_0x47d948b1", structs.decode_BIG_f),
    0x5708B903: ("unknown_0x5708b903", structs.decode_BIG_f),
    0xAFC8C571: ("unknown_0xafc8c571", structs.decode_BIG_f),
    0x28BFFDC5: ("unknown_0x28bffdc5", structs.decode_BIG_f),
    0x66351D36: ("echo_ring_color", _decode_echo_ring_color),
    0x99A65CA7: ("unknown_0x99a65ca7", structs.decode_BIG_f),
    0x51F19DEA: ("unknown_0x51f19dea", structs.decode_BIG_f),
}
