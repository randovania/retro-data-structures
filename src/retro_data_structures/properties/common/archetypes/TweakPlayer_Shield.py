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

    class TweakPlayer_ShieldJson(typing_extensions.TypedDict):
        max_energy: float
        usage_rate: float
        recharge_rate: float
        allows_motion: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xD42FA1C1, 0x787855E6, 0x5DADD6AB, 0x59EFBB34)


@dataclasses.dataclass()
class TweakPlayer_Shield(BaseProperty):
    max_energy: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD42FA1C1, original_name="MaxEnergy"),
        },
    )
    usage_rate: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x787855E6, original_name="UsageRate"),
        },
    )
    recharge_rate: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5DADD6AB, original_name="RechargeRate"),
        },
    )
    allows_motion: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x59EFBB34, original_name="AllowsMotion"),
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
        if property_count != 4:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLH?")

        dec = _FAST_FORMAT.unpack(data.read(37))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\xd4/\xa1\xc1")  # 0xd42fa1c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_energy))

        data.write(b"xxU\xe6")  # 0x787855e6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.usage_rate))

        data.write(b"]\xad\xd6\xab")  # 0x5dadd6ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recharge_rate))

        data.write(b"Y\xef\xbb4")  # 0x59efbb34
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.allows_motion))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_ShieldJson", data)
        return cls(
            max_energy=json_data["max_energy"],
            usage_rate=json_data["usage_rate"],
            recharge_rate=json_data["recharge_rate"],
            allows_motion=json_data["allows_motion"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "max_energy": self.max_energy,
            "usage_rate": self.usage_rate,
            "recharge_rate": self.recharge_rate,
            "allows_motion": self.allows_motion,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD42FA1C1: ("max_energy", structs.decode_BIG_f),
    0x787855E6: ("usage_rate", structs.decode_BIG_f),
    0x5DADD6AB: ("recharge_rate", structs.decode_BIG_f),
    0x59EFBB34: ("allows_motion", structs.decode_BIG_bool_),
}
