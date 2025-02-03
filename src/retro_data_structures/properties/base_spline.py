from __future__ import annotations

import dataclasses
import typing

from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util


def cached_tangent_default() -> tuple[float, float]:
    return (0.0, 0.0)


@dataclasses.dataclass()
class Knot(BaseProperty):
    time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Time"),
        },
    )  # X position
    amplitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Amplitude"),
        },
    )  # Y position
    unk_a: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="UnknownA"),
        },
    )
    unk_b: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="UnknownB"),
        },
    )
    cached_tangents_a: tuple[float, float] | None = dataclasses.field(
        default_factory=cached_tangent_default,
        metadata={
            "reflection": FieldReflection[tuple](list, id=0x00000004, original_name="CachedTangentsA"),
        },
    )
    cached_tangents_b: tuple[float, float] | None = dataclasses.field(
        default_factory=cached_tangent_default,
        metadata={
            "reflection": FieldReflection[tuple](list, id=0x00000005, original_name="CachedTangentsB"),
        },
    )

    @classmethod
    def from_json(cls, data: dict) -> typing.Self:
        return cls(
            time=data["time"],
            amplitude=data["amplitude"],
            unk_a=data["unk_a"],
            unk_b=data["unk_b"],
            cached_tangents_a=data["cached_tangents_a"],
            cached_tangents_b=data["cached_tangents_b"],
        )

    def to_json(self) -> dict:
        return {
            "time": self.time,
            "amplitude": self.amplitude,
            "unk_a": self.unk_a,
            "unk_b": self.unk_b,
            "cached_tangents_a": self.cached_tangents_a,
            "cached_tangents_b": self.cached_tangents_b,
        }


@dataclasses.dataclass()
class BaseSpline(BaseProperty):
    pre_infinity: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000000, original_name="PreInfinity"),
        },
    )
    post_infinity: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="PostInfinity"),
        },
    )
    knots: list[Knot] = dataclasses.field(
        default_factory=list,
        metadata={
            "reflection": FieldReflection[list](list, id=0x00000002, original_name="Knots"),
        },
    )
    clamp_mode: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="ClampMode"),
        },
    )
    minimum_amplitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="MinimumAmplitude"),
        },
    )
    maximum_amplitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="MaximumAmplitude"),
        },
    )

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        return cls(
            knots=[Knot.from_json(knot) for knot in data["knots"]],
            minimum_amplitude=data["minimum_amplitude"],
            maximum_amplitude=data["maximum_amplitude"],
            pre_infinity=data["pre_infinity"],
            post_infinity=data["post_infinity"],
            clamp_mode=data["clamp_mode"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "knots": [knot.to_json() for knot in self.knots],
            "minimum_amplitude": self.minimum_amplitude,
            "maximum_amplitude": self.maximum_amplitude,
            "pre_infinity": self.pre_infinity,
            "post_infinity": self.post_infinity,
            "clamp_mode": self.clamp_mode,
        }
