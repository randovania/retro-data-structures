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
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SnakeWeedSwarmJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        scale: json_util.JsonValue
        active: bool
        animation_parameters: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        spacing: float
        height: float
        unknown_0x00000008: float
        weapon_damage_radius_: float
        max_player_distance: float
        lowered_time: float
        lowered_time_variation_: float
        max_z_offset: float
        speed: float
        speed_variation: float
        unknown_0x00000010: float
        scale_min: float
        scale_max: float
        distance_below_ground: float
        unnamed_0x00000014: json_util.JsonObject
        unused: float
        sfx1: int
        sfx2: int
        sfx3: int


@dataclasses.dataclass()
class SnakeWeedSwarm(BaseObjectType):
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
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Active"),
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
    spacing: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Spacing"),
        },
    )
    height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Height"),
        },
    )
    unknown_0x00000008: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown"),
        },
    )
    weapon_damage_radius_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="WeaponDamageRadius "),
        },
    )
    max_player_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="MaxPlayerDistance"),
        },
    )
    lowered_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="LoweredTime"),
        },
    )
    lowered_time_variation_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="LoweredTimeVariation "),
        },
    )
    max_z_offset: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="MaxZOffset"),
        },
    )
    speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Speed"),
        },
    )
    speed_variation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="SpeedVariation"),
        },
    )
    unknown_0x00000010: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="Unknown"),
        },
    )
    scale_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="ScaleMin"),
        },
    )
    scale_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="ScaleMax"),
        },
    )
    distance_below_ground: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="DistanceBelowGround"),
        },
    )
    unnamed_0x00000014: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000014,
                original_name="20",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unused: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="unused"),
        },
    )
    sfx1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000016, original_name="Sfx1"),
        },
    )
    sfx2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000017, original_name="Sfx2"),
        },
    )
    sfx3: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000018, original_name="Sfx3"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x6D

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unnamed_0x00000005 = ActorParameters.from_stream(data, game, property_size)
        spacing = structs.BIG_f.unpack(data.read(4))[0]
        height = structs.BIG_f.unpack(data.read(4))[0]
        unknown_0x00000008 = structs.BIG_f.unpack(data.read(4))[0]
        weapon_damage_radius_ = structs.BIG_f.unpack(data.read(4))[0]
        max_player_distance = structs.BIG_f.unpack(data.read(4))[0]
        lowered_time = structs.BIG_f.unpack(data.read(4))[0]
        lowered_time_variation_ = structs.BIG_f.unpack(data.read(4))[0]
        max_z_offset = structs.BIG_f.unpack(data.read(4))[0]
        speed = structs.BIG_f.unpack(data.read(4))[0]
        speed_variation = structs.BIG_f.unpack(data.read(4))[0]
        unknown_0x00000010 = structs.BIG_f.unpack(data.read(4))[0]
        scale_min = structs.BIG_f.unpack(data.read(4))[0]
        scale_max = structs.BIG_f.unpack(data.read(4))[0]
        distance_below_ground = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000014 = DamageInfo.from_stream(data, game, property_size)
        unused = structs.BIG_f.unpack(data.read(4))[0]
        sfx1 = structs.BIG_l.unpack(data.read(4))[0]
        sfx2 = structs.BIG_l.unpack(data.read(4))[0]
        sfx3 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            scale,
            active,
            animation_parameters,
            unnamed_0x00000005,
            spacing,
            height,
            unknown_0x00000008,
            weapon_damage_radius_,
            max_player_distance,
            lowered_time,
            lowered_time_variation_,
            max_z_offset,
            speed,
            speed_variation,
            unknown_0x00000010,
            scale_min,
            scale_max,
            distance_below_ground,
            unnamed_0x00000014,
            unused,
            sfx1,
            sfx2,
            sfx3,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x19")  # 25 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        self.animation_parameters.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.spacing))
        data.write(structs.BIG_f.pack(self.height))
        data.write(structs.BIG_f.pack(self.unknown_0x00000008))
        data.write(structs.BIG_f.pack(self.weapon_damage_radius_))
        data.write(structs.BIG_f.pack(self.max_player_distance))
        data.write(structs.BIG_f.pack(self.lowered_time))
        data.write(structs.BIG_f.pack(self.lowered_time_variation_))
        data.write(structs.BIG_f.pack(self.max_z_offset))
        data.write(structs.BIG_f.pack(self.speed))
        data.write(structs.BIG_f.pack(self.speed_variation))
        data.write(structs.BIG_f.pack(self.unknown_0x00000010))
        data.write(structs.BIG_f.pack(self.scale_min))
        data.write(structs.BIG_f.pack(self.scale_max))
        data.write(structs.BIG_f.pack(self.distance_below_ground))
        self.unnamed_0x00000014.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unused))
        data.write(structs.BIG_l.pack(self.sfx1))
        data.write(structs.BIG_l.pack(self.sfx2))
        data.write(structs.BIG_l.pack(self.sfx3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SnakeWeedSwarmJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            scale=Vector.from_json(json_data["scale"]),
            active=json_data["active"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            spacing=json_data["spacing"],
            height=json_data["height"],
            unknown_0x00000008=json_data["unknown_0x00000008"],
            weapon_damage_radius_=json_data["weapon_damage_radius_"],
            max_player_distance=json_data["max_player_distance"],
            lowered_time=json_data["lowered_time"],
            lowered_time_variation_=json_data["lowered_time_variation_"],
            max_z_offset=json_data["max_z_offset"],
            speed=json_data["speed"],
            speed_variation=json_data["speed_variation"],
            unknown_0x00000010=json_data["unknown_0x00000010"],
            scale_min=json_data["scale_min"],
            scale_max=json_data["scale_max"],
            distance_below_ground=json_data["distance_below_ground"],
            unnamed_0x00000014=DamageInfo.from_json(json_data["unnamed_0x00000014"]),
            unused=json_data["unused"],
            sfx1=json_data["sfx1"],
            sfx2=json_data["sfx2"],
            sfx3=json_data["sfx3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "scale": self.scale.to_json(),
            "active": self.active,
            "animation_parameters": self.animation_parameters.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "spacing": self.spacing,
            "height": self.height,
            "unknown_0x00000008": self.unknown_0x00000008,
            "weapon_damage_radius_": self.weapon_damage_radius_,
            "max_player_distance": self.max_player_distance,
            "lowered_time": self.lowered_time,
            "lowered_time_variation_": self.lowered_time_variation_,
            "max_z_offset": self.max_z_offset,
            "speed": self.speed,
            "speed_variation": self.speed_variation,
            "unknown_0x00000010": self.unknown_0x00000010,
            "scale_min": self.scale_min,
            "scale_max": self.scale_max,
            "distance_below_ground": self.distance_below_ground,
            "unnamed_0x00000014": self.unnamed_0x00000014.to_json(),
            "unused": self.unused,
            "sfx1": self.sfx1,
            "sfx2": self.sfx2,
            "sfx3": self.sfx3,
        }

    def _dependencies_for_sfx1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx1)

    def _dependencies_for_sfx2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx2)

    def _dependencies_for_sfx3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx3)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_sfx1, "sfx1", "int"),
            (self._dependencies_for_sfx2, "sfx2", "int"),
            (self._dependencies_for_sfx3, "sfx3", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SnakeWeedSwarm.{field_name} ({field_type}): {e}")
