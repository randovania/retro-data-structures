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

    class GeneratorJson(typing_extensions.TypedDict):
        name: str
        spawn_count: int
        no_reuse_followers: bool
        no_inherit_xf: bool
        offset: json_util.JsonValue
        active: bool
        min_scale: float
        max_scale: float


@dataclasses.dataclass()
class Generator(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    spawn_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="SpawnCount"),
        },
    )
    no_reuse_followers: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="NoReuseFollowers"),
        },
    )
    no_inherit_xf: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="NoInheritXf"),
        },
    )
    offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Offset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000005, original_name="Active"),
        },
    )
    min_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="MinScale"),
        },
    )
    max_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="MaxScale"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0xA

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        spawn_count = structs.BIG_l.unpack(data.read(4))[0]
        no_reuse_followers = structs.BIG_bool_.unpack(data.read(1))[0]
        no_inherit_xf = structs.BIG_bool_.unpack(data.read(1))[0]
        offset = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        min_scale = structs.BIG_f.unpack(data.read(4))[0]
        max_scale = structs.BIG_f.unpack(data.read(4))[0]
        return cls(name, spawn_count, no_reuse_followers, no_inherit_xf, offset, active, min_scale, max_scale)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x08")  # 8 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.spawn_count))
        data.write(structs.BIG_bool_.pack(self.no_reuse_followers))
        data.write(structs.BIG_bool_.pack(self.no_inherit_xf))
        self.offset.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.min_scale))
        data.write(structs.BIG_f.pack(self.max_scale))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GeneratorJson", data)
        return cls(
            name=json_data["name"],
            spawn_count=json_data["spawn_count"],
            no_reuse_followers=json_data["no_reuse_followers"],
            no_inherit_xf=json_data["no_inherit_xf"],
            offset=Vector.from_json(json_data["offset"]),
            active=json_data["active"],
            min_scale=json_data["min_scale"],
            max_scale=json_data["max_scale"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "spawn_count": self.spawn_count,
            "no_reuse_followers": self.no_reuse_followers,
            "no_inherit_xf": self.no_inherit_xf,
            "offset": self.offset.to_json(),
            "active": self.active,
            "min_scale": self.min_scale,
            "max_scale": self.max_scale,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
