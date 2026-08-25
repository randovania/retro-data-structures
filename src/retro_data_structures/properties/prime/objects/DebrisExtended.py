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

    class DebrisExtendedJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        lin_cone_angle: float
        lin_min_mag: float
        lin_max_mag: float
        ang_min_mag: float
        ang_max_mag: float
        min_duration: float
        max_duration: float
        color_in_t: float
        color_out_t_: float
        color: json_util.JsonValue
        ends_color: json_util.JsonValue
        scale_out_t: float
        end_scale_: json_util.JsonValue
        restitution: float
        downward_speed_: float
        local_offset_: json_util.JsonValue
        model: int
        unnamed: json_util.JsonObject
        particle1: int
        particle1_scale: json_util.JsonValue
        particle1_global_translation_: bool
        defer_delete_till_particle1_done_: bool
        particle1_orientation: int
        particle2: int
        particle2_scale: json_util.JsonValue
        particle2_global_translation: bool
        defer_delete_till_particle2_done: bool
        particle2_orientation: int
        particle3: int
        particle3_scale: json_util.JsonValue
        particle3_orientation: int
        solid: bool
        die_on_projectile: bool
        no_bounce: bool
        active: bool


@dataclasses.dataclass()
class DebrisExtended(BaseObjectType):
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
    lin_cone_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="LinConeAngle"),
        },
    )
    lin_min_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="LinMinMag"),
        },
    )
    lin_max_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="LinMaxMag"),
        },
    )
    ang_min_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="AngMinMag"),
        },
    )
    ang_max_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="AngMaxMag"),
        },
    )
    min_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="MinDuration"),
        },
    )
    max_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="MaxDuration"),
        },
    )
    color_in_t: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="ColorInT"),
        },
    )
    color_out_t_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="ColorOutT "),
        },
    )
    color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0000000D, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    ends_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0000000E, original_name="EndsColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    scale_out_t: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="ScaleOutT"),
        },
    )
    end_scale_: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000010, original_name="EndScale ", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    restitution: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="Restitution"),
        },
    )
    downward_speed_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="DownwardSpeed "),
        },
    )
    local_offset_: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000013, original_name="LocalOffset ", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000014, original_name="Model"),
        },
    )
    unnamed: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000015,
                original_name="21",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    particle1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000016, original_name="Particle1"),
        },
    )
    particle1_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000017,
                original_name="Particle1Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle1_global_translation_: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000018, original_name="Particle1GlobalTranslation "),
        },
    )
    defer_delete_till_particle1_done_: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000019, original_name="DeferDeleteTillParticle1Done "),
        },
    )
    particle1_orientation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001A, original_name="Particle1Orientation"),
        },
    )
    particle2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000001B, original_name="Particle2"),
        },
    )
    particle2_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x0000001C,
                original_name="Particle2Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle2_global_translation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000001D, original_name="Particle2GlobalTranslation"),
        },
    )
    defer_delete_till_particle2_done: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000001E, original_name="DeferDeleteTillParticle2Done"),
        },
    )
    particle2_orientation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="Particle2Orientation"),
        },
    )
    particle3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000020, original_name="Particle3"),
        },
    )
    particle3_scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000021,
                original_name="Particle3Scale",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    particle3_orientation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000022, original_name="Particle3Orientation"),
        },
    )
    solid: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000023, original_name="Solid"),
        },
    )
    die_on_projectile: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000024, original_name="DieOnProjectile"),
        },
    )
    no_bounce: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000025, original_name="NoBounce"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000026, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x45

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
        lin_cone_angle = structs.BIG_f.unpack(data.read(4))[0]
        lin_min_mag = structs.BIG_f.unpack(data.read(4))[0]
        lin_max_mag = structs.BIG_f.unpack(data.read(4))[0]
        ang_min_mag = structs.BIG_f.unpack(data.read(4))[0]
        ang_max_mag = structs.BIG_f.unpack(data.read(4))[0]
        min_duration = structs.BIG_f.unpack(data.read(4))[0]
        max_duration = structs.BIG_f.unpack(data.read(4))[0]
        color_in_t = structs.BIG_f.unpack(data.read(4))[0]
        color_out_t_ = structs.BIG_f.unpack(data.read(4))[0]
        color = Color.from_stream(data, game, property_size)
        ends_color = Color.from_stream(data, game, property_size)
        scale_out_t = structs.BIG_f.unpack(data.read(4))[0]
        end_scale_ = Vector.from_stream(data, game, property_size)
        restitution = structs.BIG_f.unpack(data.read(4))[0]
        downward_speed_ = structs.BIG_f.unpack(data.read(4))[0]
        local_offset_ = Vector.from_stream(data, game, property_size)
        model = structs.BIG_L.unpack(data.read(4))[0]
        unnamed = ActorParameters.from_stream(data, game, property_size)
        particle1 = structs.BIG_L.unpack(data.read(4))[0]
        particle1_scale = Vector.from_stream(data, game, property_size)
        particle1_global_translation_ = structs.BIG_bool_.unpack(data.read(1))[0]
        defer_delete_till_particle1_done_ = structs.BIG_bool_.unpack(data.read(1))[0]
        particle1_orientation = structs.BIG_l.unpack(data.read(4))[0]
        particle2 = structs.BIG_L.unpack(data.read(4))[0]
        particle2_scale = Vector.from_stream(data, game, property_size)
        particle2_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]
        defer_delete_till_particle2_done = structs.BIG_bool_.unpack(data.read(1))[0]
        particle2_orientation = structs.BIG_l.unpack(data.read(4))[0]
        particle3 = structs.BIG_L.unpack(data.read(4))[0]
        particle3_scale = Vector.from_stream(data, game, property_size)
        particle3_orientation = structs.BIG_l.unpack(data.read(4))[0]
        solid = structs.BIG_bool_.unpack(data.read(1))[0]
        die_on_projectile = structs.BIG_bool_.unpack(data.read(1))[0]
        no_bounce = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            lin_cone_angle,
            lin_min_mag,
            lin_max_mag,
            ang_min_mag,
            ang_max_mag,
            min_duration,
            max_duration,
            color_in_t,
            color_out_t_,
            color,
            ends_color,
            scale_out_t,
            end_scale_,
            restitution,
            downward_speed_,
            local_offset_,
            model,
            unnamed,
            particle1,
            particle1_scale,
            particle1_global_translation_,
            defer_delete_till_particle1_done_,
            particle1_orientation,
            particle2,
            particle2_scale,
            particle2_global_translation,
            defer_delete_till_particle2_done,
            particle2_orientation,
            particle3,
            particle3_scale,
            particle3_orientation,
            solid,
            die_on_projectile,
            no_bounce,
            active,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00'")  # 39 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.lin_cone_angle))
        data.write(structs.BIG_f.pack(self.lin_min_mag))
        data.write(structs.BIG_f.pack(self.lin_max_mag))
        data.write(structs.BIG_f.pack(self.ang_min_mag))
        data.write(structs.BIG_f.pack(self.ang_max_mag))
        data.write(structs.BIG_f.pack(self.min_duration))
        data.write(structs.BIG_f.pack(self.max_duration))
        data.write(structs.BIG_f.pack(self.color_in_t))
        data.write(structs.BIG_f.pack(self.color_out_t_))
        self.color.to_stream(data, game)
        self.ends_color.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.scale_out_t))
        self.end_scale_.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.restitution))
        data.write(structs.BIG_f.pack(self.downward_speed_))
        self.local_offset_.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.model))
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle1))
        self.particle1_scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.particle1_global_translation_))
        data.write(structs.BIG_bool_.pack(self.defer_delete_till_particle1_done_))
        data.write(structs.BIG_l.pack(self.particle1_orientation))
        data.write(structs.BIG_L.pack(self.particle2))
        self.particle2_scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.particle2_global_translation))
        data.write(structs.BIG_bool_.pack(self.defer_delete_till_particle2_done))
        data.write(structs.BIG_l.pack(self.particle2_orientation))
        data.write(structs.BIG_L.pack(self.particle3))
        self.particle3_scale.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.particle3_orientation))
        data.write(structs.BIG_bool_.pack(self.solid))
        data.write(structs.BIG_bool_.pack(self.die_on_projectile))
        data.write(structs.BIG_bool_.pack(self.no_bounce))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DebrisExtendedJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            lin_cone_angle=json_data["lin_cone_angle"],
            lin_min_mag=json_data["lin_min_mag"],
            lin_max_mag=json_data["lin_max_mag"],
            ang_min_mag=json_data["ang_min_mag"],
            ang_max_mag=json_data["ang_max_mag"],
            min_duration=json_data["min_duration"],
            max_duration=json_data["max_duration"],
            color_in_t=json_data["color_in_t"],
            color_out_t_=json_data["color_out_t_"],
            color=Color.from_json(json_data["color"]),
            ends_color=Color.from_json(json_data["ends_color"]),
            scale_out_t=json_data["scale_out_t"],
            end_scale_=Vector.from_json(json_data["end_scale_"]),
            restitution=json_data["restitution"],
            downward_speed_=json_data["downward_speed_"],
            local_offset_=Vector.from_json(json_data["local_offset_"]),
            model=json_data["model"],
            unnamed=ActorParameters.from_json(json_data["unnamed"]),
            particle1=json_data["particle1"],
            particle1_scale=Vector.from_json(json_data["particle1_scale"]),
            particle1_global_translation_=json_data["particle1_global_translation_"],
            defer_delete_till_particle1_done_=json_data["defer_delete_till_particle1_done_"],
            particle1_orientation=json_data["particle1_orientation"],
            particle2=json_data["particle2"],
            particle2_scale=Vector.from_json(json_data["particle2_scale"]),
            particle2_global_translation=json_data["particle2_global_translation"],
            defer_delete_till_particle2_done=json_data["defer_delete_till_particle2_done"],
            particle2_orientation=json_data["particle2_orientation"],
            particle3=json_data["particle3"],
            particle3_scale=Vector.from_json(json_data["particle3_scale"]),
            particle3_orientation=json_data["particle3_orientation"],
            solid=json_data["solid"],
            die_on_projectile=json_data["die_on_projectile"],
            no_bounce=json_data["no_bounce"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "lin_cone_angle": self.lin_cone_angle,
            "lin_min_mag": self.lin_min_mag,
            "lin_max_mag": self.lin_max_mag,
            "ang_min_mag": self.ang_min_mag,
            "ang_max_mag": self.ang_max_mag,
            "min_duration": self.min_duration,
            "max_duration": self.max_duration,
            "color_in_t": self.color_in_t,
            "color_out_t_": self.color_out_t_,
            "color": self.color.to_json(),
            "ends_color": self.ends_color.to_json(),
            "scale_out_t": self.scale_out_t,
            "end_scale_": self.end_scale_.to_json(),
            "restitution": self.restitution,
            "downward_speed_": self.downward_speed_,
            "local_offset_": self.local_offset_.to_json(),
            "model": self.model,
            "unnamed": self.unnamed.to_json(),
            "particle1": self.particle1,
            "particle1_scale": self.particle1_scale.to_json(),
            "particle1_global_translation_": self.particle1_global_translation_,
            "defer_delete_till_particle1_done_": self.defer_delete_till_particle1_done_,
            "particle1_orientation": self.particle1_orientation,
            "particle2": self.particle2,
            "particle2_scale": self.particle2_scale.to_json(),
            "particle2_global_translation": self.particle2_global_translation,
            "defer_delete_till_particle2_done": self.defer_delete_till_particle2_done,
            "particle2_orientation": self.particle2_orientation,
            "particle3": self.particle3,
            "particle3_scale": self.particle3_scale.to_json(),
            "particle3_orientation": self.particle3_orientation,
            "solid": self.solid,
            "die_on_projectile": self.die_on_projectile,
            "no_bounce": self.no_bounce,
            "active": self.active,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_particle1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle1)

    def _dependencies_for_particle2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle2)

    def _dependencies_for_particle3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle3)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.unnamed.dependencies_for, "unnamed", "ActorParameters"),
            (self._dependencies_for_particle1, "particle1", "AssetId"),
            (self._dependencies_for_particle2, "particle2", "AssetId"),
            (self._dependencies_for_particle3, "particle3", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for DebrisExtended.{field_name} ({field_type}): {e}")
