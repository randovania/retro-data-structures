# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.GuessStruct import GuessStruct
from retro_data_structures.properties.prime.archetypes.IntBool import IntBool
from retro_data_structures.properties.prime.archetypes.NewCameraShakerStruct import NewCameraShakerStruct
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class NewCameraShakerJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        active: bool
        unnamed_0x00000003: json_util.JsonObject
        unnamed_0x00000004: json_util.JsonObject
        shaker_x: json_util.JsonObject
        shaker_y: json_util.JsonObject
        shaker_z: json_util.JsonObject


@dataclasses.dataclass()
class NewCameraShaker(BaseObjectType):
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
    unnamed_0x00000003: IntBool = dataclasses.field(
        default_factory=IntBool,
        metadata={
            "reflection": FieldReflection[IntBool](
                IntBool, id=0x00000003, original_name="3", from_json=IntBool.from_json, to_json=IntBool.to_json
            ),
        },
    )
    unnamed_0x00000004: GuessStruct = dataclasses.field(
        default_factory=GuessStruct,
        metadata={
            "reflection": FieldReflection[GuessStruct](
                GuessStruct,
                id=0x00000004,
                original_name="4",
                from_json=GuessStruct.from_json,
                to_json=GuessStruct.to_json,
            ),
        },
    )
    shaker_x: NewCameraShakerStruct = dataclasses.field(
        default_factory=NewCameraShakerStruct,
        metadata={
            "reflection": FieldReflection[NewCameraShakerStruct](
                NewCameraShakerStruct,
                id=0x00000005,
                original_name="ShakerX",
                from_json=NewCameraShakerStruct.from_json,
                to_json=NewCameraShakerStruct.to_json,
            ),
        },
    )
    shaker_y: NewCameraShakerStruct = dataclasses.field(
        default_factory=NewCameraShakerStruct,
        metadata={
            "reflection": FieldReflection[NewCameraShakerStruct](
                NewCameraShakerStruct,
                id=0x00000006,
                original_name="ShakerY",
                from_json=NewCameraShakerStruct.from_json,
                to_json=NewCameraShakerStruct.to_json,
            ),
        },
    )
    shaker_z: NewCameraShakerStruct = dataclasses.field(
        default_factory=NewCameraShakerStruct,
        metadata={
            "reflection": FieldReflection[NewCameraShakerStruct](
                NewCameraShakerStruct,
                id=0x00000007,
                original_name="ShakerZ",
                from_json=NewCameraShakerStruct.from_json,
                to_json=NewCameraShakerStruct.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x89

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed_0x00000003 = IntBool.from_stream(data, game, property_size)
        unnamed_0x00000004 = GuessStruct.from_stream(data, game, property_size)
        shaker_x = NewCameraShakerStruct.from_stream(data, game, property_size)
        shaker_y = NewCameraShakerStruct.from_stream(data, game, property_size)
        shaker_z = NewCameraShakerStruct.from_stream(data, game, property_size)
        return cls(name, position, active, unnamed_0x00000003, unnamed_0x00000004, shaker_x, shaker_y, shaker_z)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x08")  # 8 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed_0x00000003.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.shaker_x.to_stream(data, game)
        self.shaker_y.to_stream(data, game)
        self.shaker_z.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("NewCameraShakerJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            active=json_data["active"],
            unnamed_0x00000003=IntBool.from_json(json_data["unnamed_0x00000003"]),
            unnamed_0x00000004=GuessStruct.from_json(json_data["unnamed_0x00000004"]),
            shaker_x=NewCameraShakerStruct.from_json(json_data["shaker_x"]),
            shaker_y=NewCameraShakerStruct.from_json(json_data["shaker_y"]),
            shaker_z=NewCameraShakerStruct.from_json(json_data["shaker_z"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "active": self.active,
            "unnamed_0x00000003": self.unnamed_0x00000003.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "shaker_x": self.shaker_x.to_json(),
            "shaker_y": self.shaker_y.to_json(),
            "shaker_z": self.shaker_z.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
