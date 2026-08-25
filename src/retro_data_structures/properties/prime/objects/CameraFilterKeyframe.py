# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraFilterKeyframeJson(typing_extensions.TypedDict):
        name: str
        active: bool
        filter_type: int
        filter_shape: int
        filter_index: int
        filter_group: int
        filter_color: json_util.JsonValue
        fade_in_duration: float
        fade_out_duration: float
        overlay_texture: int


class FilterType(enum.IntEnum):
    Passthrough = 0
    Multiply = 1
    Invert = 2
    Add = 3
    Subtract = 4
    Blend = 5
    Widescreen = 6
    SceneAdd = 7
    NoColor = 8
    InvDstMultiply = 9

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


class FilterShape(enum.IntEnum):
    Fullscreen = 0
    FullscreenHalvesLeftRight = 1
    FullscreenHalvesTopBottom = 2
    FullscreenQuarters = 3
    CinemaBars = 4
    ScanLinesEven = 5
    ScanLinesOdd = 6
    RandomStatic = 7
    CookieCutterDepthRandomStatic = 8

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
class CameraFilterKeyframe(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Active"),
        },
    )
    filter_type: FilterType = dataclasses.field(
        default=FilterType.Passthrough,
        metadata={
            "reflection": FieldReflection[FilterType](
                FilterType,
                id=0x00000002,
                original_name="FilterType",
                from_json=FilterType.from_json,
                to_json=FilterType.to_json,
            ),
        },
    )
    filter_shape: FilterShape = dataclasses.field(
        default=FilterShape.Fullscreen,
        metadata={
            "reflection": FieldReflection[FilterShape](
                FilterShape,
                id=0x00000003,
                original_name="FilterShape",
                from_json=FilterShape.from_json,
                to_json=FilterShape.to_json,
            ),
        },
    )
    filter_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="FilterIndex"),
        },
    )
    filter_group: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="FilterGroup"),
        },
    )
    filter_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000006, original_name="FilterColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    fade_in_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="FadeInDuration"),
        },
    )
    fade_out_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="FadeOutDuration"),
        },
    )
    overlay_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="OverlayTexture"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x18

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        filter_type = FilterType.from_stream(data, game)
        filter_shape = FilterShape.from_stream(data, game)
        filter_index = structs.BIG_l.unpack(data.read(4))[0]
        filter_group = structs.BIG_l.unpack(data.read(4))[0]
        filter_color = Color.from_stream(data, game, property_size)
        fade_in_duration = structs.BIG_f.unpack(data.read(4))[0]
        fade_out_duration = structs.BIG_f.unpack(data.read(4))[0]
        overlay_texture = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            active,
            filter_type,
            filter_shape,
            filter_index,
            filter_group,
            filter_color,
            fade_in_duration,
            fade_out_duration,
            overlay_texture,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\n")  # 10 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        self.filter_type.to_stream(data, game)
        self.filter_shape.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.filter_index))
        data.write(structs.BIG_l.pack(self.filter_group))
        self.filter_color.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.fade_in_duration))
        data.write(structs.BIG_f.pack(self.fade_out_duration))
        data.write(structs.BIG_L.pack(self.overlay_texture))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraFilterKeyframeJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            filter_type=FilterType.from_json(json_data["filter_type"]),
            filter_shape=FilterShape.from_json(json_data["filter_shape"]),
            filter_index=json_data["filter_index"],
            filter_group=json_data["filter_group"],
            filter_color=Color.from_json(json_data["filter_color"]),
            fade_in_duration=json_data["fade_in_duration"],
            fade_out_duration=json_data["fade_out_duration"],
            overlay_texture=json_data["overlay_texture"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "filter_type": self.filter_type.to_json(),
            "filter_shape": self.filter_shape.to_json(),
            "filter_index": self.filter_index,
            "filter_group": self.filter_group,
            "filter_color": self.filter_color.to_json(),
            "fade_in_duration": self.fade_in_duration,
            "fade_out_duration": self.fade_out_duration,
            "overlay_texture": self.overlay_texture,
        }

    def _dependencies_for_overlay_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.overlay_texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_overlay_texture(asset_manager)
