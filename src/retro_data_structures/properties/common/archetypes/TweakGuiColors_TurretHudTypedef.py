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

    class TweakGuiColors_TurretHudTypedefJson(typing_extensions.TypedDict):
        frame_color: json_util.JsonValue
        font_color: json_util.JsonValue
        font_outline_color: json_util.JsonValue
        energy_bar_fill_color: json_util.JsonValue
        energy_bar_shadow_color: json_util.JsonValue
        energy_bar_empty_color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xA485372C, 0x1A96EC67, 0x844AB6B0, 0xBDB697A9, 0xB9A9FC6E, 0x37E381C2)


@dataclasses.dataclass()
class TweakGuiColors_TurretHudTypedef(BaseProperty):
    frame_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA485372C, original_name="FrameColor", from_json=Color.from_json, to_json=Color.to_json
            ),
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
    energy_bar_fill_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xBDB697A9,
                original_name="EnergyBarFillColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    energy_bar_shadow_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xB9A9FC6E,
                original_name="EnergyBarShadowColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    energy_bar_empty_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x37E381C2,
                original_name="EnergyBarEmptyColor",
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
        if property_count != 6:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHffffLHffffLHffffLHffffLHffffLHffff")

        dec = _FAST_FORMAT.unpack(data.read(132))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            Color(*dec[26:30]),
            Color(*dec[32:36]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"\xa4\x857,")  # 0xa485372c
        data.write(b"\x00\x10")  # size
        self.frame_color.to_stream(data, game)

        data.write(b"\x1a\x96\xecg")  # 0x1a96ec67
        data.write(b"\x00\x10")  # size
        self.font_color.to_stream(data, game)

        data.write(b"\x84J\xb6\xb0")  # 0x844ab6b0
        data.write(b"\x00\x10")  # size
        self.font_outline_color.to_stream(data, game)

        data.write(b"\xbd\xb6\x97\xa9")  # 0xbdb697a9
        data.write(b"\x00\x10")  # size
        self.energy_bar_fill_color.to_stream(data, game)

        data.write(b"\xb9\xa9\xfcn")  # 0xb9a9fc6e
        data.write(b"\x00\x10")  # size
        self.energy_bar_shadow_color.to_stream(data, game)

        data.write(b"7\xe3\x81\xc2")  # 0x37e381c2
        data.write(b"\x00\x10")  # size
        self.energy_bar_empty_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGuiColors_TurretHudTypedefJson", data)
        return cls(
            frame_color=Color.from_json(json_data["frame_color"]),
            font_color=Color.from_json(json_data["font_color"]),
            font_outline_color=Color.from_json(json_data["font_outline_color"]),
            energy_bar_fill_color=Color.from_json(json_data["energy_bar_fill_color"]),
            energy_bar_shadow_color=Color.from_json(json_data["energy_bar_shadow_color"]),
            energy_bar_empty_color=Color.from_json(json_data["energy_bar_empty_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "frame_color": self.frame_color.to_json(),
            "font_color": self.font_color.to_json(),
            "font_outline_color": self.font_outline_color.to_json(),
            "energy_bar_fill_color": self.energy_bar_fill_color.to_json(),
            "energy_bar_shadow_color": self.energy_bar_shadow_color.to_json(),
            "energy_bar_empty_color": self.energy_bar_empty_color.to_json(),
        }


def _decode_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_font_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_font_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_fill_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA485372C: ("frame_color", _decode_frame_color),
    0x1A96EC67: ("font_color", _decode_font_color),
    0x844AB6B0: ("font_outline_color", _decode_font_outline_color),
    0xBDB697A9: ("energy_bar_fill_color", _decode_energy_bar_fill_color),
    0xB9A9FC6E: ("energy_bar_shadow_color", _decode_energy_bar_shadow_color),
    0x37E381C2: ("energy_bar_empty_color", _decode_energy_bar_empty_color),
}
