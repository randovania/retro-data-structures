# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakGui_CreditsJson(typing_extensions.TypedDict):
        unknown_0x81fc78c2: str
        unknown_0x2bcd300d: str
        alternate_font: str
        font_color: json_util.JsonValue
        font_outline_color: json_util.JsonValue
        total_time: float
        text_fade_time: float
        movie_fade_time: float


@dataclasses.dataclass()
class TweakGui_Credits(BaseProperty):
    unknown_0x81fc78c2: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x81FC78C2, original_name="Unknown"),
        },
    )
    unknown_0x2bcd300d: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x2BCD300D, original_name="Unknown"),
        },
    )
    alternate_font: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xCEF90C00, original_name="AlternateFont"),
        },
    )
    font_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1A96EC67, original_name="FontColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    font_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x844AB6B0, original_name="FontOutlineColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    total_time: float = dataclasses.field(
        default=191.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x19686BF6, original_name="TotalTime"),
        },
    )
    text_fade_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x52985AD1, original_name="TextFadeTime"),
        },
    )
    movie_fade_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0F977E6, original_name="MovieFadeTime"),
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
        if property_count != 8:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81FC78C2
        unknown_0x81fc78c2 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BCD300D
        unknown_0x2bcd300d = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEF90C00
        alternate_font = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A96EC67
        font_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x844AB6B0
        font_outline_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19686BF6
        total_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52985AD1
        text_fade_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0F977E6
        movie_fade_time = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            unknown_0x81fc78c2,
            unknown_0x2bcd300d,
            alternate_font,
            font_color,
            font_outline_color,
            total_time,
            text_fade_time,
            movie_fade_time,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\x81\xfcx\xc2")  # 0x81fc78c2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x81fc78c2.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+\xcd0\r")  # 0x2bcd300d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x2bcd300d.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xce\xf9\x0c\x00")  # 0xcef90c00
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.alternate_font.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1a\x96\xecg")  # 0x1a96ec67
        data.write(b"\x00\x10")  # size
        self.font_color.to_stream(data, game)

        data.write(b"\x84J\xb6\xb0")  # 0x844ab6b0
        data.write(b"\x00\x10")  # size
        self.font_outline_color.to_stream(data, game)

        data.write(b"\x19hk\xf6")  # 0x19686bf6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.total_time))

        data.write(b"R\x98Z\xd1")  # 0x52985ad1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.text_fade_time))

        data.write(b"\xf0\xf9w\xe6")  # 0xf0f977e6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movie_fade_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_CreditsJson", data)
        return cls(
            unknown_0x81fc78c2=json_data["unknown_0x81fc78c2"],
            unknown_0x2bcd300d=json_data["unknown_0x2bcd300d"],
            alternate_font=json_data["alternate_font"],
            font_color=Color.from_json(json_data["font_color"]),
            font_outline_color=Color.from_json(json_data["font_outline_color"]),
            total_time=json_data["total_time"],
            text_fade_time=json_data["text_fade_time"],
            movie_fade_time=json_data["movie_fade_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x81fc78c2": self.unknown_0x81fc78c2,
            "unknown_0x2bcd300d": self.unknown_0x2bcd300d,
            "alternate_font": self.alternate_font,
            "font_color": self.font_color.to_json(),
            "font_outline_color": self.font_outline_color.to_json(),
            "total_time": self.total_time,
            "text_fade_time": self.text_fade_time,
            "movie_fade_time": self.movie_fade_time,
        }


def _decode_unknown_0x81fc78c2(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x2bcd300d(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_alternate_font(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_font_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_font_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x81FC78C2: ("unknown_0x81fc78c2", _decode_unknown_0x81fc78c2),
    0x2BCD300D: ("unknown_0x2bcd300d", _decode_unknown_0x2bcd300d),
    0xCEF90C00: ("alternate_font", _decode_alternate_font),
    0x1A96EC67: ("font_color", _decode_font_color),
    0x844AB6B0: ("font_outline_color", _decode_font_outline_color),
    0x19686BF6: ("total_time", structs.decode_BIG_f),
    0x52985AD1: ("text_fade_time", structs.decode_BIG_f),
    0xF0F977E6: ("movie_fade_time", structs.decode_BIG_f),
}
