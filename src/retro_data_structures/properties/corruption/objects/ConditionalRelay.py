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
from retro_data_structures.properties.corruption.archetypes.ConditionalTest import ConditionalTest
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ConditionalRelayJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        trigger_on_first_think: bool
        multiplayer_mask_and_negate: int
        conditional1: json_util.JsonObject
        conditional2: json_util.JsonObject
        conditional3: json_util.JsonObject
        conditional4: json_util.JsonObject


@dataclasses.dataclass()
class ConditionalRelay(BaseObjectType):
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
    trigger_on_first_think: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x44DB8AF2, original_name="Trigger on first Think"),
        },
    )
    multiplayer_mask_and_negate: int = dataclasses.field(
        default=7,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2CC54E77, original_name="Multiplayer Mask and Negate"),
        },
    )  # Choice
    conditional1: ConditionalTest = dataclasses.field(
        default_factory=ConditionalTest,
        metadata={
            "reflection": FieldReflection[ConditionalTest](
                ConditionalTest,
                id=0xCEC16932,
                original_name="Conditional1",
                from_json=ConditionalTest.from_json,
                to_json=ConditionalTest.to_json,
            ),
        },
    )
    conditional2: ConditionalTest = dataclasses.field(
        default_factory=ConditionalTest,
        metadata={
            "reflection": FieldReflection[ConditionalTest](
                ConditionalTest,
                id=0xE709DDC0,
                original_name="Conditional2",
                from_json=ConditionalTest.from_json,
                to_json=ConditionalTest.to_json,
            ),
        },
    )
    conditional3: ConditionalTest = dataclasses.field(
        default_factory=ConditionalTest,
        metadata={
            "reflection": FieldReflection[ConditionalTest](
                ConditionalTest,
                id=0x49614C51,
                original_name="Conditional3",
                from_json=ConditionalTest.from_json,
                to_json=ConditionalTest.to_json,
            ),
        },
    )
    conditional4: ConditionalTest = dataclasses.field(
        default_factory=ConditionalTest,
        metadata={
            "reflection": FieldReflection[ConditionalTest](
                ConditionalTest,
                id=0xB498B424,
                original_name="Conditional4",
                from_json=ConditionalTest.from_json,
                to_json=ConditionalTest.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CRLY"

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
        assert property_id == 0x44DB8AF2
        trigger_on_first_think = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CC54E77
        multiplayer_mask_and_negate = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEC16932
        conditional1 = ConditionalTest.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE709DDC0
        conditional2 = ConditionalTest.from_stream(data, game, property_size, default_override={"boolean": 0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49614C51
        conditional3 = ConditionalTest.from_stream(data, game, property_size, default_override={"boolean": 0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB498B424
        conditional4 = ConditionalTest.from_stream(data, game, property_size, default_override={"boolean": 0})

        return cls(
            editor_properties,
            trigger_on_first_think,
            multiplayer_mask_and_negate,
            conditional1,
            conditional2,
            conditional3,
            conditional4,
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

        data.write(b"D\xdb\x8a\xf2")  # 0x44db8af2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.trigger_on_first_think))

        data.write(b",\xc5Nw")  # 0x2cc54e77
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.multiplayer_mask_and_negate))

        data.write(b"\xce\xc1i2")  # 0xcec16932
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.conditional1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7\t\xdd\xc0")  # 0xe709ddc0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.conditional2.to_stream(data, game, default_override={"boolean": 0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"IaLQ")  # 0x49614c51
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.conditional3.to_stream(data, game, default_override={"boolean": 0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb4\x98\xb4$")  # 0xb498b424
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.conditional4.to_stream(data, game, default_override={"boolean": 0})
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
        json_data = typing.cast("ConditionalRelayJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            trigger_on_first_think=json_data["trigger_on_first_think"],
            multiplayer_mask_and_negate=json_data["multiplayer_mask_and_negate"],
            conditional1=ConditionalTest.from_json(json_data["conditional1"]),
            conditional2=ConditionalTest.from_json(json_data["conditional2"]),
            conditional3=ConditionalTest.from_json(json_data["conditional3"]),
            conditional4=ConditionalTest.from_json(json_data["conditional4"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "trigger_on_first_think": self.trigger_on_first_think,
            "multiplayer_mask_and_negate": self.multiplayer_mask_and_negate,
            "conditional1": self.conditional1.to_json(),
            "conditional2": self.conditional2.to_json(),
            "conditional3": self.conditional3.to_json(),
            "conditional4": self.conditional4.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_conditional1(data: typing.BinaryIO, game: Game, property_size: int) -> ConditionalTest:
    return ConditionalTest.from_stream(data, game, property_size)


def _decode_conditional2(data: typing.BinaryIO, game: Game, property_size: int) -> ConditionalTest:
    return ConditionalTest.from_stream(data, game, property_size, default_override={"boolean": 0})


def _decode_conditional3(data: typing.BinaryIO, game: Game, property_size: int) -> ConditionalTest:
    return ConditionalTest.from_stream(data, game, property_size, default_override={"boolean": 0})


def _decode_conditional4(data: typing.BinaryIO, game: Game, property_size: int) -> ConditionalTest:
    return ConditionalTest.from_stream(data, game, property_size, default_override={"boolean": 0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x44DB8AF2: ("trigger_on_first_think", structs.decode_BIG_bool_),
    0x2CC54E77: ("multiplayer_mask_and_negate", structs.decode_BIG_L),
    0xCEC16932: ("conditional1", _decode_conditional1),
    0xE709DDC0: ("conditional2", _decode_conditional2),
    0x49614C51: ("conditional3", _decode_conditional3),
    0xB498B424: ("conditional4", _decode_conditional4),
}
