# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GhorStructA import GhorStructA
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct35Json(typing_extensions.TypedDict):
        ghor_struct_a_0x8b5db983: json_util.JsonObject
        ghor_struct_a_0x04cdc6a6: json_util.JsonObject
        ghor_struct_a_0xe451d02c: json_util.JsonObject
        ghor_struct_a_0x72f708f2: json_util.JsonObject
        ghor_struct_a_0x8cb41734: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct35(BaseProperty):
    ghor_struct_a_0x8b5db983: GhorStructA = dataclasses.field(
        default_factory=GhorStructA,
        metadata={
            "reflection": FieldReflection[GhorStructA](
                GhorStructA,
                id=0x8B5DB983,
                original_name="GhorStructA",
                from_json=GhorStructA.from_json,
                to_json=GhorStructA.to_json,
            ),
        },
    )
    ghor_struct_a_0x04cdc6a6: GhorStructA = dataclasses.field(
        default_factory=GhorStructA,
        metadata={
            "reflection": FieldReflection[GhorStructA](
                GhorStructA,
                id=0x04CDC6A6,
                original_name="GhorStructA",
                from_json=GhorStructA.from_json,
                to_json=GhorStructA.to_json,
            ),
        },
    )
    ghor_struct_a_0xe451d02c: GhorStructA = dataclasses.field(
        default_factory=GhorStructA,
        metadata={
            "reflection": FieldReflection[GhorStructA](
                GhorStructA,
                id=0xE451D02C,
                original_name="GhorStructA",
                from_json=GhorStructA.from_json,
                to_json=GhorStructA.to_json,
            ),
        },
    )
    ghor_struct_a_0x72f708f2: GhorStructA = dataclasses.field(
        default_factory=GhorStructA,
        metadata={
            "reflection": FieldReflection[GhorStructA](
                GhorStructA,
                id=0x72F708F2,
                original_name="GhorStructA",
                from_json=GhorStructA.from_json,
                to_json=GhorStructA.to_json,
            ),
        },
    )
    ghor_struct_a_0x8cb41734: GhorStructA = dataclasses.field(
        default_factory=GhorStructA,
        metadata={
            "reflection": FieldReflection[GhorStructA](
                GhorStructA,
                id=0x8CB41734,
                original_name="GhorStructA",
                from_json=GhorStructA.from_json,
                to_json=GhorStructA.to_json,
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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B5DB983
        ghor_struct_a_0x8b5db983 = GhorStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04CDC6A6
        ghor_struct_a_0x04cdc6a6 = GhorStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE451D02C
        ghor_struct_a_0xe451d02c = GhorStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72F708F2
        ghor_struct_a_0x72f708f2 = GhorStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8CB41734
        ghor_struct_a_0x8cb41734 = GhorStructA.from_stream(data, game, property_size)

        return cls(
            ghor_struct_a_0x8b5db983,
            ghor_struct_a_0x04cdc6a6,
            ghor_struct_a_0xe451d02c,
            ghor_struct_a_0x72f708f2,
            ghor_struct_a_0x8cb41734,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"\x8b]\xb9\x83")  # 0x8b5db983
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_a_0x8b5db983.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x04\xcd\xc6\xa6")  # 0x4cdc6a6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_a_0x04cdc6a6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe4Q\xd0,")  # 0xe451d02c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_a_0xe451d02c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"r\xf7\x08\xf2")  # 0x72f708f2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_a_0x72f708f2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8c\xb4\x174")  # 0x8cb41734
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ghor_struct_a_0x8cb41734.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct35Json", data)
        return cls(
            ghor_struct_a_0x8b5db983=GhorStructA.from_json(json_data["ghor_struct_a_0x8b5db983"]),
            ghor_struct_a_0x04cdc6a6=GhorStructA.from_json(json_data["ghor_struct_a_0x04cdc6a6"]),
            ghor_struct_a_0xe451d02c=GhorStructA.from_json(json_data["ghor_struct_a_0xe451d02c"]),
            ghor_struct_a_0x72f708f2=GhorStructA.from_json(json_data["ghor_struct_a_0x72f708f2"]),
            ghor_struct_a_0x8cb41734=GhorStructA.from_json(json_data["ghor_struct_a_0x8cb41734"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "ghor_struct_a_0x8b5db983": self.ghor_struct_a_0x8b5db983.to_json(),
            "ghor_struct_a_0x04cdc6a6": self.ghor_struct_a_0x04cdc6a6.to_json(),
            "ghor_struct_a_0xe451d02c": self.ghor_struct_a_0xe451d02c.to_json(),
            "ghor_struct_a_0x72f708f2": self.ghor_struct_a_0x72f708f2.to_json(),
            "ghor_struct_a_0x8cb41734": self.ghor_struct_a_0x8cb41734.to_json(),
        }


def _decode_ghor_struct_a_0x8b5db983(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructA:
    return GhorStructA.from_stream(data, game, property_size)


def _decode_ghor_struct_a_0x04cdc6a6(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructA:
    return GhorStructA.from_stream(data, game, property_size)


def _decode_ghor_struct_a_0xe451d02c(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructA:
    return GhorStructA.from_stream(data, game, property_size)


def _decode_ghor_struct_a_0x72f708f2(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructA:
    return GhorStructA.from_stream(data, game, property_size)


def _decode_ghor_struct_a_0x8cb41734(data: typing.BinaryIO, game: Game, property_size: int) -> GhorStructA:
    return GhorStructA.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8B5DB983: ("ghor_struct_a_0x8b5db983", _decode_ghor_struct_a_0x8b5db983),
    0x04CDC6A6: ("ghor_struct_a_0x04cdc6a6", _decode_ghor_struct_a_0x04cdc6a6),
    0xE451D02C: ("ghor_struct_a_0xe451d02c", _decode_ghor_struct_a_0xe451d02c),
    0x72F708F2: ("ghor_struct_a_0x72f708f2", _decode_ghor_struct_a_0x72f708f2),
    0x8CB41734: ("ghor_struct_a_0x8cb41734", _decode_ghor_struct_a_0x8cb41734),
}
