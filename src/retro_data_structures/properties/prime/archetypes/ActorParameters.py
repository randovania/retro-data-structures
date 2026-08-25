# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.LightParameters import LightParameters
from retro_data_structures.properties.prime.archetypes.ScannableParameters import ScannableParameters
from retro_data_structures.properties.prime.archetypes.VisorParameters import VisorParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ActorParametersJson(typing_extensions.TypedDict):
        unnamed_0x00000000: json_util.JsonObject
        unnamed_0x00000001: json_util.JsonObject
        x_ray_model: int
        x_ray_skin: int
        thermal_model: int
        thermal_skin: int
        use_global_render_time: bool
        fade_in_time: float
        fade_out_time: float
        unnamed_0x00000009: json_util.JsonObject
        thermal_hot: bool
        force_render_unsorted: bool
        no_sort_thermal: bool
        thermal_damage_mag: float


@dataclasses.dataclass()
class ActorParameters(BaseProperty):
    unnamed_0x00000000: LightParameters = dataclasses.field(
        default_factory=LightParameters,
        metadata={
            "reflection": FieldReflection[LightParameters](
                LightParameters,
                id=0x00000000,
                original_name="0",
                from_json=LightParameters.from_json,
                to_json=LightParameters.to_json,
            ),
        },
    )
    unnamed_0x00000001: ScannableParameters = dataclasses.field(
        default_factory=ScannableParameters,
        metadata={
            "reflection": FieldReflection[ScannableParameters](
                ScannableParameters,
                id=0x00000001,
                original_name="1",
                from_json=ScannableParameters.from_json,
                to_json=ScannableParameters.to_json,
            ),
        },
    )
    x_ray_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000002, original_name="XRayModel"),
        },
    )
    x_ray_skin: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000003, original_name="XRaySkin"),
        },
    )
    thermal_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000004, original_name="ThermalModel"),
        },
    )
    thermal_skin: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000005, original_name="ThermalSkin"),
        },
    )
    use_global_render_time: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="UseGlobalRenderTime"),
        },
    )
    fade_in_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="FadeInTime"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="FadeOutTime"),
        },
    )
    unnamed_0x00000009: VisorParameters = dataclasses.field(
        default_factory=VisorParameters,
        metadata={
            "reflection": FieldReflection[VisorParameters](
                VisorParameters,
                id=0x00000009,
                original_name="9",
                from_json=VisorParameters.from_json,
                to_json=VisorParameters.to_json,
            ),
        },
    )
    thermal_hot: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="ThermalHot"),
        },
    )
    force_render_unsorted: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="ForceRenderUnsorted"),
        },
    )
    no_sort_thermal: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000C, original_name="NoSortThermal"),
        },
    )
    thermal_damage_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="ThermalDamageMag"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unnamed_0x00000000 = LightParameters.from_stream(data, game, property_size)
        unnamed_0x00000001 = ScannableParameters.from_stream(data, game, property_size)
        x_ray_model = structs.BIG_L.unpack(data.read(4))[0]
        x_ray_skin = structs.BIG_L.unpack(data.read(4))[0]
        thermal_model = structs.BIG_L.unpack(data.read(4))[0]
        thermal_skin = structs.BIG_L.unpack(data.read(4))[0]
        use_global_render_time = structs.BIG_bool_.unpack(data.read(1))[0]
        fade_in_time = structs.BIG_f.unpack(data.read(4))[0]
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000009 = VisorParameters.from_stream(data, game, property_size)
        thermal_hot = structs.BIG_bool_.unpack(data.read(1))[0]
        force_render_unsorted = structs.BIG_bool_.unpack(data.read(1))[0]
        no_sort_thermal = structs.BIG_bool_.unpack(data.read(1))[0]
        thermal_damage_mag = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            unnamed_0x00000000,
            unnamed_0x00000001,
            x_ray_model,
            x_ray_skin,
            thermal_model,
            thermal_skin,
            use_global_render_time,
            fade_in_time,
            fade_out_time,
            unnamed_0x00000009,
            thermal_hot,
            force_render_unsorted,
            no_sort_thermal,
            thermal_damage_mag,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.unnamed_0x00000000.to_stream(data, game)
        self.unnamed_0x00000001.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.x_ray_model))
        data.write(structs.BIG_L.pack(self.x_ray_skin))
        data.write(structs.BIG_L.pack(self.thermal_model))
        data.write(structs.BIG_L.pack(self.thermal_skin))
        data.write(structs.BIG_bool_.pack(self.use_global_render_time))
        data.write(structs.BIG_f.pack(self.fade_in_time))
        data.write(structs.BIG_f.pack(self.fade_out_time))
        self.unnamed_0x00000009.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.thermal_hot))
        data.write(structs.BIG_bool_.pack(self.force_render_unsorted))
        data.write(structs.BIG_bool_.pack(self.no_sort_thermal))
        data.write(structs.BIG_f.pack(self.thermal_damage_mag))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorParametersJson", data)
        return cls(
            unnamed_0x00000000=LightParameters.from_json(json_data["unnamed_0x00000000"]),
            unnamed_0x00000001=ScannableParameters.from_json(json_data["unnamed_0x00000001"]),
            x_ray_model=json_data["x_ray_model"],
            x_ray_skin=json_data["x_ray_skin"],
            thermal_model=json_data["thermal_model"],
            thermal_skin=json_data["thermal_skin"],
            use_global_render_time=json_data["use_global_render_time"],
            fade_in_time=json_data["fade_in_time"],
            fade_out_time=json_data["fade_out_time"],
            unnamed_0x00000009=VisorParameters.from_json(json_data["unnamed_0x00000009"]),
            thermal_hot=json_data["thermal_hot"],
            force_render_unsorted=json_data["force_render_unsorted"],
            no_sort_thermal=json_data["no_sort_thermal"],
            thermal_damage_mag=json_data["thermal_damage_mag"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unnamed_0x00000000": self.unnamed_0x00000000.to_json(),
            "unnamed_0x00000001": self.unnamed_0x00000001.to_json(),
            "x_ray_model": self.x_ray_model,
            "x_ray_skin": self.x_ray_skin,
            "thermal_model": self.thermal_model,
            "thermal_skin": self.thermal_skin,
            "use_global_render_time": self.use_global_render_time,
            "fade_in_time": self.fade_in_time,
            "fade_out_time": self.fade_out_time,
            "unnamed_0x00000009": self.unnamed_0x00000009.to_json(),
            "thermal_hot": self.thermal_hot,
            "force_render_unsorted": self.force_render_unsorted,
            "no_sort_thermal": self.no_sort_thermal,
            "thermal_damage_mag": self.thermal_damage_mag,
        }

    def _dependencies_for_x_ray_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.x_ray_model)

    def _dependencies_for_x_ray_skin(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.x_ray_skin)

    def _dependencies_for_thermal_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.thermal_model)

    def _dependencies_for_thermal_skin(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.thermal_skin)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000001.dependencies_for, "unnamed_0x00000001", "ScannableParameters"),
            (self._dependencies_for_x_ray_model, "x_ray_model", "AssetId"),
            (self._dependencies_for_x_ray_skin, "x_ray_skin", "AssetId"),
            (self._dependencies_for_thermal_model, "thermal_model", "AssetId"),
            (self._dependencies_for_thermal_skin, "thermal_skin", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ActorParameters.{field_name} ({field_type}): {e}")
