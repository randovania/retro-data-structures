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

    class DockJson(typing_extensions.TypedDict):
        name: str
        active: bool
        position: json_util.JsonValue
        scale: json_util.JsonValue
        dock_index: int
        area_index: int
        load_connected: bool


@dataclasses.dataclass()
class Dock(BaseObjectType):
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
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    dock_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="DockIndex"),
        },
    )
    area_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="AreaIndex"),
        },
    )
    load_connected: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="LoadConnected"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0xB

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        position = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        dock_index = structs.BIG_l.unpack(data.read(4))[0]
        area_index = structs.BIG_l.unpack(data.read(4))[0]
        load_connected = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, active, position, scale, dock_index, area_index, load_connected)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        self.position.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.dock_index))
        data.write(structs.BIG_l.pack(self.area_index))
        data.write(structs.BIG_bool_.pack(self.load_connected))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DockJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            position=Vector.from_json(json_data["position"]),
            scale=Vector.from_json(json_data["scale"]),
            dock_index=json_data["dock_index"],
            area_index=json_data["area_index"],
            load_connected=json_data["load_connected"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "position": self.position.to_json(),
            "scale": self.scale.to_json(),
            "dock_index": self.dock_index,
            "area_index": self.area_index,
            "load_connected": self.load_connected,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
