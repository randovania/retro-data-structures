# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.LightParameters import LightParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class EffectJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        particle: int
        elsc: int
        hot_in_thermal: bool
        no_timer_unless_area_occluded: bool
        rebuild_systems_on_activate: bool
        active: bool
        use_rate_inverse_cam_dist: bool
        rate_inverse_cam_dist: float
        rate_inverse_cam_dist_rate: float
        duration: float
        duration_reset_while_visible: float
        use_rate_cam_dist_range: bool
        rate_cam_dist_range_min: float
        rate_cam_dist_range_max: float
        rate_cam_dist_range_far_rate_: float
        combat_visor_visible: bool
        thermal_visor_visible: bool
        xray_visor_visible: bool
        die_when_systems_done: bool
        unnamed: json_util.JsonObject


@dataclasses.dataclass()
class Effect(BaseObjectType):
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
    particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000004, original_name="Particle"),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000005, original_name="ELSC"),
        },
    )
    hot_in_thermal: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="HotInThermal"),
        },
    )
    no_timer_unless_area_occluded: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="NoTimerUnlessAreaOccluded"),
        },
    )
    rebuild_systems_on_activate: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="RebuildSystemsOnActivate"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="Active"),
        },
    )
    use_rate_inverse_cam_dist: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="UseRateInverseCamDist"),
        },
    )
    rate_inverse_cam_dist: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="RateInverseCamDist"),
        },
    )
    rate_inverse_cam_dist_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="RateInverseCamDistRate"),
        },
    )
    duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Duration"),
        },
    )
    duration_reset_while_visible: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="DurationResetWhileVisible"),
        },
    )
    use_rate_cam_dist_range: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="UseRateCamDistRange"),
        },
    )
    rate_cam_dist_range_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="RateCamDistRangeMin"),
        },
    )
    rate_cam_dist_range_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="RateCamDistRangeMax"),
        },
    )
    rate_cam_dist_range_far_rate_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="RateCamDistRangeFarRate "),
        },
    )
    combat_visor_visible: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000013, original_name="CombatVisorVisible"),
        },
    )
    thermal_visor_visible: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000014, original_name="ThermalVisorVisible"),
        },
    )
    xray_visor_visible: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000015, original_name="XrayVisorVisible"),
        },
    )
    die_when_systems_done: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000016, original_name="DieWhenSystemsDone"),
        },
    )
    unnamed: LightParameters = dataclasses.field(
        default_factory=LightParameters,
        metadata={
            "reflection": FieldReflection[LightParameters](
                LightParameters,
                id=0x00000017,
                original_name="23",
                from_json=LightParameters.from_json,
                to_json=LightParameters.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x7

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
        particle = structs.BIG_L.unpack(data.read(4))[0]
        elsc = structs.BIG_L.unpack(data.read(4))[0]
        hot_in_thermal = structs.BIG_bool_.unpack(data.read(1))[0]
        no_timer_unless_area_occluded = structs.BIG_bool_.unpack(data.read(1))[0]
        rebuild_systems_on_activate = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        use_rate_inverse_cam_dist = structs.BIG_bool_.unpack(data.read(1))[0]
        rate_inverse_cam_dist = structs.BIG_f.unpack(data.read(4))[0]
        rate_inverse_cam_dist_rate = structs.BIG_f.unpack(data.read(4))[0]
        duration = structs.BIG_f.unpack(data.read(4))[0]
        duration_reset_while_visible = structs.BIG_f.unpack(data.read(4))[0]
        use_rate_cam_dist_range = structs.BIG_bool_.unpack(data.read(1))[0]
        rate_cam_dist_range_min = structs.BIG_f.unpack(data.read(4))[0]
        rate_cam_dist_range_max = structs.BIG_f.unpack(data.read(4))[0]
        rate_cam_dist_range_far_rate_ = structs.BIG_f.unpack(data.read(4))[0]
        combat_visor_visible = structs.BIG_bool_.unpack(data.read(1))[0]
        thermal_visor_visible = structs.BIG_bool_.unpack(data.read(1))[0]
        xray_visor_visible = structs.BIG_bool_.unpack(data.read(1))[0]
        die_when_systems_done = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed = LightParameters.from_stream(data, game, property_size)
        return cls(
            name,
            position,
            rotation,
            scale,
            particle,
            elsc,
            hot_in_thermal,
            no_timer_unless_area_occluded,
            rebuild_systems_on_activate,
            active,
            use_rate_inverse_cam_dist,
            rate_inverse_cam_dist,
            rate_inverse_cam_dist_rate,
            duration,
            duration_reset_while_visible,
            use_rate_cam_dist_range,
            rate_cam_dist_range_min,
            rate_cam_dist_range_max,
            rate_cam_dist_range_far_rate_,
            combat_visor_visible,
            thermal_visor_visible,
            xray_visor_visible,
            die_when_systems_done,
            unnamed,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x18")  # 24 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle))
        data.write(structs.BIG_L.pack(self.elsc))
        data.write(structs.BIG_bool_.pack(self.hot_in_thermal))
        data.write(structs.BIG_bool_.pack(self.no_timer_unless_area_occluded))
        data.write(structs.BIG_bool_.pack(self.rebuild_systems_on_activate))
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_bool_.pack(self.use_rate_inverse_cam_dist))
        data.write(structs.BIG_f.pack(self.rate_inverse_cam_dist))
        data.write(structs.BIG_f.pack(self.rate_inverse_cam_dist_rate))
        data.write(structs.BIG_f.pack(self.duration))
        data.write(structs.BIG_f.pack(self.duration_reset_while_visible))
        data.write(structs.BIG_bool_.pack(self.use_rate_cam_dist_range))
        data.write(structs.BIG_f.pack(self.rate_cam_dist_range_min))
        data.write(structs.BIG_f.pack(self.rate_cam_dist_range_max))
        data.write(structs.BIG_f.pack(self.rate_cam_dist_range_far_rate_))
        data.write(structs.BIG_bool_.pack(self.combat_visor_visible))
        data.write(structs.BIG_bool_.pack(self.thermal_visor_visible))
        data.write(structs.BIG_bool_.pack(self.xray_visor_visible))
        data.write(structs.BIG_bool_.pack(self.die_when_systems_done))
        self.unnamed.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EffectJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            particle=json_data["particle"],
            elsc=json_data["elsc"],
            hot_in_thermal=json_data["hot_in_thermal"],
            no_timer_unless_area_occluded=json_data["no_timer_unless_area_occluded"],
            rebuild_systems_on_activate=json_data["rebuild_systems_on_activate"],
            active=json_data["active"],
            use_rate_inverse_cam_dist=json_data["use_rate_inverse_cam_dist"],
            rate_inverse_cam_dist=json_data["rate_inverse_cam_dist"],
            rate_inverse_cam_dist_rate=json_data["rate_inverse_cam_dist_rate"],
            duration=json_data["duration"],
            duration_reset_while_visible=json_data["duration_reset_while_visible"],
            use_rate_cam_dist_range=json_data["use_rate_cam_dist_range"],
            rate_cam_dist_range_min=json_data["rate_cam_dist_range_min"],
            rate_cam_dist_range_max=json_data["rate_cam_dist_range_max"],
            rate_cam_dist_range_far_rate_=json_data["rate_cam_dist_range_far_rate_"],
            combat_visor_visible=json_data["combat_visor_visible"],
            thermal_visor_visible=json_data["thermal_visor_visible"],
            xray_visor_visible=json_data["xray_visor_visible"],
            die_when_systems_done=json_data["die_when_systems_done"],
            unnamed=LightParameters.from_json(json_data["unnamed"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "particle": self.particle,
            "elsc": self.elsc,
            "hot_in_thermal": self.hot_in_thermal,
            "no_timer_unless_area_occluded": self.no_timer_unless_area_occluded,
            "rebuild_systems_on_activate": self.rebuild_systems_on_activate,
            "active": self.active,
            "use_rate_inverse_cam_dist": self.use_rate_inverse_cam_dist,
            "rate_inverse_cam_dist": self.rate_inverse_cam_dist,
            "rate_inverse_cam_dist_rate": self.rate_inverse_cam_dist_rate,
            "duration": self.duration,
            "duration_reset_while_visible": self.duration_reset_while_visible,
            "use_rate_cam_dist_range": self.use_rate_cam_dist_range,
            "rate_cam_dist_range_min": self.rate_cam_dist_range_min,
            "rate_cam_dist_range_max": self.rate_cam_dist_range_max,
            "rate_cam_dist_range_far_rate_": self.rate_cam_dist_range_far_rate_,
            "combat_visor_visible": self.combat_visor_visible,
            "thermal_visor_visible": self.thermal_visor_visible,
            "xray_visor_visible": self.xray_visor_visible,
            "die_when_systems_done": self.die_when_systems_done,
            "unnamed": self.unnamed.to_json(),
        }

    def _dependencies_for_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle)

    def _dependencies_for_elsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.elsc)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_particle, "particle", "AssetId"),
            (self._dependencies_for_elsc, "elsc", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Effect.{field_name} ({field_type}): {e}")
