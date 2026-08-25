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
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FishCloudJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        active: bool
        model: int
        animation_parameters: json_util.JsonObject
        num_boids: float
        speed: float
        separation_radius: float
        cohesion_magnitude: float
        alignment_weight: float
        separation_magnitude: float
        weapon_repel_magnitude: float
        player_repel_magnitude: float
        containment_magnitude: float
        scatter_velocity: float
        max_scatter_angle: float
        weapon_repel_damping_speed: float
        player_repel_damping_speed: float
        containment_radius: float
        update_shift: int
        color: json_util.JsonValue
        killable: bool
        weapon_kill_radius: float
        part1_0x00000019: int
        part_count1: int
        part2: int
        part_count2: int
        part1_0x0000001d: int
        part_count3: int
        part4: int
        part_count4: int
        death_sfx: int
        repel_from_threats: bool
        hot_in_thermal: bool


@dataclasses.dataclass()
class FishCloud(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Active"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000005, original_name="Model"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000006,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    num_boids: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="NumBoids"),
        },
    )
    speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Speed"),
        },
    )
    separation_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="SeparationRadius"),
        },
    )
    cohesion_magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="CohesionMagnitude"),
        },
    )
    alignment_weight: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="AlignmentWeight"),
        },
    )
    separation_magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="SeparationMagnitude"),
        },
    )
    weapon_repel_magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="WeaponRepelMagnitude"),
        },
    )
    player_repel_magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="PlayerRepelMagnitude"),
        },
    )
    containment_magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="ContainmentMagnitude"),
        },
    )
    scatter_velocity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="ScatterVelocity"),
        },
    )
    max_scatter_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="MaxScatterAngle"),
        },
    )
    weapon_repel_damping_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="WeaponRepelDampingSpeed"),
        },
    )
    player_repel_damping_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="PlayerRepelDampingSpeed"),
        },
    )
    containment_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="ContainmentRadius"),
        },
    )
    update_shift: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000015, original_name="UpdateShift"),
        },
    )
    color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000016, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    killable: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000017, original_name="Killable"),
        },
    )
    weapon_kill_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="WeaponKillRadius"),
        },
    )
    part1_0x00000019: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000019, original_name="Part1"),
        },
    )
    part_count1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001A, original_name="PartCount1"),
        },
    )
    part2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001B, original_name="Part2"),
        },
    )
    part_count2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001C, original_name="PartCount2"),
        },
    )
    part1_0x0000001d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001D, original_name="Part1"),
        },
    )
    part_count3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001E, original_name="PartCount3"),
        },
    )
    part4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001F, original_name="Part4"),
        },
    )
    part_count4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000020, original_name="PartCount4"),
        },
    )
    death_sfx: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000021, original_name="DeathSfx"),
        },
    )
    repel_from_threats: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000022, original_name="RepelFromThreats"),
        },
    )
    hot_in_thermal: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000023, original_name="HotInThermal"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x4F

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
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        model = structs.BIG_L.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        num_boids = structs.BIG_f.unpack(data.read(4))[0]
        speed = structs.BIG_f.unpack(data.read(4))[0]
        separation_radius = structs.BIG_f.unpack(data.read(4))[0]
        cohesion_magnitude = structs.BIG_f.unpack(data.read(4))[0]
        alignment_weight = structs.BIG_f.unpack(data.read(4))[0]
        separation_magnitude = structs.BIG_f.unpack(data.read(4))[0]
        weapon_repel_magnitude = structs.BIG_f.unpack(data.read(4))[0]
        player_repel_magnitude = structs.BIG_f.unpack(data.read(4))[0]
        containment_magnitude = structs.BIG_f.unpack(data.read(4))[0]
        scatter_velocity = structs.BIG_f.unpack(data.read(4))[0]
        max_scatter_angle = structs.BIG_f.unpack(data.read(4))[0]
        weapon_repel_damping_speed = structs.BIG_f.unpack(data.read(4))[0]
        player_repel_damping_speed = structs.BIG_f.unpack(data.read(4))[0]
        containment_radius = structs.BIG_f.unpack(data.read(4))[0]
        update_shift = structs.BIG_l.unpack(data.read(4))[0]
        color = Color.from_stream(data, game, property_size)
        killable = structs.BIG_bool_.unpack(data.read(1))[0]
        weapon_kill_radius = structs.BIG_f.unpack(data.read(4))[0]
        part1_0x00000019 = structs.BIG_L.unpack(data.read(4))[0]
        part_count1 = structs.BIG_l.unpack(data.read(4))[0]
        part2 = structs.BIG_L.unpack(data.read(4))[0]
        part_count2 = structs.BIG_l.unpack(data.read(4))[0]
        part1_0x0000001d = structs.BIG_L.unpack(data.read(4))[0]
        part_count3 = structs.BIG_l.unpack(data.read(4))[0]
        part4 = structs.BIG_L.unpack(data.read(4))[0]
        part_count4 = structs.BIG_l.unpack(data.read(4))[0]
        death_sfx = structs.BIG_l.unpack(data.read(4))[0]
        repel_from_threats = structs.BIG_bool_.unpack(data.read(1))[0]
        hot_in_thermal = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            active,
            model,
            animation_parameters,
            num_boids,
            speed,
            separation_radius,
            cohesion_magnitude,
            alignment_weight,
            separation_magnitude,
            weapon_repel_magnitude,
            player_repel_magnitude,
            containment_magnitude,
            scatter_velocity,
            max_scatter_angle,
            weapon_repel_damping_speed,
            player_repel_damping_speed,
            containment_radius,
            update_shift,
            color,
            killable,
            weapon_kill_radius,
            part1_0x00000019,
            part_count1,
            part2,
            part_count2,
            part1_0x0000001d,
            part_count3,
            part4,
            part_count4,
            death_sfx,
            repel_from_threats,
            hot_in_thermal,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00$")  # 36 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_L.pack(self.model))
        self.animation_parameters.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.num_boids))
        data.write(structs.BIG_f.pack(self.speed))
        data.write(structs.BIG_f.pack(self.separation_radius))
        data.write(structs.BIG_f.pack(self.cohesion_magnitude))
        data.write(structs.BIG_f.pack(self.alignment_weight))
        data.write(structs.BIG_f.pack(self.separation_magnitude))
        data.write(structs.BIG_f.pack(self.weapon_repel_magnitude))
        data.write(structs.BIG_f.pack(self.player_repel_magnitude))
        data.write(structs.BIG_f.pack(self.containment_magnitude))
        data.write(structs.BIG_f.pack(self.scatter_velocity))
        data.write(structs.BIG_f.pack(self.max_scatter_angle))
        data.write(structs.BIG_f.pack(self.weapon_repel_damping_speed))
        data.write(structs.BIG_f.pack(self.player_repel_damping_speed))
        data.write(structs.BIG_f.pack(self.containment_radius))
        data.write(structs.BIG_l.pack(self.update_shift))
        self.color.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.killable))
        data.write(structs.BIG_f.pack(self.weapon_kill_radius))
        data.write(structs.BIG_L.pack(self.part1_0x00000019))
        data.write(structs.BIG_l.pack(self.part_count1))
        data.write(structs.BIG_L.pack(self.part2))
        data.write(structs.BIG_l.pack(self.part_count2))
        data.write(structs.BIG_L.pack(self.part1_0x0000001d))
        data.write(structs.BIG_l.pack(self.part_count3))
        data.write(structs.BIG_L.pack(self.part4))
        data.write(structs.BIG_l.pack(self.part_count4))
        data.write(structs.BIG_l.pack(self.death_sfx))
        data.write(structs.BIG_bool_.pack(self.repel_from_threats))
        data.write(structs.BIG_bool_.pack(self.hot_in_thermal))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FishCloudJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            active=json_data["active"],
            model=json_data["model"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            num_boids=json_data["num_boids"],
            speed=json_data["speed"],
            separation_radius=json_data["separation_radius"],
            cohesion_magnitude=json_data["cohesion_magnitude"],
            alignment_weight=json_data["alignment_weight"],
            separation_magnitude=json_data["separation_magnitude"],
            weapon_repel_magnitude=json_data["weapon_repel_magnitude"],
            player_repel_magnitude=json_data["player_repel_magnitude"],
            containment_magnitude=json_data["containment_magnitude"],
            scatter_velocity=json_data["scatter_velocity"],
            max_scatter_angle=json_data["max_scatter_angle"],
            weapon_repel_damping_speed=json_data["weapon_repel_damping_speed"],
            player_repel_damping_speed=json_data["player_repel_damping_speed"],
            containment_radius=json_data["containment_radius"],
            update_shift=json_data["update_shift"],
            color=Color.from_json(json_data["color"]),
            killable=json_data["killable"],
            weapon_kill_radius=json_data["weapon_kill_radius"],
            part1_0x00000019=json_data["part1_0x00000019"],
            part_count1=json_data["part_count1"],
            part2=json_data["part2"],
            part_count2=json_data["part_count2"],
            part1_0x0000001d=json_data["part1_0x0000001d"],
            part_count3=json_data["part_count3"],
            part4=json_data["part4"],
            part_count4=json_data["part_count4"],
            death_sfx=json_data["death_sfx"],
            repel_from_threats=json_data["repel_from_threats"],
            hot_in_thermal=json_data["hot_in_thermal"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "active": self.active,
            "model": self.model,
            "animation_parameters": self.animation_parameters.to_json(),
            "num_boids": self.num_boids,
            "speed": self.speed,
            "separation_radius": self.separation_radius,
            "cohesion_magnitude": self.cohesion_magnitude,
            "alignment_weight": self.alignment_weight,
            "separation_magnitude": self.separation_magnitude,
            "weapon_repel_magnitude": self.weapon_repel_magnitude,
            "player_repel_magnitude": self.player_repel_magnitude,
            "containment_magnitude": self.containment_magnitude,
            "scatter_velocity": self.scatter_velocity,
            "max_scatter_angle": self.max_scatter_angle,
            "weapon_repel_damping_speed": self.weapon_repel_damping_speed,
            "player_repel_damping_speed": self.player_repel_damping_speed,
            "containment_radius": self.containment_radius,
            "update_shift": self.update_shift,
            "color": self.color.to_json(),
            "killable": self.killable,
            "weapon_kill_radius": self.weapon_kill_radius,
            "part1_0x00000019": self.part1_0x00000019,
            "part_count1": self.part_count1,
            "part2": self.part2,
            "part_count2": self.part_count2,
            "part1_0x0000001d": self.part1_0x0000001d,
            "part_count3": self.part_count3,
            "part4": self.part4,
            "part_count4": self.part_count4,
            "death_sfx": self.death_sfx,
            "repel_from_threats": self.repel_from_threats,
            "hot_in_thermal": self.hot_in_thermal,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_part1_0x00000019(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part1_0x00000019)

    def _dependencies_for_part2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part2)

    def _dependencies_for_part1_0x0000001d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part1_0x0000001d)

    def _dependencies_for_part4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part4)

    def _dependencies_for_death_sfx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.death_sfx)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self._dependencies_for_part1_0x00000019, "part1_0x00000019", "AssetId"),
            (self._dependencies_for_part2, "part2", "AssetId"),
            (self._dependencies_for_part1_0x0000001d, "part1_0x0000001d", "AssetId"),
            (self._dependencies_for_part4, "part4", "AssetId"),
            (self._dependencies_for_death_sfx, "death_sfx", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for FishCloud.{field_name} ({field_type}): {e}")
