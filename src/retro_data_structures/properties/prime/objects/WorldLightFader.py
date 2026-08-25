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

    class WorldLightFaderJson(typing_extensions.TypedDict):
        name: str
        active: bool
        faded_light_level: float
        fade_speed: float


@dataclasses.dataclass()
class WorldLightFader(BaseObjectType):
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
    faded_light_level: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="Faded Light Level"),
        },
    )
    fade_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Fade Speed"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x82

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        faded_light_level = structs.BIG_f.unpack(data.read(4))[0]
        fade_speed = structs.BIG_f.unpack(data.read(4))[0]
        return cls(name, active, faded_light_level, fade_speed)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x04")  # 4 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.faded_light_level))
        data.write(structs.BIG_f.pack(self.fade_speed))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WorldLightFaderJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            faded_light_level=json_data["faded_light_level"],
            fade_speed=json_data["fade_speed"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "faded_light_level": self.faded_light_level,
            "fade_speed": self.fade_speed,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
