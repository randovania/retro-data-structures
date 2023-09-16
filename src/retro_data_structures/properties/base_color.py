from __future__ import annotations

import dataclasses

from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class BaseColor(BaseProperty):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 0.0

    @classmethod
    def from_json(cls, data: dict):
        return cls(data["r"], data["g"], data["b"], data["a"])

    def to_json(self) -> dict:
        return {
            "r": self.r,
            "g": self.g,
            "b": self.b,
            "a": self.a,
        }
