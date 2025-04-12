from __future__ import annotations

import dataclasses
import typing

from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util

    class KnotJson(typing_extensions.TypedDict):
        time: float
        amplitude: float
        unk_a: int
        unk_b: int
        cached_tangents_a: typing.Sequence[float] | None
        cached_tangents_b: typing.Sequence[float] | None

    class SplineJson(typing_extensions.TypedDict):
        pre_infinity: int
        post_infinity: int
        knots: typing.Sequence[json_util.JsonObject]
        clamp_mode: int
        minimum_amplitude: float
        maximum_amplitude: float


def _cached_tangents_from_json(data: json_util.JsonValue) -> tuple[float, float] | None:
    if data is None:
        return None
    assert isinstance(data, list) and len(data) == 2
    return typing.cast(tuple[float, float], (data[0], data[1]))


def _cached_tangents_to_json(data: tuple[float, float] | None) -> json_util.JsonValue:
    if data is None:
        return None
    return list(data)


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
        default=None,
        metadata={
            "reflection": FieldReflection[tuple[float, float] | None](
                tuple[float, float],
                id=0x00000004,
                original_name="CachedTangentsA",
                from_json=_cached_tangents_from_json,
                to_json=_cached_tangents_to_json,
            ),
        },
    )
    cached_tangents_b: tuple[float, float] | None = dataclasses.field(
        default=None,
        metadata={
            "reflection": FieldReflection[tuple[float, float] | None](
                tuple[float, float],
                id=0x00000005,
                original_name="CachedTangentsB",
                from_json=_cached_tangents_from_json,
                to_json=_cached_tangents_to_json,
            ),
        },
    )

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KnotJson", data)
        return cls(
            time=json_data["time"],
            amplitude=json_data["amplitude"],
            unk_a=json_data["unk_a"],
            unk_b=json_data["unk_b"],
            cached_tangents_a=_cached_tangents_from_json(json_data["cached_tangents_a"]),
            cached_tangents_b=_cached_tangents_from_json(json_data["cached_tangents_b"]),
        )

    def to_json(self) -> dict:
        return {
            "time": self.time,
            "amplitude": self.amplitude,
            "unk_a": self.unk_a,
            "unk_b": self.unk_b,
            "cached_tangents_a": _cached_tangents_to_json(self.cached_tangents_a),
            "cached_tangents_b": _cached_tangents_to_json(self.cached_tangents_b),
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
        json_data = typing.cast("SplineJson", data)
        return cls(
            knots=[Knot.from_json(knot) for knot in json_data["knots"]],
            minimum_amplitude=json_data["minimum_amplitude"],
            maximum_amplitude=json_data["maximum_amplitude"],
            pre_infinity=json_data["pre_infinity"],
            post_infinity=json_data["post_infinity"],
            clamp_mode=json_data["clamp_mode"],
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
