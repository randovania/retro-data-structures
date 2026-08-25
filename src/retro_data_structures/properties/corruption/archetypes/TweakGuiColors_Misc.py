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

    class TweakGuiColors_MiscJson(typing_extensions.TypedDict):
        unknown_0x8ed04c36: json_util.JsonValue
        unknown_0x94bb7ee5: json_util.JsonValue
        pause_screen_tweak_open_color: json_util.JsonValue
        unknown_0x415a81f8: json_util.JsonValue
        unknown_0xfe95100f: json_util.JsonValue
        pause_screen_fullscreen_bg_color: json_util.JsonValue
        unknown_0x66733e29: json_util.JsonValue
        pause_screen_frame_color: json_util.JsonValue
        pause_screen_icons_color: json_util.JsonValue
        pause_screen_text_color: json_util.JsonValue
        pause_screen_highlight_color: json_util.JsonValue
        pause_screen_helmet_color: json_util.JsonValue
        gui_cursor_color: json_util.JsonValue
        unknown_0xdb5c8a60: json_util.JsonValue
        unknown_0x166c22e0: json_util.JsonValue
        unknown_0xcec78e81: json_util.JsonValue
        unknown_0x91338f72: json_util.JsonValue
        hud_memo_text_foreground_color: json_util.JsonValue
        hud_memo_text_outline_color: json_util.JsonValue
        unknown_0xc8ddc662: json_util.JsonValue
        hud_glow_color: json_util.JsonValue
        unknown_0x5c336f85: json_util.JsonValue
        unknown_0xdefca700: json_util.JsonValue
        selected_visor_beam_color: json_util.JsonValue
        unselected_visor_beam_color: json_util.JsonValue
        energy_bar_low_filled_color: json_util.JsonValue
        energy_bar_low_shadow_color: json_util.JsonValue
        energy_bar_low_empty_color: json_util.JsonValue
        hud_damage_modulate_color: json_util.JsonValue
        damage_indicator_color: json_util.JsonValue
        hud_title_foreground_color: json_util.JsonValue
        hud_title_outline_color: json_util.JsonValue
        unknown_0xe7070332: json_util.JsonValue
        unknown_0x779c7b9c: json_util.JsonValue
        energy_warning_color: json_util.JsonValue
        missile_warning_color: json_util.JsonValue
        unknown_0x83040135: json_util.JsonValue
        unknown_0x3c1ae0ff: json_util.JsonValue
        missile_bar_shadow_color: json_util.JsonValue
        missile_bar_empty_color: json_util.JsonValue
        unknown_0xbe3c29a1: json_util.JsonValue
        missile_group_inactive_color: json_util.JsonValue
        missile_group_combo_charge_color: json_util.JsonValue
        unknown_0x4c5aff4f: json_util.JsonValue
        unknown_0x0b17b693: json_util.JsonValue
        unknown_0x8b0a4c90: json_util.JsonValue
        energy_warning_outline_color: json_util.JsonValue
        missile_warning_outline_color: json_util.JsonValue
        unknown_0x78522461: json_util.JsonValue
        flash_pass_color: json_util.JsonValue
        unknown_0x79ea6f12: json_util.JsonValue
        unknown_0xdc901206: json_util.JsonValue
        unknown_0xc54fa7bc: json_util.JsonValue
        unknown_0x18717fa7: json_util.JsonValue
        unknown_0x8b7d7378: json_util.JsonValue
        unknown_0x867b01a2: json_util.JsonValue
        unknown_0xc02eed79: json_util.JsonValue
        metroid_suck_pulse_color: json_util.JsonValue
        unknown_0xce7c9d8d: json_util.JsonValue
        energy_bar_damage_color: json_util.JsonValue
        unknown_0xafe2d45d: json_util.JsonValue
        x_ray_holo_grid_color: json_util.JsonValue
        x_ray_seeker_color: json_util.JsonValue
        x_ray_seeker_ticks_color: json_util.JsonValue
        x_ray_seeker_ticks_outer_color: json_util.JsonValue
        x_ray_top_puzzle_color: json_util.JsonValue
        x_ray_bottom_puzzle_color: json_util.JsonValue
        x_ray_left_puzzle_color: json_util.JsonValue
        x_ray_right_puzzle_color: json_util.JsonValue
        x_ray_corner_color: json_util.JsonValue
        unknown_0xa947a67c: json_util.JsonValue
        unknown_0x421bae2a: json_util.JsonValue
        unknown_0x439a3774: json_util.JsonValue
        unknown_0x8ee94c81: json_util.JsonValue
        unknown_0x716e6398: json_util.JsonValue
        steam_no_blur_color: json_util.JsonValue
        unknown_0x0f37e756: json_util.JsonValue
        unknown_0xf7283644: json_util.JsonValue
        unknown_0x37564b7d: json_util.JsonValue
        unknown_0x66b7eda3: json_util.JsonValue
        unknown_0xf895098f: json_util.JsonValue
        unknown_0x9b27be10: json_util.JsonValue
        unknown_0x6c8550c9: json_util.JsonValue
        unknown_0x5368a35f: json_util.JsonValue
        unknown_0x5a807b81: json_util.JsonValue
        unknown_0xeb63afed: json_util.JsonValue
        scan_images_color: json_util.JsonValue
        unknown_0xd3bafaf5: json_util.JsonValue
        threat_group_damage_color: json_util.JsonValue
        unknown_0x4f1d443e: json_util.JsonValue
        unknown_0x0f6451da: json_util.JsonValue
        scan_seeker_color: json_util.JsonValue
        unknown_0x43ed3310: json_util.JsonValue
        unknown_0xa781ed1d: json_util.JsonValue
        log_book_color: json_util.JsonValue
        log_book_frame_color: json_util.JsonValue
        inventory_equipped_color: json_util.JsonValue
        command_text_color: json_util.JsonValue
        command_text_outline_color: json_util.JsonValue
        unknown_0x4b03e738: json_util.JsonValue
        unknown_0xf883607c: json_util.JsonValue
        unknown_0xb68f96ec: json_util.JsonValue
        unknown_0x2e73549a: json_util.JsonValue
        unknown_0x938f3af5: json_util.JsonValue
        unknown_0x3f27fa9a: json_util.JsonValue
        unknown_0xd2fa7631: json_util.JsonValue
        unknown_0xdfcf84e1: json_util.JsonValue
        unknown_0x16912ca9: json_util.JsonValue
        unknown_0xe50cda52: json_util.JsonValue
        unknown_0x7dc076a6: json_util.JsonValue
        unknown_0xc6f86bfd: json_util.JsonValue
        unknown_0xbfffe95a: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x8ED04C36,
    0x94BB7EE5,
    0x2D037B5A,
    0x415A81F8,
    0xFE95100F,
    0xAF38A796,
    0x66733E29,
    0xFF6D31E9,
    0x9B63FFA6,
    0x7298E223,
    0x556481E8,
    0xEE8A2117,
    0xF468695D,
    0xDB5C8A60,
    0x166C22E0,
    0xCEC78E81,
    0x91338F72,
    0x2DF1EB03,
    0xB5DA30F4,
    0xC8DDC662,
    0x6991E2CD,
    0x5C336F85,
    0xDEFCA700,
    0xCB7DDAF4,
    0xF17911AA,
    0xA14C8D20,
    0xB4135CDD,
    0xE0290C48,
    0x1EC7F863,
    0xAE1317D8,
    0x22B9B01E,
    0x70A2CD6E,
    0xE7070332,
    0x779C7B9C,
    0x6F6E9D6D,
    0xC00A29F,
    0x83040135,
    0x3C1AE0FF,
    0x29453102,
    0x64337CCD,
    0xBE3C29A1,
    0xD110A12F,
    0xCEB17CDF,
    0x4C5AFF4F,
    0xB17B693,
    0x8B0A4C90,
    0xC4E17CA8,
    0xCDBD73E1,
    0x78522461,
    0x6A839A97,
    0x79EA6F12,
    0xDC901206,
    0xC54FA7BC,
    0x18717FA7,
    0x8B7D7378,
    0x867B01A2,
    0xC02EED79,
    0xE4C1BBEB,
    0xCE7C9D8D,
    0x13490420,
    0xAFE2D45D,
    0x2AF5AA06,
    0xD3CBE846,
    0x507B51DA,
    0xC61D97EF,
    0xAF0001CF,
    0x150A9B17,
    0xD66D715F,
    0xA8698FE8,
    0x4CB38E71,
    0xA947A67C,
    0x421BAE2A,
    0x439A3774,
    0x8EE94C81,
    0x716E6398,
    0xDACA46D4,
    0xF37E756,
    0xF7283644,
    0x37564B7D,
    0x66B7EDA3,
    0xF895098F,
    0x9B27BE10,
    0x6C8550C9,
    0x5368A35F,
    0x5A807B81,
    0xEB63AFED,
    0xABDBFA5B,
    0xD3BAFAF5,
    0xF8B971FA,
    0x4F1D443E,
    0xF6451DA,
    0x345E5B4E,
    0x43ED3310,
    0xA781ED1D,
    0x1B0F3A85,
    0xEB5AE665,
    0x149369FD,
    0x65EE03A7,
    0x55BB9BA8,
    0x4B03E738,
    0xF883607C,
    0xB68F96EC,
    0x2E73549A,
    0x938F3AF5,
    0x3F27FA9A,
    0xD2FA7631,
    0xDFCF84E1,
    0x16912CA9,
    0xE50CDA52,
    0x7DC076A6,
    0xC6F86BFD,
    0xBFFFE95A,
)


@dataclasses.dataclass()
class TweakGuiColors_Misc(BaseProperty):
    unknown_0x8ed04c36: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x8ED04C36, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x94bb7ee5: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x94BB7EE5, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    pause_screen_tweak_open_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x2D037B5A,
                original_name="PauseScreenTweakOpenColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x415a81f8: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x415A81F8, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xfe95100f: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xFE95100F, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    pause_screen_fullscreen_bg_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xAF38A796,
                original_name="PauseScreenFullscreenBGColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x66733e29: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x66733E29, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    pause_screen_frame_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xFF6D31E9,
                original_name="PauseScreenFrameColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    pause_screen_icons_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x9B63FFA6,
                original_name="PauseScreenIconsColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    pause_screen_text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x7298E223,
                original_name="PauseScreenTextColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    pause_screen_highlight_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x556481E8,
                original_name="PauseScreenHighlightColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    pause_screen_helmet_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xEE8A2117,
                original_name="PauseScreenHelmetColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    gui_cursor_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF468695D, original_name="GuiCursorColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdb5c8a60: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDB5C8A60, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x166c22e0: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x166C22E0, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xcec78e81: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xCEC78E81, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x91338f72: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x91338F72, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    hud_memo_text_foreground_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x2DF1EB03,
                original_name="HUDMemoTextForegroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    hud_memo_text_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xB5DA30F4,
                original_name="HUDMemoTextOutlineColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xc8ddc662: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xC8DDC662, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    hud_glow_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6991E2CD, original_name="HUDGlowColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x5c336f85: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5C336F85, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdefca700: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDEFCA700, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    selected_visor_beam_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xCB7DDAF4,
                original_name="SelectedVisorBeamColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unselected_visor_beam_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xF17911AA,
                original_name="UnselectedVisorBeamColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    energy_bar_low_filled_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xA14C8D20,
                original_name="EnergyBarLowFilledColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    energy_bar_low_shadow_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xB4135CDD,
                original_name="EnergyBarLowShadowColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    energy_bar_low_empty_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xE0290C48,
                original_name="EnergyBarLowEmptyColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    hud_damage_modulate_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x1EC7F863,
                original_name="HUDDamageModulateColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    damage_indicator_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xAE1317D8,
                original_name="DamageIndicatorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    hud_title_foreground_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x22B9B01E,
                original_name="HudTitleForegroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    hud_title_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x70A2CD6E,
                original_name="HudTitleOutlineColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xe7070332: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE7070332, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x779c7b9c: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x779C7B9C, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_warning_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x6F6E9D6D,
                original_name="EnergyWarningColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    missile_warning_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x0C00A29F,
                original_name="MissileWarningColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x83040135: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x83040135, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x3c1ae0ff: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x3C1AE0FF, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    missile_bar_shadow_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x29453102,
                original_name="MissileBarShadowColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    missile_bar_empty_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x64337CCD,
                original_name="MissileBarEmptyColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xbe3c29a1: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xBE3C29A1, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
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
    missile_group_combo_charge_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xCEB17CDF,
                original_name="MissileGroupComboChargeColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x4c5aff4f: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x4C5AFF4F, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x0b17b693: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0B17B693, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x8b0a4c90: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x8B0A4C90, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_warning_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xC4E17CA8,
                original_name="EnergyWarningOutlineColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    missile_warning_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xCDBD73E1,
                original_name="MissileWarningOutlineColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x78522461: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x78522461, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    flash_pass_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6A839A97, original_name="FlashPassColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x79ea6f12: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x79EA6F12, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdc901206: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDC901206, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xc54fa7bc: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xC54FA7BC, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x18717fa7: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x18717FA7, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x8b7d7378: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x8B7D7378, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x867b01a2: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x867B01A2, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xc02eed79: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xC02EED79, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    metroid_suck_pulse_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xE4C1BBEB,
                original_name="MetroidSuckPulseColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xce7c9d8d: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xCE7C9D8D, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    energy_bar_damage_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x13490420,
                original_name="EnergyBarDamageColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xafe2d45d: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xAFE2D45D, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    x_ray_holo_grid_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x2AF5AA06,
                original_name="XRayHoloGridColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_seeker_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD3CBE846, original_name="XRaySeekerColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    x_ray_seeker_ticks_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x507B51DA,
                original_name="XRaySeekerTicksColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_seeker_ticks_outer_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xC61D97EF,
                original_name="XRaySeekerTicksOuterColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_top_puzzle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xAF0001CF,
                original_name="XRayTopPuzzleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_bottom_puzzle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x150A9B17,
                original_name="XRayBottomPuzzleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_left_puzzle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xD66D715F,
                original_name="XRayLeftPuzzleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_right_puzzle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xA8698FE8,
                original_name="XRayRightPuzzleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    x_ray_corner_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x4CB38E71, original_name="XRayCornerColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xa947a67c: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA947A67C, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x421bae2a: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x421BAE2A, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x439a3774: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x439A3774, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x8ee94c81: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x8EE94C81, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x716e6398: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x716E6398, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    steam_no_blur_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDACA46D4, original_name="SteamNoBlurColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x0f37e756: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0F37E756, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xf7283644: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF7283644, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x37564b7d: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x37564B7D, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x66b7eda3: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x66B7EDA3, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xf895098f: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF895098F, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x9b27be10: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x9B27BE10, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x6c8550c9: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x6C8550C9, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x5368a35f: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5368A35F, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x5a807b81: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5A807B81, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xeb63afed: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xEB63AFED, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    scan_images_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xABDBFA5B, original_name="ScanImagesColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xd3bafaf5: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD3BAFAF5, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    threat_group_damage_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xF8B971FA,
                original_name="ThreatGroupDamageColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x4f1d443e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x4F1D443E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x0f6451da: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0F6451DA, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    scan_seeker_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x345E5B4E, original_name="ScanSeekerColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x43ed3310: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x43ED3310, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xa781ed1d: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA781ED1D, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    log_book_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1B0F3A85, original_name="LogBookColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    log_book_frame_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xEB5AE665,
                original_name="LogBookFrameColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    inventory_equipped_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x149369FD,
                original_name="InventoryEquippedColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    command_text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x65EE03A7, original_name="CommandTextColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    command_text_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x55BB9BA8,
                original_name="CommandTextOutlineColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x4b03e738: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x4B03E738, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xf883607c: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF883607C, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xb68f96ec: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xB68F96EC, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x2e73549a: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x2E73549A, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x938f3af5: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x938F3AF5, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x3f27fa9a: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x3F27FA9A, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xd2fa7631: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD2FA7631, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdfcf84e1: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDFCF84E1, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x16912ca9: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x16912CA9, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xe50cda52: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE50CDA52, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x7dc076a6: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7DC076A6, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xc6f86bfd: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xC6F86BFD, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xbfffe95a: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBFFFE95A, original_name="Unknown"),
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
        if property_count != 112:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHl"
            )

        dec = _FAST_FORMAT.unpack(data.read(2452))
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
            dec[96],
            dec[102],
            dec[108],
            dec[114],
            dec[120],
            dec[126],
            dec[132],
            dec[138],
            dec[144],
            dec[150],
            dec[156],
            dec[162],
            dec[168],
            dec[174],
            dec[180],
            dec[186],
            dec[192],
            dec[198],
            dec[204],
            dec[210],
            dec[216],
            dec[222],
            dec[228],
            dec[234],
            dec[240],
            dec[246],
            dec[252],
            dec[258],
            dec[264],
            dec[270],
            dec[276],
            dec[282],
            dec[288],
            dec[294],
            dec[300],
            dec[306],
            dec[312],
            dec[318],
            dec[324],
            dec[330],
            dec[336],
            dec[342],
            dec[348],
            dec[354],
            dec[360],
            dec[366],
            dec[372],
            dec[378],
            dec[384],
            dec[390],
            dec[396],
            dec[402],
            dec[408],
            dec[414],
            dec[420],
            dec[426],
            dec[432],
            dec[438],
            dec[444],
            dec[450],
            dec[456],
            dec[462],
            dec[468],
            dec[474],
            dec[480],
            dec[486],
            dec[492],
            dec[498],
            dec[504],
            dec[510],
            dec[516],
            dec[522],
            dec[528],
            dec[534],
            dec[540],
            dec[546],
            dec[552],
            dec[558],
            dec[564],
            dec[570],
            dec[576],
            dec[582],
            dec[588],
            dec[594],
            dec[600],
            dec[606],
            dec[612],
            dec[618],
            dec[624],
            dec[630],
            dec[636],
            dec[642],
            dec[648],
            dec[654],
            dec[660],
            dec[666],
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
            Color(*dec[98:102]),
            Color(*dec[104:108]),
            Color(*dec[110:114]),
            Color(*dec[116:120]),
            Color(*dec[122:126]),
            Color(*dec[128:132]),
            Color(*dec[134:138]),
            Color(*dec[140:144]),
            Color(*dec[146:150]),
            Color(*dec[152:156]),
            Color(*dec[158:162]),
            Color(*dec[164:168]),
            Color(*dec[170:174]),
            Color(*dec[176:180]),
            Color(*dec[182:186]),
            Color(*dec[188:192]),
            Color(*dec[194:198]),
            Color(*dec[200:204]),
            Color(*dec[206:210]),
            Color(*dec[212:216]),
            Color(*dec[218:222]),
            Color(*dec[224:228]),
            Color(*dec[230:234]),
            Color(*dec[236:240]),
            Color(*dec[242:246]),
            Color(*dec[248:252]),
            Color(*dec[254:258]),
            Color(*dec[260:264]),
            Color(*dec[266:270]),
            Color(*dec[272:276]),
            Color(*dec[278:282]),
            Color(*dec[284:288]),
            Color(*dec[290:294]),
            Color(*dec[296:300]),
            Color(*dec[302:306]),
            Color(*dec[308:312]),
            Color(*dec[314:318]),
            Color(*dec[320:324]),
            Color(*dec[326:330]),
            Color(*dec[332:336]),
            Color(*dec[338:342]),
            Color(*dec[344:348]),
            Color(*dec[350:354]),
            Color(*dec[356:360]),
            Color(*dec[362:366]),
            Color(*dec[368:372]),
            Color(*dec[374:378]),
            Color(*dec[380:384]),
            Color(*dec[386:390]),
            Color(*dec[392:396]),
            Color(*dec[398:402]),
            Color(*dec[404:408]),
            Color(*dec[410:414]),
            Color(*dec[416:420]),
            Color(*dec[422:426]),
            Color(*dec[428:432]),
            Color(*dec[434:438]),
            Color(*dec[440:444]),
            Color(*dec[446:450]),
            Color(*dec[452:456]),
            Color(*dec[458:462]),
            Color(*dec[464:468]),
            Color(*dec[470:474]),
            Color(*dec[476:480]),
            Color(*dec[482:486]),
            Color(*dec[488:492]),
            Color(*dec[494:498]),
            Color(*dec[500:504]),
            Color(*dec[506:510]),
            Color(*dec[512:516]),
            Color(*dec[518:522]),
            Color(*dec[524:528]),
            Color(*dec[530:534]),
            Color(*dec[536:540]),
            Color(*dec[542:546]),
            Color(*dec[548:552]),
            Color(*dec[554:558]),
            Color(*dec[560:564]),
            Color(*dec[566:570]),
            Color(*dec[572:576]),
            Color(*dec[578:582]),
            Color(*dec[584:588]),
            Color(*dec[590:594]),
            Color(*dec[596:600]),
            Color(*dec[602:606]),
            Color(*dec[608:612]),
            Color(*dec[614:618]),
            Color(*dec[620:624]),
            Color(*dec[626:630]),
            Color(*dec[632:636]),
            Color(*dec[638:642]),
            Color(*dec[644:648]),
            Color(*dec[650:654]),
            Color(*dec[656:660]),
            Color(*dec[662:666]),
            dec[668],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00p")  # 112 properties

        data.write(b"\x8e\xd0L6")  # 0x8ed04c36
        data.write(b"\x00\x10")  # size
        self.unknown_0x8ed04c36.to_stream(data, game)

        data.write(b"\x94\xbb~\xe5")  # 0x94bb7ee5
        data.write(b"\x00\x10")  # size
        self.unknown_0x94bb7ee5.to_stream(data, game)

        data.write(b"-\x03{Z")  # 0x2d037b5a
        data.write(b"\x00\x10")  # size
        self.pause_screen_tweak_open_color.to_stream(data, game)

        data.write(b"AZ\x81\xf8")  # 0x415a81f8
        data.write(b"\x00\x10")  # size
        self.unknown_0x415a81f8.to_stream(data, game)

        data.write(b"\xfe\x95\x10\x0f")  # 0xfe95100f
        data.write(b"\x00\x10")  # size
        self.unknown_0xfe95100f.to_stream(data, game)

        data.write(b"\xaf8\xa7\x96")  # 0xaf38a796
        data.write(b"\x00\x10")  # size
        self.pause_screen_fullscreen_bg_color.to_stream(data, game)

        data.write(b"fs>)")  # 0x66733e29
        data.write(b"\x00\x10")  # size
        self.unknown_0x66733e29.to_stream(data, game)

        data.write(b"\xffm1\xe9")  # 0xff6d31e9
        data.write(b"\x00\x10")  # size
        self.pause_screen_frame_color.to_stream(data, game)

        data.write(b"\x9bc\xff\xa6")  # 0x9b63ffa6
        data.write(b"\x00\x10")  # size
        self.pause_screen_icons_color.to_stream(data, game)

        data.write(b"r\x98\xe2#")  # 0x7298e223
        data.write(b"\x00\x10")  # size
        self.pause_screen_text_color.to_stream(data, game)

        data.write(b"Ud\x81\xe8")  # 0x556481e8
        data.write(b"\x00\x10")  # size
        self.pause_screen_highlight_color.to_stream(data, game)

        data.write(b"\xee\x8a!\x17")  # 0xee8a2117
        data.write(b"\x00\x10")  # size
        self.pause_screen_helmet_color.to_stream(data, game)

        data.write(b"\xf4hi]")  # 0xf468695d
        data.write(b"\x00\x10")  # size
        self.gui_cursor_color.to_stream(data, game)

        data.write(b"\xdb\\\x8a`")  # 0xdb5c8a60
        data.write(b"\x00\x10")  # size
        self.unknown_0xdb5c8a60.to_stream(data, game)

        data.write(b'\x16l"\xe0')  # 0x166c22e0
        data.write(b"\x00\x10")  # size
        self.unknown_0x166c22e0.to_stream(data, game)

        data.write(b"\xce\xc7\x8e\x81")  # 0xcec78e81
        data.write(b"\x00\x10")  # size
        self.unknown_0xcec78e81.to_stream(data, game)

        data.write(b"\x913\x8fr")  # 0x91338f72
        data.write(b"\x00\x10")  # size
        self.unknown_0x91338f72.to_stream(data, game)

        data.write(b"-\xf1\xeb\x03")  # 0x2df1eb03
        data.write(b"\x00\x10")  # size
        self.hud_memo_text_foreground_color.to_stream(data, game)

        data.write(b"\xb5\xda0\xf4")  # 0xb5da30f4
        data.write(b"\x00\x10")  # size
        self.hud_memo_text_outline_color.to_stream(data, game)

        data.write(b"\xc8\xdd\xc6b")  # 0xc8ddc662
        data.write(b"\x00\x10")  # size
        self.unknown_0xc8ddc662.to_stream(data, game)

        data.write(b"i\x91\xe2\xcd")  # 0x6991e2cd
        data.write(b"\x00\x10")  # size
        self.hud_glow_color.to_stream(data, game)

        data.write(b"\\3o\x85")  # 0x5c336f85
        data.write(b"\x00\x10")  # size
        self.unknown_0x5c336f85.to_stream(data, game)

        data.write(b"\xde\xfc\xa7\x00")  # 0xdefca700
        data.write(b"\x00\x10")  # size
        self.unknown_0xdefca700.to_stream(data, game)

        data.write(b"\xcb}\xda\xf4")  # 0xcb7ddaf4
        data.write(b"\x00\x10")  # size
        self.selected_visor_beam_color.to_stream(data, game)

        data.write(b"\xf1y\x11\xaa")  # 0xf17911aa
        data.write(b"\x00\x10")  # size
        self.unselected_visor_beam_color.to_stream(data, game)

        data.write(b"\xa1L\x8d ")  # 0xa14c8d20
        data.write(b"\x00\x10")  # size
        self.energy_bar_low_filled_color.to_stream(data, game)

        data.write(b"\xb4\x13\\\xdd")  # 0xb4135cdd
        data.write(b"\x00\x10")  # size
        self.energy_bar_low_shadow_color.to_stream(data, game)

        data.write(b"\xe0)\x0cH")  # 0xe0290c48
        data.write(b"\x00\x10")  # size
        self.energy_bar_low_empty_color.to_stream(data, game)

        data.write(b"\x1e\xc7\xf8c")  # 0x1ec7f863
        data.write(b"\x00\x10")  # size
        self.hud_damage_modulate_color.to_stream(data, game)

        data.write(b"\xae\x13\x17\xd8")  # 0xae1317d8
        data.write(b"\x00\x10")  # size
        self.damage_indicator_color.to_stream(data, game)

        data.write(b'"\xb9\xb0\x1e')  # 0x22b9b01e
        data.write(b"\x00\x10")  # size
        self.hud_title_foreground_color.to_stream(data, game)

        data.write(b"p\xa2\xcdn")  # 0x70a2cd6e
        data.write(b"\x00\x10")  # size
        self.hud_title_outline_color.to_stream(data, game)

        data.write(b"\xe7\x07\x032")  # 0xe7070332
        data.write(b"\x00\x10")  # size
        self.unknown_0xe7070332.to_stream(data, game)

        data.write(b"w\x9c{\x9c")  # 0x779c7b9c
        data.write(b"\x00\x10")  # size
        self.unknown_0x779c7b9c.to_stream(data, game)

        data.write(b"on\x9dm")  # 0x6f6e9d6d
        data.write(b"\x00\x10")  # size
        self.energy_warning_color.to_stream(data, game)

        data.write(b"\x0c\x00\xa2\x9f")  # 0xc00a29f
        data.write(b"\x00\x10")  # size
        self.missile_warning_color.to_stream(data, game)

        data.write(b"\x83\x04\x015")  # 0x83040135
        data.write(b"\x00\x10")  # size
        self.unknown_0x83040135.to_stream(data, game)

        data.write(b"<\x1a\xe0\xff")  # 0x3c1ae0ff
        data.write(b"\x00\x10")  # size
        self.unknown_0x3c1ae0ff.to_stream(data, game)

        data.write(b")E1\x02")  # 0x29453102
        data.write(b"\x00\x10")  # size
        self.missile_bar_shadow_color.to_stream(data, game)

        data.write(b"d3|\xcd")  # 0x64337ccd
        data.write(b"\x00\x10")  # size
        self.missile_bar_empty_color.to_stream(data, game)

        data.write(b"\xbe<)\xa1")  # 0xbe3c29a1
        data.write(b"\x00\x10")  # size
        self.unknown_0xbe3c29a1.to_stream(data, game)

        data.write(b"\xd1\x10\xa1/")  # 0xd110a12f
        data.write(b"\x00\x10")  # size
        self.missile_group_inactive_color.to_stream(data, game)

        data.write(b"\xce\xb1|\xdf")  # 0xceb17cdf
        data.write(b"\x00\x10")  # size
        self.missile_group_combo_charge_color.to_stream(data, game)

        data.write(b"LZ\xffO")  # 0x4c5aff4f
        data.write(b"\x00\x10")  # size
        self.unknown_0x4c5aff4f.to_stream(data, game)

        data.write(b"\x0b\x17\xb6\x93")  # 0xb17b693
        data.write(b"\x00\x10")  # size
        self.unknown_0x0b17b693.to_stream(data, game)

        data.write(b"\x8b\nL\x90")  # 0x8b0a4c90
        data.write(b"\x00\x10")  # size
        self.unknown_0x8b0a4c90.to_stream(data, game)

        data.write(b"\xc4\xe1|\xa8")  # 0xc4e17ca8
        data.write(b"\x00\x10")  # size
        self.energy_warning_outline_color.to_stream(data, game)

        data.write(b"\xcd\xbds\xe1")  # 0xcdbd73e1
        data.write(b"\x00\x10")  # size
        self.missile_warning_outline_color.to_stream(data, game)

        data.write(b"xR$a")  # 0x78522461
        data.write(b"\x00\x10")  # size
        self.unknown_0x78522461.to_stream(data, game)

        data.write(b"j\x83\x9a\x97")  # 0x6a839a97
        data.write(b"\x00\x10")  # size
        self.flash_pass_color.to_stream(data, game)

        data.write(b"y\xeao\x12")  # 0x79ea6f12
        data.write(b"\x00\x10")  # size
        self.unknown_0x79ea6f12.to_stream(data, game)

        data.write(b"\xdc\x90\x12\x06")  # 0xdc901206
        data.write(b"\x00\x10")  # size
        self.unknown_0xdc901206.to_stream(data, game)

        data.write(b"\xc5O\xa7\xbc")  # 0xc54fa7bc
        data.write(b"\x00\x10")  # size
        self.unknown_0xc54fa7bc.to_stream(data, game)

        data.write(b"\x18q\x7f\xa7")  # 0x18717fa7
        data.write(b"\x00\x10")  # size
        self.unknown_0x18717fa7.to_stream(data, game)

        data.write(b"\x8b}sx")  # 0x8b7d7378
        data.write(b"\x00\x10")  # size
        self.unknown_0x8b7d7378.to_stream(data, game)

        data.write(b"\x86{\x01\xa2")  # 0x867b01a2
        data.write(b"\x00\x10")  # size
        self.unknown_0x867b01a2.to_stream(data, game)

        data.write(b"\xc0.\xedy")  # 0xc02eed79
        data.write(b"\x00\x10")  # size
        self.unknown_0xc02eed79.to_stream(data, game)

        data.write(b"\xe4\xc1\xbb\xeb")  # 0xe4c1bbeb
        data.write(b"\x00\x10")  # size
        self.metroid_suck_pulse_color.to_stream(data, game)

        data.write(b"\xce|\x9d\x8d")  # 0xce7c9d8d
        data.write(b"\x00\x10")  # size
        self.unknown_0xce7c9d8d.to_stream(data, game)

        data.write(b"\x13I\x04 ")  # 0x13490420
        data.write(b"\x00\x10")  # size
        self.energy_bar_damage_color.to_stream(data, game)

        data.write(b"\xaf\xe2\xd4]")  # 0xafe2d45d
        data.write(b"\x00\x10")  # size
        self.unknown_0xafe2d45d.to_stream(data, game)

        data.write(b"*\xf5\xaa\x06")  # 0x2af5aa06
        data.write(b"\x00\x10")  # size
        self.x_ray_holo_grid_color.to_stream(data, game)

        data.write(b"\xd3\xcb\xe8F")  # 0xd3cbe846
        data.write(b"\x00\x10")  # size
        self.x_ray_seeker_color.to_stream(data, game)

        data.write(b"P{Q\xda")  # 0x507b51da
        data.write(b"\x00\x10")  # size
        self.x_ray_seeker_ticks_color.to_stream(data, game)

        data.write(b"\xc6\x1d\x97\xef")  # 0xc61d97ef
        data.write(b"\x00\x10")  # size
        self.x_ray_seeker_ticks_outer_color.to_stream(data, game)

        data.write(b"\xaf\x00\x01\xcf")  # 0xaf0001cf
        data.write(b"\x00\x10")  # size
        self.x_ray_top_puzzle_color.to_stream(data, game)

        data.write(b"\x15\n\x9b\x17")  # 0x150a9b17
        data.write(b"\x00\x10")  # size
        self.x_ray_bottom_puzzle_color.to_stream(data, game)

        data.write(b"\xd6mq_")  # 0xd66d715f
        data.write(b"\x00\x10")  # size
        self.x_ray_left_puzzle_color.to_stream(data, game)

        data.write(b"\xa8i\x8f\xe8")  # 0xa8698fe8
        data.write(b"\x00\x10")  # size
        self.x_ray_right_puzzle_color.to_stream(data, game)

        data.write(b"L\xb3\x8eq")  # 0x4cb38e71
        data.write(b"\x00\x10")  # size
        self.x_ray_corner_color.to_stream(data, game)

        data.write(b"\xa9G\xa6|")  # 0xa947a67c
        data.write(b"\x00\x10")  # size
        self.unknown_0xa947a67c.to_stream(data, game)

        data.write(b"B\x1b\xae*")  # 0x421bae2a
        data.write(b"\x00\x10")  # size
        self.unknown_0x421bae2a.to_stream(data, game)

        data.write(b"C\x9a7t")  # 0x439a3774
        data.write(b"\x00\x10")  # size
        self.unknown_0x439a3774.to_stream(data, game)

        data.write(b"\x8e\xe9L\x81")  # 0x8ee94c81
        data.write(b"\x00\x10")  # size
        self.unknown_0x8ee94c81.to_stream(data, game)

        data.write(b"qnc\x98")  # 0x716e6398
        data.write(b"\x00\x10")  # size
        self.unknown_0x716e6398.to_stream(data, game)

        data.write(b"\xda\xcaF\xd4")  # 0xdaca46d4
        data.write(b"\x00\x10")  # size
        self.steam_no_blur_color.to_stream(data, game)

        data.write(b"\x0f7\xe7V")  # 0xf37e756
        data.write(b"\x00\x10")  # size
        self.unknown_0x0f37e756.to_stream(data, game)

        data.write(b"\xf7(6D")  # 0xf7283644
        data.write(b"\x00\x10")  # size
        self.unknown_0xf7283644.to_stream(data, game)

        data.write(b"7VK}")  # 0x37564b7d
        data.write(b"\x00\x10")  # size
        self.unknown_0x37564b7d.to_stream(data, game)

        data.write(b"f\xb7\xed\xa3")  # 0x66b7eda3
        data.write(b"\x00\x10")  # size
        self.unknown_0x66b7eda3.to_stream(data, game)

        data.write(b"\xf8\x95\t\x8f")  # 0xf895098f
        data.write(b"\x00\x10")  # size
        self.unknown_0xf895098f.to_stream(data, game)

        data.write(b"\x9b'\xbe\x10")  # 0x9b27be10
        data.write(b"\x00\x10")  # size
        self.unknown_0x9b27be10.to_stream(data, game)

        data.write(b"l\x85P\xc9")  # 0x6c8550c9
        data.write(b"\x00\x10")  # size
        self.unknown_0x6c8550c9.to_stream(data, game)

        data.write(b"Sh\xa3_")  # 0x5368a35f
        data.write(b"\x00\x10")  # size
        self.unknown_0x5368a35f.to_stream(data, game)

        data.write(b"Z\x80{\x81")  # 0x5a807b81
        data.write(b"\x00\x10")  # size
        self.unknown_0x5a807b81.to_stream(data, game)

        data.write(b"\xebc\xaf\xed")  # 0xeb63afed
        data.write(b"\x00\x10")  # size
        self.unknown_0xeb63afed.to_stream(data, game)

        data.write(b"\xab\xdb\xfa[")  # 0xabdbfa5b
        data.write(b"\x00\x10")  # size
        self.scan_images_color.to_stream(data, game)

        data.write(b"\xd3\xba\xfa\xf5")  # 0xd3bafaf5
        data.write(b"\x00\x10")  # size
        self.unknown_0xd3bafaf5.to_stream(data, game)

        data.write(b"\xf8\xb9q\xfa")  # 0xf8b971fa
        data.write(b"\x00\x10")  # size
        self.threat_group_damage_color.to_stream(data, game)

        data.write(b"O\x1dD>")  # 0x4f1d443e
        data.write(b"\x00\x10")  # size
        self.unknown_0x4f1d443e.to_stream(data, game)

        data.write(b"\x0fdQ\xda")  # 0xf6451da
        data.write(b"\x00\x10")  # size
        self.unknown_0x0f6451da.to_stream(data, game)

        data.write(b"4^[N")  # 0x345e5b4e
        data.write(b"\x00\x10")  # size
        self.scan_seeker_color.to_stream(data, game)

        data.write(b"C\xed3\x10")  # 0x43ed3310
        data.write(b"\x00\x10")  # size
        self.unknown_0x43ed3310.to_stream(data, game)

        data.write(b"\xa7\x81\xed\x1d")  # 0xa781ed1d
        data.write(b"\x00\x10")  # size
        self.unknown_0xa781ed1d.to_stream(data, game)

        data.write(b"\x1b\x0f:\x85")  # 0x1b0f3a85
        data.write(b"\x00\x10")  # size
        self.log_book_color.to_stream(data, game)

        data.write(b"\xebZ\xe6e")  # 0xeb5ae665
        data.write(b"\x00\x10")  # size
        self.log_book_frame_color.to_stream(data, game)

        data.write(b"\x14\x93i\xfd")  # 0x149369fd
        data.write(b"\x00\x10")  # size
        self.inventory_equipped_color.to_stream(data, game)

        data.write(b"e\xee\x03\xa7")  # 0x65ee03a7
        data.write(b"\x00\x10")  # size
        self.command_text_color.to_stream(data, game)

        data.write(b"U\xbb\x9b\xa8")  # 0x55bb9ba8
        data.write(b"\x00\x10")  # size
        self.command_text_outline_color.to_stream(data, game)

        data.write(b"K\x03\xe78")  # 0x4b03e738
        data.write(b"\x00\x10")  # size
        self.unknown_0x4b03e738.to_stream(data, game)

        data.write(b"\xf8\x83`|")  # 0xf883607c
        data.write(b"\x00\x10")  # size
        self.unknown_0xf883607c.to_stream(data, game)

        data.write(b"\xb6\x8f\x96\xec")  # 0xb68f96ec
        data.write(b"\x00\x10")  # size
        self.unknown_0xb68f96ec.to_stream(data, game)

        data.write(b".sT\x9a")  # 0x2e73549a
        data.write(b"\x00\x10")  # size
        self.unknown_0x2e73549a.to_stream(data, game)

        data.write(b"\x93\x8f:\xf5")  # 0x938f3af5
        data.write(b"\x00\x10")  # size
        self.unknown_0x938f3af5.to_stream(data, game)

        data.write(b"?'\xfa\x9a")  # 0x3f27fa9a
        data.write(b"\x00\x10")  # size
        self.unknown_0x3f27fa9a.to_stream(data, game)

        data.write(b"\xd2\xfav1")  # 0xd2fa7631
        data.write(b"\x00\x10")  # size
        self.unknown_0xd2fa7631.to_stream(data, game)

        data.write(b"\xdf\xcf\x84\xe1")  # 0xdfcf84e1
        data.write(b"\x00\x10")  # size
        self.unknown_0xdfcf84e1.to_stream(data, game)

        data.write(b"\x16\x91,\xa9")  # 0x16912ca9
        data.write(b"\x00\x10")  # size
        self.unknown_0x16912ca9.to_stream(data, game)

        data.write(b"\xe5\x0c\xdaR")  # 0xe50cda52
        data.write(b"\x00\x10")  # size
        self.unknown_0xe50cda52.to_stream(data, game)

        data.write(b"}\xc0v\xa6")  # 0x7dc076a6
        data.write(b"\x00\x10")  # size
        self.unknown_0x7dc076a6.to_stream(data, game)

        data.write(b"\xc6\xf8k\xfd")  # 0xc6f86bfd
        data.write(b"\x00\x10")  # size
        self.unknown_0xc6f86bfd.to_stream(data, game)

        data.write(b"\xbf\xff\xe9Z")  # 0xbfffe95a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xbfffe95a))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGuiColors_MiscJson", data)
        return cls(
            unknown_0x8ed04c36=Color.from_json(json_data["unknown_0x8ed04c36"]),
            unknown_0x94bb7ee5=Color.from_json(json_data["unknown_0x94bb7ee5"]),
            pause_screen_tweak_open_color=Color.from_json(json_data["pause_screen_tweak_open_color"]),
            unknown_0x415a81f8=Color.from_json(json_data["unknown_0x415a81f8"]),
            unknown_0xfe95100f=Color.from_json(json_data["unknown_0xfe95100f"]),
            pause_screen_fullscreen_bg_color=Color.from_json(json_data["pause_screen_fullscreen_bg_color"]),
            unknown_0x66733e29=Color.from_json(json_data["unknown_0x66733e29"]),
            pause_screen_frame_color=Color.from_json(json_data["pause_screen_frame_color"]),
            pause_screen_icons_color=Color.from_json(json_data["pause_screen_icons_color"]),
            pause_screen_text_color=Color.from_json(json_data["pause_screen_text_color"]),
            pause_screen_highlight_color=Color.from_json(json_data["pause_screen_highlight_color"]),
            pause_screen_helmet_color=Color.from_json(json_data["pause_screen_helmet_color"]),
            gui_cursor_color=Color.from_json(json_data["gui_cursor_color"]),
            unknown_0xdb5c8a60=Color.from_json(json_data["unknown_0xdb5c8a60"]),
            unknown_0x166c22e0=Color.from_json(json_data["unknown_0x166c22e0"]),
            unknown_0xcec78e81=Color.from_json(json_data["unknown_0xcec78e81"]),
            unknown_0x91338f72=Color.from_json(json_data["unknown_0x91338f72"]),
            hud_memo_text_foreground_color=Color.from_json(json_data["hud_memo_text_foreground_color"]),
            hud_memo_text_outline_color=Color.from_json(json_data["hud_memo_text_outline_color"]),
            unknown_0xc8ddc662=Color.from_json(json_data["unknown_0xc8ddc662"]),
            hud_glow_color=Color.from_json(json_data["hud_glow_color"]),
            unknown_0x5c336f85=Color.from_json(json_data["unknown_0x5c336f85"]),
            unknown_0xdefca700=Color.from_json(json_data["unknown_0xdefca700"]),
            selected_visor_beam_color=Color.from_json(json_data["selected_visor_beam_color"]),
            unselected_visor_beam_color=Color.from_json(json_data["unselected_visor_beam_color"]),
            energy_bar_low_filled_color=Color.from_json(json_data["energy_bar_low_filled_color"]),
            energy_bar_low_shadow_color=Color.from_json(json_data["energy_bar_low_shadow_color"]),
            energy_bar_low_empty_color=Color.from_json(json_data["energy_bar_low_empty_color"]),
            hud_damage_modulate_color=Color.from_json(json_data["hud_damage_modulate_color"]),
            damage_indicator_color=Color.from_json(json_data["damage_indicator_color"]),
            hud_title_foreground_color=Color.from_json(json_data["hud_title_foreground_color"]),
            hud_title_outline_color=Color.from_json(json_data["hud_title_outline_color"]),
            unknown_0xe7070332=Color.from_json(json_data["unknown_0xe7070332"]),
            unknown_0x779c7b9c=Color.from_json(json_data["unknown_0x779c7b9c"]),
            energy_warning_color=Color.from_json(json_data["energy_warning_color"]),
            missile_warning_color=Color.from_json(json_data["missile_warning_color"]),
            unknown_0x83040135=Color.from_json(json_data["unknown_0x83040135"]),
            unknown_0x3c1ae0ff=Color.from_json(json_data["unknown_0x3c1ae0ff"]),
            missile_bar_shadow_color=Color.from_json(json_data["missile_bar_shadow_color"]),
            missile_bar_empty_color=Color.from_json(json_data["missile_bar_empty_color"]),
            unknown_0xbe3c29a1=Color.from_json(json_data["unknown_0xbe3c29a1"]),
            missile_group_inactive_color=Color.from_json(json_data["missile_group_inactive_color"]),
            missile_group_combo_charge_color=Color.from_json(json_data["missile_group_combo_charge_color"]),
            unknown_0x4c5aff4f=Color.from_json(json_data["unknown_0x4c5aff4f"]),
            unknown_0x0b17b693=Color.from_json(json_data["unknown_0x0b17b693"]),
            unknown_0x8b0a4c90=Color.from_json(json_data["unknown_0x8b0a4c90"]),
            energy_warning_outline_color=Color.from_json(json_data["energy_warning_outline_color"]),
            missile_warning_outline_color=Color.from_json(json_data["missile_warning_outline_color"]),
            unknown_0x78522461=Color.from_json(json_data["unknown_0x78522461"]),
            flash_pass_color=Color.from_json(json_data["flash_pass_color"]),
            unknown_0x79ea6f12=Color.from_json(json_data["unknown_0x79ea6f12"]),
            unknown_0xdc901206=Color.from_json(json_data["unknown_0xdc901206"]),
            unknown_0xc54fa7bc=Color.from_json(json_data["unknown_0xc54fa7bc"]),
            unknown_0x18717fa7=Color.from_json(json_data["unknown_0x18717fa7"]),
            unknown_0x8b7d7378=Color.from_json(json_data["unknown_0x8b7d7378"]),
            unknown_0x867b01a2=Color.from_json(json_data["unknown_0x867b01a2"]),
            unknown_0xc02eed79=Color.from_json(json_data["unknown_0xc02eed79"]),
            metroid_suck_pulse_color=Color.from_json(json_data["metroid_suck_pulse_color"]),
            unknown_0xce7c9d8d=Color.from_json(json_data["unknown_0xce7c9d8d"]),
            energy_bar_damage_color=Color.from_json(json_data["energy_bar_damage_color"]),
            unknown_0xafe2d45d=Color.from_json(json_data["unknown_0xafe2d45d"]),
            x_ray_holo_grid_color=Color.from_json(json_data["x_ray_holo_grid_color"]),
            x_ray_seeker_color=Color.from_json(json_data["x_ray_seeker_color"]),
            x_ray_seeker_ticks_color=Color.from_json(json_data["x_ray_seeker_ticks_color"]),
            x_ray_seeker_ticks_outer_color=Color.from_json(json_data["x_ray_seeker_ticks_outer_color"]),
            x_ray_top_puzzle_color=Color.from_json(json_data["x_ray_top_puzzle_color"]),
            x_ray_bottom_puzzle_color=Color.from_json(json_data["x_ray_bottom_puzzle_color"]),
            x_ray_left_puzzle_color=Color.from_json(json_data["x_ray_left_puzzle_color"]),
            x_ray_right_puzzle_color=Color.from_json(json_data["x_ray_right_puzzle_color"]),
            x_ray_corner_color=Color.from_json(json_data["x_ray_corner_color"]),
            unknown_0xa947a67c=Color.from_json(json_data["unknown_0xa947a67c"]),
            unknown_0x421bae2a=Color.from_json(json_data["unknown_0x421bae2a"]),
            unknown_0x439a3774=Color.from_json(json_data["unknown_0x439a3774"]),
            unknown_0x8ee94c81=Color.from_json(json_data["unknown_0x8ee94c81"]),
            unknown_0x716e6398=Color.from_json(json_data["unknown_0x716e6398"]),
            steam_no_blur_color=Color.from_json(json_data["steam_no_blur_color"]),
            unknown_0x0f37e756=Color.from_json(json_data["unknown_0x0f37e756"]),
            unknown_0xf7283644=Color.from_json(json_data["unknown_0xf7283644"]),
            unknown_0x37564b7d=Color.from_json(json_data["unknown_0x37564b7d"]),
            unknown_0x66b7eda3=Color.from_json(json_data["unknown_0x66b7eda3"]),
            unknown_0xf895098f=Color.from_json(json_data["unknown_0xf895098f"]),
            unknown_0x9b27be10=Color.from_json(json_data["unknown_0x9b27be10"]),
            unknown_0x6c8550c9=Color.from_json(json_data["unknown_0x6c8550c9"]),
            unknown_0x5368a35f=Color.from_json(json_data["unknown_0x5368a35f"]),
            unknown_0x5a807b81=Color.from_json(json_data["unknown_0x5a807b81"]),
            unknown_0xeb63afed=Color.from_json(json_data["unknown_0xeb63afed"]),
            scan_images_color=Color.from_json(json_data["scan_images_color"]),
            unknown_0xd3bafaf5=Color.from_json(json_data["unknown_0xd3bafaf5"]),
            threat_group_damage_color=Color.from_json(json_data["threat_group_damage_color"]),
            unknown_0x4f1d443e=Color.from_json(json_data["unknown_0x4f1d443e"]),
            unknown_0x0f6451da=Color.from_json(json_data["unknown_0x0f6451da"]),
            scan_seeker_color=Color.from_json(json_data["scan_seeker_color"]),
            unknown_0x43ed3310=Color.from_json(json_data["unknown_0x43ed3310"]),
            unknown_0xa781ed1d=Color.from_json(json_data["unknown_0xa781ed1d"]),
            log_book_color=Color.from_json(json_data["log_book_color"]),
            log_book_frame_color=Color.from_json(json_data["log_book_frame_color"]),
            inventory_equipped_color=Color.from_json(json_data["inventory_equipped_color"]),
            command_text_color=Color.from_json(json_data["command_text_color"]),
            command_text_outline_color=Color.from_json(json_data["command_text_outline_color"]),
            unknown_0x4b03e738=Color.from_json(json_data["unknown_0x4b03e738"]),
            unknown_0xf883607c=Color.from_json(json_data["unknown_0xf883607c"]),
            unknown_0xb68f96ec=Color.from_json(json_data["unknown_0xb68f96ec"]),
            unknown_0x2e73549a=Color.from_json(json_data["unknown_0x2e73549a"]),
            unknown_0x938f3af5=Color.from_json(json_data["unknown_0x938f3af5"]),
            unknown_0x3f27fa9a=Color.from_json(json_data["unknown_0x3f27fa9a"]),
            unknown_0xd2fa7631=Color.from_json(json_data["unknown_0xd2fa7631"]),
            unknown_0xdfcf84e1=Color.from_json(json_data["unknown_0xdfcf84e1"]),
            unknown_0x16912ca9=Color.from_json(json_data["unknown_0x16912ca9"]),
            unknown_0xe50cda52=Color.from_json(json_data["unknown_0xe50cda52"]),
            unknown_0x7dc076a6=Color.from_json(json_data["unknown_0x7dc076a6"]),
            unknown_0xc6f86bfd=Color.from_json(json_data["unknown_0xc6f86bfd"]),
            unknown_0xbfffe95a=json_data["unknown_0xbfffe95a"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x8ed04c36": self.unknown_0x8ed04c36.to_json(),
            "unknown_0x94bb7ee5": self.unknown_0x94bb7ee5.to_json(),
            "pause_screen_tweak_open_color": self.pause_screen_tweak_open_color.to_json(),
            "unknown_0x415a81f8": self.unknown_0x415a81f8.to_json(),
            "unknown_0xfe95100f": self.unknown_0xfe95100f.to_json(),
            "pause_screen_fullscreen_bg_color": self.pause_screen_fullscreen_bg_color.to_json(),
            "unknown_0x66733e29": self.unknown_0x66733e29.to_json(),
            "pause_screen_frame_color": self.pause_screen_frame_color.to_json(),
            "pause_screen_icons_color": self.pause_screen_icons_color.to_json(),
            "pause_screen_text_color": self.pause_screen_text_color.to_json(),
            "pause_screen_highlight_color": self.pause_screen_highlight_color.to_json(),
            "pause_screen_helmet_color": self.pause_screen_helmet_color.to_json(),
            "gui_cursor_color": self.gui_cursor_color.to_json(),
            "unknown_0xdb5c8a60": self.unknown_0xdb5c8a60.to_json(),
            "unknown_0x166c22e0": self.unknown_0x166c22e0.to_json(),
            "unknown_0xcec78e81": self.unknown_0xcec78e81.to_json(),
            "unknown_0x91338f72": self.unknown_0x91338f72.to_json(),
            "hud_memo_text_foreground_color": self.hud_memo_text_foreground_color.to_json(),
            "hud_memo_text_outline_color": self.hud_memo_text_outline_color.to_json(),
            "unknown_0xc8ddc662": self.unknown_0xc8ddc662.to_json(),
            "hud_glow_color": self.hud_glow_color.to_json(),
            "unknown_0x5c336f85": self.unknown_0x5c336f85.to_json(),
            "unknown_0xdefca700": self.unknown_0xdefca700.to_json(),
            "selected_visor_beam_color": self.selected_visor_beam_color.to_json(),
            "unselected_visor_beam_color": self.unselected_visor_beam_color.to_json(),
            "energy_bar_low_filled_color": self.energy_bar_low_filled_color.to_json(),
            "energy_bar_low_shadow_color": self.energy_bar_low_shadow_color.to_json(),
            "energy_bar_low_empty_color": self.energy_bar_low_empty_color.to_json(),
            "hud_damage_modulate_color": self.hud_damage_modulate_color.to_json(),
            "damage_indicator_color": self.damage_indicator_color.to_json(),
            "hud_title_foreground_color": self.hud_title_foreground_color.to_json(),
            "hud_title_outline_color": self.hud_title_outline_color.to_json(),
            "unknown_0xe7070332": self.unknown_0xe7070332.to_json(),
            "unknown_0x779c7b9c": self.unknown_0x779c7b9c.to_json(),
            "energy_warning_color": self.energy_warning_color.to_json(),
            "missile_warning_color": self.missile_warning_color.to_json(),
            "unknown_0x83040135": self.unknown_0x83040135.to_json(),
            "unknown_0x3c1ae0ff": self.unknown_0x3c1ae0ff.to_json(),
            "missile_bar_shadow_color": self.missile_bar_shadow_color.to_json(),
            "missile_bar_empty_color": self.missile_bar_empty_color.to_json(),
            "unknown_0xbe3c29a1": self.unknown_0xbe3c29a1.to_json(),
            "missile_group_inactive_color": self.missile_group_inactive_color.to_json(),
            "missile_group_combo_charge_color": self.missile_group_combo_charge_color.to_json(),
            "unknown_0x4c5aff4f": self.unknown_0x4c5aff4f.to_json(),
            "unknown_0x0b17b693": self.unknown_0x0b17b693.to_json(),
            "unknown_0x8b0a4c90": self.unknown_0x8b0a4c90.to_json(),
            "energy_warning_outline_color": self.energy_warning_outline_color.to_json(),
            "missile_warning_outline_color": self.missile_warning_outline_color.to_json(),
            "unknown_0x78522461": self.unknown_0x78522461.to_json(),
            "flash_pass_color": self.flash_pass_color.to_json(),
            "unknown_0x79ea6f12": self.unknown_0x79ea6f12.to_json(),
            "unknown_0xdc901206": self.unknown_0xdc901206.to_json(),
            "unknown_0xc54fa7bc": self.unknown_0xc54fa7bc.to_json(),
            "unknown_0x18717fa7": self.unknown_0x18717fa7.to_json(),
            "unknown_0x8b7d7378": self.unknown_0x8b7d7378.to_json(),
            "unknown_0x867b01a2": self.unknown_0x867b01a2.to_json(),
            "unknown_0xc02eed79": self.unknown_0xc02eed79.to_json(),
            "metroid_suck_pulse_color": self.metroid_suck_pulse_color.to_json(),
            "unknown_0xce7c9d8d": self.unknown_0xce7c9d8d.to_json(),
            "energy_bar_damage_color": self.energy_bar_damage_color.to_json(),
            "unknown_0xafe2d45d": self.unknown_0xafe2d45d.to_json(),
            "x_ray_holo_grid_color": self.x_ray_holo_grid_color.to_json(),
            "x_ray_seeker_color": self.x_ray_seeker_color.to_json(),
            "x_ray_seeker_ticks_color": self.x_ray_seeker_ticks_color.to_json(),
            "x_ray_seeker_ticks_outer_color": self.x_ray_seeker_ticks_outer_color.to_json(),
            "x_ray_top_puzzle_color": self.x_ray_top_puzzle_color.to_json(),
            "x_ray_bottom_puzzle_color": self.x_ray_bottom_puzzle_color.to_json(),
            "x_ray_left_puzzle_color": self.x_ray_left_puzzle_color.to_json(),
            "x_ray_right_puzzle_color": self.x_ray_right_puzzle_color.to_json(),
            "x_ray_corner_color": self.x_ray_corner_color.to_json(),
            "unknown_0xa947a67c": self.unknown_0xa947a67c.to_json(),
            "unknown_0x421bae2a": self.unknown_0x421bae2a.to_json(),
            "unknown_0x439a3774": self.unknown_0x439a3774.to_json(),
            "unknown_0x8ee94c81": self.unknown_0x8ee94c81.to_json(),
            "unknown_0x716e6398": self.unknown_0x716e6398.to_json(),
            "steam_no_blur_color": self.steam_no_blur_color.to_json(),
            "unknown_0x0f37e756": self.unknown_0x0f37e756.to_json(),
            "unknown_0xf7283644": self.unknown_0xf7283644.to_json(),
            "unknown_0x37564b7d": self.unknown_0x37564b7d.to_json(),
            "unknown_0x66b7eda3": self.unknown_0x66b7eda3.to_json(),
            "unknown_0xf895098f": self.unknown_0xf895098f.to_json(),
            "unknown_0x9b27be10": self.unknown_0x9b27be10.to_json(),
            "unknown_0x6c8550c9": self.unknown_0x6c8550c9.to_json(),
            "unknown_0x5368a35f": self.unknown_0x5368a35f.to_json(),
            "unknown_0x5a807b81": self.unknown_0x5a807b81.to_json(),
            "unknown_0xeb63afed": self.unknown_0xeb63afed.to_json(),
            "scan_images_color": self.scan_images_color.to_json(),
            "unknown_0xd3bafaf5": self.unknown_0xd3bafaf5.to_json(),
            "threat_group_damage_color": self.threat_group_damage_color.to_json(),
            "unknown_0x4f1d443e": self.unknown_0x4f1d443e.to_json(),
            "unknown_0x0f6451da": self.unknown_0x0f6451da.to_json(),
            "scan_seeker_color": self.scan_seeker_color.to_json(),
            "unknown_0x43ed3310": self.unknown_0x43ed3310.to_json(),
            "unknown_0xa781ed1d": self.unknown_0xa781ed1d.to_json(),
            "log_book_color": self.log_book_color.to_json(),
            "log_book_frame_color": self.log_book_frame_color.to_json(),
            "inventory_equipped_color": self.inventory_equipped_color.to_json(),
            "command_text_color": self.command_text_color.to_json(),
            "command_text_outline_color": self.command_text_outline_color.to_json(),
            "unknown_0x4b03e738": self.unknown_0x4b03e738.to_json(),
            "unknown_0xf883607c": self.unknown_0xf883607c.to_json(),
            "unknown_0xb68f96ec": self.unknown_0xb68f96ec.to_json(),
            "unknown_0x2e73549a": self.unknown_0x2e73549a.to_json(),
            "unknown_0x938f3af5": self.unknown_0x938f3af5.to_json(),
            "unknown_0x3f27fa9a": self.unknown_0x3f27fa9a.to_json(),
            "unknown_0xd2fa7631": self.unknown_0xd2fa7631.to_json(),
            "unknown_0xdfcf84e1": self.unknown_0xdfcf84e1.to_json(),
            "unknown_0x16912ca9": self.unknown_0x16912ca9.to_json(),
            "unknown_0xe50cda52": self.unknown_0xe50cda52.to_json(),
            "unknown_0x7dc076a6": self.unknown_0x7dc076a6.to_json(),
            "unknown_0xc6f86bfd": self.unknown_0xc6f86bfd.to_json(),
            "unknown_0xbfffe95a": self.unknown_0xbfffe95a,
        }


def _decode_unknown_0x8ed04c36(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x94bb7ee5(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_tweak_open_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x415a81f8(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xfe95100f(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_fullscreen_bg_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x66733e29(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_icons_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_pause_screen_helmet_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_gui_cursor_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdb5c8a60(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x166c22e0(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xcec78e81(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x91338f72(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_memo_text_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_memo_text_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xc8ddc662(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_glow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x5c336f85(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdefca700(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_selected_visor_beam_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unselected_visor_beam_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_low_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_low_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_low_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_damage_modulate_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_damage_indicator_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_title_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_title_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xe7070332(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x779c7b9c(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x83040135(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x3c1ae0ff(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xbe3c29a1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_combo_charge_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x4c5aff4f(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x0b17b693(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x8b0a4c90(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_warning_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_warning_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x78522461(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flash_pass_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x79ea6f12(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdc901206(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xc54fa7bc(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x18717fa7(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x8b7d7378(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x867b01a2(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xc02eed79(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_metroid_suck_pulse_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xce7c9d8d(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xafe2d45d(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_holo_grid_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_ticks_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_ticks_outer_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_top_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_bottom_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_left_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_right_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_corner_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xa947a67c(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x421bae2a(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x439a3774(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x8ee94c81(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x716e6398(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_steam_no_blur_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x0f37e756(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xf7283644(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x37564b7d(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x66b7eda3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xf895098f(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x9b27be10(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x6c8550c9(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x5368a35f(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x5a807b81(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xeb63afed(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_images_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xd3bafaf5(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_group_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x4f1d443e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x0f6451da(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_seeker_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x43ed3310(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xa781ed1d(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_log_book_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_log_book_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inventory_equipped_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_command_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_command_text_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x4b03e738(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xf883607c(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xb68f96ec(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x2e73549a(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x938f3af5(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x3f27fa9a(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xd2fa7631(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdfcf84e1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x16912ca9(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xe50cda52(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x7dc076a6(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xc6f86bfd(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8ED04C36: ("unknown_0x8ed04c36", _decode_unknown_0x8ed04c36),
    0x94BB7EE5: ("unknown_0x94bb7ee5", _decode_unknown_0x94bb7ee5),
    0x2D037B5A: ("pause_screen_tweak_open_color", _decode_pause_screen_tweak_open_color),
    0x415A81F8: ("unknown_0x415a81f8", _decode_unknown_0x415a81f8),
    0xFE95100F: ("unknown_0xfe95100f", _decode_unknown_0xfe95100f),
    0xAF38A796: ("pause_screen_fullscreen_bg_color", _decode_pause_screen_fullscreen_bg_color),
    0x66733E29: ("unknown_0x66733e29", _decode_unknown_0x66733e29),
    0xFF6D31E9: ("pause_screen_frame_color", _decode_pause_screen_frame_color),
    0x9B63FFA6: ("pause_screen_icons_color", _decode_pause_screen_icons_color),
    0x7298E223: ("pause_screen_text_color", _decode_pause_screen_text_color),
    0x556481E8: ("pause_screen_highlight_color", _decode_pause_screen_highlight_color),
    0xEE8A2117: ("pause_screen_helmet_color", _decode_pause_screen_helmet_color),
    0xF468695D: ("gui_cursor_color", _decode_gui_cursor_color),
    0xDB5C8A60: ("unknown_0xdb5c8a60", _decode_unknown_0xdb5c8a60),
    0x166C22E0: ("unknown_0x166c22e0", _decode_unknown_0x166c22e0),
    0xCEC78E81: ("unknown_0xcec78e81", _decode_unknown_0xcec78e81),
    0x91338F72: ("unknown_0x91338f72", _decode_unknown_0x91338f72),
    0x2DF1EB03: ("hud_memo_text_foreground_color", _decode_hud_memo_text_foreground_color),
    0xB5DA30F4: ("hud_memo_text_outline_color", _decode_hud_memo_text_outline_color),
    0xC8DDC662: ("unknown_0xc8ddc662", _decode_unknown_0xc8ddc662),
    0x6991E2CD: ("hud_glow_color", _decode_hud_glow_color),
    0x5C336F85: ("unknown_0x5c336f85", _decode_unknown_0x5c336f85),
    0xDEFCA700: ("unknown_0xdefca700", _decode_unknown_0xdefca700),
    0xCB7DDAF4: ("selected_visor_beam_color", _decode_selected_visor_beam_color),
    0xF17911AA: ("unselected_visor_beam_color", _decode_unselected_visor_beam_color),
    0xA14C8D20: ("energy_bar_low_filled_color", _decode_energy_bar_low_filled_color),
    0xB4135CDD: ("energy_bar_low_shadow_color", _decode_energy_bar_low_shadow_color),
    0xE0290C48: ("energy_bar_low_empty_color", _decode_energy_bar_low_empty_color),
    0x1EC7F863: ("hud_damage_modulate_color", _decode_hud_damage_modulate_color),
    0xAE1317D8: ("damage_indicator_color", _decode_damage_indicator_color),
    0x22B9B01E: ("hud_title_foreground_color", _decode_hud_title_foreground_color),
    0x70A2CD6E: ("hud_title_outline_color", _decode_hud_title_outline_color),
    0xE7070332: ("unknown_0xe7070332", _decode_unknown_0xe7070332),
    0x779C7B9C: ("unknown_0x779c7b9c", _decode_unknown_0x779c7b9c),
    0x6F6E9D6D: ("energy_warning_color", _decode_energy_warning_color),
    0x0C00A29F: ("missile_warning_color", _decode_missile_warning_color),
    0x83040135: ("unknown_0x83040135", _decode_unknown_0x83040135),
    0x3C1AE0FF: ("unknown_0x3c1ae0ff", _decode_unknown_0x3c1ae0ff),
    0x29453102: ("missile_bar_shadow_color", _decode_missile_bar_shadow_color),
    0x64337CCD: ("missile_bar_empty_color", _decode_missile_bar_empty_color),
    0xBE3C29A1: ("unknown_0xbe3c29a1", _decode_unknown_0xbe3c29a1),
    0xD110A12F: ("missile_group_inactive_color", _decode_missile_group_inactive_color),
    0xCEB17CDF: ("missile_group_combo_charge_color", _decode_missile_group_combo_charge_color),
    0x4C5AFF4F: ("unknown_0x4c5aff4f", _decode_unknown_0x4c5aff4f),
    0x0B17B693: ("unknown_0x0b17b693", _decode_unknown_0x0b17b693),
    0x8B0A4C90: ("unknown_0x8b0a4c90", _decode_unknown_0x8b0a4c90),
    0xC4E17CA8: ("energy_warning_outline_color", _decode_energy_warning_outline_color),
    0xCDBD73E1: ("missile_warning_outline_color", _decode_missile_warning_outline_color),
    0x78522461: ("unknown_0x78522461", _decode_unknown_0x78522461),
    0x6A839A97: ("flash_pass_color", _decode_flash_pass_color),
    0x79EA6F12: ("unknown_0x79ea6f12", _decode_unknown_0x79ea6f12),
    0xDC901206: ("unknown_0xdc901206", _decode_unknown_0xdc901206),
    0xC54FA7BC: ("unknown_0xc54fa7bc", _decode_unknown_0xc54fa7bc),
    0x18717FA7: ("unknown_0x18717fa7", _decode_unknown_0x18717fa7),
    0x8B7D7378: ("unknown_0x8b7d7378", _decode_unknown_0x8b7d7378),
    0x867B01A2: ("unknown_0x867b01a2", _decode_unknown_0x867b01a2),
    0xC02EED79: ("unknown_0xc02eed79", _decode_unknown_0xc02eed79),
    0xE4C1BBEB: ("metroid_suck_pulse_color", _decode_metroid_suck_pulse_color),
    0xCE7C9D8D: ("unknown_0xce7c9d8d", _decode_unknown_0xce7c9d8d),
    0x13490420: ("energy_bar_damage_color", _decode_energy_bar_damage_color),
    0xAFE2D45D: ("unknown_0xafe2d45d", _decode_unknown_0xafe2d45d),
    0x2AF5AA06: ("x_ray_holo_grid_color", _decode_x_ray_holo_grid_color),
    0xD3CBE846: ("x_ray_seeker_color", _decode_x_ray_seeker_color),
    0x507B51DA: ("x_ray_seeker_ticks_color", _decode_x_ray_seeker_ticks_color),
    0xC61D97EF: ("x_ray_seeker_ticks_outer_color", _decode_x_ray_seeker_ticks_outer_color),
    0xAF0001CF: ("x_ray_top_puzzle_color", _decode_x_ray_top_puzzle_color),
    0x150A9B17: ("x_ray_bottom_puzzle_color", _decode_x_ray_bottom_puzzle_color),
    0xD66D715F: ("x_ray_left_puzzle_color", _decode_x_ray_left_puzzle_color),
    0xA8698FE8: ("x_ray_right_puzzle_color", _decode_x_ray_right_puzzle_color),
    0x4CB38E71: ("x_ray_corner_color", _decode_x_ray_corner_color),
    0xA947A67C: ("unknown_0xa947a67c", _decode_unknown_0xa947a67c),
    0x421BAE2A: ("unknown_0x421bae2a", _decode_unknown_0x421bae2a),
    0x439A3774: ("unknown_0x439a3774", _decode_unknown_0x439a3774),
    0x8EE94C81: ("unknown_0x8ee94c81", _decode_unknown_0x8ee94c81),
    0x716E6398: ("unknown_0x716e6398", _decode_unknown_0x716e6398),
    0xDACA46D4: ("steam_no_blur_color", _decode_steam_no_blur_color),
    0x0F37E756: ("unknown_0x0f37e756", _decode_unknown_0x0f37e756),
    0xF7283644: ("unknown_0xf7283644", _decode_unknown_0xf7283644),
    0x37564B7D: ("unknown_0x37564b7d", _decode_unknown_0x37564b7d),
    0x66B7EDA3: ("unknown_0x66b7eda3", _decode_unknown_0x66b7eda3),
    0xF895098F: ("unknown_0xf895098f", _decode_unknown_0xf895098f),
    0x9B27BE10: ("unknown_0x9b27be10", _decode_unknown_0x9b27be10),
    0x6C8550C9: ("unknown_0x6c8550c9", _decode_unknown_0x6c8550c9),
    0x5368A35F: ("unknown_0x5368a35f", _decode_unknown_0x5368a35f),
    0x5A807B81: ("unknown_0x5a807b81", _decode_unknown_0x5a807b81),
    0xEB63AFED: ("unknown_0xeb63afed", _decode_unknown_0xeb63afed),
    0xABDBFA5B: ("scan_images_color", _decode_scan_images_color),
    0xD3BAFAF5: ("unknown_0xd3bafaf5", _decode_unknown_0xd3bafaf5),
    0xF8B971FA: ("threat_group_damage_color", _decode_threat_group_damage_color),
    0x4F1D443E: ("unknown_0x4f1d443e", _decode_unknown_0x4f1d443e),
    0x0F6451DA: ("unknown_0x0f6451da", _decode_unknown_0x0f6451da),
    0x345E5B4E: ("scan_seeker_color", _decode_scan_seeker_color),
    0x43ED3310: ("unknown_0x43ed3310", _decode_unknown_0x43ed3310),
    0xA781ED1D: ("unknown_0xa781ed1d", _decode_unknown_0xa781ed1d),
    0x1B0F3A85: ("log_book_color", _decode_log_book_color),
    0xEB5AE665: ("log_book_frame_color", _decode_log_book_frame_color),
    0x149369FD: ("inventory_equipped_color", _decode_inventory_equipped_color),
    0x65EE03A7: ("command_text_color", _decode_command_text_color),
    0x55BB9BA8: ("command_text_outline_color", _decode_command_text_outline_color),
    0x4B03E738: ("unknown_0x4b03e738", _decode_unknown_0x4b03e738),
    0xF883607C: ("unknown_0xf883607c", _decode_unknown_0xf883607c),
    0xB68F96EC: ("unknown_0xb68f96ec", _decode_unknown_0xb68f96ec),
    0x2E73549A: ("unknown_0x2e73549a", _decode_unknown_0x2e73549a),
    0x938F3AF5: ("unknown_0x938f3af5", _decode_unknown_0x938f3af5),
    0x3F27FA9A: ("unknown_0x3f27fa9a", _decode_unknown_0x3f27fa9a),
    0xD2FA7631: ("unknown_0xd2fa7631", _decode_unknown_0xd2fa7631),
    0xDFCF84E1: ("unknown_0xdfcf84e1", _decode_unknown_0xdfcf84e1),
    0x16912CA9: ("unknown_0x16912ca9", _decode_unknown_0x16912ca9),
    0xE50CDA52: ("unknown_0xe50cda52", _decode_unknown_0xe50cda52),
    0x7DC076A6: ("unknown_0x7dc076a6", _decode_unknown_0x7dc076a6),
    0xC6F86BFD: ("unknown_0xc6f86bfd", _decode_unknown_0xc6f86bfd),
    0xBFFFE95A: ("unknown_0xbfffe95a", structs.decode_BIG_l),
}
