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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MazeNodeJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        column: int
        row: int
        side: int
        actor_pos: json_util.JsonValue
        trigger_pos: json_util.JsonValue
        effect_pos: json_util.JsonValue


class Side(enum.IntEnum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3

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
class MazeNode(BaseObjectType):
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
    column: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="Column"),
        },
    )
    row: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="Row"),
        },
    )
    side: Side = dataclasses.field(
        default=Side.Top,
        metadata={
            "reflection": FieldReflection[Side](
                Side, id=0x00000006, original_name="Side", from_json=Side.from_json, to_json=Side.to_json
            ),
        },
    )
    actor_pos: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000007, original_name="ActorPos", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    trigger_pos: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000008, original_name="TriggerPos", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    effect_pos: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000009, original_name="EffectPos", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x85

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
        column = structs.BIG_l.unpack(data.read(4))[0]
        row = structs.BIG_l.unpack(data.read(4))[0]
        side = Side.from_stream(data, game)
        actor_pos = Vector.from_stream(data, game, property_size)
        trigger_pos = Vector.from_stream(data, game, property_size)
        effect_pos = Vector.from_stream(data, game, property_size)
        return cls(name, position, rotation, active, column, row, side, actor_pos, trigger_pos, effect_pos)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\n")  # 10 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_l.pack(self.column))
        data.write(structs.BIG_l.pack(self.row))
        self.side.to_stream(data, game)
        self.actor_pos.to_stream(data, game)
        self.trigger_pos.to_stream(data, game)
        self.effect_pos.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MazeNodeJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            column=json_data["column"],
            row=json_data["row"],
            side=Side.from_json(json_data["side"]),
            actor_pos=Vector.from_json(json_data["actor_pos"]),
            trigger_pos=Vector.from_json(json_data["trigger_pos"]),
            effect_pos=Vector.from_json(json_data["effect_pos"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "column": self.column,
            "row": self.row,
            "side": self.side.to_json(),
            "actor_pos": self.actor_pos.to_json(),
            "trigger_pos": self.trigger_pos.to_json(),
            "effect_pos": self.effect_pos.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
