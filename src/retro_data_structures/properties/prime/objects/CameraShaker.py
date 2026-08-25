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

    class CameraShakerJson(typing_extensions.TypedDict):
        name: str
        horizontal_shake: float
        unused_0x00000002: float
        unused_0x00000003: float
        unused_0x00000004: float
        vertical_shake: float
        unused_0x00000006: float
        shake_duration: float
        active: bool


@dataclasses.dataclass()
class CameraShaker(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    horizontal_shake: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="HorizontalShake"),
        },
    )
    unused_0x00000002: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="(unused)"),
        },
    )
    unused_0x00000003: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="(unused)"),
        },
    )
    unused_0x00000004: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="(unused)"),
        },
    )
    vertical_shake: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="VerticalShake"),
        },
    )
    unused_0x00000006: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="(unused)"),
        },
    )
    shake_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="ShakeDuration"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x1C

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        horizontal_shake = structs.BIG_f.unpack(data.read(4))[0]
        unused_0x00000002 = structs.BIG_f.unpack(data.read(4))[0]
        unused_0x00000003 = structs.BIG_f.unpack(data.read(4))[0]
        unused_0x00000004 = structs.BIG_f.unpack(data.read(4))[0]
        vertical_shake = structs.BIG_f.unpack(data.read(4))[0]
        unused_0x00000006 = structs.BIG_f.unpack(data.read(4))[0]
        shake_duration = structs.BIG_f.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            horizontal_shake,
            unused_0x00000002,
            unused_0x00000003,
            unused_0x00000004,
            vertical_shake,
            unused_0x00000006,
            shake_duration,
            active,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\t")  # 9 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_f.pack(self.horizontal_shake))
        data.write(structs.BIG_f.pack(self.unused_0x00000002))
        data.write(structs.BIG_f.pack(self.unused_0x00000003))
        data.write(structs.BIG_f.pack(self.unused_0x00000004))
        data.write(structs.BIG_f.pack(self.vertical_shake))
        data.write(structs.BIG_f.pack(self.unused_0x00000006))
        data.write(structs.BIG_f.pack(self.shake_duration))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraShakerJson", data)
        return cls(
            name=json_data["name"],
            horizontal_shake=json_data["horizontal_shake"],
            unused_0x00000002=json_data["unused_0x00000002"],
            unused_0x00000003=json_data["unused_0x00000003"],
            unused_0x00000004=json_data["unused_0x00000004"],
            vertical_shake=json_data["vertical_shake"],
            unused_0x00000006=json_data["unused_0x00000006"],
            shake_duration=json_data["shake_duration"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "horizontal_shake": self.horizontal_shake,
            "unused_0x00000002": self.unused_0x00000002,
            "unused_0x00000003": self.unused_0x00000003,
            "unused_0x00000004": self.unused_0x00000004,
            "vertical_shake": self.vertical_shake,
            "unused_0x00000006": self.unused_0x00000006,
            "shake_duration": self.shake_duration,
            "active": self.active,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
