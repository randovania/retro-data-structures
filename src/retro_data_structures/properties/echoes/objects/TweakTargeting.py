# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.TIcon_Configurations import TIcon_Configurations
from retro_data_structures.properties.common.archetypes.TweakTargeting_Charge_Gauge import TweakTargeting_Charge_Gauge
from retro_data_structures.properties.common.archetypes.TweakTargeting_LockDagger import TweakTargeting_LockDagger
from retro_data_structures.properties.common.archetypes.TweakTargeting_LockFire import TweakTargeting_LockFire
from retro_data_structures.properties.common.archetypes.TweakTargeting_OuterBeamIcon import TweakTargeting_OuterBeamIcon
from retro_data_structures.properties.common.archetypes.TweakTargeting_Scan import TweakTargeting_Scan
from retro_data_structures.properties.echoes.archetypes.TweakTargeting_VulnerabilityIndicator import (
    TweakTargeting_VulnerabilityIndicator,
)
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TweakTargetingJson(typing_extensions.TypedDict):
        instance_name: str
        unknown_0x5173932f: json_util.JsonObject
        unknown_0x23ff4be4: json_util.JsonObject
        unknown_0x92e98613: json_util.JsonObject
        unknown_0x64833842: json_util.JsonObject
        unknown_0x8dfd6e3c: json_util.JsonObject
        charge_gauge: json_util.JsonObject
        lock_fire: json_util.JsonObject
        lock_dagger: json_util.JsonObject
        scan: json_util.JsonObject
        unknown_0xc3410560: int
        unknown_0x3eb13041: float
        unknown_0x5e67cab0: float
        unknown_0xe0ca98ac: float
        lock_on_confirm_reticle_scale: float
        unknown_0x9f8d62c1: float
        unknown_0xff5eeeb9: float
        unknown_0x0d0b660d: float
        seeker_target_reticle_scale: float
        unknown_0x03efc783: float
        unknown_0xdcbd7bf8: float
        unknown_0x2acd6b4b: float
        unknown_0xb4c6c331: float
        unknown_0x27d02089: float
        unknown_0xae89310e: float
        unknown_0xb27644df: float
        unknown_0x21e2d1cc: float
        orbit_point_occluded_opacity: float
        unknown_0x5c489cb5: float
        orbit_point_z_offset: float
        unknown_0x61a6a38e: float
        unknown_0xfbdf31f9: float
        unknown_0xf76f7d0b: float
        unknown_0x810b3a08: float
        unknown_0x73fe1553: float
        unknown_0xc8aef6f2: float
        unknown_0x69b1e76c: float
        unknown_0x8a0dfd23: float
        unknown_0x8299e96e: float
        unknown_0xa18a3f25: float
        unknown_0x23be9bb2: float
        unknown_0x8d512b82: float
        unknown_0x39f1698d: float
        unknown_0xc768c1e9: float
        unknown_0x55c47b0e: float
        unknown_0xa009aea2: float
        unknown_0x38080bbf: float
        unknown_0x71017dbe: float
        unknown_0x4a996997: float
        unknown_0x9f9fa6f3: float
        unknown_0x932fea01: float
        unknown_0x165f0fa8: float
        unknown_0x6bd6b11f: float
        unknown_0x42420f6e: json_util.JsonValue
        flower_reticle_scale: float
        flower_reticle_color: json_util.JsonValue
        unknown_0xb090e147: float
        unknown_0x4c73a43d: float
        unknown_0x6543d31b: float
        unknown_0x8cd2d1ce: float
        missile_bracket_color: json_util.JsonValue
        unknown_0x45910e5d: float
        unknown_0x07b30fa0: float
        unknown_0x13ce8500: json_util.JsonValue
        unknown_0x9829f256: json_util.JsonValue
        unknown_0x77a613b9: json_util.JsonValue
        unknown_0xdfa81287: json_util.JsonValue
        lock_on_confirm_reticle_color: json_util.JsonValue
        seeker_reticle_color: json_util.JsonValue
        unknown_0x618d150a: float
        unknown_0x209a2a8c: float
        unknown_0xacb3f8f7: float
        unknown_0xeda4c771: float
        unknown_0xd3427574: float
        unknown_0x92554af2: float
        unknown_0x1e134e75: float
        unknown_0x5f0471f3: float
        unknown_0xe90548ac: float
        unknown_0xa812772a: float
        unknown_0x2d75c7be: float
        unknown_0x6c62f838: float
        unknown_0xf98e6242: float
        unknown_0xb8995dc4: float
        unknown_0x5009c614: float
        unknown_0x111ef992: float
        grapple_icon_scale: float
        grapple_icon_scale_inactive: float
        unknown_0x498d794a: float
        unknown_0x089a46cc: float
        grapple_icon_color: json_util.JsonValue
        grapple_icon_color_inactive: json_util.JsonValue
        unknown_0x083b1cc8: json_util.JsonValue
        unknown_0x966982b1: float
        unknown_0xf9799f5f: json_util.JsonValue
        unknown_0x9b980788: float
        orbit_point_model_color: json_util.JsonValue
        crosshairs_color: json_util.JsonValue
        unknown_0x2ff52290: float
        unknown_0x8a548cc9: bool
        unknown_0x65d449e1: json_util.JsonValue
        unknown_0x42c7fbe4: float
        unknown_0x13820c03: float
        unknown_0x52953385: float
        x_ray_seeker_reticle_color: json_util.JsonValue
        unknown_0xdd8cf478: float
        unknown_0xcbac6d52: float
        unknown_0x980a75b6: float
        unknown_0xcd1e0e91: float
        unknown_0xce9cf241: float
        unknown_0xb6531e99: float
        unknown_0x77e5c6b5: float
        unknown_0xfef5668b: float
        health_color: json_util.JsonValue
        power_vulnerability_indicator: json_util.JsonObject
        light_vulnerability_indicator: json_util.JsonObject
        dark_vulnerability_indicator: json_util.JsonObject
        annihilator_vulnerability_indicator: json_util.JsonObject


@dataclasses.dataclass()
class TweakTargeting(BaseObjectType):
    instance_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x7FDA1466, original_name="InstanceName"),
        },
    )
    unknown_0x5173932f: TweakTargeting_OuterBeamIcon = dataclasses.field(
        default_factory=TweakTargeting_OuterBeamIcon,
        metadata={
            "reflection": FieldReflection[TweakTargeting_OuterBeamIcon](
                TweakTargeting_OuterBeamIcon,
                id=0x5173932F,
                original_name="Unknown",
                from_json=TweakTargeting_OuterBeamIcon.from_json,
                to_json=TweakTargeting_OuterBeamIcon.to_json,
            ),
        },
    )
    unknown_0x23ff4be4: TIcon_Configurations = dataclasses.field(
        default_factory=TIcon_Configurations,
        metadata={
            "reflection": FieldReflection[TIcon_Configurations](
                TIcon_Configurations,
                id=0x23FF4BE4,
                original_name="Unknown",
                from_json=TIcon_Configurations.from_json,
                to_json=TIcon_Configurations.to_json,
            ),
        },
    )
    unknown_0x92e98613: TIcon_Configurations = dataclasses.field(
        default_factory=TIcon_Configurations,
        metadata={
            "reflection": FieldReflection[TIcon_Configurations](
                TIcon_Configurations,
                id=0x92E98613,
                original_name="Unknown",
                from_json=TIcon_Configurations.from_json,
                to_json=TIcon_Configurations.to_json,
            ),
        },
    )
    unknown_0x64833842: TIcon_Configurations = dataclasses.field(
        default_factory=TIcon_Configurations,
        metadata={
            "reflection": FieldReflection[TIcon_Configurations](
                TIcon_Configurations,
                id=0x64833842,
                original_name="Unknown",
                from_json=TIcon_Configurations.from_json,
                to_json=TIcon_Configurations.to_json,
            ),
        },
    )
    unknown_0x8dfd6e3c: TIcon_Configurations = dataclasses.field(
        default_factory=TIcon_Configurations,
        metadata={
            "reflection": FieldReflection[TIcon_Configurations](
                TIcon_Configurations,
                id=0x8DFD6E3C,
                original_name="Unknown",
                from_json=TIcon_Configurations.from_json,
                to_json=TIcon_Configurations.to_json,
            ),
        },
    )
    charge_gauge: TweakTargeting_Charge_Gauge = dataclasses.field(
        default_factory=TweakTargeting_Charge_Gauge,
        metadata={
            "reflection": FieldReflection[TweakTargeting_Charge_Gauge](
                TweakTargeting_Charge_Gauge,
                id=0xBC5A41B2,
                original_name="Charge_Gauge",
                from_json=TweakTargeting_Charge_Gauge.from_json,
                to_json=TweakTargeting_Charge_Gauge.to_json,
            ),
        },
    )
    lock_fire: TweakTargeting_LockFire = dataclasses.field(
        default_factory=TweakTargeting_LockFire,
        metadata={
            "reflection": FieldReflection[TweakTargeting_LockFire](
                TweakTargeting_LockFire,
                id=0x00183589,
                original_name="LockFire",
                from_json=TweakTargeting_LockFire.from_json,
                to_json=TweakTargeting_LockFire.to_json,
            ),
        },
    )
    lock_dagger: TweakTargeting_LockDagger = dataclasses.field(
        default_factory=TweakTargeting_LockDagger,
        metadata={
            "reflection": FieldReflection[TweakTargeting_LockDagger](
                TweakTargeting_LockDagger,
                id=0xD20ECC07,
                original_name="LockDagger",
                from_json=TweakTargeting_LockDagger.from_json,
                to_json=TweakTargeting_LockDagger.to_json,
            ),
        },
    )
    scan: TweakTargeting_Scan = dataclasses.field(
        default_factory=TweakTargeting_Scan,
        metadata={
            "reflection": FieldReflection[TweakTargeting_Scan](
                TweakTargeting_Scan,
                id=0x65EF9F2A,
                original_name="Scan",
                from_json=TweakTargeting_Scan.from_json,
                to_json=TweakTargeting_Scan.to_json,
            ),
        },
    )
    unknown_0xc3410560: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC3410560, original_name="Unknown"),
        },
    )
    unknown_0x3eb13041: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3EB13041, original_name="Unknown"),
        },
    )
    unknown_0x5e67cab0: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E67CAB0, original_name="Unknown"),
        },
    )
    unknown_0xe0ca98ac: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE0CA98AC, original_name="Unknown"),
        },
    )
    lock_on_confirm_reticle_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC1E35ABB, original_name="LockOnConfirmReticleScale"),
        },
    )
    unknown_0x9f8d62c1: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F8D62C1, original_name="Unknown"),
        },
    )
    unknown_0xff5eeeb9: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF5EEEB9, original_name="Unknown"),
        },
    )
    unknown_0x0d0b660d: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D0B660D, original_name="Unknown"),
        },
    )
    seeker_target_reticle_scale: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x132DD09E, original_name="SeekerTargetReticleScale"),
        },
    )
    unknown_0x03efc783: float = dataclasses.field(
        default=-120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03EFC783, original_name="Unknown"),
        },
    )
    unknown_0xdcbd7bf8: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDCBD7BF8, original_name="Unknown"),
        },
    )
    unknown_0x2acd6b4b: float = dataclasses.field(
        default=0.9599999785423279,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2ACD6B4B, original_name="Unknown"),
        },
    )
    unknown_0xb4c6c331: float = dataclasses.field(
        default=0.46000000834465027,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB4C6C331, original_name="Unknown"),
        },
    )
    unknown_0x27d02089: float = dataclasses.field(
        default=0.17000000178813934,
        metadata={
            "reflection": FieldReflection[float](float, id=0x27D02089, original_name="Unknown"),
        },
    )
    unknown_0xae89310e: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAE89310E, original_name="Unknown"),
        },
    )
    unknown_0xb27644df: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB27644DF, original_name="Unknown"),
        },
    )
    unknown_0x21e2d1cc: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x21E2D1CC, original_name="Unknown"),
        },
    )
    orbit_point_occluded_opacity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E3AFEF8, original_name="OrbitPointOccludedOpacity"),
        },
    )
    unknown_0x5c489cb5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5C489CB5, original_name="Unknown"),
        },
    )
    orbit_point_z_offset: float = dataclasses.field(
        default=-0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEF2C842E, original_name="OrbitPointZOffset"),
        },
    )
    unknown_0x61a6a38e: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61A6A38E, original_name="Unknown"),
        },
    )
    unknown_0xfbdf31f9: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFBDF31F9, original_name="Unknown"),
        },
    )
    unknown_0xf76f7d0b: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF76F7D0B, original_name="Unknown"),
        },
    )
    unknown_0x810b3a08: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x810B3A08, original_name="Unknown"),
        },
    )
    unknown_0x73fe1553: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x73FE1553, original_name="Unknown"),
        },
    )
    unknown_0xc8aef6f2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC8AEF6F2, original_name="Unknown"),
        },
    )
    unknown_0x69b1e76c: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x69B1E76C, original_name="Unknown"),
        },
    )
    unknown_0x8a0dfd23: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A0DFD23, original_name="Unknown"),
        },
    )
    unknown_0x8299e96e: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8299E96E, original_name="Unknown"),
        },
    )
    unknown_0xa18a3f25: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA18A3F25, original_name="Unknown"),
        },
    )
    unknown_0x23be9bb2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23BE9BB2, original_name="Unknown"),
        },
    )
    unknown_0x8d512b82: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D512B82, original_name="Unknown"),
        },
    )
    unknown_0x39f1698d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39F1698D, original_name="Unknown"),
        },
    )
    unknown_0xc768c1e9: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC768C1E9, original_name="Unknown"),
        },
    )
    unknown_0x55c47b0e: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x55C47B0E, original_name="Unknown"),
        },
    )
    unknown_0xa009aea2: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA009AEA2, original_name="Unknown"),
        },
    )
    unknown_0x38080bbf: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38080BBF, original_name="Unknown"),
        },
    )
    unknown_0x71017dbe: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0x71017DBE, original_name="Unknown"),
        },
    )
    unknown_0x4a996997: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A996997, original_name="Unknown"),
        },
    )
    unknown_0x9f9fa6f3: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F9FA6F3, original_name="Unknown"),
        },
    )
    unknown_0x932fea01: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x932FEA01, original_name="Unknown"),
        },
    )
    unknown_0x165f0fa8: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x165F0FA8, original_name="Unknown"),
        },
    )
    unknown_0x6bd6b11f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6BD6B11F, original_name="Unknown"),
        },
    )
    unknown_0x42420f6e: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x42420F6E, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    flower_reticle_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA63229F1, original_name="FlowerReticleScale"),
        },
    )
    flower_reticle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xBDA45F1A,
                original_name="FlowerReticleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xb090e147: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB090E147, original_name="Unknown"),
        },
    )
    unknown_0x4c73a43d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4C73A43D, original_name="Unknown"),
        },
    )
    unknown_0x6543d31b: float = dataclasses.field(
        default=0.8999999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6543D31B, original_name="Unknown"),
        },
    )
    unknown_0x8cd2d1ce: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8CD2D1CE, original_name="Unknown"),
        },
    )
    missile_bracket_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xE42F6BE0,
                original_name="MissileBracketColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x45910e5d: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x45910E5D, original_name="Unknown"),
        },
    )
    unknown_0x07b30fa0: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x07B30FA0, original_name="Unknown"),
        },
    )
    unknown_0x13ce8500: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x13CE8500, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x9829f256: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x9829F256, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x77a613b9: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x77A613B9, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xdfa81287: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xDFA81287, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    lock_on_confirm_reticle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xDA752C50,
                original_name="LockOnConfirmReticleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    seeker_reticle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x7B544E14,
                original_name="SeekerReticleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x618d150a: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x618D150A, original_name="Unknown"),
        },
    )
    unknown_0x209a2a8c: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x209A2A8C, original_name="Unknown"),
        },
    )
    unknown_0xacb3f8f7: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xACB3F8F7, original_name="Unknown"),
        },
    )
    unknown_0xeda4c771: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEDA4C771, original_name="Unknown"),
        },
    )
    unknown_0xd3427574: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD3427574, original_name="Unknown"),
        },
    )
    unknown_0x92554af2: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x92554AF2, original_name="Unknown"),
        },
    )
    unknown_0x1e134e75: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E134E75, original_name="Unknown"),
        },
    )
    unknown_0x5f0471f3: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5F0471F3, original_name="Unknown"),
        },
    )
    unknown_0xe90548ac: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE90548AC, original_name="Unknown"),
        },
    )
    unknown_0xa812772a: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA812772A, original_name="Unknown"),
        },
    )
    unknown_0x2d75c7be: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2D75C7BE, original_name="Unknown"),
        },
    )
    unknown_0x6c62f838: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C62F838, original_name="Unknown"),
        },
    )
    unknown_0xf98e6242: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF98E6242, original_name="Unknown"),
        },
    )
    unknown_0xb8995dc4: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB8995DC4, original_name="Unknown"),
        },
    )
    unknown_0x5009c614: float = dataclasses.field(
        default=160.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5009C614, original_name="Unknown"),
        },
    )
    unknown_0x111ef992: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x111EF992, original_name="Unknown"),
        },
    )
    grapple_icon_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC0FF888, original_name="GrappleIconScale"),
        },
    )
    grapple_icon_scale_inactive: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF229E05E, original_name="GrappleIconScaleInactive"),
        },
    )
    unknown_0x498d794a: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x498D794A, original_name="Unknown"),
        },
    )
    unknown_0x089a46cc: float = dataclasses.field(
        default=240.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x089A46CC, original_name="Unknown"),
        },
    )
    grapple_icon_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF7998E63, original_name="GrappleIconColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    grapple_icon_color_inactive: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x3CE853E3,
                original_name="GrappleIconColorInactive",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x083b1cc8: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x083B1CC8, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x966982b1: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x966982B1, original_name="Unknown"),
        },
    )
    unknown_0xf9799f5f: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF9799F5F, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x9b980788: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9B980788, original_name="Unknown"),
        },
    )
    orbit_point_model_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x3523A47F,
                original_name="OrbitPointModelColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    crosshairs_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x27358B4D, original_name="CrosshairsColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x2ff52290: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2FF52290, original_name="Unknown"),
        },
    )
    unknown_0x8a548cc9: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8A548CC9, original_name="Unknown"),
        },
    )
    unknown_0x65d449e1: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x65D449E1, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x42c7fbe4: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0x42C7FBE4, original_name="Unknown"),
        },
    )
    unknown_0x13820c03: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x13820C03, original_name="Unknown"),
        },
    )
    unknown_0x52953385: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x52953385, original_name="Unknown"),
        },
    )
    x_ray_seeker_reticle_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x0CD8FE5D,
                original_name="XRaySeekerReticleColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0xdd8cf478: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDD8CF478, original_name="Unknown"),
        },
    )
    unknown_0xcbac6d52: float = dataclasses.field(
        default=32.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCBAC6D52, original_name="Unknown"),
        },
    )
    unknown_0x980a75b6: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x980A75B6, original_name="Unknown"),
        },
    )
    unknown_0xcd1e0e91: float = dataclasses.field(
        default=18.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD1E0E91, original_name="Unknown"),
        },
    )
    unknown_0xce9cf241: float = dataclasses.field(
        default=1.399999976158142,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCE9CF241, original_name="Unknown"),
        },
    )
    unknown_0xb6531e99: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB6531E99, original_name="Unknown"),
        },
    )
    unknown_0x77e5c6b5: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x77E5C6B5, original_name="Unknown"),
        },
    )
    unknown_0xfef5668b: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFEF5668B, original_name="Unknown"),
        },
    )
    health_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5CE2A16F, original_name="HealthColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    power_vulnerability_indicator: TweakTargeting_VulnerabilityIndicator = dataclasses.field(
        default_factory=TweakTargeting_VulnerabilityIndicator,
        metadata={
            "reflection": FieldReflection[TweakTargeting_VulnerabilityIndicator](
                TweakTargeting_VulnerabilityIndicator,
                id=0x1E179603,
                original_name="PowerVulnerabilityIndicator",
                from_json=TweakTargeting_VulnerabilityIndicator.from_json,
                to_json=TweakTargeting_VulnerabilityIndicator.to_json,
            ),
        },
    )
    light_vulnerability_indicator: TweakTargeting_VulnerabilityIndicator = dataclasses.field(
        default_factory=TweakTargeting_VulnerabilityIndicator,
        metadata={
            "reflection": FieldReflection[TweakTargeting_VulnerabilityIndicator](
                TweakTargeting_VulnerabilityIndicator,
                id=0x2B70CEF8,
                original_name="LightVulnerabilityIndicator",
                from_json=TweakTargeting_VulnerabilityIndicator.from_json,
                to_json=TweakTargeting_VulnerabilityIndicator.to_json,
            ),
        },
    )
    dark_vulnerability_indicator: TweakTargeting_VulnerabilityIndicator = dataclasses.field(
        default_factory=TweakTargeting_VulnerabilityIndicator,
        metadata={
            "reflection": FieldReflection[TweakTargeting_VulnerabilityIndicator](
                TweakTargeting_VulnerabilityIndicator,
                id=0x946CEFDE,
                original_name="DarkVulnerabilityIndicator",
                from_json=TweakTargeting_VulnerabilityIndicator.from_json,
                to_json=TweakTargeting_VulnerabilityIndicator.to_json,
            ),
        },
    )
    annihilator_vulnerability_indicator: TweakTargeting_VulnerabilityIndicator = dataclasses.field(
        default_factory=TweakTargeting_VulnerabilityIndicator,
        metadata={
            "reflection": FieldReflection[TweakTargeting_VulnerabilityIndicator](
                TweakTargeting_VulnerabilityIndicator,
                id=0x921C86E1,
                original_name="AnnihilatorVulnerabilityIndicator",
                from_json=TweakTargeting_VulnerabilityIndicator.from_json,
                to_json=TweakTargeting_VulnerabilityIndicator.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return "TWTG"

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 117:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDA1466
        instance_name = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5173932F
        unknown_0x5173932f = TweakTargeting_OuterBeamIcon.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23FF4BE4
        unknown_0x23ff4be4 = TIcon_Configurations.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92E98613
        unknown_0x92e98613 = TIcon_Configurations.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64833842
        unknown_0x64833842 = TIcon_Configurations.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8DFD6E3C
        unknown_0x8dfd6e3c = TIcon_Configurations.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC5A41B2
        charge_gauge = TweakTargeting_Charge_Gauge.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00183589
        lock_fire = TweakTargeting_LockFire.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD20ECC07
        lock_dagger = TweakTargeting_LockDagger.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65EF9F2A
        scan = TweakTargeting_Scan.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3410560
        unknown_0xc3410560 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3EB13041
        unknown_0x3eb13041 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E67CAB0
        unknown_0x5e67cab0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0CA98AC
        unknown_0xe0ca98ac = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC1E35ABB
        lock_on_confirm_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F8D62C1
        unknown_0x9f8d62c1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF5EEEB9
        unknown_0xff5eeeb9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D0B660D
        unknown_0x0d0b660d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x132DD09E
        seeker_target_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03EFC783
        unknown_0x03efc783 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCBD7BF8
        unknown_0xdcbd7bf8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ACD6B4B
        unknown_0x2acd6b4b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB4C6C331
        unknown_0xb4c6c331 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27D02089
        unknown_0x27d02089 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE89310E
        unknown_0xae89310e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB27644DF
        unknown_0xb27644df = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21E2D1CC
        unknown_0x21e2d1cc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E3AFEF8
        orbit_point_occluded_opacity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C489CB5
        unknown_0x5c489cb5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF2C842E
        orbit_point_z_offset = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61A6A38E
        unknown_0x61a6a38e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBDF31F9
        unknown_0xfbdf31f9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF76F7D0B
        unknown_0xf76f7d0b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x810B3A08
        unknown_0x810b3a08 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73FE1553
        unknown_0x73fe1553 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8AEF6F2
        unknown_0xc8aef6f2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69B1E76C
        unknown_0x69b1e76c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A0DFD23
        unknown_0x8a0dfd23 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8299E96E
        unknown_0x8299e96e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA18A3F25
        unknown_0xa18a3f25 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23BE9BB2
        unknown_0x23be9bb2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D512B82
        unknown_0x8d512b82 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39F1698D
        unknown_0x39f1698d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC768C1E9
        unknown_0xc768c1e9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55C47B0E
        unknown_0x55c47b0e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA009AEA2
        unknown_0xa009aea2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38080BBF
        unknown_0x38080bbf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71017DBE
        unknown_0x71017dbe = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A996997
        unknown_0x4a996997 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F9FA6F3
        unknown_0x9f9fa6f3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x932FEA01
        unknown_0x932fea01 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x165F0FA8
        unknown_0x165f0fa8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BD6B11F
        unknown_0x6bd6b11f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42420F6E
        unknown_0x42420f6e = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA63229F1
        flower_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBDA45F1A
        flower_reticle_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB090E147
        unknown_0xb090e147 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C73A43D
        unknown_0x4c73a43d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6543D31B
        unknown_0x6543d31b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8CD2D1CE
        unknown_0x8cd2d1ce = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE42F6BE0
        missile_bracket_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45910E5D
        unknown_0x45910e5d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07B30FA0
        unknown_0x07b30fa0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13CE8500
        unknown_0x13ce8500 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9829F256
        unknown_0x9829f256 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77A613B9
        unknown_0x77a613b9 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFA81287
        unknown_0xdfa81287 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDA752C50
        lock_on_confirm_reticle_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B544E14
        seeker_reticle_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x618D150A
        unknown_0x618d150a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x209A2A8C
        unknown_0x209a2a8c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACB3F8F7
        unknown_0xacb3f8f7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA4C771
        unknown_0xeda4c771 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3427574
        unknown_0xd3427574 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92554AF2
        unknown_0x92554af2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E134E75
        unknown_0x1e134e75 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F0471F3
        unknown_0x5f0471f3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE90548AC
        unknown_0xe90548ac = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA812772A
        unknown_0xa812772a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D75C7BE
        unknown_0x2d75c7be = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C62F838
        unknown_0x6c62f838 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF98E6242
        unknown_0xf98e6242 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8995DC4
        unknown_0xb8995dc4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5009C614
        unknown_0x5009c614 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x111EF992
        unknown_0x111ef992 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC0FF888
        grapple_icon_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF229E05E
        grapple_icon_scale_inactive = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x498D794A
        unknown_0x498d794a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x089A46CC
        unknown_0x089a46cc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF7998E63
        grapple_icon_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3CE853E3
        grapple_icon_color_inactive = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x083B1CC8
        unknown_0x083b1cc8 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x966982B1
        unknown_0x966982b1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9799F5F
        unknown_0xf9799f5f = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B980788
        unknown_0x9b980788 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3523A47F
        orbit_point_model_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27358B4D
        crosshairs_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2FF52290
        unknown_0x2ff52290 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A548CC9
        unknown_0x8a548cc9 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65D449E1
        unknown_0x65d449e1 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42C7FBE4
        unknown_0x42c7fbe4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13820C03
        unknown_0x13820c03 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52953385
        unknown_0x52953385 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CD8FE5D
        x_ray_seeker_reticle_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD8CF478
        unknown_0xdd8cf478 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCBAC6D52
        unknown_0xcbac6d52 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x980A75B6
        unknown_0x980a75b6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD1E0E91
        unknown_0xcd1e0e91 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE9CF241
        unknown_0xce9cf241 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6531E99
        unknown_0xb6531e99 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77E5C6B5
        unknown_0x77e5c6b5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFEF5668B
        unknown_0xfef5668b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5CE2A16F
        health_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E179603
        power_vulnerability_indicator = TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B70CEF8
        light_vulnerability_indicator = TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x946CEFDE
        dark_vulnerability_indicator = TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x921C86E1
        annihilator_vulnerability_indicator = TweakTargeting_VulnerabilityIndicator.from_stream(
            data, game, property_size
        )

        return cls(
            instance_name,
            unknown_0x5173932f,
            unknown_0x23ff4be4,
            unknown_0x92e98613,
            unknown_0x64833842,
            unknown_0x8dfd6e3c,
            charge_gauge,
            lock_fire,
            lock_dagger,
            scan,
            unknown_0xc3410560,
            unknown_0x3eb13041,
            unknown_0x5e67cab0,
            unknown_0xe0ca98ac,
            lock_on_confirm_reticle_scale,
            unknown_0x9f8d62c1,
            unknown_0xff5eeeb9,
            unknown_0x0d0b660d,
            seeker_target_reticle_scale,
            unknown_0x03efc783,
            unknown_0xdcbd7bf8,
            unknown_0x2acd6b4b,
            unknown_0xb4c6c331,
            unknown_0x27d02089,
            unknown_0xae89310e,
            unknown_0xb27644df,
            unknown_0x21e2d1cc,
            orbit_point_occluded_opacity,
            unknown_0x5c489cb5,
            orbit_point_z_offset,
            unknown_0x61a6a38e,
            unknown_0xfbdf31f9,
            unknown_0xf76f7d0b,
            unknown_0x810b3a08,
            unknown_0x73fe1553,
            unknown_0xc8aef6f2,
            unknown_0x69b1e76c,
            unknown_0x8a0dfd23,
            unknown_0x8299e96e,
            unknown_0xa18a3f25,
            unknown_0x23be9bb2,
            unknown_0x8d512b82,
            unknown_0x39f1698d,
            unknown_0xc768c1e9,
            unknown_0x55c47b0e,
            unknown_0xa009aea2,
            unknown_0x38080bbf,
            unknown_0x71017dbe,
            unknown_0x4a996997,
            unknown_0x9f9fa6f3,
            unknown_0x932fea01,
            unknown_0x165f0fa8,
            unknown_0x6bd6b11f,
            unknown_0x42420f6e,
            flower_reticle_scale,
            flower_reticle_color,
            unknown_0xb090e147,
            unknown_0x4c73a43d,
            unknown_0x6543d31b,
            unknown_0x8cd2d1ce,
            missile_bracket_color,
            unknown_0x45910e5d,
            unknown_0x07b30fa0,
            unknown_0x13ce8500,
            unknown_0x9829f256,
            unknown_0x77a613b9,
            unknown_0xdfa81287,
            lock_on_confirm_reticle_color,
            seeker_reticle_color,
            unknown_0x618d150a,
            unknown_0x209a2a8c,
            unknown_0xacb3f8f7,
            unknown_0xeda4c771,
            unknown_0xd3427574,
            unknown_0x92554af2,
            unknown_0x1e134e75,
            unknown_0x5f0471f3,
            unknown_0xe90548ac,
            unknown_0xa812772a,
            unknown_0x2d75c7be,
            unknown_0x6c62f838,
            unknown_0xf98e6242,
            unknown_0xb8995dc4,
            unknown_0x5009c614,
            unknown_0x111ef992,
            grapple_icon_scale,
            grapple_icon_scale_inactive,
            unknown_0x498d794a,
            unknown_0x089a46cc,
            grapple_icon_color,
            grapple_icon_color_inactive,
            unknown_0x083b1cc8,
            unknown_0x966982b1,
            unknown_0xf9799f5f,
            unknown_0x9b980788,
            orbit_point_model_color,
            crosshairs_color,
            unknown_0x2ff52290,
            unknown_0x8a548cc9,
            unknown_0x65d449e1,
            unknown_0x42c7fbe4,
            unknown_0x13820c03,
            unknown_0x52953385,
            x_ray_seeker_reticle_color,
            unknown_0xdd8cf478,
            unknown_0xcbac6d52,
            unknown_0x980a75b6,
            unknown_0xcd1e0e91,
            unknown_0xce9cf241,
            unknown_0xb6531e99,
            unknown_0x77e5c6b5,
            unknown_0xfef5668b,
            health_color,
            power_vulnerability_indicator,
            light_vulnerability_indicator,
            dark_vulnerability_indicator,
            annihilator_vulnerability_indicator,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00u")  # 117 properties

        data.write(b"\x7f\xda\x14f")  # 0x7fda1466
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.instance_name.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Qs\x93/")  # 0x5173932f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x5173932f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"#\xffK\xe4")  # 0x23ff4be4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x23ff4be4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x92\xe9\x86\x13")  # 0x92e98613
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x92e98613.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"d\x838B")  # 0x64833842
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x64833842.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8d\xfdn<")  # 0x8dfd6e3c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x8dfd6e3c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbcZA\xb2")  # 0xbc5a41b2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.charge_gauge.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\x185\x89")  # 0x183589
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.lock_fire.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd2\x0e\xcc\x07")  # 0xd20ecc07
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.lock_dagger.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"e\xef\x9f*")  # 0x65ef9f2a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.scan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc3A\x05`")  # 0xc3410560
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc3410560))

        data.write(b">\xb10A")  # 0x3eb13041
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3eb13041))

        data.write(b"^g\xca\xb0")  # 0x5e67cab0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5e67cab0))

        data.write(b"\xe0\xca\x98\xac")  # 0xe0ca98ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe0ca98ac))

        data.write(b"\xc1\xe3Z\xbb")  # 0xc1e35abb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lock_on_confirm_reticle_scale))

        data.write(b"\x9f\x8db\xc1")  # 0x9f8d62c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9f8d62c1))

        data.write(b"\xff^\xee\xb9")  # 0xff5eeeb9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xff5eeeb9))

        data.write(b"\r\x0bf\r")  # 0xd0b660d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0d0b660d))

        data.write(b"\x13-\xd0\x9e")  # 0x132dd09e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.seeker_target_reticle_scale))

        data.write(b"\x03\xef\xc7\x83")  # 0x3efc783
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x03efc783))

        data.write(b"\xdc\xbd{\xf8")  # 0xdcbd7bf8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdcbd7bf8))

        data.write(b"*\xcdkK")  # 0x2acd6b4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2acd6b4b))

        data.write(b"\xb4\xc6\xc31")  # 0xb4c6c331
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb4c6c331))

        data.write(b"'\xd0 \x89")  # 0x27d02089
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x27d02089))

        data.write(b"\xae\x891\x0e")  # 0xae89310e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xae89310e))

        data.write(b"\xb2vD\xdf")  # 0xb27644df
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb27644df))

        data.write(b"!\xe2\xd1\xcc")  # 0x21e2d1cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x21e2d1cc))

        data.write(b"\x8e:\xfe\xf8")  # 0x8e3afef8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.orbit_point_occluded_opacity))

        data.write(b"\\H\x9c\xb5")  # 0x5c489cb5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5c489cb5))

        data.write(b"\xef,\x84.")  # 0xef2c842e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.orbit_point_z_offset))

        data.write(b"a\xa6\xa3\x8e")  # 0x61a6a38e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x61a6a38e))

        data.write(b"\xfb\xdf1\xf9")  # 0xfbdf31f9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfbdf31f9))

        data.write(b"\xf7o}\x0b")  # 0xf76f7d0b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf76f7d0b))

        data.write(b"\x81\x0b:\x08")  # 0x810b3a08
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x810b3a08))

        data.write(b"s\xfe\x15S")  # 0x73fe1553
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x73fe1553))

        data.write(b"\xc8\xae\xf6\xf2")  # 0xc8aef6f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc8aef6f2))

        data.write(b"i\xb1\xe7l")  # 0x69b1e76c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x69b1e76c))

        data.write(b"\x8a\r\xfd#")  # 0x8a0dfd23
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8a0dfd23))

        data.write(b"\x82\x99\xe9n")  # 0x8299e96e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8299e96e))

        data.write(b"\xa1\x8a?%")  # 0xa18a3f25
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa18a3f25))

        data.write(b"#\xbe\x9b\xb2")  # 0x23be9bb2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x23be9bb2))

        data.write(b"\x8dQ+\x82")  # 0x8d512b82
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8d512b82))

        data.write(b"9\xf1i\x8d")  # 0x39f1698d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x39f1698d))

        data.write(b"\xc7h\xc1\xe9")  # 0xc768c1e9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc768c1e9))

        data.write(b"U\xc4{\x0e")  # 0x55c47b0e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x55c47b0e))

        data.write(b"\xa0\t\xae\xa2")  # 0xa009aea2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa009aea2))

        data.write(b"8\x08\x0b\xbf")  # 0x38080bbf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x38080bbf))

        data.write(b"q\x01}\xbe")  # 0x71017dbe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x71017dbe))

        data.write(b"J\x99i\x97")  # 0x4a996997
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4a996997))

        data.write(b"\x9f\x9f\xa6\xf3")  # 0x9f9fa6f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9f9fa6f3))

        data.write(b"\x93/\xea\x01")  # 0x932fea01
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x932fea01))

        data.write(b"\x16_\x0f\xa8")  # 0x165f0fa8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x165f0fa8))

        data.write(b"k\xd6\xb1\x1f")  # 0x6bd6b11f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6bd6b11f))

        data.write(b"BB\x0fn")  # 0x42420f6e
        data.write(b"\x00\x10")  # size
        self.unknown_0x42420f6e.to_stream(data, game)

        data.write(b"\xa62)\xf1")  # 0xa63229f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flower_reticle_scale))

        data.write(b"\xbd\xa4_\x1a")  # 0xbda45f1a
        data.write(b"\x00\x10")  # size
        self.flower_reticle_color.to_stream(data, game)

        data.write(b"\xb0\x90\xe1G")  # 0xb090e147
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb090e147))

        data.write(b"Ls\xa4=")  # 0x4c73a43d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4c73a43d))

        data.write(b"eC\xd3\x1b")  # 0x6543d31b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6543d31b))

        data.write(b"\x8c\xd2\xd1\xce")  # 0x8cd2d1ce
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8cd2d1ce))

        data.write(b"\xe4/k\xe0")  # 0xe42f6be0
        data.write(b"\x00\x10")  # size
        self.missile_bracket_color.to_stream(data, game)

        data.write(b"E\x91\x0e]")  # 0x45910e5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x45910e5d))

        data.write(b"\x07\xb3\x0f\xa0")  # 0x7b30fa0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x07b30fa0))

        data.write(b"\x13\xce\x85\x00")  # 0x13ce8500
        data.write(b"\x00\x10")  # size
        self.unknown_0x13ce8500.to_stream(data, game)

        data.write(b"\x98)\xf2V")  # 0x9829f256
        data.write(b"\x00\x10")  # size
        self.unknown_0x9829f256.to_stream(data, game)

        data.write(b"w\xa6\x13\xb9")  # 0x77a613b9
        data.write(b"\x00\x10")  # size
        self.unknown_0x77a613b9.to_stream(data, game)

        data.write(b"\xdf\xa8\x12\x87")  # 0xdfa81287
        data.write(b"\x00\x10")  # size
        self.unknown_0xdfa81287.to_stream(data, game)

        data.write(b"\xdau,P")  # 0xda752c50
        data.write(b"\x00\x10")  # size
        self.lock_on_confirm_reticle_color.to_stream(data, game)

        data.write(b"{TN\x14")  # 0x7b544e14
        data.write(b"\x00\x10")  # size
        self.seeker_reticle_color.to_stream(data, game)

        data.write(b"a\x8d\x15\n")  # 0x618d150a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x618d150a))

        data.write(b" \x9a*\x8c")  # 0x209a2a8c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x209a2a8c))

        data.write(b"\xac\xb3\xf8\xf7")  # 0xacb3f8f7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xacb3f8f7))

        data.write(b"\xed\xa4\xc7q")  # 0xeda4c771
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeda4c771))

        data.write(b"\xd3But")  # 0xd3427574
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd3427574))

        data.write(b"\x92UJ\xf2")  # 0x92554af2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x92554af2))

        data.write(b"\x1e\x13Nu")  # 0x1e134e75
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1e134e75))

        data.write(b"_\x04q\xf3")  # 0x5f0471f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5f0471f3))

        data.write(b"\xe9\x05H\xac")  # 0xe90548ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe90548ac))

        data.write(b"\xa8\x12w*")  # 0xa812772a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa812772a))

        data.write(b"-u\xc7\xbe")  # 0x2d75c7be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2d75c7be))

        data.write(b"lb\xf88")  # 0x6c62f838
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6c62f838))

        data.write(b"\xf9\x8ebB")  # 0xf98e6242
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf98e6242))

        data.write(b"\xb8\x99]\xc4")  # 0xb8995dc4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb8995dc4))

        data.write(b"P\t\xc6\x14")  # 0x5009c614
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5009c614))

        data.write(b"\x11\x1e\xf9\x92")  # 0x111ef992
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x111ef992))

        data.write(b"\xec\x0f\xf8\x88")  # 0xec0ff888
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_icon_scale))

        data.write(b"\xf2)\xe0^")  # 0xf229e05e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_icon_scale_inactive))

        data.write(b"I\x8dyJ")  # 0x498d794a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x498d794a))

        data.write(b"\x08\x9aF\xcc")  # 0x89a46cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x089a46cc))

        data.write(b"\xf7\x99\x8ec")  # 0xf7998e63
        data.write(b"\x00\x10")  # size
        self.grapple_icon_color.to_stream(data, game)

        data.write(b"<\xe8S\xe3")  # 0x3ce853e3
        data.write(b"\x00\x10")  # size
        self.grapple_icon_color_inactive.to_stream(data, game)

        data.write(b"\x08;\x1c\xc8")  # 0x83b1cc8
        data.write(b"\x00\x10")  # size
        self.unknown_0x083b1cc8.to_stream(data, game)

        data.write(b"\x96i\x82\xb1")  # 0x966982b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x966982b1))

        data.write(b"\xf9y\x9f_")  # 0xf9799f5f
        data.write(b"\x00\x10")  # size
        self.unknown_0xf9799f5f.to_stream(data, game)

        data.write(b"\x9b\x98\x07\x88")  # 0x9b980788
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9b980788))

        data.write(b"5#\xa4\x7f")  # 0x3523a47f
        data.write(b"\x00\x10")  # size
        self.orbit_point_model_color.to_stream(data, game)

        data.write(b"'5\x8bM")  # 0x27358b4d
        data.write(b"\x00\x10")  # size
        self.crosshairs_color.to_stream(data, game)

        data.write(b'/\xf5"\x90')  # 0x2ff52290
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2ff52290))

        data.write(b"\x8aT\x8c\xc9")  # 0x8a548cc9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x8a548cc9))

        data.write(b"e\xd4I\xe1")  # 0x65d449e1
        data.write(b"\x00\x10")  # size
        self.unknown_0x65d449e1.to_stream(data, game)

        data.write(b"B\xc7\xfb\xe4")  # 0x42c7fbe4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x42c7fbe4))

        data.write(b"\x13\x82\x0c\x03")  # 0x13820c03
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x13820c03))

        data.write(b"R\x953\x85")  # 0x52953385
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x52953385))

        data.write(b"\x0c\xd8\xfe]")  # 0xcd8fe5d
        data.write(b"\x00\x10")  # size
        self.x_ray_seeker_reticle_color.to_stream(data, game)

        data.write(b"\xdd\x8c\xf4x")  # 0xdd8cf478
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdd8cf478))

        data.write(b"\xcb\xacmR")  # 0xcbac6d52
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcbac6d52))

        data.write(b"\x98\nu\xb6")  # 0x980a75b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x980a75b6))

        data.write(b"\xcd\x1e\x0e\x91")  # 0xcd1e0e91
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd1e0e91))

        data.write(b"\xce\x9c\xf2A")  # 0xce9cf241
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xce9cf241))

        data.write(b"\xb6S\x1e\x99")  # 0xb6531e99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb6531e99))

        data.write(b"w\xe5\xc6\xb5")  # 0x77e5c6b5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x77e5c6b5))

        data.write(b"\xfe\xf5f\x8b")  # 0xfef5668b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfef5668b))

        data.write(b"\\\xe2\xa1o")  # 0x5ce2a16f
        data.write(b"\x00\x10")  # size
        self.health_color.to_stream(data, game)

        data.write(b"\x1e\x17\x96\x03")  # 0x1e179603
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_vulnerability_indicator.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+p\xce\xf8")  # 0x2b70cef8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.light_vulnerability_indicator.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x94l\xef\xde")  # 0x946cefde
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dark_vulnerability_indicator.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x92\x1c\x86\xe1")  # 0x921c86e1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.annihilator_vulnerability_indicator.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargetingJson", data)
        return cls(
            instance_name=json_data["instance_name"],
            unknown_0x5173932f=TweakTargeting_OuterBeamIcon.from_json(json_data["unknown_0x5173932f"]),
            unknown_0x23ff4be4=TIcon_Configurations.from_json(json_data["unknown_0x23ff4be4"]),
            unknown_0x92e98613=TIcon_Configurations.from_json(json_data["unknown_0x92e98613"]),
            unknown_0x64833842=TIcon_Configurations.from_json(json_data["unknown_0x64833842"]),
            unknown_0x8dfd6e3c=TIcon_Configurations.from_json(json_data["unknown_0x8dfd6e3c"]),
            charge_gauge=TweakTargeting_Charge_Gauge.from_json(json_data["charge_gauge"]),
            lock_fire=TweakTargeting_LockFire.from_json(json_data["lock_fire"]),
            lock_dagger=TweakTargeting_LockDagger.from_json(json_data["lock_dagger"]),
            scan=TweakTargeting_Scan.from_json(json_data["scan"]),
            unknown_0xc3410560=json_data["unknown_0xc3410560"],
            unknown_0x3eb13041=json_data["unknown_0x3eb13041"],
            unknown_0x5e67cab0=json_data["unknown_0x5e67cab0"],
            unknown_0xe0ca98ac=json_data["unknown_0xe0ca98ac"],
            lock_on_confirm_reticle_scale=json_data["lock_on_confirm_reticle_scale"],
            unknown_0x9f8d62c1=json_data["unknown_0x9f8d62c1"],
            unknown_0xff5eeeb9=json_data["unknown_0xff5eeeb9"],
            unknown_0x0d0b660d=json_data["unknown_0x0d0b660d"],
            seeker_target_reticle_scale=json_data["seeker_target_reticle_scale"],
            unknown_0x03efc783=json_data["unknown_0x03efc783"],
            unknown_0xdcbd7bf8=json_data["unknown_0xdcbd7bf8"],
            unknown_0x2acd6b4b=json_data["unknown_0x2acd6b4b"],
            unknown_0xb4c6c331=json_data["unknown_0xb4c6c331"],
            unknown_0x27d02089=json_data["unknown_0x27d02089"],
            unknown_0xae89310e=json_data["unknown_0xae89310e"],
            unknown_0xb27644df=json_data["unknown_0xb27644df"],
            unknown_0x21e2d1cc=json_data["unknown_0x21e2d1cc"],
            orbit_point_occluded_opacity=json_data["orbit_point_occluded_opacity"],
            unknown_0x5c489cb5=json_data["unknown_0x5c489cb5"],
            orbit_point_z_offset=json_data["orbit_point_z_offset"],
            unknown_0x61a6a38e=json_data["unknown_0x61a6a38e"],
            unknown_0xfbdf31f9=json_data["unknown_0xfbdf31f9"],
            unknown_0xf76f7d0b=json_data["unknown_0xf76f7d0b"],
            unknown_0x810b3a08=json_data["unknown_0x810b3a08"],
            unknown_0x73fe1553=json_data["unknown_0x73fe1553"],
            unknown_0xc8aef6f2=json_data["unknown_0xc8aef6f2"],
            unknown_0x69b1e76c=json_data["unknown_0x69b1e76c"],
            unknown_0x8a0dfd23=json_data["unknown_0x8a0dfd23"],
            unknown_0x8299e96e=json_data["unknown_0x8299e96e"],
            unknown_0xa18a3f25=json_data["unknown_0xa18a3f25"],
            unknown_0x23be9bb2=json_data["unknown_0x23be9bb2"],
            unknown_0x8d512b82=json_data["unknown_0x8d512b82"],
            unknown_0x39f1698d=json_data["unknown_0x39f1698d"],
            unknown_0xc768c1e9=json_data["unknown_0xc768c1e9"],
            unknown_0x55c47b0e=json_data["unknown_0x55c47b0e"],
            unknown_0xa009aea2=json_data["unknown_0xa009aea2"],
            unknown_0x38080bbf=json_data["unknown_0x38080bbf"],
            unknown_0x71017dbe=json_data["unknown_0x71017dbe"],
            unknown_0x4a996997=json_data["unknown_0x4a996997"],
            unknown_0x9f9fa6f3=json_data["unknown_0x9f9fa6f3"],
            unknown_0x932fea01=json_data["unknown_0x932fea01"],
            unknown_0x165f0fa8=json_data["unknown_0x165f0fa8"],
            unknown_0x6bd6b11f=json_data["unknown_0x6bd6b11f"],
            unknown_0x42420f6e=Color.from_json(json_data["unknown_0x42420f6e"]),
            flower_reticle_scale=json_data["flower_reticle_scale"],
            flower_reticle_color=Color.from_json(json_data["flower_reticle_color"]),
            unknown_0xb090e147=json_data["unknown_0xb090e147"],
            unknown_0x4c73a43d=json_data["unknown_0x4c73a43d"],
            unknown_0x6543d31b=json_data["unknown_0x6543d31b"],
            unknown_0x8cd2d1ce=json_data["unknown_0x8cd2d1ce"],
            missile_bracket_color=Color.from_json(json_data["missile_bracket_color"]),
            unknown_0x45910e5d=json_data["unknown_0x45910e5d"],
            unknown_0x07b30fa0=json_data["unknown_0x07b30fa0"],
            unknown_0x13ce8500=Color.from_json(json_data["unknown_0x13ce8500"]),
            unknown_0x9829f256=Color.from_json(json_data["unknown_0x9829f256"]),
            unknown_0x77a613b9=Color.from_json(json_data["unknown_0x77a613b9"]),
            unknown_0xdfa81287=Color.from_json(json_data["unknown_0xdfa81287"]),
            lock_on_confirm_reticle_color=Color.from_json(json_data["lock_on_confirm_reticle_color"]),
            seeker_reticle_color=Color.from_json(json_data["seeker_reticle_color"]),
            unknown_0x618d150a=json_data["unknown_0x618d150a"],
            unknown_0x209a2a8c=json_data["unknown_0x209a2a8c"],
            unknown_0xacb3f8f7=json_data["unknown_0xacb3f8f7"],
            unknown_0xeda4c771=json_data["unknown_0xeda4c771"],
            unknown_0xd3427574=json_data["unknown_0xd3427574"],
            unknown_0x92554af2=json_data["unknown_0x92554af2"],
            unknown_0x1e134e75=json_data["unknown_0x1e134e75"],
            unknown_0x5f0471f3=json_data["unknown_0x5f0471f3"],
            unknown_0xe90548ac=json_data["unknown_0xe90548ac"],
            unknown_0xa812772a=json_data["unknown_0xa812772a"],
            unknown_0x2d75c7be=json_data["unknown_0x2d75c7be"],
            unknown_0x6c62f838=json_data["unknown_0x6c62f838"],
            unknown_0xf98e6242=json_data["unknown_0xf98e6242"],
            unknown_0xb8995dc4=json_data["unknown_0xb8995dc4"],
            unknown_0x5009c614=json_data["unknown_0x5009c614"],
            unknown_0x111ef992=json_data["unknown_0x111ef992"],
            grapple_icon_scale=json_data["grapple_icon_scale"],
            grapple_icon_scale_inactive=json_data["grapple_icon_scale_inactive"],
            unknown_0x498d794a=json_data["unknown_0x498d794a"],
            unknown_0x089a46cc=json_data["unknown_0x089a46cc"],
            grapple_icon_color=Color.from_json(json_data["grapple_icon_color"]),
            grapple_icon_color_inactive=Color.from_json(json_data["grapple_icon_color_inactive"]),
            unknown_0x083b1cc8=Color.from_json(json_data["unknown_0x083b1cc8"]),
            unknown_0x966982b1=json_data["unknown_0x966982b1"],
            unknown_0xf9799f5f=Color.from_json(json_data["unknown_0xf9799f5f"]),
            unknown_0x9b980788=json_data["unknown_0x9b980788"],
            orbit_point_model_color=Color.from_json(json_data["orbit_point_model_color"]),
            crosshairs_color=Color.from_json(json_data["crosshairs_color"]),
            unknown_0x2ff52290=json_data["unknown_0x2ff52290"],
            unknown_0x8a548cc9=json_data["unknown_0x8a548cc9"],
            unknown_0x65d449e1=Color.from_json(json_data["unknown_0x65d449e1"]),
            unknown_0x42c7fbe4=json_data["unknown_0x42c7fbe4"],
            unknown_0x13820c03=json_data["unknown_0x13820c03"],
            unknown_0x52953385=json_data["unknown_0x52953385"],
            x_ray_seeker_reticle_color=Color.from_json(json_data["x_ray_seeker_reticle_color"]),
            unknown_0xdd8cf478=json_data["unknown_0xdd8cf478"],
            unknown_0xcbac6d52=json_data["unknown_0xcbac6d52"],
            unknown_0x980a75b6=json_data["unknown_0x980a75b6"],
            unknown_0xcd1e0e91=json_data["unknown_0xcd1e0e91"],
            unknown_0xce9cf241=json_data["unknown_0xce9cf241"],
            unknown_0xb6531e99=json_data["unknown_0xb6531e99"],
            unknown_0x77e5c6b5=json_data["unknown_0x77e5c6b5"],
            unknown_0xfef5668b=json_data["unknown_0xfef5668b"],
            health_color=Color.from_json(json_data["health_color"]),
            power_vulnerability_indicator=TweakTargeting_VulnerabilityIndicator.from_json(
                json_data["power_vulnerability_indicator"]
            ),
            light_vulnerability_indicator=TweakTargeting_VulnerabilityIndicator.from_json(
                json_data["light_vulnerability_indicator"]
            ),
            dark_vulnerability_indicator=TweakTargeting_VulnerabilityIndicator.from_json(
                json_data["dark_vulnerability_indicator"]
            ),
            annihilator_vulnerability_indicator=TweakTargeting_VulnerabilityIndicator.from_json(
                json_data["annihilator_vulnerability_indicator"]
            ),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "instance_name": self.instance_name,
            "unknown_0x5173932f": self.unknown_0x5173932f.to_json(),
            "unknown_0x23ff4be4": self.unknown_0x23ff4be4.to_json(),
            "unknown_0x92e98613": self.unknown_0x92e98613.to_json(),
            "unknown_0x64833842": self.unknown_0x64833842.to_json(),
            "unknown_0x8dfd6e3c": self.unknown_0x8dfd6e3c.to_json(),
            "charge_gauge": self.charge_gauge.to_json(),
            "lock_fire": self.lock_fire.to_json(),
            "lock_dagger": self.lock_dagger.to_json(),
            "scan": self.scan.to_json(),
            "unknown_0xc3410560": self.unknown_0xc3410560,
            "unknown_0x3eb13041": self.unknown_0x3eb13041,
            "unknown_0x5e67cab0": self.unknown_0x5e67cab0,
            "unknown_0xe0ca98ac": self.unknown_0xe0ca98ac,
            "lock_on_confirm_reticle_scale": self.lock_on_confirm_reticle_scale,
            "unknown_0x9f8d62c1": self.unknown_0x9f8d62c1,
            "unknown_0xff5eeeb9": self.unknown_0xff5eeeb9,
            "unknown_0x0d0b660d": self.unknown_0x0d0b660d,
            "seeker_target_reticle_scale": self.seeker_target_reticle_scale,
            "unknown_0x03efc783": self.unknown_0x03efc783,
            "unknown_0xdcbd7bf8": self.unknown_0xdcbd7bf8,
            "unknown_0x2acd6b4b": self.unknown_0x2acd6b4b,
            "unknown_0xb4c6c331": self.unknown_0xb4c6c331,
            "unknown_0x27d02089": self.unknown_0x27d02089,
            "unknown_0xae89310e": self.unknown_0xae89310e,
            "unknown_0xb27644df": self.unknown_0xb27644df,
            "unknown_0x21e2d1cc": self.unknown_0x21e2d1cc,
            "orbit_point_occluded_opacity": self.orbit_point_occluded_opacity,
            "unknown_0x5c489cb5": self.unknown_0x5c489cb5,
            "orbit_point_z_offset": self.orbit_point_z_offset,
            "unknown_0x61a6a38e": self.unknown_0x61a6a38e,
            "unknown_0xfbdf31f9": self.unknown_0xfbdf31f9,
            "unknown_0xf76f7d0b": self.unknown_0xf76f7d0b,
            "unknown_0x810b3a08": self.unknown_0x810b3a08,
            "unknown_0x73fe1553": self.unknown_0x73fe1553,
            "unknown_0xc8aef6f2": self.unknown_0xc8aef6f2,
            "unknown_0x69b1e76c": self.unknown_0x69b1e76c,
            "unknown_0x8a0dfd23": self.unknown_0x8a0dfd23,
            "unknown_0x8299e96e": self.unknown_0x8299e96e,
            "unknown_0xa18a3f25": self.unknown_0xa18a3f25,
            "unknown_0x23be9bb2": self.unknown_0x23be9bb2,
            "unknown_0x8d512b82": self.unknown_0x8d512b82,
            "unknown_0x39f1698d": self.unknown_0x39f1698d,
            "unknown_0xc768c1e9": self.unknown_0xc768c1e9,
            "unknown_0x55c47b0e": self.unknown_0x55c47b0e,
            "unknown_0xa009aea2": self.unknown_0xa009aea2,
            "unknown_0x38080bbf": self.unknown_0x38080bbf,
            "unknown_0x71017dbe": self.unknown_0x71017dbe,
            "unknown_0x4a996997": self.unknown_0x4a996997,
            "unknown_0x9f9fa6f3": self.unknown_0x9f9fa6f3,
            "unknown_0x932fea01": self.unknown_0x932fea01,
            "unknown_0x165f0fa8": self.unknown_0x165f0fa8,
            "unknown_0x6bd6b11f": self.unknown_0x6bd6b11f,
            "unknown_0x42420f6e": self.unknown_0x42420f6e.to_json(),
            "flower_reticle_scale": self.flower_reticle_scale,
            "flower_reticle_color": self.flower_reticle_color.to_json(),
            "unknown_0xb090e147": self.unknown_0xb090e147,
            "unknown_0x4c73a43d": self.unknown_0x4c73a43d,
            "unknown_0x6543d31b": self.unknown_0x6543d31b,
            "unknown_0x8cd2d1ce": self.unknown_0x8cd2d1ce,
            "missile_bracket_color": self.missile_bracket_color.to_json(),
            "unknown_0x45910e5d": self.unknown_0x45910e5d,
            "unknown_0x07b30fa0": self.unknown_0x07b30fa0,
            "unknown_0x13ce8500": self.unknown_0x13ce8500.to_json(),
            "unknown_0x9829f256": self.unknown_0x9829f256.to_json(),
            "unknown_0x77a613b9": self.unknown_0x77a613b9.to_json(),
            "unknown_0xdfa81287": self.unknown_0xdfa81287.to_json(),
            "lock_on_confirm_reticle_color": self.lock_on_confirm_reticle_color.to_json(),
            "seeker_reticle_color": self.seeker_reticle_color.to_json(),
            "unknown_0x618d150a": self.unknown_0x618d150a,
            "unknown_0x209a2a8c": self.unknown_0x209a2a8c,
            "unknown_0xacb3f8f7": self.unknown_0xacb3f8f7,
            "unknown_0xeda4c771": self.unknown_0xeda4c771,
            "unknown_0xd3427574": self.unknown_0xd3427574,
            "unknown_0x92554af2": self.unknown_0x92554af2,
            "unknown_0x1e134e75": self.unknown_0x1e134e75,
            "unknown_0x5f0471f3": self.unknown_0x5f0471f3,
            "unknown_0xe90548ac": self.unknown_0xe90548ac,
            "unknown_0xa812772a": self.unknown_0xa812772a,
            "unknown_0x2d75c7be": self.unknown_0x2d75c7be,
            "unknown_0x6c62f838": self.unknown_0x6c62f838,
            "unknown_0xf98e6242": self.unknown_0xf98e6242,
            "unknown_0xb8995dc4": self.unknown_0xb8995dc4,
            "unknown_0x5009c614": self.unknown_0x5009c614,
            "unknown_0x111ef992": self.unknown_0x111ef992,
            "grapple_icon_scale": self.grapple_icon_scale,
            "grapple_icon_scale_inactive": self.grapple_icon_scale_inactive,
            "unknown_0x498d794a": self.unknown_0x498d794a,
            "unknown_0x089a46cc": self.unknown_0x089a46cc,
            "grapple_icon_color": self.grapple_icon_color.to_json(),
            "grapple_icon_color_inactive": self.grapple_icon_color_inactive.to_json(),
            "unknown_0x083b1cc8": self.unknown_0x083b1cc8.to_json(),
            "unknown_0x966982b1": self.unknown_0x966982b1,
            "unknown_0xf9799f5f": self.unknown_0xf9799f5f.to_json(),
            "unknown_0x9b980788": self.unknown_0x9b980788,
            "orbit_point_model_color": self.orbit_point_model_color.to_json(),
            "crosshairs_color": self.crosshairs_color.to_json(),
            "unknown_0x2ff52290": self.unknown_0x2ff52290,
            "unknown_0x8a548cc9": self.unknown_0x8a548cc9,
            "unknown_0x65d449e1": self.unknown_0x65d449e1.to_json(),
            "unknown_0x42c7fbe4": self.unknown_0x42c7fbe4,
            "unknown_0x13820c03": self.unknown_0x13820c03,
            "unknown_0x52953385": self.unknown_0x52953385,
            "x_ray_seeker_reticle_color": self.x_ray_seeker_reticle_color.to_json(),
            "unknown_0xdd8cf478": self.unknown_0xdd8cf478,
            "unknown_0xcbac6d52": self.unknown_0xcbac6d52,
            "unknown_0x980a75b6": self.unknown_0x980a75b6,
            "unknown_0xcd1e0e91": self.unknown_0xcd1e0e91,
            "unknown_0xce9cf241": self.unknown_0xce9cf241,
            "unknown_0xb6531e99": self.unknown_0xb6531e99,
            "unknown_0x77e5c6b5": self.unknown_0x77e5c6b5,
            "unknown_0xfef5668b": self.unknown_0xfef5668b,
            "health_color": self.health_color.to_json(),
            "power_vulnerability_indicator": self.power_vulnerability_indicator.to_json(),
            "light_vulnerability_indicator": self.light_vulnerability_indicator.to_json(),
            "dark_vulnerability_indicator": self.dark_vulnerability_indicator.to_json(),
            "annihilator_vulnerability_indicator": self.annihilator_vulnerability_indicator.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x5173932f(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_OuterBeamIcon:
    return TweakTargeting_OuterBeamIcon.from_stream(data, game, property_size)


def _decode_unknown_0x23ff4be4(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size)


def _decode_unknown_0x92e98613(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size)


def _decode_unknown_0x64833842(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size)


def _decode_unknown_0x8dfd6e3c(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size)


def _decode_charge_gauge(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_Charge_Gauge:
    return TweakTargeting_Charge_Gauge.from_stream(data, game, property_size)


def _decode_lock_fire(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_LockFire:
    return TweakTargeting_LockFire.from_stream(data, game, property_size)


def _decode_lock_dagger(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_LockDagger:
    return TweakTargeting_LockDagger.from_stream(data, game, property_size)


def _decode_scan(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_Scan:
    return TweakTargeting_Scan.from_stream(data, game, property_size)


def _decode_unknown_0x42420f6e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flower_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bracket_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x13ce8500(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x9829f256(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x77a613b9(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xdfa81287(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_lock_on_confirm_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_seeker_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grapple_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grapple_icon_color_inactive(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x083b1cc8(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xf9799f5f(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_point_model_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_crosshairs_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x65d449e1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_health_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_power_vulnerability_indicator(
    data: typing.BinaryIO, game: Game, property_size: int
) -> TweakTargeting_VulnerabilityIndicator:
    return TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)


def _decode_light_vulnerability_indicator(
    data: typing.BinaryIO, game: Game, property_size: int
) -> TweakTargeting_VulnerabilityIndicator:
    return TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)


def _decode_dark_vulnerability_indicator(
    data: typing.BinaryIO, game: Game, property_size: int
) -> TweakTargeting_VulnerabilityIndicator:
    return TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)


def _decode_annihilator_vulnerability_indicator(
    data: typing.BinaryIO, game: Game, property_size: int
) -> TweakTargeting_VulnerabilityIndicator:
    return TweakTargeting_VulnerabilityIndicator.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FDA1466: ("instance_name", _decode_instance_name),
    0x5173932F: ("unknown_0x5173932f", _decode_unknown_0x5173932f),
    0x23FF4BE4: ("unknown_0x23ff4be4", _decode_unknown_0x23ff4be4),
    0x92E98613: ("unknown_0x92e98613", _decode_unknown_0x92e98613),
    0x64833842: ("unknown_0x64833842", _decode_unknown_0x64833842),
    0x8DFD6E3C: ("unknown_0x8dfd6e3c", _decode_unknown_0x8dfd6e3c),
    0xBC5A41B2: ("charge_gauge", _decode_charge_gauge),
    0x00183589: ("lock_fire", _decode_lock_fire),
    0xD20ECC07: ("lock_dagger", _decode_lock_dagger),
    0x65EF9F2A: ("scan", _decode_scan),
    0xC3410560: ("unknown_0xc3410560", structs.decode_BIG_l),
    0x3EB13041: ("unknown_0x3eb13041", structs.decode_BIG_f),
    0x5E67CAB0: ("unknown_0x5e67cab0", structs.decode_BIG_f),
    0xE0CA98AC: ("unknown_0xe0ca98ac", structs.decode_BIG_f),
    0xC1E35ABB: ("lock_on_confirm_reticle_scale", structs.decode_BIG_f),
    0x9F8D62C1: ("unknown_0x9f8d62c1", structs.decode_BIG_f),
    0xFF5EEEB9: ("unknown_0xff5eeeb9", structs.decode_BIG_f),
    0x0D0B660D: ("unknown_0x0d0b660d", structs.decode_BIG_f),
    0x132DD09E: ("seeker_target_reticle_scale", structs.decode_BIG_f),
    0x03EFC783: ("unknown_0x03efc783", structs.decode_BIG_f),
    0xDCBD7BF8: ("unknown_0xdcbd7bf8", structs.decode_BIG_f),
    0x2ACD6B4B: ("unknown_0x2acd6b4b", structs.decode_BIG_f),
    0xB4C6C331: ("unknown_0xb4c6c331", structs.decode_BIG_f),
    0x27D02089: ("unknown_0x27d02089", structs.decode_BIG_f),
    0xAE89310E: ("unknown_0xae89310e", structs.decode_BIG_f),
    0xB27644DF: ("unknown_0xb27644df", structs.decode_BIG_f),
    0x21E2D1CC: ("unknown_0x21e2d1cc", structs.decode_BIG_f),
    0x8E3AFEF8: ("orbit_point_occluded_opacity", structs.decode_BIG_f),
    0x5C489CB5: ("unknown_0x5c489cb5", structs.decode_BIG_f),
    0xEF2C842E: ("orbit_point_z_offset", structs.decode_BIG_f),
    0x61A6A38E: ("unknown_0x61a6a38e", structs.decode_BIG_f),
    0xFBDF31F9: ("unknown_0xfbdf31f9", structs.decode_BIG_f),
    0xF76F7D0B: ("unknown_0xf76f7d0b", structs.decode_BIG_f),
    0x810B3A08: ("unknown_0x810b3a08", structs.decode_BIG_f),
    0x73FE1553: ("unknown_0x73fe1553", structs.decode_BIG_f),
    0xC8AEF6F2: ("unknown_0xc8aef6f2", structs.decode_BIG_f),
    0x69B1E76C: ("unknown_0x69b1e76c", structs.decode_BIG_f),
    0x8A0DFD23: ("unknown_0x8a0dfd23", structs.decode_BIG_f),
    0x8299E96E: ("unknown_0x8299e96e", structs.decode_BIG_f),
    0xA18A3F25: ("unknown_0xa18a3f25", structs.decode_BIG_f),
    0x23BE9BB2: ("unknown_0x23be9bb2", structs.decode_BIG_f),
    0x8D512B82: ("unknown_0x8d512b82", structs.decode_BIG_f),
    0x39F1698D: ("unknown_0x39f1698d", structs.decode_BIG_f),
    0xC768C1E9: ("unknown_0xc768c1e9", structs.decode_BIG_f),
    0x55C47B0E: ("unknown_0x55c47b0e", structs.decode_BIG_f),
    0xA009AEA2: ("unknown_0xa009aea2", structs.decode_BIG_f),
    0x38080BBF: ("unknown_0x38080bbf", structs.decode_BIG_f),
    0x71017DBE: ("unknown_0x71017dbe", structs.decode_BIG_f),
    0x4A996997: ("unknown_0x4a996997", structs.decode_BIG_f),
    0x9F9FA6F3: ("unknown_0x9f9fa6f3", structs.decode_BIG_f),
    0x932FEA01: ("unknown_0x932fea01", structs.decode_BIG_f),
    0x165F0FA8: ("unknown_0x165f0fa8", structs.decode_BIG_f),
    0x6BD6B11F: ("unknown_0x6bd6b11f", structs.decode_BIG_f),
    0x42420F6E: ("unknown_0x42420f6e", _decode_unknown_0x42420f6e),
    0xA63229F1: ("flower_reticle_scale", structs.decode_BIG_f),
    0xBDA45F1A: ("flower_reticle_color", _decode_flower_reticle_color),
    0xB090E147: ("unknown_0xb090e147", structs.decode_BIG_f),
    0x4C73A43D: ("unknown_0x4c73a43d", structs.decode_BIG_f),
    0x6543D31B: ("unknown_0x6543d31b", structs.decode_BIG_f),
    0x8CD2D1CE: ("unknown_0x8cd2d1ce", structs.decode_BIG_f),
    0xE42F6BE0: ("missile_bracket_color", _decode_missile_bracket_color),
    0x45910E5D: ("unknown_0x45910e5d", structs.decode_BIG_f),
    0x07B30FA0: ("unknown_0x07b30fa0", structs.decode_BIG_f),
    0x13CE8500: ("unknown_0x13ce8500", _decode_unknown_0x13ce8500),
    0x9829F256: ("unknown_0x9829f256", _decode_unknown_0x9829f256),
    0x77A613B9: ("unknown_0x77a613b9", _decode_unknown_0x77a613b9),
    0xDFA81287: ("unknown_0xdfa81287", _decode_unknown_0xdfa81287),
    0xDA752C50: ("lock_on_confirm_reticle_color", _decode_lock_on_confirm_reticle_color),
    0x7B544E14: ("seeker_reticle_color", _decode_seeker_reticle_color),
    0x618D150A: ("unknown_0x618d150a", structs.decode_BIG_f),
    0x209A2A8C: ("unknown_0x209a2a8c", structs.decode_BIG_f),
    0xACB3F8F7: ("unknown_0xacb3f8f7", structs.decode_BIG_f),
    0xEDA4C771: ("unknown_0xeda4c771", structs.decode_BIG_f),
    0xD3427574: ("unknown_0xd3427574", structs.decode_BIG_f),
    0x92554AF2: ("unknown_0x92554af2", structs.decode_BIG_f),
    0x1E134E75: ("unknown_0x1e134e75", structs.decode_BIG_f),
    0x5F0471F3: ("unknown_0x5f0471f3", structs.decode_BIG_f),
    0xE90548AC: ("unknown_0xe90548ac", structs.decode_BIG_f),
    0xA812772A: ("unknown_0xa812772a", structs.decode_BIG_f),
    0x2D75C7BE: ("unknown_0x2d75c7be", structs.decode_BIG_f),
    0x6C62F838: ("unknown_0x6c62f838", structs.decode_BIG_f),
    0xF98E6242: ("unknown_0xf98e6242", structs.decode_BIG_f),
    0xB8995DC4: ("unknown_0xb8995dc4", structs.decode_BIG_f),
    0x5009C614: ("unknown_0x5009c614", structs.decode_BIG_f),
    0x111EF992: ("unknown_0x111ef992", structs.decode_BIG_f),
    0xEC0FF888: ("grapple_icon_scale", structs.decode_BIG_f),
    0xF229E05E: ("grapple_icon_scale_inactive", structs.decode_BIG_f),
    0x498D794A: ("unknown_0x498d794a", structs.decode_BIG_f),
    0x089A46CC: ("unknown_0x089a46cc", structs.decode_BIG_f),
    0xF7998E63: ("grapple_icon_color", _decode_grapple_icon_color),
    0x3CE853E3: ("grapple_icon_color_inactive", _decode_grapple_icon_color_inactive),
    0x083B1CC8: ("unknown_0x083b1cc8", _decode_unknown_0x083b1cc8),
    0x966982B1: ("unknown_0x966982b1", structs.decode_BIG_f),
    0xF9799F5F: ("unknown_0xf9799f5f", _decode_unknown_0xf9799f5f),
    0x9B980788: ("unknown_0x9b980788", structs.decode_BIG_f),
    0x3523A47F: ("orbit_point_model_color", _decode_orbit_point_model_color),
    0x27358B4D: ("crosshairs_color", _decode_crosshairs_color),
    0x2FF52290: ("unknown_0x2ff52290", structs.decode_BIG_f),
    0x8A548CC9: ("unknown_0x8a548cc9", structs.decode_BIG_bool_),
    0x65D449E1: ("unknown_0x65d449e1", _decode_unknown_0x65d449e1),
    0x42C7FBE4: ("unknown_0x42c7fbe4", structs.decode_BIG_f),
    0x13820C03: ("unknown_0x13820c03", structs.decode_BIG_f),
    0x52953385: ("unknown_0x52953385", structs.decode_BIG_f),
    0x0CD8FE5D: ("x_ray_seeker_reticle_color", _decode_x_ray_seeker_reticle_color),
    0xDD8CF478: ("unknown_0xdd8cf478", structs.decode_BIG_f),
    0xCBAC6D52: ("unknown_0xcbac6d52", structs.decode_BIG_f),
    0x980A75B6: ("unknown_0x980a75b6", structs.decode_BIG_f),
    0xCD1E0E91: ("unknown_0xcd1e0e91", structs.decode_BIG_f),
    0xCE9CF241: ("unknown_0xce9cf241", structs.decode_BIG_f),
    0xB6531E99: ("unknown_0xb6531e99", structs.decode_BIG_f),
    0x77E5C6B5: ("unknown_0x77e5c6b5", structs.decode_BIG_f),
    0xFEF5668B: ("unknown_0xfef5668b", structs.decode_BIG_f),
    0x5CE2A16F: ("health_color", _decode_health_color),
    0x1E179603: ("power_vulnerability_indicator", _decode_power_vulnerability_indicator),
    0x2B70CEF8: ("light_vulnerability_indicator", _decode_light_vulnerability_indicator),
    0x946CEFDE: ("dark_vulnerability_indicator", _decode_dark_vulnerability_indicator),
    0x921C86E1: ("annihilator_vulnerability_indicator", _decode_annihilator_vulnerability_indicator),
}
