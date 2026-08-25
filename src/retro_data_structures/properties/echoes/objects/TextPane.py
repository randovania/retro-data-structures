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
from retro_data_structures.properties.echoes.archetypes.TextProperties import TextProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TextPaneJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        gui_label: str
        text_properties: json_util.JsonObject
        japan_text_properties: json_util.JsonObject
        pivot_offset: json_util.JsonValue
        default_string: int
        default_string_name: str
        blend_mode: int
        fade_in_time: float
        fade_out_time: float
        depth_compare: bool
        depth_update: bool
        depth_backwards: bool


@dataclasses.dataclass()
class TextPane(BaseObjectType):
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
    gui_label: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x73939407, original_name="GuiLabel"),
        },
    )
    text_properties: TextProperties = dataclasses.field(
        default_factory=TextProperties,
        metadata={
            "reflection": FieldReflection[TextProperties](
                TextProperties,
                id=0xE0543E66,
                original_name="TextProperties",
                from_json=TextProperties.from_json,
                to_json=TextProperties.to_json,
            ),
        },
    )
    japan_text_properties: TextProperties = dataclasses.field(
        default_factory=TextProperties,
        metadata={
            "reflection": FieldReflection[TextProperties](
                TextProperties,
                id=0xC8E441FA,
                original_name="JapanTextProperties",
                from_json=TextProperties.from_json,
                to_json=TextProperties.to_json,
            ),
        },
    )
    pivot_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xDEF21BF5, original_name="PivotOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    default_string: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRG"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE7AC3927, original_name="DefaultString"),
        },
    )
    default_string_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xD501C87E, original_name="DefaultStringName"),
        },
    )
    blend_mode: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x94F0365C, original_name="Blend_Mode"),
        },
    )
    fade_in_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AA341F, original_name="FadeInTime"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7C269EBC, original_name="FadeOutTime"),
        },
    )
    depth_compare: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x94C01B0C, original_name="Depth_Compare"),
        },
    )
    depth_update: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAED25A51, original_name="Depth_Update"),
        },
    )
    depth_backwards: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x35DC43D0, original_name="Depth_Backwards"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "TXPN"

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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73939407
        gui_label = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0543E66
        text_properties = TextProperties.from_stream(
            data, game, property_size, default_override={"text_bounding_width": 80, "text_bounding_height": 10}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8E441FA
        japan_text_properties = TextProperties.from_stream(
            data, game, property_size, default_override={"text_bounding_width": 80, "text_bounding_height": 10}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDEF21BF5
        pivot_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7AC3927
        default_string = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD501C87E
        default_string_name = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94F0365C
        blend_mode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90AA341F
        fade_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C269EBC
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94C01B0C
        depth_compare = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAED25A51
        depth_update = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35DC43D0
        depth_backwards = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            gui_label,
            text_properties,
            japan_text_properties,
            pivot_offset,
            default_string,
            default_string_name,
            blend_mode,
            fade_in_time,
            fade_out_time,
            depth_compare,
            depth_update,
            depth_backwards,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0c")  # 12 properties
        num_properties_written = 12

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"s\x93\x94\x07")  # 0x73939407
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.gui_label.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe0T>f")  # 0xe0543e66
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.text_properties.to_stream(
            data, game, default_override={"text_bounding_width": 80, "text_bounding_height": 10}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.japan_text_properties != default_override.get("japan_text_properties", TextProperties()):
            num_properties_written += 1
            data.write(b"\xc8\xe4A\xfa")  # 0xc8e441fa
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.japan_text_properties.to_stream(
                data, game, default_override={"text_bounding_width": 80, "text_bounding_height": 10}
            )
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        data.write(b"\xde\xf2\x1b\xf5")  # 0xdef21bf5
        data.write(b"\x00\x0c")  # size
        self.pivot_offset.to_stream(data, game)

        data.write(b"\xe7\xac9'")  # 0xe7ac3927
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.default_string))

        data.write(b"\xd5\x01\xc8~")  # 0xd501c87e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.default_string_name.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x94\xf06\\")  # 0x94f0365c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.blend_mode))

        data.write(b"\x90\xaa4\x1f")  # 0x90aa341f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_time))

        data.write(b"|&\x9e\xbc")  # 0x7c269ebc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

        data.write(b"\x94\xc0\x1b\x0c")  # 0x94c01b0c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.depth_compare))

        data.write(b"\xae\xd2ZQ")  # 0xaed25a51
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.depth_update))

        data.write(b"5\xdcC\xd0")  # 0x35dc43d0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.depth_backwards))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TextPaneJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            gui_label=json_data["gui_label"],
            text_properties=TextProperties.from_json(json_data["text_properties"]),
            japan_text_properties=TextProperties.from_json(json_data["japan_text_properties"]),
            pivot_offset=Vector.from_json(json_data["pivot_offset"]),
            default_string=json_data["default_string"],
            default_string_name=json_data["default_string_name"],
            blend_mode=json_data["blend_mode"],
            fade_in_time=json_data["fade_in_time"],
            fade_out_time=json_data["fade_out_time"],
            depth_compare=json_data["depth_compare"],
            depth_update=json_data["depth_update"],
            depth_backwards=json_data["depth_backwards"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "gui_label": self.gui_label,
            "text_properties": self.text_properties.to_json(),
            "japan_text_properties": self.japan_text_properties.to_json(),
            "pivot_offset": self.pivot_offset.to_json(),
            "default_string": self.default_string,
            "default_string_name": self.default_string_name,
            "blend_mode": self.blend_mode,
            "fade_in_time": self.fade_in_time,
            "fade_out_time": self.fade_out_time,
            "depth_compare": self.depth_compare,
            "depth_update": self.depth_update,
            "depth_backwards": self.depth_backwards,
        }

    def _dependencies_for_default_string(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.default_string)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.text_properties.dependencies_for, "text_properties", "TextProperties"),
            (self.japan_text_properties.dependencies_for, "japan_text_properties", "TextProperties"),
            (self._dependencies_for_default_string, "default_string", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for TextPane.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_gui_label(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_text_properties(data: typing.BinaryIO, game: Game, property_size: int) -> TextProperties:
    return TextProperties.from_stream(
        data, game, property_size, default_override={"text_bounding_width": 80, "text_bounding_height": 10}
    )


def _decode_japan_text_properties(data: typing.BinaryIO, game: Game, property_size: int) -> TextProperties:
    return TextProperties.from_stream(
        data, game, property_size, default_override={"text_bounding_width": 80, "text_bounding_height": 10}
    )


def _decode_pivot_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_default_string_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x73939407: ("gui_label", _decode_gui_label),
    0xE0543E66: ("text_properties", _decode_text_properties),
    0xC8E441FA: ("japan_text_properties", _decode_japan_text_properties),
    0xDEF21BF5: ("pivot_offset", _decode_pivot_offset),
    0xE7AC3927: ("default_string", structs.decode_BIG_L),
    0xD501C87E: ("default_string_name", _decode_default_string_name),
    0x94F0365C: ("blend_mode", structs.decode_BIG_l),
    0x90AA341F: ("fade_in_time", structs.decode_BIG_f),
    0x7C269EBC: ("fade_out_time", structs.decode_BIG_f),
    0x94C01B0C: ("depth_compare", structs.decode_BIG_bool_),
    0xAED25A51: ("depth_update", structs.decode_BIG_bool_),
    0x35DC43D0: ("depth_backwards", structs.decode_BIG_bool_),
}
