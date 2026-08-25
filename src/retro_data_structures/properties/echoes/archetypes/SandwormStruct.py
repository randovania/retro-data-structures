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

    class SandwormStructJson(typing_extensions.TypedDict):
        unknown_0x98106ee2: float
        unknown_0x95081226: float
        unknown_0xc2064265: float
        move_speed_multiplier: float
        unknown_0x59f14d7c: int
        unknown_0x9606b4b0: int
        unknown_0xfc2697dd: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x98106EE2, 0x95081226, 0xC2064265, 0xFE9133CD, 0x59F14D7C, 0x9606B4B0, 0xFC2697DD)


@dataclasses.dataclass()
class SandwormStruct(BaseProperty):
    unknown_0x98106ee2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x98106EE2, original_name="Unknown"),
        },
    )
    unknown_0x95081226: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95081226, original_name="Unknown"),
        },
    )
    unknown_0xc2064265: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC2064265, original_name="Unknown"),
        },
    )
    move_speed_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFE9133CD, original_name="MoveSpeedMultiplier"),
        },
    )
    unknown_0x59f14d7c: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x59F14D7C, original_name="Unknown"),
        },
    )
    unknown_0x9606b4b0: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9606B4B0, original_name="Unknown"),
        },
    )
    unknown_0xfc2697dd: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFC2697DD, original_name="Unknown"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(70))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\x98\x10n\xe2")  # 0x98106ee2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x98106ee2))

        data.write(b"\x95\x08\x12&")  # 0x95081226
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95081226))

        data.write(b"\xc2\x06Be")  # 0xc2064265
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc2064265))

        data.write(b"\xfe\x913\xcd")  # 0xfe9133cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move_speed_multiplier))

        data.write(b"Y\xf1M|")  # 0x59f14d7c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x59f14d7c))

        data.write(b"\x96\x06\xb4\xb0")  # 0x9606b4b0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9606b4b0))

        data.write(b"\xfc&\x97\xdd")  # 0xfc2697dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfc2697dd))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandwormStructJson", data)
        return cls(
            unknown_0x98106ee2=json_data["unknown_0x98106ee2"],
            unknown_0x95081226=json_data["unknown_0x95081226"],
            unknown_0xc2064265=json_data["unknown_0xc2064265"],
            move_speed_multiplier=json_data["move_speed_multiplier"],
            unknown_0x59f14d7c=json_data["unknown_0x59f14d7c"],
            unknown_0x9606b4b0=json_data["unknown_0x9606b4b0"],
            unknown_0xfc2697dd=json_data["unknown_0xfc2697dd"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x98106ee2": self.unknown_0x98106ee2,
            "unknown_0x95081226": self.unknown_0x95081226,
            "unknown_0xc2064265": self.unknown_0xc2064265,
            "move_speed_multiplier": self.move_speed_multiplier,
            "unknown_0x59f14d7c": self.unknown_0x59f14d7c,
            "unknown_0x9606b4b0": self.unknown_0x9606b4b0,
            "unknown_0xfc2697dd": self.unknown_0xfc2697dd,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x98106EE2: ("unknown_0x98106ee2", structs.decode_BIG_f),
    0x95081226: ("unknown_0x95081226", structs.decode_BIG_f),
    0xC2064265: ("unknown_0xc2064265", structs.decode_BIG_f),
    0xFE9133CD: ("move_speed_multiplier", structs.decode_BIG_f),
    0x59F14D7C: ("unknown_0x59f14d7c", structs.decode_BIG_l),
    0x9606B4B0: ("unknown_0x9606b4b0", structs.decode_BIG_l),
    0xFC2697DD: ("unknown_0xfc2697dd", structs.decode_BIG_l),
}
