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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TextPropertiesJson(typing_extensions.TypedDict):
        text_bounding_width: int
        text_bounding_height: int
        line_spacing: float
        line_extra_space: int
        character_extra_space: int
        foreground_color: json_util.JsonValue
        outline_color: json_util.JsonValue
        geometry_color: json_util.JsonValue
        default_font: int
        unknown_0x18dd95cd: int
        unknown_0x42091548: int
        wrap_text: bool
        draw_shadow: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xEE521DC6,
    0xF2D36ABB,
    0x1A996292,
    0x5EFF913,
    0x45830901,
    0x3F39E635,
    0x60D78569,
    0x5908EF39,
    0xDB9F8B6,
    0x18DD95CD,
    0x42091548,
    0x330573E9,
    0xD8A2EEF0,
)


@dataclasses.dataclass()
class TextProperties(BaseProperty):
    text_bounding_width: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEE521DC6, original_name="TextBoundingWidth"),
        },
    )
    text_bounding_height: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF2D36ABB, original_name="TextBoundingHeight"),
        },
    )
    line_spacing: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A996292, original_name="LineSpacing"),
        },
    )
    line_extra_space: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x05EFF913, original_name="LineExtraSpace"),
        },
    )
    character_extra_space: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x45830901, original_name="CharacterExtraSpace"),
        },
    )
    foreground_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x3F39E635, original_name="ForegroundColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x60D78569, original_name="OutlineColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    geometry_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5908EF39, original_name="GeometryColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    default_font: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["FONT"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0DB9F8B6, original_name="DefaultFont"),
        },
    )
    unknown_0x18dd95cd: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x18DD95CD, original_name="Unknown"),
        },
    )
    unknown_0x42091548: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42091548, original_name="Unknown"),
        },
    )
    wrap_text: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x330573E9, original_name="WrapText"),
        },
    )
    draw_shadow: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xD8A2EEF0, original_name="DrawShadow"),
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
        if property_count != 13:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHlLHfLHlLHlLHffffLHffffLHffffLHQLHlLHlLH?LH?")

        dec = _FAST_FORMAT.unpack(data.read(164))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[21],
            dec[27],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            Color(*dec[17:21]),
            Color(*dec[23:27]),
            Color(*dec[29:33]),
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\r")  # 13 properties

        data.write(b"\xeeR\x1d\xc6")  # 0xee521dc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.text_bounding_width))

        data.write(b"\xf2\xd3j\xbb")  # 0xf2d36abb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.text_bounding_height))

        data.write(b"\x1a\x99b\x92")  # 0x1a996292
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.line_spacing))

        data.write(b"\x05\xef\xf9\x13")  # 0x5eff913
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.line_extra_space))

        data.write(b"E\x83\t\x01")  # 0x45830901
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.character_extra_space))

        data.write(b"?9\xe65")  # 0x3f39e635
        data.write(b"\x00\x10")  # size
        self.foreground_color.to_stream(data, game)

        data.write(b"`\xd7\x85i")  # 0x60d78569
        data.write(b"\x00\x10")  # size
        self.outline_color.to_stream(data, game)

        data.write(b"Y\x08\xef9")  # 0x5908ef39
        data.write(b"\x00\x10")  # size
        self.geometry_color.to_stream(data, game)

        data.write(b"\r\xb9\xf8\xb6")  # 0xdb9f8b6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.default_font))

        data.write(b"\x18\xdd\x95\xcd")  # 0x18dd95cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x18dd95cd))

        data.write(b"B\t\x15H")  # 0x42091548
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x42091548))

        data.write(b"3\x05s\xe9")  # 0x330573e9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.wrap_text))

        data.write(b"\xd8\xa2\xee\xf0")  # 0xd8a2eef0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.draw_shadow))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TextPropertiesJson", data)
        return cls(
            text_bounding_width=json_data["text_bounding_width"],
            text_bounding_height=json_data["text_bounding_height"],
            line_spacing=json_data["line_spacing"],
            line_extra_space=json_data["line_extra_space"],
            character_extra_space=json_data["character_extra_space"],
            foreground_color=Color.from_json(json_data["foreground_color"]),
            outline_color=Color.from_json(json_data["outline_color"]),
            geometry_color=Color.from_json(json_data["geometry_color"]),
            default_font=json_data["default_font"],
            unknown_0x18dd95cd=json_data["unknown_0x18dd95cd"],
            unknown_0x42091548=json_data["unknown_0x42091548"],
            wrap_text=json_data["wrap_text"],
            draw_shadow=json_data["draw_shadow"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "text_bounding_width": self.text_bounding_width,
            "text_bounding_height": self.text_bounding_height,
            "line_spacing": self.line_spacing,
            "line_extra_space": self.line_extra_space,
            "character_extra_space": self.character_extra_space,
            "foreground_color": self.foreground_color.to_json(),
            "outline_color": self.outline_color.to_json(),
            "geometry_color": self.geometry_color.to_json(),
            "default_font": self.default_font,
            "unknown_0x18dd95cd": self.unknown_0x18dd95cd,
            "unknown_0x42091548": self.unknown_0x42091548,
            "wrap_text": self.wrap_text,
            "draw_shadow": self.draw_shadow,
        }


def _decode_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_geometry_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xEE521DC6: ("text_bounding_width", structs.decode_BIG_l),
    0xF2D36ABB: ("text_bounding_height", structs.decode_BIG_l),
    0x1A996292: ("line_spacing", structs.decode_BIG_f),
    0x05EFF913: ("line_extra_space", structs.decode_BIG_l),
    0x45830901: ("character_extra_space", structs.decode_BIG_l),
    0x3F39E635: ("foreground_color", _decode_foreground_color),
    0x60D78569: ("outline_color", _decode_outline_color),
    0x5908EF39: ("geometry_color", _decode_geometry_color),
    0x0DB9F8B6: ("default_font", structs.decode_BIG_Q),
    0x18DD95CD: ("unknown_0x18dd95cd", structs.decode_BIG_l),
    0x42091548: ("unknown_0x42091548", structs.decode_BIG_l),
    0x330573E9: ("wrap_text", structs.decode_BIG_bool_),
    0xD8A2EEF0: ("draw_shadow", structs.decode_BIG_bool_),
}
