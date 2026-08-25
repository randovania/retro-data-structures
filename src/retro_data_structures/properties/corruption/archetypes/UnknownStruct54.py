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

    class UnknownStruct54Json(typing_extensions.TypedDict):
        time: float
        unknown: float
        damping: float
        coloration: float
        cross_talk: float
        mix: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x44335AFF, 0x5724CCD8, 0xFCF4AAB0, 0x5D6B1084, 0xFB11A412, 0xDE9DD8B8)


@dataclasses.dataclass()
class UnknownStruct54(BaseProperty):
    time: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0x44335AFF, original_name="Time"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5724CCD8, original_name="Unknown"),
        },
    )
    damping: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFCF4AAB0, original_name="Damping"),
        },
    )
    coloration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5D6B1084, original_name="Coloration"),
        },
    )
    cross_talk: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB11A412, original_name="CrossTalk"),
        },
    )
    mix: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE9DD8B8, original_name="Mix"),
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
        if property_count != 6:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(60))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"D3Z\xff")  # 0x44335aff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time))

        data.write(b"W$\xcc\xd8")  # 0x5724ccd8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xfc\xf4\xaa\xb0")  # 0xfcf4aab0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damping))

        data.write(b"]k\x10\x84")  # 0x5d6b1084
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.coloration))

        data.write(b"\xfb\x11\xa4\x12")  # 0xfb11a412
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cross_talk))

        data.write(b"\xde\x9d\xd8\xb8")  # 0xde9dd8b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mix))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct54Json", data)
        return cls(
            time=json_data["time"],
            unknown=json_data["unknown"],
            damping=json_data["damping"],
            coloration=json_data["coloration"],
            cross_talk=json_data["cross_talk"],
            mix=json_data["mix"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "time": self.time,
            "unknown": self.unknown,
            "damping": self.damping,
            "coloration": self.coloration,
            "cross_talk": self.cross_talk,
            "mix": self.mix,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x44335AFF: ("time", structs.decode_BIG_f),
    0x5724CCD8: ("unknown", structs.decode_BIG_f),
    0xFCF4AAB0: ("damping", structs.decode_BIG_f),
    0x5D6B1084: ("coloration", structs.decode_BIG_f),
    0xFB11A412: ("cross_talk", structs.decode_BIG_f),
    0xDE9DD8B8: ("mix", structs.decode_BIG_f),
}
