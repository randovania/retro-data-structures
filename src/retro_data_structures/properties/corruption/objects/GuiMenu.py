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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GuiMenuJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        text: int
        choice0_enabled: bool
        choice1_enabled: bool
        choice2_enabled: bool
        choice3_enabled: bool
        cancel_enabled: bool


@dataclasses.dataclass()
class GuiMenu(BaseObjectType):
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
    text: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRG"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x25FA292E, original_name="Text"),
        },
    )
    choice0_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x940BFB9E, original_name="Choice0Enabled"),
        },
    )
    choice1_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0FAEB7F1, original_name="Choice1Enabled"),
        },
    )
    choice2_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x78306501, original_name="Choice2Enabled"),
        },
    )
    choice3_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE395296E, original_name="Choice3Enabled"),
        },
    )
    cancel_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x732FA0B0, original_name="CancelEnabled"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "GMNU"

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
        assert property_id == 0x25FA292E
        text = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x940BFB9E
        choice0_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FAEB7F1
        choice1_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78306501
        choice2_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE395296E
        choice3_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x732FA0B0
        cancel_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties, text, choice0_enabled, choice1_enabled, choice2_enabled, choice3_enabled, cancel_enabled
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

        data.write(b"%\xfa).")  # 0x25fa292e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.text))

        data.write(b"\x94\x0b\xfb\x9e")  # 0x940bfb9e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.choice0_enabled))

        data.write(b"\x0f\xae\xb7\xf1")  # 0xfaeb7f1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.choice1_enabled))

        data.write(b"x0e\x01")  # 0x78306501
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.choice2_enabled))

        data.write(b"\xe3\x95)n")  # 0xe395296e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.choice3_enabled))

        data.write(b"s/\xa0\xb0")  # 0x732fa0b0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.cancel_enabled))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GuiMenuJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            text=json_data["text"],
            choice0_enabled=json_data["choice0_enabled"],
            choice1_enabled=json_data["choice1_enabled"],
            choice2_enabled=json_data["choice2_enabled"],
            choice3_enabled=json_data["choice3_enabled"],
            cancel_enabled=json_data["cancel_enabled"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "text": self.text,
            "choice0_enabled": self.choice0_enabled,
            "choice1_enabled": self.choice1_enabled,
            "choice2_enabled": self.choice2_enabled,
            "choice3_enabled": self.choice3_enabled,
            "cancel_enabled": self.cancel_enabled,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x25FA292E: ("text", structs.decode_BIG_Q),
    0x940BFB9E: ("choice0_enabled", structs.decode_BIG_bool_),
    0x0FAEB7F1: ("choice1_enabled", structs.decode_BIG_bool_),
    0x78306501: ("choice2_enabled", structs.decode_BIG_bool_),
    0xE395296E: ("choice3_enabled", structs.decode_BIG_bool_),
    0x732FA0B0: ("cancel_enabled", structs.decode_BIG_bool_),
}
