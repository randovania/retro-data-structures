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
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DoorJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        animation_parameters: json_util.JsonObject
        unnamed: json_util.JsonObject
        orbit_pos: json_util.JsonValue
        collision_size: json_util.JsonValue
        collision_offset: json_util.JsonValue
        active: bool
        open: bool
        projectiles_collide: bool
        animation_length: float
        is_morphball_door: bool


@dataclasses.dataclass()
class Door(BaseObjectType):
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
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000004,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unnamed: ActorParameters = dataclasses.field(
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
    orbit_pos: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000006, original_name="OrbitPos", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_size: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000007, original_name="CollisionSize", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000008,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="Active"),
        },
    )
    open: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="Open"),
        },
    )
    projectiles_collide: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="ProjectilesCollide"),
        },
    )
    animation_length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="AnimationLength"),
        },
    )
    is_morphball_door: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="IsMorphballDoor"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x3

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
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed = ActorParameters.from_stream(data, game, property_size)
        orbit_pos = Vector.from_stream(data, game, property_size)
        collision_size = Vector.from_stream(data, game, property_size)
        collision_offset = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        open = structs.BIG_bool_.unpack(data.read(1))[0]
        projectiles_collide = structs.BIG_bool_.unpack(data.read(1))[0]
        animation_length = structs.BIG_f.unpack(data.read(4))[0]
        is_morphball_door = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            animation_parameters,
            unnamed,
            orbit_pos,
            collision_size,
            collision_offset,
            active,
            open,
            projectiles_collide,
            animation_length,
            is_morphball_door,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0e")  # 14 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.animation_parameters.to_stream(data, game)
        self.unnamed.to_stream(data, game)
        self.orbit_pos.to_stream(data, game)
        self.collision_size.to_stream(data, game)
        self.collision_offset.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_bool_.pack(self.open))
        data.write(structs.BIG_bool_.pack(self.projectiles_collide))
        data.write(structs.BIG_f.pack(self.animation_length))
        data.write(structs.BIG_bool_.pack(self.is_morphball_door))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DoorJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed=ActorParameters.from_json(json_data["unnamed"]),
            orbit_pos=Vector.from_json(json_data["orbit_pos"]),
            collision_size=Vector.from_json(json_data["collision_size"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            active=json_data["active"],
            open=json_data["open"],
            projectiles_collide=json_data["projectiles_collide"],
            animation_length=json_data["animation_length"],
            is_morphball_door=json_data["is_morphball_door"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed": self.unnamed.to_json(),
            "orbit_pos": self.orbit_pos.to_json(),
            "collision_size": self.collision_size.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "active": self.active,
            "open": self.open,
            "projectiles_collide": self.projectiles_collide,
            "animation_length": self.animation_length,
            "is_morphball_door": self.is_morphball_door,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed.dependencies_for, "unnamed", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Door.{field_name} ({field_type}): {e}")
