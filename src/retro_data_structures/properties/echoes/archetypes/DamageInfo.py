# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DamageInfoJson(typing_extensions.TypedDict):
        di_weapon_type: int
        di_damage: float
        di_radius: float
        di_knock_back_power: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x119FBD31, 0xF2D02613, 0xEE1BE914, 0x555FF80A)


@dataclasses.dataclass()
class DamageInfo(BaseProperty):
    di_weapon_type: enums.WeaponTypeEnum = dataclasses.field(
        default=enums.WeaponTypeEnum.Power,
        metadata={
            "reflection": FieldReflection[enums.WeaponTypeEnum](
                enums.WeaponTypeEnum,
                id=0x119FBD31,
                original_name="DI_WeaponType",
                from_json=enums.WeaponTypeEnum.from_json,
                to_json=enums.WeaponTypeEnum.to_json,
            ),
        },
    )
    di_damage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF2D02613, original_name="DI_Damage"),
        },
    )
    di_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE1BE914, original_name="DI_Radius"),
        },
    )
    di_knock_back_power: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x555FF80A, original_name="DI_KnockBackPower"),
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
            _FAST_FORMAT = struct.Struct(">LHLLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(40))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            enums.WeaponTypeEnum(dec[2]),
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\x11\x9f\xbd1")  # 0x119fbd31
        data.write(b"\x00\x04")  # size
        self.di_weapon_type.to_stream(data, game)

        data.write(b"\xf2\xd0&\x13")  # 0xf2d02613
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.di_damage))

        data.write(b"\xee\x1b\xe9\x14")  # 0xee1be914
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.di_radius))

        data.write(b"U_\xf8\n")  # 0x555ff80a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.di_knock_back_power))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DamageInfoJson", data)
        return cls(
            di_weapon_type=enums.WeaponTypeEnum.from_json(json_data["di_weapon_type"]),
            di_damage=json_data["di_damage"],
            di_radius=json_data["di_radius"],
            di_knock_back_power=json_data["di_knock_back_power"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "di_weapon_type": self.di_weapon_type.to_json(),
            "di_damage": self.di_damage,
            "di_radius": self.di_radius,
            "di_knock_back_power": self.di_knock_back_power,
        }


def _decode_di_weapon_type(data: typing.BinaryIO, game: Game, property_size: int) -> enums.WeaponTypeEnum:
    return enums.WeaponTypeEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x119FBD31: ("di_weapon_type", _decode_di_weapon_type),
    0xF2D02613: ("di_damage", structs.decode_BIG_f),
    0xEE1BE914: ("di_radius", structs.decode_BIG_f),
    0x555FF80A: ("di_knock_back_power", structs.decode_BIG_f),
}
