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

    class DockJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        dock_number: int
        area_number: int
        is_virtual: bool
        load_connected_immediate: bool
        show_soft_transition: bool


@dataclasses.dataclass()
class Dock(BaseObjectType):
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
    dock_number: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1101E91B, original_name="DockNumber"),
        },
    )
    area_number: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x610EEC90, original_name="AreaNumber"),
        },
    )
    is_virtual: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x870E6D6F, original_name="IsVirtual"),
        },
    )
    load_connected_immediate: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF3839D6F, original_name="LoadConnectedImmediate"),
        },
    )
    show_soft_transition: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x222D9DAF, original_name="ShowSoftTransition"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DOCK"

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
        if property_count != 6:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1101E91B
        dock_number = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x610EEC90
        area_number = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x870E6D6F
        is_virtual = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3839D6F
        load_connected_immediate = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x222D9DAF
        show_soft_transition = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties, dock_number, area_number, is_virtual, load_connected_immediate, show_soft_transition
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x11\x01\xe9\x1b")  # 0x1101e91b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dock_number))

        data.write(b"a\x0e\xec\x90")  # 0x610eec90
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.area_number))

        data.write(b"\x87\x0emo")  # 0x870e6d6f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_virtual))

        data.write(b"\xf3\x83\x9do")  # 0xf3839d6f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.load_connected_immediate))

        data.write(b'"-\x9d\xaf')  # 0x222d9daf
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.show_soft_transition))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DockJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            dock_number=json_data["dock_number"],
            area_number=json_data["area_number"],
            is_virtual=json_data["is_virtual"],
            load_connected_immediate=json_data["load_connected_immediate"],
            show_soft_transition=json_data["show_soft_transition"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "dock_number": self.dock_number,
            "area_number": self.area_number,
            "is_virtual": self.is_virtual,
            "load_connected_immediate": self.load_connected_immediate,
            "show_soft_transition": self.show_soft_transition,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x1101E91B: ("dock_number", structs.decode_BIG_l),
    0x610EEC90: ("area_number", structs.decode_BIG_l),
    0x870E6D6F: ("is_virtual", structs.decode_BIG_bool_),
    0xF3839D6F: ("load_connected_immediate", structs.decode_BIG_bool_),
    0x222D9DAF: ("show_soft_transition", structs.decode_BIG_bool_),
}
