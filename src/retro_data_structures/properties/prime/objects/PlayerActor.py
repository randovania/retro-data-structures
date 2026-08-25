# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.prime.archetypes.PlayerActorStruct import PlayerActorStruct
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PlayerActorJson(typing_extensions.TypedDict):
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
        model: int
        animation_parameters: json_util.JsonObject
        unnamed_0x0000000c: json_util.JsonObject
        loop: bool
        snow: bool
        solid: bool
        active: bool
        unnamed_0x00000011: json_util.JsonObject
        beam: int


class Beam(enum.IntEnum):
    Current = 0
    Power = 1
    Ice = 2
    Wave = 3
    Plasma = 4
    Phazon = 5

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class PlayerActor(BaseObjectType):
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
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="Model"),
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
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="Loop"),
        },
    )
    snow: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="Snow"),
        },
    )
    solid: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="Solid"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="Active"),
        },
    )
    unnamed_0x00000011: PlayerActorStruct = dataclasses.field(
        default_factory=PlayerActorStruct,
        metadata={
            "reflection": FieldReflection[PlayerActorStruct](
                PlayerActorStruct,
                id=0x00000011,
                original_name="17",
                from_json=PlayerActorStruct.from_json,
                to_json=PlayerActorStruct.to_json,
            ),
        },
    )
    beam: Beam = dataclasses.field(
        default=Beam.Current,
        metadata={
            "reflection": FieldReflection[Beam](
                Beam, id=0x00000012, original_name="Beam", from_json=Beam.from_json, to_json=Beam.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x4C

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
        model = structs.BIG_L.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x0000000c = ActorParameters.from_stream(data, game, property_size)
        loop = structs.BIG_bool_.unpack(data.read(1))[0]
        snow = structs.BIG_bool_.unpack(data.read(1))[0]
        solid = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed_0x00000011 = PlayerActorStruct.from_stream(data, game, property_size)
        beam = Beam.from_stream(data, game)
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
            model,
            animation_parameters,
            unnamed_0x0000000c,
            loop,
            snow,
            solid,
            active,
            unnamed_0x00000011,
            beam,
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
        data.write(structs.BIG_f.pack(self.mass))
        data.write(structs.BIG_f.pack(self.gravity))
        self.unnamed_0x00000008.to_stream(data, game)
        self.unnamed_0x00000009.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.model))
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x0000000c.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.loop))
        data.write(structs.BIG_bool_.pack(self.snow))
        data.write(structs.BIG_bool_.pack(self.solid))
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed_0x00000011.to_stream(data, game)
        self.beam.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerActorJson", data)
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
            model=json_data["model"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x0000000c=ActorParameters.from_json(json_data["unnamed_0x0000000c"]),
            loop=json_data["loop"],
            snow=json_data["snow"],
            solid=json_data["solid"],
            active=json_data["active"],
            unnamed_0x00000011=PlayerActorStruct.from_json(json_data["unnamed_0x00000011"]),
            beam=Beam.from_json(json_data["beam"]),
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
            "model": self.model,
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x0000000c": self.unnamed_0x0000000c.to_json(),
            "loop": self.loop,
            "snow": self.snow,
            "solid": self.solid,
            "active": self.active,
            "unnamed_0x00000011": self.unnamed_0x00000011.to_json(),
            "beam": self.beam.to_json(),
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x0000000c.dependencies_for, "unnamed_0x0000000c", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PlayerActor.{field_name} ({field_type}): {e}")
