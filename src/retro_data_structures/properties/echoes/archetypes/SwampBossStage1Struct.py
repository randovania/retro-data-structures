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

    class SwampBossStage1StructJson(typing_extensions.TypedDict):
        unknown_0x98106ee2: float
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0xbb0ffdd6: int
        unknown_0x60b0ae31: int
        first_attack: int
        second_attack: int
        third_attack: int
        fourth_attack: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x98106EE2, 0x95E7A2C2, 0x76BA1C18, 0xBB0FFDD6, 0x60B0AE31, 0x9CFA9ACB, 0x180F81DD, 0x42617CFD, 0xC39F864E)


@dataclasses.dataclass()
class SwampBossStage1Struct(BaseProperty):
    unknown_0x98106ee2: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x98106EE2, original_name="Unknown"),
        },
    )
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0xbb0ffdd6: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBB0FFDD6, original_name="Unknown"),
        },
    )
    unknown_0x60b0ae31: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x60B0AE31, original_name="Unknown"),
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
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC39F864E, original_name="FourthAttack"),
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
        if property_count != 9:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHlLHlLHlLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(90))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24]) == _FAST_IDS
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\x98\x10n\xe2")  # 0x98106ee2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x98106ee2))

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b"\xbb\x0f\xfd\xd6")  # 0xbb0ffdd6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xbb0ffdd6))

        data.write(b"`\xb0\xae1")  # 0x60b0ae31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x60b0ae31))

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

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwampBossStage1StructJson", data)
        return cls(
            unknown_0x98106ee2=json_data["unknown_0x98106ee2"],
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0xbb0ffdd6=json_data["unknown_0xbb0ffdd6"],
            unknown_0x60b0ae31=json_data["unknown_0x60b0ae31"],
            first_attack=json_data["first_attack"],
            second_attack=json_data["second_attack"],
            third_attack=json_data["third_attack"],
            fourth_attack=json_data["fourth_attack"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x98106ee2": self.unknown_0x98106ee2,
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0xbb0ffdd6": self.unknown_0xbb0ffdd6,
            "unknown_0x60b0ae31": self.unknown_0x60b0ae31,
            "first_attack": self.first_attack,
            "second_attack": self.second_attack,
            "third_attack": self.third_attack,
            "fourth_attack": self.fourth_attack,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x98106EE2: ("unknown_0x98106ee2", structs.decode_BIG_f),
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0xBB0FFDD6: ("unknown_0xbb0ffdd6", structs.decode_BIG_l),
    0x60B0AE31: ("unknown_0x60b0ae31", structs.decode_BIG_l),
    0x9CFA9ACB: ("first_attack", structs.decode_BIG_l),
    0x180F81DD: ("second_attack", structs.decode_BIG_l),
    0x42617CFD: ("third_attack", structs.decode_BIG_l),
    0xC39F864E: ("fourth_attack", structs.decode_BIG_l),
}
