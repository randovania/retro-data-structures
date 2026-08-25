# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PatternedAITypedefJson(typing_extensions.TypedDict):
        mass: float
        speed: float
        turn_speed: float
        detection_range: float
        detection_height_range: float
        detection_angle: float
        min_attack_range: float
        max_attack_range: float
        average_attack_time: float
        attack_time_variation: float
        leash_radius: float
        player_leash_radius: float
        player_leash_time: float
        contact_damage: json_util.JsonObject
        damage_wait_time: float
        unnamed: json_util.JsonObject
        vulnerability: json_util.JsonObject
        half_extend: float
        height: float
        body_origin: json_util.JsonValue
        step_up_height: float
        x_damage: float
        frozen_x_damage: float
        x_damage_delay: float
        death_sound: int
        animation_parameters: json_util.JsonObject
        active: bool
        state_machine: int
        into_freeze_duration: float
        out_of_freeze_duration: float
        freeze_duration: float
        path_finding_index: int
        particle_2_scale_0x00000020: json_util.JsonValue
        particle_1: int
        electric: int
        particle_2_scale_0x00000023: json_util.JsonValue
        particle_2: int
        ice_shatter_sound: int


@dataclasses.dataclass()
class PatternedAITypedef(BaseProperty):
    mass: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Mass"),
        },
    )
    speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Speed"),
        },
    )
    turn_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="Turn Speed"),
        },
    )
    detection_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Detection Range"),
        },
    )
    detection_height_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Detection Height Range"),
        },
    )
    detection_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Detection Angle"),
        },
    )
    min_attack_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Min Attack Range"),
        },
    )
    max_attack_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Max Attack Range"),
        },
    )
    average_attack_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Average Attack Time"),
        },
    )
    attack_time_variation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Attack Time Variation"),
        },
    )
    leash_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="Leash Radius"),
        },
    )
    player_leash_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="Player Leash Radius"),
        },
    )
    player_leash_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="Player Leash Time"),
        },
    )
    contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000D,
                original_name="ContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_wait_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Damage Wait Time"),
        },
    )
    unnamed: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x0000000F,
                original_name="15",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000010,
                original_name="Vulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    half_extend: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="Half Extend"),
        },
    )
    height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="Height"),
        },
    )
    body_origin: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000013, original_name="Body Origin", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    step_up_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Step Up Height"),
        },
    )
    x_damage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="xDamage"),
        },
    )
    frozen_x_damage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="frozenX Damage"),
        },
    )
    x_damage_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="xDamage Delay"),
        },
    )
    death_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000018, original_name="Death Sound"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000019,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000001A, original_name="Active"),
        },
    )
    state_machine: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["AFSM"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001B, original_name="State Machine"),
        },
    )
    into_freeze_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="Into Freeze Duration"),
        },
    )
    out_of_freeze_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="Out Of Freeze Duration"),
        },
    )
    freeze_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="Freeze Duration"),
        },
    )
    path_finding_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="Path Finding Index"),
        },
    )
    particle_2_scale_0x00000020: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000020,
                original_name="Particle 2 Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000021, original_name="Particle 1"),
        },
    )
    electric: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000022, original_name="Electric"),
        },
    )
    particle_2_scale_0x00000023: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000023,
                original_name="Particle 2 Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000024, original_name="Particle 2"),
        },
    )
    ice_shatter_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000025, original_name="Ice Shatter Sound"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        mass = structs.BIG_f.unpack(data.read(4))[0]
        speed = structs.BIG_f.unpack(data.read(4))[0]
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]
        detection_range = structs.BIG_f.unpack(data.read(4))[0]
        detection_height_range = structs.BIG_f.unpack(data.read(4))[0]
        detection_angle = structs.BIG_f.unpack(data.read(4))[0]
        min_attack_range = structs.BIG_f.unpack(data.read(4))[0]
        max_attack_range = structs.BIG_f.unpack(data.read(4))[0]
        average_attack_time = structs.BIG_f.unpack(data.read(4))[0]
        attack_time_variation = structs.BIG_f.unpack(data.read(4))[0]
        leash_radius = structs.BIG_f.unpack(data.read(4))[0]
        player_leash_radius = structs.BIG_f.unpack(data.read(4))[0]
        player_leash_time = structs.BIG_f.unpack(data.read(4))[0]
        contact_damage = DamageInfo.from_stream(data, game, property_size)
        damage_wait_time = structs.BIG_f.unpack(data.read(4))[0]
        unnamed = HealthInfo.from_stream(data, game, property_size)
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
        half_extend = structs.BIG_f.unpack(data.read(4))[0]
        height = structs.BIG_f.unpack(data.read(4))[0]
        body_origin = Vector.from_stream(data, game, property_size)
        step_up_height = structs.BIG_f.unpack(data.read(4))[0]
        x_damage = structs.BIG_f.unpack(data.read(4))[0]
        frozen_x_damage = structs.BIG_f.unpack(data.read(4))[0]
        x_damage_delay = structs.BIG_f.unpack(data.read(4))[0]
        death_sound = structs.BIG_l.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        state_machine = structs.BIG_L.unpack(data.read(4))[0]
        into_freeze_duration = structs.BIG_f.unpack(data.read(4))[0]
        out_of_freeze_duration = structs.BIG_f.unpack(data.read(4))[0]
        freeze_duration = structs.BIG_f.unpack(data.read(4))[0]
        path_finding_index = structs.BIG_l.unpack(data.read(4))[0]
        particle_2_scale_0x00000020 = Vector.from_stream(data, game, property_size)
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        electric = structs.BIG_l.unpack(data.read(4))[0]
        particle_2_scale_0x00000023 = Vector.from_stream(data, game, property_size)
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        ice_shatter_sound = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            mass,
            speed,
            turn_speed,
            detection_range,
            detection_height_range,
            detection_angle,
            min_attack_range,
            max_attack_range,
            average_attack_time,
            attack_time_variation,
            leash_radius,
            player_leash_radius,
            player_leash_time,
            contact_damage,
            damage_wait_time,
            unnamed,
            vulnerability,
            half_extend,
            height,
            body_origin,
            step_up_height,
            x_damage,
            frozen_x_damage,
            x_damage_delay,
            death_sound,
            animation_parameters,
            active,
            state_machine,
            into_freeze_duration,
            out_of_freeze_duration,
            freeze_duration,
            path_finding_index,
            particle_2_scale_0x00000020,
            particle_1,
            electric,
            particle_2_scale_0x00000023,
            particle_2,
            ice_shatter_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.mass))
        data.write(structs.BIG_f.pack(self.speed))
        data.write(structs.BIG_f.pack(self.turn_speed))
        data.write(structs.BIG_f.pack(self.detection_range))
        data.write(structs.BIG_f.pack(self.detection_height_range))
        data.write(structs.BIG_f.pack(self.detection_angle))
        data.write(structs.BIG_f.pack(self.min_attack_range))
        data.write(structs.BIG_f.pack(self.max_attack_range))
        data.write(structs.BIG_f.pack(self.average_attack_time))
        data.write(structs.BIG_f.pack(self.attack_time_variation))
        data.write(structs.BIG_f.pack(self.leash_radius))
        data.write(structs.BIG_f.pack(self.player_leash_radius))
        data.write(structs.BIG_f.pack(self.player_leash_time))
        self.contact_damage.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.damage_wait_time))
        self.unnamed.to_stream(data, game)
        self.vulnerability.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.half_extend))
        data.write(structs.BIG_f.pack(self.height))
        self.body_origin.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.step_up_height))
        data.write(structs.BIG_f.pack(self.x_damage))
        data.write(structs.BIG_f.pack(self.frozen_x_damage))
        data.write(structs.BIG_f.pack(self.x_damage_delay))
        data.write(structs.BIG_l.pack(self.death_sound))
        self.animation_parameters.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_L.pack(self.state_machine))
        data.write(structs.BIG_f.pack(self.into_freeze_duration))
        data.write(structs.BIG_f.pack(self.out_of_freeze_duration))
        data.write(structs.BIG_f.pack(self.freeze_duration))
        data.write(structs.BIG_l.pack(self.path_finding_index))
        self.particle_2_scale_0x00000020.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_l.pack(self.electric))
        self.particle_2_scale_0x00000023.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_l.pack(self.ice_shatter_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PatternedAITypedefJson", data)
        return cls(
            mass=json_data["mass"],
            speed=json_data["speed"],
            turn_speed=json_data["turn_speed"],
            detection_range=json_data["detection_range"],
            detection_height_range=json_data["detection_height_range"],
            detection_angle=json_data["detection_angle"],
            min_attack_range=json_data["min_attack_range"],
            max_attack_range=json_data["max_attack_range"],
            average_attack_time=json_data["average_attack_time"],
            attack_time_variation=json_data["attack_time_variation"],
            leash_radius=json_data["leash_radius"],
            player_leash_radius=json_data["player_leash_radius"],
            player_leash_time=json_data["player_leash_time"],
            contact_damage=DamageInfo.from_json(json_data["contact_damage"]),
            damage_wait_time=json_data["damage_wait_time"],
            unnamed=HealthInfo.from_json(json_data["unnamed"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            half_extend=json_data["half_extend"],
            height=json_data["height"],
            body_origin=Vector.from_json(json_data["body_origin"]),
            step_up_height=json_data["step_up_height"],
            x_damage=json_data["x_damage"],
            frozen_x_damage=json_data["frozen_x_damage"],
            x_damage_delay=json_data["x_damage_delay"],
            death_sound=json_data["death_sound"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            active=json_data["active"],
            state_machine=json_data["state_machine"],
            into_freeze_duration=json_data["into_freeze_duration"],
            out_of_freeze_duration=json_data["out_of_freeze_duration"],
            freeze_duration=json_data["freeze_duration"],
            path_finding_index=json_data["path_finding_index"],
            particle_2_scale_0x00000020=Vector.from_json(json_data["particle_2_scale_0x00000020"]),
            particle_1=json_data["particle_1"],
            electric=json_data["electric"],
            particle_2_scale_0x00000023=Vector.from_json(json_data["particle_2_scale_0x00000023"]),
            particle_2=json_data["particle_2"],
            ice_shatter_sound=json_data["ice_shatter_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "mass": self.mass,
            "speed": self.speed,
            "turn_speed": self.turn_speed,
            "detection_range": self.detection_range,
            "detection_height_range": self.detection_height_range,
            "detection_angle": self.detection_angle,
            "min_attack_range": self.min_attack_range,
            "max_attack_range": self.max_attack_range,
            "average_attack_time": self.average_attack_time,
            "attack_time_variation": self.attack_time_variation,
            "leash_radius": self.leash_radius,
            "player_leash_radius": self.player_leash_radius,
            "player_leash_time": self.player_leash_time,
            "contact_damage": self.contact_damage.to_json(),
            "damage_wait_time": self.damage_wait_time,
            "unnamed": self.unnamed.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "half_extend": self.half_extend,
            "height": self.height,
            "body_origin": self.body_origin.to_json(),
            "step_up_height": self.step_up_height,
            "x_damage": self.x_damage,
            "frozen_x_damage": self.frozen_x_damage,
            "x_damage_delay": self.x_damage_delay,
            "death_sound": self.death_sound,
            "animation_parameters": self.animation_parameters.to_json(),
            "active": self.active,
            "state_machine": self.state_machine,
            "into_freeze_duration": self.into_freeze_duration,
            "out_of_freeze_duration": self.out_of_freeze_duration,
            "freeze_duration": self.freeze_duration,
            "path_finding_index": self.path_finding_index,
            "particle_2_scale_0x00000020": self.particle_2_scale_0x00000020.to_json(),
            "particle_1": self.particle_1,
            "electric": self.electric,
            "particle_2_scale_0x00000023": self.particle_2_scale_0x00000023.to_json(),
            "particle_2": self.particle_2,
            "ice_shatter_sound": self.ice_shatter_sound,
        }

    def _dependencies_for_death_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.death_sound)

    def _dependencies_for_state_machine(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.state_machine)

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_ice_shatter_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.ice_shatter_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_death_sound, "death_sound", "int"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self._dependencies_for_state_machine, "state_machine", "AssetId"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_ice_shatter_sound, "ice_shatter_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PatternedAITypedef.{field_name} ({field_type}): {e}")
