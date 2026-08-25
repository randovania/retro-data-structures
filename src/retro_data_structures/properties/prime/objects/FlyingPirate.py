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
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FlyingPirateJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        max_cover_distance: float
        hearing_distance: float
        flying_pirate_type: int
        gun_projectile: int
        gun_damage_info: json_util.JsonObject
        gun_sfx: int
        alt_projectile: int
        alt_projectile_damage_info: json_util.JsonObject
        kamikaze_projectile_info: int
        knockback_delay: float
        flying_height: float
        particle_gen_desc: int
        kamikaze_damage_info: json_util.JsonObject
        unknown_7: float
        unknown_8: float
        unknown_9: float
        unknown_10: float
        rag_doll_sfx1: int
        rag_doll_sfx2: int
        cover_check_chance: float
        unknown_14: float
        unknown_15: float
        particle_gen1: int
        particle_gen2: int
        particle_gen3: int
        knockback_sfx: int
        death_sfx: int
        aggression_chance: float
        unknown_19: float
        projectile_homing_distance: float


@dataclasses.dataclass()
class FlyingPirate(BaseObjectType):
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
    unnamed_0x00000004: PatternedAITypedef = dataclasses.field(
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
    unnamed_0x00000005: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000005,
                original_name="5",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    max_cover_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="MaxCoverDistance"),
        },
    )
    hearing_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="HearingDistance"),
        },
    )
    flying_pirate_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="FlyingPirateType"),
        },
    )
    gun_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="GunProjectile"),
        },
    )
    gun_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000A,
                original_name="GunDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    gun_sfx: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="GunSFX"),
        },
    )
    alt_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="AltProjectile"),
        },
    )
    alt_projectile_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000D,
                original_name="AltProjectileDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    kamikaze_projectile_info: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="KamikazeProjectileInfo"),
        },
    )
    knockback_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="KnockbackDelay"),
        },
    )
    flying_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="FlyingHeight"),
        },
    )
    particle_gen_desc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="ParticleGenDesc"),
        },
    )
    kamikaze_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000012,
                original_name="KamikazeDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Unknown 8"),
        },
    )
    unknown_9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="Unknown 9"),
        },
    )
    unknown_10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="Unknown 10"),
        },
    )
    rag_doll_sfx1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000017, original_name="RagDollSFX1"),
        },
    )
    rag_doll_sfx2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000018, original_name="RagDollSFX2"),
        },
    )
    cover_check_chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000019, original_name="CoverCheckChance"),
        },
    )
    unknown_14: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001A, original_name="Unknown 14"),
        },
    )
    unknown_15: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="Unknown 15"),
        },
    )
    particle_gen1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001C, original_name="ParticleGen1"),
        },
    )
    particle_gen2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001D, original_name="ParticleGen2"),
        },
    )
    particle_gen3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001E, original_name="ParticleGen3"),
        },
    )
    knockback_sfx: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="KnockbackSFX"),
        },
    )
    death_sfx: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000020, original_name="DeathSFX"),
        },
    )
    aggression_chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000021, original_name="AggressionChance"),
        },
    )
    unknown_19: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000022, original_name="Unknown 19"),
        },
    )
    projectile_homing_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000023, original_name="ProjectileHomingDistance"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x25

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
        unnamed_0x00000004 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000005 = ActorParameters.from_stream(data, game, property_size)
        max_cover_distance = structs.BIG_f.unpack(data.read(4))[0]
        hearing_distance = structs.BIG_f.unpack(data.read(4))[0]
        flying_pirate_type = structs.BIG_l.unpack(data.read(4))[0]
        gun_projectile = structs.BIG_L.unpack(data.read(4))[0]
        gun_damage_info = DamageInfo.from_stream(data, game, property_size)
        gun_sfx = structs.BIG_l.unpack(data.read(4))[0]
        alt_projectile = structs.BIG_L.unpack(data.read(4))[0]
        alt_projectile_damage_info = DamageInfo.from_stream(data, game, property_size)
        kamikaze_projectile_info = structs.BIG_L.unpack(data.read(4))[0]
        knockback_delay = structs.BIG_f.unpack(data.read(4))[0]
        flying_height = structs.BIG_f.unpack(data.read(4))[0]
        particle_gen_desc = structs.BIG_L.unpack(data.read(4))[0]
        kamikaze_damage_info = DamageInfo.from_stream(data, game, property_size)
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_f.unpack(data.read(4))[0]
        rag_doll_sfx1 = structs.BIG_l.unpack(data.read(4))[0]
        rag_doll_sfx2 = structs.BIG_l.unpack(data.read(4))[0]
        cover_check_chance = structs.BIG_f.unpack(data.read(4))[0]
        unknown_14 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_15 = structs.BIG_f.unpack(data.read(4))[0]
        particle_gen1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_gen2 = structs.BIG_L.unpack(data.read(4))[0]
        particle_gen3 = structs.BIG_L.unpack(data.read(4))[0]
        knockback_sfx = structs.BIG_l.unpack(data.read(4))[0]
        death_sfx = structs.BIG_l.unpack(data.read(4))[0]
        aggression_chance = structs.BIG_f.unpack(data.read(4))[0]
        unknown_19 = structs.BIG_f.unpack(data.read(4))[0]
        projectile_homing_distance = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            max_cover_distance,
            hearing_distance,
            flying_pirate_type,
            gun_projectile,
            gun_damage_info,
            gun_sfx,
            alt_projectile,
            alt_projectile_damage_info,
            kamikaze_projectile_info,
            knockback_delay,
            flying_height,
            particle_gen_desc,
            kamikaze_damage_info,
            unknown_7,
            unknown_8,
            unknown_9,
            unknown_10,
            rag_doll_sfx1,
            rag_doll_sfx2,
            cover_check_chance,
            unknown_14,
            unknown_15,
            particle_gen1,
            particle_gen2,
            particle_gen3,
            knockback_sfx,
            death_sfx,
            aggression_chance,
            unknown_19,
            projectile_homing_distance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00$")  # 36 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.max_cover_distance))
        data.write(structs.BIG_f.pack(self.hearing_distance))
        data.write(structs.BIG_l.pack(self.flying_pirate_type))
        data.write(structs.BIG_L.pack(self.gun_projectile))
        self.gun_damage_info.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.gun_sfx))
        data.write(structs.BIG_L.pack(self.alt_projectile))
        self.alt_projectile_damage_info.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.kamikaze_projectile_info))
        data.write(structs.BIG_f.pack(self.knockback_delay))
        data.write(structs.BIG_f.pack(self.flying_height))
        data.write(structs.BIG_L.pack(self.particle_gen_desc))
        self.kamikaze_damage_info.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        data.write(structs.BIG_f.pack(self.unknown_9))
        data.write(structs.BIG_f.pack(self.unknown_10))
        data.write(structs.BIG_l.pack(self.rag_doll_sfx1))
        data.write(structs.BIG_l.pack(self.rag_doll_sfx2))
        data.write(structs.BIG_f.pack(self.cover_check_chance))
        data.write(structs.BIG_f.pack(self.unknown_14))
        data.write(structs.BIG_f.pack(self.unknown_15))
        data.write(structs.BIG_L.pack(self.particle_gen1))
        data.write(structs.BIG_L.pack(self.particle_gen2))
        data.write(structs.BIG_L.pack(self.particle_gen3))
        data.write(structs.BIG_l.pack(self.knockback_sfx))
        data.write(structs.BIG_l.pack(self.death_sfx))
        data.write(structs.BIG_f.pack(self.aggression_chance))
        data.write(structs.BIG_f.pack(self.unknown_19))
        data.write(structs.BIG_f.pack(self.projectile_homing_distance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            max_cover_distance=json_data["max_cover_distance"],
            hearing_distance=json_data["hearing_distance"],
            flying_pirate_type=json_data["flying_pirate_type"],
            gun_projectile=json_data["gun_projectile"],
            gun_damage_info=DamageInfo.from_json(json_data["gun_damage_info"]),
            gun_sfx=json_data["gun_sfx"],
            alt_projectile=json_data["alt_projectile"],
            alt_projectile_damage_info=DamageInfo.from_json(json_data["alt_projectile_damage_info"]),
            kamikaze_projectile_info=json_data["kamikaze_projectile_info"],
            knockback_delay=json_data["knockback_delay"],
            flying_height=json_data["flying_height"],
            particle_gen_desc=json_data["particle_gen_desc"],
            kamikaze_damage_info=DamageInfo.from_json(json_data["kamikaze_damage_info"]),
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            rag_doll_sfx1=json_data["rag_doll_sfx1"],
            rag_doll_sfx2=json_data["rag_doll_sfx2"],
            cover_check_chance=json_data["cover_check_chance"],
            unknown_14=json_data["unknown_14"],
            unknown_15=json_data["unknown_15"],
            particle_gen1=json_data["particle_gen1"],
            particle_gen2=json_data["particle_gen2"],
            particle_gen3=json_data["particle_gen3"],
            knockback_sfx=json_data["knockback_sfx"],
            death_sfx=json_data["death_sfx"],
            aggression_chance=json_data["aggression_chance"],
            unknown_19=json_data["unknown_19"],
            projectile_homing_distance=json_data["projectile_homing_distance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "max_cover_distance": self.max_cover_distance,
            "hearing_distance": self.hearing_distance,
            "flying_pirate_type": self.flying_pirate_type,
            "gun_projectile": self.gun_projectile,
            "gun_damage_info": self.gun_damage_info.to_json(),
            "gun_sfx": self.gun_sfx,
            "alt_projectile": self.alt_projectile,
            "alt_projectile_damage_info": self.alt_projectile_damage_info.to_json(),
            "kamikaze_projectile_info": self.kamikaze_projectile_info,
            "knockback_delay": self.knockback_delay,
            "flying_height": self.flying_height,
            "particle_gen_desc": self.particle_gen_desc,
            "kamikaze_damage_info": self.kamikaze_damage_info.to_json(),
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "rag_doll_sfx1": self.rag_doll_sfx1,
            "rag_doll_sfx2": self.rag_doll_sfx2,
            "cover_check_chance": self.cover_check_chance,
            "unknown_14": self.unknown_14,
            "unknown_15": self.unknown_15,
            "particle_gen1": self.particle_gen1,
            "particle_gen2": self.particle_gen2,
            "particle_gen3": self.particle_gen3,
            "knockback_sfx": self.knockback_sfx,
            "death_sfx": self.death_sfx,
            "aggression_chance": self.aggression_chance,
            "unknown_19": self.unknown_19,
            "projectile_homing_distance": self.projectile_homing_distance,
        }

    def _dependencies_for_gun_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.gun_projectile)

    def _dependencies_for_gun_sfx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.gun_sfx)

    def _dependencies_for_alt_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.alt_projectile)

    def _dependencies_for_kamikaze_projectile_info(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.kamikaze_projectile_info)

    def _dependencies_for_particle_gen_desc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_gen_desc)

    def _dependencies_for_rag_doll_sfx1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.rag_doll_sfx1)

    def _dependencies_for_rag_doll_sfx2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.rag_doll_sfx2)

    def _dependencies_for_particle_gen1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_gen1)

    def _dependencies_for_particle_gen2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_gen2)

    def _dependencies_for_particle_gen3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_gen3)

    def _dependencies_for_knockback_sfx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.knockback_sfx)

    def _dependencies_for_death_sfx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.death_sfx)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_gun_projectile, "gun_projectile", "AssetId"),
            (self._dependencies_for_gun_sfx, "gun_sfx", "int"),
            (self._dependencies_for_alt_projectile, "alt_projectile", "AssetId"),
            (self._dependencies_for_kamikaze_projectile_info, "kamikaze_projectile_info", "AssetId"),
            (self._dependencies_for_particle_gen_desc, "particle_gen_desc", "AssetId"),
            (self._dependencies_for_rag_doll_sfx1, "rag_doll_sfx1", "int"),
            (self._dependencies_for_rag_doll_sfx2, "rag_doll_sfx2", "int"),
            (self._dependencies_for_particle_gen1, "particle_gen1", "AssetId"),
            (self._dependencies_for_particle_gen2, "particle_gen2", "AssetId"),
            (self._dependencies_for_particle_gen3, "particle_gen3", "AssetId"),
            (self._dependencies_for_knockback_sfx, "knockback_sfx", "int"),
            (self._dependencies_for_death_sfx, "death_sfx", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for FlyingPirate.{field_name} ({field_type}): {e}")
