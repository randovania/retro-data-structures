# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FishCloudModifierJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        active: bool
        repulsor: bool
        swirl: bool
        radius: float
        priority: float


@dataclasses.dataclass()
class FishCloudModifier(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="Active"),
        },
    )
    repulsor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Repulsor"),
        },
    )
    swirl: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Swirl"),
        },
    )
    radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Radius"),
        },
    )
    priority: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Priority"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x50

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        repulsor = structs.BIG_bool_.unpack(data.read(1))[0]
        swirl = structs.BIG_bool_.unpack(data.read(1))[0]
        radius = structs.BIG_f.unpack(data.read(4))[0]
        priority = structs.BIG_f.unpack(data.read(4))[0]
        return cls(name, position, active, repulsor, swirl, radius, priority)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_bool_.pack(self.repulsor))
        data.write(structs.BIG_bool_.pack(self.swirl))
        data.write(structs.BIG_f.pack(self.radius))
        data.write(structs.BIG_f.pack(self.priority))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FishCloudModifierJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            active=json_data["active"],
            repulsor=json_data["repulsor"],
            swirl=json_data["swirl"],
            radius=json_data["radius"],
            priority=json_data["priority"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "active": self.active,
            "repulsor": self.repulsor,
            "swirl": self.swirl,
            "radius": self.radius,
            "priority": self.priority,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
