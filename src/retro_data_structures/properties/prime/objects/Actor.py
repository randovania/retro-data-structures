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
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ActorJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        gravity: float
        unnamed_0x00000008: json_util.JsonObject
        unnamed_0x00000009: json_util.JsonObject
        static_model: int
        animation_parameters: json_util.JsonObject
        unnamed_0x0000000c: json_util.JsonObject
        is_loop: bool
        immovable: bool
        is_solid: bool
        is_camera_through: bool
        active: bool
        render_texture_set: int
        x_ray_alpha: float
        thermal_visible_through_geometry: bool
        draws_shadow: bool
        scale_animation: bool
        material_flag54: bool


@dataclasses.dataclass()
class Actor(BaseObjectType):
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
    gravity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Gravity"),
        },
    )
    unnamed_0x00000008: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo, id=0x00000008, original_name="8", from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
            ),
        },
    )
    unnamed_0x00000009: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000009,
                original_name="9",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    static_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="StaticModel"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x0000000B,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unnamed_0x0000000c: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x0000000C,
                original_name="12",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    is_loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="IsLoop"),
        },
    )
    immovable: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="Immovable"),
        },
    )
    is_solid: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="IsSolid"),
        },
    )
    is_camera_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="IsCameraThrough"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000011, original_name="Active"),
        },
    )
    render_texture_set: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000012, original_name="RenderTextureSet"),
        },
    )
    x_ray_alpha: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="XRayAlpha"),
        },
    )
    thermal_visible_through_geometry: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000014, original_name="ThermalVisibleThroughGeometry"),
        },
    )
    draws_shadow: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000015, original_name="DrawsShadow"),
        },
    )
    scale_animation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000016, original_name="ScaleAnimation"),
        },
    )
    material_flag54: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000017, original_name="MaterialFlag54"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x0

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
        gravity = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000008 = HealthInfo.from_stream(data, game, property_size)
        unnamed_0x00000009 = DamageVulnerability.from_stream(data, game, property_size)
        static_model = structs.BIG_L.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x0000000c = ActorParameters.from_stream(data, game, property_size)
        is_loop = structs.BIG_bool_.unpack(data.read(1))[0]
        immovable = structs.BIG_bool_.unpack(data.read(1))[0]
        is_solid = structs.BIG_bool_.unpack(data.read(1))[0]
        is_camera_through = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        render_texture_set = structs.BIG_l.unpack(data.read(4))[0]
        x_ray_alpha = structs.BIG_f.unpack(data.read(4))[0]
        thermal_visible_through_geometry = structs.BIG_bool_.unpack(data.read(1))[0]
        draws_shadow = structs.BIG_bool_.unpack(data.read(1))[0]
        scale_animation = structs.BIG_bool_.unpack(data.read(1))[0]
        material_flag54 = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            collision_box,
            collision_offset,
            mass,
            gravity,
            unnamed_0x00000008,
            unnamed_0x00000009,
            static_model,
            animation_parameters,
            unnamed_0x0000000c,
            is_loop,
            immovable,
            is_solid,
            is_camera_through,
            active,
            render_texture_set,
            x_ray_alpha,
            thermal_visible_through_geometry,
            draws_shadow,
            scale_animation,
            material_flag54,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x18")  # 24 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.collision_box.to_stream(data, game)
        self.collision_offset.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.mass))
        data.write(structs.BIG_f.pack(self.gravity))
        self.unnamed_0x00000008.to_stream(data, game)
        self.unnamed_0x00000009.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.static_model))
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x0000000c.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.is_loop))
        data.write(structs.BIG_bool_.pack(self.immovable))
        data.write(structs.BIG_bool_.pack(self.is_solid))
        data.write(structs.BIG_bool_.pack(self.is_camera_through))
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_l.pack(self.render_texture_set))
        data.write(structs.BIG_f.pack(self.x_ray_alpha))
        data.write(structs.BIG_bool_.pack(self.thermal_visible_through_geometry))
        data.write(structs.BIG_bool_.pack(self.draws_shadow))
        data.write(structs.BIG_bool_.pack(self.scale_animation))
        data.write(structs.BIG_bool_.pack(self.material_flag54))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            mass=json_data["mass"],
            gravity=json_data["gravity"],
            unnamed_0x00000008=HealthInfo.from_json(json_data["unnamed_0x00000008"]),
            unnamed_0x00000009=DamageVulnerability.from_json(json_data["unnamed_0x00000009"]),
            static_model=json_data["static_model"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x0000000c=ActorParameters.from_json(json_data["unnamed_0x0000000c"]),
            is_loop=json_data["is_loop"],
            immovable=json_data["immovable"],
            is_solid=json_data["is_solid"],
            is_camera_through=json_data["is_camera_through"],
            active=json_data["active"],
            render_texture_set=json_data["render_texture_set"],
            x_ray_alpha=json_data["x_ray_alpha"],
            thermal_visible_through_geometry=json_data["thermal_visible_through_geometry"],
            draws_shadow=json_data["draws_shadow"],
            scale_animation=json_data["scale_animation"],
            material_flag54=json_data["material_flag54"],
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
            "gravity": self.gravity,
            "unnamed_0x00000008": self.unnamed_0x00000008.to_json(),
            "unnamed_0x00000009": self.unnamed_0x00000009.to_json(),
            "static_model": self.static_model,
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x0000000c": self.unnamed_0x0000000c.to_json(),
            "is_loop": self.is_loop,
            "immovable": self.immovable,
            "is_solid": self.is_solid,
            "is_camera_through": self.is_camera_through,
            "active": self.active,
            "render_texture_set": self.render_texture_set,
            "x_ray_alpha": self.x_ray_alpha,
            "thermal_visible_through_geometry": self.thermal_visible_through_geometry,
            "draws_shadow": self.draws_shadow,
            "scale_animation": self.scale_animation,
            "material_flag54": self.material_flag54,
        }

    def _dependencies_for_static_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.static_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_static_model, "static_model", "AssetId"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x0000000c.dependencies_for, "unnamed_0x0000000c", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Actor.{field_name} ({field_type}): {e}")
