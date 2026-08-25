# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.prime as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ScanImageJson(typing_extensions.TypedDict):
        texture: int
        appear_percentage: float
        unnamed: int
        animation_cell_width: int
        animation_cell_height: int
        animation_swap_interval: float
        fade_time: float


@dataclasses.dataclass()
class ScanImage(BaseProperty):
    texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000000, original_name="Texture"),
        },
    )
    appear_percentage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="AppearPercentage"),
        },
    )
    unnamed: enums.ScanImagePaneEnum = dataclasses.field(
        default=enums.ScanImagePaneEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ScanImagePaneEnum](
                enums.ScanImagePaneEnum,
                id=0x00000002,
                original_name="2",
                from_json=enums.ScanImagePaneEnum.from_json,
                to_json=enums.ScanImagePaneEnum.to_json,
            ),
        },
    )
    animation_cell_width: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="AnimationCellWidth"),
        },
    )
    animation_cell_height: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="AnimationCellHeight"),
        },
    )
    animation_swap_interval: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="AnimationSwapInterval"),
        },
    )
    fade_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="FadeTime"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        texture = structs.BIG_L.unpack(data.read(4))[0]
        appear_percentage = structs.BIG_f.unpack(data.read(4))[0]
        unnamed = enums.ScanImagePaneEnum.from_stream(data, game)
        animation_cell_width = structs.BIG_l.unpack(data.read(4))[0]
        animation_cell_height = structs.BIG_l.unpack(data.read(4))[0]
        animation_swap_interval = structs.BIG_f.unpack(data.read(4))[0]
        fade_time = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            texture,
            appear_percentage,
            unnamed,
            animation_cell_width,
            animation_cell_height,
            animation_swap_interval,
            fade_time,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_L.pack(self.texture))
        data.write(structs.BIG_f.pack(self.appear_percentage))
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.animation_cell_width))
        data.write(structs.BIG_l.pack(self.animation_cell_height))
        data.write(structs.BIG_f.pack(self.animation_swap_interval))
        data.write(structs.BIG_f.pack(self.fade_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScanImageJson", data)
        return cls(
            texture=json_data["texture"],
            appear_percentage=json_data["appear_percentage"],
            unnamed=enums.ScanImagePaneEnum.from_json(json_data["unnamed"]),
            animation_cell_width=json_data["animation_cell_width"],
            animation_cell_height=json_data["animation_cell_height"],
            animation_swap_interval=json_data["animation_swap_interval"],
            fade_time=json_data["fade_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "texture": self.texture,
            "appear_percentage": self.appear_percentage,
            "unnamed": self.unnamed.to_json(),
            "animation_cell_width": self.animation_cell_width,
            "animation_cell_height": self.animation_cell_height,
            "animation_swap_interval": self.animation_swap_interval,
            "fade_time": self.fade_time,
        }

    def _dependencies_for_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_texture(asset_manager)
