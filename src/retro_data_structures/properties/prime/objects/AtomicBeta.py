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

    class AtomicBetaJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        electric_particles: int
        weapon_particles: int
        unnamed_0x00000008: json_util.JsonObject
        particles: int
        beam_fade_time: float
        beam_radius: float
        move_speed: float
        unnamed_0x0000000d: json_util.JsonObject
        min_speed: float
        max_speed: float
        speed_step: float
        out_of_range_sound: int
        in_range_sound1: int
        in_range_sound2: int
        beam_damage_interval: float


@dataclasses.dataclass()
class AtomicBeta(BaseObjectType):
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
    electric_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="ElectricParticles"),
        },
    )
    weapon_particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000007, original_name="WeaponParticles"),
        },
    )
    unnamed_0x00000008: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo, id=0x00000008, original_name="8", from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
            ),
        },
    )
    particles: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="Particles"),
        },
    )
    beam_fade_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="BeamFadeTime"),
        },
    )
    beam_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="BeamRadius"),
        },
    )
    move_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="MoveSpeed"),
        },
    )
    unnamed_0x0000000d: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000D,
                original_name="13",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    min_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="MinSpeed"),
        },
    )
    max_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="MaxSpeed"),
        },
    )
    speed_step: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="SpeedStep"),
        },
    )
    out_of_range_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000011, original_name="OutOfRangeSound"),
        },
    )
    in_range_sound1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000012, original_name="InRangeSound1"),
        },
    )
    in_range_sound2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="InRangeSound2"),
        },
    )
    beam_damage_interval: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="BeamDamageInterval"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x77

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
        electric_particles = structs.BIG_L.unpack(data.read(4))[0]
        weapon_particles = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x00000008 = DamageInfo.from_stream(data, game, property_size)
        particles = structs.BIG_L.unpack(data.read(4))[0]
        beam_fade_time = structs.BIG_f.unpack(data.read(4))[0]
        beam_radius = structs.BIG_f.unpack(data.read(4))[0]
        move_speed = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x0000000d = DamageVulnerability.from_stream(data, game, property_size)
        min_speed = structs.BIG_f.unpack(data.read(4))[0]
        max_speed = structs.BIG_f.unpack(data.read(4))[0]
        speed_step = structs.BIG_f.unpack(data.read(4))[0]
        out_of_range_sound = structs.BIG_l.unpack(data.read(4))[0]
        in_range_sound1 = structs.BIG_l.unpack(data.read(4))[0]
        in_range_sound2 = structs.BIG_l.unpack(data.read(4))[0]
        beam_damage_interval = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            electric_particles,
            weapon_particles,
            unnamed_0x00000008,
            particles,
            beam_fade_time,
            beam_radius,
            move_speed,
            unnamed_0x0000000d,
            min_speed,
            max_speed,
            speed_step,
            out_of_range_sound,
            in_range_sound1,
            in_range_sound2,
            beam_damage_interval,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x15")  # 21 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.electric_particles))
        data.write(structs.BIG_L.pack(self.weapon_particles))
        self.unnamed_0x00000008.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particles))
        data.write(structs.BIG_f.pack(self.beam_fade_time))
        data.write(structs.BIG_f.pack(self.beam_radius))
        data.write(structs.BIG_f.pack(self.move_speed))
        self.unnamed_0x0000000d.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.min_speed))
        data.write(structs.BIG_f.pack(self.max_speed))
        data.write(structs.BIG_f.pack(self.speed_step))
        data.write(structs.BIG_l.pack(self.out_of_range_sound))
        data.write(structs.BIG_l.pack(self.in_range_sound1))
        data.write(structs.BIG_l.pack(self.in_range_sound2))
        data.write(structs.BIG_f.pack(self.beam_damage_interval))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AtomicBetaJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            electric_particles=json_data["electric_particles"],
            weapon_particles=json_data["weapon_particles"],
            unnamed_0x00000008=DamageInfo.from_json(json_data["unnamed_0x00000008"]),
            particles=json_data["particles"],
            beam_fade_time=json_data["beam_fade_time"],
            beam_radius=json_data["beam_radius"],
            move_speed=json_data["move_speed"],
            unnamed_0x0000000d=DamageVulnerability.from_json(json_data["unnamed_0x0000000d"]),
            min_speed=json_data["min_speed"],
            max_speed=json_data["max_speed"],
            speed_step=json_data["speed_step"],
            out_of_range_sound=json_data["out_of_range_sound"],
            in_range_sound1=json_data["in_range_sound1"],
            in_range_sound2=json_data["in_range_sound2"],
            beam_damage_interval=json_data["beam_damage_interval"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "electric_particles": self.electric_particles,
            "weapon_particles": self.weapon_particles,
            "unnamed_0x00000008": self.unnamed_0x00000008.to_json(),
            "particles": self.particles,
            "beam_fade_time": self.beam_fade_time,
            "beam_radius": self.beam_radius,
            "move_speed": self.move_speed,
            "unnamed_0x0000000d": self.unnamed_0x0000000d.to_json(),
            "min_speed": self.min_speed,
            "max_speed": self.max_speed,
            "speed_step": self.speed_step,
            "out_of_range_sound": self.out_of_range_sound,
            "in_range_sound1": self.in_range_sound1,
            "in_range_sound2": self.in_range_sound2,
            "beam_damage_interval": self.beam_damage_interval,
        }

    def _dependencies_for_electric_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electric_particles)

    def _dependencies_for_weapon_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_particles)

    def _dependencies_for_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particles)

    def _dependencies_for_out_of_range_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.out_of_range_sound)

    def _dependencies_for_in_range_sound1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.in_range_sound1)

    def _dependencies_for_in_range_sound2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.in_range_sound2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_electric_particles, "electric_particles", "AssetId"),
            (self._dependencies_for_weapon_particles, "weapon_particles", "AssetId"),
            (self._dependencies_for_particles, "particles", "AssetId"),
            (self._dependencies_for_out_of_range_sound, "out_of_range_sound", "int"),
            (self._dependencies_for_in_range_sound1, "in_range_sound1", "int"),
            (self._dependencies_for_in_range_sound2, "in_range_sound2", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for AtomicBeta.{field_name} ({field_type}): {e}")
