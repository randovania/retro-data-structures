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
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakGui_LogBookJson(typing_extensions.TypedDict):
        main_window_border_color: json_util.JsonValue
        main_window_text_color: json_util.JsonValue
        main_window_selected_text_color: json_util.JsonValue
        unknown_0xfe98f30e: json_util.JsonValue
        unknown_0x39e57ac0: json_util.JsonValue
        legend_background_color: json_util.JsonValue
        node_color: json_util.JsonValue
        selected_node_color: json_util.JsonValue
        parent_node_color: json_util.JsonValue
        unknown_0x56843943: json_util.JsonValue
        selected_text_cursor_color: json_util.JsonValue
        unknown_0x905ce2c0: float
        text_scale: float
        selected_text_scale: float
        transition_time: float
        node_collapse_motion: json_util.JsonObject
        selected_node_collapse_motion: json_util.JsonObject
        node_expand_motion: json_util.JsonObject
        rotation_speed: float
        node_scale: float
        selected_node_scale: float
        selected_text_cursor_scale: float
        scan_model_scale: float
        unknown_0x925b9d4a: json_util.JsonObject
        unknown_0x075a0734: json_util.JsonValue
        unknown_0x8ef43309: float
        fog_near: float
        fog_far: float
        fog_color: json_util.JsonValue
        unknown_0xeef15783: float
        unknown_0x78055ab2: float
        unknown_0x09e3197f: float
        unknown_0xfaffce1f: float
        unknown_0xe5280e7c: float
        background_sweep_color: json_util.JsonValue
        background_sweep_radius: float
        background_sweep_time: float
        scan_text_window_background_color: json_util.JsonValue
        scan_text_window_border_color: json_util.JsonValue
        scan_text_window_font_color: json_util.JsonValue
        legend_window_background_color: json_util.JsonValue
        legend_window_border_color: json_util.JsonValue
        legend_window_font_color: json_util.JsonValue
        legend_hide_time: float
        unknown_0x7f35c573: json_util.JsonValue
        unknown_0xe0d77cf1: json_util.JsonValue
        unknown_0x903d9b7e: json_util.JsonValue
        unknown_0x0fdf22fc: json_util.JsonValue
        unknown_0xbeaf9d6b: json_util.JsonValue
        unknown_0x7e8247d6: json_util.JsonValue
        unknown_0x8b3f7902: json_util.JsonValue
        unknown_0xdc1abb82: json_util.JsonValue
        unknown_0x306b2b24: json_util.JsonValue
        frame_color: json_util.JsonValue
        unknown_0x1a4b8068: json_util.JsonValue
        slider_background_color: json_util.JsonValue
        slider_selection_color: json_util.JsonValue
        slider_scale: float
        slider_speed: float
        unknown_0x58795865: float
        unknown_0x35e0bd31: float
        menu_option_color: json_util.JsonValue
        menu_option_enabled_arrow_color: json_util.JsonValue
        menu_option_disabled_arrow_color: json_util.JsonValue
        menu_option_scale: float
        menu_option_arrow_scale: float
        model_rotation_speed: float
        unknown_0x60914b79: float
        unknown_0x1fd44d9b: float
        model_light1_position: json_util.JsonValue
        model_light1_color: json_util.JsonValue
        model_light2_position: json_util.JsonValue
        model_light2_color: json_util.JsonValue
        model_ambient_light_color: json_util.JsonValue


@dataclasses.dataclass()
class TweakGui_LogBook(BaseProperty):
    main_window_border_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xBA5A65C8,
                original_name="MainWindowBorderColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    main_window_text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xBFF0E37B,
                original_name="MainWindowTextColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    main_window_selected_text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x28B49A88,
                original_name="MainWindowSelectedTextColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xfe98f30e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xFE98F30E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x39e57ac0: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x39E57AC0, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    legend_background_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xA6B633FA,
                original_name="LegendBackgroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    node_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xAC80013B, original_name="NodeColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    selected_node_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x5946B439,
                original_name="SelectedNodeColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    parent_node_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xC5AA728C, original_name="ParentNodeColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x56843943: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x56843943, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    selected_text_cursor_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x6BD4783A,
                original_name="SelectedTextCursorColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x905ce2c0: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x905CE2C0, original_name="Unknown"),
        },
    )
    text_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5FA64C77, original_name="TextScale"),
        },
    )
    selected_text_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAA60F975, original_name="SelectedTextScale"),
        },
    )
    transition_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1832935E, original_name="TransitionTime"),
        },
    )
    node_collapse_motion: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x165943F6,
                original_name="NodeCollapseMotion",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    selected_node_collapse_motion: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x9AD04DD7,
                original_name="SelectedNodeCollapseMotion",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    node_expand_motion: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x08719A9C,
                original_name="NodeExpandMotion",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    rotation_speed: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x11CD076F, original_name="RotationSpeed"),
        },
    )
    node_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB71677D0, original_name="NodeScale"),
        },
    )
    selected_node_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x42D0C2D2, original_name="SelectedNodeScale"),
        },
    )
    selected_text_cursor_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x70420ED1, original_name="SelectedTextCursorScale"),
        },
    )
    scan_model_scale: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC0CB3936, original_name="ScanModelScale"),
        },
    )
    unknown_0x925b9d4a: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x925B9D4A, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x075a0734: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x075A0734, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x8ef43309: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8EF43309, original_name="Unknown"),
        },
    )
    fog_near: float = dataclasses.field(
        default=11.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4194622E, original_name="FogNear"),
        },
    )
    fog_far: float = dataclasses.field(
        default=18.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3935A756, original_name="FogFar"),
        },
    )
    fog_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE578C0DD, original_name="FogColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xeef15783: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEEF15783, original_name="Unknown"),
        },
    )
    unknown_0x78055ab2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78055AB2, original_name="Unknown"),
        },
    )
    unknown_0x09e3197f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x09E3197F, original_name="Unknown"),
        },
    )
    unknown_0xfaffce1f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFAFFCE1F, original_name="Unknown"),
        },
    )
    unknown_0xe5280e7c: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE5280E7C, original_name="Unknown"),
        },
    )
    background_sweep_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x647D9F91,
                original_name="BackgroundSweepColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    background_sweep_radius: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7120F18F, original_name="BackgroundSweepRadius"),
        },
    )
    background_sweep_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4DEF660D, original_name="BackgroundSweepTime"),
        },
    )
    scan_text_window_background_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xC7C1967B,
                original_name="ScanTextWindowBackgroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    scan_text_window_border_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xF74BBAD2,
                original_name="ScanTextWindowBorderColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    scan_text_window_font_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xE31421E2,
                original_name="ScanTextWindowFontColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    legend_window_background_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x0B8F0DDB,
                original_name="LegendWindowBackgroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    legend_window_border_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x0A7A4155,
                original_name="LegendWindowBorderColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    legend_window_font_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x527A0B10,
                original_name="LegendWindowFontColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    legend_hide_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7927CA67, original_name="LegendHideTime"),
        },
    )
    unknown_0x7f35c573: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7F35C573, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xe0d77cf1: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE0D77CF1, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x903d9b7e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x903D9B7E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x0fdf22fc: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0FDF22FC, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xbeaf9d6b: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xBEAF9D6B, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x7e8247d6: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7E8247D6, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x8b3f7902: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x8B3F7902, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdc1abb82: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDC1ABB82, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x306b2b24: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x306B2B24, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    frame_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA485372C, original_name="FrameColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x1a4b8068: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1A4B8068, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    slider_background_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xCC2F25F1,
                original_name="SliderBackgroundColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    slider_selection_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xCB8D5CAF,
                original_name="SliderSelectionColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    slider_scale: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3F44254F, original_name="SliderScale"),
        },
    )
    slider_speed: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7087C377, original_name="SliderSpeed"),
        },
    )
    unknown_0x58795865: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x58795865, original_name="Unknown"),
        },
    )
    unknown_0x35e0bd31: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x35E0BD31, original_name="Unknown"),
        },
    )
    menu_option_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE7C283BE, original_name="MenuOptionColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    menu_option_enabled_arrow_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xDABCB730,
                original_name="MenuOptionEnabledArrowColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    menu_option_disabled_arrow_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x9C2195D7,
                original_name="MenuOptionDisabledArrowColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    menu_option_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFC54F555, original_name="MenuOptionScale"),
        },
    )
    menu_option_arrow_scale: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEF549530, original_name="MenuOptionArrowScale"),
        },
    )
    model_rotation_speed: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFA7A92B8, original_name="ModelRotationSpeed"),
        },
    )
    unknown_0x60914b79: float = dataclasses.field(
        default=-80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x60914B79, original_name="Unknown"),
        },
    )
    unknown_0x1fd44d9b: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1FD44D9B, original_name="Unknown"),
        },
    )
    model_light1_position: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x06C93AFA,
                original_name="ModelLight1Position",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    model_light1_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x33924AFB, original_name="ModelLight1Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    model_light2_position: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x17B45083,
                original_name="ModelLight2Position",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    model_light2_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xAA702CFA, original_name="ModelLight2Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    model_ambient_light_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x62FF6D72,
                original_name="ModelAmbientLightColor",
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
        if property_count != 74:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA5A65C8
        main_window_border_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFF0E37B
        main_window_text_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28B49A88
        main_window_selected_text_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE98F30E
        unknown_0xfe98f30e = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39E57AC0
        unknown_0x39e57ac0 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6B633FA
        legend_background_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC80013B
        node_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5946B439
        selected_node_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5AA728C
        parent_node_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56843943
        unknown_0x56843943 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BD4783A
        selected_text_cursor_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x905CE2C0
        unknown_0x905ce2c0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FA64C77
        text_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA60F975
        selected_text_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1832935E
        transition_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x165943F6
        node_collapse_motion = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AD04DD7
        selected_node_collapse_motion = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08719A9C
        node_expand_motion = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11CD076F
        rotation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB71677D0
        node_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42D0C2D2
        selected_node_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70420ED1
        selected_text_cursor_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC0CB3936
        scan_model_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x925B9D4A
        unknown_0x925b9d4a = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x075A0734
        unknown_0x075a0734 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8EF43309
        unknown_0x8ef43309 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4194622E
        fog_near = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3935A756
        fog_far = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE578C0DD
        fog_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEEF15783
        unknown_0xeef15783 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78055AB2
        unknown_0x78055ab2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09E3197F
        unknown_0x09e3197f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFAFFCE1F
        unknown_0xfaffce1f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE5280E7C
        unknown_0xe5280e7c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x647D9F91
        background_sweep_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7120F18F
        background_sweep_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4DEF660D
        background_sweep_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7C1967B
        scan_text_window_background_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF74BBAD2
        scan_text_window_border_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE31421E2
        scan_text_window_font_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B8F0DDB
        legend_window_background_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A7A4155
        legend_window_border_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x527A0B10
        legend_window_font_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7927CA67
        legend_hide_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F35C573
        unknown_0x7f35c573 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0D77CF1
        unknown_0xe0d77cf1 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x903D9B7E
        unknown_0x903d9b7e = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FDF22FC
        unknown_0x0fdf22fc = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBEAF9D6B
        unknown_0xbeaf9d6b = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E8247D6
        unknown_0x7e8247d6 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B3F7902
        unknown_0x8b3f7902 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC1ABB82
        unknown_0xdc1abb82 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x306B2B24
        unknown_0x306b2b24 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA485372C
        frame_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A4B8068
        unknown_0x1a4b8068 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC2F25F1
        slider_background_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB8D5CAF
        slider_selection_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3F44254F
        slider_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7087C377
        slider_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58795865
        unknown_0x58795865 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35E0BD31
        unknown_0x35e0bd31 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7C283BE
        menu_option_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDABCB730
        menu_option_enabled_arrow_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C2195D7
        menu_option_disabled_arrow_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC54F555
        menu_option_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF549530
        menu_option_arrow_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFA7A92B8
        model_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60914B79
        unknown_0x60914b79 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1FD44D9B
        unknown_0x1fd44d9b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06C93AFA
        model_light1_position = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33924AFB
        model_light1_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17B45083
        model_light2_position = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA702CFA
        model_light2_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62FF6D72
        model_ambient_light_color = Color.from_stream(data, game, property_size)

        return cls(
            main_window_border_color,
            main_window_text_color,
            main_window_selected_text_color,
            unknown_0xfe98f30e,
            unknown_0x39e57ac0,
            legend_background_color,
            node_color,
            selected_node_color,
            parent_node_color,
            unknown_0x56843943,
            selected_text_cursor_color,
            unknown_0x905ce2c0,
            text_scale,
            selected_text_scale,
            transition_time,
            node_collapse_motion,
            selected_node_collapse_motion,
            node_expand_motion,
            rotation_speed,
            node_scale,
            selected_node_scale,
            selected_text_cursor_scale,
            scan_model_scale,
            unknown_0x925b9d4a,
            unknown_0x075a0734,
            unknown_0x8ef43309,
            fog_near,
            fog_far,
            fog_color,
            unknown_0xeef15783,
            unknown_0x78055ab2,
            unknown_0x09e3197f,
            unknown_0xfaffce1f,
            unknown_0xe5280e7c,
            background_sweep_color,
            background_sweep_radius,
            background_sweep_time,
            scan_text_window_background_color,
            scan_text_window_border_color,
            scan_text_window_font_color,
            legend_window_background_color,
            legend_window_border_color,
            legend_window_font_color,
            legend_hide_time,
            unknown_0x7f35c573,
            unknown_0xe0d77cf1,
            unknown_0x903d9b7e,
            unknown_0x0fdf22fc,
            unknown_0xbeaf9d6b,
            unknown_0x7e8247d6,
            unknown_0x8b3f7902,
            unknown_0xdc1abb82,
            unknown_0x306b2b24,
            frame_color,
            unknown_0x1a4b8068,
            slider_background_color,
            slider_selection_color,
            slider_scale,
            slider_speed,
            unknown_0x58795865,
            unknown_0x35e0bd31,
            menu_option_color,
            menu_option_enabled_arrow_color,
            menu_option_disabled_arrow_color,
            menu_option_scale,
            menu_option_arrow_scale,
            model_rotation_speed,
            unknown_0x60914b79,
            unknown_0x1fd44d9b,
            model_light1_position,
            model_light1_color,
            model_light2_position,
            model_light2_color,
            model_ambient_light_color,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00J")  # 74 properties

        data.write(b"\xbaZe\xc8")  # 0xba5a65c8
        data.write(b"\x00\x10")  # size
        self.main_window_border_color.to_stream(data, game)

        data.write(b"\xbf\xf0\xe3{")  # 0xbff0e37b
        data.write(b"\x00\x10")  # size
        self.main_window_text_color.to_stream(data, game)

        data.write(b"(\xb4\x9a\x88")  # 0x28b49a88
        data.write(b"\x00\x10")  # size
        self.main_window_selected_text_color.to_stream(data, game)

        data.write(b"\xfe\x98\xf3\x0e")  # 0xfe98f30e
        data.write(b"\x00\x10")  # size
        self.unknown_0xfe98f30e.to_stream(data, game)

        data.write(b"9\xe5z\xc0")  # 0x39e57ac0
        data.write(b"\x00\x10")  # size
        self.unknown_0x39e57ac0.to_stream(data, game)

        data.write(b"\xa6\xb63\xfa")  # 0xa6b633fa
        data.write(b"\x00\x10")  # size
        self.legend_background_color.to_stream(data, game)

        data.write(b"\xac\x80\x01;")  # 0xac80013b
        data.write(b"\x00\x10")  # size
        self.node_color.to_stream(data, game)

        data.write(b"YF\xb49")  # 0x5946b439
        data.write(b"\x00\x10")  # size
        self.selected_node_color.to_stream(data, game)

        data.write(b"\xc5\xaar\x8c")  # 0xc5aa728c
        data.write(b"\x00\x10")  # size
        self.parent_node_color.to_stream(data, game)

        data.write(b"V\x849C")  # 0x56843943
        data.write(b"\x00\x10")  # size
        self.unknown_0x56843943.to_stream(data, game)

        data.write(b"k\xd4x:")  # 0x6bd4783a
        data.write(b"\x00\x10")  # size
        self.selected_text_cursor_color.to_stream(data, game)

        data.write(b"\x90\\\xe2\xc0")  # 0x905ce2c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x905ce2c0))

        data.write(b"_\xa6Lw")  # 0x5fa64c77
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.text_scale))

        data.write(b"\xaa`\xf9u")  # 0xaa60f975
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.selected_text_scale))

        data.write(b"\x182\x93^")  # 0x1832935e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.transition_time))

        data.write(b"\x16YC\xf6")  # 0x165943f6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.node_collapse_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9a\xd0M\xd7")  # 0x9ad04dd7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.selected_node_collapse_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x08q\x9a\x9c")  # 0x8719a9c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.node_expand_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x11\xcd\x07o")  # 0x11cd076f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_speed))

        data.write(b"\xb7\x16w\xd0")  # 0xb71677d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.node_scale))

        data.write(b"B\xd0\xc2\xd2")  # 0x42d0c2d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.selected_node_scale))

        data.write(b"pB\x0e\xd1")  # 0x70420ed1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.selected_text_cursor_scale))

        data.write(b"\xc0\xcb96")  # 0xc0cb3936
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_model_scale))

        data.write(b"\x92[\x9dJ")  # 0x925b9d4a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x925b9d4a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x07Z\x074")  # 0x75a0734
        data.write(b"\x00\x10")  # size
        self.unknown_0x075a0734.to_stream(data, game)

        data.write(b"\x8e\xf43\t")  # 0x8ef43309
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8ef43309))

        data.write(b"A\x94b.")  # 0x4194622e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fog_near))

        data.write(b"95\xa7V")  # 0x3935a756
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fog_far))

        data.write(b"\xe5x\xc0\xdd")  # 0xe578c0dd
        data.write(b"\x00\x10")  # size
        self.fog_color.to_stream(data, game)

        data.write(b"\xee\xf1W\x83")  # 0xeef15783
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeef15783))

        data.write(b"x\x05Z\xb2")  # 0x78055ab2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78055ab2))

        data.write(b"\t\xe3\x19\x7f")  # 0x9e3197f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x09e3197f))

        data.write(b"\xfa\xff\xce\x1f")  # 0xfaffce1f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfaffce1f))

        data.write(b"\xe5(\x0e|")  # 0xe5280e7c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe5280e7c))

        data.write(b"d}\x9f\x91")  # 0x647d9f91
        data.write(b"\x00\x10")  # size
        self.background_sweep_color.to_stream(data, game)

        data.write(b"q \xf1\x8f")  # 0x7120f18f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.background_sweep_radius))

        data.write(b"M\xeff\r")  # 0x4def660d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.background_sweep_time))

        data.write(b"\xc7\xc1\x96{")  # 0xc7c1967b
        data.write(b"\x00\x10")  # size
        self.scan_text_window_background_color.to_stream(data, game)

        data.write(b"\xf7K\xba\xd2")  # 0xf74bbad2
        data.write(b"\x00\x10")  # size
        self.scan_text_window_border_color.to_stream(data, game)

        data.write(b"\xe3\x14!\xe2")  # 0xe31421e2
        data.write(b"\x00\x10")  # size
        self.scan_text_window_font_color.to_stream(data, game)

        data.write(b"\x0b\x8f\r\xdb")  # 0xb8f0ddb
        data.write(b"\x00\x10")  # size
        self.legend_window_background_color.to_stream(data, game)

        data.write(b"\nzAU")  # 0xa7a4155
        data.write(b"\x00\x10")  # size
        self.legend_window_border_color.to_stream(data, game)

        data.write(b"Rz\x0b\x10")  # 0x527a0b10
        data.write(b"\x00\x10")  # size
        self.legend_window_font_color.to_stream(data, game)

        data.write(b"y'\xcag")  # 0x7927ca67
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.legend_hide_time))

        data.write(b"\x7f5\xc5s")  # 0x7f35c573
        data.write(b"\x00\x10")  # size
        self.unknown_0x7f35c573.to_stream(data, game)

        data.write(b"\xe0\xd7|\xf1")  # 0xe0d77cf1
        data.write(b"\x00\x10")  # size
        self.unknown_0xe0d77cf1.to_stream(data, game)

        data.write(b"\x90=\x9b~")  # 0x903d9b7e
        data.write(b"\x00\x10")  # size
        self.unknown_0x903d9b7e.to_stream(data, game)

        data.write(b'\x0f\xdf"\xfc')  # 0xfdf22fc
        data.write(b"\x00\x10")  # size
        self.unknown_0x0fdf22fc.to_stream(data, game)

        data.write(b"\xbe\xaf\x9dk")  # 0xbeaf9d6b
        data.write(b"\x00\x10")  # size
        self.unknown_0xbeaf9d6b.to_stream(data, game)

        data.write(b"~\x82G\xd6")  # 0x7e8247d6
        data.write(b"\x00\x10")  # size
        self.unknown_0x7e8247d6.to_stream(data, game)

        data.write(b"\x8b?y\x02")  # 0x8b3f7902
        data.write(b"\x00\x10")  # size
        self.unknown_0x8b3f7902.to_stream(data, game)

        data.write(b"\xdc\x1a\xbb\x82")  # 0xdc1abb82
        data.write(b"\x00\x10")  # size
        self.unknown_0xdc1abb82.to_stream(data, game)

        data.write(b"0k+$")  # 0x306b2b24
        data.write(b"\x00\x10")  # size
        self.unknown_0x306b2b24.to_stream(data, game)

        data.write(b"\xa4\x857,")  # 0xa485372c
        data.write(b"\x00\x10")  # size
        self.frame_color.to_stream(data, game)

        data.write(b"\x1aK\x80h")  # 0x1a4b8068
        data.write(b"\x00\x10")  # size
        self.unknown_0x1a4b8068.to_stream(data, game)

        data.write(b"\xcc/%\xf1")  # 0xcc2f25f1
        data.write(b"\x00\x10")  # size
        self.slider_background_color.to_stream(data, game)

        data.write(b"\xcb\x8d\\\xaf")  # 0xcb8d5caf
        data.write(b"\x00\x10")  # size
        self.slider_selection_color.to_stream(data, game)

        data.write(b"?D%O")  # 0x3f44254f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.slider_scale))

        data.write(b"p\x87\xc3w")  # 0x7087c377
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.slider_speed))

        data.write(b"XyXe")  # 0x58795865
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x58795865))

        data.write(b"5\xe0\xbd1")  # 0x35e0bd31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x35e0bd31))

        data.write(b"\xe7\xc2\x83\xbe")  # 0xe7c283be
        data.write(b"\x00\x10")  # size
        self.menu_option_color.to_stream(data, game)

        data.write(b"\xda\xbc\xb70")  # 0xdabcb730
        data.write(b"\x00\x10")  # size
        self.menu_option_enabled_arrow_color.to_stream(data, game)

        data.write(b"\x9c!\x95\xd7")  # 0x9c2195d7
        data.write(b"\x00\x10")  # size
        self.menu_option_disabled_arrow_color.to_stream(data, game)

        data.write(b"\xfcT\xf5U")  # 0xfc54f555
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.menu_option_scale))

        data.write(b"\xefT\x950")  # 0xef549530
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.menu_option_arrow_scale))

        data.write(b"\xfaz\x92\xb8")  # 0xfa7a92b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.model_rotation_speed))

        data.write(b"`\x91Ky")  # 0x60914b79
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x60914b79))

        data.write(b"\x1f\xd4M\x9b")  # 0x1fd44d9b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1fd44d9b))

        data.write(b"\x06\xc9:\xfa")  # 0x6c93afa
        data.write(b"\x00\x0c")  # size
        self.model_light1_position.to_stream(data, game)

        data.write(b"3\x92J\xfb")  # 0x33924afb
        data.write(b"\x00\x10")  # size
        self.model_light1_color.to_stream(data, game)

        data.write(b"\x17\xb4P\x83")  # 0x17b45083
        data.write(b"\x00\x0c")  # size
        self.model_light2_position.to_stream(data, game)

        data.write(b"\xaap,\xfa")  # 0xaa702cfa
        data.write(b"\x00\x10")  # size
        self.model_light2_color.to_stream(data, game)

        data.write(b"b\xffmr")  # 0x62ff6d72
        data.write(b"\x00\x10")  # size
        self.model_ambient_light_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_LogBookJson", data)
        return cls(
            main_window_border_color=Color.from_json(json_data["main_window_border_color"]),
            main_window_text_color=Color.from_json(json_data["main_window_text_color"]),
            main_window_selected_text_color=Color.from_json(json_data["main_window_selected_text_color"]),
            unknown_0xfe98f30e=Color.from_json(json_data["unknown_0xfe98f30e"]),
            unknown_0x39e57ac0=Color.from_json(json_data["unknown_0x39e57ac0"]),
            legend_background_color=Color.from_json(json_data["legend_background_color"]),
            node_color=Color.from_json(json_data["node_color"]),
            selected_node_color=Color.from_json(json_data["selected_node_color"]),
            parent_node_color=Color.from_json(json_data["parent_node_color"]),
            unknown_0x56843943=Color.from_json(json_data["unknown_0x56843943"]),
            selected_text_cursor_color=Color.from_json(json_data["selected_text_cursor_color"]),
            unknown_0x905ce2c0=json_data["unknown_0x905ce2c0"],
            text_scale=json_data["text_scale"],
            selected_text_scale=json_data["selected_text_scale"],
            transition_time=json_data["transition_time"],
            node_collapse_motion=Spline.from_json(json_data["node_collapse_motion"]),
            selected_node_collapse_motion=Spline.from_json(json_data["selected_node_collapse_motion"]),
            node_expand_motion=Spline.from_json(json_data["node_expand_motion"]),
            rotation_speed=json_data["rotation_speed"],
            node_scale=json_data["node_scale"],
            selected_node_scale=json_data["selected_node_scale"],
            selected_text_cursor_scale=json_data["selected_text_cursor_scale"],
            scan_model_scale=json_data["scan_model_scale"],
            unknown_0x925b9d4a=Spline.from_json(json_data["unknown_0x925b9d4a"]),
            unknown_0x075a0734=Color.from_json(json_data["unknown_0x075a0734"]),
            unknown_0x8ef43309=json_data["unknown_0x8ef43309"],
            fog_near=json_data["fog_near"],
            fog_far=json_data["fog_far"],
            fog_color=Color.from_json(json_data["fog_color"]),
            unknown_0xeef15783=json_data["unknown_0xeef15783"],
            unknown_0x78055ab2=json_data["unknown_0x78055ab2"],
            unknown_0x09e3197f=json_data["unknown_0x09e3197f"],
            unknown_0xfaffce1f=json_data["unknown_0xfaffce1f"],
            unknown_0xe5280e7c=json_data["unknown_0xe5280e7c"],
            background_sweep_color=Color.from_json(json_data["background_sweep_color"]),
            background_sweep_radius=json_data["background_sweep_radius"],
            background_sweep_time=json_data["background_sweep_time"],
            scan_text_window_background_color=Color.from_json(json_data["scan_text_window_background_color"]),
            scan_text_window_border_color=Color.from_json(json_data["scan_text_window_border_color"]),
            scan_text_window_font_color=Color.from_json(json_data["scan_text_window_font_color"]),
            legend_window_background_color=Color.from_json(json_data["legend_window_background_color"]),
            legend_window_border_color=Color.from_json(json_data["legend_window_border_color"]),
            legend_window_font_color=Color.from_json(json_data["legend_window_font_color"]),
            legend_hide_time=json_data["legend_hide_time"],
            unknown_0x7f35c573=Color.from_json(json_data["unknown_0x7f35c573"]),
            unknown_0xe0d77cf1=Color.from_json(json_data["unknown_0xe0d77cf1"]),
            unknown_0x903d9b7e=Color.from_json(json_data["unknown_0x903d9b7e"]),
            unknown_0x0fdf22fc=Color.from_json(json_data["unknown_0x0fdf22fc"]),
            unknown_0xbeaf9d6b=Color.from_json(json_data["unknown_0xbeaf9d6b"]),
            unknown_0x7e8247d6=Color.from_json(json_data["unknown_0x7e8247d6"]),
            unknown_0x8b3f7902=Color.from_json(json_data["unknown_0x8b3f7902"]),
            unknown_0xdc1abb82=Color.from_json(json_data["unknown_0xdc1abb82"]),
            unknown_0x306b2b24=Color.from_json(json_data["unknown_0x306b2b24"]),
            frame_color=Color.from_json(json_data["frame_color"]),
            unknown_0x1a4b8068=Color.from_json(json_data["unknown_0x1a4b8068"]),
            slider_background_color=Color.from_json(json_data["slider_background_color"]),
            slider_selection_color=Color.from_json(json_data["slider_selection_color"]),
            slider_scale=json_data["slider_scale"],
            slider_speed=json_data["slider_speed"],
            unknown_0x58795865=json_data["unknown_0x58795865"],
            unknown_0x35e0bd31=json_data["unknown_0x35e0bd31"],
            menu_option_color=Color.from_json(json_data["menu_option_color"]),
            menu_option_enabled_arrow_color=Color.from_json(json_data["menu_option_enabled_arrow_color"]),
            menu_option_disabled_arrow_color=Color.from_json(json_data["menu_option_disabled_arrow_color"]),
            menu_option_scale=json_data["menu_option_scale"],
            menu_option_arrow_scale=json_data["menu_option_arrow_scale"],
            model_rotation_speed=json_data["model_rotation_speed"],
            unknown_0x60914b79=json_data["unknown_0x60914b79"],
            unknown_0x1fd44d9b=json_data["unknown_0x1fd44d9b"],
            model_light1_position=Vector.from_json(json_data["model_light1_position"]),
            model_light1_color=Color.from_json(json_data["model_light1_color"]),
            model_light2_position=Vector.from_json(json_data["model_light2_position"]),
            model_light2_color=Color.from_json(json_data["model_light2_color"]),
            model_ambient_light_color=Color.from_json(json_data["model_ambient_light_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "main_window_border_color": self.main_window_border_color.to_json(),
            "main_window_text_color": self.main_window_text_color.to_json(),
            "main_window_selected_text_color": self.main_window_selected_text_color.to_json(),
            "unknown_0xfe98f30e": self.unknown_0xfe98f30e.to_json(),
            "unknown_0x39e57ac0": self.unknown_0x39e57ac0.to_json(),
            "legend_background_color": self.legend_background_color.to_json(),
            "node_color": self.node_color.to_json(),
            "selected_node_color": self.selected_node_color.to_json(),
            "parent_node_color": self.parent_node_color.to_json(),
            "unknown_0x56843943": self.unknown_0x56843943.to_json(),
            "selected_text_cursor_color": self.selected_text_cursor_color.to_json(),
            "unknown_0x905ce2c0": self.unknown_0x905ce2c0,
            "text_scale": self.text_scale,
            "selected_text_scale": self.selected_text_scale,
            "transition_time": self.transition_time,
            "node_collapse_motion": self.node_collapse_motion.to_json(),
            "selected_node_collapse_motion": self.selected_node_collapse_motion.to_json(),
            "node_expand_motion": self.node_expand_motion.to_json(),
            "rotation_speed": self.rotation_speed,
            "node_scale": self.node_scale,
            "selected_node_scale": self.selected_node_scale,
            "selected_text_cursor_scale": self.selected_text_cursor_scale,
            "scan_model_scale": self.scan_model_scale,
            "unknown_0x925b9d4a": self.unknown_0x925b9d4a.to_json(),
            "unknown_0x075a0734": self.unknown_0x075a0734.to_json(),
            "unknown_0x8ef43309": self.unknown_0x8ef43309,
            "fog_near": self.fog_near,
            "fog_far": self.fog_far,
            "fog_color": self.fog_color.to_json(),
            "unknown_0xeef15783": self.unknown_0xeef15783,
            "unknown_0x78055ab2": self.unknown_0x78055ab2,
            "unknown_0x09e3197f": self.unknown_0x09e3197f,
            "unknown_0xfaffce1f": self.unknown_0xfaffce1f,
            "unknown_0xe5280e7c": self.unknown_0xe5280e7c,
            "background_sweep_color": self.background_sweep_color.to_json(),
            "background_sweep_radius": self.background_sweep_radius,
            "background_sweep_time": self.background_sweep_time,
            "scan_text_window_background_color": self.scan_text_window_background_color.to_json(),
            "scan_text_window_border_color": self.scan_text_window_border_color.to_json(),
            "scan_text_window_font_color": self.scan_text_window_font_color.to_json(),
            "legend_window_background_color": self.legend_window_background_color.to_json(),
            "legend_window_border_color": self.legend_window_border_color.to_json(),
            "legend_window_font_color": self.legend_window_font_color.to_json(),
            "legend_hide_time": self.legend_hide_time,
            "unknown_0x7f35c573": self.unknown_0x7f35c573.to_json(),
            "unknown_0xe0d77cf1": self.unknown_0xe0d77cf1.to_json(),
            "unknown_0x903d9b7e": self.unknown_0x903d9b7e.to_json(),
            "unknown_0x0fdf22fc": self.unknown_0x0fdf22fc.to_json(),
            "unknown_0xbeaf9d6b": self.unknown_0xbeaf9d6b.to_json(),
            "unknown_0x7e8247d6": self.unknown_0x7e8247d6.to_json(),
            "unknown_0x8b3f7902": self.unknown_0x8b3f7902.to_json(),
            "unknown_0xdc1abb82": self.unknown_0xdc1abb82.to_json(),
            "unknown_0x306b2b24": self.unknown_0x306b2b24.to_json(),
            "frame_color": self.frame_color.to_json(),
            "unknown_0x1a4b8068": self.unknown_0x1a4b8068.to_json(),
            "slider_background_color": self.slider_background_color.to_json(),
            "slider_selection_color": self.slider_selection_color.to_json(),
            "slider_scale": self.slider_scale,
            "slider_speed": self.slider_speed,
            "unknown_0x58795865": self.unknown_0x58795865,
            "unknown_0x35e0bd31": self.unknown_0x35e0bd31,
            "menu_option_color": self.menu_option_color.to_json(),
            "menu_option_enabled_arrow_color": self.menu_option_enabled_arrow_color.to_json(),
            "menu_option_disabled_arrow_color": self.menu_option_disabled_arrow_color.to_json(),
            "menu_option_scale": self.menu_option_scale,
            "menu_option_arrow_scale": self.menu_option_arrow_scale,
            "model_rotation_speed": self.model_rotation_speed,
            "unknown_0x60914b79": self.unknown_0x60914b79,
            "unknown_0x1fd44d9b": self.unknown_0x1fd44d9b,
            "model_light1_position": self.model_light1_position.to_json(),
            "model_light1_color": self.model_light1_color.to_json(),
            "model_light2_position": self.model_light2_position.to_json(),
            "model_light2_color": self.model_light2_color.to_json(),
            "model_ambient_light_color": self.model_ambient_light_color.to_json(),
        }


def _decode_main_window_border_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_main_window_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_main_window_selected_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xfe98f30e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x39e57ac0(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_node_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_selected_node_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_parent_node_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x56843943(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_selected_text_cursor_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_node_collapse_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_selected_node_collapse_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_node_expand_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x925b9d4a(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x075a0734(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_background_sweep_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_text_window_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_text_window_border_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_text_window_font_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_window_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_window_border_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_window_font_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x7f35c573(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xe0d77cf1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x903d9b7e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x0fdf22fc(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xbeaf9d6b(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x7e8247d6(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x8b3f7902(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdc1abb82(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x306b2b24(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x1a4b8068(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_slider_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_slider_selection_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_menu_option_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_menu_option_enabled_arrow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_menu_option_disabled_arrow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_model_light1_position(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_model_light1_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_model_light2_position(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_model_light2_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_model_ambient_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xBA5A65C8: ("main_window_border_color", _decode_main_window_border_color),
    0xBFF0E37B: ("main_window_text_color", _decode_main_window_text_color),
    0x28B49A88: ("main_window_selected_text_color", _decode_main_window_selected_text_color),
    0xFE98F30E: ("unknown_0xfe98f30e", _decode_unknown_0xfe98f30e),
    0x39E57AC0: ("unknown_0x39e57ac0", _decode_unknown_0x39e57ac0),
    0xA6B633FA: ("legend_background_color", _decode_legend_background_color),
    0xAC80013B: ("node_color", _decode_node_color),
    0x5946B439: ("selected_node_color", _decode_selected_node_color),
    0xC5AA728C: ("parent_node_color", _decode_parent_node_color),
    0x56843943: ("unknown_0x56843943", _decode_unknown_0x56843943),
    0x6BD4783A: ("selected_text_cursor_color", _decode_selected_text_cursor_color),
    0x905CE2C0: ("unknown_0x905ce2c0", structs.decode_BIG_f),
    0x5FA64C77: ("text_scale", structs.decode_BIG_f),
    0xAA60F975: ("selected_text_scale", structs.decode_BIG_f),
    0x1832935E: ("transition_time", structs.decode_BIG_f),
    0x165943F6: ("node_collapse_motion", _decode_node_collapse_motion),
    0x9AD04DD7: ("selected_node_collapse_motion", _decode_selected_node_collapse_motion),
    0x08719A9C: ("node_expand_motion", _decode_node_expand_motion),
    0x11CD076F: ("rotation_speed", structs.decode_BIG_f),
    0xB71677D0: ("node_scale", structs.decode_BIG_f),
    0x42D0C2D2: ("selected_node_scale", structs.decode_BIG_f),
    0x70420ED1: ("selected_text_cursor_scale", structs.decode_BIG_f),
    0xC0CB3936: ("scan_model_scale", structs.decode_BIG_f),
    0x925B9D4A: ("unknown_0x925b9d4a", _decode_unknown_0x925b9d4a),
    0x075A0734: ("unknown_0x075a0734", _decode_unknown_0x075a0734),
    0x8EF43309: ("unknown_0x8ef43309", structs.decode_BIG_f),
    0x4194622E: ("fog_near", structs.decode_BIG_f),
    0x3935A756: ("fog_far", structs.decode_BIG_f),
    0xE578C0DD: ("fog_color", _decode_fog_color),
    0xEEF15783: ("unknown_0xeef15783", structs.decode_BIG_f),
    0x78055AB2: ("unknown_0x78055ab2", structs.decode_BIG_f),
    0x09E3197F: ("unknown_0x09e3197f", structs.decode_BIG_f),
    0xFAFFCE1F: ("unknown_0xfaffce1f", structs.decode_BIG_f),
    0xE5280E7C: ("unknown_0xe5280e7c", structs.decode_BIG_f),
    0x647D9F91: ("background_sweep_color", _decode_background_sweep_color),
    0x7120F18F: ("background_sweep_radius", structs.decode_BIG_f),
    0x4DEF660D: ("background_sweep_time", structs.decode_BIG_f),
    0xC7C1967B: ("scan_text_window_background_color", _decode_scan_text_window_background_color),
    0xF74BBAD2: ("scan_text_window_border_color", _decode_scan_text_window_border_color),
    0xE31421E2: ("scan_text_window_font_color", _decode_scan_text_window_font_color),
    0x0B8F0DDB: ("legend_window_background_color", _decode_legend_window_background_color),
    0x0A7A4155: ("legend_window_border_color", _decode_legend_window_border_color),
    0x527A0B10: ("legend_window_font_color", _decode_legend_window_font_color),
    0x7927CA67: ("legend_hide_time", structs.decode_BIG_f),
    0x7F35C573: ("unknown_0x7f35c573", _decode_unknown_0x7f35c573),
    0xE0D77CF1: ("unknown_0xe0d77cf1", _decode_unknown_0xe0d77cf1),
    0x903D9B7E: ("unknown_0x903d9b7e", _decode_unknown_0x903d9b7e),
    0x0FDF22FC: ("unknown_0x0fdf22fc", _decode_unknown_0x0fdf22fc),
    0xBEAF9D6B: ("unknown_0xbeaf9d6b", _decode_unknown_0xbeaf9d6b),
    0x7E8247D6: ("unknown_0x7e8247d6", _decode_unknown_0x7e8247d6),
    0x8B3F7902: ("unknown_0x8b3f7902", _decode_unknown_0x8b3f7902),
    0xDC1ABB82: ("unknown_0xdc1abb82", _decode_unknown_0xdc1abb82),
    0x306B2B24: ("unknown_0x306b2b24", _decode_unknown_0x306b2b24),
    0xA485372C: ("frame_color", _decode_frame_color),
    0x1A4B8068: ("unknown_0x1a4b8068", _decode_unknown_0x1a4b8068),
    0xCC2F25F1: ("slider_background_color", _decode_slider_background_color),
    0xCB8D5CAF: ("slider_selection_color", _decode_slider_selection_color),
    0x3F44254F: ("slider_scale", structs.decode_BIG_f),
    0x7087C377: ("slider_speed", structs.decode_BIG_f),
    0x58795865: ("unknown_0x58795865", structs.decode_BIG_f),
    0x35E0BD31: ("unknown_0x35e0bd31", structs.decode_BIG_f),
    0xE7C283BE: ("menu_option_color", _decode_menu_option_color),
    0xDABCB730: ("menu_option_enabled_arrow_color", _decode_menu_option_enabled_arrow_color),
    0x9C2195D7: ("menu_option_disabled_arrow_color", _decode_menu_option_disabled_arrow_color),
    0xFC54F555: ("menu_option_scale", structs.decode_BIG_f),
    0xEF549530: ("menu_option_arrow_scale", structs.decode_BIG_f),
    0xFA7A92B8: ("model_rotation_speed", structs.decode_BIG_f),
    0x60914B79: ("unknown_0x60914b79", structs.decode_BIG_f),
    0x1FD44D9B: ("unknown_0x1fd44d9b", structs.decode_BIG_f),
    0x06C93AFA: ("model_light1_position", _decode_model_light1_position),
    0x33924AFB: ("model_light1_color", _decode_model_light1_color),
    0x17B45083: ("model_light2_position", _decode_model_light2_position),
    0xAA702CFA: ("model_light2_color", _decode_model_light2_color),
    0x62FF6D72: ("model_ambient_light_color", _decode_model_ambient_light_color),
}
