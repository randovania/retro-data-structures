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

    class ActorRotateJson(typing_extensions.TypedDict):
        name: str
        rotation_offset: json_util.JsonValue
        time_scale: float
        update_actors: bool
        update_on_register: bool
        active: bool


@dataclasses.dataclass()
class ActorRotate(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    rotation_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000001,
                original_name="RotationOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    time_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="TimeScale"),
        },
    )
    update_actors: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="UpdateActors"),
        },
    )
    update_on_register: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="UpdateOnRegister"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000005, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x39

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        rotation_offset = Vector.from_stream(data, game, property_size)
        time_scale = structs.BIG_f.unpack(data.read(4))[0]
        update_actors = structs.BIG_bool_.unpack(data.read(1))[0]
        update_on_register = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, rotation_offset, time_scale, update_actors, update_on_register, active)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x06")  # 6 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.rotation_offset.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.time_scale))
        data.write(structs.BIG_bool_.pack(self.update_actors))
        data.write(structs.BIG_bool_.pack(self.update_on_register))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorRotateJson", data)
        return cls(
            name=json_data["name"],
            rotation_offset=Vector.from_json(json_data["rotation_offset"]),
            time_scale=json_data["time_scale"],
            update_actors=json_data["update_actors"],
            update_on_register=json_data["update_on_register"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "rotation_offset": self.rotation_offset.to_json(),
            "time_scale": self.time_scale,
            "update_actors": self.update_actors,
            "update_on_register": self.update_on_register,
            "active": self.active,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
