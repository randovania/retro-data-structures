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
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class AreaAttributesJson(typing_extensions.TypedDict):
        load: int
        show_skybox: bool
        fx_type_: int
        env_fx_densit: float
        thermal_heat: float
        x_ray_fog_distance: float
        world_lightning_level: float
        skybox: int
        phazon_type: int


class FXType(enum.IntEnum):
    _None = 0
    Snow = 1
    Rain = 2
    Bubbles = 3

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


class PhazonType(enum.IntEnum):
    _None = 0
    Blue = 1
    Orange = 2

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
class AreaAttributes(BaseObjectType):
    load: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000000, original_name="Load"),
        },
    )
    show_skybox: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="ShowSkybox"),
        },
    )
    fx_type_: FXType = dataclasses.field(
        default=FXType._None,
        metadata={
            "reflection": FieldReflection[FXType](
                FXType, id=0x00000002, original_name="FXType ", from_json=FXType.from_json, to_json=FXType.to_json
            ),
        },
    )
    env_fx_densit: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="EnvFxDensit"),
        },
    )
    thermal_heat: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="thermalHeat"),
        },
    )
    x_ray_fog_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="XRayFogDistance"),
        },
    )
    world_lightning_level: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="WorldLightningLevel"),
        },
    )
    skybox: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000007, original_name="Skybox"),
        },
    )
    phazon_type: PhazonType = dataclasses.field(
        default=PhazonType._None,
        metadata={
            "reflection": FieldReflection[PhazonType](
                PhazonType,
                id=0x00000008,
                original_name="PhazonType",
                from_json=PhazonType.from_json,
                to_json=PhazonType.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> int:
        return 0x4E

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        load = structs.BIG_l.unpack(data.read(4))[0]
        show_skybox = structs.BIG_bool_.unpack(data.read(1))[0]
        fx_type_ = FXType.from_stream(data, game)
        env_fx_densit = structs.BIG_f.unpack(data.read(4))[0]
        thermal_heat = structs.BIG_f.unpack(data.read(4))[0]
        x_ray_fog_distance = structs.BIG_f.unpack(data.read(4))[0]
        world_lightning_level = structs.BIG_f.unpack(data.read(4))[0]
        skybox = structs.BIG_L.unpack(data.read(4))[0]
        phazon_type = PhazonType.from_stream(data, game)
        return cls(
            load,
            show_skybox,
            fx_type_,
            env_fx_densit,
            thermal_heat,
            x_ray_fog_distance,
            world_lightning_level,
            skybox,
            phazon_type,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\t")  # 9 properties
        data.write(structs.BIG_l.pack(self.load))
        data.write(structs.BIG_bool_.pack(self.show_skybox))
        self.fx_type_.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.env_fx_densit))
        data.write(structs.BIG_f.pack(self.thermal_heat))
        data.write(structs.BIG_f.pack(self.x_ray_fog_distance))
        data.write(structs.BIG_f.pack(self.world_lightning_level))
        data.write(structs.BIG_L.pack(self.skybox))
        self.phazon_type.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AreaAttributesJson", data)
        return cls(
            load=json_data["load"],
            show_skybox=json_data["show_skybox"],
            fx_type_=FXType.from_json(json_data["fx_type_"]),
            env_fx_densit=json_data["env_fx_densit"],
            thermal_heat=json_data["thermal_heat"],
            x_ray_fog_distance=json_data["x_ray_fog_distance"],
            world_lightning_level=json_data["world_lightning_level"],
            skybox=json_data["skybox"],
            phazon_type=PhazonType.from_json(json_data["phazon_type"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "load": self.load,
            "show_skybox": self.show_skybox,
            "fx_type_": self.fx_type_.to_json(),
            "env_fx_densit": self.env_fx_densit,
            "thermal_heat": self.thermal_heat,
            "x_ray_fog_distance": self.x_ray_fog_distance,
            "world_lightning_level": self.world_lightning_level,
            "skybox": self.skybox,
            "phazon_type": self.phazon_type.to_json(),
        }

    def _dependencies_for_skybox(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.skybox)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_skybox(asset_manager)
