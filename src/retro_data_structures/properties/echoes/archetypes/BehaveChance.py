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

    class BehaveChanceJson(typing_extensions.TypedDict):
        lurk: float
        unknown: float
        attack: float
        move: float
        lurk_time: float
        charge_attack: float
        num_bolts: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xD3A313A5, 0x3CFA69F1, 0x1AF89F4B, 0xE7E66F66, 0xB9D9C2D2, 0xCFABDD5F, 0x5AB228B6)


@dataclasses.dataclass()
class BehaveChance(BaseProperty):
    lurk: float = dataclasses.field(
        default=-0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD3A313A5, original_name="Lurk"),
        },
    )
    unknown: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3CFA69F1, original_name="Unknown"),
        },
    )
    attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AF89F4B, original_name="Attack"),
        },
    )
    move: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7E66F66, original_name="Move"),
        },
    )
    lurk_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB9D9C2D2, original_name="LurkTime"),
        },
    )
    charge_attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCFABDD5F, original_name="ChargeAttack"),
        },
    )
    num_bolts: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5AB228B6, original_name="NumBolts"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHl")

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

        data.write(b"\xd3\xa3\x13\xa5")  # 0xd3a313a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lurk))

        data.write(b"<\xfai\xf1")  # 0x3cfa69f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x1a\xf8\x9fK")  # 0x1af89f4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack))

        data.write(b"\xe7\xe6of")  # 0xe7e66f66
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.move))

        data.write(b"\xb9\xd9\xc2\xd2")  # 0xb9d9c2d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lurk_time))

        data.write(b"\xcf\xab\xdd_")  # 0xcfabdd5f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.charge_attack))

        data.write(b"Z\xb2(\xb6")  # 0x5ab228b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.num_bolts))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BehaveChanceJson", data)
        return cls(
            lurk=json_data["lurk"],
            unknown=json_data["unknown"],
            attack=json_data["attack"],
            move=json_data["move"],
            lurk_time=json_data["lurk_time"],
            charge_attack=json_data["charge_attack"],
            num_bolts=json_data["num_bolts"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "lurk": self.lurk,
            "unknown": self.unknown,
            "attack": self.attack,
            "move": self.move,
            "lurk_time": self.lurk_time,
            "charge_attack": self.charge_attack,
            "num_bolts": self.num_bolts,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD3A313A5: ("lurk", structs.decode_BIG_f),
    0x3CFA69F1: ("unknown", structs.decode_BIG_f),
    0x1AF89F4B: ("attack", structs.decode_BIG_f),
    0xE7E66F66: ("move", structs.decode_BIG_f),
    0xB9D9C2D2: ("lurk_time", structs.decode_BIG_f),
    0xCFABDD5F: ("charge_attack", structs.decode_BIG_f),
    0x5AB228B6: ("num_bolts", structs.decode_BIG_l),
}
