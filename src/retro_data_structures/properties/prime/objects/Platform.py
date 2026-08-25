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

    class PlatformJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        model: int
        animation_parameters: json_util.JsonObject
        unnamed_0x00000008: json_util.JsonObject
        speed: float
        active: bool
        dcln: int
        unnamed_0x0000000c: json_util.JsonObject
        unnamed_0x0000000d: json_util.JsonObject
        detect_collision: bool
        x_ray_alpha: float
        rain_splashes: bool
        max_rain_splashes: int
        rain_gen_rate: int


@dataclasses.dataclass()
class Platform(BaseObjectType):
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
                Vector, id=0x00000004, original_name="Collision Box", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000005,
                original_name="Collision Offset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="Model"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000007,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unnamed_0x00000008: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000008,
                original_name="8",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Speed"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="Active"),
        },
    )
    dcln: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["DCLN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="DCLN"),
        },
    )
    unnamed_0x0000000c: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x0000000C,
                original_name="12",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
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
    detect_collision: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="DetectCollision"),
        },
    )
    x_ray_alpha: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="XRayAlpha"),
        },
    )
    rain_splashes: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="RainSplashes"),
        },
    )
    max_rain_splashes: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000011, original_name="MaxRainSplashes"),
        },
    )
    rain_gen_rate: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000012, original_name="RainGenRate"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x8

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
        model = structs.BIG_L.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x00000008 = ActorParameters.from_stream(data, game, property_size)
        speed = structs.BIG_f.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        dcln = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x0000000c = HealthInfo.from_stream(data, game, property_size)
        unnamed_0x0000000d = DamageVulnerability.from_stream(data, game, property_size)
        detect_collision = structs.BIG_bool_.unpack(data.read(1))[0]
        x_ray_alpha = structs.BIG_f.unpack(data.read(4))[0]
        rain_splashes = structs.BIG_bool_.unpack(data.read(1))[0]
        max_rain_splashes = structs.BIG_l.unpack(data.read(4))[0]
        rain_gen_rate = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            collision_box,
            collision_offset,
            model,
            animation_parameters,
            unnamed_0x00000008,
            speed,
            active,
            dcln,
            unnamed_0x0000000c,
            unnamed_0x0000000d,
            detect_collision,
            x_ray_alpha,
            rain_splashes,
            max_rain_splashes,
            rain_gen_rate,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x13")  # 19 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.collision_box.to_stream(data, game)
        self.collision_offset.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.model))
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x00000008.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.speed))
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_L.pack(self.dcln))
        self.unnamed_0x0000000c.to_stream(data, game)
        self.unnamed_0x0000000d.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.detect_collision))
        data.write(structs.BIG_f.pack(self.x_ray_alpha))
        data.write(structs.BIG_bool_.pack(self.rain_splashes))
        data.write(structs.BIG_l.pack(self.max_rain_splashes))
        data.write(structs.BIG_l.pack(self.rain_gen_rate))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlatformJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            model=json_data["model"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x00000008=ActorParameters.from_json(json_data["unnamed_0x00000008"]),
            speed=json_data["speed"],
            active=json_data["active"],
            dcln=json_data["dcln"],
            unnamed_0x0000000c=HealthInfo.from_json(json_data["unnamed_0x0000000c"]),
            unnamed_0x0000000d=DamageVulnerability.from_json(json_data["unnamed_0x0000000d"]),
            detect_collision=json_data["detect_collision"],
            x_ray_alpha=json_data["x_ray_alpha"],
            rain_splashes=json_data["rain_splashes"],
            max_rain_splashes=json_data["max_rain_splashes"],
            rain_gen_rate=json_data["rain_gen_rate"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "model": self.model,
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x00000008": self.unnamed_0x00000008.to_json(),
            "speed": self.speed,
            "active": self.active,
            "dcln": self.dcln,
            "unnamed_0x0000000c": self.unnamed_0x0000000c.to_json(),
            "unnamed_0x0000000d": self.unnamed_0x0000000d.to_json(),
            "detect_collision": self.detect_collision,
            "x_ray_alpha": self.x_ray_alpha,
            "rain_splashes": self.rain_splashes,
            "max_rain_splashes": self.max_rain_splashes,
            "rain_gen_rate": self.rain_gen_rate,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_dcln(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dcln)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x00000008.dependencies_for, "unnamed_0x00000008", "ActorParameters"),
            (self._dependencies_for_dcln, "dcln", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Platform.{field_name} ({field_type}): {e}")
