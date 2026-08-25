# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SpawnPointStructJson(typing_extensions.TypedDict):
        power_beam: int
        dark_beam: int
        light_beam: int
        annihilator_beam: int
        power_beam_combo: int
        dark_beam_combo: int
        light_beam_combo: int
        annihilator_beam_combo: int
        charge_combo_upgrade: int
        combat_visor: int
        scan_visor: int
        dark_visor: int
        echo_visor: int
        varia_suit: int
        dark_suit: int
        light_suit: int
        morph_ball: int
        boost_ball: int
        spider_ball: int
        bomb: int
        light_bomb: int
        dark_bomb: int
        annihilator_bomb: int
        charge_upgrade: int
        grapple_beam: int
        double_jump: int
        gravity_boost: int
        seeker: int
        screw_attack: int
        translator_upgrade: int
        temple_key1: int
        temple_key2: int
        temple_key3: int
        temple_key4: int
        temple_key5: int
        temple_key6: int
        temple_key7: int
        temple_key8: int
        temple_key9: int
        sand_key1: int
        sand_key2: int
        sand_key3: int
        swamp_key1: int
        swamp_key2: int
        swamp_key3: int
        cliffside_key1: int
        cliffside_key2: int
        cliffside_key3: int
        energy: int
        energy_tank: int
        unknown_0x161898dc: int
        power_bomb: int
        missile: int
        dark_beam_ammo: int
        light_beam_ammo: int
        percentage_increase: int
        misc_counter1: int
        misc_counter2: int
        misc_counter3: int
        misc_counter4: int
        change_to_power_beam: int
        change_to_dark_beam: int
        change_to_light_beam: int
        change_to_annihilator_beam: int
        multi_charge_upgrade: int
        invisibility: int
        amplified_damage: int
        invincibility: int
        unknown_0x66ae338e: int
        unknown_0x210e495e: int
        unknown_0x1c6e60ee: int
        unknown_0xae4ebcfe: int
        frag_count: int
        died_count: int
        archenemy_count: int
        persistent_counter1: int
        persistent_counter2: int
        persistent_counter3: int
        persistent_counter4: int
        persistent_counter5: int
        persistent_counter6: int
        persistent_counter7: int
        persistent_counter8: int
        change_to_combat_visor: int
        change_to_scan_visor: int
        change_to_dark_visor: int
        change_to_echo_visor: int
        coin_amplifier: int
        coin_counter: int
        unlimited_missiles: int
        unlimited_beam_ammo: int
        dark_shield: int
        light_shield: int
        absorb_attack: int
        death_ball: int
        scan_virus: int
        visor_static: int
        beam_weapons_disabled: int
        missile_weapons_disabled: int
        unknown_0x32f5e918: int
        disable_ball: int
        disable_double_jump: int
        activate_morphball_boost: int
        hacked_effect: int
        activate_morphball_damage: int
        translator_upgrade1: int
        translator_upgrade2: int
        translator_upgrade3: int
        translator_upgrade4: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x9ACA45BC,
    0x92BB94B7,
    0x6BE340BA,
    0xC73B2C90,
    0xEFD4DABE,
    0x9B06BD3C,
    0x6D7172BF,
    0x16D89ACC,
    0xEA86A2B9,
    0x26A5E3C1,
    0x9DE8731D,
    0x3B0AB10B,
    0x95A30488,
    0xAB603F7,
    0x4DA55282,
    0xB4FD868F,
    0x3EC5A9F5,
    0x8C98247D,
    0xBD8B547C,
    0x53387689,
    0x57EB9E8B,
    0xAEB34A86,
    0xFB33F2A1,
    0x4B15EB9A,
    0x44FBB19C,
    0xF55BE12C,
    0xBC25CAED,
    0xA6B376F,
    0xD8A9BBCB,
    0x7D1C9685,
    0x8F6CDCF9,
    0x9DD97317,
    0x25651472,
    0xB8B22CCB,
    0xE4BAE,
    0x12BBE440,
    0xAA078325,
    0xF2649373,
    0x4AD8F416,
    0xC271CFBC,
    0xD0C46052,
    0x68780737,
    0x6EFFCF82,
    0x7C4A606C,
    0xC4F60709,
    0xC20D622B,
    0xD0B8CDC5,
    0x6804AAA0,
    0x1C397F0,
    0xFC6F860C,
    0x161898DC,
    0xA6C29B8D,
    0xEC7FB0EF,
    0xFCECF744,
    0x32052F91,
    0x6E4038AB,
    0x14387AAB,
    0x68DD545,
    0xBE31B220,
    0x23E68A99,
    0x8ECB6665,
    0x92C402AB,
    0x7FE26363,
    0xD7F8586A,
    0x27D254AF,
    0x19926420,
    0xCE284C09,
    0xDEC999C3,
    0x66AE338E,
    0x210E495E,
    0x1C6E60EE,
    0xAE4EBCFE,
    0x5351DBA5,
    0x2DB9A0A,
    0x7B980651,
    0xE9861C49,
    0xFB33B3A7,
    0x438FD4C2,
    0xDE58EC7B,
    0x66E48B1E,
    0x745124F0,
    0xCCED4395,
    0x948E53C3,
    0xD438F8E4,
    0x89E950C4,
    0x2F0B92D2,
    0x81A22751,
    0xDB8F0E87,
    0xAF6F361A,
    0xAE8DEE81,
    0xD1FFB49F,
    0xBC51DE4B,
    0x88414F93,
    0xFBE21590,
    0xD0B6A007,
    0xC45848FE,
    0x92B916D7,
    0xA6257CD8,
    0x6BF24C24,
    0x32F5E918,
    0x1CE95541,
    0x5DD9004D,
    0xF64F1DBD,
    0x76000D1E,
    0x85AB52BC,
    0x711C150F,
    0x63A9BAE1,
    0xDB15DD84,
    0x46C2E53D,
)


@dataclasses.dataclass()
class SpawnPointStruct(BaseProperty):
    power_beam: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9ACA45BC, original_name="PowerBeam"),
        },
    )
    dark_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x92BB94B7, original_name="DarkBeam"),
        },
    )
    light_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6BE340BA, original_name="LightBeam"),
        },
    )
    annihilator_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC73B2C90, original_name="AnnihilatorBeam"),
        },
    )
    power_beam_combo: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEFD4DABE, original_name="PowerBeamCombo"),
        },
    )
    dark_beam_combo: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9B06BD3C, original_name="DarkBeamCombo"),
        },
    )
    light_beam_combo: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6D7172BF, original_name="LightBeamCombo"),
        },
    )
    annihilator_beam_combo: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x16D89ACC, original_name="AnnihilatorBeamCombo"),
        },
    )
    charge_combo_upgrade: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEA86A2B9, original_name="ChargeComboUpgrade"),
        },
    )
    combat_visor: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x26A5E3C1, original_name="CombatVisor"),
        },
    )
    scan_visor: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9DE8731D, original_name="ScanVisor"),
        },
    )
    dark_visor: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3B0AB10B, original_name="DarkVisor"),
        },
    )
    echo_visor: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x95A30488, original_name="EchoVisor"),
        },
    )
    varia_suit: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0AB603F7, original_name="VariaSuit"),
        },
    )
    dark_suit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4DA55282, original_name="DarkSuit"),
        },
    )
    light_suit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB4FD868F, original_name="LightSuit"),
        },
    )
    morph_ball: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3EC5A9F5, original_name="MorphBall"),
        },
    )
    boost_ball: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8C98247D, original_name="BoostBall"),
        },
    )
    spider_ball: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBD8B547C, original_name="SpiderBall"),
        },
    )
    bomb: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x53387689, original_name="Bomb"),
        },
    )
    light_bomb: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x57EB9E8B, original_name="LightBomb"),
        },
    )
    dark_bomb: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAEB34A86, original_name="DarkBomb"),
        },
    )
    annihilator_bomb: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFB33F2A1, original_name="AnnihilatorBomb"),
        },
    )
    charge_upgrade: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4B15EB9A, original_name="ChargeUpgrade"),
        },
    )  # Choice
    grapple_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x44FBB19C, original_name="GrappleBeam"),
        },
    )
    double_jump: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF55BE12C, original_name="DoubleJump"),
        },
    )
    gravity_boost: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBC25CAED, original_name="GravityBoost"),
        },
    )
    seeker: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0A6B376F, original_name="Seeker"),
        },
    )
    screw_attack: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD8A9BBCB, original_name="ScrewAttack"),
        },
    )
    translator_upgrade: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7D1C9685, original_name="TranslatorUpgrade"),
        },
    )
    temple_key1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8F6CDCF9, original_name="TempleKey1"),
        },
    )
    temple_key2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9DD97317, original_name="TempleKey2"),
        },
    )
    temple_key3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x25651472, original_name="TempleKey3"),
        },
    )
    temple_key4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB8B22CCB, original_name="TempleKey4"),
        },
    )
    temple_key5: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x000E4BAE, original_name="TempleKey5"),
        },
    )
    temple_key6: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x12BBE440, original_name="TempleKey6"),
        },
    )
    temple_key7: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAA078325, original_name="TempleKey7"),
        },
    )
    temple_key8: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF2649373, original_name="TempleKey8"),
        },
    )
    temple_key9: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x4AD8F416, original_name="TempleKey9"),
        },
    )
    sand_key1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC271CFBC, original_name="SandKey1"),
        },
    )
    sand_key2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD0C46052, original_name="SandKey2"),
        },
    )
    sand_key3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x68780737, original_name="SandKey3"),
        },
    )
    swamp_key1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6EFFCF82, original_name="SwampKey1"),
        },
    )
    swamp_key2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7C4A606C, original_name="SwampKey2"),
        },
    )
    swamp_key3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC4F60709, original_name="SwampKey3"),
        },
    )
    cliffside_key1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC20D622B, original_name="CliffsideKey1"),
        },
    )
    cliffside_key2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD0B8CDC5, original_name="CliffsideKey2"),
        },
    )
    cliffside_key3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6804AAA0, original_name="CliffsideKey3"),
        },
    )
    energy: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x01C397F0, original_name="Energy"),
        },
    )
    energy_tank: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFC6F860C, original_name="EnergyTank"),
        },
    )
    unknown_0x161898dc: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x161898DC, original_name="Unknown"),
        },
    )
    power_bomb: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA6C29B8D, original_name="PowerBomb"),
        },
    )
    missile: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEC7FB0EF, original_name="Missile"),
        },
    )
    dark_beam_ammo: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFCECF744, original_name="DarkBeamAmmo"),
        },
    )
    light_beam_ammo: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x32052F91, original_name="LightBeamAmmo"),
        },
    )
    percentage_increase: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6E4038AB, original_name="PercentageIncrease"),
        },
    )
    misc_counter1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x14387AAB, original_name="MiscCounter1"),
        },
    )
    misc_counter2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x068DD545, original_name="MiscCounter2"),
        },
    )
    misc_counter3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBE31B220, original_name="MiscCounter3"),
        },
    )
    misc_counter4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x23E68A99, original_name="MiscCounter4"),
        },
    )
    change_to_power_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8ECB6665, original_name="ChangeToPowerBeam"),
        },
    )
    change_to_dark_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x92C402AB, original_name="ChangeToDarkBeam"),
        },
    )
    change_to_light_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7FE26363, original_name="ChangeToLightBeam"),
        },
    )
    change_to_annihilator_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD7F8586A, original_name="ChangeToAnnihilatorBeam"),
        },
    )
    multi_charge_upgrade: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x27D254AF, original_name="MultiChargeUpgrade"),
        },
    )
    invisibility: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x19926420, original_name="Invisibility"),
        },
    )
    amplified_damage: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCE284C09, original_name="AmplifiedDamage"),
        },
    )
    invincibility: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDEC999C3, original_name="Invincibility"),
        },
    )
    unknown_0x66ae338e: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x66AE338E, original_name="Unknown"),
        },
    )
    unknown_0x210e495e: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x210E495E, original_name="Unknown"),
        },
    )
    unknown_0x1c6e60ee: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1C6E60EE, original_name="Unknown"),
        },
    )
    unknown_0xae4ebcfe: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAE4EBCFE, original_name="Unknown"),
        },
    )
    frag_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5351DBA5, original_name="FragCount"),
        },
    )
    died_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x02DB9A0A, original_name="DiedCount"),
        },
    )
    archenemy_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7B980651, original_name="ArchenemyCount"),
        },
    )
    persistent_counter1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE9861C49, original_name="PersistentCounter1"),
        },
    )
    persistent_counter2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFB33B3A7, original_name="PersistentCounter2"),
        },
    )
    persistent_counter3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x438FD4C2, original_name="PersistentCounter3"),
        },
    )
    persistent_counter4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDE58EC7B, original_name="PersistentCounter4"),
        },
    )
    persistent_counter5: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x66E48B1E, original_name="PersistentCounter5"),
        },
    )
    persistent_counter6: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x745124F0, original_name="PersistentCounter6"),
        },
    )
    persistent_counter7: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCCED4395, original_name="PersistentCounter7"),
        },
    )
    persistent_counter8: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x948E53C3, original_name="PersistentCounter8"),
        },
    )
    change_to_combat_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD438F8E4, original_name="ChangeToCombatVisor"),
        },
    )
    change_to_scan_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x89E950C4, original_name="ChangeToScanVisor"),
        },
    )
    change_to_dark_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2F0B92D2, original_name="ChangeToDarkVisor"),
        },
    )
    change_to_echo_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x81A22751, original_name="ChangeToEchoVisor"),
        },
    )
    coin_amplifier: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDB8F0E87, original_name="CoinAmplifier"),
        },
    )
    coin_counter: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAF6F361A, original_name="CoinCounter"),
        },
    )
    unlimited_missiles: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAE8DEE81, original_name="UnlimitedMissiles"),
        },
    )
    unlimited_beam_ammo: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD1FFB49F, original_name="UnlimitedBeamAmmo"),
        },
    )
    dark_shield: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBC51DE4B, original_name="DarkShield"),
        },
    )
    light_shield: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x88414F93, original_name="LightShield"),
        },
    )
    absorb_attack: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFBE21590, original_name="AbsorbAttack"),
        },
    )
    death_ball: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD0B6A007, original_name="DeathBall"),
        },
    )
    scan_virus: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC45848FE, original_name="ScanVirus"),
        },
    )
    visor_static: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x92B916D7, original_name="VisorStatic"),
        },
    )
    beam_weapons_disabled: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA6257CD8, original_name="BeamWeaponsDisabled"),
        },
    )
    missile_weapons_disabled: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6BF24C24, original_name="MissileWeaponsDisabled"),
        },
    )
    unknown_0x32f5e918: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x32F5E918, original_name="Unknown"),
        },
    )
    disable_ball: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1CE95541, original_name="DisableBall"),
        },
    )
    disable_double_jump: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5DD9004D, original_name="DisableDoubleJump"),
        },
    )
    activate_morphball_boost: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF64F1DBD, original_name="ActivateMorphballBoost"),
        },
    )
    hacked_effect: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x76000D1E, original_name="HackedEffect"),
        },
    )
    activate_morphball_damage: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x85AB52BC, original_name="ActivateMorphballDamage"),
        },
    )
    translator_upgrade1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x711C150F, original_name="TranslatorUpgrade1"),
        },
    )
    translator_upgrade2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x63A9BAE1, original_name="TranslatorUpgrade2"),
        },
    )
    translator_upgrade3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDB15DD84, original_name="TranslatorUpgrade3"),
        },
    )
    translator_upgrade4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x46C2E53D, original_name="TranslatorUpgrade4"),
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
        if property_count != 109:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHLLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHlLHl"
            )

        dec = _FAST_FORMAT.unpack(data.read(1090))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[60],
            dec[63],
            dec[66],
            dec[69],
            dec[72],
            dec[75],
            dec[78],
            dec[81],
            dec[84],
            dec[87],
            dec[90],
            dec[93],
            dec[96],
            dec[99],
            dec[102],
            dec[105],
            dec[108],
            dec[111],
            dec[114],
            dec[117],
            dec[120],
            dec[123],
            dec[126],
            dec[129],
            dec[132],
            dec[135],
            dec[138],
            dec[141],
            dec[144],
            dec[147],
            dec[150],
            dec[153],
            dec[156],
            dec[159],
            dec[162],
            dec[165],
            dec[168],
            dec[171],
            dec[174],
            dec[177],
            dec[180],
            dec[183],
            dec[186],
            dec[189],
            dec[192],
            dec[195],
            dec[198],
            dec[201],
            dec[204],
            dec[207],
            dec[210],
            dec[213],
            dec[216],
            dec[219],
            dec[222],
            dec[225],
            dec[228],
            dec[231],
            dec[234],
            dec[237],
            dec[240],
            dec[243],
            dec[246],
            dec[249],
            dec[252],
            dec[255],
            dec[258],
            dec[261],
            dec[264],
            dec[267],
            dec[270],
            dec[273],
            dec[276],
            dec[279],
            dec[282],
            dec[285],
            dec[288],
            dec[291],
            dec[294],
            dec[297],
            dec[300],
            dec[303],
            dec[306],
            dec[309],
            dec[312],
            dec[315],
            dec[318],
            dec[321],
            dec[324],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
            dec[65],
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            dec[86],
            dec[89],
            dec[92],
            dec[95],
            dec[98],
            dec[101],
            dec[104],
            dec[107],
            dec[110],
            dec[113],
            dec[116],
            dec[119],
            dec[122],
            dec[125],
            dec[128],
            dec[131],
            dec[134],
            dec[137],
            dec[140],
            dec[143],
            dec[146],
            dec[149],
            dec[152],
            dec[155],
            dec[158],
            dec[161],
            dec[164],
            dec[167],
            dec[170],
            dec[173],
            dec[176],
            dec[179],
            dec[182],
            dec[185],
            dec[188],
            dec[191],
            dec[194],
            dec[197],
            dec[200],
            dec[203],
            dec[206],
            dec[209],
            dec[212],
            dec[215],
            dec[218],
            dec[221],
            dec[224],
            dec[227],
            dec[230],
            dec[233],
            dec[236],
            dec[239],
            dec[242],
            dec[245],
            dec[248],
            dec[251],
            dec[254],
            dec[257],
            dec[260],
            dec[263],
            dec[266],
            dec[269],
            dec[272],
            dec[275],
            dec[278],
            dec[281],
            dec[284],
            dec[287],
            dec[290],
            dec[293],
            dec[296],
            dec[299],
            dec[302],
            dec[305],
            dec[308],
            dec[311],
            dec[314],
            dec[317],
            dec[320],
            dec[323],
            dec[326],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00m")  # 109 properties

        data.write(b"\x9a\xcaE\xbc")  # 0x9aca45bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.power_beam))

        data.write(b"\x92\xbb\x94\xb7")  # 0x92bb94b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_beam))

        data.write(b"k\xe3@\xba")  # 0x6be340ba
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_beam))

        data.write(b"\xc7;,\x90")  # 0xc73b2c90
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.annihilator_beam))

        data.write(b"\xef\xd4\xda\xbe")  # 0xefd4dabe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.power_beam_combo))

        data.write(b"\x9b\x06\xbd<")  # 0x9b06bd3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_beam_combo))

        data.write(b"mqr\xbf")  # 0x6d7172bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_beam_combo))

        data.write(b"\x16\xd8\x9a\xcc")  # 0x16d89acc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.annihilator_beam_combo))

        data.write(b"\xea\x86\xa2\xb9")  # 0xea86a2b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.charge_combo_upgrade))

        data.write(b"&\xa5\xe3\xc1")  # 0x26a5e3c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.combat_visor))

        data.write(b"\x9d\xe8s\x1d")  # 0x9de8731d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.scan_visor))

        data.write(b";\n\xb1\x0b")  # 0x3b0ab10b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_visor))

        data.write(b"\x95\xa3\x04\x88")  # 0x95a30488
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.echo_visor))

        data.write(b"\n\xb6\x03\xf7")  # 0xab603f7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.varia_suit))

        data.write(b"M\xa5R\x82")  # 0x4da55282
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_suit))

        data.write(b"\xb4\xfd\x86\x8f")  # 0xb4fd868f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_suit))

        data.write(b">\xc5\xa9\xf5")  # 0x3ec5a9f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.morph_ball))

        data.write(b"\x8c\x98$}")  # 0x8c98247d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.boost_ball))

        data.write(b"\xbd\x8bT|")  # 0xbd8b547c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.spider_ball))

        data.write(b"S8v\x89")  # 0x53387689
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.bomb))

        data.write(b"W\xeb\x9e\x8b")  # 0x57eb9e8b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_bomb))

        data.write(b"\xae\xb3J\x86")  # 0xaeb34a86
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_bomb))

        data.write(b"\xfb3\xf2\xa1")  # 0xfb33f2a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.annihilator_bomb))

        data.write(b"K\x15\xeb\x9a")  # 0x4b15eb9a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.charge_upgrade))

        data.write(b"D\xfb\xb1\x9c")  # 0x44fbb19c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grapple_beam))

        data.write(b"\xf5[\xe1,")  # 0xf55be12c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.double_jump))

        data.write(b"\xbc%\xca\xed")  # 0xbc25caed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.gravity_boost))

        data.write(b"\nk7o")  # 0xa6b376f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.seeker))

        data.write(b"\xd8\xa9\xbb\xcb")  # 0xd8a9bbcb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.screw_attack))

        data.write(b"}\x1c\x96\x85")  # 0x7d1c9685
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.translator_upgrade))

        data.write(b"\x8fl\xdc\xf9")  # 0x8f6cdcf9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key1))

        data.write(b"\x9d\xd9s\x17")  # 0x9dd97317
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key2))

        data.write(b"%e\x14r")  # 0x25651472
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key3))

        data.write(b"\xb8\xb2,\xcb")  # 0xb8b22ccb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key4))

        data.write(b"\x00\x0eK\xae")  # 0xe4bae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key5))

        data.write(b"\x12\xbb\xe4@")  # 0x12bbe440
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key6))

        data.write(b"\xaa\x07\x83%")  # 0xaa078325
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key7))

        data.write(b"\xf2d\x93s")  # 0xf2649373
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key8))

        data.write(b"J\xd8\xf4\x16")  # 0x4ad8f416
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.temple_key9))

        data.write(b"\xc2q\xcf\xbc")  # 0xc271cfbc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sand_key1))

        data.write(b"\xd0\xc4`R")  # 0xd0c46052
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sand_key2))

        data.write(b"hx\x077")  # 0x68780737
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sand_key3))

        data.write(b"n\xff\xcf\x82")  # 0x6effcf82
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.swamp_key1))

        data.write(b"|J`l")  # 0x7c4a606c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.swamp_key2))

        data.write(b"\xc4\xf6\x07\t")  # 0xc4f60709
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.swamp_key3))

        data.write(b"\xc2\rb+")  # 0xc20d622b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.cliffside_key1))

        data.write(b"\xd0\xb8\xcd\xc5")  # 0xd0b8cdc5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.cliffside_key2))

        data.write(b"h\x04\xaa\xa0")  # 0x6804aaa0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.cliffside_key3))

        data.write(b"\x01\xc3\x97\xf0")  # 0x1c397f0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.energy))

        data.write(b"\xfco\x86\x0c")  # 0xfc6f860c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.energy_tank))

        data.write(b"\x16\x18\x98\xdc")  # 0x161898dc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x161898dc))

        data.write(b"\xa6\xc2\x9b\x8d")  # 0xa6c29b8d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.power_bomb))

        data.write(b"\xec\x7f\xb0\xef")  # 0xec7fb0ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.missile))

        data.write(b"\xfc\xec\xf7D")  # 0xfcecf744
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_beam_ammo))

        data.write(b"2\x05/\x91")  # 0x32052f91
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_beam_ammo))

        data.write(b"n@8\xab")  # 0x6e4038ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.percentage_increase))

        data.write(b"\x148z\xab")  # 0x14387aab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.misc_counter1))

        data.write(b"\x06\x8d\xd5E")  # 0x68dd545
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.misc_counter2))

        data.write(b"\xbe1\xb2 ")  # 0xbe31b220
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.misc_counter3))

        data.write(b"#\xe6\x8a\x99")  # 0x23e68a99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.misc_counter4))

        data.write(b"\x8e\xcbfe")  # 0x8ecb6665
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_power_beam))

        data.write(b"\x92\xc4\x02\xab")  # 0x92c402ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_dark_beam))

        data.write(b"\x7f\xe2cc")  # 0x7fe26363
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_light_beam))

        data.write(b"\xd7\xf8Xj")  # 0xd7f8586a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_annihilator_beam))

        data.write(b"'\xd2T\xaf")  # 0x27d254af
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.multi_charge_upgrade))

        data.write(b"\x19\x92d ")  # 0x19926420
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.invisibility))

        data.write(b"\xce(L\t")  # 0xce284c09
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.amplified_damage))

        data.write(b"\xde\xc9\x99\xc3")  # 0xdec999c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.invincibility))

        data.write(b"f\xae3\x8e")  # 0x66ae338e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x66ae338e))

        data.write(b"!\x0eI^")  # 0x210e495e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x210e495e))

        data.write(b"\x1cn`\xee")  # 0x1c6e60ee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x1c6e60ee))

        data.write(b"\xaeN\xbc\xfe")  # 0xae4ebcfe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xae4ebcfe))

        data.write(b"SQ\xdb\xa5")  # 0x5351dba5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.frag_count))

        data.write(b"\x02\xdb\x9a\n")  # 0x2db9a0a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.died_count))

        data.write(b"{\x98\x06Q")  # 0x7b980651
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.archenemy_count))

        data.write(b"\xe9\x86\x1cI")  # 0xe9861c49
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter1))

        data.write(b"\xfb3\xb3\xa7")  # 0xfb33b3a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter2))

        data.write(b"C\x8f\xd4\xc2")  # 0x438fd4c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter3))

        data.write(b"\xdeX\xec{")  # 0xde58ec7b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter4))

        data.write(b"f\xe4\x8b\x1e")  # 0x66e48b1e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter5))

        data.write(b"tQ$\xf0")  # 0x745124f0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter6))

        data.write(b"\xcc\xedC\x95")  # 0xcced4395
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter7))

        data.write(b"\x94\x8eS\xc3")  # 0x948e53c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.persistent_counter8))

        data.write(b"\xd48\xf8\xe4")  # 0xd438f8e4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_combat_visor))

        data.write(b"\x89\xe9P\xc4")  # 0x89e950c4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_scan_visor))

        data.write(b"/\x0b\x92\xd2")  # 0x2f0b92d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_dark_visor))

        data.write(b"\x81\xa2'Q")  # 0x81a22751
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.change_to_echo_visor))

        data.write(b"\xdb\x8f\x0e\x87")  # 0xdb8f0e87
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_amplifier))

        data.write(b"\xafo6\x1a")  # 0xaf6f361a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_counter))

        data.write(b"\xae\x8d\xee\x81")  # 0xae8dee81
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unlimited_missiles))

        data.write(b"\xd1\xff\xb4\x9f")  # 0xd1ffb49f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unlimited_beam_ammo))

        data.write(b"\xbcQ\xdeK")  # 0xbc51de4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_shield))

        data.write(b"\x88AO\x93")  # 0x88414f93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_shield))

        data.write(b"\xfb\xe2\x15\x90")  # 0xfbe21590
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.absorb_attack))

        data.write(b"\xd0\xb6\xa0\x07")  # 0xd0b6a007
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.death_ball))

        data.write(b"\xc4XH\xfe")  # 0xc45848fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.scan_virus))

        data.write(b"\x92\xb9\x16\xd7")  # 0x92b916d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.visor_static))

        data.write(b"\xa6%|\xd8")  # 0xa6257cd8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.beam_weapons_disabled))

        data.write(b"k\xf2L$")  # 0x6bf24c24
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.missile_weapons_disabled))

        data.write(b"2\xf5\xe9\x18")  # 0x32f5e918
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x32f5e918))

        data.write(b"\x1c\xe9UA")  # 0x1ce95541
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.disable_ball))

        data.write(b"]\xd9\x00M")  # 0x5dd9004d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.disable_double_jump))

        data.write(b"\xf6O\x1d\xbd")  # 0xf64f1dbd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.activate_morphball_boost))

        data.write(b"v\x00\r\x1e")  # 0x76000d1e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.hacked_effect))

        data.write(b"\x85\xabR\xbc")  # 0x85ab52bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.activate_morphball_damage))

        data.write(b"q\x1c\x15\x0f")  # 0x711c150f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.translator_upgrade1))

        data.write(b"c\xa9\xba\xe1")  # 0x63a9bae1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.translator_upgrade2))

        data.write(b"\xdb\x15\xdd\x84")  # 0xdb15dd84
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.translator_upgrade3))

        data.write(b"F\xc2\xe5=")  # 0x46c2e53d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.translator_upgrade4))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpawnPointStructJson", data)
        return cls(
            power_beam=json_data["power_beam"],
            dark_beam=json_data["dark_beam"],
            light_beam=json_data["light_beam"],
            annihilator_beam=json_data["annihilator_beam"],
            power_beam_combo=json_data["power_beam_combo"],
            dark_beam_combo=json_data["dark_beam_combo"],
            light_beam_combo=json_data["light_beam_combo"],
            annihilator_beam_combo=json_data["annihilator_beam_combo"],
            charge_combo_upgrade=json_data["charge_combo_upgrade"],
            combat_visor=json_data["combat_visor"],
            scan_visor=json_data["scan_visor"],
            dark_visor=json_data["dark_visor"],
            echo_visor=json_data["echo_visor"],
            varia_suit=json_data["varia_suit"],
            dark_suit=json_data["dark_suit"],
            light_suit=json_data["light_suit"],
            morph_ball=json_data["morph_ball"],
            boost_ball=json_data["boost_ball"],
            spider_ball=json_data["spider_ball"],
            bomb=json_data["bomb"],
            light_bomb=json_data["light_bomb"],
            dark_bomb=json_data["dark_bomb"],
            annihilator_bomb=json_data["annihilator_bomb"],
            charge_upgrade=json_data["charge_upgrade"],
            grapple_beam=json_data["grapple_beam"],
            double_jump=json_data["double_jump"],
            gravity_boost=json_data["gravity_boost"],
            seeker=json_data["seeker"],
            screw_attack=json_data["screw_attack"],
            translator_upgrade=json_data["translator_upgrade"],
            temple_key1=json_data["temple_key1"],
            temple_key2=json_data["temple_key2"],
            temple_key3=json_data["temple_key3"],
            temple_key4=json_data["temple_key4"],
            temple_key5=json_data["temple_key5"],
            temple_key6=json_data["temple_key6"],
            temple_key7=json_data["temple_key7"],
            temple_key8=json_data["temple_key8"],
            temple_key9=json_data["temple_key9"],
            sand_key1=json_data["sand_key1"],
            sand_key2=json_data["sand_key2"],
            sand_key3=json_data["sand_key3"],
            swamp_key1=json_data["swamp_key1"],
            swamp_key2=json_data["swamp_key2"],
            swamp_key3=json_data["swamp_key3"],
            cliffside_key1=json_data["cliffside_key1"],
            cliffside_key2=json_data["cliffside_key2"],
            cliffside_key3=json_data["cliffside_key3"],
            energy=json_data["energy"],
            energy_tank=json_data["energy_tank"],
            unknown_0x161898dc=json_data["unknown_0x161898dc"],
            power_bomb=json_data["power_bomb"],
            missile=json_data["missile"],
            dark_beam_ammo=json_data["dark_beam_ammo"],
            light_beam_ammo=json_data["light_beam_ammo"],
            percentage_increase=json_data["percentage_increase"],
            misc_counter1=json_data["misc_counter1"],
            misc_counter2=json_data["misc_counter2"],
            misc_counter3=json_data["misc_counter3"],
            misc_counter4=json_data["misc_counter4"],
            change_to_power_beam=json_data["change_to_power_beam"],
            change_to_dark_beam=json_data["change_to_dark_beam"],
            change_to_light_beam=json_data["change_to_light_beam"],
            change_to_annihilator_beam=json_data["change_to_annihilator_beam"],
            multi_charge_upgrade=json_data["multi_charge_upgrade"],
            invisibility=json_data["invisibility"],
            amplified_damage=json_data["amplified_damage"],
            invincibility=json_data["invincibility"],
            unknown_0x66ae338e=json_data["unknown_0x66ae338e"],
            unknown_0x210e495e=json_data["unknown_0x210e495e"],
            unknown_0x1c6e60ee=json_data["unknown_0x1c6e60ee"],
            unknown_0xae4ebcfe=json_data["unknown_0xae4ebcfe"],
            frag_count=json_data["frag_count"],
            died_count=json_data["died_count"],
            archenemy_count=json_data["archenemy_count"],
            persistent_counter1=json_data["persistent_counter1"],
            persistent_counter2=json_data["persistent_counter2"],
            persistent_counter3=json_data["persistent_counter3"],
            persistent_counter4=json_data["persistent_counter4"],
            persistent_counter5=json_data["persistent_counter5"],
            persistent_counter6=json_data["persistent_counter6"],
            persistent_counter7=json_data["persistent_counter7"],
            persistent_counter8=json_data["persistent_counter8"],
            change_to_combat_visor=json_data["change_to_combat_visor"],
            change_to_scan_visor=json_data["change_to_scan_visor"],
            change_to_dark_visor=json_data["change_to_dark_visor"],
            change_to_echo_visor=json_data["change_to_echo_visor"],
            coin_amplifier=json_data["coin_amplifier"],
            coin_counter=json_data["coin_counter"],
            unlimited_missiles=json_data["unlimited_missiles"],
            unlimited_beam_ammo=json_data["unlimited_beam_ammo"],
            dark_shield=json_data["dark_shield"],
            light_shield=json_data["light_shield"],
            absorb_attack=json_data["absorb_attack"],
            death_ball=json_data["death_ball"],
            scan_virus=json_data["scan_virus"],
            visor_static=json_data["visor_static"],
            beam_weapons_disabled=json_data["beam_weapons_disabled"],
            missile_weapons_disabled=json_data["missile_weapons_disabled"],
            unknown_0x32f5e918=json_data["unknown_0x32f5e918"],
            disable_ball=json_data["disable_ball"],
            disable_double_jump=json_data["disable_double_jump"],
            activate_morphball_boost=json_data["activate_morphball_boost"],
            hacked_effect=json_data["hacked_effect"],
            activate_morphball_damage=json_data["activate_morphball_damage"],
            translator_upgrade1=json_data["translator_upgrade1"],
            translator_upgrade2=json_data["translator_upgrade2"],
            translator_upgrade3=json_data["translator_upgrade3"],
            translator_upgrade4=json_data["translator_upgrade4"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "power_beam": self.power_beam,
            "dark_beam": self.dark_beam,
            "light_beam": self.light_beam,
            "annihilator_beam": self.annihilator_beam,
            "power_beam_combo": self.power_beam_combo,
            "dark_beam_combo": self.dark_beam_combo,
            "light_beam_combo": self.light_beam_combo,
            "annihilator_beam_combo": self.annihilator_beam_combo,
            "charge_combo_upgrade": self.charge_combo_upgrade,
            "combat_visor": self.combat_visor,
            "scan_visor": self.scan_visor,
            "dark_visor": self.dark_visor,
            "echo_visor": self.echo_visor,
            "varia_suit": self.varia_suit,
            "dark_suit": self.dark_suit,
            "light_suit": self.light_suit,
            "morph_ball": self.morph_ball,
            "boost_ball": self.boost_ball,
            "spider_ball": self.spider_ball,
            "bomb": self.bomb,
            "light_bomb": self.light_bomb,
            "dark_bomb": self.dark_bomb,
            "annihilator_bomb": self.annihilator_bomb,
            "charge_upgrade": self.charge_upgrade,
            "grapple_beam": self.grapple_beam,
            "double_jump": self.double_jump,
            "gravity_boost": self.gravity_boost,
            "seeker": self.seeker,
            "screw_attack": self.screw_attack,
            "translator_upgrade": self.translator_upgrade,
            "temple_key1": self.temple_key1,
            "temple_key2": self.temple_key2,
            "temple_key3": self.temple_key3,
            "temple_key4": self.temple_key4,
            "temple_key5": self.temple_key5,
            "temple_key6": self.temple_key6,
            "temple_key7": self.temple_key7,
            "temple_key8": self.temple_key8,
            "temple_key9": self.temple_key9,
            "sand_key1": self.sand_key1,
            "sand_key2": self.sand_key2,
            "sand_key3": self.sand_key3,
            "swamp_key1": self.swamp_key1,
            "swamp_key2": self.swamp_key2,
            "swamp_key3": self.swamp_key3,
            "cliffside_key1": self.cliffside_key1,
            "cliffside_key2": self.cliffside_key2,
            "cliffside_key3": self.cliffside_key3,
            "energy": self.energy,
            "energy_tank": self.energy_tank,
            "unknown_0x161898dc": self.unknown_0x161898dc,
            "power_bomb": self.power_bomb,
            "missile": self.missile,
            "dark_beam_ammo": self.dark_beam_ammo,
            "light_beam_ammo": self.light_beam_ammo,
            "percentage_increase": self.percentage_increase,
            "misc_counter1": self.misc_counter1,
            "misc_counter2": self.misc_counter2,
            "misc_counter3": self.misc_counter3,
            "misc_counter4": self.misc_counter4,
            "change_to_power_beam": self.change_to_power_beam,
            "change_to_dark_beam": self.change_to_dark_beam,
            "change_to_light_beam": self.change_to_light_beam,
            "change_to_annihilator_beam": self.change_to_annihilator_beam,
            "multi_charge_upgrade": self.multi_charge_upgrade,
            "invisibility": self.invisibility,
            "amplified_damage": self.amplified_damage,
            "invincibility": self.invincibility,
            "unknown_0x66ae338e": self.unknown_0x66ae338e,
            "unknown_0x210e495e": self.unknown_0x210e495e,
            "unknown_0x1c6e60ee": self.unknown_0x1c6e60ee,
            "unknown_0xae4ebcfe": self.unknown_0xae4ebcfe,
            "frag_count": self.frag_count,
            "died_count": self.died_count,
            "archenemy_count": self.archenemy_count,
            "persistent_counter1": self.persistent_counter1,
            "persistent_counter2": self.persistent_counter2,
            "persistent_counter3": self.persistent_counter3,
            "persistent_counter4": self.persistent_counter4,
            "persistent_counter5": self.persistent_counter5,
            "persistent_counter6": self.persistent_counter6,
            "persistent_counter7": self.persistent_counter7,
            "persistent_counter8": self.persistent_counter8,
            "change_to_combat_visor": self.change_to_combat_visor,
            "change_to_scan_visor": self.change_to_scan_visor,
            "change_to_dark_visor": self.change_to_dark_visor,
            "change_to_echo_visor": self.change_to_echo_visor,
            "coin_amplifier": self.coin_amplifier,
            "coin_counter": self.coin_counter,
            "unlimited_missiles": self.unlimited_missiles,
            "unlimited_beam_ammo": self.unlimited_beam_ammo,
            "dark_shield": self.dark_shield,
            "light_shield": self.light_shield,
            "absorb_attack": self.absorb_attack,
            "death_ball": self.death_ball,
            "scan_virus": self.scan_virus,
            "visor_static": self.visor_static,
            "beam_weapons_disabled": self.beam_weapons_disabled,
            "missile_weapons_disabled": self.missile_weapons_disabled,
            "unknown_0x32f5e918": self.unknown_0x32f5e918,
            "disable_ball": self.disable_ball,
            "disable_double_jump": self.disable_double_jump,
            "activate_morphball_boost": self.activate_morphball_boost,
            "hacked_effect": self.hacked_effect,
            "activate_morphball_damage": self.activate_morphball_damage,
            "translator_upgrade1": self.translator_upgrade1,
            "translator_upgrade2": self.translator_upgrade2,
            "translator_upgrade3": self.translator_upgrade3,
            "translator_upgrade4": self.translator_upgrade4,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x9ACA45BC: ("power_beam", structs.decode_BIG_l),
    0x92BB94B7: ("dark_beam", structs.decode_BIG_l),
    0x6BE340BA: ("light_beam", structs.decode_BIG_l),
    0xC73B2C90: ("annihilator_beam", structs.decode_BIG_l),
    0xEFD4DABE: ("power_beam_combo", structs.decode_BIG_l),
    0x9B06BD3C: ("dark_beam_combo", structs.decode_BIG_l),
    0x6D7172BF: ("light_beam_combo", structs.decode_BIG_l),
    0x16D89ACC: ("annihilator_beam_combo", structs.decode_BIG_l),
    0xEA86A2B9: ("charge_combo_upgrade", structs.decode_BIG_l),
    0x26A5E3C1: ("combat_visor", structs.decode_BIG_l),
    0x9DE8731D: ("scan_visor", structs.decode_BIG_l),
    0x3B0AB10B: ("dark_visor", structs.decode_BIG_l),
    0x95A30488: ("echo_visor", structs.decode_BIG_l),
    0x0AB603F7: ("varia_suit", structs.decode_BIG_l),
    0x4DA55282: ("dark_suit", structs.decode_BIG_l),
    0xB4FD868F: ("light_suit", structs.decode_BIG_l),
    0x3EC5A9F5: ("morph_ball", structs.decode_BIG_l),
    0x8C98247D: ("boost_ball", structs.decode_BIG_l),
    0xBD8B547C: ("spider_ball", structs.decode_BIG_l),
    0x53387689: ("bomb", structs.decode_BIG_l),
    0x57EB9E8B: ("light_bomb", structs.decode_BIG_l),
    0xAEB34A86: ("dark_bomb", structs.decode_BIG_l),
    0xFB33F2A1: ("annihilator_bomb", structs.decode_BIG_l),
    0x4B15EB9A: ("charge_upgrade", structs.decode_BIG_L),
    0x44FBB19C: ("grapple_beam", structs.decode_BIG_l),
    0xF55BE12C: ("double_jump", structs.decode_BIG_l),
    0xBC25CAED: ("gravity_boost", structs.decode_BIG_l),
    0x0A6B376F: ("seeker", structs.decode_BIG_l),
    0xD8A9BBCB: ("screw_attack", structs.decode_BIG_l),
    0x7D1C9685: ("translator_upgrade", structs.decode_BIG_l),
    0x8F6CDCF9: ("temple_key1", structs.decode_BIG_l),
    0x9DD97317: ("temple_key2", structs.decode_BIG_l),
    0x25651472: ("temple_key3", structs.decode_BIG_l),
    0xB8B22CCB: ("temple_key4", structs.decode_BIG_l),
    0x000E4BAE: ("temple_key5", structs.decode_BIG_l),
    0x12BBE440: ("temple_key6", structs.decode_BIG_l),
    0xAA078325: ("temple_key7", structs.decode_BIG_l),
    0xF2649373: ("temple_key8", structs.decode_BIG_l),
    0x4AD8F416: ("temple_key9", structs.decode_BIG_l),
    0xC271CFBC: ("sand_key1", structs.decode_BIG_l),
    0xD0C46052: ("sand_key2", structs.decode_BIG_l),
    0x68780737: ("sand_key3", structs.decode_BIG_l),
    0x6EFFCF82: ("swamp_key1", structs.decode_BIG_l),
    0x7C4A606C: ("swamp_key2", structs.decode_BIG_l),
    0xC4F60709: ("swamp_key3", structs.decode_BIG_l),
    0xC20D622B: ("cliffside_key1", structs.decode_BIG_l),
    0xD0B8CDC5: ("cliffside_key2", structs.decode_BIG_l),
    0x6804AAA0: ("cliffside_key3", structs.decode_BIG_l),
    0x01C397F0: ("energy", structs.decode_BIG_l),
    0xFC6F860C: ("energy_tank", structs.decode_BIG_l),
    0x161898DC: ("unknown_0x161898dc", structs.decode_BIG_l),
    0xA6C29B8D: ("power_bomb", structs.decode_BIG_l),
    0xEC7FB0EF: ("missile", structs.decode_BIG_l),
    0xFCECF744: ("dark_beam_ammo", structs.decode_BIG_l),
    0x32052F91: ("light_beam_ammo", structs.decode_BIG_l),
    0x6E4038AB: ("percentage_increase", structs.decode_BIG_l),
    0x14387AAB: ("misc_counter1", structs.decode_BIG_l),
    0x068DD545: ("misc_counter2", structs.decode_BIG_l),
    0xBE31B220: ("misc_counter3", structs.decode_BIG_l),
    0x23E68A99: ("misc_counter4", structs.decode_BIG_l),
    0x8ECB6665: ("change_to_power_beam", structs.decode_BIG_l),
    0x92C402AB: ("change_to_dark_beam", structs.decode_BIG_l),
    0x7FE26363: ("change_to_light_beam", structs.decode_BIG_l),
    0xD7F8586A: ("change_to_annihilator_beam", structs.decode_BIG_l),
    0x27D254AF: ("multi_charge_upgrade", structs.decode_BIG_l),
    0x19926420: ("invisibility", structs.decode_BIG_l),
    0xCE284C09: ("amplified_damage", structs.decode_BIG_l),
    0xDEC999C3: ("invincibility", structs.decode_BIG_l),
    0x66AE338E: ("unknown_0x66ae338e", structs.decode_BIG_l),
    0x210E495E: ("unknown_0x210e495e", structs.decode_BIG_l),
    0x1C6E60EE: ("unknown_0x1c6e60ee", structs.decode_BIG_l),
    0xAE4EBCFE: ("unknown_0xae4ebcfe", structs.decode_BIG_l),
    0x5351DBA5: ("frag_count", structs.decode_BIG_l),
    0x02DB9A0A: ("died_count", structs.decode_BIG_l),
    0x7B980651: ("archenemy_count", structs.decode_BIG_l),
    0xE9861C49: ("persistent_counter1", structs.decode_BIG_l),
    0xFB33B3A7: ("persistent_counter2", structs.decode_BIG_l),
    0x438FD4C2: ("persistent_counter3", structs.decode_BIG_l),
    0xDE58EC7B: ("persistent_counter4", structs.decode_BIG_l),
    0x66E48B1E: ("persistent_counter5", structs.decode_BIG_l),
    0x745124F0: ("persistent_counter6", structs.decode_BIG_l),
    0xCCED4395: ("persistent_counter7", structs.decode_BIG_l),
    0x948E53C3: ("persistent_counter8", structs.decode_BIG_l),
    0xD438F8E4: ("change_to_combat_visor", structs.decode_BIG_l),
    0x89E950C4: ("change_to_scan_visor", structs.decode_BIG_l),
    0x2F0B92D2: ("change_to_dark_visor", structs.decode_BIG_l),
    0x81A22751: ("change_to_echo_visor", structs.decode_BIG_l),
    0xDB8F0E87: ("coin_amplifier", structs.decode_BIG_l),
    0xAF6F361A: ("coin_counter", structs.decode_BIG_l),
    0xAE8DEE81: ("unlimited_missiles", structs.decode_BIG_l),
    0xD1FFB49F: ("unlimited_beam_ammo", structs.decode_BIG_l),
    0xBC51DE4B: ("dark_shield", structs.decode_BIG_l),
    0x88414F93: ("light_shield", structs.decode_BIG_l),
    0xFBE21590: ("absorb_attack", structs.decode_BIG_l),
    0xD0B6A007: ("death_ball", structs.decode_BIG_l),
    0xC45848FE: ("scan_virus", structs.decode_BIG_l),
    0x92B916D7: ("visor_static", structs.decode_BIG_l),
    0xA6257CD8: ("beam_weapons_disabled", structs.decode_BIG_l),
    0x6BF24C24: ("missile_weapons_disabled", structs.decode_BIG_l),
    0x32F5E918: ("unknown_0x32f5e918", structs.decode_BIG_l),
    0x1CE95541: ("disable_ball", structs.decode_BIG_l),
    0x5DD9004D: ("disable_double_jump", structs.decode_BIG_l),
    0xF64F1DBD: ("activate_morphball_boost", structs.decode_BIG_l),
    0x76000D1E: ("hacked_effect", structs.decode_BIG_l),
    0x85AB52BC: ("activate_morphball_damage", structs.decode_BIG_l),
    0x711C150F: ("translator_upgrade1", structs.decode_BIG_l),
    0x63A9BAE1: ("translator_upgrade2", structs.decode_BIG_l),
    0xDB15DD84: ("translator_upgrade3", structs.decode_BIG_l),
    0x46C2E53D: ("translator_upgrade4", structs.decode_BIG_l),
}
