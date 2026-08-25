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

    class ShadowProjectorJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        active: bool
        shadow_scale: float
        shadow_offset: json_util.JsonValue
        unknown_4: float
        shadow_opacity: float
        unknown_6: float
        unknown_7: bool
        unknown_8: int


@dataclasses.dataclass()
class ShadowProjector(BaseObjectType):
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
    shadow_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Shadow Scale"),
        },
    )
    shadow_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Shadow Offset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Unknown 4"),
        },
    )
    shadow_opacity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Shadow Opacity"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Unknown 6"),
        },
    )
    unknown_7: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="Unknown 7"),
        },
    )
    unknown_8: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Unknown 8"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x8A

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        shadow_scale = structs.BIG_f.unpack(data.read(4))[0]
        shadow_offset = Vector.from_stream(data, game, property_size)
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        shadow_opacity = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_8 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            active,
            shadow_scale,
            shadow_offset,
            unknown_4,
            shadow_opacity,
            unknown_6,
            unknown_7,
            unknown_8,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\n")  # 10 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.shadow_scale))
        self.shadow_offset.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.shadow_opacity))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_bool_.pack(self.unknown_7))
        data.write(structs.BIG_l.pack(self.unknown_8))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShadowProjectorJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            active=json_data["active"],
            shadow_scale=json_data["shadow_scale"],
            shadow_offset=Vector.from_json(json_data["shadow_offset"]),
            unknown_4=json_data["unknown_4"],
            shadow_opacity=json_data["shadow_opacity"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "active": self.active,
            "shadow_scale": self.shadow_scale,
            "shadow_offset": self.shadow_offset.to_json(),
            "unknown_4": self.unknown_4,
            "shadow_opacity": self.shadow_opacity,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
