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

    class WaypointJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        speed: float
        pause: float
        pattern_translate: int
        pattern_orient: int
        pattern_fit: int
        behavior: int
        behavior_orient: int
        behaviour_modifiers: int
        animation: int


@dataclasses.dataclass()
class Waypoint(BaseObjectType):
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
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Active"),
        },
    )
    speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Speed"),
        },
    )
    pause: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Pause"),
        },
    )
    pattern_translate: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="PatternTranslate"),
        },
    )
    pattern_orient: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="PatternOrient"),
        },
    )
    pattern_fit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="PatternFit"),
        },
    )
    behavior: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Behavior"),
        },
    )
    behavior_orient: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000A, original_name="BehaviorOrient"),
        },
    )
    behaviour_modifiers: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="BehaviourModifiers"),
        },
    )
    animation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000C, original_name="Animation"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x2

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        speed = structs.BIG_f.unpack(data.read(4))[0]
        pause = structs.BIG_f.unpack(data.read(4))[0]
        pattern_translate = structs.BIG_l.unpack(data.read(4))[0]
        pattern_orient = structs.BIG_l.unpack(data.read(4))[0]
        pattern_fit = structs.BIG_l.unpack(data.read(4))[0]
        behavior = structs.BIG_l.unpack(data.read(4))[0]
        behavior_orient = structs.BIG_l.unpack(data.read(4))[0]
        behaviour_modifiers = structs.BIG_l.unpack(data.read(4))[0]
        animation = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            active,
            speed,
            pause,
            pattern_translate,
            pattern_orient,
            pattern_fit,
            behavior,
            behavior_orient,
            behaviour_modifiers,
            animation,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\r")  # 13 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.speed))
        data.write(structs.BIG_f.pack(self.pause))
        data.write(structs.BIG_l.pack(self.pattern_translate))
        data.write(structs.BIG_l.pack(self.pattern_orient))
        data.write(structs.BIG_l.pack(self.pattern_fit))
        data.write(structs.BIG_l.pack(self.behavior))
        data.write(structs.BIG_l.pack(self.behavior_orient))
        data.write(structs.BIG_l.pack(self.behaviour_modifiers))
        data.write(structs.BIG_l.pack(self.animation))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WaypointJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            speed=json_data["speed"],
            pause=json_data["pause"],
            pattern_translate=json_data["pattern_translate"],
            pattern_orient=json_data["pattern_orient"],
            pattern_fit=json_data["pattern_fit"],
            behavior=json_data["behavior"],
            behavior_orient=json_data["behavior_orient"],
            behaviour_modifiers=json_data["behaviour_modifiers"],
            animation=json_data["animation"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "speed": self.speed,
            "pause": self.pause,
            "pattern_translate": self.pattern_translate,
            "pattern_orient": self.pattern_orient,
            "pattern_fit": self.pattern_fit,
            "behavior": self.behavior,
            "behavior_orient": self.behavior_orient,
            "behaviour_modifiers": self.behaviour_modifiers,
            "animation": self.animation,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
