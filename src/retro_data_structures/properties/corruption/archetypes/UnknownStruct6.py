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

    class UnknownStruct6Json(typing_extensions.TypedDict):
        gravity_buster_chance: float
        combat_hatches_chance: float
        dark_samus_echoes_chance: float
        turret_chance: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xA14433C3, 0xAFE48213, 0x5A5D4D0, 0xD5780905)


@dataclasses.dataclass()
class UnknownStruct6(BaseProperty):
    gravity_buster_chance: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA14433C3, original_name="GravityBusterChance"),
        },
    )
    combat_hatches_chance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAFE48213, original_name="CombatHatchesChance"),
        },
    )
    dark_samus_echoes_chance: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x05A5D4D0, original_name="DarkSamusEchoesChance"),
        },
    )
    turret_chance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5780905, original_name="TurretChance"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(40))
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

        data.write(b"\xa1D3\xc3")  # 0xa14433c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gravity_buster_chance))

        data.write(b"\xaf\xe4\x82\x13")  # 0xafe48213
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.combat_hatches_chance))

        data.write(b"\x05\xa5\xd4\xd0")  # 0x5a5d4d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dark_samus_echoes_chance))

        data.write(b"\xd5x\t\x05")  # 0xd5780905
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turret_chance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct6Json", data)
        return cls(
            gravity_buster_chance=json_data["gravity_buster_chance"],
            combat_hatches_chance=json_data["combat_hatches_chance"],
            dark_samus_echoes_chance=json_data["dark_samus_echoes_chance"],
            turret_chance=json_data["turret_chance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "gravity_buster_chance": self.gravity_buster_chance,
            "combat_hatches_chance": self.combat_hatches_chance,
            "dark_samus_echoes_chance": self.dark_samus_echoes_chance,
            "turret_chance": self.turret_chance,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA14433C3: ("gravity_buster_chance", structs.decode_BIG_f),
    0xAFE48213: ("combat_hatches_chance", structs.decode_BIG_f),
    0x05A5D4D0: ("dark_samus_echoes_chance", structs.decode_BIG_f),
    0xD5780905: ("turret_chance", structs.decode_BIG_f),
}
