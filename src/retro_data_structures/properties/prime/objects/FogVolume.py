# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FogVolumeJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        scale: json_util.JsonValue
        flicker_speed: float
        unknown: float
        fog_color: json_util.JsonValue
        active: bool


@dataclasses.dataclass()
class FogVolume(BaseObjectType):
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
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    flicker_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="FlickerSpeed"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Unknown"),
        },
    )
    fog_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000005, original_name="FogColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x65

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        flicker_speed = structs.BIG_f.unpack(data.read(4))[0]
        unknown = structs.BIG_f.unpack(data.read(4))[0]
        fog_color = Color.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, position, scale, flicker_speed, unknown, fog_color, active)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.flicker_speed))
        data.write(structs.BIG_f.pack(self.unknown))
        self.fog_color.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FogVolumeJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            scale=Vector.from_json(json_data["scale"]),
            flicker_speed=json_data["flicker_speed"],
            unknown=json_data["unknown"],
            fog_color=Color.from_json(json_data["fog_color"]),
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "scale": self.scale.to_json(),
            "flicker_speed": self.flicker_speed,
            "unknown": self.unknown,
            "fog_color": self.fog_color.to_json(),
            "active": self.active,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
