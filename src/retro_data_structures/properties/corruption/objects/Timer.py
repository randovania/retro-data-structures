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
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TimerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        time: float
        random_adjust: float
        auto_start: bool
        loop: bool


@dataclasses.dataclass()
class Timer(BaseObjectType):
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
    time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x44335AFF, original_name="Time"),
        },
    )
    random_adjust: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3AD39B31, original_name="RandomAdjust"),
        },
    )
    auto_start: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3217DFF8, original_name="AutoStart"),
        },
    )
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEDA47FF6, original_name="Loop"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "TIMR"

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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44335AFF
        time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AD39B31
        random_adjust = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3217DFF8
        auto_start = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA47FF6
        loop = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(editor_properties, time, random_adjust, auto_start, loop)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"D3Z\xff")  # 0x44335aff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time))

        data.write(b":\xd3\x9b1")  # 0x3ad39b31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.random_adjust))

        data.write(b"2\x17\xdf\xf8")  # 0x3217dff8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_start))

        data.write(b"\xed\xa4\x7f\xf6")  # 0xeda47ff6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.loop))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TimerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            time=json_data["time"],
            random_adjust=json_data["random_adjust"],
            auto_start=json_data["auto_start"],
            loop=json_data["loop"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "time": self.time,
            "random_adjust": self.random_adjust,
            "auto_start": self.auto_start,
            "loop": self.loop,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x44335AFF: ("time", structs.decode_BIG_f),
    0x3AD39B31: ("random_adjust", structs.decode_BIG_f),
    0x3217DFF8: ("auto_start", structs.decode_BIG_bool_),
    0xEDA47FF6: ("loop", structs.decode_BIG_bool_),
}
