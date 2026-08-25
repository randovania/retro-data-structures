# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.prime as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PickupJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        collision_scale: json_util.JsonValue
        scan_collision_offset: json_util.JsonValue
        unnamed_0x00000006: int
        capacity: int
        amount: int
        drop_rate: float
        life_time: float
        fade_length: float
        model: int
        animation_parameters: json_util.JsonObject
        unnamed_0x0000000e: json_util.JsonObject
        active: bool
        spawn_delay: float
        particle: int


@dataclasses.dataclass()
class Pickup(BaseObjectType):
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
    collision_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000004,
                original_name="Collision Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    scan_collision_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000005,
                original_name="Scan/Collision Offset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    unnamed_0x00000006: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0x00000006,
                original_name="6",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    capacity: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="Capacity"),
        },
    )
    amount: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="Amount"),
        },
    )
    drop_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Drop Rate"),
        },
    )
    life_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="Life Time"),
        },
    )
    fade_length: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="Fade Length"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="Model"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x0000000D,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unnamed_0x0000000e: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x0000000E,
                original_name="14",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="Active"),
        },
    )
    spawn_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="Spawn Delay"),
        },
    )
    particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="Particle"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x11

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
        collision_scale = Vector.from_stream(data, game, property_size)
        scan_collision_offset = Vector.from_stream(data, game, property_size)
        unnamed_0x00000006 = enums.PlayerItemEnum.from_stream(data, game)
        capacity = structs.BIG_l.unpack(data.read(4))[0]
        amount = structs.BIG_l.unpack(data.read(4))[0]
        drop_rate = structs.BIG_f.unpack(data.read(4))[0]
        life_time = structs.BIG_f.unpack(data.read(4))[0]
        fade_length = structs.BIG_f.unpack(data.read(4))[0]
        model = structs.BIG_L.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x0000000e = ActorParameters.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        spawn_delay = structs.BIG_f.unpack(data.read(4))[0]
        particle = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            collision_scale,
            scan_collision_offset,
            unnamed_0x00000006,
            capacity,
            amount,
            drop_rate,
            life_time,
            fade_length,
            model,
            animation_parameters,
            unnamed_0x0000000e,
            active,
            spawn_delay,
            particle,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x12")  # 18 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.collision_scale.to_stream(data, game)
        self.scan_collision_offset.to_stream(data, game)
        self.unnamed_0x00000006.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.capacity))
        data.write(structs.BIG_l.pack(self.amount))
        data.write(structs.BIG_f.pack(self.drop_rate))
        data.write(structs.BIG_f.pack(self.life_time))
        data.write(structs.BIG_f.pack(self.fade_length))
        data.write(structs.BIG_L.pack(self.model))
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x0000000e.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.spawn_delay))
        data.write(structs.BIG_L.pack(self.particle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PickupJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            collision_scale=Vector.from_json(json_data["collision_scale"]),
            scan_collision_offset=Vector.from_json(json_data["scan_collision_offset"]),
            unnamed_0x00000006=enums.PlayerItemEnum.from_json(json_data["unnamed_0x00000006"]),
            capacity=json_data["capacity"],
            amount=json_data["amount"],
            drop_rate=json_data["drop_rate"],
            life_time=json_data["life_time"],
            fade_length=json_data["fade_length"],
            model=json_data["model"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x0000000e=ActorParameters.from_json(json_data["unnamed_0x0000000e"]),
            active=json_data["active"],
            spawn_delay=json_data["spawn_delay"],
            particle=json_data["particle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "collision_scale": self.collision_scale.to_json(),
            "scan_collision_offset": self.scan_collision_offset.to_json(),
            "unnamed_0x00000006": self.unnamed_0x00000006.to_json(),
            "capacity": self.capacity,
            "amount": self.amount,
            "drop_rate": self.drop_rate,
            "life_time": self.life_time,
            "fade_length": self.fade_length,
            "model": self.model,
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x0000000e": self.unnamed_0x0000000e.to_json(),
            "active": self.active,
            "spawn_delay": self.spawn_delay,
            "particle": self.particle,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x0000000e.dependencies_for, "unnamed_0x0000000e", "ActorParameters"),
            (self._dependencies_for_particle, "particle", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Pickup.{field_name} ({field_type}): {e}")
