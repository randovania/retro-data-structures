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
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.SpacePirateStruct import SpacePirateStruct
from retro_data_structures.properties.corruption.archetypes.SpacePirateWeaponData import SpacePirateWeaponData
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SpacePirateDataJson(typing_extensions.TypedDict):
        attack_behavior: int
        can_interrupt_tasks: bool
        warp_in: bool
        unknown_0x87929c41: bool
        unknown_0x9a0ce9b2: bool
        unknown_0x4d61342a: bool
        initial_taunt_chance: float
        combat_taunt_chance: float
        instant_attack: bool
        unknown_0x97c95a99: bool
        aggressiveness: float
        cover_check: float
        search_radius: float
        hearing_radius: float
        approach_radius: float
        unknown_0x733da88a: float
        unknown_0x03fdbe4a: bool
        dodge_check: float
        unknown_0x4ead288e: float
        no_backing_up: bool
        no_knockback_movement: bool
        no_melee_attack: bool
        blade_damage: json_util.JsonObject
        unknown_0x71587b45: float
        unknown_0x7903312e: float
        unknown_0x1b454a27: int
        gun_track_delay: float
        unknown_0x615bb850: int
        unknown_0x7b1f1541: int
        has_cloak: bool
        cloak_opacity: float
        cloak_time: float
        decloak_time: float
        cover_cloak_chance: float
        melee_cloak_chance: float
        can_combat_teleport: bool
        min_teleport_dist: float
        min_teleport_time: float
        unknown_0x2eb81206: float
        unknown_0x02e75b93: float
        unknown_0x0881a3b5: bool
        unknown_0x38b6452e: bool
        unknown_0xe3794994: float
        unknown_0x54f66da0: float
        unknown_0x506c5c8a: float
        unknown_0x159f33d6: float
        unknown_0x0524bc7e: json_util.JsonValue
        unknown_0x256b394f: json_util.JsonValue
        unknown_0x824db7ce: float
        unknown_0xe527cde8: bool
        unknown_0x61e801d4: float
        unknown_0xf19b113e: float
        unknown_0x80c6880f: float
        unknown_0x08358a6a: float
        unknown_0xa00204b0: float
        unknown_0x0806c08d: float
        unknown_0x17db0cf2: float
        sound_alert: int
        sound_hurled: int
        sound_death: int
        unknown_0x8a36b5d5: int
        unknown_0x34e20697: float
        grenade_data: json_util.JsonObject
        space_pirate_struct_0x4fdab367: json_util.JsonObject
        space_pirate_struct_0x37212693: json_util.JsonObject
        space_pirate_struct_0x91b4cb73: json_util.JsonObject
        has_shield: bool
        unknown_0x4aee5c47: bool
        shield_vulnerability: json_util.JsonObject
        hyper_shield_vulnerability: json_util.JsonObject
        unknown_0x0d1d1648: float
        char: json_util.JsonObject
        grapple_data: json_util.JsonObject
        shield_busted_scan_info: int
        has_armor: bool
        armor_health: json_util.JsonObject
        armor_vulnerability: json_util.JsonObject
        head_armor_vulnerability: json_util.JsonObject
        armor_broken_model: int
        armor_broken_skin_rules: int
        head_armor_model: int
        collar_armor_model: int
        left_collar_armor_model: int
        right_collar_armor_model: int
        spine1_armor_model: int
        spine2_armor_model: int
        left_hip_armor_model: int
        right_hip_armor_model: int
        skeleton_root_armor_model: int
        is_gandrayda: bool
        unknown_0x040a4edf: int
        unknown_0x5c572665: int
        unknown_0xcca41d93: float
        unknown_0x767f168e: bool
        keep_target_time: float
        unknown_0x668ec0a0: float
        unknown_0x14950f43: float
        unknown_0x761ed7af: int


@dataclasses.dataclass()
class SpacePirateData(BaseProperty):
    attack_behavior: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8E1E1586, original_name="AttackBehavior"),
        },
    )
    can_interrupt_tasks: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA40CB847, original_name="CanInterruptTasks"),
        },
    )
    warp_in: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7428A29F, original_name="WarpIn"),
        },
    )
    unknown_0x87929c41: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x87929C41, original_name="Unknown"),
        },
    )
    unknown_0x9a0ce9b2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9A0CE9B2, original_name="Unknown"),
        },
    )
    unknown_0x4d61342a: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4D61342A, original_name="Unknown"),
        },
    )
    initial_taunt_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2D8264EA, original_name="InitialTauntChance"),
        },
    )
    combat_taunt_chance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA6AF0C57, original_name="CombatTauntChance"),
        },
    )
    instant_attack: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6697712A, original_name="InstantAttack"),
        },
    )
    unknown_0x97c95a99: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x97C95A99, original_name="Unknown"),
        },
    )
    aggressiveness: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9579B1F2, original_name="Aggressiveness"),
        },
    )
    cover_check: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF89AB419, original_name="CoverCheck"),
        },
    )
    search_radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED9BF5A3, original_name="SearchRadius"),
        },
    )
    hearing_radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED69488F, original_name="HearingRadius"),
        },
    )
    approach_radius: float = dataclasses.field(
        default=1000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3CB99B1E, original_name="ApproachRadius"),
        },
    )
    unknown_0x733da88a: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x733DA88A, original_name="Unknown"),
        },
    )
    unknown_0x03fdbe4a: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x03FDBE4A, original_name="Unknown"),
        },
    )
    dodge_check: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC36E745, original_name="DodgeCheck"),
        },
    )
    unknown_0x4ead288e: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4EAD288E, original_name="Unknown"),
        },
    )
    no_backing_up: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF11EC8EE, original_name="NoBackingUp"),
        },
    )
    no_knockback_movement: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x808576EE, original_name="NoKnockbackMovement"),
        },
    )
    no_melee_attack: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6BC22735, original_name="NoMeleeAttack"),
        },
    )
    blade_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xA5912430,
                original_name="BladeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x71587b45: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x71587B45, original_name="Unknown"),
        },
    )
    unknown_0x7903312e: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7903312E, original_name="Unknown"),
        },
    )
    unknown_0x1b454a27: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1B454A27, original_name="Unknown"),
        },
    )
    gun_track_delay: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB2AC2D96, original_name="GunTrackDelay"),
        },
    )
    unknown_0x615bb850: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x615BB850, original_name="Unknown"),
        },
    )
    unknown_0x7b1f1541: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7B1F1541, original_name="Unknown"),
        },
    )
    has_cloak: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7A4B4AEA, original_name="HasCloak"),
        },
    )
    cloak_opacity: float = dataclasses.field(
        default=0.02500000037252903,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BC6F1D5, original_name="CloakOpacity"),
        },
    )
    cloak_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x388BC31F, original_name="CloakTime"),
        },
    )
    decloak_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4319C840, original_name="DecloakTime"),
        },
    )
    cover_cloak_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8AA60B6C, original_name="CoverCloakChance"),
        },
    )
    melee_cloak_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x57E862AA, original_name="MeleeCloakChance"),
        },
    )
    can_combat_teleport: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFCD4ED64, original_name="CanCombatTeleport"),
        },
    )
    min_teleport_dist: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFAA81D3A, original_name="MinTeleportDist"),
        },
    )
    min_teleport_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA90369E6, original_name="MinTeleportTime"),
        },
    )
    unknown_0x2eb81206: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2EB81206, original_name="Unknown"),
        },
    )
    unknown_0x02e75b93: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x02E75B93, original_name="Unknown"),
        },
    )
    unknown_0x0881a3b5: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0881A3B5, original_name="Unknown"),
        },
    )
    unknown_0x38b6452e: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x38B6452E, original_name="Unknown"),
        },
    )
    unknown_0xe3794994: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE3794994, original_name="Unknown"),
        },
    )
    unknown_0x54f66da0: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54F66DA0, original_name="Unknown"),
        },
    )
    unknown_0x506c5c8a: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x506C5C8A, original_name="Unknown"),
        },
    )
    unknown_0x159f33d6: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x159F33D6, original_name="Unknown"),
        },
    )
    unknown_0x0524bc7e: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x0524BC7E, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0x256b394f: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x256B394F, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0x824db7ce: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x824DB7CE, original_name="Unknown"),
        },
    )
    unknown_0xe527cde8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE527CDE8, original_name="Unknown"),
        },
    )
    unknown_0x61e801d4: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61E801D4, original_name="Unknown"),
        },
    )
    unknown_0xf19b113e: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF19B113E, original_name="Unknown"),
        },
    )
    unknown_0x80c6880f: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x80C6880F, original_name="Unknown"),
        },
    )
    unknown_0x08358a6a: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08358A6A, original_name="Unknown"),
        },
    )
    unknown_0xa00204b0: float = dataclasses.field(
        default=16.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA00204B0, original_name="Unknown"),
        },
    )
    unknown_0x0806c08d: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0806C08D, original_name="Unknown"),
        },
    )
    unknown_0x17db0cf2: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17DB0CF2, original_name="Unknown"),
        },
    )
    sound_alert: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC245A874, original_name="Sound_Alert"),
        },
    )
    sound_hurled: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC192E357, original_name="Sound_Hurled"),
        },
    )
    sound_death: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1B412C4B, original_name="Sound_Death"),
        },
    )
    unknown_0x8a36b5d5: int = dataclasses.field(
        default=10000,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8A36B5D5, original_name="Unknown"),
        },
    )
    unknown_0x34e20697: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x34E20697, original_name="Unknown"),
        },
    )
    grenade_data: SpacePirateWeaponData = dataclasses.field(
        default_factory=SpacePirateWeaponData,
        metadata={
            "reflection": FieldReflection[SpacePirateWeaponData](
                SpacePirateWeaponData,
                id=0xC3B6103B,
                original_name="GrenadeData",
                from_json=SpacePirateWeaponData.from_json,
                to_json=SpacePirateWeaponData.to_json,
            ),
        },
    )
    space_pirate_struct_0x4fdab367: SpacePirateStruct = dataclasses.field(
        default_factory=SpacePirateStruct,
        metadata={
            "reflection": FieldReflection[SpacePirateStruct](
                SpacePirateStruct,
                id=0x4FDAB367,
                original_name="SpacePirateStruct",
                from_json=SpacePirateStruct.from_json,
                to_json=SpacePirateStruct.to_json,
            ),
        },
    )
    space_pirate_struct_0x37212693: SpacePirateStruct = dataclasses.field(
        default_factory=SpacePirateStruct,
        metadata={
            "reflection": FieldReflection[SpacePirateStruct](
                SpacePirateStruct,
                id=0x37212693,
                original_name="SpacePirateStruct",
                from_json=SpacePirateStruct.from_json,
                to_json=SpacePirateStruct.to_json,
            ),
        },
    )
    space_pirate_struct_0x91b4cb73: SpacePirateStruct = dataclasses.field(
        default_factory=SpacePirateStruct,
        metadata={
            "reflection": FieldReflection[SpacePirateStruct](
                SpacePirateStruct,
                id=0x91B4CB73,
                original_name="SpacePirateStruct",
                from_json=SpacePirateStruct.from_json,
                to_json=SpacePirateStruct.to_json,
            ),
        },
    )
    has_shield: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x07C1DE29, original_name="HasShield"),
        },
    )
    unknown_0x4aee5c47: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4AEE5C47, original_name="Unknown"),
        },
    )
    shield_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xD34F1323,
                original_name="ShieldVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    hyper_shield_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x8255F594,
                original_name="HyperShieldVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0x0d1d1648: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D1D1648, original_name="Unknown"),
        },
    )
    char: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xC699AD35,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    grapple_data: GrappleData = dataclasses.field(
        default_factory=GrappleData,
        metadata={
            "reflection": FieldReflection[GrappleData](
                GrappleData,
                id=0xBE1AFBC0,
                original_name="GrappleData",
                from_json=GrappleData.from_json,
                to_json=GrappleData.to_json,
            ),
        },
    )
    shield_busted_scan_info: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x71E83F06, original_name="ShieldBustedScanInfo"),
        },
    )
    has_armor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFDE9C4DF, original_name="HasArmor"),
        },
    )
    armor_health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xF18384D4,
                original_name="ArmorHealth",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    armor_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x896D5BD9,
                original_name="ArmorVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    head_armor_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xC13A3E1F,
                original_name="HeadArmorVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    armor_broken_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7579CC86, original_name="ArmorBrokenModel"),
        },
    )
    armor_broken_skin_rules: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x65D86552, original_name="ArmorBrokenSkinRules"),
        },
    )
    head_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x68002BD7, original_name="HeadArmorModel"),
        },
    )
    collar_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAD315C7C, original_name="CollarArmorModel"),
        },
    )
    left_collar_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x042A25ED, original_name="LeftCollarArmorModel"),
        },
    )
    right_collar_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE39B8B1E, original_name="RightCollarArmorModel"),
        },
    )
    spine1_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x356C166A, original_name="Spine1ArmorModel"),
        },
    )
    spine2_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1CA4A298, original_name="Spine2ArmorModel"),
        },
    )
    left_hip_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDF44507E, original_name="LeftHipArmorModel"),
        },
    )
    right_hip_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD2C9A656, original_name="RightHipArmorModel"),
        },
    )
    skeleton_root_armor_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD4E26A8E, original_name="SkeletonRootArmorModel"),
        },
    )
    is_gandrayda: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x531A8C85, original_name="IsGandrayda"),
        },
    )
    unknown_0x040a4edf: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x040A4EDF, original_name="Unknown"),
        },
    )
    unknown_0x5c572665: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5C572665, original_name="Unknown"),
        },
    )
    unknown_0xcca41d93: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCCA41D93, original_name="Unknown"),
        },
    )
    unknown_0x767f168e: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x767F168E, original_name="Unknown"),
        },
    )
    keep_target_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x89A5EDC8, original_name="KeepTargetTime"),
        },
    )
    unknown_0x668ec0a0: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x668EC0A0, original_name="Unknown"),
        },
    )
    unknown_0x14950f43: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14950F43, original_name="Unknown"),
        },
    )
    unknown_0x761ed7af: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x761ED7AF, original_name="Unknown"),
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
        if property_count != 98:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E1E1586
        attack_behavior = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA40CB847
        can_interrupt_tasks = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7428A29F
        warp_in = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87929C41
        unknown_0x87929c41 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A0CE9B2
        unknown_0x9a0ce9b2 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D61342A
        unknown_0x4d61342a = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D8264EA
        initial_taunt_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6AF0C57
        combat_taunt_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6697712A
        instant_attack = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97C95A99
        unknown_0x97c95a99 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9579B1F2
        aggressiveness = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF89AB419
        cover_check = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED9BF5A3
        search_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED69488F
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3CB99B1E
        approach_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733DA88A
        unknown_0x733da88a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03FDBE4A
        unknown_0x03fdbe4a = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC36E745
        dodge_check = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EAD288E
        unknown_0x4ead288e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF11EC8EE
        no_backing_up = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x808576EE
        no_knockback_movement = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BC22735
        no_melee_attack = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA5912430
        blade_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_damage": 10.0, "di_knock_back_power": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71587B45
        unknown_0x71587b45 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7903312E
        unknown_0x7903312e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B454A27
        unknown_0x1b454a27 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2AC2D96
        gun_track_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x615BB850
        unknown_0x615bb850 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B1F1541
        unknown_0x7b1f1541 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A4B4AEA
        has_cloak = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BC6F1D5
        cloak_opacity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388BC31F
        cloak_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4319C840
        decloak_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8AA60B6C
        cover_cloak_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57E862AA
        melee_cloak_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFCD4ED64
        can_combat_teleport = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFAA81D3A
        min_teleport_dist = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA90369E6
        min_teleport_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2EB81206
        unknown_0x2eb81206 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02E75B93
        unknown_0x02e75b93 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0881A3B5
        unknown_0x0881a3b5 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38B6452E
        unknown_0x38b6452e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE3794994
        unknown_0xe3794994 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54F66DA0
        unknown_0x54f66da0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x506C5C8A
        unknown_0x506c5c8a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x159F33D6
        unknown_0x159f33d6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0524BC7E
        unknown_0x0524bc7e = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x256B394F
        unknown_0x256b394f = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x824DB7CE
        unknown_0x824db7ce = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE527CDE8
        unknown_0xe527cde8 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61E801D4
        unknown_0x61e801d4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF19B113E
        unknown_0xf19b113e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80C6880F
        unknown_0x80c6880f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08358A6A
        unknown_0x08358a6a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA00204B0
        unknown_0xa00204b0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0806C08D
        unknown_0x0806c08d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17DB0CF2
        unknown_0x17db0cf2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC245A874
        sound_alert = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC192E357
        sound_hurled = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B412C4B
        sound_death = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A36B5D5
        unknown_0x8a36b5d5 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34E20697
        unknown_0x34e20697 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3B6103B
        grenade_data = SpacePirateWeaponData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4FDAB367
        space_pirate_struct_0x4fdab367 = SpacePirateStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37212693
        space_pirate_struct_0x37212693 = SpacePirateStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91B4CB73
        space_pirate_struct_0x91b4cb73 = SpacePirateStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07C1DE29
        has_shield = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AEE5C47
        unknown_0x4aee5c47 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD34F1323
        shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8255F594
        hyper_shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D1D1648
        unknown_0x0d1d1648 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC699AD35
        char = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE1AFBC0
        grapple_data = GrappleData.from_stream(data, game, property_size, default_override={"grapple_type": 1})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71E83F06
        shield_busted_scan_info = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFDE9C4DF
        has_armor = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF18384D4
        armor_health = HealthInfo.from_stream(
            data, game, property_size, default_override={"health": 100.0, "hi_knock_back_resistance": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x896D5BD9
        armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC13A3E1F
        head_armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7579CC86
        armor_broken_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65D86552
        armor_broken_skin_rules = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68002BD7
        head_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD315C7C
        collar_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x042A25ED
        left_collar_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE39B8B1E
        right_collar_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x356C166A
        spine1_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CA4A298
        spine2_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF44507E
        left_hip_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD2C9A656
        right_hip_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4E26A8E
        skeleton_root_armor_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531A8C85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x040A4EDF
        unknown_0x040a4edf = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C572665
        unknown_0x5c572665 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCA41D93
        unknown_0xcca41d93 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x767F168E
        unknown_0x767f168e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89A5EDC8
        keep_target_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x668EC0A0
        unknown_0x668ec0a0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14950F43
        unknown_0x14950f43 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x761ED7AF
        unknown_0x761ed7af = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            attack_behavior,
            can_interrupt_tasks,
            warp_in,
            unknown_0x87929c41,
            unknown_0x9a0ce9b2,
            unknown_0x4d61342a,
            initial_taunt_chance,
            combat_taunt_chance,
            instant_attack,
            unknown_0x97c95a99,
            aggressiveness,
            cover_check,
            search_radius,
            hearing_radius,
            approach_radius,
            unknown_0x733da88a,
            unknown_0x03fdbe4a,
            dodge_check,
            unknown_0x4ead288e,
            no_backing_up,
            no_knockback_movement,
            no_melee_attack,
            blade_damage,
            unknown_0x71587b45,
            unknown_0x7903312e,
            unknown_0x1b454a27,
            gun_track_delay,
            unknown_0x615bb850,
            unknown_0x7b1f1541,
            has_cloak,
            cloak_opacity,
            cloak_time,
            decloak_time,
            cover_cloak_chance,
            melee_cloak_chance,
            can_combat_teleport,
            min_teleport_dist,
            min_teleport_time,
            unknown_0x2eb81206,
            unknown_0x02e75b93,
            unknown_0x0881a3b5,
            unknown_0x38b6452e,
            unknown_0xe3794994,
            unknown_0x54f66da0,
            unknown_0x506c5c8a,
            unknown_0x159f33d6,
            unknown_0x0524bc7e,
            unknown_0x256b394f,
            unknown_0x824db7ce,
            unknown_0xe527cde8,
            unknown_0x61e801d4,
            unknown_0xf19b113e,
            unknown_0x80c6880f,
            unknown_0x08358a6a,
            unknown_0xa00204b0,
            unknown_0x0806c08d,
            unknown_0x17db0cf2,
            sound_alert,
            sound_hurled,
            sound_death,
            unknown_0x8a36b5d5,
            unknown_0x34e20697,
            grenade_data,
            space_pirate_struct_0x4fdab367,
            space_pirate_struct_0x37212693,
            space_pirate_struct_0x91b4cb73,
            has_shield,
            unknown_0x4aee5c47,
            shield_vulnerability,
            hyper_shield_vulnerability,
            unknown_0x0d1d1648,
            char,
            grapple_data,
            shield_busted_scan_info,
            has_armor,
            armor_health,
            armor_vulnerability,
            head_armor_vulnerability,
            armor_broken_model,
            armor_broken_skin_rules,
            head_armor_model,
            collar_armor_model,
            left_collar_armor_model,
            right_collar_armor_model,
            spine1_armor_model,
            spine2_armor_model,
            left_hip_armor_model,
            right_hip_armor_model,
            skeleton_root_armor_model,
            is_gandrayda,
            unknown_0x040a4edf,
            unknown_0x5c572665,
            unknown_0xcca41d93,
            unknown_0x767f168e,
            keep_target_time,
            unknown_0x668ec0a0,
            unknown_0x14950f43,
            unknown_0x761ed7af,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00b")  # 98 properties

        data.write(b"\x8e\x1e\x15\x86")  # 0x8e1e1586
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.attack_behavior))

        data.write(b"\xa4\x0c\xb8G")  # 0xa40cb847
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_interrupt_tasks))

        data.write(b"t(\xa2\x9f")  # 0x7428a29f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.warp_in))

        data.write(b"\x87\x92\x9cA")  # 0x87929c41
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x87929c41))

        data.write(b"\x9a\x0c\xe9\xb2")  # 0x9a0ce9b2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x9a0ce9b2))

        data.write(b"Ma4*")  # 0x4d61342a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4d61342a))

        data.write(b"-\x82d\xea")  # 0x2d8264ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_taunt_chance))

        data.write(b"\xa6\xaf\x0cW")  # 0xa6af0c57
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.combat_taunt_chance))

        data.write(b"f\x97q*")  # 0x6697712a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.instant_attack))

        data.write(b"\x97\xc9Z\x99")  # 0x97c95a99
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x97c95a99))

        data.write(b"\x95y\xb1\xf2")  # 0x9579b1f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aggressiveness))

        data.write(b"\xf8\x9a\xb4\x19")  # 0xf89ab419
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cover_check))

        data.write(b"\xed\x9b\xf5\xa3")  # 0xed9bf5a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.search_radius))

        data.write(b"\xediH\x8f")  # 0xed69488f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b"<\xb9\x9b\x1e")  # 0x3cb99b1e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.approach_radius))

        data.write(b"s=\xa8\x8a")  # 0x733da88a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x733da88a))

        data.write(b"\x03\xfd\xbeJ")  # 0x3fdbe4a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x03fdbe4a))

        data.write(b"\xdc6\xe7E")  # 0xdc36e745
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_check))

        data.write(b"N\xad(\x8e")  # 0x4ead288e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4ead288e))

        data.write(b"\xf1\x1e\xc8\xee")  # 0xf11ec8ee
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.no_backing_up))

        data.write(b"\x80\x85v\xee")  # 0x808576ee
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.no_knockback_movement))

        data.write(b"k\xc2'5")  # 0x6bc22735
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.no_melee_attack))

        data.write(b"\xa5\x91$0")  # 0xa5912430
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blade_damage.to_stream(data, game, default_override={"di_damage": 10.0, "di_knock_back_power": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"qX{E")  # 0x71587b45
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x71587b45))

        data.write(b"y\x031.")  # 0x7903312e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7903312e))

        data.write(b"\x1bEJ'")  # 0x1b454a27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x1b454a27))

        data.write(b"\xb2\xac-\x96")  # 0xb2ac2d96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gun_track_delay))

        data.write(b"a[\xb8P")  # 0x615bb850
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x615bb850))

        data.write(b"{\x1f\x15A")  # 0x7b1f1541
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7b1f1541))

        data.write(b"zKJ\xea")  # 0x7a4b4aea
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.has_cloak))

        data.write(b"[\xc6\xf1\xd5")  # 0x5bc6f1d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cloak_opacity))

        data.write(b"8\x8b\xc3\x1f")  # 0x388bc31f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cloak_time))

        data.write(b"C\x19\xc8@")  # 0x4319c840
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.decloak_time))

        data.write(b"\x8a\xa6\x0bl")  # 0x8aa60b6c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cover_cloak_chance))

        data.write(b"W\xe8b\xaa")  # 0x57e862aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_cloak_chance))

        data.write(b"\xfc\xd4\xedd")  # 0xfcd4ed64
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_combat_teleport))

        data.write(b"\xfa\xa8\x1d:")  # 0xfaa81d3a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_teleport_dist))

        data.write(b"\xa9\x03i\xe6")  # 0xa90369e6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_teleport_time))

        data.write(b".\xb8\x12\x06")  # 0x2eb81206
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2eb81206))

        data.write(b"\x02\xe7[\x93")  # 0x2e75b93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x02e75b93))

        data.write(b"\x08\x81\xa3\xb5")  # 0x881a3b5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x0881a3b5))

        data.write(b"8\xb6E.")  # 0x38b6452e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x38b6452e))

        data.write(b"\xe3yI\x94")  # 0xe3794994
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe3794994))

        data.write(b"T\xf6m\xa0")  # 0x54f66da0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x54f66da0))

        data.write(b"Pl\\\x8a")  # 0x506c5c8a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x506c5c8a))

        data.write(b"\x15\x9f3\xd6")  # 0x159f33d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x159f33d6))

        data.write(b"\x05$\xbc~")  # 0x524bc7e
        data.write(b"\x00\x0c")  # size
        self.unknown_0x0524bc7e.to_stream(data, game)

        data.write(b"%k9O")  # 0x256b394f
        data.write(b"\x00\x0c")  # size
        self.unknown_0x256b394f.to_stream(data, game)

        data.write(b"\x82M\xb7\xce")  # 0x824db7ce
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x824db7ce))

        data.write(b"\xe5'\xcd\xe8")  # 0xe527cde8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xe527cde8))

        data.write(b"a\xe8\x01\xd4")  # 0x61e801d4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x61e801d4))

        data.write(b"\xf1\x9b\x11>")  # 0xf19b113e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf19b113e))

        data.write(b"\x80\xc6\x88\x0f")  # 0x80c6880f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x80c6880f))

        data.write(b"\x085\x8aj")  # 0x8358a6a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x08358a6a))

        data.write(b"\xa0\x02\x04\xb0")  # 0xa00204b0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa00204b0))

        data.write(b"\x08\x06\xc0\x8d")  # 0x806c08d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0806c08d))

        data.write(b"\x17\xdb\x0c\xf2")  # 0x17db0cf2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x17db0cf2))

        data.write(b"\xc2E\xa8t")  # 0xc245a874
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_alert))

        data.write(b"\xc1\x92\xe3W")  # 0xc192e357
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_hurled))

        data.write(b"\x1bA,K")  # 0x1b412c4b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_death))

        data.write(b"\x8a6\xb5\xd5")  # 0x8a36b5d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x8a36b5d5))

        data.write(b"4\xe2\x06\x97")  # 0x34e20697
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x34e20697))

        data.write(b"\xc3\xb6\x10;")  # 0xc3b6103b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grenade_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"O\xda\xb3g")  # 0x4fdab367
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.space_pirate_struct_0x4fdab367.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"7!&\x93")  # 0x37212693
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.space_pirate_struct_0x37212693.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x91\xb4\xcbs")  # 0x91b4cb73
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.space_pirate_struct_0x91b4cb73.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x07\xc1\xde)")  # 0x7c1de29
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.has_shield))

        data.write(b"J\xee\\G")  # 0x4aee5c47
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4aee5c47))

        data.write(b"\xd3O\x13#")  # 0xd34f1323
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x82U\xf5\x94")  # 0x8255f594
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\r\x1d\x16H")  # 0xd1d1648
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0d1d1648))

        data.write(b"\xc6\x99\xad5")  # 0xc699ad35
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbe\x1a\xfb\xc0")  # 0xbe1afbc0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_data.to_stream(data, game, default_override={"grapple_type": 1})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"q\xe8?\x06")  # 0x71e83f06
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.shield_busted_scan_info))

        data.write(b"\xfd\xe9\xc4\xdf")  # 0xfde9c4df
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.has_armor))

        data.write(b"\xf1\x83\x84\xd4")  # 0xf18384d4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.armor_health.to_stream(data, game, default_override={"health": 100.0, "hi_knock_back_resistance": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x89m[\xd9")  # 0x896d5bd9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.armor_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc1:>\x1f")  # 0xc13a3e1f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.head_armor_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"uy\xcc\x86")  # 0x7579cc86
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_broken_model))

        data.write(b"e\xd8eR")  # 0x65d86552
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.armor_broken_skin_rules))

        data.write(b"h\x00+\xd7")  # 0x68002bd7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.head_armor_model))

        data.write(b"\xad1\\|")  # 0xad315c7c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.collar_armor_model))

        data.write(b"\x04*%\xed")  # 0x42a25ed
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_collar_armor_model))

        data.write(b"\xe3\x9b\x8b\x1e")  # 0xe39b8b1e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_collar_armor_model))

        data.write(b"5l\x16j")  # 0x356c166a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.spine1_armor_model))

        data.write(b"\x1c\xa4\xa2\x98")  # 0x1ca4a298
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.spine2_armor_model))

        data.write(b"\xdfDP~")  # 0xdf44507e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_hip_armor_model))

        data.write(b"\xd2\xc9\xa6V")  # 0xd2c9a656
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_hip_armor_model))

        data.write(b"\xd4\xe2j\x8e")  # 0xd4e26a8e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.skeleton_root_armor_model))

        data.write(b"S\x1a\x8c\x85")  # 0x531a8c85
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b"\x04\nN\xdf")  # 0x40a4edf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x040a4edf))

        data.write(b"\\W&e")  # 0x5c572665
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x5c572665))

        data.write(b"\xcc\xa4\x1d\x93")  # 0xcca41d93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcca41d93))

        data.write(b"v\x7f\x16\x8e")  # 0x767f168e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x767f168e))

        data.write(b"\x89\xa5\xed\xc8")  # 0x89a5edc8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.keep_target_time))

        data.write(b"f\x8e\xc0\xa0")  # 0x668ec0a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x668ec0a0))

        data.write(b"\x14\x95\x0fC")  # 0x14950f43
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x14950f43))

        data.write(b"v\x1e\xd7\xaf")  # 0x761ed7af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x761ed7af))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpacePirateDataJson", data)
        return cls(
            attack_behavior=json_data["attack_behavior"],
            can_interrupt_tasks=json_data["can_interrupt_tasks"],
            warp_in=json_data["warp_in"],
            unknown_0x87929c41=json_data["unknown_0x87929c41"],
            unknown_0x9a0ce9b2=json_data["unknown_0x9a0ce9b2"],
            unknown_0x4d61342a=json_data["unknown_0x4d61342a"],
            initial_taunt_chance=json_data["initial_taunt_chance"],
            combat_taunt_chance=json_data["combat_taunt_chance"],
            instant_attack=json_data["instant_attack"],
            unknown_0x97c95a99=json_data["unknown_0x97c95a99"],
            aggressiveness=json_data["aggressiveness"],
            cover_check=json_data["cover_check"],
            search_radius=json_data["search_radius"],
            hearing_radius=json_data["hearing_radius"],
            approach_radius=json_data["approach_radius"],
            unknown_0x733da88a=json_data["unknown_0x733da88a"],
            unknown_0x03fdbe4a=json_data["unknown_0x03fdbe4a"],
            dodge_check=json_data["dodge_check"],
            unknown_0x4ead288e=json_data["unknown_0x4ead288e"],
            no_backing_up=json_data["no_backing_up"],
            no_knockback_movement=json_data["no_knockback_movement"],
            no_melee_attack=json_data["no_melee_attack"],
            blade_damage=DamageInfo.from_json(json_data["blade_damage"]),
            unknown_0x71587b45=json_data["unknown_0x71587b45"],
            unknown_0x7903312e=json_data["unknown_0x7903312e"],
            unknown_0x1b454a27=json_data["unknown_0x1b454a27"],
            gun_track_delay=json_data["gun_track_delay"],
            unknown_0x615bb850=json_data["unknown_0x615bb850"],
            unknown_0x7b1f1541=json_data["unknown_0x7b1f1541"],
            has_cloak=json_data["has_cloak"],
            cloak_opacity=json_data["cloak_opacity"],
            cloak_time=json_data["cloak_time"],
            decloak_time=json_data["decloak_time"],
            cover_cloak_chance=json_data["cover_cloak_chance"],
            melee_cloak_chance=json_data["melee_cloak_chance"],
            can_combat_teleport=json_data["can_combat_teleport"],
            min_teleport_dist=json_data["min_teleport_dist"],
            min_teleport_time=json_data["min_teleport_time"],
            unknown_0x2eb81206=json_data["unknown_0x2eb81206"],
            unknown_0x02e75b93=json_data["unknown_0x02e75b93"],
            unknown_0x0881a3b5=json_data["unknown_0x0881a3b5"],
            unknown_0x38b6452e=json_data["unknown_0x38b6452e"],
            unknown_0xe3794994=json_data["unknown_0xe3794994"],
            unknown_0x54f66da0=json_data["unknown_0x54f66da0"],
            unknown_0x506c5c8a=json_data["unknown_0x506c5c8a"],
            unknown_0x159f33d6=json_data["unknown_0x159f33d6"],
            unknown_0x0524bc7e=Vector.from_json(json_data["unknown_0x0524bc7e"]),
            unknown_0x256b394f=Vector.from_json(json_data["unknown_0x256b394f"]),
            unknown_0x824db7ce=json_data["unknown_0x824db7ce"],
            unknown_0xe527cde8=json_data["unknown_0xe527cde8"],
            unknown_0x61e801d4=json_data["unknown_0x61e801d4"],
            unknown_0xf19b113e=json_data["unknown_0xf19b113e"],
            unknown_0x80c6880f=json_data["unknown_0x80c6880f"],
            unknown_0x08358a6a=json_data["unknown_0x08358a6a"],
            unknown_0xa00204b0=json_data["unknown_0xa00204b0"],
            unknown_0x0806c08d=json_data["unknown_0x0806c08d"],
            unknown_0x17db0cf2=json_data["unknown_0x17db0cf2"],
            sound_alert=json_data["sound_alert"],
            sound_hurled=json_data["sound_hurled"],
            sound_death=json_data["sound_death"],
            unknown_0x8a36b5d5=json_data["unknown_0x8a36b5d5"],
            unknown_0x34e20697=json_data["unknown_0x34e20697"],
            grenade_data=SpacePirateWeaponData.from_json(json_data["grenade_data"]),
            space_pirate_struct_0x4fdab367=SpacePirateStruct.from_json(json_data["space_pirate_struct_0x4fdab367"]),
            space_pirate_struct_0x37212693=SpacePirateStruct.from_json(json_data["space_pirate_struct_0x37212693"]),
            space_pirate_struct_0x91b4cb73=SpacePirateStruct.from_json(json_data["space_pirate_struct_0x91b4cb73"]),
            has_shield=json_data["has_shield"],
            unknown_0x4aee5c47=json_data["unknown_0x4aee5c47"],
            shield_vulnerability=DamageVulnerability.from_json(json_data["shield_vulnerability"]),
            hyper_shield_vulnerability=DamageVulnerability.from_json(json_data["hyper_shield_vulnerability"]),
            unknown_0x0d1d1648=json_data["unknown_0x0d1d1648"],
            char=AnimationParameters.from_json(json_data["char"]),
            grapple_data=GrappleData.from_json(json_data["grapple_data"]),
            shield_busted_scan_info=json_data["shield_busted_scan_info"],
            has_armor=json_data["has_armor"],
            armor_health=HealthInfo.from_json(json_data["armor_health"]),
            armor_vulnerability=DamageVulnerability.from_json(json_data["armor_vulnerability"]),
            head_armor_vulnerability=DamageVulnerability.from_json(json_data["head_armor_vulnerability"]),
            armor_broken_model=json_data["armor_broken_model"],
            armor_broken_skin_rules=json_data["armor_broken_skin_rules"],
            head_armor_model=json_data["head_armor_model"],
            collar_armor_model=json_data["collar_armor_model"],
            left_collar_armor_model=json_data["left_collar_armor_model"],
            right_collar_armor_model=json_data["right_collar_armor_model"],
            spine1_armor_model=json_data["spine1_armor_model"],
            spine2_armor_model=json_data["spine2_armor_model"],
            left_hip_armor_model=json_data["left_hip_armor_model"],
            right_hip_armor_model=json_data["right_hip_armor_model"],
            skeleton_root_armor_model=json_data["skeleton_root_armor_model"],
            is_gandrayda=json_data["is_gandrayda"],
            unknown_0x040a4edf=json_data["unknown_0x040a4edf"],
            unknown_0x5c572665=json_data["unknown_0x5c572665"],
            unknown_0xcca41d93=json_data["unknown_0xcca41d93"],
            unknown_0x767f168e=json_data["unknown_0x767f168e"],
            keep_target_time=json_data["keep_target_time"],
            unknown_0x668ec0a0=json_data["unknown_0x668ec0a0"],
            unknown_0x14950f43=json_data["unknown_0x14950f43"],
            unknown_0x761ed7af=json_data["unknown_0x761ed7af"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "attack_behavior": self.attack_behavior,
            "can_interrupt_tasks": self.can_interrupt_tasks,
            "warp_in": self.warp_in,
            "unknown_0x87929c41": self.unknown_0x87929c41,
            "unknown_0x9a0ce9b2": self.unknown_0x9a0ce9b2,
            "unknown_0x4d61342a": self.unknown_0x4d61342a,
            "initial_taunt_chance": self.initial_taunt_chance,
            "combat_taunt_chance": self.combat_taunt_chance,
            "instant_attack": self.instant_attack,
            "unknown_0x97c95a99": self.unknown_0x97c95a99,
            "aggressiveness": self.aggressiveness,
            "cover_check": self.cover_check,
            "search_radius": self.search_radius,
            "hearing_radius": self.hearing_radius,
            "approach_radius": self.approach_radius,
            "unknown_0x733da88a": self.unknown_0x733da88a,
            "unknown_0x03fdbe4a": self.unknown_0x03fdbe4a,
            "dodge_check": self.dodge_check,
            "unknown_0x4ead288e": self.unknown_0x4ead288e,
            "no_backing_up": self.no_backing_up,
            "no_knockback_movement": self.no_knockback_movement,
            "no_melee_attack": self.no_melee_attack,
            "blade_damage": self.blade_damage.to_json(),
            "unknown_0x71587b45": self.unknown_0x71587b45,
            "unknown_0x7903312e": self.unknown_0x7903312e,
            "unknown_0x1b454a27": self.unknown_0x1b454a27,
            "gun_track_delay": self.gun_track_delay,
            "unknown_0x615bb850": self.unknown_0x615bb850,
            "unknown_0x7b1f1541": self.unknown_0x7b1f1541,
            "has_cloak": self.has_cloak,
            "cloak_opacity": self.cloak_opacity,
            "cloak_time": self.cloak_time,
            "decloak_time": self.decloak_time,
            "cover_cloak_chance": self.cover_cloak_chance,
            "melee_cloak_chance": self.melee_cloak_chance,
            "can_combat_teleport": self.can_combat_teleport,
            "min_teleport_dist": self.min_teleport_dist,
            "min_teleport_time": self.min_teleport_time,
            "unknown_0x2eb81206": self.unknown_0x2eb81206,
            "unknown_0x02e75b93": self.unknown_0x02e75b93,
            "unknown_0x0881a3b5": self.unknown_0x0881a3b5,
            "unknown_0x38b6452e": self.unknown_0x38b6452e,
            "unknown_0xe3794994": self.unknown_0xe3794994,
            "unknown_0x54f66da0": self.unknown_0x54f66da0,
            "unknown_0x506c5c8a": self.unknown_0x506c5c8a,
            "unknown_0x159f33d6": self.unknown_0x159f33d6,
            "unknown_0x0524bc7e": self.unknown_0x0524bc7e.to_json(),
            "unknown_0x256b394f": self.unknown_0x256b394f.to_json(),
            "unknown_0x824db7ce": self.unknown_0x824db7ce,
            "unknown_0xe527cde8": self.unknown_0xe527cde8,
            "unknown_0x61e801d4": self.unknown_0x61e801d4,
            "unknown_0xf19b113e": self.unknown_0xf19b113e,
            "unknown_0x80c6880f": self.unknown_0x80c6880f,
            "unknown_0x08358a6a": self.unknown_0x08358a6a,
            "unknown_0xa00204b0": self.unknown_0xa00204b0,
            "unknown_0x0806c08d": self.unknown_0x0806c08d,
            "unknown_0x17db0cf2": self.unknown_0x17db0cf2,
            "sound_alert": self.sound_alert,
            "sound_hurled": self.sound_hurled,
            "sound_death": self.sound_death,
            "unknown_0x8a36b5d5": self.unknown_0x8a36b5d5,
            "unknown_0x34e20697": self.unknown_0x34e20697,
            "grenade_data": self.grenade_data.to_json(),
            "space_pirate_struct_0x4fdab367": self.space_pirate_struct_0x4fdab367.to_json(),
            "space_pirate_struct_0x37212693": self.space_pirate_struct_0x37212693.to_json(),
            "space_pirate_struct_0x91b4cb73": self.space_pirate_struct_0x91b4cb73.to_json(),
            "has_shield": self.has_shield,
            "unknown_0x4aee5c47": self.unknown_0x4aee5c47,
            "shield_vulnerability": self.shield_vulnerability.to_json(),
            "hyper_shield_vulnerability": self.hyper_shield_vulnerability.to_json(),
            "unknown_0x0d1d1648": self.unknown_0x0d1d1648,
            "char": self.char.to_json(),
            "grapple_data": self.grapple_data.to_json(),
            "shield_busted_scan_info": self.shield_busted_scan_info,
            "has_armor": self.has_armor,
            "armor_health": self.armor_health.to_json(),
            "armor_vulnerability": self.armor_vulnerability.to_json(),
            "head_armor_vulnerability": self.head_armor_vulnerability.to_json(),
            "armor_broken_model": self.armor_broken_model,
            "armor_broken_skin_rules": self.armor_broken_skin_rules,
            "head_armor_model": self.head_armor_model,
            "collar_armor_model": self.collar_armor_model,
            "left_collar_armor_model": self.left_collar_armor_model,
            "right_collar_armor_model": self.right_collar_armor_model,
            "spine1_armor_model": self.spine1_armor_model,
            "spine2_armor_model": self.spine2_armor_model,
            "left_hip_armor_model": self.left_hip_armor_model,
            "right_hip_armor_model": self.right_hip_armor_model,
            "skeleton_root_armor_model": self.skeleton_root_armor_model,
            "is_gandrayda": self.is_gandrayda,
            "unknown_0x040a4edf": self.unknown_0x040a4edf,
            "unknown_0x5c572665": self.unknown_0x5c572665,
            "unknown_0xcca41d93": self.unknown_0xcca41d93,
            "unknown_0x767f168e": self.unknown_0x767f168e,
            "keep_target_time": self.keep_target_time,
            "unknown_0x668ec0a0": self.unknown_0x668ec0a0,
            "unknown_0x14950f43": self.unknown_0x14950f43,
            "unknown_0x761ed7af": self.unknown_0x761ed7af,
        }


def _decode_blade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_damage": 10.0, "di_knock_back_power": 5.0}
    )


def _decode_unknown_0x0524bc7e(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0x256b394f(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_grenade_data(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateWeaponData:
    return SpacePirateWeaponData.from_stream(data, game, property_size)


def _decode_space_pirate_struct_0x4fdab367(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateStruct:
    return SpacePirateStruct.from_stream(data, game, property_size)


def _decode_space_pirate_struct_0x37212693(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateStruct:
    return SpacePirateStruct.from_stream(data, game, property_size)


def _decode_space_pirate_struct_0x91b4cb73(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateStruct:
    return SpacePirateStruct.from_stream(data, game, property_size)


def _decode_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_char(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size, default_override={"grapple_type": 1})


def _decode_armor_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(
        data, game, property_size, default_override={"health": 100.0, "hi_knock_back_resistance": 5.0}
    )


def _decode_armor_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_head_armor_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8E1E1586: ("attack_behavior", structs.decode_BIG_l),
    0xA40CB847: ("can_interrupt_tasks", structs.decode_BIG_bool_),
    0x7428A29F: ("warp_in", structs.decode_BIG_bool_),
    0x87929C41: ("unknown_0x87929c41", structs.decode_BIG_bool_),
    0x9A0CE9B2: ("unknown_0x9a0ce9b2", structs.decode_BIG_bool_),
    0x4D61342A: ("unknown_0x4d61342a", structs.decode_BIG_bool_),
    0x2D8264EA: ("initial_taunt_chance", structs.decode_BIG_f),
    0xA6AF0C57: ("combat_taunt_chance", structs.decode_BIG_f),
    0x6697712A: ("instant_attack", structs.decode_BIG_bool_),
    0x97C95A99: ("unknown_0x97c95a99", structs.decode_BIG_bool_),
    0x9579B1F2: ("aggressiveness", structs.decode_BIG_f),
    0xF89AB419: ("cover_check", structs.decode_BIG_f),
    0xED9BF5A3: ("search_radius", structs.decode_BIG_f),
    0xED69488F: ("hearing_radius", structs.decode_BIG_f),
    0x3CB99B1E: ("approach_radius", structs.decode_BIG_f),
    0x733DA88A: ("unknown_0x733da88a", structs.decode_BIG_f),
    0x03FDBE4A: ("unknown_0x03fdbe4a", structs.decode_BIG_bool_),
    0xDC36E745: ("dodge_check", structs.decode_BIG_f),
    0x4EAD288E: ("unknown_0x4ead288e", structs.decode_BIG_f),
    0xF11EC8EE: ("no_backing_up", structs.decode_BIG_bool_),
    0x808576EE: ("no_knockback_movement", structs.decode_BIG_bool_),
    0x6BC22735: ("no_melee_attack", structs.decode_BIG_bool_),
    0xA5912430: ("blade_damage", _decode_blade_damage),
    0x71587B45: ("unknown_0x71587b45", structs.decode_BIG_f),
    0x7903312E: ("unknown_0x7903312e", structs.decode_BIG_f),
    0x1B454A27: ("unknown_0x1b454a27", structs.decode_BIG_l),
    0xB2AC2D96: ("gun_track_delay", structs.decode_BIG_f),
    0x615BB850: ("unknown_0x615bb850", structs.decode_BIG_l),
    0x7B1F1541: ("unknown_0x7b1f1541", structs.decode_BIG_l),
    0x7A4B4AEA: ("has_cloak", structs.decode_BIG_bool_),
    0x5BC6F1D5: ("cloak_opacity", structs.decode_BIG_f),
    0x388BC31F: ("cloak_time", structs.decode_BIG_f),
    0x4319C840: ("decloak_time", structs.decode_BIG_f),
    0x8AA60B6C: ("cover_cloak_chance", structs.decode_BIG_f),
    0x57E862AA: ("melee_cloak_chance", structs.decode_BIG_f),
    0xFCD4ED64: ("can_combat_teleport", structs.decode_BIG_bool_),
    0xFAA81D3A: ("min_teleport_dist", structs.decode_BIG_f),
    0xA90369E6: ("min_teleport_time", structs.decode_BIG_f),
    0x2EB81206: ("unknown_0x2eb81206", structs.decode_BIG_f),
    0x02E75B93: ("unknown_0x02e75b93", structs.decode_BIG_f),
    0x0881A3B5: ("unknown_0x0881a3b5", structs.decode_BIG_bool_),
    0x38B6452E: ("unknown_0x38b6452e", structs.decode_BIG_bool_),
    0xE3794994: ("unknown_0xe3794994", structs.decode_BIG_f),
    0x54F66DA0: ("unknown_0x54f66da0", structs.decode_BIG_f),
    0x506C5C8A: ("unknown_0x506c5c8a", structs.decode_BIG_f),
    0x159F33D6: ("unknown_0x159f33d6", structs.decode_BIG_f),
    0x0524BC7E: ("unknown_0x0524bc7e", _decode_unknown_0x0524bc7e),
    0x256B394F: ("unknown_0x256b394f", _decode_unknown_0x256b394f),
    0x824DB7CE: ("unknown_0x824db7ce", structs.decode_BIG_f),
    0xE527CDE8: ("unknown_0xe527cde8", structs.decode_BIG_bool_),
    0x61E801D4: ("unknown_0x61e801d4", structs.decode_BIG_f),
    0xF19B113E: ("unknown_0xf19b113e", structs.decode_BIG_f),
    0x80C6880F: ("unknown_0x80c6880f", structs.decode_BIG_f),
    0x08358A6A: ("unknown_0x08358a6a", structs.decode_BIG_f),
    0xA00204B0: ("unknown_0xa00204b0", structs.decode_BIG_f),
    0x0806C08D: ("unknown_0x0806c08d", structs.decode_BIG_f),
    0x17DB0CF2: ("unknown_0x17db0cf2", structs.decode_BIG_f),
    0xC245A874: ("sound_alert", structs.decode_BIG_Q),
    0xC192E357: ("sound_hurled", structs.decode_BIG_Q),
    0x1B412C4B: ("sound_death", structs.decode_BIG_Q),
    0x8A36B5D5: ("unknown_0x8a36b5d5", structs.decode_BIG_l),
    0x34E20697: ("unknown_0x34e20697", structs.decode_BIG_f),
    0xC3B6103B: ("grenade_data", _decode_grenade_data),
    0x4FDAB367: ("space_pirate_struct_0x4fdab367", _decode_space_pirate_struct_0x4fdab367),
    0x37212693: ("space_pirate_struct_0x37212693", _decode_space_pirate_struct_0x37212693),
    0x91B4CB73: ("space_pirate_struct_0x91b4cb73", _decode_space_pirate_struct_0x91b4cb73),
    0x07C1DE29: ("has_shield", structs.decode_BIG_bool_),
    0x4AEE5C47: ("unknown_0x4aee5c47", structs.decode_BIG_bool_),
    0xD34F1323: ("shield_vulnerability", _decode_shield_vulnerability),
    0x8255F594: ("hyper_shield_vulnerability", _decode_hyper_shield_vulnerability),
    0x0D1D1648: ("unknown_0x0d1d1648", structs.decode_BIG_f),
    0xC699AD35: ("char", _decode_char),
    0xBE1AFBC0: ("grapple_data", _decode_grapple_data),
    0x71E83F06: ("shield_busted_scan_info", structs.decode_BIG_Q),
    0xFDE9C4DF: ("has_armor", structs.decode_BIG_bool_),
    0xF18384D4: ("armor_health", _decode_armor_health),
    0x896D5BD9: ("armor_vulnerability", _decode_armor_vulnerability),
    0xC13A3E1F: ("head_armor_vulnerability", _decode_head_armor_vulnerability),
    0x7579CC86: ("armor_broken_model", structs.decode_BIG_Q),
    0x65D86552: ("armor_broken_skin_rules", structs.decode_BIG_Q),
    0x68002BD7: ("head_armor_model", structs.decode_BIG_Q),
    0xAD315C7C: ("collar_armor_model", structs.decode_BIG_Q),
    0x042A25ED: ("left_collar_armor_model", structs.decode_BIG_Q),
    0xE39B8B1E: ("right_collar_armor_model", structs.decode_BIG_Q),
    0x356C166A: ("spine1_armor_model", structs.decode_BIG_Q),
    0x1CA4A298: ("spine2_armor_model", structs.decode_BIG_Q),
    0xDF44507E: ("left_hip_armor_model", structs.decode_BIG_Q),
    0xD2C9A656: ("right_hip_armor_model", structs.decode_BIG_Q),
    0xD4E26A8E: ("skeleton_root_armor_model", structs.decode_BIG_Q),
    0x531A8C85: ("is_gandrayda", structs.decode_BIG_bool_),
    0x040A4EDF: ("unknown_0x040a4edf", structs.decode_BIG_l),
    0x5C572665: ("unknown_0x5c572665", structs.decode_BIG_l),
    0xCCA41D93: ("unknown_0xcca41d93", structs.decode_BIG_f),
    0x767F168E: ("unknown_0x767f168e", structs.decode_BIG_bool_),
    0x89A5EDC8: ("keep_target_time", structs.decode_BIG_f),
    0x668EC0A0: ("unknown_0x668ec0a0", structs.decode_BIG_f),
    0x14950F43: ("unknown_0x14950f43", structs.decode_BIG_f),
    0x761ED7AF: ("unknown_0x761ed7af", structs.decode_BIG_l),
}
