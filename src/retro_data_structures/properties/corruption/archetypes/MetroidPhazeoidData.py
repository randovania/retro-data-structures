# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ElectricBeamInfo import ElectricBeamInfo
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.archetypes.MetroidPhazeoidStruct import MetroidPhazeoidStruct
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MetroidPhazeoidDataJson(typing_extensions.TypedDict):
        disable_player_grab: bool
        disable_pirate_grab: bool
        disable_hungry_mode: bool
        post_hatch_scale: float
        unknown_0xef6d8c96: float
        unknown_0x763e71ae: float
        recheck_path_time: float
        recheck_path_distance: float
        scan_delay: float
        patrol: json_util.JsonObject
        attack: json_util.JsonObject
        hungry: json_util.JsonObject
        flyer_movement_mode_0x7b6c604a: json_util.JsonObject
        flyer_movement_mode_0x292754af: json_util.JsonObject
        ball_lift: json_util.JsonObject
        initial_vulnerability: json_util.JsonObject
        hungry_vulnerability: json_util.JsonObject
        ball_lift_vulnerability: json_util.JsonObject
        phase_out_vulnerability: json_util.JsonObject
        phase_out_radius_missile: float
        metroid_phazeoid_struct_0x7c187bd0: json_util.JsonObject
        metroid_phazeoid_struct_0x0c7b243d: json_util.JsonObject
        metroid_phazeoid_struct_0x33b1809f: json_util.JsonObject
        metroid_phazeoid_struct_0x0ec6856a: json_util.JsonObject
        metroid_phazeoid_struct_0x61fab47a: json_util.JsonObject
        metroid_phazeoid_struct_0x26aac761: json_util.JsonObject
        brain_vulnerability: json_util.JsonObject
        x_ray_brain_radius: float
        normal_brain_radius: float
        phase_out_time_min: float
        phase_out_time_max: float
        phase_in_time_min: float
        phase_in_time_max: float
        phase_temple_disable_time_max: float
        phase_temple_disable_time_min: float
        unknown_0xa77f2fe5: float
        unknown_0x411f8004: float
        unknown_0xd14fc373: float
        unknown_0x372f6c92: float
        ball_lift_slope_padding: float
        unknown_0x900a62f6: float
        arc_range_min: float
        arc_range_max: float
        unknown_0x9aab0b9a: float
        unknown_0x7ccba47b: float
        arc_attack: json_util.JsonObject
        unknown_0x0a8b169f: float
        unknown_0xecebb97e: float
        unknown_0x2b53dc0d: float
        energy_drain: json_util.JsonObject
        unknown_0x3af75fcc: float
        max_static_intensity: float
        ball_lift_delay_min: float
        ball_lift_delay_max: float
        unknown_0x283f2238: float
        unknown_0xce5f8dd9: float
        unknown_0x638d46ce: float
        unknown_0x85ede92f: float
        hungry_damage_threshold: float
        unknown_0x677e48ea: bool
        unknown_0x7edf931d: bool
        unknown_0x15283674: bool
        unknown_0x1ae10f78: float
        unknown_0x93f9240c: float
        phase_out_says_actions: float
        max_says_actions: float
        arc_effect: int
        arc_explosion: int
        sound_arc_explosion: int
        arc_number: int
        arc_length: float
        arc_move_time_max: float
        arc_move_time_min: float
        arc_on_time_max: float
        arc_on_time_min: float
        unknown_0x6dc77716: float
        unknown_0x6fc4508c: float
        unknown_0x7de8da8d: float
        unknown_0xf67dbaab: float
        blur_radius: float
        blur_duration: float


@dataclasses.dataclass()
class MetroidPhazeoidData(BaseProperty):
    disable_player_grab: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x74288EF3, original_name="DisablePlayerGrab"),
        },
    )
    disable_pirate_grab: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0679E20C, original_name="DisablePirateGrab"),
        },
    )
    disable_hungry_mode: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAE46D80E, original_name="DisableHungryMode"),
        },
    )
    post_hatch_scale: float = dataclasses.field(
        default=0.6600000262260437,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBD62D02E, original_name="PostHatchScale"),
        },
    )
    unknown_0xef6d8c96: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEF6D8C96, original_name="Unknown"),
        },
    )
    unknown_0x763e71ae: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x763E71AE, original_name="Unknown"),
        },
    )
    recheck_path_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9AA90B6B, original_name="RecheckPathTime"),
        },
    )
    recheck_path_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7626EC89, original_name="RecheckPathDistance"),
        },
    )
    scan_delay: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FC827A2, original_name="ScanDelay"),
        },
    )
    patrol: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xCCDD3ACA,
                original_name="Patrol",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    attack: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xFA2A173F,
                original_name="Attack",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    hungry: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x97EED1F6,
                original_name="Hungry",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0x7b6c604a: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x7B6C604A,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0x292754af: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x292754AF,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    ball_lift: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x18B5143A,
                original_name="BallLift",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    initial_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xEDD0D40D,
                original_name="InitialVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    hungry_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x8D7E81D6,
                original_name="HungryVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    ball_lift_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xF68EADC9,
                original_name="BallLiftVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    phase_out_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xDC020DA7,
                original_name="PhaseOutVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    phase_out_radius_missile: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA438A3CD, original_name="PhaseOutRadiusMissile"),
        },
    )
    metroid_phazeoid_struct_0x7c187bd0: MetroidPhazeoidStruct = dataclasses.field(
        default_factory=MetroidPhazeoidStruct,
        metadata={
            "reflection": FieldReflection[MetroidPhazeoidStruct](
                MetroidPhazeoidStruct,
                id=0x7C187BD0,
                original_name="MetroidPhazeoidStruct",
                from_json=MetroidPhazeoidStruct.from_json,
                to_json=MetroidPhazeoidStruct.to_json,
            ),
        },
    )
    metroid_phazeoid_struct_0x0c7b243d: MetroidPhazeoidStruct = dataclasses.field(
        default_factory=MetroidPhazeoidStruct,
        metadata={
            "reflection": FieldReflection[MetroidPhazeoidStruct](
                MetroidPhazeoidStruct,
                id=0x0C7B243D,
                original_name="MetroidPhazeoidStruct",
                from_json=MetroidPhazeoidStruct.from_json,
                to_json=MetroidPhazeoidStruct.to_json,
            ),
        },
    )
    metroid_phazeoid_struct_0x33b1809f: MetroidPhazeoidStruct = dataclasses.field(
        default_factory=MetroidPhazeoidStruct,
        metadata={
            "reflection": FieldReflection[MetroidPhazeoidStruct](
                MetroidPhazeoidStruct,
                id=0x33B1809F,
                original_name="MetroidPhazeoidStruct",
                from_json=MetroidPhazeoidStruct.from_json,
                to_json=MetroidPhazeoidStruct.to_json,
            ),
        },
    )
    metroid_phazeoid_struct_0x0ec6856a: MetroidPhazeoidStruct = dataclasses.field(
        default_factory=MetroidPhazeoidStruct,
        metadata={
            "reflection": FieldReflection[MetroidPhazeoidStruct](
                MetroidPhazeoidStruct,
                id=0x0EC6856A,
                original_name="MetroidPhazeoidStruct",
                from_json=MetroidPhazeoidStruct.from_json,
                to_json=MetroidPhazeoidStruct.to_json,
            ),
        },
    )
    metroid_phazeoid_struct_0x61fab47a: MetroidPhazeoidStruct = dataclasses.field(
        default_factory=MetroidPhazeoidStruct,
        metadata={
            "reflection": FieldReflection[MetroidPhazeoidStruct](
                MetroidPhazeoidStruct,
                id=0x61FAB47A,
                original_name="MetroidPhazeoidStruct",
                from_json=MetroidPhazeoidStruct.from_json,
                to_json=MetroidPhazeoidStruct.to_json,
            ),
        },
    )
    metroid_phazeoid_struct_0x26aac761: MetroidPhazeoidStruct = dataclasses.field(
        default_factory=MetroidPhazeoidStruct,
        metadata={
            "reflection": FieldReflection[MetroidPhazeoidStruct](
                MetroidPhazeoidStruct,
                id=0x26AAC761,
                original_name="MetroidPhazeoidStruct",
                from_json=MetroidPhazeoidStruct.from_json,
                to_json=MetroidPhazeoidStruct.to_json,
            ),
        },
    )
    brain_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x243AB10D,
                original_name="BrainVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    x_ray_brain_radius: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DC4AC9C, original_name="XRayBrainRadius"),
        },
    )
    normal_brain_radius: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7CB760A5, original_name="NormalBrainRadius"),
        },
    )
    phase_out_time_min: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x06A2BBB8, original_name="PhaseOutTimeMin"),
        },
    )
    phase_out_time_max: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE0C21459, original_name="PhaseOutTimeMax"),
        },
    )
    phase_in_time_min: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x544FA232, original_name="PhaseInTimeMin"),
        },
    )
    phase_in_time_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB22F0DD3, original_name="PhaseInTimeMax"),
        },
    )
    phase_temple_disable_time_max: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xACDACC80, original_name="PhaseTempleDisableTimeMax"),
        },
    )
    phase_temple_disable_time_min: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4ABA6361, original_name="PhaseTempleDisableTimeMin"),
        },
    )
    unknown_0xa77f2fe5: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA77F2FE5, original_name="Unknown"),
        },
    )
    unknown_0x411f8004: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x411F8004, original_name="Unknown"),
        },
    )
    unknown_0xd14fc373: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD14FC373, original_name="Unknown"),
        },
    )
    unknown_0x372f6c92: float = dataclasses.field(
        default=-50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x372F6C92, original_name="Unknown"),
        },
    )
    ball_lift_slope_padding: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF67D89B1, original_name="BallLiftSlopePadding"),
        },
    )
    unknown_0x900a62f6: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x900A62F6, original_name="Unknown"),
        },
    )
    arc_range_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1B7CF27, original_name="ArcRangeMin"),
        },
    )
    arc_range_max: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47D760C6, original_name="ArcRangeMax"),
        },
    )
    unknown_0x9aab0b9a: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9AAB0B9A, original_name="Unknown"),
        },
    )
    unknown_0x7ccba47b: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7CCBA47B, original_name="Unknown"),
        },
    )
    arc_attack: ElectricBeamInfo = dataclasses.field(
        default_factory=ElectricBeamInfo,
        metadata={
            "reflection": FieldReflection[ElectricBeamInfo](
                ElectricBeamInfo,
                id=0x6D417F4C,
                original_name="ArcAttack",
                from_json=ElectricBeamInfo.from_json,
                to_json=ElectricBeamInfo.to_json,
            ),
        },
    )
    unknown_0x0a8b169f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A8B169F, original_name="Unknown"),
        },
    )
    unknown_0xecebb97e: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xECEBB97E, original_name="Unknown"),
        },
    )
    unknown_0x2b53dc0d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B53DC0D, original_name="Unknown"),
        },
    )
    energy_drain: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x79CCC5B8, original_name="EnergyDrain", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x3af75fcc: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3AF75FCC, original_name="Unknown"),
        },
    )
    max_static_intensity: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7B4922A, original_name="MaxStaticIntensity"),
        },
    )
    ball_lift_delay_min: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4F4842A3, original_name="BallLiftDelayMin"),
        },
    )
    ball_lift_delay_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA928ED42, original_name="BallLiftDelayMax"),
        },
    )
    unknown_0x283f2238: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x283F2238, original_name="Unknown"),
        },
    )
    unknown_0xce5f8dd9: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCE5F8DD9, original_name="Unknown"),
        },
    )
    unknown_0x638d46ce: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x638D46CE, original_name="Unknown"),
        },
    )
    unknown_0x85ede92f: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x85EDE92F, original_name="Unknown"),
        },
    )
    hungry_damage_threshold: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x62FB47A5, original_name="HungryDamageThreshold"),
        },
    )
    unknown_0x677e48ea: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x677E48EA, original_name="Unknown"),
        },
    )
    unknown_0x7edf931d: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7EDF931D, original_name="Unknown"),
        },
    )
    unknown_0x15283674: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x15283674, original_name="Unknown"),
        },
    )
    unknown_0x1ae10f78: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AE10F78, original_name="Unknown"),
        },
    )
    unknown_0x93f9240c: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x93F9240C, original_name="Unknown"),
        },
    )
    phase_out_says_actions: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50B079ED, original_name="PhaseOutSaysActions"),
        },
    )
    max_says_actions: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB15B41FA, original_name="MaxSaysActions"),
        },
    )
    arc_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5562C40D, original_name="ArcEffect"),
        },
    )
    arc_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x11F74E71, original_name="ArcExplosion"),
        },
    )
    sound_arc_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3509CDD9, original_name="Sound_ArcExplosion"),
        },
    )
    arc_number: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x953BC1D2, original_name="ArcNumber"),
        },
    )
    arc_length: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x21828087, original_name="ArcLength"),
        },
    )
    arc_move_time_max: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x328B3E6E, original_name="ArcMoveTimeMax"),
        },
    )
    arc_move_time_min: float = dataclasses.field(
        default=0.020999999716877937,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4EB918F, original_name="ArcMoveTimeMin"),
        },
    )
    arc_on_time_max: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x55EBB850, original_name="ArcOnTimeMax"),
        },
    )
    arc_on_time_min: float = dataclasses.field(
        default=0.020999999716877937,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB38B17B1, original_name="ArcOnTimeMin"),
        },
    )
    unknown_0x6dc77716: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6DC77716, original_name="Unknown"),
        },
    )
    unknown_0x6fc4508c: float = dataclasses.field(
        default=-3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6FC4508C, original_name="Unknown"),
        },
    )
    unknown_0x7de8da8d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7DE8DA8D, original_name="Unknown"),
        },
    )
    unknown_0xf67dbaab: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF67DBAAB, original_name="Unknown"),
        },
    )
    blur_radius: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6F6EB1F4, original_name="BlurRadius"),
        },
    )
    blur_duration: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6409EDB3, original_name="BlurDuration"),
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
        if property_count != 81:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74288EF3
        disable_player_grab = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0679E20C
        disable_pirate_grab = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE46D80E
        disable_hungry_mode = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD62D02E
        post_hatch_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF6D8C96
        unknown_0xef6d8c96 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x763E71AE
        unknown_0x763e71ae = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AA90B6B
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626EC89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FC827A2
        scan_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCDD3ACA
        patrol = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFA2A173F
        attack = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97EED1F6
        hungry = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B6C604A
        flyer_movement_mode_0x7b6c604a = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x292754AF
        flyer_movement_mode_0x292754af = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18B5143A
        ball_lift = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDD0D40D
        initial_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D7E81D6
        hungry_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF68EADC9
        ball_lift_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC020DA7
        phase_out_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA438A3CD
        phase_out_radius_missile = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C187BD0
        metroid_phazeoid_struct_0x7c187bd0 = MetroidPhazeoidStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C7B243D
        metroid_phazeoid_struct_0x0c7b243d = MetroidPhazeoidStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33B1809F
        metroid_phazeoid_struct_0x33b1809f = MetroidPhazeoidStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0EC6856A
        metroid_phazeoid_struct_0x0ec6856a = MetroidPhazeoidStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61FAB47A
        metroid_phazeoid_struct_0x61fab47a = MetroidPhazeoidStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26AAC761
        metroid_phazeoid_struct_0x26aac761 = MetroidPhazeoidStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x243AB10D
        brain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DC4AC9C
        x_ray_brain_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CB760A5
        normal_brain_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06A2BBB8
        phase_out_time_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0C21459
        phase_out_time_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x544FA232
        phase_in_time_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB22F0DD3
        phase_in_time_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACDACC80
        phase_temple_disable_time_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ABA6361
        phase_temple_disable_time_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA77F2FE5
        unknown_0xa77f2fe5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x411F8004
        unknown_0x411f8004 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD14FC373
        unknown_0xd14fc373 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x372F6C92
        unknown_0x372f6c92 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF67D89B1
        ball_lift_slope_padding = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x900A62F6
        unknown_0x900a62f6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1B7CF27
        arc_range_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47D760C6
        arc_range_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AAB0B9A
        unknown_0x9aab0b9a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CCBA47B
        unknown_0x7ccba47b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D417F4C
        arc_attack = ElectricBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A8B169F
        unknown_0x0a8b169f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xECEBB97E
        unknown_0xecebb97e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B53DC0D
        unknown_0x2b53dc0d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79CCC5B8
        energy_drain = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AF75FCC
        unknown_0x3af75fcc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7B4922A
        max_static_intensity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F4842A3
        ball_lift_delay_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA928ED42
        ball_lift_delay_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x283F2238
        unknown_0x283f2238 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE5F8DD9
        unknown_0xce5f8dd9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x638D46CE
        unknown_0x638d46ce = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85EDE92F
        unknown_0x85ede92f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62FB47A5
        hungry_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x677E48EA
        unknown_0x677e48ea = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7EDF931D
        unknown_0x7edf931d = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15283674
        unknown_0x15283674 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AE10F78
        unknown_0x1ae10f78 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93F9240C
        unknown_0x93f9240c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50B079ED
        phase_out_says_actions = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB15B41FA
        max_says_actions = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5562C40D
        arc_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11F74E71
        arc_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3509CDD9
        sound_arc_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x953BC1D2
        arc_number = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21828087
        arc_length = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x328B3E6E
        arc_move_time_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4EB918F
        arc_move_time_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55EBB850
        arc_on_time_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB38B17B1
        arc_on_time_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DC77716
        unknown_0x6dc77716 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6FC4508C
        unknown_0x6fc4508c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DE8DA8D
        unknown_0x7de8da8d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF67DBAAB
        unknown_0xf67dbaab = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6F6EB1F4
        blur_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6409EDB3
        blur_duration = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            disable_player_grab,
            disable_pirate_grab,
            disable_hungry_mode,
            post_hatch_scale,
            unknown_0xef6d8c96,
            unknown_0x763e71ae,
            recheck_path_time,
            recheck_path_distance,
            scan_delay,
            patrol,
            attack,
            hungry,
            flyer_movement_mode_0x7b6c604a,
            flyer_movement_mode_0x292754af,
            ball_lift,
            initial_vulnerability,
            hungry_vulnerability,
            ball_lift_vulnerability,
            phase_out_vulnerability,
            phase_out_radius_missile,
            metroid_phazeoid_struct_0x7c187bd0,
            metroid_phazeoid_struct_0x0c7b243d,
            metroid_phazeoid_struct_0x33b1809f,
            metroid_phazeoid_struct_0x0ec6856a,
            metroid_phazeoid_struct_0x61fab47a,
            metroid_phazeoid_struct_0x26aac761,
            brain_vulnerability,
            x_ray_brain_radius,
            normal_brain_radius,
            phase_out_time_min,
            phase_out_time_max,
            phase_in_time_min,
            phase_in_time_max,
            phase_temple_disable_time_max,
            phase_temple_disable_time_min,
            unknown_0xa77f2fe5,
            unknown_0x411f8004,
            unknown_0xd14fc373,
            unknown_0x372f6c92,
            ball_lift_slope_padding,
            unknown_0x900a62f6,
            arc_range_min,
            arc_range_max,
            unknown_0x9aab0b9a,
            unknown_0x7ccba47b,
            arc_attack,
            unknown_0x0a8b169f,
            unknown_0xecebb97e,
            unknown_0x2b53dc0d,
            energy_drain,
            unknown_0x3af75fcc,
            max_static_intensity,
            ball_lift_delay_min,
            ball_lift_delay_max,
            unknown_0x283f2238,
            unknown_0xce5f8dd9,
            unknown_0x638d46ce,
            unknown_0x85ede92f,
            hungry_damage_threshold,
            unknown_0x677e48ea,
            unknown_0x7edf931d,
            unknown_0x15283674,
            unknown_0x1ae10f78,
            unknown_0x93f9240c,
            phase_out_says_actions,
            max_says_actions,
            arc_effect,
            arc_explosion,
            sound_arc_explosion,
            arc_number,
            arc_length,
            arc_move_time_max,
            arc_move_time_min,
            arc_on_time_max,
            arc_on_time_min,
            unknown_0x6dc77716,
            unknown_0x6fc4508c,
            unknown_0x7de8da8d,
            unknown_0xf67dbaab,
            blur_radius,
            blur_duration,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00Q")  # 81 properties

        data.write(b"t(\x8e\xf3")  # 0x74288ef3
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.disable_player_grab))

        data.write(b"\x06y\xe2\x0c")  # 0x679e20c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.disable_pirate_grab))

        data.write(b"\xaeF\xd8\x0e")  # 0xae46d80e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.disable_hungry_mode))

        data.write(b"\xbdb\xd0.")  # 0xbd62d02e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.post_hatch_scale))

        data.write(b"\xefm\x8c\x96")  # 0xef6d8c96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xef6d8c96))

        data.write(b"v>q\xae")  # 0x763e71ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x763e71ae))

        data.write(b"\x9a\xa9\x0bk")  # 0x9aa90b6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b"v&\xec\x89")  # 0x7626ec89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b"\x7f\xc8'\xa2")  # 0x7fc827a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_delay))

        data.write(b"\xcc\xdd:\xca")  # 0xccdd3aca
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patrol.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfa*\x17?")  # 0xfa2a173f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x97\xee\xd1\xf6")  # 0x97eed1f6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hungry.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{l`J")  # 0x7b6c604a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0x7b6c604a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")'T\xaf")  # 0x292754af
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0x292754af.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x18\xb5\x14:")  # 0x18b5143a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_lift.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\xd0\xd4\r")  # 0xedd0d40d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.initial_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8d~\x81\xd6")  # 0x8d7e81d6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hungry_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf6\x8e\xad\xc9")  # 0xf68eadc9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_lift_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdc\x02\r\xa7")  # 0xdc020da7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phase_out_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa48\xa3\xcd")  # 0xa438a3cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_out_radius_missile))

        data.write(b"|\x18{\xd0")  # 0x7c187bd0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_phazeoid_struct_0x7c187bd0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0c{$=")  # 0xc7b243d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_phazeoid_struct_0x0c7b243d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\xb1\x80\x9f")  # 0x33b1809f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_phazeoid_struct_0x33b1809f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0e\xc6\x85j")  # 0xec6856a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_phazeoid_struct_0x0ec6856a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"a\xfa\xb4z")  # 0x61fab47a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_phazeoid_struct_0x61fab47a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&\xaa\xc7a")  # 0x26aac761
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_phazeoid_struct_0x26aac761.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"$:\xb1\r")  # 0x243ab10d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.brain_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"-\xc4\xac\x9c")  # 0x2dc4ac9c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.x_ray_brain_radius))

        data.write(b"|\xb7`\xa5")  # 0x7cb760a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.normal_brain_radius))

        data.write(b"\x06\xa2\xbb\xb8")  # 0x6a2bbb8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_out_time_min))

        data.write(b"\xe0\xc2\x14Y")  # 0xe0c21459
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_out_time_max))

        data.write(b"TO\xa22")  # 0x544fa232
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_in_time_min))

        data.write(b"\xb2/\r\xd3")  # 0xb22f0dd3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_in_time_max))

        data.write(b"\xac\xda\xcc\x80")  # 0xacdacc80
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_temple_disable_time_max))

        data.write(b"J\xbaca")  # 0x4aba6361
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_temple_disable_time_min))

        data.write(b"\xa7\x7f/\xe5")  # 0xa77f2fe5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa77f2fe5))

        data.write(b"A\x1f\x80\x04")  # 0x411f8004
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x411f8004))

        data.write(b"\xd1O\xc3s")  # 0xd14fc373
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd14fc373))

        data.write(b"7/l\x92")  # 0x372f6c92
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x372f6c92))

        data.write(b"\xf6}\x89\xb1")  # 0xf67d89b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_lift_slope_padding))

        data.write(b"\x90\nb\xf6")  # 0x900a62f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x900a62f6))

        data.write(b"\xa1\xb7\xcf'")  # 0xa1b7cf27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_range_min))

        data.write(b"G\xd7`\xc6")  # 0x47d760c6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_range_max))

        data.write(b"\x9a\xab\x0b\x9a")  # 0x9aab0b9a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9aab0b9a))

        data.write(b"|\xcb\xa4{")  # 0x7ccba47b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7ccba47b))

        data.write(b"mA\x7fL")  # 0x6d417f4c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.arc_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\n\x8b\x16\x9f")  # 0xa8b169f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a8b169f))

        data.write(b"\xec\xeb\xb9~")  # 0xecebb97e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xecebb97e))

        data.write(b"+S\xdc\r")  # 0x2b53dc0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2b53dc0d))

        data.write(b"y\xcc\xc5\xb8")  # 0x79ccc5b8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.energy_drain.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b":\xf7_\xcc")  # 0x3af75fcc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3af75fcc))

        data.write(b"\xe7\xb4\x92*")  # 0xe7b4922a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_static_intensity))

        data.write(b"OHB\xa3")  # 0x4f4842a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_lift_delay_min))

        data.write(b"\xa9(\xedB")  # 0xa928ed42
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_lift_delay_max))

        data.write(b'(?"8')  # 0x283f2238
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x283f2238))

        data.write(b"\xce_\x8d\xd9")  # 0xce5f8dd9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xce5f8dd9))

        data.write(b"c\x8dF\xce")  # 0x638d46ce
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x638d46ce))

        data.write(b"\x85\xed\xe9/")  # 0x85ede92f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x85ede92f))

        data.write(b"b\xfbG\xa5")  # 0x62fb47a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hungry_damage_threshold))

        data.write(b"g~H\xea")  # 0x677e48ea
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x677e48ea))

        data.write(b"~\xdf\x93\x1d")  # 0x7edf931d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7edf931d))

        data.write(b"\x15(6t")  # 0x15283674
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x15283674))

        data.write(b"\x1a\xe1\x0fx")  # 0x1ae10f78
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1ae10f78))

        data.write(b"\x93\xf9$\x0c")  # 0x93f9240c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x93f9240c))

        data.write(b"P\xb0y\xed")  # 0x50b079ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phase_out_says_actions))

        data.write(b"\xb1[A\xfa")  # 0xb15b41fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_says_actions))

        data.write(b"Ub\xc4\r")  # 0x5562c40d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.arc_effect))

        data.write(b"\x11\xf7Nq")  # 0x11f74e71
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.arc_explosion))

        data.write(b"5\t\xcd\xd9")  # 0x3509cdd9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_arc_explosion))

        data.write(b"\x95;\xc1\xd2")  # 0x953bc1d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.arc_number))

        data.write(b"!\x82\x80\x87")  # 0x21828087
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_length))

        data.write(b"2\x8b>n")  # 0x328b3e6e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_move_time_max))

        data.write(b"\xd4\xeb\x91\x8f")  # 0xd4eb918f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_move_time_min))

        data.write(b"U\xeb\xb8P")  # 0x55ebb850
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_on_time_max))

        data.write(b"\xb3\x8b\x17\xb1")  # 0xb38b17b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_on_time_min))

        data.write(b"m\xc7w\x16")  # 0x6dc77716
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6dc77716))

        data.write(b"o\xc4P\x8c")  # 0x6fc4508c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6fc4508c))

        data.write(b"}\xe8\xda\x8d")  # 0x7de8da8d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7de8da8d))

        data.write(b"\xf6}\xba\xab")  # 0xf67dbaab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf67dbaab))

        data.write(b"on\xb1\xf4")  # 0x6f6eb1f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.blur_radius))

        data.write(b"d\t\xed\xb3")  # 0x6409edb3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.blur_duration))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidPhazeoidDataJson", data)
        return cls(
            disable_player_grab=json_data["disable_player_grab"],
            disable_pirate_grab=json_data["disable_pirate_grab"],
            disable_hungry_mode=json_data["disable_hungry_mode"],
            post_hatch_scale=json_data["post_hatch_scale"],
            unknown_0xef6d8c96=json_data["unknown_0xef6d8c96"],
            unknown_0x763e71ae=json_data["unknown_0x763e71ae"],
            recheck_path_time=json_data["recheck_path_time"],
            recheck_path_distance=json_data["recheck_path_distance"],
            scan_delay=json_data["scan_delay"],
            patrol=FlyerMovementMode.from_json(json_data["patrol"]),
            attack=FlyerMovementMode.from_json(json_data["attack"]),
            hungry=FlyerMovementMode.from_json(json_data["hungry"]),
            flyer_movement_mode_0x7b6c604a=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0x7b6c604a"]),
            flyer_movement_mode_0x292754af=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0x292754af"]),
            ball_lift=FlyerMovementMode.from_json(json_data["ball_lift"]),
            initial_vulnerability=DamageVulnerability.from_json(json_data["initial_vulnerability"]),
            hungry_vulnerability=DamageVulnerability.from_json(json_data["hungry_vulnerability"]),
            ball_lift_vulnerability=DamageVulnerability.from_json(json_data["ball_lift_vulnerability"]),
            phase_out_vulnerability=DamageVulnerability.from_json(json_data["phase_out_vulnerability"]),
            phase_out_radius_missile=json_data["phase_out_radius_missile"],
            metroid_phazeoid_struct_0x7c187bd0=MetroidPhazeoidStruct.from_json(
                json_data["metroid_phazeoid_struct_0x7c187bd0"]
            ),
            metroid_phazeoid_struct_0x0c7b243d=MetroidPhazeoidStruct.from_json(
                json_data["metroid_phazeoid_struct_0x0c7b243d"]
            ),
            metroid_phazeoid_struct_0x33b1809f=MetroidPhazeoidStruct.from_json(
                json_data["metroid_phazeoid_struct_0x33b1809f"]
            ),
            metroid_phazeoid_struct_0x0ec6856a=MetroidPhazeoidStruct.from_json(
                json_data["metroid_phazeoid_struct_0x0ec6856a"]
            ),
            metroid_phazeoid_struct_0x61fab47a=MetroidPhazeoidStruct.from_json(
                json_data["metroid_phazeoid_struct_0x61fab47a"]
            ),
            metroid_phazeoid_struct_0x26aac761=MetroidPhazeoidStruct.from_json(
                json_data["metroid_phazeoid_struct_0x26aac761"]
            ),
            brain_vulnerability=DamageVulnerability.from_json(json_data["brain_vulnerability"]),
            x_ray_brain_radius=json_data["x_ray_brain_radius"],
            normal_brain_radius=json_data["normal_brain_radius"],
            phase_out_time_min=json_data["phase_out_time_min"],
            phase_out_time_max=json_data["phase_out_time_max"],
            phase_in_time_min=json_data["phase_in_time_min"],
            phase_in_time_max=json_data["phase_in_time_max"],
            phase_temple_disable_time_max=json_data["phase_temple_disable_time_max"],
            phase_temple_disable_time_min=json_data["phase_temple_disable_time_min"],
            unknown_0xa77f2fe5=json_data["unknown_0xa77f2fe5"],
            unknown_0x411f8004=json_data["unknown_0x411f8004"],
            unknown_0xd14fc373=json_data["unknown_0xd14fc373"],
            unknown_0x372f6c92=json_data["unknown_0x372f6c92"],
            ball_lift_slope_padding=json_data["ball_lift_slope_padding"],
            unknown_0x900a62f6=json_data["unknown_0x900a62f6"],
            arc_range_min=json_data["arc_range_min"],
            arc_range_max=json_data["arc_range_max"],
            unknown_0x9aab0b9a=json_data["unknown_0x9aab0b9a"],
            unknown_0x7ccba47b=json_data["unknown_0x7ccba47b"],
            arc_attack=ElectricBeamInfo.from_json(json_data["arc_attack"]),
            unknown_0x0a8b169f=json_data["unknown_0x0a8b169f"],
            unknown_0xecebb97e=json_data["unknown_0xecebb97e"],
            unknown_0x2b53dc0d=json_data["unknown_0x2b53dc0d"],
            energy_drain=Spline.from_json(json_data["energy_drain"]),
            unknown_0x3af75fcc=json_data["unknown_0x3af75fcc"],
            max_static_intensity=json_data["max_static_intensity"],
            ball_lift_delay_min=json_data["ball_lift_delay_min"],
            ball_lift_delay_max=json_data["ball_lift_delay_max"],
            unknown_0x283f2238=json_data["unknown_0x283f2238"],
            unknown_0xce5f8dd9=json_data["unknown_0xce5f8dd9"],
            unknown_0x638d46ce=json_data["unknown_0x638d46ce"],
            unknown_0x85ede92f=json_data["unknown_0x85ede92f"],
            hungry_damage_threshold=json_data["hungry_damage_threshold"],
            unknown_0x677e48ea=json_data["unknown_0x677e48ea"],
            unknown_0x7edf931d=json_data["unknown_0x7edf931d"],
            unknown_0x15283674=json_data["unknown_0x15283674"],
            unknown_0x1ae10f78=json_data["unknown_0x1ae10f78"],
            unknown_0x93f9240c=json_data["unknown_0x93f9240c"],
            phase_out_says_actions=json_data["phase_out_says_actions"],
            max_says_actions=json_data["max_says_actions"],
            arc_effect=json_data["arc_effect"],
            arc_explosion=json_data["arc_explosion"],
            sound_arc_explosion=json_data["sound_arc_explosion"],
            arc_number=json_data["arc_number"],
            arc_length=json_data["arc_length"],
            arc_move_time_max=json_data["arc_move_time_max"],
            arc_move_time_min=json_data["arc_move_time_min"],
            arc_on_time_max=json_data["arc_on_time_max"],
            arc_on_time_min=json_data["arc_on_time_min"],
            unknown_0x6dc77716=json_data["unknown_0x6dc77716"],
            unknown_0x6fc4508c=json_data["unknown_0x6fc4508c"],
            unknown_0x7de8da8d=json_data["unknown_0x7de8da8d"],
            unknown_0xf67dbaab=json_data["unknown_0xf67dbaab"],
            blur_radius=json_data["blur_radius"],
            blur_duration=json_data["blur_duration"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "disable_player_grab": self.disable_player_grab,
            "disable_pirate_grab": self.disable_pirate_grab,
            "disable_hungry_mode": self.disable_hungry_mode,
            "post_hatch_scale": self.post_hatch_scale,
            "unknown_0xef6d8c96": self.unknown_0xef6d8c96,
            "unknown_0x763e71ae": self.unknown_0x763e71ae,
            "recheck_path_time": self.recheck_path_time,
            "recheck_path_distance": self.recheck_path_distance,
            "scan_delay": self.scan_delay,
            "patrol": self.patrol.to_json(),
            "attack": self.attack.to_json(),
            "hungry": self.hungry.to_json(),
            "flyer_movement_mode_0x7b6c604a": self.flyer_movement_mode_0x7b6c604a.to_json(),
            "flyer_movement_mode_0x292754af": self.flyer_movement_mode_0x292754af.to_json(),
            "ball_lift": self.ball_lift.to_json(),
            "initial_vulnerability": self.initial_vulnerability.to_json(),
            "hungry_vulnerability": self.hungry_vulnerability.to_json(),
            "ball_lift_vulnerability": self.ball_lift_vulnerability.to_json(),
            "phase_out_vulnerability": self.phase_out_vulnerability.to_json(),
            "phase_out_radius_missile": self.phase_out_radius_missile,
            "metroid_phazeoid_struct_0x7c187bd0": self.metroid_phazeoid_struct_0x7c187bd0.to_json(),
            "metroid_phazeoid_struct_0x0c7b243d": self.metroid_phazeoid_struct_0x0c7b243d.to_json(),
            "metroid_phazeoid_struct_0x33b1809f": self.metroid_phazeoid_struct_0x33b1809f.to_json(),
            "metroid_phazeoid_struct_0x0ec6856a": self.metroid_phazeoid_struct_0x0ec6856a.to_json(),
            "metroid_phazeoid_struct_0x61fab47a": self.metroid_phazeoid_struct_0x61fab47a.to_json(),
            "metroid_phazeoid_struct_0x26aac761": self.metroid_phazeoid_struct_0x26aac761.to_json(),
            "brain_vulnerability": self.brain_vulnerability.to_json(),
            "x_ray_brain_radius": self.x_ray_brain_radius,
            "normal_brain_radius": self.normal_brain_radius,
            "phase_out_time_min": self.phase_out_time_min,
            "phase_out_time_max": self.phase_out_time_max,
            "phase_in_time_min": self.phase_in_time_min,
            "phase_in_time_max": self.phase_in_time_max,
            "phase_temple_disable_time_max": self.phase_temple_disable_time_max,
            "phase_temple_disable_time_min": self.phase_temple_disable_time_min,
            "unknown_0xa77f2fe5": self.unknown_0xa77f2fe5,
            "unknown_0x411f8004": self.unknown_0x411f8004,
            "unknown_0xd14fc373": self.unknown_0xd14fc373,
            "unknown_0x372f6c92": self.unknown_0x372f6c92,
            "ball_lift_slope_padding": self.ball_lift_slope_padding,
            "unknown_0x900a62f6": self.unknown_0x900a62f6,
            "arc_range_min": self.arc_range_min,
            "arc_range_max": self.arc_range_max,
            "unknown_0x9aab0b9a": self.unknown_0x9aab0b9a,
            "unknown_0x7ccba47b": self.unknown_0x7ccba47b,
            "arc_attack": self.arc_attack.to_json(),
            "unknown_0x0a8b169f": self.unknown_0x0a8b169f,
            "unknown_0xecebb97e": self.unknown_0xecebb97e,
            "unknown_0x2b53dc0d": self.unknown_0x2b53dc0d,
            "energy_drain": self.energy_drain.to_json(),
            "unknown_0x3af75fcc": self.unknown_0x3af75fcc,
            "max_static_intensity": self.max_static_intensity,
            "ball_lift_delay_min": self.ball_lift_delay_min,
            "ball_lift_delay_max": self.ball_lift_delay_max,
            "unknown_0x283f2238": self.unknown_0x283f2238,
            "unknown_0xce5f8dd9": self.unknown_0xce5f8dd9,
            "unknown_0x638d46ce": self.unknown_0x638d46ce,
            "unknown_0x85ede92f": self.unknown_0x85ede92f,
            "hungry_damage_threshold": self.hungry_damage_threshold,
            "unknown_0x677e48ea": self.unknown_0x677e48ea,
            "unknown_0x7edf931d": self.unknown_0x7edf931d,
            "unknown_0x15283674": self.unknown_0x15283674,
            "unknown_0x1ae10f78": self.unknown_0x1ae10f78,
            "unknown_0x93f9240c": self.unknown_0x93f9240c,
            "phase_out_says_actions": self.phase_out_says_actions,
            "max_says_actions": self.max_says_actions,
            "arc_effect": self.arc_effect,
            "arc_explosion": self.arc_explosion,
            "sound_arc_explosion": self.sound_arc_explosion,
            "arc_number": self.arc_number,
            "arc_length": self.arc_length,
            "arc_move_time_max": self.arc_move_time_max,
            "arc_move_time_min": self.arc_move_time_min,
            "arc_on_time_max": self.arc_on_time_max,
            "arc_on_time_min": self.arc_on_time_min,
            "unknown_0x6dc77716": self.unknown_0x6dc77716,
            "unknown_0x6fc4508c": self.unknown_0x6fc4508c,
            "unknown_0x7de8da8d": self.unknown_0x7de8da8d,
            "unknown_0xf67dbaab": self.unknown_0xf67dbaab,
            "blur_radius": self.blur_radius,
            "blur_duration": self.blur_duration,
        }


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_hungry(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_flyer_movement_mode_0x7b6c604a(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_flyer_movement_mode_0x292754af(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_ball_lift(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_initial_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hungry_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_ball_lift_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_phase_out_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x7c187bd0(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x0c7b243d(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x33b1809f(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x0ec6856a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x61fab47a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x26aac761(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_brain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_arc_attack(data: typing.BinaryIO, game: Game, property_size: int) -> ElectricBeamInfo:
    return ElectricBeamInfo.from_stream(data, game, property_size)


def _decode_energy_drain(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x74288EF3: ("disable_player_grab", structs.decode_BIG_bool_),
    0x0679E20C: ("disable_pirate_grab", structs.decode_BIG_bool_),
    0xAE46D80E: ("disable_hungry_mode", structs.decode_BIG_bool_),
    0xBD62D02E: ("post_hatch_scale", structs.decode_BIG_f),
    0xEF6D8C96: ("unknown_0xef6d8c96", structs.decode_BIG_f),
    0x763E71AE: ("unknown_0x763e71ae", structs.decode_BIG_f),
    0x9AA90B6B: ("recheck_path_time", structs.decode_BIG_f),
    0x7626EC89: ("recheck_path_distance", structs.decode_BIG_f),
    0x7FC827A2: ("scan_delay", structs.decode_BIG_f),
    0xCCDD3ACA: ("patrol", _decode_patrol),
    0xFA2A173F: ("attack", _decode_attack),
    0x97EED1F6: ("hungry", _decode_hungry),
    0x7B6C604A: ("flyer_movement_mode_0x7b6c604a", _decode_flyer_movement_mode_0x7b6c604a),
    0x292754AF: ("flyer_movement_mode_0x292754af", _decode_flyer_movement_mode_0x292754af),
    0x18B5143A: ("ball_lift", _decode_ball_lift),
    0xEDD0D40D: ("initial_vulnerability", _decode_initial_vulnerability),
    0x8D7E81D6: ("hungry_vulnerability", _decode_hungry_vulnerability),
    0xF68EADC9: ("ball_lift_vulnerability", _decode_ball_lift_vulnerability),
    0xDC020DA7: ("phase_out_vulnerability", _decode_phase_out_vulnerability),
    0xA438A3CD: ("phase_out_radius_missile", structs.decode_BIG_f),
    0x7C187BD0: ("metroid_phazeoid_struct_0x7c187bd0", _decode_metroid_phazeoid_struct_0x7c187bd0),
    0x0C7B243D: ("metroid_phazeoid_struct_0x0c7b243d", _decode_metroid_phazeoid_struct_0x0c7b243d),
    0x33B1809F: ("metroid_phazeoid_struct_0x33b1809f", _decode_metroid_phazeoid_struct_0x33b1809f),
    0x0EC6856A: ("metroid_phazeoid_struct_0x0ec6856a", _decode_metroid_phazeoid_struct_0x0ec6856a),
    0x61FAB47A: ("metroid_phazeoid_struct_0x61fab47a", _decode_metroid_phazeoid_struct_0x61fab47a),
    0x26AAC761: ("metroid_phazeoid_struct_0x26aac761", _decode_metroid_phazeoid_struct_0x26aac761),
    0x243AB10D: ("brain_vulnerability", _decode_brain_vulnerability),
    0x2DC4AC9C: ("x_ray_brain_radius", structs.decode_BIG_f),
    0x7CB760A5: ("normal_brain_radius", structs.decode_BIG_f),
    0x06A2BBB8: ("phase_out_time_min", structs.decode_BIG_f),
    0xE0C21459: ("phase_out_time_max", structs.decode_BIG_f),
    0x544FA232: ("phase_in_time_min", structs.decode_BIG_f),
    0xB22F0DD3: ("phase_in_time_max", structs.decode_BIG_f),
    0xACDACC80: ("phase_temple_disable_time_max", structs.decode_BIG_f),
    0x4ABA6361: ("phase_temple_disable_time_min", structs.decode_BIG_f),
    0xA77F2FE5: ("unknown_0xa77f2fe5", structs.decode_BIG_f),
    0x411F8004: ("unknown_0x411f8004", structs.decode_BIG_f),
    0xD14FC373: ("unknown_0xd14fc373", structs.decode_BIG_f),
    0x372F6C92: ("unknown_0x372f6c92", structs.decode_BIG_f),
    0xF67D89B1: ("ball_lift_slope_padding", structs.decode_BIG_f),
    0x900A62F6: ("unknown_0x900a62f6", structs.decode_BIG_f),
    0xA1B7CF27: ("arc_range_min", structs.decode_BIG_f),
    0x47D760C6: ("arc_range_max", structs.decode_BIG_f),
    0x9AAB0B9A: ("unknown_0x9aab0b9a", structs.decode_BIG_f),
    0x7CCBA47B: ("unknown_0x7ccba47b", structs.decode_BIG_f),
    0x6D417F4C: ("arc_attack", _decode_arc_attack),
    0x0A8B169F: ("unknown_0x0a8b169f", structs.decode_BIG_f),
    0xECEBB97E: ("unknown_0xecebb97e", structs.decode_BIG_f),
    0x2B53DC0D: ("unknown_0x2b53dc0d", structs.decode_BIG_f),
    0x79CCC5B8: ("energy_drain", _decode_energy_drain),
    0x3AF75FCC: ("unknown_0x3af75fcc", structs.decode_BIG_f),
    0xE7B4922A: ("max_static_intensity", structs.decode_BIG_f),
    0x4F4842A3: ("ball_lift_delay_min", structs.decode_BIG_f),
    0xA928ED42: ("ball_lift_delay_max", structs.decode_BIG_f),
    0x283F2238: ("unknown_0x283f2238", structs.decode_BIG_f),
    0xCE5F8DD9: ("unknown_0xce5f8dd9", structs.decode_BIG_f),
    0x638D46CE: ("unknown_0x638d46ce", structs.decode_BIG_f),
    0x85EDE92F: ("unknown_0x85ede92f", structs.decode_BIG_f),
    0x62FB47A5: ("hungry_damage_threshold", structs.decode_BIG_f),
    0x677E48EA: ("unknown_0x677e48ea", structs.decode_BIG_bool_),
    0x7EDF931D: ("unknown_0x7edf931d", structs.decode_BIG_bool_),
    0x15283674: ("unknown_0x15283674", structs.decode_BIG_bool_),
    0x1AE10F78: ("unknown_0x1ae10f78", structs.decode_BIG_f),
    0x93F9240C: ("unknown_0x93f9240c", structs.decode_BIG_f),
    0x50B079ED: ("phase_out_says_actions", structs.decode_BIG_f),
    0xB15B41FA: ("max_says_actions", structs.decode_BIG_f),
    0x5562C40D: ("arc_effect", structs.decode_BIG_Q),
    0x11F74E71: ("arc_explosion", structs.decode_BIG_Q),
    0x3509CDD9: ("sound_arc_explosion", structs.decode_BIG_Q),
    0x953BC1D2: ("arc_number", structs.decode_BIG_l),
    0x21828087: ("arc_length", structs.decode_BIG_f),
    0x328B3E6E: ("arc_move_time_max", structs.decode_BIG_f),
    0xD4EB918F: ("arc_move_time_min", structs.decode_BIG_f),
    0x55EBB850: ("arc_on_time_max", structs.decode_BIG_f),
    0xB38B17B1: ("arc_on_time_min", structs.decode_BIG_f),
    0x6DC77716: ("unknown_0x6dc77716", structs.decode_BIG_f),
    0x6FC4508C: ("unknown_0x6fc4508c", structs.decode_BIG_f),
    0x7DE8DA8D: ("unknown_0x7de8da8d", structs.decode_BIG_f),
    0xF67DBAAB: ("unknown_0xf67dbaab", structs.decode_BIG_f),
    0x6F6EB1F4: ("blur_radius", structs.decode_BIG_f),
    0x6409EDB3: ("blur_duration", structs.decode_BIG_f),
}
