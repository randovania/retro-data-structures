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
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class BabygothJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        fireball_attack_time: float
        fireball_attack_time_variance: float
        fireball_weapon: int
        fireball_damage: json_util.JsonObject
        attack_contact_damage: json_util.JsonObject
        fire_breath_weapon: int
        fire_breath_particles: int
        fire_breath_damage: json_util.JsonObject
        mouth_vulnerability: json_util.JsonObject
        shell_vulnerability: json_util.JsonObject
        no_shell_model: int
        no_shell_skin: int
        shell_hp: float
        shell_crack_sound: int
        intermediate_crack_particles: int
        crack_one_particles: int
        crack_two_particles: int
        destroy_shell_particles: int
        crack_one_sound: int
        crack_two_sound: int
        destroy_shell_sound: int
        time_until_attack: float
        attack_cooldown_time: float
        interest_time: float
        flame_player_steam_texture: int
        flame_player_hit_sound: int
        flame_player_ice_texture: int


@dataclasses.dataclass()
class Babygoth(BaseObjectType):
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
    fireball_attack_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="FireballAttackTime"),
        },
    )
    fireball_attack_time_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="FireballAttackTimeVariance"),
        },
    )
    fireball_weapon: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="FireballWeapon"),
        },
    )
    fireball_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000009,
                original_name="FireballDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    attack_contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000A,
                original_name="AttackContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    fire_breath_weapon: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="FireBreathWeapon"),
        },
    )
    fire_breath_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="FireBreathParticles"),
        },
    )
    fire_breath_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000D,
                original_name="FireBreathDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    mouth_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000E,
                original_name="MouthVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    shell_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000F,
                original_name="ShellVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    no_shell_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000010, original_name="NoShellModel"),
        },
    )
    no_shell_skin: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="NoShellSkin"),
        },
    )
    shell_hp: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="ShellHP"),
        },
    )
    shell_crack_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="ShellCrackSound"),
        },
    )
    intermediate_crack_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000014, original_name="IntermediateCrackParticles"),
        },
    )
    crack_one_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000015, original_name="CrackOneParticles"),
        },
    )
    crack_two_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000016, original_name="CrackTwoParticles"),
        },
    )
    destroy_shell_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000017, original_name="DestroyShellParticles"),
        },
    )
    crack_one_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000018, original_name="CrackOneSound"),
        },
    )
    crack_two_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000019, original_name="CrackTwoSound"),
        },
    )
    destroy_shell_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000001A, original_name="DestroyShellSound"),
        },
    )
    time_until_attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="TimeUntilAttack"),
        },
    )
    attack_cooldown_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="AttackCooldownTime"),
        },
    )
    interest_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="InterestTime"),
        },
    )
    flame_player_steam_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001E, original_name="FlamePlayerSteamTexture"),
        },
    )
    flame_player_hit_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="FlamePlayerHitSound"),
        },
    )
    flame_player_ice_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000020, original_name="FlamePlayerIceTexture"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x66

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
        fireball_attack_time = structs.BIG_f.unpack(data.read(4))[0]
        fireball_attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]
        fireball_weapon = structs.BIG_L.unpack(data.read(4))[0]
        fireball_damage = DamageInfo.from_stream(data, game, property_size)
        attack_contact_damage = DamageInfo.from_stream(data, game, property_size)
        fire_breath_weapon = structs.BIG_L.unpack(data.read(4))[0]
        fire_breath_particles = structs.BIG_L.unpack(data.read(4))[0]
        fire_breath_damage = DamageInfo.from_stream(data, game, property_size)
        mouth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
        shell_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
        no_shell_model = structs.BIG_L.unpack(data.read(4))[0]
        no_shell_skin = structs.BIG_L.unpack(data.read(4))[0]
        shell_hp = structs.BIG_f.unpack(data.read(4))[0]
        shell_crack_sound = structs.BIG_l.unpack(data.read(4))[0]
        intermediate_crack_particles = structs.BIG_L.unpack(data.read(4))[0]
        crack_one_particles = structs.BIG_L.unpack(data.read(4))[0]
        crack_two_particles = structs.BIG_L.unpack(data.read(4))[0]
        destroy_shell_particles = structs.BIG_L.unpack(data.read(4))[0]
        crack_one_sound = structs.BIG_l.unpack(data.read(4))[0]
        crack_two_sound = structs.BIG_l.unpack(data.read(4))[0]
        destroy_shell_sound = structs.BIG_l.unpack(data.read(4))[0]
        time_until_attack = structs.BIG_f.unpack(data.read(4))[0]
        attack_cooldown_time = structs.BIG_f.unpack(data.read(4))[0]
        interest_time = structs.BIG_f.unpack(data.read(4))[0]
        flame_player_steam_texture = structs.BIG_L.unpack(data.read(4))[0]
        flame_player_hit_sound = structs.BIG_l.unpack(data.read(4))[0]
        flame_player_ice_texture = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            fireball_attack_time,
            fireball_attack_time_variance,
            fireball_weapon,
            fireball_damage,
            attack_contact_damage,
            fire_breath_weapon,
            fire_breath_particles,
            fire_breath_damage,
            mouth_vulnerability,
            shell_vulnerability,
            no_shell_model,
            no_shell_skin,
            shell_hp,
            shell_crack_sound,
            intermediate_crack_particles,
            crack_one_particles,
            crack_two_particles,
            destroy_shell_particles,
            crack_one_sound,
            crack_two_sound,
            destroy_shell_sound,
            time_until_attack,
            attack_cooldown_time,
            interest_time,
            flame_player_steam_texture,
            flame_player_hit_sound,
            flame_player_ice_texture,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00!")  # 33 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.fireball_attack_time))
        data.write(structs.BIG_f.pack(self.fireball_attack_time_variance))
        data.write(structs.BIG_L.pack(self.fireball_weapon))
        self.fireball_damage.to_stream(data, game)
        self.attack_contact_damage.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.fire_breath_weapon))
        data.write(structs.BIG_L.pack(self.fire_breath_particles))
        self.fire_breath_damage.to_stream(data, game)
        self.mouth_vulnerability.to_stream(data, game)
        self.shell_vulnerability.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.no_shell_model))
        data.write(structs.BIG_L.pack(self.no_shell_skin))
        data.write(structs.BIG_f.pack(self.shell_hp))
        data.write(structs.BIG_l.pack(self.shell_crack_sound))
        data.write(structs.BIG_L.pack(self.intermediate_crack_particles))
        data.write(structs.BIG_L.pack(self.crack_one_particles))
        data.write(structs.BIG_L.pack(self.crack_two_particles))
        data.write(structs.BIG_L.pack(self.destroy_shell_particles))
        data.write(structs.BIG_l.pack(self.crack_one_sound))
        data.write(structs.BIG_l.pack(self.crack_two_sound))
        data.write(structs.BIG_l.pack(self.destroy_shell_sound))
        data.write(structs.BIG_f.pack(self.time_until_attack))
        data.write(structs.BIG_f.pack(self.attack_cooldown_time))
        data.write(structs.BIG_f.pack(self.interest_time))
        data.write(structs.BIG_L.pack(self.flame_player_steam_texture))
        data.write(structs.BIG_l.pack(self.flame_player_hit_sound))
        data.write(structs.BIG_L.pack(self.flame_player_ice_texture))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BabygothJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            fireball_attack_time=json_data["fireball_attack_time"],
            fireball_attack_time_variance=json_data["fireball_attack_time_variance"],
            fireball_weapon=json_data["fireball_weapon"],
            fireball_damage=DamageInfo.from_json(json_data["fireball_damage"]),
            attack_contact_damage=DamageInfo.from_json(json_data["attack_contact_damage"]),
            fire_breath_weapon=json_data["fire_breath_weapon"],
            fire_breath_particles=json_data["fire_breath_particles"],
            fire_breath_damage=DamageInfo.from_json(json_data["fire_breath_damage"]),
            mouth_vulnerability=DamageVulnerability.from_json(json_data["mouth_vulnerability"]),
            shell_vulnerability=DamageVulnerability.from_json(json_data["shell_vulnerability"]),
            no_shell_model=json_data["no_shell_model"],
            no_shell_skin=json_data["no_shell_skin"],
            shell_hp=json_data["shell_hp"],
            shell_crack_sound=json_data["shell_crack_sound"],
            intermediate_crack_particles=json_data["intermediate_crack_particles"],
            crack_one_particles=json_data["crack_one_particles"],
            crack_two_particles=json_data["crack_two_particles"],
            destroy_shell_particles=json_data["destroy_shell_particles"],
            crack_one_sound=json_data["crack_one_sound"],
            crack_two_sound=json_data["crack_two_sound"],
            destroy_shell_sound=json_data["destroy_shell_sound"],
            time_until_attack=json_data["time_until_attack"],
            attack_cooldown_time=json_data["attack_cooldown_time"],
            interest_time=json_data["interest_time"],
            flame_player_steam_texture=json_data["flame_player_steam_texture"],
            flame_player_hit_sound=json_data["flame_player_hit_sound"],
            flame_player_ice_texture=json_data["flame_player_ice_texture"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "fireball_attack_time": self.fireball_attack_time,
            "fireball_attack_time_variance": self.fireball_attack_time_variance,
            "fireball_weapon": self.fireball_weapon,
            "fireball_damage": self.fireball_damage.to_json(),
            "attack_contact_damage": self.attack_contact_damage.to_json(),
            "fire_breath_weapon": self.fire_breath_weapon,
            "fire_breath_particles": self.fire_breath_particles,
            "fire_breath_damage": self.fire_breath_damage.to_json(),
            "mouth_vulnerability": self.mouth_vulnerability.to_json(),
            "shell_vulnerability": self.shell_vulnerability.to_json(),
            "no_shell_model": self.no_shell_model,
            "no_shell_skin": self.no_shell_skin,
            "shell_hp": self.shell_hp,
            "shell_crack_sound": self.shell_crack_sound,
            "intermediate_crack_particles": self.intermediate_crack_particles,
            "crack_one_particles": self.crack_one_particles,
            "crack_two_particles": self.crack_two_particles,
            "destroy_shell_particles": self.destroy_shell_particles,
            "crack_one_sound": self.crack_one_sound,
            "crack_two_sound": self.crack_two_sound,
            "destroy_shell_sound": self.destroy_shell_sound,
            "time_until_attack": self.time_until_attack,
            "attack_cooldown_time": self.attack_cooldown_time,
            "interest_time": self.interest_time,
            "flame_player_steam_texture": self.flame_player_steam_texture,
            "flame_player_hit_sound": self.flame_player_hit_sound,
            "flame_player_ice_texture": self.flame_player_ice_texture,
        }

    def _dependencies_for_fireball_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fireball_weapon)

    def _dependencies_for_fire_breath_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fire_breath_weapon)

    def _dependencies_for_fire_breath_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fire_breath_particles)

    def _dependencies_for_no_shell_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.no_shell_model)

    def _dependencies_for_no_shell_skin(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.no_shell_skin)

    def _dependencies_for_shell_crack_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shell_crack_sound)

    def _dependencies_for_intermediate_crack_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.intermediate_crack_particles)

    def _dependencies_for_crack_one_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.crack_one_particles)

    def _dependencies_for_crack_two_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.crack_two_particles)

    def _dependencies_for_destroy_shell_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.destroy_shell_particles)

    def _dependencies_for_crack_one_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.crack_one_sound)

    def _dependencies_for_crack_two_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.crack_two_sound)

    def _dependencies_for_destroy_shell_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.destroy_shell_sound)

    def _dependencies_for_flame_player_steam_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.flame_player_steam_texture)

    def _dependencies_for_flame_player_hit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.flame_player_hit_sound)

    def _dependencies_for_flame_player_ice_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.flame_player_ice_texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_fireball_weapon, "fireball_weapon", "AssetId"),
            (self._dependencies_for_fire_breath_weapon, "fire_breath_weapon", "AssetId"),
            (self._dependencies_for_fire_breath_particles, "fire_breath_particles", "AssetId"),
            (self._dependencies_for_no_shell_model, "no_shell_model", "AssetId"),
            (self._dependencies_for_no_shell_skin, "no_shell_skin", "AssetId"),
            (self._dependencies_for_shell_crack_sound, "shell_crack_sound", "int"),
            (self._dependencies_for_intermediate_crack_particles, "intermediate_crack_particles", "AssetId"),
            (self._dependencies_for_crack_one_particles, "crack_one_particles", "AssetId"),
            (self._dependencies_for_crack_two_particles, "crack_two_particles", "AssetId"),
            (self._dependencies_for_destroy_shell_particles, "destroy_shell_particles", "AssetId"),
            (self._dependencies_for_crack_one_sound, "crack_one_sound", "int"),
            (self._dependencies_for_crack_two_sound, "crack_two_sound", "int"),
            (self._dependencies_for_destroy_shell_sound, "destroy_shell_sound", "int"),
            (self._dependencies_for_flame_player_steam_texture, "flame_player_steam_texture", "AssetId"),
            (self._dependencies_for_flame_player_hit_sound, "flame_player_hit_sound", "int"),
            (self._dependencies_for_flame_player_ice_texture, "flame_player_ice_texture", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Babygoth.{field_name} ({field_type}): {e}")
