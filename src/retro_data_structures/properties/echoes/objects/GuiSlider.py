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
from retro_data_structures.properties.common.archetypes.GuiWidgetProperties import GuiWidgetProperties
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class GuiSliderJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        gui_widget_properties: json_util.JsonObject
        min_value: float
        max_value: float
        increment: float
        slide_speed: float
        slide_sound: int
        slide_sound_volume: int


@dataclasses.dataclass()
class GuiSlider(BaseObjectType):
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
    gui_widget_properties: GuiWidgetProperties = dataclasses.field(
        default_factory=GuiWidgetProperties,
        metadata={
            "reflection": FieldReflection[GuiWidgetProperties](
                GuiWidgetProperties,
                id=0x91CEFA1E,
                original_name="GuiWidgetProperties",
                from_json=GuiWidgetProperties.from_json,
                to_json=GuiWidgetProperties.to_json,
            ),
        },
    )
    min_value: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2CCBBDFE, original_name="MinValue"),
        },
    )
    max_value: float = dataclasses.field(
        default=255.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C84C588, original_name="MaxValue"),
        },
    )
    increment: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A68DB52, original_name="Increment"),
        },
    )
    slide_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEDB6062B, original_name="SlideSpeed"),
        },
    )
    slide_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xD158734B, original_name="SlideSound"),
        },
    )
    slide_sound_volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x20DDB661, original_name="SlideSoundVolume"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "GSLD"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptGui.rel"]

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
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={"active": False})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91CEFA1E
        gui_widget_properties = GuiWidgetProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CCBBDFE
        min_value = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C84C588
        max_value = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A68DB52
        increment = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDB6062B
        slide_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD158734B
        slide_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20DDB661
        slide_sound_volume = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            gui_widget_properties,
            min_value,
            max_value,
            increment,
            slide_speed,
            slide_sound,
            slide_sound_volume,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={"active": False})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x91\xce\xfa\x1e")  # 0x91cefa1e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.gui_widget_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b",\xcb\xbd\xfe")  # 0x2ccbbdfe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_value))

        data.write(b"l\x84\xc5\x88")  # 0x6c84c588
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_value))

        data.write(b"\x8ah\xdbR")  # 0x8a68db52
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.increment))

        data.write(b"\xed\xb6\x06+")  # 0xedb6062b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.slide_speed))

        data.write(b"\xd1XsK")  # 0xd158734b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.slide_sound))

        data.write(b" \xdd\xb6a")  # 0x20ddb661
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.slide_sound_volume))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GuiSliderJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            gui_widget_properties=GuiWidgetProperties.from_json(json_data["gui_widget_properties"]),
            min_value=json_data["min_value"],
            max_value=json_data["max_value"],
            increment=json_data["increment"],
            slide_speed=json_data["slide_speed"],
            slide_sound=json_data["slide_sound"],
            slide_sound_volume=json_data["slide_sound_volume"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "gui_widget_properties": self.gui_widget_properties.to_json(),
            "min_value": self.min_value,
            "max_value": self.max_value,
            "increment": self.increment,
            "slide_speed": self.slide_speed,
            "slide_sound": self.slide_sound,
            "slide_sound_volume": self.slide_sound_volume,
        }

    def _dependencies_for_slide_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.slide_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_slide_sound(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={"active": False})


def _decode_gui_widget_properties(data: typing.BinaryIO, game: Game, property_size: int) -> GuiWidgetProperties:
    return GuiWidgetProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x91CEFA1E: ("gui_widget_properties", _decode_gui_widget_properties),
    0x2CCBBDFE: ("min_value", structs.decode_BIG_f),
    0x6C84C588: ("max_value", structs.decode_BIG_f),
    0x8A68DB52: ("increment", structs.decode_BIG_f),
    0xEDB6062B: ("slide_speed", structs.decode_BIG_f),
    0xD158734B: ("slide_sound", structs.decode_BIG_l),
    0x20DDB661: ("slide_sound_volume", structs.decode_BIG_l),
}
