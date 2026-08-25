# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CounterConditionsJson(typing_extensions.TypedDict):
        counter_condition1: int
        counter_condition2: int
        counter_condition3: int
        counter_condition4: int
        counter_condition5: int
        counter_condition6: int
        counter_condition7: int
        counter_condition8: int
        counter_condition9: int
        counter_condition10: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x1628F23A,
    0x49D5DD4,
    0xBC213AB1,
    0x21F60208,
    0x994A656D,
    0x8BFFCA83,
    0x3343ADE6,
    0x6B20BDB0,
    0xD39CDAD5,
    0x9215E813,
)


@dataclasses.dataclass()
class CounterConditions(BaseProperty):
    counter_condition1: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1628F23A, original_name="CounterCondition1"),
        },
    )
    counter_condition2: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x049D5DD4, original_name="CounterCondition2"),
        },
    )
    counter_condition3: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBC213AB1, original_name="CounterCondition3"),
        },
    )
    counter_condition4: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x21F60208, original_name="CounterCondition4"),
        },
    )
    counter_condition5: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x994A656D, original_name="CounterCondition5"),
        },
    )
    counter_condition6: int = dataclasses.field(
        default=6,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8BFFCA83, original_name="CounterCondition6"),
        },
    )
    counter_condition7: int = dataclasses.field(
        default=7,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3343ADE6, original_name="CounterCondition7"),
        },
    )
    counter_condition8: int = dataclasses.field(
        default=8,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6B20BDB0, original_name="CounterCondition8"),
        },
    )
    counter_condition9: int = dataclasses.field(
        default=9,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD39CDAD5, original_name="CounterCondition9"),
        },
    )
    counter_condition10: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9215E813, original_name="CounterCondition10"),
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
        if property_count != 10:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHlLHlLHlLHlLHlLHlLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(100))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\x16(\xf2:")  # 0x1628f23a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition1))

        data.write(b"\x04\x9d]\xd4")  # 0x49d5dd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition2))

        data.write(b"\xbc!:\xb1")  # 0xbc213ab1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition3))

        data.write(b"!\xf6\x02\x08")  # 0x21f60208
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition4))

        data.write(b"\x99Jem")  # 0x994a656d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition5))

        data.write(b"\x8b\xff\xca\x83")  # 0x8bffca83
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition6))

        data.write(b"3C\xad\xe6")  # 0x3343ade6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition7))

        data.write(b"k \xbd\xb0")  # 0x6b20bdb0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition8))

        data.write(b"\xd3\x9c\xda\xd5")  # 0xd39cdad5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition9))

        data.write(b"\x92\x15\xe8\x13")  # 0x9215e813
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.counter_condition10))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CounterConditionsJson", data)
        return cls(
            counter_condition1=json_data["counter_condition1"],
            counter_condition2=json_data["counter_condition2"],
            counter_condition3=json_data["counter_condition3"],
            counter_condition4=json_data["counter_condition4"],
            counter_condition5=json_data["counter_condition5"],
            counter_condition6=json_data["counter_condition6"],
            counter_condition7=json_data["counter_condition7"],
            counter_condition8=json_data["counter_condition8"],
            counter_condition9=json_data["counter_condition9"],
            counter_condition10=json_data["counter_condition10"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "counter_condition1": self.counter_condition1,
            "counter_condition2": self.counter_condition2,
            "counter_condition3": self.counter_condition3,
            "counter_condition4": self.counter_condition4,
            "counter_condition5": self.counter_condition5,
            "counter_condition6": self.counter_condition6,
            "counter_condition7": self.counter_condition7,
            "counter_condition8": self.counter_condition8,
            "counter_condition9": self.counter_condition9,
            "counter_condition10": self.counter_condition10,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1628F23A: ("counter_condition1", structs.decode_BIG_l),
    0x049D5DD4: ("counter_condition2", structs.decode_BIG_l),
    0xBC213AB1: ("counter_condition3", structs.decode_BIG_l),
    0x21F60208: ("counter_condition4", structs.decode_BIG_l),
    0x994A656D: ("counter_condition5", structs.decode_BIG_l),
    0x8BFFCA83: ("counter_condition6", structs.decode_BIG_l),
    0x3343ADE6: ("counter_condition7", structs.decode_BIG_l),
    0x6B20BDB0: ("counter_condition8", structs.decode_BIG_l),
    0xD39CDAD5: ("counter_condition9", structs.decode_BIG_l),
    0x9215E813: ("counter_condition10", structs.decode_BIG_l),
}
