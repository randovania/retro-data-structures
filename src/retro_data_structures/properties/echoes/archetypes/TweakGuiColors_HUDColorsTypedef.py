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

    class TweakGuiColors_HUDColorsTypedefJson(typing_extensions.TypedDict):
        unknown_0xc8ddc662: json_util.JsonValue
        threat_group_active_color: json_util.JsonValue
        threat_group_inactive_color: json_util.JsonValue
        unknown_0xa6609cc5: json_util.JsonValue
        missile_group_active_color: json_util.JsonValue
        missile_group_inactive_color: json_util.JsonValue
        unknown_0xdcaab836: json_util.JsonValue
        energy_bar_filled_color: json_util.JsonValue
        energy_bar_shadow_color: json_util.JsonValue
        energy_bar_empty_color: json_util.JsonValue
        energy_tanks_filled_color: json_util.JsonValue
        energy_tanks_empty_color: json_util.JsonValue
        radar_widget_color: json_util.JsonValue
        active_text_foreground_color: json_util.JsonValue
        inactive_text_foreground_color: json_util.JsonValue
        text_shadow_outline_color: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xC8DDC662,
    0x2F3CACAF,
    0x74E5FFA1,
    0xA6609CC5,
    0xCBB3FB76,
    0xD110A12F,
    0xDCAAB836,
    0xACF62D93,
    0xB9A9FC6E,
    0x37E381C2,
    0x4377E677,
    0x63384F81,
    0xA709DB40,
    0xAA4A5604,
    0x6CCCDF8F,
    0xDAA7D80,
)


@dataclasses.dataclass()
class TweakGuiColors_HUDColorsTypedef(BaseProperty):
    unknown_0xc8ddc662: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xC8DDC662, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    threat_group_active_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x2F3CACAF,
                original_name="ThreatGroupActiveColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    threat_group_inactive_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x74E5FFA1,
                original_name="ThreatGroupInactiveColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xa6609cc5: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA6609CC5, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    missile_group_active_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xCBB3FB76,
                original_name="MissileGroupActiveColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    missile_group_inactive_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xD110A12F,
                original_name="MissileGroupInactiveColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xdcaab836: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDCAAB836, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_bar_filled_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xACF62D93,
                original_name="EnergyBarFilledColor",
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
    energy_tanks_filled_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x4377E677,
                original_name="EnergyTanksFilledColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    energy_tanks_empty_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x63384F81,
                original_name="EnergyTanksEmptyColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    radar_widget_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA709DB40, original_name="RadarWidgetColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    active_text_foreground_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xAA4A5604,
                original_name="ActiveTextForegroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    inactive_text_foreground_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x6CCCDF8F,
                original_name="InactiveTextForegroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    text_shadow_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x0DAA7D80,
                original_name="TextShadowOutlineColor",
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
        if property_count != 16:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffff"
            )

        dec = _FAST_FORMAT.unpack(data.read(352))
        assert (
            dec[0],
            dec[6],
            dec[12],
            dec[18],
            dec[24],
            dec[30],
            dec[36],
            dec[42],
            dec[48],
            dec[54],
            dec[60],
            dec[66],
            dec[72],
            dec[78],
            dec[84],
            dec[90],
        ) == _FAST_IDS
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
            Color(*dec[62:66]),
            Color(*dec[68:72]),
            Color(*dec[74:78]),
            Color(*dec[80:84]),
            Color(*dec[86:90]),
            Color(*dec[92:96]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x10")  # 16 properties

        data.write(b"\xc8\xdd\xc6b")  # 0xc8ddc662
        data.write(b"\x00\x10")  # size
        self.unknown_0xc8ddc662.to_stream(data, game)

        data.write(b"/<\xac\xaf")  # 0x2f3cacaf
        data.write(b"\x00\x10")  # size
        self.threat_group_active_color.to_stream(data, game)

        data.write(b"t\xe5\xff\xa1")  # 0x74e5ffa1
        data.write(b"\x00\x10")  # size
        self.threat_group_inactive_color.to_stream(data, game)

        data.write(b"\xa6`\x9c\xc5")  # 0xa6609cc5
        data.write(b"\x00\x10")  # size
        self.unknown_0xa6609cc5.to_stream(data, game)

        data.write(b"\xcb\xb3\xfbv")  # 0xcbb3fb76
        data.write(b"\x00\x10")  # size
        self.missile_group_active_color.to_stream(data, game)

        data.write(b"\xd1\x10\xa1/")  # 0xd110a12f
        data.write(b"\x00\x10")  # size
        self.missile_group_inactive_color.to_stream(data, game)

        data.write(b"\xdc\xaa\xb86")  # 0xdcaab836
        data.write(b"\x00\x10")  # size
        self.unknown_0xdcaab836.to_stream(data, game)

        data.write(b"\xac\xf6-\x93")  # 0xacf62d93
        data.write(b"\x00\x10")  # size
        self.energy_bar_filled_color.to_stream(data, game)

        data.write(b"\xb9\xa9\xfcn")  # 0xb9a9fc6e
        data.write(b"\x00\x10")  # size
        self.energy_bar_shadow_color.to_stream(data, game)

        data.write(b"7\xe3\x81\xc2")  # 0x37e381c2
        data.write(b"\x00\x10")  # size
        self.energy_bar_empty_color.to_stream(data, game)

        data.write(b"Cw\xe6w")  # 0x4377e677
        data.write(b"\x00\x10")  # size
        self.energy_tanks_filled_color.to_stream(data, game)

        data.write(b"c8O\x81")  # 0x63384f81
        data.write(b"\x00\x10")  # size
        self.energy_tanks_empty_color.to_stream(data, game)

        data.write(b"\xa7\t\xdb@")  # 0xa709db40
        data.write(b"\x00\x10")  # size
        self.radar_widget_color.to_stream(data, game)

        data.write(b"\xaaJV\x04")  # 0xaa4a5604
        data.write(b"\x00\x10")  # size
        self.active_text_foreground_color.to_stream(data, game)

        data.write(b"l\xcc\xdf\x8f")  # 0x6cccdf8f
        data.write(b"\x00\x10")  # size
        self.inactive_text_foreground_color.to_stream(data, game)

        data.write(b"\r\xaa}\x80")  # 0xdaa7d80
        data.write(b"\x00\x10")  # size
        self.text_shadow_outline_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGuiColors_HUDColorsTypedefJson", data)
        return cls(
            unknown_0xc8ddc662=Color.from_json(json_data["unknown_0xc8ddc662"]),
            threat_group_active_color=Color.from_json(json_data["threat_group_active_color"]),
            threat_group_inactive_color=Color.from_json(json_data["threat_group_inactive_color"]),
            unknown_0xa6609cc5=Color.from_json(json_data["unknown_0xa6609cc5"]),
            missile_group_active_color=Color.from_json(json_data["missile_group_active_color"]),
            missile_group_inactive_color=Color.from_json(json_data["missile_group_inactive_color"]),
            unknown_0xdcaab836=Color.from_json(json_data["unknown_0xdcaab836"]),
            energy_bar_filled_color=Color.from_json(json_data["energy_bar_filled_color"]),
            energy_bar_shadow_color=Color.from_json(json_data["energy_bar_shadow_color"]),
            energy_bar_empty_color=Color.from_json(json_data["energy_bar_empty_color"]),
            energy_tanks_filled_color=Color.from_json(json_data["energy_tanks_filled_color"]),
            energy_tanks_empty_color=Color.from_json(json_data["energy_tanks_empty_color"]),
            radar_widget_color=Color.from_json(json_data["radar_widget_color"]),
            active_text_foreground_color=Color.from_json(json_data["active_text_foreground_color"]),
            inactive_text_foreground_color=Color.from_json(json_data["inactive_text_foreground_color"]),
            text_shadow_outline_color=Color.from_json(json_data["text_shadow_outline_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xc8ddc662": self.unknown_0xc8ddc662.to_json(),
            "threat_group_active_color": self.threat_group_active_color.to_json(),
            "threat_group_inactive_color": self.threat_group_inactive_color.to_json(),
            "unknown_0xa6609cc5": self.unknown_0xa6609cc5.to_json(),
            "missile_group_active_color": self.missile_group_active_color.to_json(),
            "missile_group_inactive_color": self.missile_group_inactive_color.to_json(),
            "unknown_0xdcaab836": self.unknown_0xdcaab836.to_json(),
            "energy_bar_filled_color": self.energy_bar_filled_color.to_json(),
            "energy_bar_shadow_color": self.energy_bar_shadow_color.to_json(),
            "energy_bar_empty_color": self.energy_bar_empty_color.to_json(),
            "energy_tanks_filled_color": self.energy_tanks_filled_color.to_json(),
            "energy_tanks_empty_color": self.energy_tanks_empty_color.to_json(),
            "radar_widget_color": self.radar_widget_color.to_json(),
            "active_text_foreground_color": self.active_text_foreground_color.to_json(),
            "inactive_text_foreground_color": self.inactive_text_foreground_color.to_json(),
            "text_shadow_outline_color": self.text_shadow_outline_color.to_json(),
        }


def _decode_unknown_0xc8ddc662(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_group_active_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_group_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xa6609cc5(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_active_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdcaab836(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_tanks_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_tanks_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_radar_widget_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_active_text_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inactive_text_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_text_shadow_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC8DDC662: ("unknown_0xc8ddc662", _decode_unknown_0xc8ddc662),
    0x2F3CACAF: ("threat_group_active_color", _decode_threat_group_active_color),
    0x74E5FFA1: ("threat_group_inactive_color", _decode_threat_group_inactive_color),
    0xA6609CC5: ("unknown_0xa6609cc5", _decode_unknown_0xa6609cc5),
    0xCBB3FB76: ("missile_group_active_color", _decode_missile_group_active_color),
    0xD110A12F: ("missile_group_inactive_color", _decode_missile_group_inactive_color),
    0xDCAAB836: ("unknown_0xdcaab836", _decode_unknown_0xdcaab836),
    0xACF62D93: ("energy_bar_filled_color", _decode_energy_bar_filled_color),
    0xB9A9FC6E: ("energy_bar_shadow_color", _decode_energy_bar_shadow_color),
    0x37E381C2: ("energy_bar_empty_color", _decode_energy_bar_empty_color),
    0x4377E677: ("energy_tanks_filled_color", _decode_energy_tanks_filled_color),
    0x63384F81: ("energy_tanks_empty_color", _decode_energy_tanks_empty_color),
    0xA709DB40: ("radar_widget_color", _decode_radar_widget_color),
    0xAA4A5604: ("active_text_foreground_color", _decode_active_text_foreground_color),
    0x6CCCDF8F: ("inactive_text_foreground_color", _decode_inactive_text_foreground_color),
    0x0DAA7D80: ("text_shadow_outline_color", _decode_text_shadow_outline_color),
}
