# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.FluidLayerMotion import FluidLayerMotion

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FluidUVMotionJson(typing_extensions.TypedDict):
        fluid_layer_motion_1: json_util.JsonObject
        fluid_layer_motion_2: json_util.JsonObject
        fluid_layer_motion_3: json_util.JsonObject
        time_to_wrap: float
        orientation: float


@dataclasses.dataclass()
class FluidUVMotion(BaseProperty):
    fluid_layer_motion_1: FluidLayerMotion = dataclasses.field(
        default_factory=FluidLayerMotion,
        metadata={
            "reflection": FieldReflection[FluidLayerMotion](
                FluidLayerMotion,
                id=0x00000000,
                original_name="Fluid Layer Motion 1",
                from_json=FluidLayerMotion.from_json,
                to_json=FluidLayerMotion.to_json,
            ),
        },
    )
    fluid_layer_motion_2: FluidLayerMotion = dataclasses.field(
        default_factory=FluidLayerMotion,
        metadata={
            "reflection": FieldReflection[FluidLayerMotion](
                FluidLayerMotion,
                id=0x00000001,
                original_name="Fluid Layer Motion 2",
                from_json=FluidLayerMotion.from_json,
                to_json=FluidLayerMotion.to_json,
            ),
        },
    )
    fluid_layer_motion_3: FluidLayerMotion = dataclasses.field(
        default_factory=FluidLayerMotion,
        metadata={
            "reflection": FieldReflection[FluidLayerMotion](
                FluidLayerMotion,
                id=0x00000002,
                original_name="Fluid Layer Motion 3",
                from_json=FluidLayerMotion.from_json,
                to_json=FluidLayerMotion.to_json,
            ),
        },
    )
    time_to_wrap: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Time To Wrap"),
        },
    )
    orientation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Orientation"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        fluid_layer_motion_1 = FluidLayerMotion.from_stream(data, game, property_size)
        fluid_layer_motion_2 = FluidLayerMotion.from_stream(data, game, property_size)
        fluid_layer_motion_3 = FluidLayerMotion.from_stream(data, game, property_size)
        time_to_wrap = structs.BIG_f.unpack(data.read(4))[0]
        orientation = structs.BIG_f.unpack(data.read(4))[0]
        return cls(fluid_layer_motion_1, fluid_layer_motion_2, fluid_layer_motion_3, time_to_wrap, orientation)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.fluid_layer_motion_1.to_stream(data, game)
        self.fluid_layer_motion_2.to_stream(data, game)
        self.fluid_layer_motion_3.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.time_to_wrap))
        data.write(structs.BIG_f.pack(self.orientation))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FluidUVMotionJson", data)
        return cls(
            fluid_layer_motion_1=FluidLayerMotion.from_json(json_data["fluid_layer_motion_1"]),
            fluid_layer_motion_2=FluidLayerMotion.from_json(json_data["fluid_layer_motion_2"]),
            fluid_layer_motion_3=FluidLayerMotion.from_json(json_data["fluid_layer_motion_3"]),
            time_to_wrap=json_data["time_to_wrap"],
            orientation=json_data["orientation"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "fluid_layer_motion_1": self.fluid_layer_motion_1.to_json(),
            "fluid_layer_motion_2": self.fluid_layer_motion_2.to_json(),
            "fluid_layer_motion_3": self.fluid_layer_motion_3.to_json(),
            "time_to_wrap": self.time_to_wrap,
            "orientation": self.orientation,
        }
