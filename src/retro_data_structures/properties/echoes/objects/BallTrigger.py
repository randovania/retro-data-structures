# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.TriggerInfo import TriggerInfo
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class BallTriggerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        trigger: json_util.JsonObject
        attraction_force: float
        attraction_angle: float
        attraction_distance: float
        attraction_direction: json_util.JsonValue
        no_ball_movement: bool
        bounds_size_multiplier: float


@dataclasses.dataclass()
class BallTrigger(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    trigger: TriggerInfo = dataclasses.field(
        default_factory=TriggerInfo,
        metadata={
            "reflection": FieldReflection[TriggerInfo](
                TriggerInfo,
                id=0x77A27411,
                original_name="Trigger",
                from_json=TriggerInfo.from_json,
                to_json=TriggerInfo.to_json,
            ),
        },
    )
    attraction_force: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB61B1149, original_name="AttractionForce"),
        },
    )
    attraction_angle: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x81AF51D5, original_name="AttractionAngle"),
        },
    )
    attraction_distance: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBB38D077, original_name="AttractionDistance"),
        },
    )
    attraction_direction: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xEA511D83,
                original_name="AttractionDirection",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    no_ball_movement: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB613F4E4, original_name="NoBallMovement"),
        },
    )
    bounds_size_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2766636A, original_name="BoundsSizeMultiplier"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "BALT"

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 8:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77A27411
        trigger = TriggerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB61B1149
        attraction_force = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81AF51D5
        attraction_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB38D077
        attraction_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA511D83
        attraction_direction = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB613F4E4
        no_ball_movement = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2766636A
        bounds_size_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            trigger,
            attraction_force,
            attraction_angle,
            attraction_distance,
            attraction_direction,
            no_ball_movement,
            bounds_size_multiplier,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x07")  # 7 properties
        num_properties_written = 7

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\xa2t\x11")  # 0x77a27411
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.trigger.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb6\x1b\x11I")  # 0xb61b1149
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attraction_force))

        data.write(b"\x81\xafQ\xd5")  # 0x81af51d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attraction_angle))

        data.write(b"\xbb8\xd0w")  # 0xbb38d077
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attraction_distance))

        data.write(b"\xeaQ\x1d\x83")  # 0xea511d83
        data.write(b"\x00\x0c")  # size
        self.attraction_direction.to_stream(data, game)

        data.write(b"\xb6\x13\xf4\xe4")  # 0xb613f4e4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.no_ball_movement))

        if self.bounds_size_multiplier != default_override.get("bounds_size_multiplier", 1.0):
            num_properties_written += 1
            data.write(b"'fcj")  # 0x2766636a
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.bounds_size_multiplier))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BallTriggerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            trigger=TriggerInfo.from_json(json_data["trigger"]),
            attraction_force=json_data["attraction_force"],
            attraction_angle=json_data["attraction_angle"],
            attraction_distance=json_data["attraction_distance"],
            attraction_direction=Vector.from_json(json_data["attraction_direction"]),
            no_ball_movement=json_data["no_ball_movement"],
            bounds_size_multiplier=json_data["bounds_size_multiplier"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "trigger": self.trigger.to_json(),
            "attraction_force": self.attraction_force,
            "attraction_angle": self.attraction_angle,
            "attraction_distance": self.attraction_distance,
            "attraction_direction": self.attraction_direction.to_json(),
            "no_ball_movement": self.no_ball_movement,
            "bounds_size_multiplier": self.bounds_size_multiplier,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_trigger(data: typing.BinaryIO, game: Game, property_size: int) -> TriggerInfo:
    return TriggerInfo.from_stream(data, game, property_size)


def _decode_attraction_direction(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x77A27411: ("trigger", _decode_trigger),
    0xB61B1149: ("attraction_force", structs.decode_BIG_f),
    0x81AF51D5: ("attraction_angle", structs.decode_BIG_f),
    0xBB38D077: ("attraction_distance", structs.decode_BIG_f),
    0xEA511D83: ("attraction_direction", _decode_attraction_direction),
    0xB613F4E4: ("no_ball_movement", structs.decode_BIG_bool_),
    0x2766636A: ("bounds_size_multiplier", structs.decode_BIG_f),
}
