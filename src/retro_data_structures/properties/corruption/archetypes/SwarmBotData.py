# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.SwarmSoundData import SwarmSoundData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SwarmBotDataJson(typing_extensions.TypedDict):
        unknown_0x6315837d: int
        unknown_0x6c605925: int
        unknown_0x37ded7f2: bool
        unknown_0xcab4e0b3: int
        unknown_0xb3fbffc8: float
        part_0xb07a5895: int
        part_0xa3b64d8c: int
        part_0xa5b4ed57: int
        bot_vulnerability_effect: int
        unknown_0x056b2de2: bool
        unknown_0x14eddffc: bool
        can_spin_attack: bool
        unknown_0x46f96675: bool
        unknown_0xe6c41f91: bool
        unknown_0x204b8e19: float
        unknown_0xbf0f6889: float
        damage_info_0x1e054e04: json_util.JsonObject
        dive_bomb_damage: json_util.JsonObject
        pulse_projectile: int
        pulse_projectile_damage: json_util.JsonObject
        damage_info_0x4d19c32e: json_util.JsonObject
        damage_info_0x840ba904: json_util.JsonObject
        part_0xaf7ffe63: int
        electric_effect: int
        elsc: int
        part_0xf2dc8618: int
        part_0xd53f059b: int
        death_explosion: int
        sound_locomotion_looped: json_util.JsonObject
        swarm_sound_data_0x9c04df2f: json_util.JsonObject
        swarm_sound_data_0x8d79b556: json_util.JsonObject
        caud_0xeb9a9949: int
        sound_form_pulse_ring: int
        sound_fire_pulse_ring: int
        sound_break_pulse_ring: int
        sound_form_circ_saw: int
        sound_circ_saw_dive: int
        sound_circ_saw_hit_ground: int
        sound_circ_saw_hit_player: int
        sound_form_electric_eel: int
        caud_0x84360d80: int
        caud_0xd2be3af7: int
        splash_sound_small: int
        sound_break_electric_eel: int
        sound_swarm_broken: int
        sound_swarm_bot_stunned: int
        timing_constraint_duration: float
        sound_swarm_bot_begin_dive: int
        sound_swarm_bot_killed: int
        sound_swarm_bot_explosion: int


@dataclasses.dataclass()
class SwarmBotData(BaseProperty):
    unknown_0x6315837d: int = dataclasses.field(
        default=8,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6315837D, original_name="Unknown"),
        },
    )
    unknown_0x6c605925: int = dataclasses.field(
        default=8,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6C605925, original_name="Unknown"),
        },
    )
    unknown_0x37ded7f2: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x37DED7F2, original_name="Unknown"),
        },
    )
    unknown_0xcab4e0b3: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCAB4E0B3, original_name="Unknown"),
        },
    )
    unknown_0xb3fbffc8: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB3FBFFC8, original_name="Unknown"),
        },
    )
    part_0xb07a5895: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB07A5895, original_name="PART"),
        },
    )
    part_0xa3b64d8c: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA3B64D8C, original_name="PART"),
        },
    )
    part_0xa5b4ed57: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA5B4ED57, original_name="PART"),
        },
    )
    bot_vulnerability_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x10CBC9FD, original_name="BotVulnerabilityEffect"),
        },
    )
    unknown_0x056b2de2: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x056B2DE2, original_name="Unknown"),
        },
    )
    unknown_0x14eddffc: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x14EDDFFC, original_name="Unknown"),
        },
    )
    can_spin_attack: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9BC4FC8D, original_name="CanSpinAttack"),
        },
    )
    unknown_0x46f96675: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x46F96675, original_name="Unknown"),
        },
    )
    unknown_0xe6c41f91: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE6C41F91, original_name="Unknown"),
        },
    )
    unknown_0x204b8e19: float = dataclasses.field(
        default=28.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x204B8E19, original_name="Unknown"),
        },
    )
    unknown_0xbf0f6889: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF0F6889, original_name="Unknown"),
        },
    )
    damage_info_0x1e054e04: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1E054E04,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    dive_bomb_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xBC7B9832,
                original_name="DiveBombDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    pulse_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2B309650, original_name="PulseProjectile"),
        },
    )
    pulse_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x3C8B534D,
                original_name="PulseProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x4d19c32e: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4D19C32E,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x840ba904: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x840BA904,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    part_0xaf7ffe63: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAF7FFE63, original_name="PART"),
        },
    )
    electric_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x49FAE143, original_name="ElectricEffect"),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x570AA8F2, original_name="ELSC"),
        },
    )
    part_0xf2dc8618: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF2DC8618, original_name="PART"),
        },
    )
    part_0xd53f059b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD53F059B, original_name="PART"),
        },
    )
    death_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0687C33E, original_name="DeathExplosion"),
        },
    )
    sound_locomotion_looped: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x13F55169,
                original_name="Sound_LocomotionLooped",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    swarm_sound_data_0x9c04df2f: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x9C04DF2F,
                original_name="SwarmSoundData",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    swarm_sound_data_0x8d79b556: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x8D79B556,
                original_name="SwarmSoundData",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    caud_0xeb9a9949: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEB9A9949, original_name="CAUD"),
        },
    )
    sound_form_pulse_ring: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC3DE457E, original_name="Sound_FormPulseRing"),
        },
    )
    sound_fire_pulse_ring: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAB633EF1, original_name="Sound_FirePulseRing"),
        },
    )
    sound_break_pulse_ring: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2A430EB0, original_name="Sound_BreakPulseRing"),
        },
    )
    sound_form_circ_saw: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAF1768C4, original_name="Sound_FormCircSaw"),
        },
    )
    sound_circ_saw_dive: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x435A0B62, original_name="Sound_CircSawDive"),
        },
    )
    sound_circ_saw_hit_ground: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x13EC5401, original_name="Sound_CircSawHitGround"),
        },
    )
    sound_circ_saw_hit_player: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE5A34FB3, original_name="Sound_CircSawHitPlayer"),
        },
    )
    sound_form_electric_eel: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7B38D80D, original_name="Sound_FormElectricEel"),
        },
    )
    caud_0x84360d80: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x84360D80, original_name="CAUD"),
        },
    )
    caud_0xd2be3af7: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD2BE3AF7, original_name="CAUD"),
        },
    )
    splash_sound_small: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9ECC3D08, original_name="SplashSoundSmall"),
        },
    )
    sound_break_electric_eel: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCF4F5348, original_name="Sound_BreakElectricEel"),
        },
    )
    sound_swarm_broken: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x05117E35, original_name="Sound_SwarmBroken"),
        },
    )
    sound_swarm_bot_stunned: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA53694C2, original_name="Sound_SwarmBotStunned"),
        },
    )
    timing_constraint_duration: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC478968, original_name="TimingConstraintDuration"),
        },
    )
    sound_swarm_bot_begin_dive: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x091CB316, original_name="Sound_SwarmBotBeginDive"),
        },
    )
    sound_swarm_bot_killed: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x358177CC, original_name="Sound_SwarmBotKilled"),
        },
    )
    sound_swarm_bot_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAB3E98B8, original_name="Sound_SwarmBotExplosion"),
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
        if property_count != 50:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6315837D
        unknown_0x6315837d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C605925
        unknown_0x6c605925 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37DED7F2
        unknown_0x37ded7f2 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCAB4E0B3
        unknown_0xcab4e0b3 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3FBFFC8
        unknown_0xb3fbffc8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB07A5895
        part_0xb07a5895 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3B64D8C
        part_0xa3b64d8c = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA5B4ED57
        part_0xa5b4ed57 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10CBC9FD
        bot_vulnerability_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x056B2DE2
        unknown_0x056b2de2 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14EDDFFC
        unknown_0x14eddffc = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9BC4FC8D
        can_spin_attack = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46F96675
        unknown_0x46f96675 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE6C41F91
        unknown_0xe6c41f91 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x204B8E19
        unknown_0x204b8e19 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF0F6889
        unknown_0xbf0f6889 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E054E04
        damage_info_0x1e054e04 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC7B9832
        dive_bomb_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B309650
        pulse_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C8B534D
        pulse_projectile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D19C32E
        damage_info_0x4d19c32e = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x840BA904
        damage_info_0x840ba904 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF7FFE63
        part_0xaf7ffe63 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49FAE143
        electric_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x570AA8F2
        elsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2DC8618
        part_0xf2dc8618 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD53F059B
        part_0xd53f059b = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0687C33E
        death_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13F55169
        sound_locomotion_looped = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C04DF2F
        swarm_sound_data_0x9c04df2f = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D79B556
        swarm_sound_data_0x8d79b556 = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB9A9949
        caud_0xeb9a9949 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3DE457E
        sound_form_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB633EF1
        sound_fire_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A430EB0
        sound_break_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF1768C4
        sound_form_circ_saw = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x435A0B62
        sound_circ_saw_dive = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13EC5401
        sound_circ_saw_hit_ground = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE5A34FB3
        sound_circ_saw_hit_player = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B38D80D
        sound_form_electric_eel = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84360D80
        caud_0x84360d80 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD2BE3AF7
        caud_0xd2be3af7 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ECC3D08
        splash_sound_small = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF4F5348
        sound_break_electric_eel = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05117E35
        sound_swarm_broken = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA53694C2
        sound_swarm_bot_stunned = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC478968
        timing_constraint_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x091CB316
        sound_swarm_bot_begin_dive = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x358177CC
        sound_swarm_bot_killed = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB3E98B8
        sound_swarm_bot_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            unknown_0x6315837d,
            unknown_0x6c605925,
            unknown_0x37ded7f2,
            unknown_0xcab4e0b3,
            unknown_0xb3fbffc8,
            part_0xb07a5895,
            part_0xa3b64d8c,
            part_0xa5b4ed57,
            bot_vulnerability_effect,
            unknown_0x056b2de2,
            unknown_0x14eddffc,
            can_spin_attack,
            unknown_0x46f96675,
            unknown_0xe6c41f91,
            unknown_0x204b8e19,
            unknown_0xbf0f6889,
            damage_info_0x1e054e04,
            dive_bomb_damage,
            pulse_projectile,
            pulse_projectile_damage,
            damage_info_0x4d19c32e,
            damage_info_0x840ba904,
            part_0xaf7ffe63,
            electric_effect,
            elsc,
            part_0xf2dc8618,
            part_0xd53f059b,
            death_explosion,
            sound_locomotion_looped,
            swarm_sound_data_0x9c04df2f,
            swarm_sound_data_0x8d79b556,
            caud_0xeb9a9949,
            sound_form_pulse_ring,
            sound_fire_pulse_ring,
            sound_break_pulse_ring,
            sound_form_circ_saw,
            sound_circ_saw_dive,
            sound_circ_saw_hit_ground,
            sound_circ_saw_hit_player,
            sound_form_electric_eel,
            caud_0x84360d80,
            caud_0xd2be3af7,
            splash_sound_small,
            sound_break_electric_eel,
            sound_swarm_broken,
            sound_swarm_bot_stunned,
            timing_constraint_duration,
            sound_swarm_bot_begin_dive,
            sound_swarm_bot_killed,
            sound_swarm_bot_explosion,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x002")  # 50 properties

        data.write(b"c\x15\x83}")  # 0x6315837d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6315837d))

        data.write(b"l`Y%")  # 0x6c605925
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6c605925))

        data.write(b"7\xde\xd7\xf2")  # 0x37ded7f2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x37ded7f2))

        data.write(b"\xca\xb4\xe0\xb3")  # 0xcab4e0b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xcab4e0b3))

        data.write(b"\xb3\xfb\xff\xc8")  # 0xb3fbffc8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb3fbffc8))

        data.write(b"\xb0zX\x95")  # 0xb07a5895
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xb07a5895))

        data.write(b"\xa3\xb6M\x8c")  # 0xa3b64d8c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xa3b64d8c))

        data.write(b"\xa5\xb4\xedW")  # 0xa5b4ed57
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xa5b4ed57))

        data.write(b"\x10\xcb\xc9\xfd")  # 0x10cbc9fd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.bot_vulnerability_effect))

        data.write(b"\x05k-\xe2")  # 0x56b2de2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x056b2de2))

        data.write(b"\x14\xed\xdf\xfc")  # 0x14eddffc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x14eddffc))

        data.write(b"\x9b\xc4\xfc\x8d")  # 0x9bc4fc8d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_spin_attack))

        data.write(b"F\xf9fu")  # 0x46f96675
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x46f96675))

        data.write(b"\xe6\xc4\x1f\x91")  # 0xe6c41f91
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xe6c41f91))

        data.write(b" K\x8e\x19")  # 0x204b8e19
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x204b8e19))

        data.write(b"\xbf\x0fh\x89")  # 0xbf0f6889
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbf0f6889))

        data.write(b"\x1e\x05N\x04")  # 0x1e054e04
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x1e054e04.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbc{\x982")  # 0xbc7b9832
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dive_bomb_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+0\x96P")  # 0x2b309650
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.pulse_projectile))

        data.write(b"<\x8bSM")  # 0x3c8b534d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.pulse_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"M\x19\xc3.")  # 0x4d19c32e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x4d19c32e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x84\x0b\xa9\x04")  # 0x840ba904
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x840ba904.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaf\x7f\xfec")  # 0xaf7ffe63
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xaf7ffe63))

        data.write(b"I\xfa\xe1C")  # 0x49fae143
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.electric_effect))

        data.write(b"W\n\xa8\xf2")  # 0x570aa8f2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc))

        data.write(b"\xf2\xdc\x86\x18")  # 0xf2dc8618
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xf2dc8618))

        data.write(b"\xd5?\x05\x9b")  # 0xd53f059b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xd53f059b))

        data.write(b"\x06\x87\xc3>")  # 0x687c33e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death_explosion))

        data.write(b"\x13\xf5Qi")  # 0x13f55169
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_locomotion_looped.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9c\x04\xdf/")  # 0x9c04df2f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_sound_data_0x9c04df2f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8dy\xb5V")  # 0x8d79b556
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_sound_data_0x8d79b556.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xeb\x9a\x99I")  # 0xeb9a9949
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xeb9a9949))

        data.write(b"\xc3\xdeE~")  # 0xc3de457e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_form_pulse_ring))

        data.write(b"\xabc>\xf1")  # 0xab633ef1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_fire_pulse_ring))

        data.write(b"*C\x0e\xb0")  # 0x2a430eb0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_break_pulse_ring))

        data.write(b"\xaf\x17h\xc4")  # 0xaf1768c4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_form_circ_saw))

        data.write(b"CZ\x0bb")  # 0x435a0b62
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_circ_saw_dive))

        data.write(b"\x13\xecT\x01")  # 0x13ec5401
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_circ_saw_hit_ground))

        data.write(b"\xe5\xa3O\xb3")  # 0xe5a34fb3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_circ_saw_hit_player))

        data.write(b"{8\xd8\r")  # 0x7b38d80d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_form_electric_eel))

        data.write(b"\x846\r\x80")  # 0x84360d80
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x84360d80))

        data.write(b"\xd2\xbe:\xf7")  # 0xd2be3af7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xd2be3af7))

        data.write(b"\x9e\xcc=\x08")  # 0x9ecc3d08
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_small))

        data.write(b"\xcfOSH")  # 0xcf4f5348
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_break_electric_eel))

        data.write(b"\x05\x11~5")  # 0x5117e35
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_broken))

        data.write(b"\xa56\x94\xc2")  # 0xa53694c2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_stunned))

        data.write(b"\xdcG\x89h")  # 0xdc478968
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.timing_constraint_duration))

        data.write(b"\t\x1c\xb3\x16")  # 0x91cb316
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_begin_dive))

        data.write(b"5\x81w\xcc")  # 0x358177cc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_killed))

        data.write(b"\xab>\x98\xb8")  # 0xab3e98b8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_explosion))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwarmBotDataJson", data)
        return cls(
            unknown_0x6315837d=json_data["unknown_0x6315837d"],
            unknown_0x6c605925=json_data["unknown_0x6c605925"],
            unknown_0x37ded7f2=json_data["unknown_0x37ded7f2"],
            unknown_0xcab4e0b3=json_data["unknown_0xcab4e0b3"],
            unknown_0xb3fbffc8=json_data["unknown_0xb3fbffc8"],
            part_0xb07a5895=json_data["part_0xb07a5895"],
            part_0xa3b64d8c=json_data["part_0xa3b64d8c"],
            part_0xa5b4ed57=json_data["part_0xa5b4ed57"],
            bot_vulnerability_effect=json_data["bot_vulnerability_effect"],
            unknown_0x056b2de2=json_data["unknown_0x056b2de2"],
            unknown_0x14eddffc=json_data["unknown_0x14eddffc"],
            can_spin_attack=json_data["can_spin_attack"],
            unknown_0x46f96675=json_data["unknown_0x46f96675"],
            unknown_0xe6c41f91=json_data["unknown_0xe6c41f91"],
            unknown_0x204b8e19=json_data["unknown_0x204b8e19"],
            unknown_0xbf0f6889=json_data["unknown_0xbf0f6889"],
            damage_info_0x1e054e04=DamageInfo.from_json(json_data["damage_info_0x1e054e04"]),
            dive_bomb_damage=DamageInfo.from_json(json_data["dive_bomb_damage"]),
            pulse_projectile=json_data["pulse_projectile"],
            pulse_projectile_damage=DamageInfo.from_json(json_data["pulse_projectile_damage"]),
            damage_info_0x4d19c32e=DamageInfo.from_json(json_data["damage_info_0x4d19c32e"]),
            damage_info_0x840ba904=DamageInfo.from_json(json_data["damage_info_0x840ba904"]),
            part_0xaf7ffe63=json_data["part_0xaf7ffe63"],
            electric_effect=json_data["electric_effect"],
            elsc=json_data["elsc"],
            part_0xf2dc8618=json_data["part_0xf2dc8618"],
            part_0xd53f059b=json_data["part_0xd53f059b"],
            death_explosion=json_data["death_explosion"],
            sound_locomotion_looped=SwarmSoundData.from_json(json_data["sound_locomotion_looped"]),
            swarm_sound_data_0x9c04df2f=SwarmSoundData.from_json(json_data["swarm_sound_data_0x9c04df2f"]),
            swarm_sound_data_0x8d79b556=SwarmSoundData.from_json(json_data["swarm_sound_data_0x8d79b556"]),
            caud_0xeb9a9949=json_data["caud_0xeb9a9949"],
            sound_form_pulse_ring=json_data["sound_form_pulse_ring"],
            sound_fire_pulse_ring=json_data["sound_fire_pulse_ring"],
            sound_break_pulse_ring=json_data["sound_break_pulse_ring"],
            sound_form_circ_saw=json_data["sound_form_circ_saw"],
            sound_circ_saw_dive=json_data["sound_circ_saw_dive"],
            sound_circ_saw_hit_ground=json_data["sound_circ_saw_hit_ground"],
            sound_circ_saw_hit_player=json_data["sound_circ_saw_hit_player"],
            sound_form_electric_eel=json_data["sound_form_electric_eel"],
            caud_0x84360d80=json_data["caud_0x84360d80"],
            caud_0xd2be3af7=json_data["caud_0xd2be3af7"],
            splash_sound_small=json_data["splash_sound_small"],
            sound_break_electric_eel=json_data["sound_break_electric_eel"],
            sound_swarm_broken=json_data["sound_swarm_broken"],
            sound_swarm_bot_stunned=json_data["sound_swarm_bot_stunned"],
            timing_constraint_duration=json_data["timing_constraint_duration"],
            sound_swarm_bot_begin_dive=json_data["sound_swarm_bot_begin_dive"],
            sound_swarm_bot_killed=json_data["sound_swarm_bot_killed"],
            sound_swarm_bot_explosion=json_data["sound_swarm_bot_explosion"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x6315837d": self.unknown_0x6315837d,
            "unknown_0x6c605925": self.unknown_0x6c605925,
            "unknown_0x37ded7f2": self.unknown_0x37ded7f2,
            "unknown_0xcab4e0b3": self.unknown_0xcab4e0b3,
            "unknown_0xb3fbffc8": self.unknown_0xb3fbffc8,
            "part_0xb07a5895": self.part_0xb07a5895,
            "part_0xa3b64d8c": self.part_0xa3b64d8c,
            "part_0xa5b4ed57": self.part_0xa5b4ed57,
            "bot_vulnerability_effect": self.bot_vulnerability_effect,
            "unknown_0x056b2de2": self.unknown_0x056b2de2,
            "unknown_0x14eddffc": self.unknown_0x14eddffc,
            "can_spin_attack": self.can_spin_attack,
            "unknown_0x46f96675": self.unknown_0x46f96675,
            "unknown_0xe6c41f91": self.unknown_0xe6c41f91,
            "unknown_0x204b8e19": self.unknown_0x204b8e19,
            "unknown_0xbf0f6889": self.unknown_0xbf0f6889,
            "damage_info_0x1e054e04": self.damage_info_0x1e054e04.to_json(),
            "dive_bomb_damage": self.dive_bomb_damage.to_json(),
            "pulse_projectile": self.pulse_projectile,
            "pulse_projectile_damage": self.pulse_projectile_damage.to_json(),
            "damage_info_0x4d19c32e": self.damage_info_0x4d19c32e.to_json(),
            "damage_info_0x840ba904": self.damage_info_0x840ba904.to_json(),
            "part_0xaf7ffe63": self.part_0xaf7ffe63,
            "electric_effect": self.electric_effect,
            "elsc": self.elsc,
            "part_0xf2dc8618": self.part_0xf2dc8618,
            "part_0xd53f059b": self.part_0xd53f059b,
            "death_explosion": self.death_explosion,
            "sound_locomotion_looped": self.sound_locomotion_looped.to_json(),
            "swarm_sound_data_0x9c04df2f": self.swarm_sound_data_0x9c04df2f.to_json(),
            "swarm_sound_data_0x8d79b556": self.swarm_sound_data_0x8d79b556.to_json(),
            "caud_0xeb9a9949": self.caud_0xeb9a9949,
            "sound_form_pulse_ring": self.sound_form_pulse_ring,
            "sound_fire_pulse_ring": self.sound_fire_pulse_ring,
            "sound_break_pulse_ring": self.sound_break_pulse_ring,
            "sound_form_circ_saw": self.sound_form_circ_saw,
            "sound_circ_saw_dive": self.sound_circ_saw_dive,
            "sound_circ_saw_hit_ground": self.sound_circ_saw_hit_ground,
            "sound_circ_saw_hit_player": self.sound_circ_saw_hit_player,
            "sound_form_electric_eel": self.sound_form_electric_eel,
            "caud_0x84360d80": self.caud_0x84360d80,
            "caud_0xd2be3af7": self.caud_0xd2be3af7,
            "splash_sound_small": self.splash_sound_small,
            "sound_break_electric_eel": self.sound_break_electric_eel,
            "sound_swarm_broken": self.sound_swarm_broken,
            "sound_swarm_bot_stunned": self.sound_swarm_bot_stunned,
            "timing_constraint_duration": self.timing_constraint_duration,
            "sound_swarm_bot_begin_dive": self.sound_swarm_bot_begin_dive,
            "sound_swarm_bot_killed": self.sound_swarm_bot_killed,
            "sound_swarm_bot_explosion": self.sound_swarm_bot_explosion,
        }


def _decode_damage_info_0x1e054e04(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_dive_bomb_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_pulse_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x4d19c32e(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x840ba904(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_sound_locomotion_looped(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_swarm_sound_data_0x9c04df2f(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_swarm_sound_data_0x8d79b556(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6315837D: ("unknown_0x6315837d", structs.decode_BIG_l),
    0x6C605925: ("unknown_0x6c605925", structs.decode_BIG_l),
    0x37DED7F2: ("unknown_0x37ded7f2", structs.decode_BIG_bool_),
    0xCAB4E0B3: ("unknown_0xcab4e0b3", structs.decode_BIG_l),
    0xB3FBFFC8: ("unknown_0xb3fbffc8", structs.decode_BIG_f),
    0xB07A5895: ("part_0xb07a5895", structs.decode_BIG_Q),
    0xA3B64D8C: ("part_0xa3b64d8c", structs.decode_BIG_Q),
    0xA5B4ED57: ("part_0xa5b4ed57", structs.decode_BIG_Q),
    0x10CBC9FD: ("bot_vulnerability_effect", structs.decode_BIG_Q),
    0x056B2DE2: ("unknown_0x056b2de2", structs.decode_BIG_bool_),
    0x14EDDFFC: ("unknown_0x14eddffc", structs.decode_BIG_bool_),
    0x9BC4FC8D: ("can_spin_attack", structs.decode_BIG_bool_),
    0x46F96675: ("unknown_0x46f96675", structs.decode_BIG_bool_),
    0xE6C41F91: ("unknown_0xe6c41f91", structs.decode_BIG_bool_),
    0x204B8E19: ("unknown_0x204b8e19", structs.decode_BIG_f),
    0xBF0F6889: ("unknown_0xbf0f6889", structs.decode_BIG_f),
    0x1E054E04: ("damage_info_0x1e054e04", _decode_damage_info_0x1e054e04),
    0xBC7B9832: ("dive_bomb_damage", _decode_dive_bomb_damage),
    0x2B309650: ("pulse_projectile", structs.decode_BIG_Q),
    0x3C8B534D: ("pulse_projectile_damage", _decode_pulse_projectile_damage),
    0x4D19C32E: ("damage_info_0x4d19c32e", _decode_damage_info_0x4d19c32e),
    0x840BA904: ("damage_info_0x840ba904", _decode_damage_info_0x840ba904),
    0xAF7FFE63: ("part_0xaf7ffe63", structs.decode_BIG_Q),
    0x49FAE143: ("electric_effect", structs.decode_BIG_Q),
    0x570AA8F2: ("elsc", structs.decode_BIG_Q),
    0xF2DC8618: ("part_0xf2dc8618", structs.decode_BIG_Q),
    0xD53F059B: ("part_0xd53f059b", structs.decode_BIG_Q),
    0x0687C33E: ("death_explosion", structs.decode_BIG_Q),
    0x13F55169: ("sound_locomotion_looped", _decode_sound_locomotion_looped),
    0x9C04DF2F: ("swarm_sound_data_0x9c04df2f", _decode_swarm_sound_data_0x9c04df2f),
    0x8D79B556: ("swarm_sound_data_0x8d79b556", _decode_swarm_sound_data_0x8d79b556),
    0xEB9A9949: ("caud_0xeb9a9949", structs.decode_BIG_Q),
    0xC3DE457E: ("sound_form_pulse_ring", structs.decode_BIG_Q),
    0xAB633EF1: ("sound_fire_pulse_ring", structs.decode_BIG_Q),
    0x2A430EB0: ("sound_break_pulse_ring", structs.decode_BIG_Q),
    0xAF1768C4: ("sound_form_circ_saw", structs.decode_BIG_Q),
    0x435A0B62: ("sound_circ_saw_dive", structs.decode_BIG_Q),
    0x13EC5401: ("sound_circ_saw_hit_ground", structs.decode_BIG_Q),
    0xE5A34FB3: ("sound_circ_saw_hit_player", structs.decode_BIG_Q),
    0x7B38D80D: ("sound_form_electric_eel", structs.decode_BIG_Q),
    0x84360D80: ("caud_0x84360d80", structs.decode_BIG_Q),
    0xD2BE3AF7: ("caud_0xd2be3af7", structs.decode_BIG_Q),
    0x9ECC3D08: ("splash_sound_small", structs.decode_BIG_Q),
    0xCF4F5348: ("sound_break_electric_eel", structs.decode_BIG_Q),
    0x05117E35: ("sound_swarm_broken", structs.decode_BIG_Q),
    0xA53694C2: ("sound_swarm_bot_stunned", structs.decode_BIG_Q),
    0xDC478968: ("timing_constraint_duration", structs.decode_BIG_f),
    0x091CB316: ("sound_swarm_bot_begin_dive", structs.decode_BIG_Q),
    0x358177CC: ("sound_swarm_bot_killed", structs.decode_BIG_Q),
    0xAB3E98B8: ("sound_swarm_bot_explosion", structs.decode_BIG_Q),
}
