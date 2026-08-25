# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CounterJson(typing_extensions.TypedDict):
        name: str
        initial: int
        max: int
        auto_reset: bool
        active: bool


@dataclasses.dataclass()
class Counter(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    initial: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Initial"),
        },
    )
    max: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="Max"),
        },
    )
    auto_reset: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="AutoReset"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x6

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        initial = structs.BIG_l.unpack(data.read(4))[0]
        max = structs.BIG_l.unpack(data.read(4))[0]
        auto_reset = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, initial, max, auto_reset, active)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x05")  # 5 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.initial))
        data.write(structs.BIG_l.pack(self.max))
        data.write(structs.BIG_bool_.pack(self.auto_reset))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CounterJson", data)
        return cls(
            name=json_data["name"],
            initial=json_data["initial"],
            max=json_data["max"],
            auto_reset=json_data["auto_reset"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "initial": self.initial,
            "max": self.max,
            "auto_reset": self.auto_reset,
            "active": self.active,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
