# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.UnknownStruct54 import UnknownStruct54
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class RoomAcousticsJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        priority: int
        unknown_struct54: json_util.JsonObject


class Priority(enum.IntEnum):
    Unknown1 = 477433555
    Unknown2 = 984224020
    Unknown3 = 3559813316
    Unknown4 = 464330772
    Unknown5 = 2642601662

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
class RoomAcoustics(BaseObjectType):
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
    priority: Priority = dataclasses.field(
        default=Priority.Unknown2,
        metadata={
            "reflection": FieldReflection[Priority](
                Priority,
                id=0x0BE7CA9E,
                original_name="Priority",
                from_json=Priority.from_json,
                to_json=Priority.to_json,
            ),
        },
    )
    unknown_struct54: UnknownStruct54 = dataclasses.field(
        default_factory=UnknownStruct54,
        metadata={
            "reflection": FieldReflection[UnknownStruct54](
                UnknownStruct54,
                id=0x555B055E,
                original_name="UnknownStruct54",
                from_json=UnknownStruct54.from_json,
                to_json=UnknownStruct54.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "RMAC"

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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BE7CA9E
        priority = Priority.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x555B055E
        unknown_struct54 = UnknownStruct54.from_stream(data, game, property_size)

        return cls(editor_properties, priority, unknown_struct54)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0b\xe7\xca\x9e")  # 0xbe7ca9e
        data.write(b"\x00\x04")  # size
        self.priority.to_stream(data, game)

        data.write(b"U[\x05^")  # 0x555b055e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct54.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RoomAcousticsJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            priority=Priority.from_json(json_data["priority"]),
            unknown_struct54=UnknownStruct54.from_json(json_data["unknown_struct54"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "priority": self.priority.to_json(),
            "unknown_struct54": self.unknown_struct54.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_priority(data: typing.BinaryIO, game: Game, property_size: int) -> Priority:
    return Priority.from_stream(data, game)


def _decode_unknown_struct54(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct54:
    return UnknownStruct54.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x0BE7CA9E: ("priority", _decode_priority),
    0x555B055E: ("unknown_struct54", _decode_unknown_struct54),
}
