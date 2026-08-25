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

    class TweakAutoMapper_BaseJson(typing_extensions.TypedDict):
        unknown_0xcbe595d8: bool
        unknown_0x8ecb53a6: bool
        scale_move_speed_with_camera_distance: bool
        unknown_0x6bea9324: float
        unknown_0x065dd754: float
        unknown_0x57a46c09: float
        unknown_0xc87f5379: float
        unknown_0xbcc758c2: float
        unknown_0x8a4e16e4: bool
        unknown_0x2aae6322: int
        unknown_0x0c939a90: json_util.JsonObject
        unknown_0xb54255b5: float
        unknown_0x0c64cec4: float
        unknown_0xd33eb347: json_util.JsonObject
        unknown_0x335ebc7e: float
        map_screen_compass_size: float
        map_screen_compass_position: json_util.JsonValue
        map_screen_area_opacity: float
        unknown_0x533c5684: json_util.JsonValue
        unknown_0xeb383668: float
        unknown_0x27151ede: float
        unknown_0x434172c3: float
        unknown_0x68097036: float
        unknown_0x03adcf46: json_util.JsonValue
        unknown_0xd3fae283: json_util.JsonValue
        unknown_0x65d2cf45: json_util.JsonValue
        unknown_0xb5752c08: json_util.JsonValue
        unknown_0x035d01ce: json_util.JsonValue
        unknown_0x805d5fa3: json_util.JsonValue
        unknown_0x36757265: json_util.JsonValue
        unknown_0x7bdb0edf: float
        unknown_0x12221909: float
        unknown_0x38dbbc09: float
        unknown_0x30610062: float
        unknown_0xb6acea88: float
        unknown_0x73de4110: float
        unknown_0x2920db55: float
        map_screen_zoom_speed: float
        map_screen_circle_speed: float
        map_screen_move_speed: float
        unknown_0xd69f6b5c: float
        unknown_0xab82e268: json_util.JsonValue
        unknown_0x1daacfae: json_util.JsonValue
        unknown_0x47967404: float
        unknown_0x0ece1950: float
        unknown_0x9ac1bdde: float
        unknown_0x97a19386: float
        unknown_0xcb9e3a54: float
        unknown_0x2511a49b: float
        unknown_0x16c9f38e: float
        unknown_0xbc7e2e4d: float
        unknown_0x15564d32: float
        unknown_0xf5479260: float
        unknown_0x271b644e: float
        unknown_0x52dc08c1: float
        unknown_0x9980db64: float
        unknown_0x23f59057: float
        unknown_0xad3d5a3f: float
        unknown_0x3315d22b: float
        unknown_0x9e4007b6: float
        unknown_0x7a8d3d46: float
        unknown_0x2b97d64c: bool
        unknown_0xbdc57ce0: float
        unknown_0x7d59c854: float
        unknown_0x3c4ef7d2: float
        unknown_0x2b483e9f: float
        unknown_0x706f52fe: float
        unknown_0x62f9ebf6: float
        unknown_0xa9a53853: float
        unknown_0x722b1bc0: float
        unknown_0xf8252bca: float
        unknown_0xd1997970: float
        player_model_color: json_util.JsonValue
        unknown_0x5a87c156: json_util.JsonValue
        player_surface_color: json_util.JsonValue
        player_outline_color: json_util.JsonValue
        text_color: json_util.JsonValue
        text_outline_color: json_util.JsonValue
        unknown_0x1a4b8068: json_util.JsonValue
        frame_color: json_util.JsonValue
        title_color: json_util.JsonValue
        legend_background_color: json_util.JsonValue
        legend_gradient_color: json_util.JsonValue


@dataclasses.dataclass()
class TweakAutoMapper_Base(BaseProperty):
    unknown_0xcbe595d8: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCBE595D8, original_name="Unknown"),
        },
    )
    unknown_0x8ecb53a6: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8ECB53A6, original_name="Unknown"),
        },
    )
    scale_move_speed_with_camera_distance: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x30B13740, original_name="ScaleMoveSpeedWithCameraDistance"),
        },
    )
    unknown_0x6bea9324: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6BEA9324, original_name="Unknown"),
        },
    )
    unknown_0x065dd754: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x065DD754, original_name="Unknown"),
        },
    )
    unknown_0x57a46c09: float = dataclasses.field(
        default=1000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x57A46C09, original_name="Unknown"),
        },
    )
    unknown_0xc87f5379: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC87F5379, original_name="Unknown"),
        },
    )
    unknown_0xbcc758c2: float = dataclasses.field(
        default=250.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBCC758C2, original_name="Unknown"),
        },
    )
    unknown_0x8a4e16e4: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8A4E16E4, original_name="Unknown"),
        },
    )
    unknown_0x2aae6322: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2AAE6322, original_name="Unknown"),
        },
    )
    unknown_0x0c939a90: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x0C939A90, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xb54255b5: float = dataclasses.field(
        default=-89.9000015258789,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB54255B5, original_name="Unknown"),
        },
    )
    unknown_0x0c64cec4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0C64CEC4, original_name="Unknown"),
        },
    )
    unknown_0xd33eb347: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xD33EB347, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x335ebc7e: float = dataclasses.field(
        default=75.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x335EBC7E, original_name="Unknown"),
        },
    )
    map_screen_compass_size: float = dataclasses.field(
        default=32.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6119D07F, original_name="MapScreenCompassSize"),
        },
    )
    map_screen_compass_position: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xDBC799A4,
                original_name="MapScreenCompassPosition",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    map_screen_area_opacity: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x45BE3F6B, original_name="MapScreenAreaOpacity"),
        },
    )
    unknown_0x533c5684: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x533C5684, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xeb383668: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEB383668, original_name="Unknown"),
        },
    )
    unknown_0x27151ede: float = dataclasses.field(
        default=-45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x27151EDE, original_name="Unknown"),
        },
    )
    unknown_0x434172c3: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x434172C3, original_name="Unknown"),
        },
    )
    unknown_0x68097036: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x68097036, original_name="Unknown"),
        },
    )
    unknown_0x03adcf46: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x03ADCF46, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xd3fae283: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD3FAE283, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x65d2cf45: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x65D2CF45, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xb5752c08: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xB5752C08, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x035d01ce: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x035D01CE, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x805d5fa3: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x805D5FA3, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x36757265: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x36757265, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x7bdb0edf: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7BDB0EDF, original_name="Unknown"),
        },
    )
    unknown_0x12221909: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x12221909, original_name="Unknown"),
        },
    )
    unknown_0x38dbbc09: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38DBBC09, original_name="Unknown"),
        },
    )
    unknown_0x30610062: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x30610062, original_name="Unknown"),
        },
    )
    unknown_0xb6acea88: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB6ACEA88, original_name="Unknown"),
        },
    )
    unknown_0x73de4110: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x73DE4110, original_name="Unknown"),
        },
    )
    unknown_0x2920db55: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2920DB55, original_name="Unknown"),
        },
    )
    map_screen_zoom_speed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x19069725, original_name="MapScreenZoomSpeed"),
        },
    )
    map_screen_circle_speed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BA0DE1E, original_name="MapScreenCircleSpeed"),
        },
    )
    map_screen_move_speed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x310B37A1, original_name="MapScreenMoveSpeed"),
        },
    )
    unknown_0xd69f6b5c: float = dataclasses.field(
        default=2.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD69F6B5C, original_name="Unknown"),
        },
    )
    unknown_0xab82e268: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xAB82E268, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x1daacfae: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1DAACFAE, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x47967404: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47967404, original_name="Unknown"),
        },
    )
    unknown_0x0ece1950: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0ECE1950, original_name="Unknown"),
        },
    )
    unknown_0x9ac1bdde: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9AC1BDDE, original_name="Unknown"),
        },
    )
    unknown_0x97a19386: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x97A19386, original_name="Unknown"),
        },
    )
    unknown_0xcb9e3a54: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCB9E3A54, original_name="Unknown"),
        },
    )
    unknown_0x2511a49b: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2511A49B, original_name="Unknown"),
        },
    )
    unknown_0x16c9f38e: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16C9F38E, original_name="Unknown"),
        },
    )
    unknown_0xbc7e2e4d: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC7E2E4D, original_name="Unknown"),
        },
    )
    unknown_0x15564d32: float = dataclasses.field(
        default=3.569999933242798,
        metadata={
            "reflection": FieldReflection[float](float, id=0x15564D32, original_name="Unknown"),
        },
    )
    unknown_0xf5479260: float = dataclasses.field(
        default=3.569999933242798,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF5479260, original_name="Unknown"),
        },
    )
    unknown_0x271b644e: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x271B644E, original_name="Unknown"),
        },
    )
    unknown_0x52dc08c1: float = dataclasses.field(
        default=24.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x52DC08C1, original_name="Unknown"),
        },
    )
    unknown_0x9980db64: float = dataclasses.field(
        default=348.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9980DB64, original_name="Unknown"),
        },
    )
    unknown_0x23f59057: float = dataclasses.field(
        default=152.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23F59057, original_name="Unknown"),
        },
    )
    unknown_0xad3d5a3f: float = dataclasses.field(
        default=114.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD3D5A3F, original_name="Unknown"),
        },
    )
    unknown_0x3315d22b: float = dataclasses.field(
        default=0.8500000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3315D22B, original_name="Unknown"),
        },
    )
    unknown_0x9e4007b6: float = dataclasses.field(
        default=1.850000023841858,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9E4007B6, original_name="Unknown"),
        },
    )
    unknown_0x7a8d3d46: float = dataclasses.field(
        default=1.3600000143051147,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A8D3D46, original_name="Unknown"),
        },
    )
    unknown_0x2b97d64c: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2B97D64C, original_name="Unknown"),
        },
    )
    unknown_0xbdc57ce0: float = dataclasses.field(
        default=800.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBDC57CE0, original_name="Unknown"),
        },
    )
    unknown_0x7d59c854: float = dataclasses.field(
        default=400.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D59C854, original_name="Unknown"),
        },
    )
    unknown_0x3c4ef7d2: float = dataclasses.field(
        default=2000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3C4EF7D2, original_name="Unknown"),
        },
    )
    unknown_0x2b483e9f: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B483E9F, original_name="Unknown"),
        },
    )
    unknown_0x706f52fe: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x706F52FE, original_name="Unknown"),
        },
    )
    unknown_0x62f9ebf6: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x62F9EBF6, original_name="Unknown"),
        },
    )
    unknown_0xa9a53853: float = dataclasses.field(
        default=0.6349999904632568,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA9A53853, original_name="Unknown"),
        },
    )
    unknown_0x722b1bc0: float = dataclasses.field(
        default=-0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0x722B1BC0, original_name="Unknown"),
        },
    )
    unknown_0xf8252bca: float = dataclasses.field(
        default=1.600000023841858,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8252BCA, original_name="Unknown"),
        },
    )
    unknown_0xd1997970: float = dataclasses.field(
        default=1.2000000476837158,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD1997970, original_name="Unknown"),
        },
    )
    player_model_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x4C3FC933, original_name="PlayerModelColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x5a87c156: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5A87C156, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    player_surface_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x9C0C5318,
                original_name="PlayerSurfaceColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    player_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x2A247EDE,
                original_name="PlayerOutlineColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    text_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x44303A9C, original_name="TextColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    text_outline_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF2E13506, original_name="TextOutlineColor", from_json=Color.from_json, to_json=Color.to_json
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
    frame_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA485372C, original_name="FrameColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    title_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x536647D5, original_name="TitleColor", from_json=Color.from_json, to_json=Color.to_json
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
    legend_gradient_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x01CEA7F9,
                original_name="LegendGradientColor",
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
        if property_count != 83:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCBE595D8
        unknown_0xcbe595d8 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ECB53A6
        unknown_0x8ecb53a6 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30B13740
        scale_move_speed_with_camera_distance = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BEA9324
        unknown_0x6bea9324 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x065DD754
        unknown_0x065dd754 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57A46C09
        unknown_0x57a46c09 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC87F5379
        unknown_0xc87f5379 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBCC758C2
        unknown_0xbcc758c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A4E16E4
        unknown_0x8a4e16e4 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AAE6322
        unknown_0x2aae6322 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C939A90
        unknown_0x0c939a90 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB54255B5
        unknown_0xb54255b5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C64CEC4
        unknown_0x0c64cec4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD33EB347
        unknown_0xd33eb347 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x335EBC7E
        unknown_0x335ebc7e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6119D07F
        map_screen_compass_size = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDBC799A4
        map_screen_compass_position = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45BE3F6B
        map_screen_area_opacity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x533C5684
        unknown_0x533c5684 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB383668
        unknown_0xeb383668 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27151EDE
        unknown_0x27151ede = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x434172C3
        unknown_0x434172c3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68097036
        unknown_0x68097036 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03ADCF46
        unknown_0x03adcf46 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3FAE283
        unknown_0xd3fae283 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65D2CF45
        unknown_0x65d2cf45 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5752C08
        unknown_0xb5752c08 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x035D01CE
        unknown_0x035d01ce = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x805D5FA3
        unknown_0x805d5fa3 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36757265
        unknown_0x36757265 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7BDB0EDF
        unknown_0x7bdb0edf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12221909
        unknown_0x12221909 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38DBBC09
        unknown_0x38dbbc09 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30610062
        unknown_0x30610062 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6ACEA88
        unknown_0xb6acea88 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73DE4110
        unknown_0x73de4110 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2920DB55
        unknown_0x2920db55 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19069725
        map_screen_zoom_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BA0DE1E
        map_screen_circle_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x310B37A1
        map_screen_move_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD69F6B5C
        unknown_0xd69f6b5c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB82E268
        unknown_0xab82e268 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1DAACFAE
        unknown_0x1daacfae = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47967404
        unknown_0x47967404 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ECE1950
        unknown_0x0ece1950 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AC1BDDE
        unknown_0x9ac1bdde = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97A19386
        unknown_0x97a19386 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB9E3A54
        unknown_0xcb9e3a54 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2511A49B
        unknown_0x2511a49b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16C9F38E
        unknown_0x16c9f38e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC7E2E4D
        unknown_0xbc7e2e4d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15564D32
        unknown_0x15564d32 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5479260
        unknown_0xf5479260 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x271B644E
        unknown_0x271b644e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52DC08C1
        unknown_0x52dc08c1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9980DB64
        unknown_0x9980db64 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23F59057
        unknown_0x23f59057 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD3D5A3F
        unknown_0xad3d5a3f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3315D22B
        unknown_0x3315d22b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9E4007B6
        unknown_0x9e4007b6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A8D3D46
        unknown_0x7a8d3d46 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B97D64C
        unknown_0x2b97d64c = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBDC57CE0
        unknown_0xbdc57ce0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D59C854
        unknown_0x7d59c854 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C4EF7D2
        unknown_0x3c4ef7d2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B483E9F
        unknown_0x2b483e9f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x706F52FE
        unknown_0x706f52fe = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62F9EBF6
        unknown_0x62f9ebf6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9A53853
        unknown_0xa9a53853 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x722B1BC0
        unknown_0x722b1bc0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8252BCA
        unknown_0xf8252bca = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1997970
        unknown_0xd1997970 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C3FC933
        player_model_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5A87C156
        unknown_0x5a87c156 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C0C5318
        player_surface_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A247EDE
        player_outline_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44303A9C
        text_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2E13506
        text_outline_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A4B8068
        unknown_0x1a4b8068 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA485372C
        frame_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x536647D5
        title_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6B633FA
        legend_background_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01CEA7F9
        legend_gradient_color = Color.from_stream(data, game, property_size)

        return cls(
            unknown_0xcbe595d8,
            unknown_0x8ecb53a6,
            scale_move_speed_with_camera_distance,
            unknown_0x6bea9324,
            unknown_0x065dd754,
            unknown_0x57a46c09,
            unknown_0xc87f5379,
            unknown_0xbcc758c2,
            unknown_0x8a4e16e4,
            unknown_0x2aae6322,
            unknown_0x0c939a90,
            unknown_0xb54255b5,
            unknown_0x0c64cec4,
            unknown_0xd33eb347,
            unknown_0x335ebc7e,
            map_screen_compass_size,
            map_screen_compass_position,
            map_screen_area_opacity,
            unknown_0x533c5684,
            unknown_0xeb383668,
            unknown_0x27151ede,
            unknown_0x434172c3,
            unknown_0x68097036,
            unknown_0x03adcf46,
            unknown_0xd3fae283,
            unknown_0x65d2cf45,
            unknown_0xb5752c08,
            unknown_0x035d01ce,
            unknown_0x805d5fa3,
            unknown_0x36757265,
            unknown_0x7bdb0edf,
            unknown_0x12221909,
            unknown_0x38dbbc09,
            unknown_0x30610062,
            unknown_0xb6acea88,
            unknown_0x73de4110,
            unknown_0x2920db55,
            map_screen_zoom_speed,
            map_screen_circle_speed,
            map_screen_move_speed,
            unknown_0xd69f6b5c,
            unknown_0xab82e268,
            unknown_0x1daacfae,
            unknown_0x47967404,
            unknown_0x0ece1950,
            unknown_0x9ac1bdde,
            unknown_0x97a19386,
            unknown_0xcb9e3a54,
            unknown_0x2511a49b,
            unknown_0x16c9f38e,
            unknown_0xbc7e2e4d,
            unknown_0x15564d32,
            unknown_0xf5479260,
            unknown_0x271b644e,
            unknown_0x52dc08c1,
            unknown_0x9980db64,
            unknown_0x23f59057,
            unknown_0xad3d5a3f,
            unknown_0x3315d22b,
            unknown_0x9e4007b6,
            unknown_0x7a8d3d46,
            unknown_0x2b97d64c,
            unknown_0xbdc57ce0,
            unknown_0x7d59c854,
            unknown_0x3c4ef7d2,
            unknown_0x2b483e9f,
            unknown_0x706f52fe,
            unknown_0x62f9ebf6,
            unknown_0xa9a53853,
            unknown_0x722b1bc0,
            unknown_0xf8252bca,
            unknown_0xd1997970,
            player_model_color,
            unknown_0x5a87c156,
            player_surface_color,
            player_outline_color,
            text_color,
            text_outline_color,
            unknown_0x1a4b8068,
            frame_color,
            title_color,
            legend_background_color,
            legend_gradient_color,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00S")  # 83 properties

        data.write(b"\xcb\xe5\x95\xd8")  # 0xcbe595d8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xcbe595d8))

        data.write(b"\x8e\xcbS\xa6")  # 0x8ecb53a6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x8ecb53a6))

        data.write(b"0\xb17@")  # 0x30b13740
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scale_move_speed_with_camera_distance))

        data.write(b"k\xea\x93$")  # 0x6bea9324
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6bea9324))

        data.write(b"\x06]\xd7T")  # 0x65dd754
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x065dd754))

        data.write(b"W\xa4l\t")  # 0x57a46c09
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x57a46c09))

        data.write(b"\xc8\x7fSy")  # 0xc87f5379
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc87f5379))

        data.write(b"\xbc\xc7X\xc2")  # 0xbcc758c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbcc758c2))

        data.write(b"\x8aN\x16\xe4")  # 0x8a4e16e4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x8a4e16e4))

        data.write(b'*\xaec"')  # 0x2aae6322
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2aae6322))

        data.write(b"\x0c\x93\x9a\x90")  # 0xc939a90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x0c939a90.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb5BU\xb5")  # 0xb54255b5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb54255b5))

        data.write(b"\x0cd\xce\xc4")  # 0xc64cec4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0c64cec4))

        data.write(b"\xd3>\xb3G")  # 0xd33eb347
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xd33eb347.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3^\xbc~")  # 0x335ebc7e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x335ebc7e))

        data.write(b"a\x19\xd0\x7f")  # 0x6119d07f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.map_screen_compass_size))

        data.write(b"\xdb\xc7\x99\xa4")  # 0xdbc799a4
        data.write(b"\x00\x0c")  # size
        self.map_screen_compass_position.to_stream(data, game)

        data.write(b"E\xbe?k")  # 0x45be3f6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.map_screen_area_opacity))

        data.write(b"S<V\x84")  # 0x533c5684
        data.write(b"\x00\x10")  # size
        self.unknown_0x533c5684.to_stream(data, game)

        data.write(b"\xeb86h")  # 0xeb383668
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeb383668))

        data.write(b"'\x15\x1e\xde")  # 0x27151ede
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x27151ede))

        data.write(b"CAr\xc3")  # 0x434172c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x434172c3))

        data.write(b"h\tp6")  # 0x68097036
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x68097036))

        data.write(b"\x03\xad\xcfF")  # 0x3adcf46
        data.write(b"\x00\x10")  # size
        self.unknown_0x03adcf46.to_stream(data, game)

        data.write(b"\xd3\xfa\xe2\x83")  # 0xd3fae283
        data.write(b"\x00\x10")  # size
        self.unknown_0xd3fae283.to_stream(data, game)

        data.write(b"e\xd2\xcfE")  # 0x65d2cf45
        data.write(b"\x00\x10")  # size
        self.unknown_0x65d2cf45.to_stream(data, game)

        data.write(b"\xb5u,\x08")  # 0xb5752c08
        data.write(b"\x00\x10")  # size
        self.unknown_0xb5752c08.to_stream(data, game)

        data.write(b"\x03]\x01\xce")  # 0x35d01ce
        data.write(b"\x00\x10")  # size
        self.unknown_0x035d01ce.to_stream(data, game)

        data.write(b"\x80]_\xa3")  # 0x805d5fa3
        data.write(b"\x00\x10")  # size
        self.unknown_0x805d5fa3.to_stream(data, game)

        data.write(b"6ure")  # 0x36757265
        data.write(b"\x00\x10")  # size
        self.unknown_0x36757265.to_stream(data, game)

        data.write(b"{\xdb\x0e\xdf")  # 0x7bdb0edf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7bdb0edf))

        data.write(b'\x12"\x19\t')  # 0x12221909
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x12221909))

        data.write(b"8\xdb\xbc\t")  # 0x38dbbc09
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x38dbbc09))

        data.write(b"0a\x00b")  # 0x30610062
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x30610062))

        data.write(b"\xb6\xac\xea\x88")  # 0xb6acea88
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb6acea88))

        data.write(b"s\xdeA\x10")  # 0x73de4110
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x73de4110))

        data.write(b") \xdbU")  # 0x2920db55
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2920db55))

        data.write(b"\x19\x06\x97%")  # 0x19069725
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.map_screen_zoom_speed))

        data.write(b"[\xa0\xde\x1e")  # 0x5ba0de1e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.map_screen_circle_speed))

        data.write(b"1\x0b7\xa1")  # 0x310b37a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.map_screen_move_speed))

        data.write(b"\xd6\x9fk\\")  # 0xd69f6b5c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd69f6b5c))

        data.write(b"\xab\x82\xe2h")  # 0xab82e268
        data.write(b"\x00\x10")  # size
        self.unknown_0xab82e268.to_stream(data, game)

        data.write(b"\x1d\xaa\xcf\xae")  # 0x1daacfae
        data.write(b"\x00\x10")  # size
        self.unknown_0x1daacfae.to_stream(data, game)

        data.write(b"G\x96t\x04")  # 0x47967404
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x47967404))

        data.write(b"\x0e\xce\x19P")  # 0xece1950
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0ece1950))

        data.write(b"\x9a\xc1\xbd\xde")  # 0x9ac1bdde
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9ac1bdde))

        data.write(b"\x97\xa1\x93\x86")  # 0x97a19386
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x97a19386))

        data.write(b"\xcb\x9e:T")  # 0xcb9e3a54
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcb9e3a54))

        data.write(b"%\x11\xa4\x9b")  # 0x2511a49b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2511a49b))

        data.write(b"\x16\xc9\xf3\x8e")  # 0x16c9f38e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x16c9f38e))

        data.write(b"\xbc~.M")  # 0xbc7e2e4d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc7e2e4d))

        data.write(b"\x15VM2")  # 0x15564d32
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x15564d32))

        data.write(b"\xf5G\x92`")  # 0xf5479260
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf5479260))

        data.write(b"'\x1bdN")  # 0x271b644e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x271b644e))

        data.write(b"R\xdc\x08\xc1")  # 0x52dc08c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x52dc08c1))

        data.write(b"\x99\x80\xdbd")  # 0x9980db64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9980db64))

        data.write(b"#\xf5\x90W")  # 0x23f59057
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x23f59057))

        data.write(b"\xad=Z?")  # 0xad3d5a3f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xad3d5a3f))

        data.write(b"3\x15\xd2+")  # 0x3315d22b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3315d22b))

        data.write(b"\x9e@\x07\xb6")  # 0x9e4007b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9e4007b6))

        data.write(b"z\x8d=F")  # 0x7a8d3d46
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7a8d3d46))

        data.write(b"+\x97\xd6L")  # 0x2b97d64c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2b97d64c))

        data.write(b"\xbd\xc5|\xe0")  # 0xbdc57ce0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbdc57ce0))

        data.write(b"}Y\xc8T")  # 0x7d59c854
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7d59c854))

        data.write(b"<N\xf7\xd2")  # 0x3c4ef7d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3c4ef7d2))

        data.write(b"+H>\x9f")  # 0x2b483e9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2b483e9f))

        data.write(b"poR\xfe")  # 0x706f52fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x706f52fe))

        data.write(b"b\xf9\xeb\xf6")  # 0x62f9ebf6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x62f9ebf6))

        data.write(b"\xa9\xa58S")  # 0xa9a53853
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa9a53853))

        data.write(b"r+\x1b\xc0")  # 0x722b1bc0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x722b1bc0))

        data.write(b"\xf8%+\xca")  # 0xf8252bca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf8252bca))

        data.write(b"\xd1\x99yp")  # 0xd1997970
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd1997970))

        data.write(b"L?\xc93")  # 0x4c3fc933
        data.write(b"\x00\x10")  # size
        self.player_model_color.to_stream(data, game)

        data.write(b"Z\x87\xc1V")  # 0x5a87c156
        data.write(b"\x00\x10")  # size
        self.unknown_0x5a87c156.to_stream(data, game)

        data.write(b"\x9c\x0cS\x18")  # 0x9c0c5318
        data.write(b"\x00\x10")  # size
        self.player_surface_color.to_stream(data, game)

        data.write(b"*$~\xde")  # 0x2a247ede
        data.write(b"\x00\x10")  # size
        self.player_outline_color.to_stream(data, game)

        data.write(b"D0:\x9c")  # 0x44303a9c
        data.write(b"\x00\x10")  # size
        self.text_color.to_stream(data, game)

        data.write(b"\xf2\xe15\x06")  # 0xf2e13506
        data.write(b"\x00\x10")  # size
        self.text_outline_color.to_stream(data, game)

        data.write(b"\x1aK\x80h")  # 0x1a4b8068
        data.write(b"\x00\x10")  # size
        self.unknown_0x1a4b8068.to_stream(data, game)

        data.write(b"\xa4\x857,")  # 0xa485372c
        data.write(b"\x00\x10")  # size
        self.frame_color.to_stream(data, game)

        data.write(b"SfG\xd5")  # 0x536647d5
        data.write(b"\x00\x10")  # size
        self.title_color.to_stream(data, game)

        data.write(b"\xa6\xb63\xfa")  # 0xa6b633fa
        data.write(b"\x00\x10")  # size
        self.legend_background_color.to_stream(data, game)

        data.write(b"\x01\xce\xa7\xf9")  # 0x1cea7f9
        data.write(b"\x00\x10")  # size
        self.legend_gradient_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakAutoMapper_BaseJson", data)
        return cls(
            unknown_0xcbe595d8=json_data["unknown_0xcbe595d8"],
            unknown_0x8ecb53a6=json_data["unknown_0x8ecb53a6"],
            scale_move_speed_with_camera_distance=json_data["scale_move_speed_with_camera_distance"],
            unknown_0x6bea9324=json_data["unknown_0x6bea9324"],
            unknown_0x065dd754=json_data["unknown_0x065dd754"],
            unknown_0x57a46c09=json_data["unknown_0x57a46c09"],
            unknown_0xc87f5379=json_data["unknown_0xc87f5379"],
            unknown_0xbcc758c2=json_data["unknown_0xbcc758c2"],
            unknown_0x8a4e16e4=json_data["unknown_0x8a4e16e4"],
            unknown_0x2aae6322=json_data["unknown_0x2aae6322"],
            unknown_0x0c939a90=Spline.from_json(json_data["unknown_0x0c939a90"]),
            unknown_0xb54255b5=json_data["unknown_0xb54255b5"],
            unknown_0x0c64cec4=json_data["unknown_0x0c64cec4"],
            unknown_0xd33eb347=Spline.from_json(json_data["unknown_0xd33eb347"]),
            unknown_0x335ebc7e=json_data["unknown_0x335ebc7e"],
            map_screen_compass_size=json_data["map_screen_compass_size"],
            map_screen_compass_position=Vector.from_json(json_data["map_screen_compass_position"]),
            map_screen_area_opacity=json_data["map_screen_area_opacity"],
            unknown_0x533c5684=Color.from_json(json_data["unknown_0x533c5684"]),
            unknown_0xeb383668=json_data["unknown_0xeb383668"],
            unknown_0x27151ede=json_data["unknown_0x27151ede"],
            unknown_0x434172c3=json_data["unknown_0x434172c3"],
            unknown_0x68097036=json_data["unknown_0x68097036"],
            unknown_0x03adcf46=Color.from_json(json_data["unknown_0x03adcf46"]),
            unknown_0xd3fae283=Color.from_json(json_data["unknown_0xd3fae283"]),
            unknown_0x65d2cf45=Color.from_json(json_data["unknown_0x65d2cf45"]),
            unknown_0xb5752c08=Color.from_json(json_data["unknown_0xb5752c08"]),
            unknown_0x035d01ce=Color.from_json(json_data["unknown_0x035d01ce"]),
            unknown_0x805d5fa3=Color.from_json(json_data["unknown_0x805d5fa3"]),
            unknown_0x36757265=Color.from_json(json_data["unknown_0x36757265"]),
            unknown_0x7bdb0edf=json_data["unknown_0x7bdb0edf"],
            unknown_0x12221909=json_data["unknown_0x12221909"],
            unknown_0x38dbbc09=json_data["unknown_0x38dbbc09"],
            unknown_0x30610062=json_data["unknown_0x30610062"],
            unknown_0xb6acea88=json_data["unknown_0xb6acea88"],
            unknown_0x73de4110=json_data["unknown_0x73de4110"],
            unknown_0x2920db55=json_data["unknown_0x2920db55"],
            map_screen_zoom_speed=json_data["map_screen_zoom_speed"],
            map_screen_circle_speed=json_data["map_screen_circle_speed"],
            map_screen_move_speed=json_data["map_screen_move_speed"],
            unknown_0xd69f6b5c=json_data["unknown_0xd69f6b5c"],
            unknown_0xab82e268=Color.from_json(json_data["unknown_0xab82e268"]),
            unknown_0x1daacfae=Color.from_json(json_data["unknown_0x1daacfae"]),
            unknown_0x47967404=json_data["unknown_0x47967404"],
            unknown_0x0ece1950=json_data["unknown_0x0ece1950"],
            unknown_0x9ac1bdde=json_data["unknown_0x9ac1bdde"],
            unknown_0x97a19386=json_data["unknown_0x97a19386"],
            unknown_0xcb9e3a54=json_data["unknown_0xcb9e3a54"],
            unknown_0x2511a49b=json_data["unknown_0x2511a49b"],
            unknown_0x16c9f38e=json_data["unknown_0x16c9f38e"],
            unknown_0xbc7e2e4d=json_data["unknown_0xbc7e2e4d"],
            unknown_0x15564d32=json_data["unknown_0x15564d32"],
            unknown_0xf5479260=json_data["unknown_0xf5479260"],
            unknown_0x271b644e=json_data["unknown_0x271b644e"],
            unknown_0x52dc08c1=json_data["unknown_0x52dc08c1"],
            unknown_0x9980db64=json_data["unknown_0x9980db64"],
            unknown_0x23f59057=json_data["unknown_0x23f59057"],
            unknown_0xad3d5a3f=json_data["unknown_0xad3d5a3f"],
            unknown_0x3315d22b=json_data["unknown_0x3315d22b"],
            unknown_0x9e4007b6=json_data["unknown_0x9e4007b6"],
            unknown_0x7a8d3d46=json_data["unknown_0x7a8d3d46"],
            unknown_0x2b97d64c=json_data["unknown_0x2b97d64c"],
            unknown_0xbdc57ce0=json_data["unknown_0xbdc57ce0"],
            unknown_0x7d59c854=json_data["unknown_0x7d59c854"],
            unknown_0x3c4ef7d2=json_data["unknown_0x3c4ef7d2"],
            unknown_0x2b483e9f=json_data["unknown_0x2b483e9f"],
            unknown_0x706f52fe=json_data["unknown_0x706f52fe"],
            unknown_0x62f9ebf6=json_data["unknown_0x62f9ebf6"],
            unknown_0xa9a53853=json_data["unknown_0xa9a53853"],
            unknown_0x722b1bc0=json_data["unknown_0x722b1bc0"],
            unknown_0xf8252bca=json_data["unknown_0xf8252bca"],
            unknown_0xd1997970=json_data["unknown_0xd1997970"],
            player_model_color=Color.from_json(json_data["player_model_color"]),
            unknown_0x5a87c156=Color.from_json(json_data["unknown_0x5a87c156"]),
            player_surface_color=Color.from_json(json_data["player_surface_color"]),
            player_outline_color=Color.from_json(json_data["player_outline_color"]),
            text_color=Color.from_json(json_data["text_color"]),
            text_outline_color=Color.from_json(json_data["text_outline_color"]),
            unknown_0x1a4b8068=Color.from_json(json_data["unknown_0x1a4b8068"]),
            frame_color=Color.from_json(json_data["frame_color"]),
            title_color=Color.from_json(json_data["title_color"]),
            legend_background_color=Color.from_json(json_data["legend_background_color"]),
            legend_gradient_color=Color.from_json(json_data["legend_gradient_color"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xcbe595d8": self.unknown_0xcbe595d8,
            "unknown_0x8ecb53a6": self.unknown_0x8ecb53a6,
            "scale_move_speed_with_camera_distance": self.scale_move_speed_with_camera_distance,
            "unknown_0x6bea9324": self.unknown_0x6bea9324,
            "unknown_0x065dd754": self.unknown_0x065dd754,
            "unknown_0x57a46c09": self.unknown_0x57a46c09,
            "unknown_0xc87f5379": self.unknown_0xc87f5379,
            "unknown_0xbcc758c2": self.unknown_0xbcc758c2,
            "unknown_0x8a4e16e4": self.unknown_0x8a4e16e4,
            "unknown_0x2aae6322": self.unknown_0x2aae6322,
            "unknown_0x0c939a90": self.unknown_0x0c939a90.to_json(),
            "unknown_0xb54255b5": self.unknown_0xb54255b5,
            "unknown_0x0c64cec4": self.unknown_0x0c64cec4,
            "unknown_0xd33eb347": self.unknown_0xd33eb347.to_json(),
            "unknown_0x335ebc7e": self.unknown_0x335ebc7e,
            "map_screen_compass_size": self.map_screen_compass_size,
            "map_screen_compass_position": self.map_screen_compass_position.to_json(),
            "map_screen_area_opacity": self.map_screen_area_opacity,
            "unknown_0x533c5684": self.unknown_0x533c5684.to_json(),
            "unknown_0xeb383668": self.unknown_0xeb383668,
            "unknown_0x27151ede": self.unknown_0x27151ede,
            "unknown_0x434172c3": self.unknown_0x434172c3,
            "unknown_0x68097036": self.unknown_0x68097036,
            "unknown_0x03adcf46": self.unknown_0x03adcf46.to_json(),
            "unknown_0xd3fae283": self.unknown_0xd3fae283.to_json(),
            "unknown_0x65d2cf45": self.unknown_0x65d2cf45.to_json(),
            "unknown_0xb5752c08": self.unknown_0xb5752c08.to_json(),
            "unknown_0x035d01ce": self.unknown_0x035d01ce.to_json(),
            "unknown_0x805d5fa3": self.unknown_0x805d5fa3.to_json(),
            "unknown_0x36757265": self.unknown_0x36757265.to_json(),
            "unknown_0x7bdb0edf": self.unknown_0x7bdb0edf,
            "unknown_0x12221909": self.unknown_0x12221909,
            "unknown_0x38dbbc09": self.unknown_0x38dbbc09,
            "unknown_0x30610062": self.unknown_0x30610062,
            "unknown_0xb6acea88": self.unknown_0xb6acea88,
            "unknown_0x73de4110": self.unknown_0x73de4110,
            "unknown_0x2920db55": self.unknown_0x2920db55,
            "map_screen_zoom_speed": self.map_screen_zoom_speed,
            "map_screen_circle_speed": self.map_screen_circle_speed,
            "map_screen_move_speed": self.map_screen_move_speed,
            "unknown_0xd69f6b5c": self.unknown_0xd69f6b5c,
            "unknown_0xab82e268": self.unknown_0xab82e268.to_json(),
            "unknown_0x1daacfae": self.unknown_0x1daacfae.to_json(),
            "unknown_0x47967404": self.unknown_0x47967404,
            "unknown_0x0ece1950": self.unknown_0x0ece1950,
            "unknown_0x9ac1bdde": self.unknown_0x9ac1bdde,
            "unknown_0x97a19386": self.unknown_0x97a19386,
            "unknown_0xcb9e3a54": self.unknown_0xcb9e3a54,
            "unknown_0x2511a49b": self.unknown_0x2511a49b,
            "unknown_0x16c9f38e": self.unknown_0x16c9f38e,
            "unknown_0xbc7e2e4d": self.unknown_0xbc7e2e4d,
            "unknown_0x15564d32": self.unknown_0x15564d32,
            "unknown_0xf5479260": self.unknown_0xf5479260,
            "unknown_0x271b644e": self.unknown_0x271b644e,
            "unknown_0x52dc08c1": self.unknown_0x52dc08c1,
            "unknown_0x9980db64": self.unknown_0x9980db64,
            "unknown_0x23f59057": self.unknown_0x23f59057,
            "unknown_0xad3d5a3f": self.unknown_0xad3d5a3f,
            "unknown_0x3315d22b": self.unknown_0x3315d22b,
            "unknown_0x9e4007b6": self.unknown_0x9e4007b6,
            "unknown_0x7a8d3d46": self.unknown_0x7a8d3d46,
            "unknown_0x2b97d64c": self.unknown_0x2b97d64c,
            "unknown_0xbdc57ce0": self.unknown_0xbdc57ce0,
            "unknown_0x7d59c854": self.unknown_0x7d59c854,
            "unknown_0x3c4ef7d2": self.unknown_0x3c4ef7d2,
            "unknown_0x2b483e9f": self.unknown_0x2b483e9f,
            "unknown_0x706f52fe": self.unknown_0x706f52fe,
            "unknown_0x62f9ebf6": self.unknown_0x62f9ebf6,
            "unknown_0xa9a53853": self.unknown_0xa9a53853,
            "unknown_0x722b1bc0": self.unknown_0x722b1bc0,
            "unknown_0xf8252bca": self.unknown_0xf8252bca,
            "unknown_0xd1997970": self.unknown_0xd1997970,
            "player_model_color": self.player_model_color.to_json(),
            "unknown_0x5a87c156": self.unknown_0x5a87c156.to_json(),
            "player_surface_color": self.player_surface_color.to_json(),
            "player_outline_color": self.player_outline_color.to_json(),
            "text_color": self.text_color.to_json(),
            "text_outline_color": self.text_outline_color.to_json(),
            "unknown_0x1a4b8068": self.unknown_0x1a4b8068.to_json(),
            "frame_color": self.frame_color.to_json(),
            "title_color": self.title_color.to_json(),
            "legend_background_color": self.legend_background_color.to_json(),
            "legend_gradient_color": self.legend_gradient_color.to_json(),
        }


def _decode_unknown_0x0c939a90(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0xd33eb347(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_map_screen_compass_position(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0x533c5684(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x03adcf46(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xd3fae283(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x65d2cf45(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xb5752c08(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x035d01ce(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x805d5fa3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x36757265(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xab82e268(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x1daacfae(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_model_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x5a87c156(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_text_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x1a4b8068(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_title_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_gradient_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCBE595D8: ("unknown_0xcbe595d8", structs.decode_BIG_bool_),
    0x8ECB53A6: ("unknown_0x8ecb53a6", structs.decode_BIG_bool_),
    0x30B13740: ("scale_move_speed_with_camera_distance", structs.decode_BIG_bool_),
    0x6BEA9324: ("unknown_0x6bea9324", structs.decode_BIG_f),
    0x065DD754: ("unknown_0x065dd754", structs.decode_BIG_f),
    0x57A46C09: ("unknown_0x57a46c09", structs.decode_BIG_f),
    0xC87F5379: ("unknown_0xc87f5379", structs.decode_BIG_f),
    0xBCC758C2: ("unknown_0xbcc758c2", structs.decode_BIG_f),
    0x8A4E16E4: ("unknown_0x8a4e16e4", structs.decode_BIG_bool_),
    0x2AAE6322: ("unknown_0x2aae6322", structs.decode_BIG_l),
    0x0C939A90: ("unknown_0x0c939a90", _decode_unknown_0x0c939a90),
    0xB54255B5: ("unknown_0xb54255b5", structs.decode_BIG_f),
    0x0C64CEC4: ("unknown_0x0c64cec4", structs.decode_BIG_f),
    0xD33EB347: ("unknown_0xd33eb347", _decode_unknown_0xd33eb347),
    0x335EBC7E: ("unknown_0x335ebc7e", structs.decode_BIG_f),
    0x6119D07F: ("map_screen_compass_size", structs.decode_BIG_f),
    0xDBC799A4: ("map_screen_compass_position", _decode_map_screen_compass_position),
    0x45BE3F6B: ("map_screen_area_opacity", structs.decode_BIG_f),
    0x533C5684: ("unknown_0x533c5684", _decode_unknown_0x533c5684),
    0xEB383668: ("unknown_0xeb383668", structs.decode_BIG_f),
    0x27151EDE: ("unknown_0x27151ede", structs.decode_BIG_f),
    0x434172C3: ("unknown_0x434172c3", structs.decode_BIG_f),
    0x68097036: ("unknown_0x68097036", structs.decode_BIG_f),
    0x03ADCF46: ("unknown_0x03adcf46", _decode_unknown_0x03adcf46),
    0xD3FAE283: ("unknown_0xd3fae283", _decode_unknown_0xd3fae283),
    0x65D2CF45: ("unknown_0x65d2cf45", _decode_unknown_0x65d2cf45),
    0xB5752C08: ("unknown_0xb5752c08", _decode_unknown_0xb5752c08),
    0x035D01CE: ("unknown_0x035d01ce", _decode_unknown_0x035d01ce),
    0x805D5FA3: ("unknown_0x805d5fa3", _decode_unknown_0x805d5fa3),
    0x36757265: ("unknown_0x36757265", _decode_unknown_0x36757265),
    0x7BDB0EDF: ("unknown_0x7bdb0edf", structs.decode_BIG_f),
    0x12221909: ("unknown_0x12221909", structs.decode_BIG_f),
    0x38DBBC09: ("unknown_0x38dbbc09", structs.decode_BIG_f),
    0x30610062: ("unknown_0x30610062", structs.decode_BIG_f),
    0xB6ACEA88: ("unknown_0xb6acea88", structs.decode_BIG_f),
    0x73DE4110: ("unknown_0x73de4110", structs.decode_BIG_f),
    0x2920DB55: ("unknown_0x2920db55", structs.decode_BIG_f),
    0x19069725: ("map_screen_zoom_speed", structs.decode_BIG_f),
    0x5BA0DE1E: ("map_screen_circle_speed", structs.decode_BIG_f),
    0x310B37A1: ("map_screen_move_speed", structs.decode_BIG_f),
    0xD69F6B5C: ("unknown_0xd69f6b5c", structs.decode_BIG_f),
    0xAB82E268: ("unknown_0xab82e268", _decode_unknown_0xab82e268),
    0x1DAACFAE: ("unknown_0x1daacfae", _decode_unknown_0x1daacfae),
    0x47967404: ("unknown_0x47967404", structs.decode_BIG_f),
    0x0ECE1950: ("unknown_0x0ece1950", structs.decode_BIG_f),
    0x9AC1BDDE: ("unknown_0x9ac1bdde", structs.decode_BIG_f),
    0x97A19386: ("unknown_0x97a19386", structs.decode_BIG_f),
    0xCB9E3A54: ("unknown_0xcb9e3a54", structs.decode_BIG_f),
    0x2511A49B: ("unknown_0x2511a49b", structs.decode_BIG_f),
    0x16C9F38E: ("unknown_0x16c9f38e", structs.decode_BIG_f),
    0xBC7E2E4D: ("unknown_0xbc7e2e4d", structs.decode_BIG_f),
    0x15564D32: ("unknown_0x15564d32", structs.decode_BIG_f),
    0xF5479260: ("unknown_0xf5479260", structs.decode_BIG_f),
    0x271B644E: ("unknown_0x271b644e", structs.decode_BIG_f),
    0x52DC08C1: ("unknown_0x52dc08c1", structs.decode_BIG_f),
    0x9980DB64: ("unknown_0x9980db64", structs.decode_BIG_f),
    0x23F59057: ("unknown_0x23f59057", structs.decode_BIG_f),
    0xAD3D5A3F: ("unknown_0xad3d5a3f", structs.decode_BIG_f),
    0x3315D22B: ("unknown_0x3315d22b", structs.decode_BIG_f),
    0x9E4007B6: ("unknown_0x9e4007b6", structs.decode_BIG_f),
    0x7A8D3D46: ("unknown_0x7a8d3d46", structs.decode_BIG_f),
    0x2B97D64C: ("unknown_0x2b97d64c", structs.decode_BIG_bool_),
    0xBDC57CE0: ("unknown_0xbdc57ce0", structs.decode_BIG_f),
    0x7D59C854: ("unknown_0x7d59c854", structs.decode_BIG_f),
    0x3C4EF7D2: ("unknown_0x3c4ef7d2", structs.decode_BIG_f),
    0x2B483E9F: ("unknown_0x2b483e9f", structs.decode_BIG_f),
    0x706F52FE: ("unknown_0x706f52fe", structs.decode_BIG_f),
    0x62F9EBF6: ("unknown_0x62f9ebf6", structs.decode_BIG_f),
    0xA9A53853: ("unknown_0xa9a53853", structs.decode_BIG_f),
    0x722B1BC0: ("unknown_0x722b1bc0", structs.decode_BIG_f),
    0xF8252BCA: ("unknown_0xf8252bca", structs.decode_BIG_f),
    0xD1997970: ("unknown_0xd1997970", structs.decode_BIG_f),
    0x4C3FC933: ("player_model_color", _decode_player_model_color),
    0x5A87C156: ("unknown_0x5a87c156", _decode_unknown_0x5a87c156),
    0x9C0C5318: ("player_surface_color", _decode_player_surface_color),
    0x2A247EDE: ("player_outline_color", _decode_player_outline_color),
    0x44303A9C: ("text_color", _decode_text_color),
    0xF2E13506: ("text_outline_color", _decode_text_outline_color),
    0x1A4B8068: ("unknown_0x1a4b8068", _decode_unknown_0x1a4b8068),
    0xA485372C: ("frame_color", _decode_frame_color),
    0x536647D5: ("title_color", _decode_title_color),
    0xA6B633FA: ("legend_background_color", _decode_legend_background_color),
    0x01CEA7F9: ("legend_gradient_color", _decode_legend_gradient_color),
}
