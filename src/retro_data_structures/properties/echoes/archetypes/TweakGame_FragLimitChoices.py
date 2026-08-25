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

    class TweakGame_FragLimitChoicesJson(typing_extensions.TypedDict):
        frag_limit0: int
        frag_limit1: int
        frag_limit2: int
        frag_limit3: int
        frag_limit4: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xA2023BA8, 0x1ABE5CCD, 0x80BF323, 0xB0B79446, 0x2D60ACFF)


@dataclasses.dataclass()
class TweakGame_FragLimitChoices(BaseProperty):
    frag_limit0: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA2023BA8, original_name="FragLimit0"),
        },
    )
    frag_limit1: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1ABE5CCD, original_name="FragLimit1"),
        },
    )
    frag_limit2: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x080BF323, original_name="FragLimit2"),
        },
    )
    frag_limit3: int = dataclasses.field(
        default=15,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB0B79446, original_name="FragLimit3"),
        },
    )
    frag_limit4: int = dataclasses.field(
        default=20,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2D60ACFF, original_name="FragLimit4"),
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
            _FAST_FORMAT = struct.Struct(">LHlLHlLHlLHlLHl")

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

        data.write(b"\xa2\x02;\xa8")  # 0xa2023ba8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.frag_limit0))

        data.write(b"\x1a\xbe\\\xcd")  # 0x1abe5ccd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.frag_limit1))

        data.write(b"\x08\x0b\xf3#")  # 0x80bf323
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.frag_limit2))

        data.write(b"\xb0\xb7\x94F")  # 0xb0b79446
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.frag_limit3))

        data.write(b"-`\xac\xff")  # 0x2d60acff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.frag_limit4))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGame_FragLimitChoicesJson", data)
        return cls(
            frag_limit0=json_data["frag_limit0"],
            frag_limit1=json_data["frag_limit1"],
            frag_limit2=json_data["frag_limit2"],
            frag_limit3=json_data["frag_limit3"],
            frag_limit4=json_data["frag_limit4"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "frag_limit0": self.frag_limit0,
            "frag_limit1": self.frag_limit1,
            "frag_limit2": self.frag_limit2,
            "frag_limit3": self.frag_limit3,
            "frag_limit4": self.frag_limit4,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA2023BA8: ("frag_limit0", structs.decode_BIG_l),
    0x1ABE5CCD: ("frag_limit1", structs.decode_BIG_l),
    0x080BF323: ("frag_limit2", structs.decode_BIG_l),
    0xB0B79446: ("frag_limit3", structs.decode_BIG_l),
    0x2D60ACFF: ("frag_limit4", structs.decode_BIG_l),
}
