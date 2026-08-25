# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MetroidHatcherDataJson(typing_extensions.TypedDict):
        hearing_range: float
        lose_interest_range: float
        lose_interest_time: float
        unknown_0xfe4588a1: float
        unknown_0xc2688b41: float
        unknown_0x7b0cc30d: float
        damage_vulnerability: json_util.JsonObject
        body_vulnerability: json_util.JsonObject
        brain_vulnerability: json_util.JsonObject
        brain_x_ray_radius: float
        brain_radius: float
        leg_vulnerability: json_util.JsonObject
        unknown_0xb9e0c90d: float
        unknown_0x81d39802: float
        tentacle_regrow_time: float
        unknown_0xf79a10b0: float
        unknown_0xc550a481: float
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0xe08106ed: float
        unknown_0x88d7c540: float
        unknown_0xace62367: float
        unknown_0x620b1b3d: float
        max_attack_height: float
        min_attack_height: float
        max_attack_forward: float
        min_attack_forward: float
        unknown_0x0978b98a: float
        unknown_0xcfcd32bb: float
        unknown_0x17d71349: float
        recheck_path_time: float
        recheck_path_distance: float
        max_num_metroids: int
        auto_spawn: bool
        max_spawn_delay: float
        min_spawn_delay: float
        unknown_0x6089191d: int
        unknown_0x258b5a9f: int
        unknown_0x2ae610e5: float
        hatch_chance: float
        maya_double: float
        unknown_0x3fee1ba4: float
        spin_attack_damage: json_util.JsonObject
        max_spin_attack_delay: float
        min_spin_attack_delay: float
        unknown_0xbeaf2105: float
        unknown_0x54ff4d38: float
        unknown_0xb29fe2d9: float
        dodge_chance: float
        unknown_0x42647ad7: float
        unknown_0xa404d536: float
        unknown_0x248d3599: float
        unknown_0xbfd77e62: float
        unknown_0xcdaa2c74: float
        unknown_0x2bca8395: float
        patrol: json_util.JsonObject
        attack_path: json_util.JsonObject
        combat: json_util.JsonObject
        stab_attack: json_util.JsonObject
        flyer_movement_mode_0x6ca56014: json_util.JsonObject
        flyer_movement_mode_0xe20e51c3: json_util.JsonObject
        flyer_movement_mode_0x25a68a0e: json_util.JsonObject
        flyer_movement_mode_0xd9b5d506: json_util.JsonObject
        flyer_movement_mode_0x8bb1c3a2: json_util.JsonObject
        stunned: json_util.JsonObject
        flyer_movement_mode_0xfb2ddfad: json_util.JsonObject
        dash: json_util.JsonObject
        flyer_movement_mode_0x5fe13a7b: json_util.JsonObject
        claw: json_util.JsonObject
        char_0x4d7dbeab: json_util.JsonObject
        char_0xa17c09bb: json_util.JsonObject
        char_0x11dc2dab: json_util.JsonObject
        char_0xfddd9abb: json_util.JsonObject
        unknown_0xc99cee00: float
        unknown_0x2ffc41e1: float
        unknown_0x7f5d9ab7: float
        unknown_0x993d3556: float
        unknown_0x08efeb79: float
        unknown_0xee8f4498: float
        unknown_0xc24d8fbd: float
        unknown_0x242d205c: float
        stun_threshold: float
        electric_ball_effect: int
        sound_ball_effect: int
        electric_visor_effect: int
        sound_visor_effect: int
        leg_hit_splash: int


@dataclasses.dataclass()
class MetroidHatcherData(BaseProperty):
    hearing_range: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25474550, original_name="HearingRange"),
        },
    )
    lose_interest_range: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x474FA589, original_name="LoseInterestRange"),
        },
    )
    lose_interest_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8B0C2BB, original_name="LoseInterestTime"),
        },
    )
    unknown_0xfe4588a1: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFE4588A1, original_name="Unknown"),
        },
    )
    unknown_0xc2688b41: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC2688B41, original_name="Unknown"),
        },
    )
    unknown_0x7b0cc30d: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7B0CC30D, original_name="Unknown"),
        },
    )
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x742B3336,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    body_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0D9230D1,
                original_name="BodyVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
    brain_x_ray_radius: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x012115A2, original_name="BrainXRayRadius"),
        },
    )
    brain_radius: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA12A4409, original_name="BrainRadius"),
        },
    )
    leg_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x9F0FF852,
                original_name="LegVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0xb9e0c90d: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB9E0C90D, original_name="Unknown"),
        },
    )
    unknown_0x81d39802: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x81D39802, original_name="Unknown"),
        },
    )
    tentacle_regrow_time: float = dataclasses.field(
        default=0.33329999446868896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA002DCB, original_name="TentacleRegrowTime"),
        },
    )
    unknown_0xf79a10b0: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF79A10B0, original_name="Unknown"),
        },
    )
    unknown_0xc550a481: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC550A481, original_name="Unknown"),
        },
    )
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0xe08106ed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE08106ED, original_name="Unknown"),
        },
    )
    unknown_0x88d7c540: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88D7C540, original_name="Unknown"),
        },
    )
    unknown_0xace62367: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xACE62367, original_name="Unknown"),
        },
    )
    unknown_0x620b1b3d: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x620B1B3D, original_name="Unknown"),
        },
    )
    max_attack_height: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE1AE51D8, original_name="MaxAttackHeight"),
        },
    )
    min_attack_height: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC8D0ACC0, original_name="MinAttackHeight"),
        },
    )
    max_attack_forward: float = dataclasses.field(
        default=16.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF3E8012D, original_name="MaxAttackForward"),
        },
    )
    min_attack_forward: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE0ADE786, original_name="MinAttackForward"),
        },
    )
    unknown_0x0978b98a: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0978B98A, original_name="Unknown"),
        },
    )
    unknown_0xcfcd32bb: float = dataclasses.field(
        default=-1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCFCD32BB, original_name="Unknown"),
        },
    )
    unknown_0x17d71349: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17D71349, original_name="Unknown"),
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
    max_num_metroids: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7915E2B3, original_name="MaxNumMetroids"),
        },
    )
    auto_spawn: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCCC0CF92, original_name="AutoSpawn"),
        },
    )
    max_spawn_delay: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75E0B0A7, original_name="MaxSpawnDelay"),
        },
    )
    min_spawn_delay: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2646A843, original_name="MinSpawnDelay"),
        },
    )
    unknown_0x6089191d: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6089191D, original_name="Unknown"),
        },
    )
    unknown_0x258b5a9f: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x258B5A9F, original_name="Unknown"),
        },
    )
    unknown_0x2ae610e5: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2AE610E5, original_name="Unknown"),
        },
    )
    hatch_chance: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x354BAE31, original_name="HatchChance"),
        },
    )
    maya_double: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4B2C801, original_name="MayaDouble"),
        },
    )
    unknown_0x3fee1ba4: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3FEE1BA4, original_name="Unknown"),
        },
    )
    spin_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xCFACFF53,
                original_name="SpinAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    max_spin_attack_delay: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6CB6D8C7, original_name="MaxSpinAttackDelay"),
        },
    )
    min_spin_attack_delay: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x682CE9ED, original_name="MinSpinAttackDelay"),
        },
    )
    unknown_0xbeaf2105: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBEAF2105, original_name="Unknown"),
        },
    )
    unknown_0x54ff4d38: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54FF4D38, original_name="Unknown"),
        },
    )
    unknown_0xb29fe2d9: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB29FE2D9, original_name="Unknown"),
        },
    )
    dodge_chance: float = dataclasses.field(
        default=0.0010000000474974513,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47BE3298, original_name="DodgeChance"),
        },
    )
    unknown_0x42647ad7: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x42647AD7, original_name="Unknown"),
        },
    )
    unknown_0xa404d536: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA404D536, original_name="Unknown"),
        },
    )
    unknown_0x248d3599: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x248D3599, original_name="Unknown"),
        },
    )
    unknown_0xbfd77e62: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBFD77E62, original_name="Unknown"),
        },
    )
    unknown_0xcdaa2c74: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCDAA2C74, original_name="Unknown"),
        },
    )
    unknown_0x2bca8395: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2BCA8395, original_name="Unknown"),
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
    attack_path: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xC845D3C0,
                original_name="AttackPath",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    combat: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xCC7D2E98,
                original_name="Combat",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    stab_attack: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xB9C3DB94,
                original_name="StabAttack",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0x6ca56014: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x6CA56014,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0xe20e51c3: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xE20E51C3,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0x25a68a0e: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x25A68A0E,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0xd9b5d506: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xD9B5D506,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0x8bb1c3a2: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x8BB1C3A2,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    stunned: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x389CB515,
                original_name="Stunned",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0xfb2ddfad: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xFB2DDFAD,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    dash: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xC558BC0D,
                original_name="Dash",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flyer_movement_mode_0x5fe13a7b: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x5FE13A7B,
                original_name="FlyerMovementMode",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    claw: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xFD38A106,
                original_name="Claw",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    char_0x4d7dbeab: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x4D7DBEAB,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    char_0xa17c09bb: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA17C09BB,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    char_0x11dc2dab: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x11DC2DAB,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    char_0xfddd9abb: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xFDDD9ABB,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_0xc99cee00: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC99CEE00, original_name="Unknown"),
        },
    )
    unknown_0x2ffc41e1: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2FFC41E1, original_name="Unknown"),
        },
    )
    unknown_0x7f5d9ab7: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7F5D9AB7, original_name="Unknown"),
        },
    )
    unknown_0x993d3556: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x993D3556, original_name="Unknown"),
        },
    )
    unknown_0x08efeb79: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08EFEB79, original_name="Unknown"),
        },
    )
    unknown_0xee8f4498: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE8F4498, original_name="Unknown"),
        },
    )
    unknown_0xc24d8fbd: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC24D8FBD, original_name="Unknown"),
        },
    )
    unknown_0x242d205c: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x242D205C, original_name="Unknown"),
        },
    )
    stun_threshold: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BDD1E4C, original_name="StunThreshold"),
        },
    )
    electric_ball_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6DA4A3B0, original_name="ElectricBallEffect"),
        },
    )
    sound_ball_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3FCD8B66, original_name="Sound_BallEffect"),
        },
    )
    electric_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCC0AF287, original_name="ElectricVisorEffect"),
        },
    )
    sound_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA3E8EC4E, original_name="Sound_VisorEffect"),
        },
    )
    leg_hit_splash: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF40A9C9D, original_name="LegHitSplash"),
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
        if property_count != 87:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25474550
        hearing_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x474FA589
        lose_interest_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8B0C2BB
        lose_interest_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE4588A1
        unknown_0xfe4588a1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2688B41
        unknown_0xc2688b41 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B0CC30D
        unknown_0x7b0cc30d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742B3336
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D9230D1
        body_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x243AB10D
        brain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x012115A2
        brain_x_ray_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA12A4409
        brain_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F0FF852
        leg_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB9E0C90D
        unknown_0xb9e0c90d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81D39802
        unknown_0x81d39802 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA002DCB
        tentacle_regrow_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF79A10B0
        unknown_0xf79a10b0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC550A481
        unknown_0xc550a481 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95E7A2C2
        unknown_0x95e7a2c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76BA1C18
        unknown_0x76ba1c18 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE08106ED
        unknown_0xe08106ed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88D7C540
        unknown_0x88d7c540 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACE62367
        unknown_0xace62367 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x620B1B3D
        unknown_0x620b1b3d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1AE51D8
        max_attack_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8D0ACC0
        min_attack_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3E8012D
        max_attack_forward = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0ADE786
        min_attack_forward = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0978B98A
        unknown_0x0978b98a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFCD32BB
        unknown_0xcfcd32bb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17D71349
        unknown_0x17d71349 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AA90B6B
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626EC89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7915E2B3
        max_num_metroids = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCC0CF92
        auto_spawn = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75E0B0A7
        max_spawn_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2646A843
        min_spawn_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6089191D
        unknown_0x6089191d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258B5A9F
        unknown_0x258b5a9f = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AE610E5
        unknown_0x2ae610e5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x354BAE31
        hatch_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4B2C801
        maya_double = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FEE1BA4
        unknown_0x3fee1ba4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFACFF53
        spin_attack_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_damage": 30.0, "di_knock_back_power": 20.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6CB6D8C7
        max_spin_attack_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x682CE9ED
        min_spin_attack_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBEAF2105
        unknown_0xbeaf2105 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54FF4D38
        unknown_0x54ff4d38 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB29FE2D9
        unknown_0xb29fe2d9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47BE3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42647AD7
        unknown_0x42647ad7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA404D536
        unknown_0xa404d536 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x248D3599
        unknown_0x248d3599 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFD77E62
        unknown_0xbfd77e62 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCDAA2C74
        unknown_0xcdaa2c74 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BCA8395
        unknown_0x2bca8395 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCDD3ACA
        patrol = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 3.0,
                "acceleration": 1.0,
                "facing_turn_rate": 30.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC845D3C0
        attack_path = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 3.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC7D2E98
        combat = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 3.0,
                "acceleration": 10.0,
                "turn_threshold": 181.0,
                "floor_buffer": 11.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB9C3DB94
        stab_attack = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 0.10000000149011612,
                "acceleration": 10.0,
                "turn_rate": 10800.0,
                "facing_turn_rate": 120.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 0.0,
                "floor_buffer": 8.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6CA56014
        flyer_movement_mode_0x6ca56014 = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 30.0,
                "acceleration": 50.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 0.0,
                "floor_buffer": 3.5,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE20E51C3
        flyer_movement_mode_0xe20e51c3 = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 30.0,
                "acceleration": 10.0,
                "facing_turn_rate": 1.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 1.0,
                "floor_buffer": 5.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25A68A0E
        flyer_movement_mode_0x25a68a0e = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 1.0,
                "acceleration": 10.0,
                "turn_threshold": 181.0,
                "height_variation_max": 0.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD9B5D506
        flyer_movement_mode_0xd9b5d506 = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 30.0,
                "acceleration": 20.0,
                "facing_turn_rate": 1.0,
                "turn_threshold": 181.0,
                "height_variation_max": 1.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8BB1C3A2
        flyer_movement_mode_0x8bb1c3a2 = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 1.0,
                "acceleration": 10.0,
                "turn_threshold": 181.0,
                "height_variation_max": 1.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x389CB515
        stunned = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 5.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 1.0,
                "floor_buffer": 5.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB2DDFAD
        flyer_movement_mode_0xfb2ddfad = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 5.0,
                "acceleration": 10.0,
                "facing_turn_rate": 15.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_min": 1.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC558BC0D
        dash = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "speed": 40.0,
                "acceleration": 100.0,
                "turn_rate": 360.0,
                "turn_threshold": 181.0,
                "avoidance_range": 1.0,
                "height_variation_max": 0.5,
                "floor_buffer": 13.0,
                "ceiling_buffer": 8.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FE13A7B
        flyer_movement_mode_0x5fe13a7b = FlyerMovementMode.from_stream(
            data,
            game,
            property_size,
            default_override={
                "acceleration": 20.0,
                "turn_threshold": 181.0,
                "floor_buffer": 12.0,
                "ceiling_buffer": 12.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFD38A106
        claw = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D7DBEAB
        char_0x4d7dbeab = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA17C09BB
        char_0xa17c09bb = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11DC2DAB
        char_0x11dc2dab = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFDDD9ABB
        char_0xfddd9abb = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC99CEE00
        unknown_0xc99cee00 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2FFC41E1
        unknown_0x2ffc41e1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F5D9AB7
        unknown_0x7f5d9ab7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x993D3556
        unknown_0x993d3556 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08EFEB79
        unknown_0x08efeb79 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEE8F4498
        unknown_0xee8f4498 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC24D8FBD
        unknown_0xc24d8fbd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x242D205C
        unknown_0x242d205c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BDD1E4C
        stun_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DA4A3B0
        electric_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FCD8B66
        sound_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC0AF287
        electric_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3E8EC4E
        sound_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF40A9C9D
        leg_hit_splash = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            hearing_range,
            lose_interest_range,
            lose_interest_time,
            unknown_0xfe4588a1,
            unknown_0xc2688b41,
            unknown_0x7b0cc30d,
            damage_vulnerability,
            body_vulnerability,
            brain_vulnerability,
            brain_x_ray_radius,
            brain_radius,
            leg_vulnerability,
            unknown_0xb9e0c90d,
            unknown_0x81d39802,
            tentacle_regrow_time,
            unknown_0xf79a10b0,
            unknown_0xc550a481,
            unknown_0x95e7a2c2,
            unknown_0x76ba1c18,
            unknown_0xe08106ed,
            unknown_0x88d7c540,
            unknown_0xace62367,
            unknown_0x620b1b3d,
            max_attack_height,
            min_attack_height,
            max_attack_forward,
            min_attack_forward,
            unknown_0x0978b98a,
            unknown_0xcfcd32bb,
            unknown_0x17d71349,
            recheck_path_time,
            recheck_path_distance,
            max_num_metroids,
            auto_spawn,
            max_spawn_delay,
            min_spawn_delay,
            unknown_0x6089191d,
            unknown_0x258b5a9f,
            unknown_0x2ae610e5,
            hatch_chance,
            maya_double,
            unknown_0x3fee1ba4,
            spin_attack_damage,
            max_spin_attack_delay,
            min_spin_attack_delay,
            unknown_0xbeaf2105,
            unknown_0x54ff4d38,
            unknown_0xb29fe2d9,
            dodge_chance,
            unknown_0x42647ad7,
            unknown_0xa404d536,
            unknown_0x248d3599,
            unknown_0xbfd77e62,
            unknown_0xcdaa2c74,
            unknown_0x2bca8395,
            patrol,
            attack_path,
            combat,
            stab_attack,
            flyer_movement_mode_0x6ca56014,
            flyer_movement_mode_0xe20e51c3,
            flyer_movement_mode_0x25a68a0e,
            flyer_movement_mode_0xd9b5d506,
            flyer_movement_mode_0x8bb1c3a2,
            stunned,
            flyer_movement_mode_0xfb2ddfad,
            dash,
            flyer_movement_mode_0x5fe13a7b,
            claw,
            char_0x4d7dbeab,
            char_0xa17c09bb,
            char_0x11dc2dab,
            char_0xfddd9abb,
            unknown_0xc99cee00,
            unknown_0x2ffc41e1,
            unknown_0x7f5d9ab7,
            unknown_0x993d3556,
            unknown_0x08efeb79,
            unknown_0xee8f4498,
            unknown_0xc24d8fbd,
            unknown_0x242d205c,
            stun_threshold,
            electric_ball_effect,
            sound_ball_effect,
            electric_visor_effect,
            sound_visor_effect,
            leg_hit_splash,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00W")  # 87 properties

        data.write(b"%GEP")  # 0x25474550
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_range))

        data.write(b"GO\xa5\x89")  # 0x474fa589
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lose_interest_range))

        data.write(b"\xf8\xb0\xc2\xbb")  # 0xf8b0c2bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lose_interest_time))

        data.write(b"\xfeE\x88\xa1")  # 0xfe4588a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfe4588a1))

        data.write(b"\xc2h\x8bA")  # 0xc2688b41
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc2688b41))

        data.write(b"{\x0c\xc3\r")  # 0x7b0cc30d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7b0cc30d))

        data.write(b"t+36")  # 0x742b3336
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\r\x920\xd1")  # 0xd9230d1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.body_vulnerability.to_stream(data, game)
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

        data.write(b"\x01!\x15\xa2")  # 0x12115a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.brain_x_ray_radius))

        data.write(b"\xa1*D\t")  # 0xa12a4409
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.brain_radius))

        data.write(b"\x9f\x0f\xf8R")  # 0x9f0ff852
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.leg_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb9\xe0\xc9\r")  # 0xb9e0c90d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb9e0c90d))

        data.write(b"\x81\xd3\x98\x02")  # 0x81d39802
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x81d39802))

        data.write(b"\xba\x00-\xcb")  # 0xba002dcb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.tentacle_regrow_time))

        data.write(b"\xf7\x9a\x10\xb0")  # 0xf79a10b0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf79a10b0))

        data.write(b"\xc5P\xa4\x81")  # 0xc550a481
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc550a481))

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b"\xe0\x81\x06\xed")  # 0xe08106ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe08106ed))

        data.write(b"\x88\xd7\xc5@")  # 0x88d7c540
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x88d7c540))

        data.write(b"\xac\xe6#g")  # 0xace62367
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xace62367))

        data.write(b"b\x0b\x1b=")  # 0x620b1b3d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x620b1b3d))

        data.write(b"\xe1\xaeQ\xd8")  # 0xe1ae51d8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_height))

        data.write(b"\xc8\xd0\xac\xc0")  # 0xc8d0acc0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_height))

        data.write(b"\xf3\xe8\x01-")  # 0xf3e8012d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_forward))

        data.write(b"\xe0\xad\xe7\x86")  # 0xe0ade786
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_forward))

        data.write(b"\tx\xb9\x8a")  # 0x978b98a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0978b98a))

        data.write(b"\xcf\xcd2\xbb")  # 0xcfcd32bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcfcd32bb))

        data.write(b"\x17\xd7\x13I")  # 0x17d71349
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x17d71349))

        data.write(b"\x9a\xa9\x0bk")  # 0x9aa90b6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b"v&\xec\x89")  # 0x7626ec89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b"y\x15\xe2\xb3")  # 0x7915e2b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_num_metroids))

        data.write(b"\xcc\xc0\xcf\x92")  # 0xccc0cf92
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_spawn))

        data.write(b"u\xe0\xb0\xa7")  # 0x75e0b0a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_spawn_delay))

        data.write(b"&F\xa8C")  # 0x2646a843
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_spawn_delay))

        data.write(b"`\x89\x19\x1d")  # 0x6089191d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6089191d))

        data.write(b"%\x8bZ\x9f")  # 0x258b5a9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x258b5a9f))

        data.write(b"*\xe6\x10\xe5")  # 0x2ae610e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2ae610e5))

        data.write(b"5K\xae1")  # 0x354bae31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hatch_chance))

        data.write(b"\xf4\xb2\xc8\x01")  # 0xf4b2c801
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maya_double))

        data.write(b"?\xee\x1b\xa4")  # 0x3fee1ba4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3fee1ba4))

        data.write(b"\xcf\xac\xffS")  # 0xcfacff53
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spin_attack_damage.to_stream(data, game, default_override={"di_damage": 30.0, "di_knock_back_power": 20.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"l\xb6\xd8\xc7")  # 0x6cb6d8c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_spin_attack_delay))

        data.write(b"h,\xe9\xed")  # 0x682ce9ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_spin_attack_delay))

        data.write(b"\xbe\xaf!\x05")  # 0xbeaf2105
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbeaf2105))

        data.write(b"T\xffM8")  # 0x54ff4d38
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x54ff4d38))

        data.write(b"\xb2\x9f\xe2\xd9")  # 0xb29fe2d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb29fe2d9))

        data.write(b"G\xbe2\x98")  # 0x47be3298
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b"Bdz\xd7")  # 0x42647ad7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x42647ad7))

        data.write(b"\xa4\x04\xd56")  # 0xa404d536
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa404d536))

        data.write(b"$\x8d5\x99")  # 0x248d3599
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x248d3599))

        data.write(b"\xbf\xd7~b")  # 0xbfd77e62
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbfd77e62))

        data.write(b"\xcd\xaa,t")  # 0xcdaa2c74
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcdaa2c74))

        data.write(b"+\xca\x83\x95")  # 0x2bca8395
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2bca8395))

        data.write(b"\xcc\xdd:\xca")  # 0xccdd3aca
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patrol.to_stream(
            data,
            game,
            default_override={
                "speed": 3.0,
                "acceleration": 1.0,
                "facing_turn_rate": 30.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc8E\xd3\xc0")  # 0xc845d3c0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack_path.to_stream(
            data,
            game,
            default_override={
                "speed": 3.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcc}.\x98")  # 0xcc7d2e98
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.combat.to_stream(
            data,
            game,
            default_override={
                "speed": 3.0,
                "acceleration": 10.0,
                "turn_threshold": 181.0,
                "floor_buffer": 11.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb9\xc3\xdb\x94")  # 0xb9c3db94
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stab_attack.to_stream(
            data,
            game,
            default_override={
                "speed": 0.10000000149011612,
                "acceleration": 10.0,
                "turn_rate": 10800.0,
                "facing_turn_rate": 120.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 0.0,
                "floor_buffer": 8.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"l\xa5`\x14")  # 0x6ca56014
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0x6ca56014.to_stream(
            data,
            game,
            default_override={
                "speed": 30.0,
                "acceleration": 50.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 0.0,
                "floor_buffer": 3.5,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe2\x0eQ\xc3")  # 0xe20e51c3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0xe20e51c3.to_stream(
            data,
            game,
            default_override={
                "speed": 30.0,
                "acceleration": 10.0,
                "facing_turn_rate": 1.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 1.0,
                "floor_buffer": 5.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"%\xa6\x8a\x0e")  # 0x25a68a0e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0x25a68a0e.to_stream(
            data,
            game,
            default_override={
                "speed": 1.0,
                "acceleration": 10.0,
                "turn_threshold": 181.0,
                "height_variation_max": 0.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd9\xb5\xd5\x06")  # 0xd9b5d506
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0xd9b5d506.to_stream(
            data,
            game,
            default_override={
                "speed": 30.0,
                "acceleration": 20.0,
                "facing_turn_rate": 1.0,
                "turn_threshold": 181.0,
                "height_variation_max": 1.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\xb1\xc3\xa2")  # 0x8bb1c3a2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0x8bb1c3a2.to_stream(
            data,
            game,
            default_override={
                "speed": 1.0,
                "acceleration": 10.0,
                "turn_threshold": 181.0,
                "height_variation_max": 1.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"8\x9c\xb5\x15")  # 0x389cb515
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stunned.to_stream(
            data,
            game,
            default_override={
                "speed": 5.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_max": 1.0,
                "floor_buffer": 5.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfb-\xdf\xad")  # 0xfb2ddfad
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0xfb2ddfad.to_stream(
            data,
            game,
            default_override={
                "speed": 5.0,
                "acceleration": 10.0,
                "facing_turn_rate": 15.0,
                "turn_threshold": 181.0,
                "use_avoidance": False,
                "height_variation_min": 1.0,
                "floor_buffer": 10.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5X\xbc\r")  # 0xc558bc0d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dash.to_stream(
            data,
            game,
            default_override={
                "speed": 40.0,
                "acceleration": 100.0,
                "turn_rate": 360.0,
                "turn_threshold": 181.0,
                "avoidance_range": 1.0,
                "height_variation_max": 0.5,
                "floor_buffer": 13.0,
                "ceiling_buffer": 8.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_\xe1:{")  # 0x5fe13a7b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flyer_movement_mode_0x5fe13a7b.to_stream(
            data,
            game,
            default_override={
                "acceleration": 20.0,
                "turn_threshold": 181.0,
                "floor_buffer": 12.0,
                "ceiling_buffer": 12.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfd8\xa1\x06")  # 0xfd38a106
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.claw.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"M}\xbe\xab")  # 0x4d7dbeab
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char_0x4d7dbeab.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa1|\t\xbb")  # 0xa17c09bb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char_0xa17c09bb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x11\xdc-\xab")  # 0x11dc2dab
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char_0x11dc2dab.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfd\xdd\x9a\xbb")  # 0xfddd9abb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char_0xfddd9abb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc9\x9c\xee\x00")  # 0xc99cee00
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc99cee00))

        data.write(b"/\xfcA\xe1")  # 0x2ffc41e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2ffc41e1))

        data.write(b"\x7f]\x9a\xb7")  # 0x7f5d9ab7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7f5d9ab7))

        data.write(b"\x99=5V")  # 0x993d3556
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x993d3556))

        data.write(b"\x08\xef\xeby")  # 0x8efeb79
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x08efeb79))

        data.write(b"\xee\x8fD\x98")  # 0xee8f4498
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xee8f4498))

        data.write(b"\xc2M\x8f\xbd")  # 0xc24d8fbd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc24d8fbd))

        data.write(b"$- \\")  # 0x242d205c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x242d205c))

        data.write(b"[\xdd\x1eL")  # 0x5bdd1e4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_threshold))

        data.write(b"m\xa4\xa3\xb0")  # 0x6da4a3b0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.electric_ball_effect))

        data.write(b"?\xcd\x8bf")  # 0x3fcd8b66
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_ball_effect))

        data.write(b"\xcc\n\xf2\x87")  # 0xcc0af287
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.electric_visor_effect))

        data.write(b"\xa3\xe8\xecN")  # 0xa3e8ec4e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_visor_effect))

        data.write(b"\xf4\n\x9c\x9d")  # 0xf40a9c9d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.leg_hit_splash))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidHatcherDataJson", data)
        return cls(
            hearing_range=json_data["hearing_range"],
            lose_interest_range=json_data["lose_interest_range"],
            lose_interest_time=json_data["lose_interest_time"],
            unknown_0xfe4588a1=json_data["unknown_0xfe4588a1"],
            unknown_0xc2688b41=json_data["unknown_0xc2688b41"],
            unknown_0x7b0cc30d=json_data["unknown_0x7b0cc30d"],
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
            body_vulnerability=DamageVulnerability.from_json(json_data["body_vulnerability"]),
            brain_vulnerability=DamageVulnerability.from_json(json_data["brain_vulnerability"]),
            brain_x_ray_radius=json_data["brain_x_ray_radius"],
            brain_radius=json_data["brain_radius"],
            leg_vulnerability=DamageVulnerability.from_json(json_data["leg_vulnerability"]),
            unknown_0xb9e0c90d=json_data["unknown_0xb9e0c90d"],
            unknown_0x81d39802=json_data["unknown_0x81d39802"],
            tentacle_regrow_time=json_data["tentacle_regrow_time"],
            unknown_0xf79a10b0=json_data["unknown_0xf79a10b0"],
            unknown_0xc550a481=json_data["unknown_0xc550a481"],
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0xe08106ed=json_data["unknown_0xe08106ed"],
            unknown_0x88d7c540=json_data["unknown_0x88d7c540"],
            unknown_0xace62367=json_data["unknown_0xace62367"],
            unknown_0x620b1b3d=json_data["unknown_0x620b1b3d"],
            max_attack_height=json_data["max_attack_height"],
            min_attack_height=json_data["min_attack_height"],
            max_attack_forward=json_data["max_attack_forward"],
            min_attack_forward=json_data["min_attack_forward"],
            unknown_0x0978b98a=json_data["unknown_0x0978b98a"],
            unknown_0xcfcd32bb=json_data["unknown_0xcfcd32bb"],
            unknown_0x17d71349=json_data["unknown_0x17d71349"],
            recheck_path_time=json_data["recheck_path_time"],
            recheck_path_distance=json_data["recheck_path_distance"],
            max_num_metroids=json_data["max_num_metroids"],
            auto_spawn=json_data["auto_spawn"],
            max_spawn_delay=json_data["max_spawn_delay"],
            min_spawn_delay=json_data["min_spawn_delay"],
            unknown_0x6089191d=json_data["unknown_0x6089191d"],
            unknown_0x258b5a9f=json_data["unknown_0x258b5a9f"],
            unknown_0x2ae610e5=json_data["unknown_0x2ae610e5"],
            hatch_chance=json_data["hatch_chance"],
            maya_double=json_data["maya_double"],
            unknown_0x3fee1ba4=json_data["unknown_0x3fee1ba4"],
            spin_attack_damage=DamageInfo.from_json(json_data["spin_attack_damage"]),
            max_spin_attack_delay=json_data["max_spin_attack_delay"],
            min_spin_attack_delay=json_data["min_spin_attack_delay"],
            unknown_0xbeaf2105=json_data["unknown_0xbeaf2105"],
            unknown_0x54ff4d38=json_data["unknown_0x54ff4d38"],
            unknown_0xb29fe2d9=json_data["unknown_0xb29fe2d9"],
            dodge_chance=json_data["dodge_chance"],
            unknown_0x42647ad7=json_data["unknown_0x42647ad7"],
            unknown_0xa404d536=json_data["unknown_0xa404d536"],
            unknown_0x248d3599=json_data["unknown_0x248d3599"],
            unknown_0xbfd77e62=json_data["unknown_0xbfd77e62"],
            unknown_0xcdaa2c74=json_data["unknown_0xcdaa2c74"],
            unknown_0x2bca8395=json_data["unknown_0x2bca8395"],
            patrol=FlyerMovementMode.from_json(json_data["patrol"]),
            attack_path=FlyerMovementMode.from_json(json_data["attack_path"]),
            combat=FlyerMovementMode.from_json(json_data["combat"]),
            stab_attack=FlyerMovementMode.from_json(json_data["stab_attack"]),
            flyer_movement_mode_0x6ca56014=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0x6ca56014"]),
            flyer_movement_mode_0xe20e51c3=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0xe20e51c3"]),
            flyer_movement_mode_0x25a68a0e=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0x25a68a0e"]),
            flyer_movement_mode_0xd9b5d506=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0xd9b5d506"]),
            flyer_movement_mode_0x8bb1c3a2=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0x8bb1c3a2"]),
            stunned=FlyerMovementMode.from_json(json_data["stunned"]),
            flyer_movement_mode_0xfb2ddfad=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0xfb2ddfad"]),
            dash=FlyerMovementMode.from_json(json_data["dash"]),
            flyer_movement_mode_0x5fe13a7b=FlyerMovementMode.from_json(json_data["flyer_movement_mode_0x5fe13a7b"]),
            claw=AnimationParameters.from_json(json_data["claw"]),
            char_0x4d7dbeab=AnimationParameters.from_json(json_data["char_0x4d7dbeab"]),
            char_0xa17c09bb=AnimationParameters.from_json(json_data["char_0xa17c09bb"]),
            char_0x11dc2dab=AnimationParameters.from_json(json_data["char_0x11dc2dab"]),
            char_0xfddd9abb=AnimationParameters.from_json(json_data["char_0xfddd9abb"]),
            unknown_0xc99cee00=json_data["unknown_0xc99cee00"],
            unknown_0x2ffc41e1=json_data["unknown_0x2ffc41e1"],
            unknown_0x7f5d9ab7=json_data["unknown_0x7f5d9ab7"],
            unknown_0x993d3556=json_data["unknown_0x993d3556"],
            unknown_0x08efeb79=json_data["unknown_0x08efeb79"],
            unknown_0xee8f4498=json_data["unknown_0xee8f4498"],
            unknown_0xc24d8fbd=json_data["unknown_0xc24d8fbd"],
            unknown_0x242d205c=json_data["unknown_0x242d205c"],
            stun_threshold=json_data["stun_threshold"],
            electric_ball_effect=json_data["electric_ball_effect"],
            sound_ball_effect=json_data["sound_ball_effect"],
            electric_visor_effect=json_data["electric_visor_effect"],
            sound_visor_effect=json_data["sound_visor_effect"],
            leg_hit_splash=json_data["leg_hit_splash"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hearing_range": self.hearing_range,
            "lose_interest_range": self.lose_interest_range,
            "lose_interest_time": self.lose_interest_time,
            "unknown_0xfe4588a1": self.unknown_0xfe4588a1,
            "unknown_0xc2688b41": self.unknown_0xc2688b41,
            "unknown_0x7b0cc30d": self.unknown_0x7b0cc30d,
            "damage_vulnerability": self.damage_vulnerability.to_json(),
            "body_vulnerability": self.body_vulnerability.to_json(),
            "brain_vulnerability": self.brain_vulnerability.to_json(),
            "brain_x_ray_radius": self.brain_x_ray_radius,
            "brain_radius": self.brain_radius,
            "leg_vulnerability": self.leg_vulnerability.to_json(),
            "unknown_0xb9e0c90d": self.unknown_0xb9e0c90d,
            "unknown_0x81d39802": self.unknown_0x81d39802,
            "tentacle_regrow_time": self.tentacle_regrow_time,
            "unknown_0xf79a10b0": self.unknown_0xf79a10b0,
            "unknown_0xc550a481": self.unknown_0xc550a481,
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0xe08106ed": self.unknown_0xe08106ed,
            "unknown_0x88d7c540": self.unknown_0x88d7c540,
            "unknown_0xace62367": self.unknown_0xace62367,
            "unknown_0x620b1b3d": self.unknown_0x620b1b3d,
            "max_attack_height": self.max_attack_height,
            "min_attack_height": self.min_attack_height,
            "max_attack_forward": self.max_attack_forward,
            "min_attack_forward": self.min_attack_forward,
            "unknown_0x0978b98a": self.unknown_0x0978b98a,
            "unknown_0xcfcd32bb": self.unknown_0xcfcd32bb,
            "unknown_0x17d71349": self.unknown_0x17d71349,
            "recheck_path_time": self.recheck_path_time,
            "recheck_path_distance": self.recheck_path_distance,
            "max_num_metroids": self.max_num_metroids,
            "auto_spawn": self.auto_spawn,
            "max_spawn_delay": self.max_spawn_delay,
            "min_spawn_delay": self.min_spawn_delay,
            "unknown_0x6089191d": self.unknown_0x6089191d,
            "unknown_0x258b5a9f": self.unknown_0x258b5a9f,
            "unknown_0x2ae610e5": self.unknown_0x2ae610e5,
            "hatch_chance": self.hatch_chance,
            "maya_double": self.maya_double,
            "unknown_0x3fee1ba4": self.unknown_0x3fee1ba4,
            "spin_attack_damage": self.spin_attack_damage.to_json(),
            "max_spin_attack_delay": self.max_spin_attack_delay,
            "min_spin_attack_delay": self.min_spin_attack_delay,
            "unknown_0xbeaf2105": self.unknown_0xbeaf2105,
            "unknown_0x54ff4d38": self.unknown_0x54ff4d38,
            "unknown_0xb29fe2d9": self.unknown_0xb29fe2d9,
            "dodge_chance": self.dodge_chance,
            "unknown_0x42647ad7": self.unknown_0x42647ad7,
            "unknown_0xa404d536": self.unknown_0xa404d536,
            "unknown_0x248d3599": self.unknown_0x248d3599,
            "unknown_0xbfd77e62": self.unknown_0xbfd77e62,
            "unknown_0xcdaa2c74": self.unknown_0xcdaa2c74,
            "unknown_0x2bca8395": self.unknown_0x2bca8395,
            "patrol": self.patrol.to_json(),
            "attack_path": self.attack_path.to_json(),
            "combat": self.combat.to_json(),
            "stab_attack": self.stab_attack.to_json(),
            "flyer_movement_mode_0x6ca56014": self.flyer_movement_mode_0x6ca56014.to_json(),
            "flyer_movement_mode_0xe20e51c3": self.flyer_movement_mode_0xe20e51c3.to_json(),
            "flyer_movement_mode_0x25a68a0e": self.flyer_movement_mode_0x25a68a0e.to_json(),
            "flyer_movement_mode_0xd9b5d506": self.flyer_movement_mode_0xd9b5d506.to_json(),
            "flyer_movement_mode_0x8bb1c3a2": self.flyer_movement_mode_0x8bb1c3a2.to_json(),
            "stunned": self.stunned.to_json(),
            "flyer_movement_mode_0xfb2ddfad": self.flyer_movement_mode_0xfb2ddfad.to_json(),
            "dash": self.dash.to_json(),
            "flyer_movement_mode_0x5fe13a7b": self.flyer_movement_mode_0x5fe13a7b.to_json(),
            "claw": self.claw.to_json(),
            "char_0x4d7dbeab": self.char_0x4d7dbeab.to_json(),
            "char_0xa17c09bb": self.char_0xa17c09bb.to_json(),
            "char_0x11dc2dab": self.char_0x11dc2dab.to_json(),
            "char_0xfddd9abb": self.char_0xfddd9abb.to_json(),
            "unknown_0xc99cee00": self.unknown_0xc99cee00,
            "unknown_0x2ffc41e1": self.unknown_0x2ffc41e1,
            "unknown_0x7f5d9ab7": self.unknown_0x7f5d9ab7,
            "unknown_0x993d3556": self.unknown_0x993d3556,
            "unknown_0x08efeb79": self.unknown_0x08efeb79,
            "unknown_0xee8f4498": self.unknown_0xee8f4498,
            "unknown_0xc24d8fbd": self.unknown_0xc24d8fbd,
            "unknown_0x242d205c": self.unknown_0x242d205c,
            "stun_threshold": self.stun_threshold,
            "electric_ball_effect": self.electric_ball_effect,
            "sound_ball_effect": self.sound_ball_effect,
            "electric_visor_effect": self.electric_visor_effect,
            "sound_visor_effect": self.sound_visor_effect,
            "leg_hit_splash": self.leg_hit_splash,
        }


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_body_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_brain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_leg_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_spin_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_damage": 30.0, "di_knock_back_power": 20.0}
    )


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 3.0,
            "acceleration": 1.0,
            "facing_turn_rate": 30.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "floor_buffer": 10.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_attack_path(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 3.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "floor_buffer": 10.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_combat(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 3.0,
            "acceleration": 10.0,
            "turn_threshold": 181.0,
            "floor_buffer": 11.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_stab_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 0.10000000149011612,
            "acceleration": 10.0,
            "turn_rate": 10800.0,
            "facing_turn_rate": 120.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "height_variation_max": 0.0,
            "floor_buffer": 8.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0x6ca56014(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 30.0,
            "acceleration": 50.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "height_variation_max": 0.0,
            "floor_buffer": 3.5,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0xe20e51c3(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 30.0,
            "acceleration": 10.0,
            "facing_turn_rate": 1.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "height_variation_max": 1.0,
            "floor_buffer": 5.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0x25a68a0e(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 1.0,
            "acceleration": 10.0,
            "turn_threshold": 181.0,
            "height_variation_max": 0.0,
            "floor_buffer": 10.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0xd9b5d506(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 30.0,
            "acceleration": 20.0,
            "facing_turn_rate": 1.0,
            "turn_threshold": 181.0,
            "height_variation_max": 1.0,
            "floor_buffer": 10.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0x8bb1c3a2(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 1.0,
            "acceleration": 10.0,
            "turn_threshold": 181.0,
            "height_variation_max": 1.0,
            "floor_buffer": 10.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_stunned(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 5.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "height_variation_max": 1.0,
            "floor_buffer": 5.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0xfb2ddfad(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 5.0,
            "acceleration": 10.0,
            "facing_turn_rate": 15.0,
            "turn_threshold": 181.0,
            "use_avoidance": False,
            "height_variation_min": 1.0,
            "floor_buffer": 10.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_dash(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={
            "speed": 40.0,
            "acceleration": 100.0,
            "turn_rate": 360.0,
            "turn_threshold": 181.0,
            "avoidance_range": 1.0,
            "height_variation_max": 0.5,
            "floor_buffer": 13.0,
            "ceiling_buffer": 8.0,
        },
    )


def _decode_flyer_movement_mode_0x5fe13a7b(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(
        data,
        game,
        property_size,
        default_override={"acceleration": 20.0, "turn_threshold": 181.0, "floor_buffer": 12.0, "ceiling_buffer": 12.0},
    )


def _decode_claw(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_char_0x4d7dbeab(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_char_0xa17c09bb(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_char_0x11dc2dab(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_char_0xfddd9abb(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x25474550: ("hearing_range", structs.decode_BIG_f),
    0x474FA589: ("lose_interest_range", structs.decode_BIG_f),
    0xF8B0C2BB: ("lose_interest_time", structs.decode_BIG_f),
    0xFE4588A1: ("unknown_0xfe4588a1", structs.decode_BIG_f),
    0xC2688B41: ("unknown_0xc2688b41", structs.decode_BIG_f),
    0x7B0CC30D: ("unknown_0x7b0cc30d", structs.decode_BIG_f),
    0x742B3336: ("damage_vulnerability", _decode_damage_vulnerability),
    0x0D9230D1: ("body_vulnerability", _decode_body_vulnerability),
    0x243AB10D: ("brain_vulnerability", _decode_brain_vulnerability),
    0x012115A2: ("brain_x_ray_radius", structs.decode_BIG_f),
    0xA12A4409: ("brain_radius", structs.decode_BIG_f),
    0x9F0FF852: ("leg_vulnerability", _decode_leg_vulnerability),
    0xB9E0C90D: ("unknown_0xb9e0c90d", structs.decode_BIG_f),
    0x81D39802: ("unknown_0x81d39802", structs.decode_BIG_f),
    0xBA002DCB: ("tentacle_regrow_time", structs.decode_BIG_f),
    0xF79A10B0: ("unknown_0xf79a10b0", structs.decode_BIG_f),
    0xC550A481: ("unknown_0xc550a481", structs.decode_BIG_f),
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0xE08106ED: ("unknown_0xe08106ed", structs.decode_BIG_f),
    0x88D7C540: ("unknown_0x88d7c540", structs.decode_BIG_f),
    0xACE62367: ("unknown_0xace62367", structs.decode_BIG_f),
    0x620B1B3D: ("unknown_0x620b1b3d", structs.decode_BIG_f),
    0xE1AE51D8: ("max_attack_height", structs.decode_BIG_f),
    0xC8D0ACC0: ("min_attack_height", structs.decode_BIG_f),
    0xF3E8012D: ("max_attack_forward", structs.decode_BIG_f),
    0xE0ADE786: ("min_attack_forward", structs.decode_BIG_f),
    0x0978B98A: ("unknown_0x0978b98a", structs.decode_BIG_f),
    0xCFCD32BB: ("unknown_0xcfcd32bb", structs.decode_BIG_f),
    0x17D71349: ("unknown_0x17d71349", structs.decode_BIG_f),
    0x9AA90B6B: ("recheck_path_time", structs.decode_BIG_f),
    0x7626EC89: ("recheck_path_distance", structs.decode_BIG_f),
    0x7915E2B3: ("max_num_metroids", structs.decode_BIG_l),
    0xCCC0CF92: ("auto_spawn", structs.decode_BIG_bool_),
    0x75E0B0A7: ("max_spawn_delay", structs.decode_BIG_f),
    0x2646A843: ("min_spawn_delay", structs.decode_BIG_f),
    0x6089191D: ("unknown_0x6089191d", structs.decode_BIG_l),
    0x258B5A9F: ("unknown_0x258b5a9f", structs.decode_BIG_l),
    0x2AE610E5: ("unknown_0x2ae610e5", structs.decode_BIG_f),
    0x354BAE31: ("hatch_chance", structs.decode_BIG_f),
    0xF4B2C801: ("maya_double", structs.decode_BIG_f),
    0x3FEE1BA4: ("unknown_0x3fee1ba4", structs.decode_BIG_f),
    0xCFACFF53: ("spin_attack_damage", _decode_spin_attack_damage),
    0x6CB6D8C7: ("max_spin_attack_delay", structs.decode_BIG_f),
    0x682CE9ED: ("min_spin_attack_delay", structs.decode_BIG_f),
    0xBEAF2105: ("unknown_0xbeaf2105", structs.decode_BIG_f),
    0x54FF4D38: ("unknown_0x54ff4d38", structs.decode_BIG_f),
    0xB29FE2D9: ("unknown_0xb29fe2d9", structs.decode_BIG_f),
    0x47BE3298: ("dodge_chance", structs.decode_BIG_f),
    0x42647AD7: ("unknown_0x42647ad7", structs.decode_BIG_f),
    0xA404D536: ("unknown_0xa404d536", structs.decode_BIG_f),
    0x248D3599: ("unknown_0x248d3599", structs.decode_BIG_f),
    0xBFD77E62: ("unknown_0xbfd77e62", structs.decode_BIG_f),
    0xCDAA2C74: ("unknown_0xcdaa2c74", structs.decode_BIG_f),
    0x2BCA8395: ("unknown_0x2bca8395", structs.decode_BIG_f),
    0xCCDD3ACA: ("patrol", _decode_patrol),
    0xC845D3C0: ("attack_path", _decode_attack_path),
    0xCC7D2E98: ("combat", _decode_combat),
    0xB9C3DB94: ("stab_attack", _decode_stab_attack),
    0x6CA56014: ("flyer_movement_mode_0x6ca56014", _decode_flyer_movement_mode_0x6ca56014),
    0xE20E51C3: ("flyer_movement_mode_0xe20e51c3", _decode_flyer_movement_mode_0xe20e51c3),
    0x25A68A0E: ("flyer_movement_mode_0x25a68a0e", _decode_flyer_movement_mode_0x25a68a0e),
    0xD9B5D506: ("flyer_movement_mode_0xd9b5d506", _decode_flyer_movement_mode_0xd9b5d506),
    0x8BB1C3A2: ("flyer_movement_mode_0x8bb1c3a2", _decode_flyer_movement_mode_0x8bb1c3a2),
    0x389CB515: ("stunned", _decode_stunned),
    0xFB2DDFAD: ("flyer_movement_mode_0xfb2ddfad", _decode_flyer_movement_mode_0xfb2ddfad),
    0xC558BC0D: ("dash", _decode_dash),
    0x5FE13A7B: ("flyer_movement_mode_0x5fe13a7b", _decode_flyer_movement_mode_0x5fe13a7b),
    0xFD38A106: ("claw", _decode_claw),
    0x4D7DBEAB: ("char_0x4d7dbeab", _decode_char_0x4d7dbeab),
    0xA17C09BB: ("char_0xa17c09bb", _decode_char_0xa17c09bb),
    0x11DC2DAB: ("char_0x11dc2dab", _decode_char_0x11dc2dab),
    0xFDDD9ABB: ("char_0xfddd9abb", _decode_char_0xfddd9abb),
    0xC99CEE00: ("unknown_0xc99cee00", structs.decode_BIG_f),
    0x2FFC41E1: ("unknown_0x2ffc41e1", structs.decode_BIG_f),
    0x7F5D9AB7: ("unknown_0x7f5d9ab7", structs.decode_BIG_f),
    0x993D3556: ("unknown_0x993d3556", structs.decode_BIG_f),
    0x08EFEB79: ("unknown_0x08efeb79", structs.decode_BIG_f),
    0xEE8F4498: ("unknown_0xee8f4498", structs.decode_BIG_f),
    0xC24D8FBD: ("unknown_0xc24d8fbd", structs.decode_BIG_f),
    0x242D205C: ("unknown_0x242d205c", structs.decode_BIG_f),
    0x5BDD1E4C: ("stun_threshold", structs.decode_BIG_f),
    0x6DA4A3B0: ("electric_ball_effect", structs.decode_BIG_Q),
    0x3FCD8B66: ("sound_ball_effect", structs.decode_BIG_Q),
    0xCC0AF287: ("electric_visor_effect", structs.decode_BIG_Q),
    0xA3E8EC4E: ("sound_visor_effect", structs.decode_BIG_Q),
    0xF40A9C9D: ("leg_hit_splash", structs.decode_BIG_Q),
}
