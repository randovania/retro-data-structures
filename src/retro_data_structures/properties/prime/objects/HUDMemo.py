# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class HUDMemoJson(typing_extensions.TypedDict):
        name: str
        display_time: float
        clear_memo_window: bool
        display_type: int
        message: int
        active: bool


class DisplayType(enum.IntEnum):
    StatusMessage = 0
    MessageBox = 1

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class HUDMemo(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    display_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="DisplayTime"),
        },
    )
    clear_memo_window: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="ClearMemoWindow"),
        },
    )
    display_type: DisplayType = dataclasses.field(
        default=DisplayType.StatusMessage,
        metadata={
            "reflection": FieldReflection[DisplayType](
                DisplayType,
                id=0x00000003,
                original_name="DisplayType",
                from_json=DisplayType.from_json,
                to_json=DisplayType.to_json,
            ),
        },
    )
    message: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRG"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000004, original_name="Message"),
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
        return 0x17

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        display_time = structs.BIG_f.unpack(data.read(4))[0]
        clear_memo_window = structs.BIG_bool_.unpack(data.read(1))[0]
        display_type = DisplayType.from_stream(data, game)
        message = structs.BIG_L.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, display_time, clear_memo_window, display_type, message, active)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x06")  # 6 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_f.pack(self.display_time))
        data.write(structs.BIG_bool_.pack(self.clear_memo_window))
        self.display_type.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.message))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("HUDMemoJson", data)
        return cls(
            name=json_data["name"],
            display_time=json_data["display_time"],
            clear_memo_window=json_data["clear_memo_window"],
            display_type=DisplayType.from_json(json_data["display_type"]),
            message=json_data["message"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "display_time": self.display_time,
            "clear_memo_window": self.clear_memo_window,
            "display_type": self.display_type.to_json(),
            "message": self.message,
            "active": self.active,
        }

    def _dependencies_for_message(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.message)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_message(asset_manager)
