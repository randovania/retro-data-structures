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

    class PowerBombGuardianStagePropertiesJson(typing_extensions.TypedDict):
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0x3eb2de35: float
        unknown_0xe50d8dd2: float
        unknown_0x64d482d5: int
        unknown_0xc3e002ac: int
        unknown_0xbb4b6680: float
        unknown_0xd356c997: float
        double_shot_chance: float
        unknown_0x87cc8ba4: int
        unknown_0x6491357e: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x95E7A2C2,
    0x76BA1C18,
    0x3EB2DE35,
    0xE50D8DD2,
    0x64D482D5,
    0xC3E002AC,
    0xBB4B6680,
    0xD356C997,
    0xCA6AC43A,
    0x87CC8BA4,
    0x6491357E,
)


@dataclasses.dataclass()
class PowerBombGuardianStageProperties(BaseProperty):
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0x3eb2de35: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3EB2DE35, original_name="Unknown"),
        },
    )
    unknown_0xe50d8dd2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE50D8DD2, original_name="Unknown"),
        },
    )
    unknown_0x64d482d5: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x64D482D5, original_name="Unknown"),
        },
    )
    unknown_0xc3e002ac: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC3E002AC, original_name="Unknown"),
        },
    )
    unknown_0xbb4b6680: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBB4B6680, original_name="Unknown"),
        },
    )
    unknown_0xd356c997: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD356C997, original_name="Unknown"),
        },
    )
    double_shot_chance: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCA6AC43A, original_name="DoubleShotChance"),
        },
    )
    unknown_0x87cc8ba4: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x87CC8BA4, original_name="Unknown"),
        },
    )
    unknown_0x6491357e: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6491357E, original_name="Unknown"),
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
        if property_count != 11:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHlLHlLHfLHfLHfLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(110))
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b">\xb2\xde5")  # 0x3eb2de35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3eb2de35))

        data.write(b"\xe5\r\x8d\xd2")  # 0xe50d8dd2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe50d8dd2))

        data.write(b"d\xd4\x82\xd5")  # 0x64d482d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x64d482d5))

        data.write(b"\xc3\xe0\x02\xac")  # 0xc3e002ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc3e002ac))

        data.write(b"\xbbKf\x80")  # 0xbb4b6680
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbb4b6680))

        data.write(b"\xd3V\xc9\x97")  # 0xd356c997
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd356c997))

        data.write(b"\xcaj\xc4:")  # 0xca6ac43a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.double_shot_chance))

        data.write(b"\x87\xcc\x8b\xa4")  # 0x87cc8ba4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x87cc8ba4))

        data.write(b"d\x915~")  # 0x6491357e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6491357e))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PowerBombGuardianStagePropertiesJson", data)
        return cls(
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0x3eb2de35=json_data["unknown_0x3eb2de35"],
            unknown_0xe50d8dd2=json_data["unknown_0xe50d8dd2"],
            unknown_0x64d482d5=json_data["unknown_0x64d482d5"],
            unknown_0xc3e002ac=json_data["unknown_0xc3e002ac"],
            unknown_0xbb4b6680=json_data["unknown_0xbb4b6680"],
            unknown_0xd356c997=json_data["unknown_0xd356c997"],
            double_shot_chance=json_data["double_shot_chance"],
            unknown_0x87cc8ba4=json_data["unknown_0x87cc8ba4"],
            unknown_0x6491357e=json_data["unknown_0x6491357e"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0x3eb2de35": self.unknown_0x3eb2de35,
            "unknown_0xe50d8dd2": self.unknown_0xe50d8dd2,
            "unknown_0x64d482d5": self.unknown_0x64d482d5,
            "unknown_0xc3e002ac": self.unknown_0xc3e002ac,
            "unknown_0xbb4b6680": self.unknown_0xbb4b6680,
            "unknown_0xd356c997": self.unknown_0xd356c997,
            "double_shot_chance": self.double_shot_chance,
            "unknown_0x87cc8ba4": self.unknown_0x87cc8ba4,
            "unknown_0x6491357e": self.unknown_0x6491357e,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0x3EB2DE35: ("unknown_0x3eb2de35", structs.decode_BIG_f),
    0xE50D8DD2: ("unknown_0xe50d8dd2", structs.decode_BIG_f),
    0x64D482D5: ("unknown_0x64d482d5", structs.decode_BIG_l),
    0xC3E002AC: ("unknown_0xc3e002ac", structs.decode_BIG_l),
    0xBB4B6680: ("unknown_0xbb4b6680", structs.decode_BIG_f),
    0xD356C997: ("unknown_0xd356c997", structs.decode_BIG_f),
    0xCA6AC43A: ("double_shot_chance", structs.decode_BIG_f),
    0x87CC8BA4: ("unknown_0x87cc8ba4", structs.decode_BIG_l),
    0x6491357E: ("unknown_0x6491357e", structs.decode_BIG_l),
}
