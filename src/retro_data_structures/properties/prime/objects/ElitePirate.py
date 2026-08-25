# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ElitePirateJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed: json_util.JsonObject
        actor_parameters: json_util.JsonObject
        taunt_interval: float
        taunt_variance: float
        unknown_1: float
        unknown_2: float
        attack_chance: float
        shot_at_time: float
        shot_at_time_variance: float
        projectile_attraction_radius: float
        energy_absorb_particle_desc_id: int
        energy_absorb_sfx_id: int
        launcher_act_params: json_util.JsonObject
        launcher_anim_params: json_util.JsonObject
        launcher_particle_gen_desc_id: int
        launcher_sfx_id: int
        grenade_model_id: int
        grenade_damage_info: json_util.JsonObject
        launcher_hp: float
        grenade_element_gen_desc_id1: int
        grenade_element_gen_desc_id2: int
        grenade_element_gen_desc_id3: int
        grenade_element_gen_desc_id4: int
        unknown_3: float
        unknown_4: float
        unknown_5: float
        unknown_6: float
        unknown_7: float
        unknown_8: float
        grenade_num_bounces: int
        grenade_bounce_sfx_id: int
        grenade_explode_sfx_id: int
        shockwave_particle_desc_id: int
        shockwave_damage_info: json_util.JsonObject
        shockwave_weapon_desc_id: int
        shockwave_electrocute_sfxid: int
        can_call_for_backup: bool
        fast_when_attracting_energy: bool


@dataclasses.dataclass()
class ElitePirate(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000001, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unnamed: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000004,
                original_name="4",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    actor_parameters: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000005,
                original_name="ActorParameters",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    taunt_interval: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="TauntInterval"),
        },
    )
    taunt_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="TauntVariance"),
        },
    )
    unknown_1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown 1"),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 2"),
        },
    )
    attack_chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="AttackChance"),
        },
    )
    shot_at_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="ShotAtTime"),
        },
    )
    shot_at_time_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="ShotAtTimeVariance"),
        },
    )
    projectile_attraction_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="ProjectileAttractionRadius"),
        },
    )
    energy_absorb_particle_desc_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="EnergyAbsorbParticleDescID"),
        },
    )
    energy_absorb_sfx_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000F, original_name="EnergyAbsorbSfxID"),
        },
    )
    launcher_act_params: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000010,
                original_name="LauncherActParams",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    launcher_anim_params: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000011,
                original_name="LauncherAnimParams",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    launcher_particle_gen_desc_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000012, original_name="LauncherParticleGenDescID"),
        },
    )
    launcher_sfx_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="LauncherSfxID"),
        },
    )
    grenade_model_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000014, original_name="GrenadeModelID"),
        },
    )
    grenade_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000015,
                original_name="GrenadeDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    launcher_hp: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="LauncherHP"),
        },
    )
    grenade_element_gen_desc_id1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000017, original_name="GrenadeElementGenDescID1"),
        },
    )
    grenade_element_gen_desc_id2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000018, original_name="GrenadeElementGenDescID2"),
        },
    )
    grenade_element_gen_desc_id3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000019, original_name="GrenadeElementGenDescID3"),
        },
    )
    grenade_element_gen_desc_id4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001A, original_name="GrenadeElementGenDescID4"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="Unknown 6"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001F, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000020, original_name="Unknown 8"),
        },
    )
    grenade_num_bounces: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000021, original_name="GrenadeNumBounces"),
        },
    )
    grenade_bounce_sfx_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000022, original_name="GrenadeBounceSfxID"),
        },
    )
    grenade_explode_sfx_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000023, original_name="GrenadeExplodeSfxID"),
        },
    )
    shockwave_particle_desc_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000024, original_name="ShockwaveParticleDescID"),
        },
    )
    shockwave_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000025,
                original_name="ShockwaveDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    shockwave_weapon_desc_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000026, original_name="ShockwaveWeaponDescID"),
        },
    )
    shockwave_electrocute_sfxid: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000027, original_name="ShockwaveElectrocuteSFXID"),
        },
    )
    can_call_for_backup: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000028, original_name="CanCallForBackup"),
        },
    )
    fast_when_attracting_energy: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000029, original_name="FastWhenAttractingEnergy"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x26

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed = PatternedAITypedef.from_stream(data, game, property_size)
        actor_parameters = ActorParameters.from_stream(data, game, property_size)
        taunt_interval = structs.BIG_f.unpack(data.read(4))[0]
        taunt_variance = structs.BIG_f.unpack(data.read(4))[0]
        unknown_1 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        attack_chance = structs.BIG_f.unpack(data.read(4))[0]
        shot_at_time = structs.BIG_f.unpack(data.read(4))[0]
        shot_at_time_variance = structs.BIG_f.unpack(data.read(4))[0]
        projectile_attraction_radius = structs.BIG_f.unpack(data.read(4))[0]
        energy_absorb_particle_desc_id = structs.BIG_L.unpack(data.read(4))[0]
        energy_absorb_sfx_id = structs.BIG_l.unpack(data.read(4))[0]
        launcher_act_params = ActorParameters.from_stream(data, game, property_size)
        launcher_anim_params = AnimationParameters.from_stream(data, game, property_size)
        launcher_particle_gen_desc_id = structs.BIG_L.unpack(data.read(4))[0]
        launcher_sfx_id = structs.BIG_l.unpack(data.read(4))[0]
        grenade_model_id = structs.BIG_L.unpack(data.read(4))[0]
        grenade_damage_info = DamageInfo.from_stream(data, game, property_size)
        launcher_hp = structs.BIG_f.unpack(data.read(4))[0]
        grenade_element_gen_desc_id1 = structs.BIG_L.unpack(data.read(4))[0]
        grenade_element_gen_desc_id2 = structs.BIG_L.unpack(data.read(4))[0]
        grenade_element_gen_desc_id3 = structs.BIG_L.unpack(data.read(4))[0]
        grenade_element_gen_desc_id4 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        grenade_num_bounces = structs.BIG_l.unpack(data.read(4))[0]
        grenade_bounce_sfx_id = structs.BIG_l.unpack(data.read(4))[0]
        grenade_explode_sfx_id = structs.BIG_l.unpack(data.read(4))[0]
        shockwave_particle_desc_id = structs.BIG_L.unpack(data.read(4))[0]
        shockwave_damage_info = DamageInfo.from_stream(data, game, property_size)
        shockwave_weapon_desc_id = structs.BIG_L.unpack(data.read(4))[0]
        shockwave_electrocute_sfxid = structs.BIG_l.unpack(data.read(4))[0]
        can_call_for_backup = structs.BIG_bool_.unpack(data.read(1))[0]
        fast_when_attracting_energy = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed,
            actor_parameters,
            taunt_interval,
            taunt_variance,
            unknown_1,
            unknown_2,
            attack_chance,
            shot_at_time,
            shot_at_time_variance,
            projectile_attraction_radius,
            energy_absorb_particle_desc_id,
            energy_absorb_sfx_id,
            launcher_act_params,
            launcher_anim_params,
            launcher_particle_gen_desc_id,
            launcher_sfx_id,
            grenade_model_id,
            grenade_damage_info,
            launcher_hp,
            grenade_element_gen_desc_id1,
            grenade_element_gen_desc_id2,
            grenade_element_gen_desc_id3,
            grenade_element_gen_desc_id4,
            unknown_3,
            unknown_4,
            unknown_5,
            unknown_6,
            unknown_7,
            unknown_8,
            grenade_num_bounces,
            grenade_bounce_sfx_id,
            grenade_explode_sfx_id,
            shockwave_particle_desc_id,
            shockwave_damage_info,
            shockwave_weapon_desc_id,
            shockwave_electrocute_sfxid,
            can_call_for_backup,
            fast_when_attracting_energy,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00*")  # 42 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed.to_stream(data, game)
        self.actor_parameters.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.taunt_interval))
        data.write(structs.BIG_f.pack(self.taunt_variance))
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_f.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.attack_chance))
        data.write(structs.BIG_f.pack(self.shot_at_time))
        data.write(structs.BIG_f.pack(self.shot_at_time_variance))
        data.write(structs.BIG_f.pack(self.projectile_attraction_radius))
        data.write(structs.BIG_L.pack(self.energy_absorb_particle_desc_id))
        data.write(structs.BIG_l.pack(self.energy_absorb_sfx_id))
        self.launcher_act_params.to_stream(data, game)
        self.launcher_anim_params.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.launcher_particle_gen_desc_id))
        data.write(structs.BIG_l.pack(self.launcher_sfx_id))
        data.write(structs.BIG_L.pack(self.grenade_model_id))
        self.grenade_damage_info.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.launcher_hp))
        data.write(structs.BIG_L.pack(self.grenade_element_gen_desc_id1))
        data.write(structs.BIG_L.pack(self.grenade_element_gen_desc_id2))
        data.write(structs.BIG_L.pack(self.grenade_element_gen_desc_id3))
        data.write(structs.BIG_L.pack(self.grenade_element_gen_desc_id4))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        data.write(structs.BIG_l.pack(self.grenade_num_bounces))
        data.write(structs.BIG_l.pack(self.grenade_bounce_sfx_id))
        data.write(structs.BIG_l.pack(self.grenade_explode_sfx_id))
        data.write(structs.BIG_L.pack(self.shockwave_particle_desc_id))
        self.shockwave_damage_info.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.shockwave_weapon_desc_id))
        data.write(structs.BIG_l.pack(self.shockwave_electrocute_sfxid))
        data.write(structs.BIG_bool_.pack(self.can_call_for_backup))
        data.write(structs.BIG_bool_.pack(self.fast_when_attracting_energy))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ElitePirateJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed=PatternedAITypedef.from_json(json_data["unnamed"]),
            actor_parameters=ActorParameters.from_json(json_data["actor_parameters"]),
            taunt_interval=json_data["taunt_interval"],
            taunt_variance=json_data["taunt_variance"],
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            attack_chance=json_data["attack_chance"],
            shot_at_time=json_data["shot_at_time"],
            shot_at_time_variance=json_data["shot_at_time_variance"],
            projectile_attraction_radius=json_data["projectile_attraction_radius"],
            energy_absorb_particle_desc_id=json_data["energy_absorb_particle_desc_id"],
            energy_absorb_sfx_id=json_data["energy_absorb_sfx_id"],
            launcher_act_params=ActorParameters.from_json(json_data["launcher_act_params"]),
            launcher_anim_params=AnimationParameters.from_json(json_data["launcher_anim_params"]),
            launcher_particle_gen_desc_id=json_data["launcher_particle_gen_desc_id"],
            launcher_sfx_id=json_data["launcher_sfx_id"],
            grenade_model_id=json_data["grenade_model_id"],
            grenade_damage_info=DamageInfo.from_json(json_data["grenade_damage_info"]),
            launcher_hp=json_data["launcher_hp"],
            grenade_element_gen_desc_id1=json_data["grenade_element_gen_desc_id1"],
            grenade_element_gen_desc_id2=json_data["grenade_element_gen_desc_id2"],
            grenade_element_gen_desc_id3=json_data["grenade_element_gen_desc_id3"],
            grenade_element_gen_desc_id4=json_data["grenade_element_gen_desc_id4"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            grenade_num_bounces=json_data["grenade_num_bounces"],
            grenade_bounce_sfx_id=json_data["grenade_bounce_sfx_id"],
            grenade_explode_sfx_id=json_data["grenade_explode_sfx_id"],
            shockwave_particle_desc_id=json_data["shockwave_particle_desc_id"],
            shockwave_damage_info=DamageInfo.from_json(json_data["shockwave_damage_info"]),
            shockwave_weapon_desc_id=json_data["shockwave_weapon_desc_id"],
            shockwave_electrocute_sfxid=json_data["shockwave_electrocute_sfxid"],
            can_call_for_backup=json_data["can_call_for_backup"],
            fast_when_attracting_energy=json_data["fast_when_attracting_energy"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed": self.unnamed.to_json(),
            "actor_parameters": self.actor_parameters.to_json(),
            "taunt_interval": self.taunt_interval,
            "taunt_variance": self.taunt_variance,
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "attack_chance": self.attack_chance,
            "shot_at_time": self.shot_at_time,
            "shot_at_time_variance": self.shot_at_time_variance,
            "projectile_attraction_radius": self.projectile_attraction_radius,
            "energy_absorb_particle_desc_id": self.energy_absorb_particle_desc_id,
            "energy_absorb_sfx_id": self.energy_absorb_sfx_id,
            "launcher_act_params": self.launcher_act_params.to_json(),
            "launcher_anim_params": self.launcher_anim_params.to_json(),
            "launcher_particle_gen_desc_id": self.launcher_particle_gen_desc_id,
            "launcher_sfx_id": self.launcher_sfx_id,
            "grenade_model_id": self.grenade_model_id,
            "grenade_damage_info": self.grenade_damage_info.to_json(),
            "launcher_hp": self.launcher_hp,
            "grenade_element_gen_desc_id1": self.grenade_element_gen_desc_id1,
            "grenade_element_gen_desc_id2": self.grenade_element_gen_desc_id2,
            "grenade_element_gen_desc_id3": self.grenade_element_gen_desc_id3,
            "grenade_element_gen_desc_id4": self.grenade_element_gen_desc_id4,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "grenade_num_bounces": self.grenade_num_bounces,
            "grenade_bounce_sfx_id": self.grenade_bounce_sfx_id,
            "grenade_explode_sfx_id": self.grenade_explode_sfx_id,
            "shockwave_particle_desc_id": self.shockwave_particle_desc_id,
            "shockwave_damage_info": self.shockwave_damage_info.to_json(),
            "shockwave_weapon_desc_id": self.shockwave_weapon_desc_id,
            "shockwave_electrocute_sfxid": self.shockwave_electrocute_sfxid,
            "can_call_for_backup": self.can_call_for_backup,
            "fast_when_attracting_energy": self.fast_when_attracting_energy,
        }

    def _dependencies_for_energy_absorb_particle_desc_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energy_absorb_particle_desc_id)

    def _dependencies_for_energy_absorb_sfx_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.energy_absorb_sfx_id)

    def _dependencies_for_launcher_particle_gen_desc_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.launcher_particle_gen_desc_id)

    def _dependencies_for_launcher_sfx_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.launcher_sfx_id)

    def _dependencies_for_grenade_model_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_model_id)

    def _dependencies_for_grenade_element_gen_desc_id1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_element_gen_desc_id1)

    def _dependencies_for_grenade_element_gen_desc_id2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_element_gen_desc_id2)

    def _dependencies_for_grenade_element_gen_desc_id3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_element_gen_desc_id3)

    def _dependencies_for_grenade_element_gen_desc_id4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_element_gen_desc_id4)

    def _dependencies_for_grenade_bounce_sfx_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grenade_bounce_sfx_id)

    def _dependencies_for_grenade_explode_sfx_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grenade_explode_sfx_id)

    def _dependencies_for_shockwave_particle_desc_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shockwave_particle_desc_id)

    def _dependencies_for_shockwave_weapon_desc_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shockwave_weapon_desc_id)

    def _dependencies_for_shockwave_electrocute_sfxid(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shockwave_electrocute_sfxid)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed.dependencies_for, "unnamed", "PatternedAITypedef"),
            (self.actor_parameters.dependencies_for, "actor_parameters", "ActorParameters"),
            (self._dependencies_for_energy_absorb_particle_desc_id, "energy_absorb_particle_desc_id", "AssetId"),
            (self._dependencies_for_energy_absorb_sfx_id, "energy_absorb_sfx_id", "int"),
            (self.launcher_act_params.dependencies_for, "launcher_act_params", "ActorParameters"),
            (self.launcher_anim_params.dependencies_for, "launcher_anim_params", "AnimationParameters"),
            (self._dependencies_for_launcher_particle_gen_desc_id, "launcher_particle_gen_desc_id", "AssetId"),
            (self._dependencies_for_launcher_sfx_id, "launcher_sfx_id", "int"),
            (self._dependencies_for_grenade_model_id, "grenade_model_id", "AssetId"),
            (self._dependencies_for_grenade_element_gen_desc_id1, "grenade_element_gen_desc_id1", "AssetId"),
            (self._dependencies_for_grenade_element_gen_desc_id2, "grenade_element_gen_desc_id2", "AssetId"),
            (self._dependencies_for_grenade_element_gen_desc_id3, "grenade_element_gen_desc_id3", "AssetId"),
            (self._dependencies_for_grenade_element_gen_desc_id4, "grenade_element_gen_desc_id4", "AssetId"),
            (self._dependencies_for_grenade_bounce_sfx_id, "grenade_bounce_sfx_id", "int"),
            (self._dependencies_for_grenade_explode_sfx_id, "grenade_explode_sfx_id", "int"),
            (self._dependencies_for_shockwave_particle_desc_id, "shockwave_particle_desc_id", "AssetId"),
            (self._dependencies_for_shockwave_weapon_desc_id, "shockwave_weapon_desc_id", "AssetId"),
            (self._dependencies_for_shockwave_electrocute_sfxid, "shockwave_electrocute_sfxid", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ElitePirate.{field_name} ({field_type}): {e}")
