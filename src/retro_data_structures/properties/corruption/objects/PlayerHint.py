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
from retro_data_structures.properties.corruption.archetypes.InterpolationMethod import InterpolationMethod
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PlayerHintJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        priority: int
        timer: float
        flags_player_hint: int
        unknown_0xb2367a60: float
        unknown_0x68d9122a: float
        control_frame_interpolation: json_util.JsonObject


@dataclasses.dataclass()
class PlayerHint(BaseObjectType):
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
    priority: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42087650, original_name="Priority"),
        },
    )
    timer: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8747552E, original_name="Timer"),
        },
    )
    flags_player_hint: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1BCE57E1, original_name="FlagsPlayerHint"),
        },
    )  # Flagset
    unknown_0xb2367a60: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB2367A60, original_name="Unknown"),
        },
    )
    unknown_0x68d9122a: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x68D9122A, original_name="Unknown"),
        },
    )
    control_frame_interpolation: InterpolationMethod = dataclasses.field(
        default_factory=InterpolationMethod,
        metadata={
            "reflection": FieldReflection[InterpolationMethod](
                InterpolationMethod,
                id=0x95D0D437,
                original_name="ControlFrameInterpolation",
                from_json=InterpolationMethod.from_json,
                to_json=InterpolationMethod.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "HINT"

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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42087650
        priority = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8747552E
        timer = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1BCE57E1
        flags_player_hint = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2367A60
        unknown_0xb2367a60 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68D9122A
        unknown_0x68d9122a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95D0D437
        control_frame_interpolation = InterpolationMethod.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            priority,
            timer,
            flags_player_hint,
            unknown_0xb2367a60,
            unknown_0x68d9122a,
            control_frame_interpolation,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"B\x08vP")  # 0x42087650
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.priority))

        data.write(b"\x87GU.")  # 0x8747552e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.timer))

        data.write(b"\x1b\xceW\xe1")  # 0x1bce57e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_player_hint))

        data.write(b"\xb26z`")  # 0xb2367a60
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb2367a60))

        data.write(b"h\xd9\x12*")  # 0x68d9122a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x68d9122a))

        data.write(b"\x95\xd0\xd47")  # 0x95d0d437
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.control_frame_interpolation.to_stream(data, game)
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
        json_data = typing.cast("PlayerHintJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            priority=json_data["priority"],
            timer=json_data["timer"],
            flags_player_hint=json_data["flags_player_hint"],
            unknown_0xb2367a60=json_data["unknown_0xb2367a60"],
            unknown_0x68d9122a=json_data["unknown_0x68d9122a"],
            control_frame_interpolation=InterpolationMethod.from_json(json_data["control_frame_interpolation"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "priority": self.priority,
            "timer": self.timer,
            "flags_player_hint": self.flags_player_hint,
            "unknown_0xb2367a60": self.unknown_0xb2367a60,
            "unknown_0x68d9122a": self.unknown_0x68d9122a,
            "control_frame_interpolation": self.control_frame_interpolation.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_control_frame_interpolation(data: typing.BinaryIO, game: Game, property_size: int) -> InterpolationMethod:
    return InterpolationMethod.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x42087650: ("priority", structs.decode_BIG_l),
    0x8747552E: ("timer", structs.decode_BIG_f),
    0x1BCE57E1: ("flags_player_hint", structs.decode_BIG_L),
    0xB2367A60: ("unknown_0xb2367a60", structs.decode_BIG_f),
    0x68D9122A: ("unknown_0x68d9122a", structs.decode_BIG_f),
    0x95D0D437: ("control_frame_interpolation", _decode_control_frame_interpolation),
}
