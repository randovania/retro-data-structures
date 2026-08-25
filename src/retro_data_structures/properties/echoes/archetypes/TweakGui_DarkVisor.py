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

    class TweakGui_DarkVisorJson(typing_extensions.TypedDict):
        dark_world_base_color: json_util.JsonValue
        dark_visor_static_color: json_util.JsonValue
        dark_visor_palette_modulate: json_util.JsonValue
        dark_visor_blur_speed: float
        dark_visor_frame_top: int
        dark_visor_frame_height: int
        dark_visor_frame_left: int
        dark_visor_frame_width: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xC571A8C6, 0x93DB3352, 0x92F8C63A, 0xAF902412, 0xFC913090, 0xD275CEEE, 0xAA8047A0, 0x2773FBB3)


@dataclasses.dataclass()
class TweakGui_DarkVisor(BaseProperty):
    dark_world_base_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xC571A8C6,
                original_name="DarkWorldBaseColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    dark_visor_static_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x93DB3352,
                original_name="DarkVisorStaticColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    dark_visor_palette_modulate: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x92F8C63A,
                original_name="DarkVisorPaletteModulate",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    dark_visor_blur_speed: float = dataclasses.field(
        default=0.0625,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAF902412, original_name="DarkVisorBlurSpeed"),
        },
    )
    dark_visor_frame_top: int = dataclasses.field(
        default=100,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFC913090, original_name="DarkVisorFrameTop"),
        },
    )
    dark_visor_frame_height: int = dataclasses.field(
        default=248,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD275CEEE, original_name="DarkVisorFrameHeight"),
        },
    )
    dark_visor_frame_left: int = dataclasses.field(
        default=50,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAA8047A0, original_name="DarkVisorFrameLeft"),
        },
    )
    dark_visor_frame_width: int = dataclasses.field(
        default=540,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2773FBB3, original_name="DarkVisorFrameWidth"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHffffLHffffLHffffLHfLHlLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(116))
        assert (dec[0], dec[6], dec[12], dec[18], dec[21], dec[24], dec[27], dec[30]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\xc5q\xa8\xc6")  # 0xc571a8c6
        data.write(b"\x00\x10")  # size
        self.dark_world_base_color.to_stream(data, game)

        data.write(b"\x93\xdb3R")  # 0x93db3352
        data.write(b"\x00\x10")  # size
        self.dark_visor_static_color.to_stream(data, game)

        data.write(b"\x92\xf8\xc6:")  # 0x92f8c63a
        data.write(b"\x00\x10")  # size
        self.dark_visor_palette_modulate.to_stream(data, game)

        data.write(b"\xaf\x90$\x12")  # 0xaf902412
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dark_visor_blur_speed))

        data.write(b"\xfc\x910\x90")  # 0xfc913090
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_visor_frame_top))

        data.write(b"\xd2u\xce\xee")  # 0xd275ceee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_visor_frame_height))

        data.write(b"\xaa\x80G\xa0")  # 0xaa8047a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_visor_frame_left))

        data.write(b"'s\xfb\xb3")  # 0x2773fbb3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_visor_frame_width))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_DarkVisorJson", data)
        return cls(
            dark_world_base_color=Color.from_json(json_data["dark_world_base_color"]),
            dark_visor_static_color=Color.from_json(json_data["dark_visor_static_color"]),
            dark_visor_palette_modulate=Color.from_json(json_data["dark_visor_palette_modulate"]),
            dark_visor_blur_speed=json_data["dark_visor_blur_speed"],
            dark_visor_frame_top=json_data["dark_visor_frame_top"],
            dark_visor_frame_height=json_data["dark_visor_frame_height"],
            dark_visor_frame_left=json_data["dark_visor_frame_left"],
            dark_visor_frame_width=json_data["dark_visor_frame_width"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "dark_world_base_color": self.dark_world_base_color.to_json(),
            "dark_visor_static_color": self.dark_visor_static_color.to_json(),
            "dark_visor_palette_modulate": self.dark_visor_palette_modulate.to_json(),
            "dark_visor_blur_speed": self.dark_visor_blur_speed,
            "dark_visor_frame_top": self.dark_visor_frame_top,
            "dark_visor_frame_height": self.dark_visor_frame_height,
            "dark_visor_frame_left": self.dark_visor_frame_left,
            "dark_visor_frame_width": self.dark_visor_frame_width,
        }


def _decode_dark_world_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_visor_static_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_visor_palette_modulate(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC571A8C6: ("dark_world_base_color", _decode_dark_world_base_color),
    0x93DB3352: ("dark_visor_static_color", _decode_dark_visor_static_color),
    0x92F8C63A: ("dark_visor_palette_modulate", _decode_dark_visor_palette_modulate),
    0xAF902412: ("dark_visor_blur_speed", structs.decode_BIG_f),
    0xFC913090: ("dark_visor_frame_top", structs.decode_BIG_l),
    0xD275CEEE: ("dark_visor_frame_height", structs.decode_BIG_l),
    0xAA8047A0: ("dark_visor_frame_left", structs.decode_BIG_l),
    0x2773FBB3: ("dark_visor_frame_width", structs.decode_BIG_l),
}
