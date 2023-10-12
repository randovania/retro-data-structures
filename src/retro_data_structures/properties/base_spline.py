from __future__ import annotations

import dataclasses
import typing

from retro_data_structures.properties.base_property import BaseProperty

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util


@dataclasses.dataclass()
class Knot:
    time: float  # X position
    amplitude: float  # Y position
    unk_a: int
    unk_b: int
    cached_tangents_a: tuple[float, float] | None
    cached_tangents_b: tuple[float, float] | None

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
    knots: list[Knot] = dataclasses.field(default_factory=list)
    minimum_amplitude: float = 0.0
    maximum_amplitude: float = 0.0
    pre_infinity: int = 0
    post_infinity: int = 0
    clamp_mode: int = 0

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
