# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FluidLayerMotionJson(typing_extensions.TypedDict):
        fluid_uv_motion: int
        time_to_wrap: float
        orientation: float
        magnitude: float
        multiplication: float


@dataclasses.dataclass()
class FluidLayerMotion(BaseProperty):
    fluid_uv_motion: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000000, original_name="Fluid UV Motion"),
        },
    )
    time_to_wrap: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Time To Wrap"),
        },
    )
    orientation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="Orientation"),
        },
    )
    magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Magnitude"),
        },
    )
    multiplication: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Multiplication"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        fluid_uv_motion = structs.BIG_l.unpack(data.read(4))[0]
        time_to_wrap = structs.BIG_f.unpack(data.read(4))[0]
        orientation = structs.BIG_f.unpack(data.read(4))[0]
        magnitude = structs.BIG_f.unpack(data.read(4))[0]
        multiplication = structs.BIG_f.unpack(data.read(4))[0]
        return cls(fluid_uv_motion, time_to_wrap, orientation, magnitude, multiplication)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_l.pack(self.fluid_uv_motion))
        data.write(structs.BIG_f.pack(self.time_to_wrap))
        data.write(structs.BIG_f.pack(self.orientation))
        data.write(structs.BIG_f.pack(self.magnitude))
        data.write(structs.BIG_f.pack(self.multiplication))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FluidLayerMotionJson", data)
        return cls(
            fluid_uv_motion=json_data["fluid_uv_motion"],
            time_to_wrap=json_data["time_to_wrap"],
            orientation=json_data["orientation"],
            magnitude=json_data["magnitude"],
            multiplication=json_data["multiplication"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "fluid_uv_motion": self.fluid_uv_motion,
            "time_to_wrap": self.time_to_wrap,
            "orientation": self.orientation,
            "magnitude": self.magnitude,
            "multiplication": self.multiplication,
        }
