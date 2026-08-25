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

    class AbilitiesJson(typing_extensions.TypedDict):
        double_jump: bool
        suit_type: int
        screw_attack: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x9DC3CDD, 0xC0BD8A5E, 0x5A066E2C)


@dataclasses.dataclass()
class Abilities(BaseProperty):
    double_jump: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x09DC3CDD, original_name="DoubleJump"),
        },
    )
    suit_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC0BD8A5E, original_name="SuitType"),
        },
    )
    screw_attack: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5A066E2C, original_name="ScrewAttack"),
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
        if property_count != 3:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(27))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\t\xdc<\xdd")  # 0x9dc3cdd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.double_jump))

        data.write(b"\xc0\xbd\x8a^")  # 0xc0bd8a5e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.suit_type))

        data.write(b"Z\x06n,")  # 0x5a066e2c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.screw_attack))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AbilitiesJson", data)
        return cls(
            double_jump=json_data["double_jump"],
            suit_type=json_data["suit_type"],
            screw_attack=json_data["screw_attack"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "double_jump": self.double_jump,
            "suit_type": self.suit_type,
            "screw_attack": self.screw_attack,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x09DC3CDD: ("double_jump", structs.decode_BIG_bool_),
    0xC0BD8A5E: ("suit_type", structs.decode_BIG_l),
    0x5A066E2C: ("screw_attack", structs.decode_BIG_l),
}
