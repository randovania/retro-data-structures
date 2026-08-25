# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DebrisJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        z_impulse: float
        velocity: json_util.JsonValue
        ends_color: json_util.JsonValue
        mass: float
        restitution: float
        duration: float
        scale_type: int
        random_ang_impulse: bool
        model: int
        unnamed: json_util.JsonObject
        particle_id: int
        particle_scale: json_util.JsonValue
        unknown: bool
        active: bool


@dataclasses.dataclass()
class Debris(BaseObjectType):
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
    z_impulse: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="ZImpulse"),
        },
    )
    velocity: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000005, original_name="Velocity", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    ends_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000006, original_name="EndsColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    mass: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Mass"),
        },
    )
    restitution: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Restitution"),
        },
    )
    duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Duration"),
        },
    )
    scale_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000A, original_name="ScaleType"),
        },
    )
    random_ang_impulse: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="RandomAngImpulse"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="Model"),
        },
    )
    unnamed: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x0000000D,
                original_name="13",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    particle_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="ParticleID"),
        },
    )
    particle_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x0000000F, original_name="ParticleScale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="Unknown"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000011, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x1B

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
        z_impulse = structs.BIG_f.unpack(data.read(4))[0]
        velocity = Vector.from_stream(data, game, property_size)
        ends_color = Color.from_stream(data, game, property_size)
        mass = structs.BIG_f.unpack(data.read(4))[0]
        restitution = structs.BIG_f.unpack(data.read(4))[0]
        duration = structs.BIG_f.unpack(data.read(4))[0]
        scale_type = structs.BIG_l.unpack(data.read(4))[0]
        random_ang_impulse = structs.BIG_bool_.unpack(data.read(1))[0]
        model = structs.BIG_L.unpack(data.read(4))[0]
        unnamed = ActorParameters.from_stream(data, game, property_size)
        particle_id = structs.BIG_L.unpack(data.read(4))[0]
        particle_scale = Vector.from_stream(data, game, property_size)
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            z_impulse,
            velocity,
            ends_color,
            mass,
            restitution,
            duration,
            scale_type,
            random_ang_impulse,
            model,
            unnamed,
            particle_id,
            particle_scale,
            unknown,
            active,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x12")  # 18 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.z_impulse))
        self.velocity.to_stream(data, game)
        self.ends_color.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.mass))
        data.write(structs.BIG_f.pack(self.restitution))
        data.write(structs.BIG_f.pack(self.duration))
        data.write(structs.BIG_l.pack(self.scale_type))
        data.write(structs.BIG_bool_.pack(self.random_ang_impulse))
        data.write(structs.BIG_L.pack(self.model))
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_id))
        self.particle_scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DebrisJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            z_impulse=json_data["z_impulse"],
            velocity=Vector.from_json(json_data["velocity"]),
            ends_color=Color.from_json(json_data["ends_color"]),
            mass=json_data["mass"],
            restitution=json_data["restitution"],
            duration=json_data["duration"],
            scale_type=json_data["scale_type"],
            random_ang_impulse=json_data["random_ang_impulse"],
            model=json_data["model"],
            unnamed=ActorParameters.from_json(json_data["unnamed"]),
            particle_id=json_data["particle_id"],
            particle_scale=Vector.from_json(json_data["particle_scale"]),
            unknown=json_data["unknown"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "z_impulse": self.z_impulse,
            "velocity": self.velocity.to_json(),
            "ends_color": self.ends_color.to_json(),
            "mass": self.mass,
            "restitution": self.restitution,
            "duration": self.duration,
            "scale_type": self.scale_type,
            "random_ang_impulse": self.random_ang_impulse,
            "model": self.model,
            "unnamed": self.unnamed.to_json(),
            "particle_id": self.particle_id,
            "particle_scale": self.particle_scale.to_json(),
            "unknown": self.unknown,
            "active": self.active,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_particle_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.unnamed.dependencies_for, "unnamed", "ActorParameters"),
            (self._dependencies_for_particle_id, "particle_id", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Debris.{field_name} ({field_type}): {e}")
