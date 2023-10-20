from __future__ import annotations

import dataclasses

from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class BaseVector(BaseProperty):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @classmethod
    def from_json(cls, data: dict):
        return cls(data["x"], data["y"], data["z"])

    def to_json(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def dependencies_for(self, asset_manager):
        yield from []
