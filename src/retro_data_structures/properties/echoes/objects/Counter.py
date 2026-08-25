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
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CounterJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        initial_count: int
        max_count: int
        auto_reset: bool
        wrap: bool


@dataclasses.dataclass()
class Counter(BaseObjectType):
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
    initial_count: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFD179A6F, original_name="Initial_Count"),
        },
    )
    max_count: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5B851589, original_name="Max_Count"),
        },
    )
    auto_reset: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7BEF45CA, original_name="AutoReset"),
        },
    )
    wrap: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF076CEF5, original_name="Wrap"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CNTR"

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
        assert property_id == 0xFD179A6F
        initial_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B851589
        max_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7BEF45CA
        auto_reset = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF076CEF5
        wrap = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(editor_properties, initial_count, max_count, auto_reset, wrap)

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

        data.write(b"\xfd\x17\x9ao")  # 0xfd179a6f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.initial_count))

        data.write(b"[\x85\x15\x89")  # 0x5b851589
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_count))

        data.write(b"{\xefE\xca")  # 0x7bef45ca
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_reset))

        data.write(b"\xf0v\xce\xf5")  # 0xf076cef5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.wrap))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CounterJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            initial_count=json_data["initial_count"],
            max_count=json_data["max_count"],
            auto_reset=json_data["auto_reset"],
            wrap=json_data["wrap"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "initial_count": self.initial_count,
            "max_count": self.max_count,
            "auto_reset": self.auto_reset,
            "wrap": self.wrap,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xFD179A6F: ("initial_count", structs.decode_BIG_l),
    0x5B851589: ("max_count", structs.decode_BIG_l),
    0x7BEF45CA: ("auto_reset", structs.decode_BIG_bool_),
    0xF076CEF5: ("wrap", structs.decode_BIG_bool_),
}
