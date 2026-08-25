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
from retro_data_structures.properties.prime.archetypes.PathCameraStruct import PathCameraStruct
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PathCameraJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        unnamed: json_util.JsonObject
        length_extent: float
        filter_mag: float
        filter_proportion: float
        initial_spline_position: int
        min_ease_dist_: float
        max_ease_dist_: float


class InitialSplinePosition(enum.IntEnum):
    BallCamBasis = 0
    Negative = 1
    Positive = 2
    ClampBasis = 3

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
class PathCamera(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Active"),
        },
    )
    unnamed: PathCameraStruct = dataclasses.field(
        default_factory=PathCameraStruct,
        metadata={
            "reflection": FieldReflection[PathCameraStruct](
                PathCameraStruct,
                id=0x00000004,
                original_name="4",
                from_json=PathCameraStruct.from_json,
                to_json=PathCameraStruct.to_json,
            ),
        },
    )
    length_extent: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="LengthExtent"),
        },
    )
    filter_mag: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="FilterMag"),
        },
    )
    filter_proportion: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="FilterProportion"),
        },
    )
    initial_spline_position: InitialSplinePosition = dataclasses.field(
        default=InitialSplinePosition.BallCamBasis,
        metadata={
            "reflection": FieldReflection[InitialSplinePosition](
                InitialSplinePosition,
                id=0x00000008,
                original_name="InitialSplinePosition",
                from_json=InitialSplinePosition.from_json,
                to_json=InitialSplinePosition.to_json,
            ),
        },
    )
    min_ease_dist_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="MinEaseDist "),
        },
    )
    max_ease_dist_: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="MaxEaseDist "),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x2F

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed = PathCameraStruct.from_stream(data, game, property_size)
        length_extent = structs.BIG_f.unpack(data.read(4))[0]
        filter_mag = structs.BIG_f.unpack(data.read(4))[0]
        filter_proportion = structs.BIG_f.unpack(data.read(4))[0]
        initial_spline_position = InitialSplinePosition.from_stream(data, game)
        min_ease_dist_ = structs.BIG_f.unpack(data.read(4))[0]
        max_ease_dist_ = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            active,
            unnamed,
            length_extent,
            filter_mag,
            filter_proportion,
            initial_spline_position,
            min_ease_dist_,
            max_ease_dist_,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0b")  # 11 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.length_extent))
        data.write(structs.BIG_f.pack(self.filter_mag))
        data.write(structs.BIG_f.pack(self.filter_proportion))
        self.initial_spline_position.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.min_ease_dist_))
        data.write(structs.BIG_f.pack(self.max_ease_dist_))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PathCameraJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            unnamed=PathCameraStruct.from_json(json_data["unnamed"]),
            length_extent=json_data["length_extent"],
            filter_mag=json_data["filter_mag"],
            filter_proportion=json_data["filter_proportion"],
            initial_spline_position=InitialSplinePosition.from_json(json_data["initial_spline_position"]),
            min_ease_dist_=json_data["min_ease_dist_"],
            max_ease_dist_=json_data["max_ease_dist_"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "unnamed": self.unnamed.to_json(),
            "length_extent": self.length_extent,
            "filter_mag": self.filter_mag,
            "filter_proportion": self.filter_proportion,
            "initial_spline_position": self.initial_spline_position.to_json(),
            "min_ease_dist_": self.min_ease_dist_,
            "max_ease_dist_": self.max_ease_dist_,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
