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

    class SwampBossStage2StructJson(typing_extensions.TypedDict):
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0x29e6ead6: float
        unknown_0x1753225e: float
        dash_chance: float
        taunt_chance: float
        first_attack: int
        second_attack: int
        third_attack: int
        fourth_attack: int
        fifth_attack: int
        health: float
        unknown_0x2e7e55f2: int
        unknown_0xef3efec0: int
        unknown_0x2b0bfd51: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x95E7A2C2,
    0x76BA1C18,
    0x29E6EAD6,
    0x1753225E,
    0xBE1AFBF8,
    0xA77F6212,
    0x9CFA9ACB,
    0x180F81DD,
    0x42617CFD,
    0xC39F864E,
    0x1994D506,
    0xF0668919,
    0x2E7E55F2,
    0xEF3EFEC0,
    0x2B0BFD51,
)


@dataclasses.dataclass()
class SwampBossStage2Struct(BaseProperty):
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0x29e6ead6: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x29E6EAD6, original_name="Unknown"),
        },
    )
    unknown_0x1753225e: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1753225E, original_name="Unknown"),
        },
    )
    dash_chance: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBE1AFBF8, original_name="DashChance"),
        },
    )
    taunt_chance: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA77F6212, original_name="TauntChance"),
        },
    )
    first_attack: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9CFA9ACB, original_name="FirstAttack"),
        },
    )
    second_attack: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x180F81DD, original_name="SecondAttack"),
        },
    )
    third_attack: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42617CFD, original_name="ThirdAttack"),
        },
    )
    fourth_attack: int = dataclasses.field(
        default=7,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC39F864E, original_name="FourthAttack"),
        },
    )
    fifth_attack: int = dataclasses.field(
        default=7,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1994D506, original_name="FifthAttack"),
        },
    )
    health: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0668919, original_name="Health"),
        },
    )
    unknown_0x2e7e55f2: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2E7E55F2, original_name="Unknown"),
        },
    )
    unknown_0xef3efec0: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEF3EFEC0, original_name="Unknown"),
        },
    )
    unknown_0x2b0bfd51: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2B0BFD51, original_name="Unknown"),
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
        if property_count != 15:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHlLHlLHlLHlLHlLHfLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(150))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
        ) == _FAST_IDS
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
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b")\xe6\xea\xd6")  # 0x29e6ead6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x29e6ead6))

        data.write(b'\x17S"^')  # 0x1753225e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1753225e))

        data.write(b"\xbe\x1a\xfb\xf8")  # 0xbe1afbf8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_chance))

        data.write(b"\xa7\x7fb\x12")  # 0xa77f6212
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.taunt_chance))

        data.write(b"\x9c\xfa\x9a\xcb")  # 0x9cfa9acb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.first_attack))

        data.write(b"\x18\x0f\x81\xdd")  # 0x180f81dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.second_attack))

        data.write(b"Ba|\xfd")  # 0x42617cfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.third_attack))

        data.write(b"\xc3\x9f\x86N")  # 0xc39f864e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.fourth_attack))

        data.write(b"\x19\x94\xd5\x06")  # 0x1994d506
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.fifth_attack))

        data.write(b"\xf0f\x89\x19")  # 0xf0668919
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.health))

        data.write(b".~U\xf2")  # 0x2e7e55f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2e7e55f2))

        data.write(b"\xef>\xfe\xc0")  # 0xef3efec0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xef3efec0))

        data.write(b"+\x0b\xfdQ")  # 0x2b0bfd51
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2b0bfd51))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwampBossStage2StructJson", data)
        return cls(
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0x29e6ead6=json_data["unknown_0x29e6ead6"],
            unknown_0x1753225e=json_data["unknown_0x1753225e"],
            dash_chance=json_data["dash_chance"],
            taunt_chance=json_data["taunt_chance"],
            first_attack=json_data["first_attack"],
            second_attack=json_data["second_attack"],
            third_attack=json_data["third_attack"],
            fourth_attack=json_data["fourth_attack"],
            fifth_attack=json_data["fifth_attack"],
            health=json_data["health"],
            unknown_0x2e7e55f2=json_data["unknown_0x2e7e55f2"],
            unknown_0xef3efec0=json_data["unknown_0xef3efec0"],
            unknown_0x2b0bfd51=json_data["unknown_0x2b0bfd51"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0x29e6ead6": self.unknown_0x29e6ead6,
            "unknown_0x1753225e": self.unknown_0x1753225e,
            "dash_chance": self.dash_chance,
            "taunt_chance": self.taunt_chance,
            "first_attack": self.first_attack,
            "second_attack": self.second_attack,
            "third_attack": self.third_attack,
            "fourth_attack": self.fourth_attack,
            "fifth_attack": self.fifth_attack,
            "health": self.health,
            "unknown_0x2e7e55f2": self.unknown_0x2e7e55f2,
            "unknown_0xef3efec0": self.unknown_0xef3efec0,
            "unknown_0x2b0bfd51": self.unknown_0x2b0bfd51,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0x29E6EAD6: ("unknown_0x29e6ead6", structs.decode_BIG_f),
    0x1753225E: ("unknown_0x1753225e", structs.decode_BIG_f),
    0xBE1AFBF8: ("dash_chance", structs.decode_BIG_f),
    0xA77F6212: ("taunt_chance", structs.decode_BIG_f),
    0x9CFA9ACB: ("first_attack", structs.decode_BIG_l),
    0x180F81DD: ("second_attack", structs.decode_BIG_l),
    0x42617CFD: ("third_attack", structs.decode_BIG_l),
    0xC39F864E: ("fourth_attack", structs.decode_BIG_l),
    0x1994D506: ("fifth_attack", structs.decode_BIG_l),
    0xF0668919: ("health", structs.decode_BIG_f),
    0x2E7E55F2: ("unknown_0x2e7e55f2", structs.decode_BIG_l),
    0xEF3EFEC0: ("unknown_0xef3efec0", structs.decode_BIG_l),
    0x2B0BFD51: ("unknown_0x2b0bfd51", structs.decode_BIG_l),
}
