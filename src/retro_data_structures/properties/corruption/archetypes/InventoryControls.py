# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class InventoryControlsJson(typing_extensions.TypedDict):
        unknown_0x340f912e: json_util.JsonObject
        menu_up: json_util.JsonObject
        menu_down: json_util.JsonObject
        menu_left: json_util.JsonObject
        menu_right: json_util.JsonObject
        menu_select: json_util.JsonObject
        unknown_0x68ea537d: json_util.JsonObject


@dataclasses.dataclass()
class InventoryControls(BaseProperty):
    unknown_0x340f912e: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x340F912E,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    menu_up: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x769909C1,
                original_name="MenuUp",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    menu_down: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x4DAB695E,
                original_name="MenuDown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    menu_left: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xC7CAE2D3,
                original_name="MenuLeft",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    menu_right: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x1595F276,
                original_name="MenuRight",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    menu_select: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xBF09B38B,
                original_name="MenuSelect",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x68ea537d: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x68EA537D,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x340F912E
        unknown_0x340f912e = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x769909C1
        menu_up = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4DAB695E
        menu_down = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7CAE2D3
        menu_left = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1595F276
        menu_right = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF09B38B
        menu_select = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68EA537D
        unknown_0x68ea537d = RevolutionControl.from_stream(data, game, property_size)

        return cls(unknown_0x340f912e, menu_up, menu_down, menu_left, menu_right, menu_select, unknown_0x68ea537d)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"4\x0f\x91.")  # 0x340f912e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x340f912e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"v\x99\t\xc1")  # 0x769909c1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.menu_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"M\xabi^")  # 0x4dab695e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.menu_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc7\xca\xe2\xd3")  # 0xc7cae2d3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.menu_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x15\x95\xf2v")  # 0x1595f276
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.menu_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbf\t\xb3\x8b")  # 0xbf09b38b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.menu_select.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"h\xeaS}")  # 0x68ea537d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x68ea537d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("InventoryControlsJson", data)
        return cls(
            unknown_0x340f912e=RevolutionControl.from_json(json_data["unknown_0x340f912e"]),
            menu_up=RevolutionControl.from_json(json_data["menu_up"]),
            menu_down=RevolutionControl.from_json(json_data["menu_down"]),
            menu_left=RevolutionControl.from_json(json_data["menu_left"]),
            menu_right=RevolutionControl.from_json(json_data["menu_right"]),
            menu_select=RevolutionControl.from_json(json_data["menu_select"]),
            unknown_0x68ea537d=RevolutionControl.from_json(json_data["unknown_0x68ea537d"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x340f912e": self.unknown_0x340f912e.to_json(),
            "menu_up": self.menu_up.to_json(),
            "menu_down": self.menu_down.to_json(),
            "menu_left": self.menu_left.to_json(),
            "menu_right": self.menu_right.to_json(),
            "menu_select": self.menu_select.to_json(),
            "unknown_0x68ea537d": self.unknown_0x68ea537d.to_json(),
        }


def _decode_unknown_0x340f912e(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_select(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x68ea537d(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x340F912E: ("unknown_0x340f912e", _decode_unknown_0x340f912e),
    0x769909C1: ("menu_up", _decode_menu_up),
    0x4DAB695E: ("menu_down", _decode_menu_down),
    0xC7CAE2D3: ("menu_left", _decode_menu_left),
    0x1595F276: ("menu_right", _decode_menu_right),
    0xBF09B38B: ("menu_select", _decode_menu_select),
    0x68EA537D: ("unknown_0x68ea537d", _decode_unknown_0x68ea537d),
}
