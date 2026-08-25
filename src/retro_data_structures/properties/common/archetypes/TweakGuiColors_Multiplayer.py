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

    class TweakGuiColors_MultiplayerJson(typing_extensions.TypedDict):
        score_text_color: json_util.JsonValue
        unknown_0xa09caefe: json_util.JsonValue
        timer_text_color: json_util.JsonValue
        timer_text_blink_color: json_util.JsonValue
        unknown_0xec4197e3: json_util.JsonValue
        unknown_0x823e2fb3: json_util.JsonValue
        unknown_0x95cc4ed8: json_util.JsonValue
        unknown_0xdb2ca6ff: json_util.JsonValue
        lockon_indicator_on_color: json_util.JsonValue
        lockon_indicator_off_color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x23CAC744,
    0xA09CAEFE,
    0x6BF04FF9,
    0x4280D00A,
    0xEC4197E3,
    0x823E2FB3,
    0x95CC4ED8,
    0xDB2CA6FF,
    0x3D27FFD,
    0x4C215775,
)


@dataclasses.dataclass()
class TweakGuiColors_Multiplayer(BaseProperty):
    score_text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x23CAC744, original_name="ScoreTextColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xa09caefe: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA09CAEFE, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    timer_text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6BF04FF9, original_name="TimerTextColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    timer_text_blink_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x4280D00A,
                original_name="TimerTextBlinkColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xec4197e3: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xEC4197E3, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x823e2fb3: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x823E2FB3, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x95cc4ed8: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x95CC4ED8, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdb2ca6ff: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDB2CA6FF, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    lockon_indicator_on_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x03D27FFD,
                original_name="LockonIndicatorOnColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    lockon_indicator_off_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x4C215775,
                original_name="LockonIndicatorOffColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
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
        if property_count != 10:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffff")

        dec = _FAST_FORMAT.unpack(data.read(220))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30], dec[36], dec[42], dec[48], dec[54]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            Color(*dec[26:30]),
            Color(*dec[32:36]),
            Color(*dec[38:42]),
            Color(*dec[44:48]),
            Color(*dec[50:54]),
            Color(*dec[56:60]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"#\xca\xc7D")  # 0x23cac744
        data.write(b"\x00\x10")  # size
        self.score_text_color.to_stream(data, game)

        data.write(b"\xa0\x9c\xae\xfe")  # 0xa09caefe
        data.write(b"\x00\x10")  # size
        self.unknown_0xa09caefe.to_stream(data, game)

        data.write(b"k\xf0O\xf9")  # 0x6bf04ff9
        data.write(b"\x00\x10")  # size
        self.timer_text_color.to_stream(data, game)

        data.write(b"B\x80\xd0\n")  # 0x4280d00a
        data.write(b"\x00\x10")  # size
        self.timer_text_blink_color.to_stream(data, game)

        data.write(b"\xecA\x97\xe3")  # 0xec4197e3
        data.write(b"\x00\x10")  # size
        self.unknown_0xec4197e3.to_stream(data, game)

        data.write(b"\x82>/\xb3")  # 0x823e2fb3
        data.write(b"\x00\x10")  # size
        self.unknown_0x823e2fb3.to_stream(data, game)

        data.write(b"\x95\xccN\xd8")  # 0x95cc4ed8
        data.write(b"\x00\x10")  # size
        self.unknown_0x95cc4ed8.to_stream(data, game)

        data.write(b"\xdb,\xa6\xff")  # 0xdb2ca6ff
        data.write(b"\x00\x10")  # size
        self.unknown_0xdb2ca6ff.to_stream(data, game)

        data.write(b"\x03\xd2\x7f\xfd")  # 0x3d27ffd
        data.write(b"\x00\x10")  # size
        self.lockon_indicator_on_color.to_stream(data, game)

        data.write(b"L!Wu")  # 0x4c215775
        data.write(b"\x00\x10")  # size
        self.lockon_indicator_off_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGuiColors_MultiplayerJson", data)
        return cls(
            score_text_color=Color.from_json(json_data["score_text_color"]),
            unknown_0xa09caefe=Color.from_json(json_data["unknown_0xa09caefe"]),
            timer_text_color=Color.from_json(json_data["timer_text_color"]),
            timer_text_blink_color=Color.from_json(json_data["timer_text_blink_color"]),
            unknown_0xec4197e3=Color.from_json(json_data["unknown_0xec4197e3"]),
            unknown_0x823e2fb3=Color.from_json(json_data["unknown_0x823e2fb3"]),
            unknown_0x95cc4ed8=Color.from_json(json_data["unknown_0x95cc4ed8"]),
            unknown_0xdb2ca6ff=Color.from_json(json_data["unknown_0xdb2ca6ff"]),
            lockon_indicator_on_color=Color.from_json(json_data["lockon_indicator_on_color"]),
            lockon_indicator_off_color=Color.from_json(json_data["lockon_indicator_off_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "score_text_color": self.score_text_color.to_json(),
            "unknown_0xa09caefe": self.unknown_0xa09caefe.to_json(),
            "timer_text_color": self.timer_text_color.to_json(),
            "timer_text_blink_color": self.timer_text_blink_color.to_json(),
            "unknown_0xec4197e3": self.unknown_0xec4197e3.to_json(),
            "unknown_0x823e2fb3": self.unknown_0x823e2fb3.to_json(),
            "unknown_0x95cc4ed8": self.unknown_0x95cc4ed8.to_json(),
            "unknown_0xdb2ca6ff": self.unknown_0xdb2ca6ff.to_json(),
            "lockon_indicator_on_color": self.lockon_indicator_on_color.to_json(),
            "lockon_indicator_off_color": self.lockon_indicator_off_color.to_json(),
        }


def _decode_score_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xa09caefe(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_timer_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_timer_text_blink_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xec4197e3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x823e2fb3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x95cc4ed8(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdb2ca6ff(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_lockon_indicator_on_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_lockon_indicator_off_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x23CAC744: ("score_text_color", _decode_score_text_color),
    0xA09CAEFE: ("unknown_0xa09caefe", _decode_unknown_0xa09caefe),
    0x6BF04FF9: ("timer_text_color", _decode_timer_text_color),
    0x4280D00A: ("timer_text_blink_color", _decode_timer_text_blink_color),
    0xEC4197E3: ("unknown_0xec4197e3", _decode_unknown_0xec4197e3),
    0x823E2FB3: ("unknown_0x823e2fb3", _decode_unknown_0x823e2fb3),
    0x95CC4ED8: ("unknown_0x95cc4ed8", _decode_unknown_0x95cc4ed8),
    0xDB2CA6FF: ("unknown_0xdb2ca6ff", _decode_unknown_0xdb2ca6ff),
    0x03D27FFD: ("lockon_indicator_on_color", _decode_lockon_indicator_on_color),
    0x4C215775: ("lockon_indicator_off_color", _decode_lockon_indicator_off_color),
}
