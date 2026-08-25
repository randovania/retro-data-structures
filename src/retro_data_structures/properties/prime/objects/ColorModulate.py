# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ColorModulateJson(typing_extensions.TypedDict):
        name: str
        color_a: json_util.JsonValue
        color_b: json_util.JsonValue
        blend_mode: int
        time_a2_b: float
        time_b2_a: float
        do_reverse: bool
        reset_target_when_done: bool
        depth_compare: bool
        depth_update: bool
        depth_backwards: bool
        active: bool


class BlendMode(enum.IntEnum):
    Alpha = 0
    Additive = 1
    Additive2 = 2
    Opaque = 3
    OpaqueAdd = 4

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
class ColorModulate(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    color_a: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000001, original_name="Color A", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    color_b: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000002, original_name="Color B", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    blend_mode: BlendMode = dataclasses.field(
        default=BlendMode.Alpha,
        metadata={
            "reflection": FieldReflection[BlendMode](
                BlendMode,
                id=0x00000003,
                original_name="BlendMode",
                from_json=BlendMode.from_json,
                to_json=BlendMode.to_json,
            ),
        },
    )
    time_a2_b: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="TimeA2B"),
        },
    )
    time_b2_a: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="TimeB2A"),
        },
    )
    do_reverse: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="DoReverse"),
        },
    )
    reset_target_when_done: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="ResetTargetWhenDone"),
        },
    )
    depth_compare: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="DepthCompare"),
        },
    )
    depth_update: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="DepthUpdate"),
        },
    )
    depth_backwards: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="DepthBackwards"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="Active"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x5E

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        color_a = Color.from_stream(data, game, property_size)
        color_b = Color.from_stream(data, game, property_size)
        blend_mode = BlendMode.from_stream(data, game)
        time_a2_b = structs.BIG_f.unpack(data.read(4))[0]
        time_b2_a = structs.BIG_f.unpack(data.read(4))[0]
        do_reverse = structs.BIG_bool_.unpack(data.read(1))[0]
        reset_target_when_done = structs.BIG_bool_.unpack(data.read(1))[0]
        depth_compare = structs.BIG_bool_.unpack(data.read(1))[0]
        depth_update = structs.BIG_bool_.unpack(data.read(1))[0]
        depth_backwards = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            color_a,
            color_b,
            blend_mode,
            time_a2_b,
            time_b2_a,
            do_reverse,
            reset_target_when_done,
            depth_compare,
            depth_update,
            depth_backwards,
            active,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0c")  # 12 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.color_a.to_stream(data, game)
        self.color_b.to_stream(data, game)
        self.blend_mode.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.time_a2_b))
        data.write(structs.BIG_f.pack(self.time_b2_a))
        data.write(structs.BIG_bool_.pack(self.do_reverse))
        data.write(structs.BIG_bool_.pack(self.reset_target_when_done))
        data.write(structs.BIG_bool_.pack(self.depth_compare))
        data.write(structs.BIG_bool_.pack(self.depth_update))
        data.write(structs.BIG_bool_.pack(self.depth_backwards))
        data.write(structs.BIG_bool_.pack(self.active))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ColorModulateJson", data)
        return cls(
            name=json_data["name"],
            color_a=Color.from_json(json_data["color_a"]),
            color_b=Color.from_json(json_data["color_b"]),
            blend_mode=BlendMode.from_json(json_data["blend_mode"]),
            time_a2_b=json_data["time_a2_b"],
            time_b2_a=json_data["time_b2_a"],
            do_reverse=json_data["do_reverse"],
            reset_target_when_done=json_data["reset_target_when_done"],
            depth_compare=json_data["depth_compare"],
            depth_update=json_data["depth_update"],
            depth_backwards=json_data["depth_backwards"],
            active=json_data["active"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "color_a": self.color_a.to_json(),
            "color_b": self.color_b.to_json(),
            "blend_mode": self.blend_mode.to_json(),
            "time_a2_b": self.time_a2_b,
            "time_b2_a": self.time_b2_a,
            "do_reverse": self.do_reverse,
            "reset_target_when_done": self.reset_target_when_done,
            "depth_compare": self.depth_compare,
            "depth_update": self.depth_update,
            "depth_backwards": self.depth_backwards,
            "active": self.active,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
