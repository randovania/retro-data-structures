# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.archetypes.ScannableParameters import ScannableParameters
from retro_data_structures.properties.corruption.archetypes.SeedBoss1HandData import SeedBoss1HandData
from retro_data_structures.properties.corruption.archetypes.SeedBoss1Shield import SeedBoss1Shield
from retro_data_structures.properties.corruption.archetypes.SeedBoss1Stage import SeedBoss1Stage
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct60 import UnknownStruct60
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SeedBoss1DataJson(typing_extensions.TypedDict):
        unknown_0xd3ad55b6: float
        foot_health: json_util.JsonObject
        foot_vulnerability: json_util.JsonObject
        left_foot: int
        left_knee: int
        left_thigh: int
        right_foot: int
        right_knee: int
        right_thigh: int
        cmdl_0x50edae7f: int
        cmdl_0x30969cfe: int
        cmdl_0xb25e271d: int
        cmdl_0x5d71b85c: int
        cmdl_0x3d0a8add: int
        cmdl_0x43223a97: int
        cmdl_0x9b76ad84: int
        cmdl_0xfb0d9f05: int
        cmdl_0x48ee50ad: int
        cmdl_0x85635b3b: int
        cmdl_0xe51869ba: int
        cmdl_0x5cea873f: int
        head_model: int
        jaw_model: int
        ice_model: int
        head_ice_model: int
        jaw_ice_model: int
        head_vulnerability: json_util.JsonObject
        head_frozen_time: float
        shockwave: json_util.JsonObject
        unknown_struct60: json_util.JsonObject
        beam_info: json_util.JsonObject
        beam_damage_info: json_util.JsonObject
        orb_slot_vulnerability: json_util.JsonObject
        foot_explosion: int
        foot_explosion_sound: int
        wpsc: int
        damage_info: json_util.JsonObject
        shock_wave_info: json_util.JsonObject
        launch_projectile_data_0x7c9c3b51: json_util.JsonObject
        hover_then_home_projectile_0x730fe427: json_util.JsonObject
        unknown_0x050924d3: json_util.JsonValue
        unknown_0x6414e848: float
        unknown_0x2a7a2da7: float
        launch_projectile_data_0x4392c34a: json_util.JsonObject
        hover_then_home_projectile_0x868e4192: json_util.JsonObject
        hand_projectile_size: json_util.JsonValue
        unknown_0x153c001b: float
        unknown_0x473b730b: float
        hand_projectile_damage_effect: int
        unknown_0x38786921: int
        charge_player_damage: json_util.JsonObject
        launch_projectile_data_0x50ae6e55: json_util.JsonObject
        hand_data: json_util.JsonObject
        unknown_0x3196b2e7: json_util.JsonValue
        unknown_0x77d3b386: json_util.JsonValue
        color_hyper_shockwave: json_util.JsonValue
        unknown_0x7ce5c47c: json_util.JsonValue
        color_hyper_quake: json_util.JsonValue
        color_energized: json_util.JsonValue
        min_taunt_time: float
        max_taunt_time: float
        seed_boss1_stage_0x45694db0: json_util.JsonObject
        seed_boss1_stage_0x338c748d: json_util.JsonObject
        seed_boss1_stage_0xa8ff9e59: json_util.JsonObject
        seed_boss1_stage_0xde4606f7: json_util.JsonObject
        shield_info: json_util.JsonObject
        foot_contact_damage: json_util.JsonObject
        unknown_0x64588114: float
        approach_player_distance: float
        approach_player_delay: float
        approach_player_time: float
        unknown_0xc2be328d: json_util.JsonObject
        scannable_parameters: json_util.JsonObject


@dataclasses.dataclass()
class SeedBoss1Data(BaseProperty):
    unknown_0xd3ad55b6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD3AD55B6, original_name="Unknown"),
        },
    )
    foot_health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xB33EB533,
                original_name="FootHealth",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    foot_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x26FA460B,
                original_name="FootVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    left_foot: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAD0DE5AC, original_name="LeftFoot"),
        },
    )
    left_knee: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFC128C15, original_name="LeftKnee"),
        },
    )
    left_thigh: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x299B8D33, original_name="LeftThigh"),
        },
    )
    right_foot: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA5BB98A6, original_name="RightFoot"),
        },
    )
    right_knee: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF4A4F11F, original_name="RightKnee"),
        },
    )
    right_thigh: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC946D250, original_name="RightThigh"),
        },
    )
    cmdl_0x50edae7f: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x50EDAE7F, original_name="CMDL"),
        },
    )
    cmdl_0x30969cfe: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x30969CFE, original_name="CMDL"),
        },
    )
    cmdl_0xb25e271d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB25E271D, original_name="CMDL"),
        },
    )
    cmdl_0x5d71b85c: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5D71B85C, original_name="CMDL"),
        },
    )
    cmdl_0x3d0a8add: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3D0A8ADD, original_name="CMDL"),
        },
    )
    cmdl_0x43223a97: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x43223A97, original_name="CMDL"),
        },
    )
    cmdl_0x9b76ad84: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9B76AD84, original_name="CMDL"),
        },
    )
    cmdl_0xfb0d9f05: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFB0D9F05, original_name="CMDL"),
        },
    )
    cmdl_0x48ee50ad: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x48EE50AD, original_name="CMDL"),
        },
    )
    cmdl_0x85635b3b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x85635B3B, original_name="CMDL"),
        },
    )
    cmdl_0xe51869ba: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE51869BA, original_name="CMDL"),
        },
    )
    cmdl_0x5cea873f: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5CEA873F, original_name="CMDL"),
        },
    )
    head_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC288AE69, original_name="HeadModel"),
        },
    )
    jaw_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCDBD44E1, original_name="JawModel"),
        },
    )
    ice_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6AD6CBBA, original_name="IceModel"),
        },
    )
    head_ice_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3AB79847, original_name="HeadIceModel"),
        },
    )
    jaw_ice_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x27B30D35, original_name="JawIceModel"),
        },
    )
    head_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xEC37E2FA,
                original_name="HeadVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    head_frozen_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCCCA3249, original_name="HeadFrozenTime"),
        },
    )
    shockwave: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x3CE6E482,
                original_name="Shockwave",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    unknown_struct60: UnknownStruct60 = dataclasses.field(
        default_factory=UnknownStruct60,
        metadata={
            "reflection": FieldReflection[UnknownStruct60](
                UnknownStruct60,
                id=0x72E00501,
                original_name="UnknownStruct60",
                from_json=UnknownStruct60.from_json,
                to_json=UnknownStruct60.to_json,
            ),
        },
    )
    beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x1598012A,
                original_name="BeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    beam_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x98821996,
                original_name="BeamDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    orb_slot_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xDD34C3C0,
                original_name="OrbSlotVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    foot_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x547B9A9A, original_name="FootExplosion"),
        },
    )
    foot_explosion_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEAF93057, original_name="FootExplosionSound"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x36C067C2, original_name="WPSC"),
        },
    )
    damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x261EEFE7,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x818F810B,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    launch_projectile_data_0x7c9c3b51: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x7C9C3B51,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    hover_then_home_projectile_0x730fe427: HoverThenHomeProjectile = dataclasses.field(
        default_factory=HoverThenHomeProjectile,
        metadata={
            "reflection": FieldReflection[HoverThenHomeProjectile](
                HoverThenHomeProjectile,
                id=0x730FE427,
                original_name="HoverThenHomeProjectile",
                from_json=HoverThenHomeProjectile.from_json,
                to_json=HoverThenHomeProjectile.to_json,
            ),
        },
    )
    unknown_0x050924d3: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x050924D3, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0x6414e848: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6414E848, original_name="Unknown"),
        },
    )
    unknown_0x2a7a2da7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A7A2DA7, original_name="Unknown"),
        },
    )
    launch_projectile_data_0x4392c34a: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x4392C34A,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    hover_then_home_projectile_0x868e4192: HoverThenHomeProjectile = dataclasses.field(
        default_factory=HoverThenHomeProjectile,
        metadata={
            "reflection": FieldReflection[HoverThenHomeProjectile](
                HoverThenHomeProjectile,
                id=0x868E4192,
                original_name="HoverThenHomeProjectile",
                from_json=HoverThenHomeProjectile.from_json,
                to_json=HoverThenHomeProjectile.to_json,
            ),
        },
    )
    hand_projectile_size: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xC8E16555,
                original_name="HandProjectileSize",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    unknown_0x153c001b: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x153C001B, original_name="Unknown"),
        },
    )
    unknown_0x473b730b: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x473B730B, original_name="Unknown"),
        },
    )
    hand_projectile_damage_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAEA60F24, original_name="HandProjectileDamageEffect"),
        },
    )
    unknown_0x38786921: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x38786921, original_name="Unknown"),
        },
    )
    charge_player_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x9E63065F,
                original_name="ChargePlayerDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    launch_projectile_data_0x50ae6e55: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x50AE6E55,
                original_name="LaunchProjectileData",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    hand_data: SeedBoss1HandData = dataclasses.field(
        default_factory=SeedBoss1HandData,
        metadata={
            "reflection": FieldReflection[SeedBoss1HandData](
                SeedBoss1HandData,
                id=0xC69F691A,
                original_name="HandData",
                from_json=SeedBoss1HandData.from_json,
                to_json=SeedBoss1HandData.to_json,
            ),
        },
    )
    unknown_0x3196b2e7: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x3196B2E7, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x77d3b386: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x77D3B386, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    color_hyper_shockwave: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xA9BE1081,
                original_name="ColorHyperShockwave",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x7ce5c47c: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x7CE5C47C, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    color_hyper_quake: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xF9656C39, original_name="ColorHyperQuake", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    color_energized: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD7142AFE, original_name="ColorEnergized", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    min_taunt_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3718EA0, original_name="MinTauntTime"),
        },
    )
    max_taunt_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD6FA5A52, original_name="MaxTauntTime"),
        },
    )
    seed_boss1_stage_0x45694db0: SeedBoss1Stage = dataclasses.field(
        default_factory=SeedBoss1Stage,
        metadata={
            "reflection": FieldReflection[SeedBoss1Stage](
                SeedBoss1Stage,
                id=0x45694DB0,
                original_name="SeedBoss1Stage",
                from_json=SeedBoss1Stage.from_json,
                to_json=SeedBoss1Stage.to_json,
            ),
        },
    )
    seed_boss1_stage_0x338c748d: SeedBoss1Stage = dataclasses.field(
        default_factory=SeedBoss1Stage,
        metadata={
            "reflection": FieldReflection[SeedBoss1Stage](
                SeedBoss1Stage,
                id=0x338C748D,
                original_name="SeedBoss1Stage",
                from_json=SeedBoss1Stage.from_json,
                to_json=SeedBoss1Stage.to_json,
            ),
        },
    )
    seed_boss1_stage_0xa8ff9e59: SeedBoss1Stage = dataclasses.field(
        default_factory=SeedBoss1Stage,
        metadata={
            "reflection": FieldReflection[SeedBoss1Stage](
                SeedBoss1Stage,
                id=0xA8FF9E59,
                original_name="SeedBoss1Stage",
                from_json=SeedBoss1Stage.from_json,
                to_json=SeedBoss1Stage.to_json,
            ),
        },
    )
    seed_boss1_stage_0xde4606f7: SeedBoss1Stage = dataclasses.field(
        default_factory=SeedBoss1Stage,
        metadata={
            "reflection": FieldReflection[SeedBoss1Stage](
                SeedBoss1Stage,
                id=0xDE4606F7,
                original_name="SeedBoss1Stage",
                from_json=SeedBoss1Stage.from_json,
                to_json=SeedBoss1Stage.to_json,
            ),
        },
    )
    shield_info: SeedBoss1Shield = dataclasses.field(
        default_factory=SeedBoss1Shield,
        metadata={
            "reflection": FieldReflection[SeedBoss1Shield](
                SeedBoss1Shield,
                id=0x2883F972,
                original_name="ShieldInfo",
                from_json=SeedBoss1Shield.from_json,
                to_json=SeedBoss1Shield.to_json,
            ),
        },
    )
    foot_contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x40AC1FD4,
                original_name="FootContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x64588114: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x64588114, original_name="Unknown"),
        },
    )
    approach_player_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x712D3274, original_name="ApproachPlayerDistance"),
        },
    )
    approach_player_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50EC86C1, original_name="ApproachPlayerDelay"),
        },
    )
    approach_player_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x536B7493, original_name="ApproachPlayerTime"),
        },
    )
    unknown_0xc2be328d: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xC2BE328D, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    scannable_parameters: ScannableParameters = dataclasses.field(
        default_factory=ScannableParameters,
        metadata={
            "reflection": FieldReflection[ScannableParameters](
                ScannableParameters,
                id=0x022FDCA5,
                original_name="ScannableParameters",
                from_json=ScannableParameters.from_json,
                to_json=ScannableParameters.to_json,
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
        if property_count != 73:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3AD55B6
        unknown_0xd3ad55b6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB33EB533
        foot_health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26FA460B
        foot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD0DE5AC
        left_foot = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC128C15
        left_knee = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x299B8D33
        left_thigh = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA5BB98A6
        right_foot = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4A4F11F
        right_knee = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC946D250
        right_thigh = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50EDAE7F
        cmdl_0x50edae7f = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30969CFE
        cmdl_0x30969cfe = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB25E271D
        cmdl_0xb25e271d = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D71B85C
        cmdl_0x5d71b85c = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D0A8ADD
        cmdl_0x3d0a8add = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43223A97
        cmdl_0x43223a97 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B76AD84
        cmdl_0x9b76ad84 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB0D9F05
        cmdl_0xfb0d9f05 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48EE50AD
        cmdl_0x48ee50ad = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85635B3B
        cmdl_0x85635b3b = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE51869BA
        cmdl_0xe51869ba = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5CEA873F
        cmdl_0x5cea873f = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC288AE69
        head_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCDBD44E1
        jaw_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6AD6CBBA
        ice_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AB79847
        head_ice_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27B30D35
        jaw_ice_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC37E2FA
        head_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCCA3249
        head_frozen_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3CE6E482
        shockwave = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72E00501
        unknown_struct60 = UnknownStruct60.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1598012A
        beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98821996
        beam_damage_info = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD34C3C0
        orb_slot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x547B9A9A
        foot_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEAF93057
        foot_explosion_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36C067C2
        wpsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x261EEFE7
        damage_info = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x818F810B
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C9C3B51
        launch_projectile_data_0x7c9c3b51 = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x730FE427
        hover_then_home_projectile_0x730fe427 = HoverThenHomeProjectile.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x050924D3
        unknown_0x050924d3 = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6414E848
        unknown_0x6414e848 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A7A2DA7
        unknown_0x2a7a2da7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4392C34A
        launch_projectile_data_0x4392c34a = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x868E4192
        hover_then_home_projectile_0x868e4192 = HoverThenHomeProjectile.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8E16555
        hand_projectile_size = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x153C001B
        unknown_0x153c001b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x473B730B
        unknown_0x473b730b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAEA60F24
        hand_projectile_damage_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38786921
        unknown_0x38786921 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9E63065F
        charge_player_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50AE6E55
        launch_projectile_data_0x50ae6e55 = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC69F691A
        hand_data = SeedBoss1HandData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3196B2E7
        unknown_0x3196b2e7 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77D3B386
        unknown_0x77d3b386 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9BE1081
        color_hyper_shockwave = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CE5C47C
        unknown_0x7ce5c47c = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9656C39
        color_hyper_quake = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD7142AFE
        color_energized = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3718EA0
        min_taunt_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6FA5A52
        max_taunt_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45694DB0
        seed_boss1_stage_0x45694db0 = SeedBoss1Stage.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x338C748D
        seed_boss1_stage_0x338c748d = SeedBoss1Stage.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8FF9E59
        seed_boss1_stage_0xa8ff9e59 = SeedBoss1Stage.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE4606F7
        seed_boss1_stage_0xde4606f7 = SeedBoss1Stage.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2883F972
        shield_info = SeedBoss1Shield.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40AC1FD4
        foot_contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64588114
        unknown_0x64588114 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x712D3274
        approach_player_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50EC86C1
        approach_player_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x536B7493
        approach_player_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2BE328D
        unknown_0xc2be328d = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x022FDCA5
        scannable_parameters = ScannableParameters.from_stream(data, game, property_size)

        return cls(
            unknown_0xd3ad55b6,
            foot_health,
            foot_vulnerability,
            left_foot,
            left_knee,
            left_thigh,
            right_foot,
            right_knee,
            right_thigh,
            cmdl_0x50edae7f,
            cmdl_0x30969cfe,
            cmdl_0xb25e271d,
            cmdl_0x5d71b85c,
            cmdl_0x3d0a8add,
            cmdl_0x43223a97,
            cmdl_0x9b76ad84,
            cmdl_0xfb0d9f05,
            cmdl_0x48ee50ad,
            cmdl_0x85635b3b,
            cmdl_0xe51869ba,
            cmdl_0x5cea873f,
            head_model,
            jaw_model,
            ice_model,
            head_ice_model,
            jaw_ice_model,
            head_vulnerability,
            head_frozen_time,
            shockwave,
            unknown_struct60,
            beam_info,
            beam_damage_info,
            orb_slot_vulnerability,
            foot_explosion,
            foot_explosion_sound,
            wpsc,
            damage_info,
            shock_wave_info,
            launch_projectile_data_0x7c9c3b51,
            hover_then_home_projectile_0x730fe427,
            unknown_0x050924d3,
            unknown_0x6414e848,
            unknown_0x2a7a2da7,
            launch_projectile_data_0x4392c34a,
            hover_then_home_projectile_0x868e4192,
            hand_projectile_size,
            unknown_0x153c001b,
            unknown_0x473b730b,
            hand_projectile_damage_effect,
            unknown_0x38786921,
            charge_player_damage,
            launch_projectile_data_0x50ae6e55,
            hand_data,
            unknown_0x3196b2e7,
            unknown_0x77d3b386,
            color_hyper_shockwave,
            unknown_0x7ce5c47c,
            color_hyper_quake,
            color_energized,
            min_taunt_time,
            max_taunt_time,
            seed_boss1_stage_0x45694db0,
            seed_boss1_stage_0x338c748d,
            seed_boss1_stage_0xa8ff9e59,
            seed_boss1_stage_0xde4606f7,
            shield_info,
            foot_contact_damage,
            unknown_0x64588114,
            approach_player_distance,
            approach_player_delay,
            approach_player_time,
            unknown_0xc2be328d,
            scannable_parameters,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00I")  # 73 properties

        data.write(b"\xd3\xadU\xb6")  # 0xd3ad55b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd3ad55b6))

        data.write(b"\xb3>\xb53")  # 0xb33eb533
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.foot_health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&\xfaF\x0b")  # 0x26fa460b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.foot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xad\r\xe5\xac")  # 0xad0de5ac
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_foot))

        data.write(b"\xfc\x12\x8c\x15")  # 0xfc128c15
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_knee))

        data.write(b")\x9b\x8d3")  # 0x299b8d33
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_thigh))

        data.write(b"\xa5\xbb\x98\xa6")  # 0xa5bb98a6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_foot))

        data.write(b"\xf4\xa4\xf1\x1f")  # 0xf4a4f11f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_knee))

        data.write(b"\xc9F\xd2P")  # 0xc946d250
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_thigh))

        data.write(b"P\xed\xae\x7f")  # 0x50edae7f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x50edae7f))

        data.write(b"0\x96\x9c\xfe")  # 0x30969cfe
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x30969cfe))

        data.write(b"\xb2^'\x1d")  # 0xb25e271d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xb25e271d))

        data.write(b"]q\xb8\\")  # 0x5d71b85c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x5d71b85c))

        data.write(b"=\n\x8a\xdd")  # 0x3d0a8add
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x3d0a8add))

        data.write(b'C":\x97')  # 0x43223a97
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x43223a97))

        data.write(b"\x9bv\xad\x84")  # 0x9b76ad84
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x9b76ad84))

        data.write(b"\xfb\r\x9f\x05")  # 0xfb0d9f05
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xfb0d9f05))

        data.write(b"H\xeeP\xad")  # 0x48ee50ad
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x48ee50ad))

        data.write(b"\x85c[;")  # 0x85635b3b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x85635b3b))

        data.write(b"\xe5\x18i\xba")  # 0xe51869ba
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xe51869ba))

        data.write(b"\\\xea\x87?")  # 0x5cea873f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x5cea873f))

        data.write(b"\xc2\x88\xaei")  # 0xc288ae69
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.head_model))

        data.write(b"\xcd\xbdD\xe1")  # 0xcdbd44e1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.jaw_model))

        data.write(b"j\xd6\xcb\xba")  # 0x6ad6cbba
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ice_model))

        data.write(b":\xb7\x98G")  # 0x3ab79847
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.head_ice_model))

        data.write(b"'\xb3\r5")  # 0x27b30d35
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.jaw_ice_model))

        data.write(b"\xec7\xe2\xfa")  # 0xec37e2fa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.head_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcc\xca2I")  # 0xccca3249
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.head_frozen_time))

        data.write(b"<\xe6\xe4\x82")  # 0x3ce6e482
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"r\xe0\x05\x01")  # 0x72e00501
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct60.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x15\x98\x01*")  # 0x1598012a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x98\x82\x19\x96")  # 0x98821996
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdd4\xc3\xc0")  # 0xdd34c3c0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orb_slot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"T{\x9a\x9a")  # 0x547b9a9a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.foot_explosion))

        data.write(b"\xea\xf90W")  # 0xeaf93057
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.foot_explosion_sound))

        data.write(b"6\xc0g\xc2")  # 0x36c067c2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc))

        data.write(b"&\x1e\xef\xe7")  # 0x261eefe7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81\x8f\x81\x0b")  # 0x818f810b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"|\x9c;Q")  # 0x7c9c3b51
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x7c9c3b51.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"s\x0f\xe4'")  # 0x730fe427
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hover_then_home_projectile_0x730fe427.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x05\t$\xd3")  # 0x50924d3
        data.write(b"\x00\x0c")  # size
        self.unknown_0x050924d3.to_stream(data, game)

        data.write(b"d\x14\xe8H")  # 0x6414e848
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6414e848))

        data.write(b"*z-\xa7")  # 0x2a7a2da7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2a7a2da7))

        data.write(b"C\x92\xc3J")  # 0x4392c34a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x4392c34a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x86\x8eA\x92")  # 0x868e4192
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hover_then_home_projectile_0x868e4192.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc8\xe1eU")  # 0xc8e16555
        data.write(b"\x00\x0c")  # size
        self.hand_projectile_size.to_stream(data, game)

        data.write(b"\x15<\x00\x1b")  # 0x153c001b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x153c001b))

        data.write(b"G;s\x0b")  # 0x473b730b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x473b730b))

        data.write(b"\xae\xa6\x0f$")  # 0xaea60f24
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.hand_projectile_damage_effect))

        data.write(b"8xi!")  # 0x38786921
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x38786921))

        data.write(b"\x9ec\x06_")  # 0x9e63065f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.charge_player_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"P\xaenU")  # 0x50ae6e55
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.launch_projectile_data_0x50ae6e55.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\x9fi\x1a")  # 0xc69f691a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hand_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"1\x96\xb2\xe7")  # 0x3196b2e7
        data.write(b"\x00\x10")  # size
        self.unknown_0x3196b2e7.to_stream(data, game)

        data.write(b"w\xd3\xb3\x86")  # 0x77d3b386
        data.write(b"\x00\x10")  # size
        self.unknown_0x77d3b386.to_stream(data, game)

        data.write(b"\xa9\xbe\x10\x81")  # 0xa9be1081
        data.write(b"\x00\x10")  # size
        self.color_hyper_shockwave.to_stream(data, game)

        data.write(b"|\xe5\xc4|")  # 0x7ce5c47c
        data.write(b"\x00\x10")  # size
        self.unknown_0x7ce5c47c.to_stream(data, game)

        data.write(b"\xf9el9")  # 0xf9656c39
        data.write(b"\x00\x10")  # size
        self.color_hyper_quake.to_stream(data, game)

        data.write(b"\xd7\x14*\xfe")  # 0xd7142afe
        data.write(b"\x00\x10")  # size
        self.color_energized.to_stream(data, game)

        data.write(b"\xc3q\x8e\xa0")  # 0xc3718ea0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_taunt_time))

        data.write(b"\xd6\xfaZR")  # 0xd6fa5a52
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_taunt_time))

        data.write(b"EiM\xb0")  # 0x45694db0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.seed_boss1_stage_0x45694db0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\x8ct\x8d")  # 0x338c748d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.seed_boss1_stage_0x338c748d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa8\xff\x9eY")  # 0xa8ff9e59
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.seed_boss1_stage_0xa8ff9e59.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdeF\x06\xf7")  # 0xde4606f7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.seed_boss1_stage_0xde4606f7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"(\x83\xf9r")  # 0x2883f972
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shield_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"@\xac\x1f\xd4")  # 0x40ac1fd4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.foot_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"dX\x81\x14")  # 0x64588114
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x64588114))

        data.write(b"q-2t")  # 0x712d3274
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.approach_player_distance))

        data.write(b"P\xec\x86\xc1")  # 0x50ec86c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.approach_player_delay))

        data.write(b"Skt\x93")  # 0x536b7493
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.approach_player_time))

        data.write(b"\xc2\xbe2\x8d")  # 0xc2be328d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xc2be328d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x02/\xdc\xa5")  # 0x22fdca5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.scannable_parameters.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss1DataJson", data)
        return cls(
            unknown_0xd3ad55b6=json_data["unknown_0xd3ad55b6"],
            foot_health=HealthInfo.from_json(json_data["foot_health"]),
            foot_vulnerability=DamageVulnerability.from_json(json_data["foot_vulnerability"]),
            left_foot=json_data["left_foot"],
            left_knee=json_data["left_knee"],
            left_thigh=json_data["left_thigh"],
            right_foot=json_data["right_foot"],
            right_knee=json_data["right_knee"],
            right_thigh=json_data["right_thigh"],
            cmdl_0x50edae7f=json_data["cmdl_0x50edae7f"],
            cmdl_0x30969cfe=json_data["cmdl_0x30969cfe"],
            cmdl_0xb25e271d=json_data["cmdl_0xb25e271d"],
            cmdl_0x5d71b85c=json_data["cmdl_0x5d71b85c"],
            cmdl_0x3d0a8add=json_data["cmdl_0x3d0a8add"],
            cmdl_0x43223a97=json_data["cmdl_0x43223a97"],
            cmdl_0x9b76ad84=json_data["cmdl_0x9b76ad84"],
            cmdl_0xfb0d9f05=json_data["cmdl_0xfb0d9f05"],
            cmdl_0x48ee50ad=json_data["cmdl_0x48ee50ad"],
            cmdl_0x85635b3b=json_data["cmdl_0x85635b3b"],
            cmdl_0xe51869ba=json_data["cmdl_0xe51869ba"],
            cmdl_0x5cea873f=json_data["cmdl_0x5cea873f"],
            head_model=json_data["head_model"],
            jaw_model=json_data["jaw_model"],
            ice_model=json_data["ice_model"],
            head_ice_model=json_data["head_ice_model"],
            jaw_ice_model=json_data["jaw_ice_model"],
            head_vulnerability=DamageVulnerability.from_json(json_data["head_vulnerability"]),
            head_frozen_time=json_data["head_frozen_time"],
            shockwave=ShockWaveInfo.from_json(json_data["shockwave"]),
            unknown_struct60=UnknownStruct60.from_json(json_data["unknown_struct60"]),
            beam_info=PlasmaBeamInfo.from_json(json_data["beam_info"]),
            beam_damage_info=DamageInfo.from_json(json_data["beam_damage_info"]),
            orb_slot_vulnerability=DamageVulnerability.from_json(json_data["orb_slot_vulnerability"]),
            foot_explosion=json_data["foot_explosion"],
            foot_explosion_sound=json_data["foot_explosion_sound"],
            wpsc=json_data["wpsc"],
            damage_info=DamageInfo.from_json(json_data["damage_info"]),
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            launch_projectile_data_0x7c9c3b51=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x7c9c3b51"]
            ),
            hover_then_home_projectile_0x730fe427=HoverThenHomeProjectile.from_json(
                json_data["hover_then_home_projectile_0x730fe427"]
            ),
            unknown_0x050924d3=Vector.from_json(json_data["unknown_0x050924d3"]),
            unknown_0x6414e848=json_data["unknown_0x6414e848"],
            unknown_0x2a7a2da7=json_data["unknown_0x2a7a2da7"],
            launch_projectile_data_0x4392c34a=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x4392c34a"]
            ),
            hover_then_home_projectile_0x868e4192=HoverThenHomeProjectile.from_json(
                json_data["hover_then_home_projectile_0x868e4192"]
            ),
            hand_projectile_size=Vector.from_json(json_data["hand_projectile_size"]),
            unknown_0x153c001b=json_data["unknown_0x153c001b"],
            unknown_0x473b730b=json_data["unknown_0x473b730b"],
            hand_projectile_damage_effect=json_data["hand_projectile_damage_effect"],
            unknown_0x38786921=json_data["unknown_0x38786921"],
            charge_player_damage=DamageInfo.from_json(json_data["charge_player_damage"]),
            launch_projectile_data_0x50ae6e55=LaunchProjectileData.from_json(
                json_data["launch_projectile_data_0x50ae6e55"]
            ),
            hand_data=SeedBoss1HandData.from_json(json_data["hand_data"]),
            unknown_0x3196b2e7=Color.from_json(json_data["unknown_0x3196b2e7"]),
            unknown_0x77d3b386=Color.from_json(json_data["unknown_0x77d3b386"]),
            color_hyper_shockwave=Color.from_json(json_data["color_hyper_shockwave"]),
            unknown_0x7ce5c47c=Color.from_json(json_data["unknown_0x7ce5c47c"]),
            color_hyper_quake=Color.from_json(json_data["color_hyper_quake"]),
            color_energized=Color.from_json(json_data["color_energized"]),
            min_taunt_time=json_data["min_taunt_time"],
            max_taunt_time=json_data["max_taunt_time"],
            seed_boss1_stage_0x45694db0=SeedBoss1Stage.from_json(json_data["seed_boss1_stage_0x45694db0"]),
            seed_boss1_stage_0x338c748d=SeedBoss1Stage.from_json(json_data["seed_boss1_stage_0x338c748d"]),
            seed_boss1_stage_0xa8ff9e59=SeedBoss1Stage.from_json(json_data["seed_boss1_stage_0xa8ff9e59"]),
            seed_boss1_stage_0xde4606f7=SeedBoss1Stage.from_json(json_data["seed_boss1_stage_0xde4606f7"]),
            shield_info=SeedBoss1Shield.from_json(json_data["shield_info"]),
            foot_contact_damage=DamageInfo.from_json(json_data["foot_contact_damage"]),
            unknown_0x64588114=json_data["unknown_0x64588114"],
            approach_player_distance=json_data["approach_player_distance"],
            approach_player_delay=json_data["approach_player_delay"],
            approach_player_time=json_data["approach_player_time"],
            unknown_0xc2be328d=Spline.from_json(json_data["unknown_0xc2be328d"]),
            scannable_parameters=ScannableParameters.from_json(json_data["scannable_parameters"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xd3ad55b6": self.unknown_0xd3ad55b6,
            "foot_health": self.foot_health.to_json(),
            "foot_vulnerability": self.foot_vulnerability.to_json(),
            "left_foot": self.left_foot,
            "left_knee": self.left_knee,
            "left_thigh": self.left_thigh,
            "right_foot": self.right_foot,
            "right_knee": self.right_knee,
            "right_thigh": self.right_thigh,
            "cmdl_0x50edae7f": self.cmdl_0x50edae7f,
            "cmdl_0x30969cfe": self.cmdl_0x30969cfe,
            "cmdl_0xb25e271d": self.cmdl_0xb25e271d,
            "cmdl_0x5d71b85c": self.cmdl_0x5d71b85c,
            "cmdl_0x3d0a8add": self.cmdl_0x3d0a8add,
            "cmdl_0x43223a97": self.cmdl_0x43223a97,
            "cmdl_0x9b76ad84": self.cmdl_0x9b76ad84,
            "cmdl_0xfb0d9f05": self.cmdl_0xfb0d9f05,
            "cmdl_0x48ee50ad": self.cmdl_0x48ee50ad,
            "cmdl_0x85635b3b": self.cmdl_0x85635b3b,
            "cmdl_0xe51869ba": self.cmdl_0xe51869ba,
            "cmdl_0x5cea873f": self.cmdl_0x5cea873f,
            "head_model": self.head_model,
            "jaw_model": self.jaw_model,
            "ice_model": self.ice_model,
            "head_ice_model": self.head_ice_model,
            "jaw_ice_model": self.jaw_ice_model,
            "head_vulnerability": self.head_vulnerability.to_json(),
            "head_frozen_time": self.head_frozen_time,
            "shockwave": self.shockwave.to_json(),
            "unknown_struct60": self.unknown_struct60.to_json(),
            "beam_info": self.beam_info.to_json(),
            "beam_damage_info": self.beam_damage_info.to_json(),
            "orb_slot_vulnerability": self.orb_slot_vulnerability.to_json(),
            "foot_explosion": self.foot_explosion,
            "foot_explosion_sound": self.foot_explosion_sound,
            "wpsc": self.wpsc,
            "damage_info": self.damage_info.to_json(),
            "shock_wave_info": self.shock_wave_info.to_json(),
            "launch_projectile_data_0x7c9c3b51": self.launch_projectile_data_0x7c9c3b51.to_json(),
            "hover_then_home_projectile_0x730fe427": self.hover_then_home_projectile_0x730fe427.to_json(),
            "unknown_0x050924d3": self.unknown_0x050924d3.to_json(),
            "unknown_0x6414e848": self.unknown_0x6414e848,
            "unknown_0x2a7a2da7": self.unknown_0x2a7a2da7,
            "launch_projectile_data_0x4392c34a": self.launch_projectile_data_0x4392c34a.to_json(),
            "hover_then_home_projectile_0x868e4192": self.hover_then_home_projectile_0x868e4192.to_json(),
            "hand_projectile_size": self.hand_projectile_size.to_json(),
            "unknown_0x153c001b": self.unknown_0x153c001b,
            "unknown_0x473b730b": self.unknown_0x473b730b,
            "hand_projectile_damage_effect": self.hand_projectile_damage_effect,
            "unknown_0x38786921": self.unknown_0x38786921,
            "charge_player_damage": self.charge_player_damage.to_json(),
            "launch_projectile_data_0x50ae6e55": self.launch_projectile_data_0x50ae6e55.to_json(),
            "hand_data": self.hand_data.to_json(),
            "unknown_0x3196b2e7": self.unknown_0x3196b2e7.to_json(),
            "unknown_0x77d3b386": self.unknown_0x77d3b386.to_json(),
            "color_hyper_shockwave": self.color_hyper_shockwave.to_json(),
            "unknown_0x7ce5c47c": self.unknown_0x7ce5c47c.to_json(),
            "color_hyper_quake": self.color_hyper_quake.to_json(),
            "color_energized": self.color_energized.to_json(),
            "min_taunt_time": self.min_taunt_time,
            "max_taunt_time": self.max_taunt_time,
            "seed_boss1_stage_0x45694db0": self.seed_boss1_stage_0x45694db0.to_json(),
            "seed_boss1_stage_0x338c748d": self.seed_boss1_stage_0x338c748d.to_json(),
            "seed_boss1_stage_0xa8ff9e59": self.seed_boss1_stage_0xa8ff9e59.to_json(),
            "seed_boss1_stage_0xde4606f7": self.seed_boss1_stage_0xde4606f7.to_json(),
            "shield_info": self.shield_info.to_json(),
            "foot_contact_damage": self.foot_contact_damage.to_json(),
            "unknown_0x64588114": self.unknown_0x64588114,
            "approach_player_distance": self.approach_player_distance,
            "approach_player_delay": self.approach_player_delay,
            "approach_player_time": self.approach_player_time,
            "unknown_0xc2be328d": self.unknown_0xc2be328d.to_json(),
            "scannable_parameters": self.scannable_parameters.to_json(),
        }


def _decode_foot_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_foot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_head_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_unknown_struct60(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct60:
    return UnknownStruct60.from_stream(data, game, property_size)


def _decode_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_beam_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_orb_slot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x7c9c3b51(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hover_then_home_projectile_0x730fe427(
    data: typing.BinaryIO, game: Game, property_size: int
) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_unknown_0x050924d3(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x4392c34a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hover_then_home_projectile_0x868e4192(
    data: typing.BinaryIO, game: Game, property_size: int
) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_hand_projectile_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_charge_player_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_launch_projectile_data_0x50ae6e55(
    data: typing.BinaryIO, game: Game, property_size: int
) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hand_data(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1HandData:
    return SeedBoss1HandData.from_stream(data, game, property_size)


def _decode_unknown_0x3196b2e7(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x77d3b386(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_hyper_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x7ce5c47c(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_hyper_quake(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_energized(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_seed_boss1_stage_0x45694db0(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_seed_boss1_stage_0x338c748d(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_seed_boss1_stage_0xa8ff9e59(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_seed_boss1_stage_0xde4606f7(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_shield_info(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Shield:
    return SeedBoss1Shield.from_stream(data, game, property_size)


def _decode_foot_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_unknown_0xc2be328d(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_scannable_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> ScannableParameters:
    return ScannableParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD3AD55B6: ("unknown_0xd3ad55b6", structs.decode_BIG_f),
    0xB33EB533: ("foot_health", _decode_foot_health),
    0x26FA460B: ("foot_vulnerability", _decode_foot_vulnerability),
    0xAD0DE5AC: ("left_foot", structs.decode_BIG_Q),
    0xFC128C15: ("left_knee", structs.decode_BIG_Q),
    0x299B8D33: ("left_thigh", structs.decode_BIG_Q),
    0xA5BB98A6: ("right_foot", structs.decode_BIG_Q),
    0xF4A4F11F: ("right_knee", structs.decode_BIG_Q),
    0xC946D250: ("right_thigh", structs.decode_BIG_Q),
    0x50EDAE7F: ("cmdl_0x50edae7f", structs.decode_BIG_Q),
    0x30969CFE: ("cmdl_0x30969cfe", structs.decode_BIG_Q),
    0xB25E271D: ("cmdl_0xb25e271d", structs.decode_BIG_Q),
    0x5D71B85C: ("cmdl_0x5d71b85c", structs.decode_BIG_Q),
    0x3D0A8ADD: ("cmdl_0x3d0a8add", structs.decode_BIG_Q),
    0x43223A97: ("cmdl_0x43223a97", structs.decode_BIG_Q),
    0x9B76AD84: ("cmdl_0x9b76ad84", structs.decode_BIG_Q),
    0xFB0D9F05: ("cmdl_0xfb0d9f05", structs.decode_BIG_Q),
    0x48EE50AD: ("cmdl_0x48ee50ad", structs.decode_BIG_Q),
    0x85635B3B: ("cmdl_0x85635b3b", structs.decode_BIG_Q),
    0xE51869BA: ("cmdl_0xe51869ba", structs.decode_BIG_Q),
    0x5CEA873F: ("cmdl_0x5cea873f", structs.decode_BIG_Q),
    0xC288AE69: ("head_model", structs.decode_BIG_Q),
    0xCDBD44E1: ("jaw_model", structs.decode_BIG_Q),
    0x6AD6CBBA: ("ice_model", structs.decode_BIG_Q),
    0x3AB79847: ("head_ice_model", structs.decode_BIG_Q),
    0x27B30D35: ("jaw_ice_model", structs.decode_BIG_Q),
    0xEC37E2FA: ("head_vulnerability", _decode_head_vulnerability),
    0xCCCA3249: ("head_frozen_time", structs.decode_BIG_f),
    0x3CE6E482: ("shockwave", _decode_shockwave),
    0x72E00501: ("unknown_struct60", _decode_unknown_struct60),
    0x1598012A: ("beam_info", _decode_beam_info),
    0x98821996: ("beam_damage_info", _decode_beam_damage_info),
    0xDD34C3C0: ("orb_slot_vulnerability", _decode_orb_slot_vulnerability),
    0x547B9A9A: ("foot_explosion", structs.decode_BIG_Q),
    0xEAF93057: ("foot_explosion_sound", structs.decode_BIG_Q),
    0x36C067C2: ("wpsc", structs.decode_BIG_Q),
    0x261EEFE7: ("damage_info", _decode_damage_info),
    0x818F810B: ("shock_wave_info", _decode_shock_wave_info),
    0x7C9C3B51: ("launch_projectile_data_0x7c9c3b51", _decode_launch_projectile_data_0x7c9c3b51),
    0x730FE427: ("hover_then_home_projectile_0x730fe427", _decode_hover_then_home_projectile_0x730fe427),
    0x050924D3: ("unknown_0x050924d3", _decode_unknown_0x050924d3),
    0x6414E848: ("unknown_0x6414e848", structs.decode_BIG_f),
    0x2A7A2DA7: ("unknown_0x2a7a2da7", structs.decode_BIG_f),
    0x4392C34A: ("launch_projectile_data_0x4392c34a", _decode_launch_projectile_data_0x4392c34a),
    0x868E4192: ("hover_then_home_projectile_0x868e4192", _decode_hover_then_home_projectile_0x868e4192),
    0xC8E16555: ("hand_projectile_size", _decode_hand_projectile_size),
    0x153C001B: ("unknown_0x153c001b", structs.decode_BIG_f),
    0x473B730B: ("unknown_0x473b730b", structs.decode_BIG_f),
    0xAEA60F24: ("hand_projectile_damage_effect", structs.decode_BIG_Q),
    0x38786921: ("unknown_0x38786921", structs.decode_BIG_Q),
    0x9E63065F: ("charge_player_damage", _decode_charge_player_damage),
    0x50AE6E55: ("launch_projectile_data_0x50ae6e55", _decode_launch_projectile_data_0x50ae6e55),
    0xC69F691A: ("hand_data", _decode_hand_data),
    0x3196B2E7: ("unknown_0x3196b2e7", _decode_unknown_0x3196b2e7),
    0x77D3B386: ("unknown_0x77d3b386", _decode_unknown_0x77d3b386),
    0xA9BE1081: ("color_hyper_shockwave", _decode_color_hyper_shockwave),
    0x7CE5C47C: ("unknown_0x7ce5c47c", _decode_unknown_0x7ce5c47c),
    0xF9656C39: ("color_hyper_quake", _decode_color_hyper_quake),
    0xD7142AFE: ("color_energized", _decode_color_energized),
    0xC3718EA0: ("min_taunt_time", structs.decode_BIG_f),
    0xD6FA5A52: ("max_taunt_time", structs.decode_BIG_f),
    0x45694DB0: ("seed_boss1_stage_0x45694db0", _decode_seed_boss1_stage_0x45694db0),
    0x338C748D: ("seed_boss1_stage_0x338c748d", _decode_seed_boss1_stage_0x338c748d),
    0xA8FF9E59: ("seed_boss1_stage_0xa8ff9e59", _decode_seed_boss1_stage_0xa8ff9e59),
    0xDE4606F7: ("seed_boss1_stage_0xde4606f7", _decode_seed_boss1_stage_0xde4606f7),
    0x2883F972: ("shield_info", _decode_shield_info),
    0x40AC1FD4: ("foot_contact_damage", _decode_foot_contact_damage),
    0x64588114: ("unknown_0x64588114", structs.decode_BIG_f),
    0x712D3274: ("approach_player_distance", structs.decode_BIG_f),
    0x50EC86C1: ("approach_player_delay", structs.decode_BIG_f),
    0x536B7493: ("approach_player_time", structs.decode_BIG_f),
    0xC2BE328D: ("unknown_0xc2be328d", _decode_unknown_0xc2be328d),
    0x022FDCA5: ("scannable_parameters", _decode_scannable_parameters),
}
