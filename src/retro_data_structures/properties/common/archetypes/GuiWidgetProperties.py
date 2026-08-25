# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GuiWidgetPropertiesJson(typing_extensions.TypedDict):
        gui_label: str
        controller_number: int
        is_locked: bool


@dataclasses.dataclass()
class GuiWidgetProperties(BaseProperty):
    gui_label: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x73939407, original_name="GuiLabel"),
        },
    )
    controller_number: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDB7F4AA2, original_name="ControllerNumber"),
        },
    )
    is_locked: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDEE730F5, original_name="IsLocked"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73939407
        gui_label = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDB7F4AA2
        controller_number = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDEE730F5
        is_locked = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(gui_label, controller_number, is_locked)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"s\x93\x94\x07")  # 0x73939407
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.gui_label.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdb\x7fJ\xa2")  # 0xdb7f4aa2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.controller_number))

        data.write(b"\xde\xe70\xf5")  # 0xdee730f5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_locked))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GuiWidgetPropertiesJson", data)
        return cls(
            gui_label=json_data["gui_label"],
            controller_number=json_data["controller_number"],
            is_locked=json_data["is_locked"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "gui_label": self.gui_label,
            "controller_number": self.controller_number,
            "is_locked": self.is_locked,
        }


def _decode_gui_label(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x73939407: ("gui_label", _decode_gui_label),
    0xDB7F4AA2: ("controller_number", structs.decode_BIG_l),
    0xDEE730F5: ("is_locked", structs.decode_BIG_bool_),
}
