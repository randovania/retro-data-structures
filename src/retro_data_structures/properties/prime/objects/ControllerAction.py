# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.prime as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ControllerActionJson(typing_extensions.TypedDict):
        name: str
        active: bool
        command: int
        deactivate_on_close: bool


@dataclasses.dataclass()
class ControllerAction(BaseObjectType):
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
    command: enums.PlayerActionEnum = dataclasses.field(
        default=enums.PlayerActionEnum.Forward,
        metadata={
            "reflection": FieldReflection[enums.PlayerActionEnum](
                enums.PlayerActionEnum,
                id=0x00000002,
                original_name="Command",
                from_json=enums.PlayerActionEnum.from_json,
                to_json=enums.PlayerActionEnum.to_json,
            ),
        },
    )
    deactivate_on_close: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="DeactivateOnClose"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x55

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        command = enums.PlayerActionEnum.from_stream(data, game)
        deactivate_on_close = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, active, command, deactivate_on_close)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x04")  # 4 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        self.command.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.deactivate_on_close))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ControllerActionJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            command=enums.PlayerActionEnum.from_json(json_data["command"]),
            deactivate_on_close=json_data["deactivate_on_close"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "command": self.command.to_json(),
            "deactivate_on_close": self.deactivate_on_close,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
