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
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class AmbientAIJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        unnamed_0x00000007: json_util.JsonObject
        unnamed_0x00000008: json_util.JsonObject
        animation_parameters: json_util.JsonObject
        unnamed_0x0000000a: json_util.JsonObject
        alert_range: float
        impact_range: float
        alert_animation_id: int
        impact_animation_id: int
        active: bool


@dataclasses.dataclass()
class AmbientAI(BaseObjectType):
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
    collision_box: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="CollisionBox", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000005,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    mass: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Mass"),
        },
    )
    unnamed_0x00000007: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo, id=0x00000007, original_name="7", from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
            ),
        },
    )
    unnamed_0x00000008: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000008,
                original_name="8",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000009,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unnamed_0x0000000a: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x0000000A,
                original_name="10",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    alert_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="AlertRange"),
        },
    )
    impact_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="ImpactRange"),
        },
    )
    alert_animation_id: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="AlertAnimationID"),
        },
    )
    impact_animation_id: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000E, original_name="ImpactAnimationID"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x75

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
        collision_box = Vector.from_stream(data, game, property_size)
        collision_offset = Vector.from_stream(data, game, property_size)
        mass = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000007 = HealthInfo.from_stream(data, game, property_size)
        unnamed_0x00000008 = DamageVulnerability.from_stream(data, game, property_size)
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x0000000a = ActorParameters.from_stream(data, game, property_size)
        alert_range = structs.BIG_f.unpack(data.read(4))[0]
        impact_range = structs.BIG_f.unpack(data.read(4))[0]
        alert_animation_id = structs.BIG_l.unpack(data.read(4))[0]
        impact_animation_id = structs.BIG_l.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            collision_box,
            collision_offset,
            mass,
            unnamed_0x00000007,
            unnamed_0x00000008,
            animation_parameters,
            unnamed_0x0000000a,
            alert_range,
            impact_range,
            alert_animation_id,
            impact_animation_id,
            active,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x10")  # 16 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.collision_box.to_stream(data, game)
        self.collision_offset.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.mass))
        self.unnamed_0x00000007.to_stream(data, game)
        self.unnamed_0x00000008.to_stream(data, game)
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x0000000a.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.alert_range))
        data.write(structs.BIG_f.pack(self.impact_range))
        data.write(structs.BIG_l.pack(self.alert_animation_id))
        data.write(structs.BIG_l.pack(self.impact_animation_id))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AmbientAIJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            mass=json_data["mass"],
            unnamed_0x00000007=HealthInfo.from_json(json_data["unnamed_0x00000007"]),
            unnamed_0x00000008=DamageVulnerability.from_json(json_data["unnamed_0x00000008"]),
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x0000000a=ActorParameters.from_json(json_data["unnamed_0x0000000a"]),
            alert_range=json_data["alert_range"],
            impact_range=json_data["impact_range"],
            alert_animation_id=json_data["alert_animation_id"],
            impact_animation_id=json_data["impact_animation_id"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "mass": self.mass,
            "unnamed_0x00000007": self.unnamed_0x00000007.to_json(),
            "unnamed_0x00000008": self.unnamed_0x00000008.to_json(),
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x0000000a": self.unnamed_0x0000000a.to_json(),
            "alert_range": self.alert_range,
            "impact_range": self.impact_range,
            "alert_animation_id": self.alert_animation_id,
            "impact_animation_id": self.impact_animation_id,
            "active": self.active,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x0000000a.dependencies_for, "unnamed_0x0000000a", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for AmbientAI.{field_name} ({field_type}): {e}")
