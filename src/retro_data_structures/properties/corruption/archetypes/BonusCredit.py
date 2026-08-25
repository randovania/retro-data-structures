# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BonusCreditJson(typing_extensions.TypedDict):
        bonus_credit: int


class BonusCreditEnum(enum.IntEnum):
    Unknown1 = 3550818934
    Unknown2 = 725797134
    Unknown3 = 828710715
    Unknown4 = 3149230457
    Unknown5 = 3214133816

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = 0xFF5DE1DA


@dataclasses.dataclass()
class BonusCredit(BaseProperty):
    bonus_credit: BonusCreditEnum = dataclasses.field(
        default=BonusCreditEnum.Unknown5,
        metadata={
            "reflection": FieldReflection[BonusCreditEnum](
                BonusCreditEnum,
                id=0xFF5DE1DA,
                original_name="BonusCredit",
                from_json=BonusCreditEnum.from_json,
                to_json=BonusCreditEnum.to_json,
            ),
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
        if property_count != 1:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHL")

        dec = _FAST_FORMAT.unpack(data.read(10))
        assert (dec[0]) == _FAST_IDS
        return cls(
            BonusCreditEnum(dec[2]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"\xff]\xe1\xda")  # 0xff5de1da
        data.write(b"\x00\x04")  # size
        self.bonus_credit.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BonusCreditJson", data)
        return cls(
            bonus_credit=BonusCreditEnum.from_json(json_data["bonus_credit"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "bonus_credit": self.bonus_credit.to_json(),
        }


def _decode_bonus_credit(data: typing.BinaryIO, game: Game, property_size: int) -> BonusCreditEnum:
    return BonusCreditEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFF5DE1DA: ("bonus_credit", _decode_bonus_credit),
}
