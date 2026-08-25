# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DarkSamusJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        unknown_0x72edeb7d: float
        unknown_0x74fa22f0: float
        glide_sound: int
        missile_ricochet_sound: int
        unknown_0x6689925b: bool
        txtr_0x3863160b: int
        unknown_0x2c6a3344: float
        melee_attack_damage: json_util.JsonObject
        part_0x6d40aa56: int
        part_0x9603a544: int
        dive_attack_damage: json_util.JsonObject
        unknown_0x4aa5dd62: float
        unknown_0x1ad7dc21: float
        dive_attack_effect: int
        scatter_shot_projectile: int
        scatter_shot_projectile2: int
        scatter_shot_damage: json_util.JsonObject
        unknown_0x378285b9: float
        unknown_0xd242e25f: float
        normal_missile_projectile: int
        normal_missile_damage: json_util.JsonObject
        unknown_0x1f1ef7a9: int
        unknown_0xc4a1a44e: int
        super_missile_projectile: int
        super_missile_damage: json_util.JsonObject
        freeze_beam_projectile: int
        freeze_beam_damage: json_util.JsonObject
        txtr_0x7ffeb33d: int
        damage_interrupt_threshold: float
        unknown_0xf317f4d5: float
        sweep_swoosh: int
        sweep_beam_damage: json_util.JsonObject
        crsc: int
        sweep_beam_sound: int
        unknown_0x0ef8dc15: int
        invulnerable_model: int
        invulnerable_skin_rules: int
        boost_ball_model: json_util.JsonObject
        boost_ball_damage: json_util.JsonObject
        boost_ball_glow: int
        swhc_0x449aa4aa: int
        swhc_0x0345fa17: int
        sound_0x2c72576b: int
        boost_ball_hit_player_sound: int
        boost_ball_collision: int
        audio_playback_parms: json_util.JsonObject
        part_0xa6c42023: int
        ice_spread_sound: int
        part_0x908b06e9: int
        part_0x494de4a4: int
        sound_0xa861649f: int
        damage_info_0x18402aa9: json_util.JsonObject
        part_0xe701daea: int
        phazon_projectile: int
        wpsc: int
        damage_info_0x58769eb2: json_util.JsonObject
        phazon_projectile_damage: json_util.JsonObject
        phazon_enrage_sphere: int
        damage_info_0x8f3af226: json_util.JsonObject
        alternate_scannable_info: int


@dataclasses.dataclass()
class DarkSamus(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    patterned: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0xB3774750,
                original_name="Patterned",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_0x72edeb7d: float = dataclasses.field(
        default=-1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72EDEB7D, original_name="Unknown"),
        },
    )
    unknown_0x74fa22f0: float = dataclasses.field(
        default=-1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x74FA22F0, original_name="Unknown"),
        },
    )
    glide_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x1F468967, original_name="GlideSound"),
        },
    )
    missile_ricochet_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x1A08AADC, original_name="MissileRicochetSound"),
        },
    )
    unknown_0x6689925b: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6689925B, original_name="Unknown"),
        },
    )
    txtr_0x3863160b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3863160B, original_name="TXTR"),
        },
    )
    unknown_0x2c6a3344: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C6A3344, original_name="Unknown"),
        },
    )
    melee_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4D790EE9,
                original_name="MeleeAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    part_0x6d40aa56: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6D40AA56, original_name="PART"),
        },
    )
    part_0x9603a544: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9603A544, original_name="PART"),
        },
    )
    dive_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8688F535,
                original_name="DiveAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x4aa5dd62: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4AA5DD62, original_name="Unknown"),
        },
    )
    unknown_0x1ad7dc21: float = dataclasses.field(
        default=500.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AD7DC21, original_name="Unknown"),
        },
    )
    dive_attack_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xED30B0EF, original_name="DiveAttackEffect"),
        },
    )
    scatter_shot_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x855F0749, original_name="ScatterShotProjectile"),
        },
    )
    scatter_shot_projectile2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x83A5517F, original_name="ScatterShotProjectile2"),
        },
    )
    scatter_shot_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8EA87062,
                original_name="ScatterShotDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x378285b9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x378285B9, original_name="Unknown"),
        },
    )
    unknown_0xd242e25f: float = dataclasses.field(
        default=300.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD242E25F, original_name="Unknown"),
        },
    )
    normal_missile_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE00DB62D, original_name="NormalMissileProjectile"),
        },
    )
    normal_missile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xC4128792,
                original_name="NormalMissileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x1f1ef7a9: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1F1EF7A9, original_name="Unknown"),
        },
    )
    unknown_0xc4a1a44e: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC4A1A44E, original_name="Unknown"),
        },
    )
    super_missile_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x29DB4EE4, original_name="SuperMissileProjectile"),
        },
    )
    super_missile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x26632B7E,
                original_name="SuperMissileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    freeze_beam_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF9104A69, original_name="FreezeBeamProjectile"),
        },
    )
    freeze_beam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB5BA1FE7,
                original_name="FreezeBeamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    txtr_0x7ffeb33d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7FFEB33D, original_name="TXTR"),
        },
    )
    damage_interrupt_threshold: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8F70D3F2, original_name="DamageInterruptThreshold"),
        },
    )
    unknown_0xf317f4d5: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF317F4D5, original_name="Unknown"),
        },
    )
    sweep_swoosh: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD2122711, original_name="SweepSwoosh"),
        },
    )
    sweep_beam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x08C2BFE0,
                original_name="SweepBeamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    crsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CRSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x68B658F2, original_name="CRSC"),
        },
    )
    sweep_beam_sound: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEA17CB66, original_name="SweepBeamSound"),
        },
    )
    unknown_0x0ef8dc15: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0EF8DC15, original_name="Unknown"),
        },
    )
    invulnerable_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x072DF331, original_name="InvulnerableModel"),
        },
    )
    invulnerable_skin_rules: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAA96399C, original_name="InvulnerableSkinRules"),
        },
    )
    boost_ball_model: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xF148F728,
                original_name="BoostBallModel",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    boost_ball_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xE18DC6FC,
                original_name="BoostBallDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    boost_ball_glow: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAC43BA34, original_name="BoostBallGlow"),
        },
    )
    swhc_0x449aa4aa: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SWHC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x449AA4AA, original_name="SWHC"),
        },
    )
    swhc_0x0345fa17: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SWHC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0345FA17, original_name="SWHC"),
        },
    )
    sound_0x2c72576b: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x2C72576B, original_name="Sound"),
        },
    )
    boost_ball_hit_player_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x9E02691C, original_name="BoostBallHitPlayerSound"),
        },
    )
    boost_ball_collision: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3433BC8B, original_name="BoostBallCollision"),
        },
    )
    audio_playback_parms: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x4841182B,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    part_0xa6c42023: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA6C42023, original_name="PART"),
        },
    )
    ice_spread_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xD3593630, original_name="IceSpreadSound"),
        },
    )
    part_0x908b06e9: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x908B06E9, original_name="PART"),
        },
    )
    part_0x494de4a4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x494DE4A4, original_name="PART"),
        },
    )
    sound_0xa861649f: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xA861649F, original_name="Sound"),
        },
    )
    damage_info_0x18402aa9: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x18402AA9,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    part_0xe701daea: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE701DAEA, original_name="PART"),
        },
    )
    phazon_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBF62B633, original_name="PhazonProjectile"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8D123FE9, original_name="WPSC"),
        },
    )
    damage_info_0x58769eb2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x58769EB2,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    phazon_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4D8E735F,
                original_name="PhazonProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    phazon_enrage_sphere: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x83106405, original_name="PhazonEnrageSphere"),
        },
    )
    damage_info_0x8f3af226: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8F3AF226,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    alternate_scannable_info: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF60AC5CC, original_name="AlternateScannableInfo"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DRKS"

    @classmethod
    def modules(cls) -> list[str]:
        return ["DarkSamus.rel"]

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
        if property_count != 63:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "detection_range": 32.0,
                "collision_radius": 0.5,
                "collision_height": 1.0,
                "creature_size": 1,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72EDEB7D
        unknown_0x72edeb7d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74FA22F0
        unknown_0x74fa22f0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F468967
        glide_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A08AADC
        missile_ricochet_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6689925B
        unknown_0x6689925b = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3863160B
        txtr_0x3863160b = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C6A3344
        unknown_0x2c6a3344 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D790EE9
        melee_attack_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D40AA56
        part_0x6d40aa56 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9603A544
        part_0x9603a544 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8688F535
        dive_attack_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AA5DD62
        unknown_0x4aa5dd62 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AD7DC21
        unknown_0x1ad7dc21 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED30B0EF
        dive_attack_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x855F0749
        scatter_shot_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83A5517F
        scatter_shot_projectile2 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8EA87062
        scatter_shot_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x378285B9
        unknown_0x378285b9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD242E25F
        unknown_0xd242e25f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE00DB62D
        normal_missile_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4128792
        normal_missile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F1EF7A9
        unknown_0x1f1ef7a9 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4A1A44E
        unknown_0xc4a1a44e = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29DB4EE4
        super_missile_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26632B7E
        super_missile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9104A69
        freeze_beam_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5BA1FE7
        freeze_beam_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FFEB33D
        txtr_0x7ffeb33d = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F70D3F2
        damage_interrupt_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF317F4D5
        unknown_0xf317f4d5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD2122711
        sweep_swoosh = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08C2BFE0
        sweep_beam_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68B658F2
        crsc = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA17CB66
        sweep_beam_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0EF8DC15
        unknown_0x0ef8dc15 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x072DF331
        invulnerable_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA96399C
        invulnerable_skin_rules = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF148F728
        boost_ball_model = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE18DC6FC
        boost_ball_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC43BA34
        boost_ball_glow = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x449AA4AA
        swhc_0x449aa4aa = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0345FA17
        swhc_0x0345fa17 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C72576B
        sound_0x2c72576b = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9E02691C
        boost_ball_hit_player_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3433BC8B
        boost_ball_collision = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4841182B
        audio_playback_parms = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6C42023
        part_0xa6c42023 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3593630
        ice_spread_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x908B06E9
        part_0x908b06e9 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x494DE4A4
        part_0x494de4a4 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA861649F
        sound_0xa861649f = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18402AA9
        damage_info_0x18402aa9 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE701DAEA
        part_0xe701daea = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF62B633
        phazon_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D123FE9
        wpsc = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58769EB2
        damage_info_0x58769eb2 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D8E735F
        phazon_projectile_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83106405
        phazon_enrage_sphere = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F3AF226
        damage_info_0x8f3af226 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF60AC5CC
        alternate_scannable_info = structs.BIG_L.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            unknown_0x72edeb7d,
            unknown_0x74fa22f0,
            glide_sound,
            missile_ricochet_sound,
            unknown_0x6689925b,
            txtr_0x3863160b,
            unknown_0x2c6a3344,
            melee_attack_damage,
            part_0x6d40aa56,
            part_0x9603a544,
            dive_attack_damage,
            unknown_0x4aa5dd62,
            unknown_0x1ad7dc21,
            dive_attack_effect,
            scatter_shot_projectile,
            scatter_shot_projectile2,
            scatter_shot_damage,
            unknown_0x378285b9,
            unknown_0xd242e25f,
            normal_missile_projectile,
            normal_missile_damage,
            unknown_0x1f1ef7a9,
            unknown_0xc4a1a44e,
            super_missile_projectile,
            super_missile_damage,
            freeze_beam_projectile,
            freeze_beam_damage,
            txtr_0x7ffeb33d,
            damage_interrupt_threshold,
            unknown_0xf317f4d5,
            sweep_swoosh,
            sweep_beam_damage,
            crsc,
            sweep_beam_sound,
            unknown_0x0ef8dc15,
            invulnerable_model,
            invulnerable_skin_rules,
            boost_ball_model,
            boost_ball_damage,
            boost_ball_glow,
            swhc_0x449aa4aa,
            swhc_0x0345fa17,
            sound_0x2c72576b,
            boost_ball_hit_player_sound,
            boost_ball_collision,
            audio_playback_parms,
            part_0xa6c42023,
            ice_spread_sound,
            part_0x908b06e9,
            part_0x494de4a4,
            sound_0xa861649f,
            damage_info_0x18402aa9,
            part_0xe701daea,
            phazon_projectile,
            wpsc,
            damage_info_0x58769eb2,
            phazon_projectile_damage,
            phazon_enrage_sphere,
            damage_info_0x8f3af226,
            alternate_scannable_info,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00?")  # 63 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(
            data,
            game,
            default_override={
                "detection_range": 32.0,
                "collision_radius": 0.5,
                "collision_height": 1.0,
                "creature_size": 1,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"r\xed\xeb}")  # 0x72edeb7d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x72edeb7d))

        data.write(b't\xfa"\xf0')  # 0x74fa22f0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x74fa22f0))

        data.write(b"\x1fF\x89g")  # 0x1f468967
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.glide_sound))

        data.write(b"\x1a\x08\xaa\xdc")  # 0x1a08aadc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.missile_ricochet_sound))

        data.write(b"f\x89\x92[")  # 0x6689925b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x6689925b))

        data.write(b"8c\x16\x0b")  # 0x3863160b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.txtr_0x3863160b))

        data.write(b",j3D")  # 0x2c6a3344
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2c6a3344))

        data.write(b"My\x0e\xe9")  # 0x4d790ee9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.melee_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"m@\xaaV")  # 0x6d40aa56
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x6d40aa56))

        data.write(b"\x96\x03\xa5D")  # 0x9603a544
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x9603a544))

        data.write(b"\x86\x88\xf55")  # 0x8688f535
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dive_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"J\xa5\xddb")  # 0x4aa5dd62
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4aa5dd62))

        data.write(b"\x1a\xd7\xdc!")  # 0x1ad7dc21
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1ad7dc21))

        data.write(b"\xed0\xb0\xef")  # 0xed30b0ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dive_attack_effect))

        data.write(b"\x85_\x07I")  # 0x855f0749
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scatter_shot_projectile))

        data.write(b"\x83\xa5Q\x7f")  # 0x83a5517f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scatter_shot_projectile2))

        data.write(b"\x8e\xa8pb")  # 0x8ea87062
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.scatter_shot_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"7\x82\x85\xb9")  # 0x378285b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x378285b9))

        data.write(b"\xd2B\xe2_")  # 0xd242e25f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd242e25f))

        data.write(b"\xe0\r\xb6-")  # 0xe00db62d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.normal_missile_projectile))

        data.write(b"\xc4\x12\x87\x92")  # 0xc4128792
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.normal_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1f\x1e\xf7\xa9")  # 0x1f1ef7a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x1f1ef7a9))

        data.write(b"\xc4\xa1\xa4N")  # 0xc4a1a44e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc4a1a44e))

        data.write(b")\xdbN\xe4")  # 0x29db4ee4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.super_missile_projectile))

        data.write(b"&c+~")  # 0x26632b7e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.super_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf9\x10Ji")  # 0xf9104a69
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.freeze_beam_projectile))

        data.write(b"\xb5\xba\x1f\xe7")  # 0xb5ba1fe7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.freeze_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x7f\xfe\xb3=")  # 0x7ffeb33d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.txtr_0x7ffeb33d))

        data.write(b"\x8fp\xd3\xf2")  # 0x8f70d3f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_interrupt_threshold))

        data.write(b"\xf3\x17\xf4\xd5")  # 0xf317f4d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf317f4d5))

        data.write(b"\xd2\x12'\x11")  # 0xd2122711
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.sweep_swoosh))

        data.write(b"\x08\xc2\xbf\xe0")  # 0x8c2bfe0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sweep_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"h\xb6X\xf2")  # 0x68b658f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.crsc))

        data.write(b"\xea\x17\xcbf")  # 0xea17cb66
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sweep_beam_sound))

        data.write(b"\x0e\xf8\xdc\x15")  # 0xef8dc15
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x0ef8dc15))

        data.write(b"\x07-\xf31")  # 0x72df331
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.invulnerable_model))

        data.write(b"\xaa\x969\x9c")  # 0xaa96399c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.invulnerable_skin_rules))

        data.write(b"\xf1H\xf7(")  # 0xf148f728
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.boost_ball_model.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe1\x8d\xc6\xfc")  # 0xe18dc6fc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.boost_ball_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xacC\xba4")  # 0xac43ba34
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.boost_ball_glow))

        data.write(b"D\x9a\xa4\xaa")  # 0x449aa4aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.swhc_0x449aa4aa))

        data.write(b"\x03E\xfa\x17")  # 0x345fa17
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.swhc_0x0345fa17))

        data.write(b",rWk")  # 0x2c72576b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0x2c72576b))

        data.write(b"\x9e\x02i\x1c")  # 0x9e02691c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.boost_ball_hit_player_sound))

        data.write(b"43\xbc\x8b")  # 0x3433bc8b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.boost_ball_collision))

        data.write(b"HA\x18+")  # 0x4841182b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa6\xc4 #")  # 0xa6c42023
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0xa6c42023))

        data.write(b"\xd3Y60")  # 0xd3593630
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.ice_spread_sound))

        data.write(b"\x90\x8b\x06\xe9")  # 0x908b06e9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x908b06e9))

        data.write(b"IM\xe4\xa4")  # 0x494de4a4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x494de4a4))

        data.write(b"\xa8ad\x9f")  # 0xa861649f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0xa861649f))

        data.write(b"\x18@*\xa9")  # 0x18402aa9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x18402aa9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7\x01\xda\xea")  # 0xe701daea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0xe701daea))

        data.write(b"\xbfb\xb63")  # 0xbf62b633
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.phazon_projectile))

        data.write(b"\x8d\x12?\xe9")  # 0x8d123fe9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.wpsc))

        data.write(b"Xv\x9e\xb2")  # 0x58769eb2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x58769eb2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"M\x8es_")  # 0x4d8e735f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phazon_projectile_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 5.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x83\x10d\x05")  # 0x83106405
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.phazon_enrage_sphere))

        data.write(b"\x8f:\xf2&")  # 0x8f3af226
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x8f3af226.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf6\n\xc5\xcc")  # 0xf60ac5cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.alternate_scannable_info))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkSamusJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            unknown_0x72edeb7d=json_data["unknown_0x72edeb7d"],
            unknown_0x74fa22f0=json_data["unknown_0x74fa22f0"],
            glide_sound=json_data["glide_sound"],
            missile_ricochet_sound=json_data["missile_ricochet_sound"],
            unknown_0x6689925b=json_data["unknown_0x6689925b"],
            txtr_0x3863160b=json_data["txtr_0x3863160b"],
            unknown_0x2c6a3344=json_data["unknown_0x2c6a3344"],
            melee_attack_damage=DamageInfo.from_json(json_data["melee_attack_damage"]),
            part_0x6d40aa56=json_data["part_0x6d40aa56"],
            part_0x9603a544=json_data["part_0x9603a544"],
            dive_attack_damage=DamageInfo.from_json(json_data["dive_attack_damage"]),
            unknown_0x4aa5dd62=json_data["unknown_0x4aa5dd62"],
            unknown_0x1ad7dc21=json_data["unknown_0x1ad7dc21"],
            dive_attack_effect=json_data["dive_attack_effect"],
            scatter_shot_projectile=json_data["scatter_shot_projectile"],
            scatter_shot_projectile2=json_data["scatter_shot_projectile2"],
            scatter_shot_damage=DamageInfo.from_json(json_data["scatter_shot_damage"]),
            unknown_0x378285b9=json_data["unknown_0x378285b9"],
            unknown_0xd242e25f=json_data["unknown_0xd242e25f"],
            normal_missile_projectile=json_data["normal_missile_projectile"],
            normal_missile_damage=DamageInfo.from_json(json_data["normal_missile_damage"]),
            unknown_0x1f1ef7a9=json_data["unknown_0x1f1ef7a9"],
            unknown_0xc4a1a44e=json_data["unknown_0xc4a1a44e"],
            super_missile_projectile=json_data["super_missile_projectile"],
            super_missile_damage=DamageInfo.from_json(json_data["super_missile_damage"]),
            freeze_beam_projectile=json_data["freeze_beam_projectile"],
            freeze_beam_damage=DamageInfo.from_json(json_data["freeze_beam_damage"]),
            txtr_0x7ffeb33d=json_data["txtr_0x7ffeb33d"],
            damage_interrupt_threshold=json_data["damage_interrupt_threshold"],
            unknown_0xf317f4d5=json_data["unknown_0xf317f4d5"],
            sweep_swoosh=json_data["sweep_swoosh"],
            sweep_beam_damage=DamageInfo.from_json(json_data["sweep_beam_damage"]),
            crsc=json_data["crsc"],
            sweep_beam_sound=json_data["sweep_beam_sound"],
            unknown_0x0ef8dc15=json_data["unknown_0x0ef8dc15"],
            invulnerable_model=json_data["invulnerable_model"],
            invulnerable_skin_rules=json_data["invulnerable_skin_rules"],
            boost_ball_model=AnimationParameters.from_json(json_data["boost_ball_model"]),
            boost_ball_damage=DamageInfo.from_json(json_data["boost_ball_damage"]),
            boost_ball_glow=json_data["boost_ball_glow"],
            swhc_0x449aa4aa=json_data["swhc_0x449aa4aa"],
            swhc_0x0345fa17=json_data["swhc_0x0345fa17"],
            sound_0x2c72576b=json_data["sound_0x2c72576b"],
            boost_ball_hit_player_sound=json_data["boost_ball_hit_player_sound"],
            boost_ball_collision=json_data["boost_ball_collision"],
            audio_playback_parms=AudioPlaybackParms.from_json(json_data["audio_playback_parms"]),
            part_0xa6c42023=json_data["part_0xa6c42023"],
            ice_spread_sound=json_data["ice_spread_sound"],
            part_0x908b06e9=json_data["part_0x908b06e9"],
            part_0x494de4a4=json_data["part_0x494de4a4"],
            sound_0xa861649f=json_data["sound_0xa861649f"],
            damage_info_0x18402aa9=DamageInfo.from_json(json_data["damage_info_0x18402aa9"]),
            part_0xe701daea=json_data["part_0xe701daea"],
            phazon_projectile=json_data["phazon_projectile"],
            wpsc=json_data["wpsc"],
            damage_info_0x58769eb2=DamageInfo.from_json(json_data["damage_info_0x58769eb2"]),
            phazon_projectile_damage=DamageInfo.from_json(json_data["phazon_projectile_damage"]),
            phazon_enrage_sphere=json_data["phazon_enrage_sphere"],
            damage_info_0x8f3af226=DamageInfo.from_json(json_data["damage_info_0x8f3af226"]),
            alternate_scannable_info=json_data["alternate_scannable_info"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "unknown_0x72edeb7d": self.unknown_0x72edeb7d,
            "unknown_0x74fa22f0": self.unknown_0x74fa22f0,
            "glide_sound": self.glide_sound,
            "missile_ricochet_sound": self.missile_ricochet_sound,
            "unknown_0x6689925b": self.unknown_0x6689925b,
            "txtr_0x3863160b": self.txtr_0x3863160b,
            "unknown_0x2c6a3344": self.unknown_0x2c6a3344,
            "melee_attack_damage": self.melee_attack_damage.to_json(),
            "part_0x6d40aa56": self.part_0x6d40aa56,
            "part_0x9603a544": self.part_0x9603a544,
            "dive_attack_damage": self.dive_attack_damage.to_json(),
            "unknown_0x4aa5dd62": self.unknown_0x4aa5dd62,
            "unknown_0x1ad7dc21": self.unknown_0x1ad7dc21,
            "dive_attack_effect": self.dive_attack_effect,
            "scatter_shot_projectile": self.scatter_shot_projectile,
            "scatter_shot_projectile2": self.scatter_shot_projectile2,
            "scatter_shot_damage": self.scatter_shot_damage.to_json(),
            "unknown_0x378285b9": self.unknown_0x378285b9,
            "unknown_0xd242e25f": self.unknown_0xd242e25f,
            "normal_missile_projectile": self.normal_missile_projectile,
            "normal_missile_damage": self.normal_missile_damage.to_json(),
            "unknown_0x1f1ef7a9": self.unknown_0x1f1ef7a9,
            "unknown_0xc4a1a44e": self.unknown_0xc4a1a44e,
            "super_missile_projectile": self.super_missile_projectile,
            "super_missile_damage": self.super_missile_damage.to_json(),
            "freeze_beam_projectile": self.freeze_beam_projectile,
            "freeze_beam_damage": self.freeze_beam_damage.to_json(),
            "txtr_0x7ffeb33d": self.txtr_0x7ffeb33d,
            "damage_interrupt_threshold": self.damage_interrupt_threshold,
            "unknown_0xf317f4d5": self.unknown_0xf317f4d5,
            "sweep_swoosh": self.sweep_swoosh,
            "sweep_beam_damage": self.sweep_beam_damage.to_json(),
            "crsc": self.crsc,
            "sweep_beam_sound": self.sweep_beam_sound,
            "unknown_0x0ef8dc15": self.unknown_0x0ef8dc15,
            "invulnerable_model": self.invulnerable_model,
            "invulnerable_skin_rules": self.invulnerable_skin_rules,
            "boost_ball_model": self.boost_ball_model.to_json(),
            "boost_ball_damage": self.boost_ball_damage.to_json(),
            "boost_ball_glow": self.boost_ball_glow,
            "swhc_0x449aa4aa": self.swhc_0x449aa4aa,
            "swhc_0x0345fa17": self.swhc_0x0345fa17,
            "sound_0x2c72576b": self.sound_0x2c72576b,
            "boost_ball_hit_player_sound": self.boost_ball_hit_player_sound,
            "boost_ball_collision": self.boost_ball_collision,
            "audio_playback_parms": self.audio_playback_parms.to_json(),
            "part_0xa6c42023": self.part_0xa6c42023,
            "ice_spread_sound": self.ice_spread_sound,
            "part_0x908b06e9": self.part_0x908b06e9,
            "part_0x494de4a4": self.part_0x494de4a4,
            "sound_0xa861649f": self.sound_0xa861649f,
            "damage_info_0x18402aa9": self.damage_info_0x18402aa9.to_json(),
            "part_0xe701daea": self.part_0xe701daea,
            "phazon_projectile": self.phazon_projectile,
            "wpsc": self.wpsc,
            "damage_info_0x58769eb2": self.damage_info_0x58769eb2.to_json(),
            "phazon_projectile_damage": self.phazon_projectile_damage.to_json(),
            "phazon_enrage_sphere": self.phazon_enrage_sphere,
            "damage_info_0x8f3af226": self.damage_info_0x8f3af226.to_json(),
            "alternate_scannable_info": self.alternate_scannable_info,
        }

    def _dependencies_for_glide_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.glide_sound)

    def _dependencies_for_missile_ricochet_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.missile_ricochet_sound)

    def _dependencies_for_txtr_0x3863160b(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.txtr_0x3863160b)

    def _dependencies_for_part_0x6d40aa56(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x6d40aa56)

    def _dependencies_for_part_0x9603a544(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x9603a544)

    def _dependencies_for_dive_attack_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dive_attack_effect)

    def _dependencies_for_scatter_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scatter_shot_projectile)

    def _dependencies_for_scatter_shot_projectile2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scatter_shot_projectile2)

    def _dependencies_for_normal_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.normal_missile_projectile)

    def _dependencies_for_super_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.super_missile_projectile)

    def _dependencies_for_freeze_beam_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.freeze_beam_projectile)

    def _dependencies_for_txtr_0x7ffeb33d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.txtr_0x7ffeb33d)

    def _dependencies_for_sweep_swoosh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sweep_swoosh)

    def _dependencies_for_crsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.crsc)

    def _dependencies_for_invulnerable_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.invulnerable_model)

    def _dependencies_for_invulnerable_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.invulnerable_skin_rules)

    def _dependencies_for_boost_ball_glow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_glow)

    def _dependencies_for_swhc_0x449aa4aa(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.swhc_0x449aa4aa)

    def _dependencies_for_swhc_0x0345fa17(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.swhc_0x0345fa17)

    def _dependencies_for_sound_0x2c72576b(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0x2c72576b)

    def _dependencies_for_boost_ball_hit_player_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.boost_ball_hit_player_sound)

    def _dependencies_for_boost_ball_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_collision)

    def _dependencies_for_part_0xa6c42023(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xa6c42023)

    def _dependencies_for_ice_spread_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.ice_spread_sound)

    def _dependencies_for_part_0x908b06e9(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x908b06e9)

    def _dependencies_for_part_0x494de4a4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x494de4a4)

    def _dependencies_for_sound_0xa861649f(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0xa861649f)

    def _dependencies_for_part_0xe701daea(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xe701daea)

    def _dependencies_for_phazon_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_projectile)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_phazon_enrage_sphere(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_enrage_sphere)

    def _dependencies_for_alternate_scannable_info(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.alternate_scannable_info)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_glide_sound, "glide_sound", "int"),
            (self._dependencies_for_missile_ricochet_sound, "missile_ricochet_sound", "int"),
            (self._dependencies_for_txtr_0x3863160b, "txtr_0x3863160b", "AssetId"),
            (self._dependencies_for_part_0x6d40aa56, "part_0x6d40aa56", "AssetId"),
            (self._dependencies_for_part_0x9603a544, "part_0x9603a544", "AssetId"),
            (self._dependencies_for_dive_attack_effect, "dive_attack_effect", "AssetId"),
            (self._dependencies_for_scatter_shot_projectile, "scatter_shot_projectile", "AssetId"),
            (self._dependencies_for_scatter_shot_projectile2, "scatter_shot_projectile2", "AssetId"),
            (self._dependencies_for_normal_missile_projectile, "normal_missile_projectile", "AssetId"),
            (self._dependencies_for_super_missile_projectile, "super_missile_projectile", "AssetId"),
            (self._dependencies_for_freeze_beam_projectile, "freeze_beam_projectile", "AssetId"),
            (self._dependencies_for_txtr_0x7ffeb33d, "txtr_0x7ffeb33d", "AssetId"),
            (self._dependencies_for_sweep_swoosh, "sweep_swoosh", "AssetId"),
            (self._dependencies_for_crsc, "crsc", "AssetId"),
            (self._dependencies_for_invulnerable_model, "invulnerable_model", "AssetId"),
            (self._dependencies_for_invulnerable_skin_rules, "invulnerable_skin_rules", "AssetId"),
            (self.boost_ball_model.dependencies_for, "boost_ball_model", "AnimationParameters"),
            (self._dependencies_for_boost_ball_glow, "boost_ball_glow", "AssetId"),
            (self._dependencies_for_swhc_0x449aa4aa, "swhc_0x449aa4aa", "AssetId"),
            (self._dependencies_for_swhc_0x0345fa17, "swhc_0x0345fa17", "AssetId"),
            (self._dependencies_for_sound_0x2c72576b, "sound_0x2c72576b", "int"),
            (self._dependencies_for_boost_ball_hit_player_sound, "boost_ball_hit_player_sound", "int"),
            (self._dependencies_for_boost_ball_collision, "boost_ball_collision", "AssetId"),
            (self.audio_playback_parms.dependencies_for, "audio_playback_parms", "AudioPlaybackParms"),
            (self._dependencies_for_part_0xa6c42023, "part_0xa6c42023", "AssetId"),
            (self._dependencies_for_ice_spread_sound, "ice_spread_sound", "int"),
            (self._dependencies_for_part_0x908b06e9, "part_0x908b06e9", "AssetId"),
            (self._dependencies_for_part_0x494de4a4, "part_0x494de4a4", "AssetId"),
            (self._dependencies_for_sound_0xa861649f, "sound_0xa861649f", "int"),
            (self._dependencies_for_part_0xe701daea, "part_0xe701daea", "AssetId"),
            (self._dependencies_for_phazon_projectile, "phazon_projectile", "AssetId"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_phazon_enrage_sphere, "phazon_enrage_sphere", "AssetId"),
            (self._dependencies_for_alternate_scannable_info, "alternate_scannable_info", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for DarkSamus.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "detection_range": 32.0,
            "collision_radius": 0.5,
            "collision_height": 1.0,
            "creature_size": 1,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_melee_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_dive_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_scatter_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_normal_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_super_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_freeze_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_sweep_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_boost_ball_model(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_boost_ball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_audio_playback_parms(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_damage_info_0x18402aa9(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x58769eb2(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 5.0}
    )


def _decode_damage_info_0x8f3af226(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x72EDEB7D: ("unknown_0x72edeb7d", structs.decode_BIG_f),
    0x74FA22F0: ("unknown_0x74fa22f0", structs.decode_BIG_f),
    0x1F468967: ("glide_sound", structs.decode_BIG_l),
    0x1A08AADC: ("missile_ricochet_sound", structs.decode_BIG_l),
    0x6689925B: ("unknown_0x6689925b", structs.decode_BIG_bool_),
    0x3863160B: ("txtr_0x3863160b", structs.decode_BIG_L),
    0x2C6A3344: ("unknown_0x2c6a3344", structs.decode_BIG_f),
    0x4D790EE9: ("melee_attack_damage", _decode_melee_attack_damage),
    0x6D40AA56: ("part_0x6d40aa56", structs.decode_BIG_L),
    0x9603A544: ("part_0x9603a544", structs.decode_BIG_L),
    0x8688F535: ("dive_attack_damage", _decode_dive_attack_damage),
    0x4AA5DD62: ("unknown_0x4aa5dd62", structs.decode_BIG_f),
    0x1AD7DC21: ("unknown_0x1ad7dc21", structs.decode_BIG_f),
    0xED30B0EF: ("dive_attack_effect", structs.decode_BIG_L),
    0x855F0749: ("scatter_shot_projectile", structs.decode_BIG_L),
    0x83A5517F: ("scatter_shot_projectile2", structs.decode_BIG_L),
    0x8EA87062: ("scatter_shot_damage", _decode_scatter_shot_damage),
    0x378285B9: ("unknown_0x378285b9", structs.decode_BIG_f),
    0xD242E25F: ("unknown_0xd242e25f", structs.decode_BIG_f),
    0xE00DB62D: ("normal_missile_projectile", structs.decode_BIG_L),
    0xC4128792: ("normal_missile_damage", _decode_normal_missile_damage),
    0x1F1EF7A9: ("unknown_0x1f1ef7a9", structs.decode_BIG_l),
    0xC4A1A44E: ("unknown_0xc4a1a44e", structs.decode_BIG_l),
    0x29DB4EE4: ("super_missile_projectile", structs.decode_BIG_L),
    0x26632B7E: ("super_missile_damage", _decode_super_missile_damage),
    0xF9104A69: ("freeze_beam_projectile", structs.decode_BIG_L),
    0xB5BA1FE7: ("freeze_beam_damage", _decode_freeze_beam_damage),
    0x7FFEB33D: ("txtr_0x7ffeb33d", structs.decode_BIG_L),
    0x8F70D3F2: ("damage_interrupt_threshold", structs.decode_BIG_f),
    0xF317F4D5: ("unknown_0xf317f4d5", structs.decode_BIG_f),
    0xD2122711: ("sweep_swoosh", structs.decode_BIG_L),
    0x08C2BFE0: ("sweep_beam_damage", _decode_sweep_beam_damage),
    0x68B658F2: ("crsc", structs.decode_BIG_L),
    0xEA17CB66: ("sweep_beam_sound", structs.decode_BIG_l),
    0x0EF8DC15: ("unknown_0x0ef8dc15", structs.decode_BIG_l),
    0x072DF331: ("invulnerable_model", structs.decode_BIG_L),
    0xAA96399C: ("invulnerable_skin_rules", structs.decode_BIG_L),
    0xF148F728: ("boost_ball_model", _decode_boost_ball_model),
    0xE18DC6FC: ("boost_ball_damage", _decode_boost_ball_damage),
    0xAC43BA34: ("boost_ball_glow", structs.decode_BIG_L),
    0x449AA4AA: ("swhc_0x449aa4aa", structs.decode_BIG_L),
    0x0345FA17: ("swhc_0x0345fa17", structs.decode_BIG_L),
    0x2C72576B: ("sound_0x2c72576b", structs.decode_BIG_l),
    0x9E02691C: ("boost_ball_hit_player_sound", structs.decode_BIG_l),
    0x3433BC8B: ("boost_ball_collision", structs.decode_BIG_L),
    0x4841182B: ("audio_playback_parms", _decode_audio_playback_parms),
    0xA6C42023: ("part_0xa6c42023", structs.decode_BIG_L),
    0xD3593630: ("ice_spread_sound", structs.decode_BIG_l),
    0x908B06E9: ("part_0x908b06e9", structs.decode_BIG_L),
    0x494DE4A4: ("part_0x494de4a4", structs.decode_BIG_L),
    0xA861649F: ("sound_0xa861649f", structs.decode_BIG_l),
    0x18402AA9: ("damage_info_0x18402aa9", _decode_damage_info_0x18402aa9),
    0xE701DAEA: ("part_0xe701daea", structs.decode_BIG_L),
    0xBF62B633: ("phazon_projectile", structs.decode_BIG_L),
    0x8D123FE9: ("wpsc", structs.decode_BIG_L),
    0x58769EB2: ("damage_info_0x58769eb2", _decode_damage_info_0x58769eb2),
    0x4D8E735F: ("phazon_projectile_damage", _decode_phazon_projectile_damage),
    0x83106405: ("phazon_enrage_sphere", structs.decode_BIG_L),
    0x8F3AF226: ("damage_info_0x8f3af226", _decode_damage_info_0x8f3af226),
    0xF60AC5CC: ("alternate_scannable_info", structs.decode_BIG_L),
}
