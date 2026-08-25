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

    class TweakGame_TimeLimitChoicesJson(typing_extensions.TypedDict):
        time_limit0: float
        time_limit1: float
        time_limit2: float
        time_limit3: float
        time_limit4: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x779E8FF4, 0xBCC25C51, 0x3A562EFF, 0xF10AFD5A, 0xEC0FCDE2)


@dataclasses.dataclass()
class TweakGame_TimeLimitChoices(BaseProperty):
    time_limit0: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x779E8FF4, original_name="TimeLimit0"),
        },
    )
    time_limit1: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBCC25C51, original_name="TimeLimit1"),
        },
    )
    time_limit2: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3A562EFF, original_name="TimeLimit2"),
        },
    )
    time_limit3: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF10AFD5A, original_name="TimeLimit3"),
        },
    )
    time_limit4: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC0FCDE2, original_name="TimeLimit4"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(50))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"w\x9e\x8f\xf4")  # 0x779e8ff4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_limit0))

        data.write(b"\xbc\xc2\\Q")  # 0xbcc25c51
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_limit1))

        data.write(b":V.\xff")  # 0x3a562eff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_limit2))

        data.write(b"\xf1\n\xfdZ")  # 0xf10afd5a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_limit3))

        data.write(b"\xec\x0f\xcd\xe2")  # 0xec0fcde2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_limit4))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGame_TimeLimitChoicesJson", data)
        return cls(
            time_limit0=json_data["time_limit0"],
            time_limit1=json_data["time_limit1"],
            time_limit2=json_data["time_limit2"],
            time_limit3=json_data["time_limit3"],
            time_limit4=json_data["time_limit4"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "time_limit0": self.time_limit0,
            "time_limit1": self.time_limit1,
            "time_limit2": self.time_limit2,
            "time_limit3": self.time_limit3,
            "time_limit4": self.time_limit4,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x779E8FF4: ("time_limit0", structs.decode_BIG_f),
    0xBCC25C51: ("time_limit1", structs.decode_BIG_f),
    0x3A562EFF: ("time_limit2", structs.decode_BIG_f),
    0xF10AFD5A: ("time_limit3", structs.decode_BIG_f),
    0xEC0FCDE2: ("time_limit4", structs.decode_BIG_f),
}
