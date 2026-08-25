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

    class BurrowerJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        jump_particles: int
        trail_particles: int
        projectile_weapon: int
        unnamed_0x00000009: json_util.JsonObject
        projectile_hit_visor_particles: int
        projectile_hit_visor_sound: int
        death_explosion_particles: int


@dataclasses.dataclass()
class Burrower(BaseObjectType):
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
    jump_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="JumpParticles"),
        },
    )
    trail_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000007, original_name="TrailParticles"),
        },
    )
    projectile_weapon: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="ProjectileWeapon"),
        },
    )
    unnamed_0x00000009: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo, id=0x00000009, original_name="9", from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
            ),
        },
    )
    projectile_hit_visor_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="ProjectileHitVisorParticles"),
        },
    )
    projectile_hit_visor_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="ProjectileHitVisorSound"),
        },
    )
    death_explosion_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="DeathExplosionParticles"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x7F

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
        jump_particles = structs.BIG_L.unpack(data.read(4))[0]
        trail_particles = structs.BIG_L.unpack(data.read(4))[0]
        projectile_weapon = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x00000009 = DamageInfo.from_stream(data, game, property_size)
        projectile_hit_visor_particles = structs.BIG_L.unpack(data.read(4))[0]
        projectile_hit_visor_sound = structs.BIG_l.unpack(data.read(4))[0]
        death_explosion_particles = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            jump_particles,
            trail_particles,
            projectile_weapon,
            unnamed_0x00000009,
            projectile_hit_visor_particles,
            projectile_hit_visor_sound,
            death_explosion_particles,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\r")  # 13 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.jump_particles))
        data.write(structs.BIG_L.pack(self.trail_particles))
        data.write(structs.BIG_L.pack(self.projectile_weapon))
        self.unnamed_0x00000009.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.projectile_hit_visor_particles))
        data.write(structs.BIG_l.pack(self.projectile_hit_visor_sound))
        data.write(structs.BIG_L.pack(self.death_explosion_particles))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BurrowerJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            jump_particles=json_data["jump_particles"],
            trail_particles=json_data["trail_particles"],
            projectile_weapon=json_data["projectile_weapon"],
            unnamed_0x00000009=DamageInfo.from_json(json_data["unnamed_0x00000009"]),
            projectile_hit_visor_particles=json_data["projectile_hit_visor_particles"],
            projectile_hit_visor_sound=json_data["projectile_hit_visor_sound"],
            death_explosion_particles=json_data["death_explosion_particles"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "jump_particles": self.jump_particles,
            "trail_particles": self.trail_particles,
            "projectile_weapon": self.projectile_weapon,
            "unnamed_0x00000009": self.unnamed_0x00000009.to_json(),
            "projectile_hit_visor_particles": self.projectile_hit_visor_particles,
            "projectile_hit_visor_sound": self.projectile_hit_visor_sound,
            "death_explosion_particles": self.death_explosion_particles,
        }

    def _dependencies_for_jump_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.jump_particles)

    def _dependencies_for_trail_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.trail_particles)

    def _dependencies_for_projectile_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_weapon)

    def _dependencies_for_projectile_hit_visor_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_hit_visor_particles)

    def _dependencies_for_projectile_hit_visor_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.projectile_hit_visor_sound)

    def _dependencies_for_death_explosion_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_explosion_particles)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_jump_particles, "jump_particles", "AssetId"),
            (self._dependencies_for_trail_particles, "trail_particles", "AssetId"),
            (self._dependencies_for_projectile_weapon, "projectile_weapon", "AssetId"),
            (self._dependencies_for_projectile_hit_visor_particles, "projectile_hit_visor_particles", "AssetId"),
            (self._dependencies_for_projectile_hit_visor_sound, "projectile_hit_visor_sound", "int"),
            (self._dependencies_for_death_explosion_particles, "death_explosion_particles", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Burrower.{field_name} ({field_type}): {e}")
