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

    class TweakPlayerGun_Beam_MiscJson(typing_extensions.TypedDict):
        ai_burn_damage: float
        unknown_0x4848f444: float
        max_absorbed_phazon_shots: int
        unknown_0x3ae5d1fa: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xF8F9BF33, 0x4848F444, 0x1E710222, 0x3AE5D1FA)


@dataclasses.dataclass()
class TweakPlayerGun_Beam_Misc(BaseProperty):
    ai_burn_damage: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8F9BF33, original_name="AIBurnDamage"),
        },
    )
    unknown_0x4848f444: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4848F444, original_name="Unknown"),
        },
    )
    max_absorbed_phazon_shots: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1E710222, original_name="MaxAbsorbedPhazonShots"),
        },
    )
    unknown_0x3ae5d1fa: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3AE5D1FA, original_name="Unknown"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHfLHlLHf")

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

        data.write(b"\xf8\xf9\xbf3")  # 0xf8f9bf33
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ai_burn_damage))

        data.write(b"HH\xf4D")  # 0x4848f444
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4848f444))

        data.write(b'\x1eq\x02"')  # 0x1e710222
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_absorbed_phazon_shots))

        data.write(b":\xe5\xd1\xfa")  # 0x3ae5d1fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3ae5d1fa))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_Beam_MiscJson", data)
        return cls(
            ai_burn_damage=json_data["ai_burn_damage"],
            unknown_0x4848f444=json_data["unknown_0x4848f444"],
            max_absorbed_phazon_shots=json_data["max_absorbed_phazon_shots"],
            unknown_0x3ae5d1fa=json_data["unknown_0x3ae5d1fa"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "ai_burn_damage": self.ai_burn_damage,
            "unknown_0x4848f444": self.unknown_0x4848f444,
            "max_absorbed_phazon_shots": self.max_absorbed_phazon_shots,
            "unknown_0x3ae5d1fa": self.unknown_0x3ae5d1fa,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF8F9BF33: ("ai_burn_damage", structs.decode_BIG_f),
    0x4848F444: ("unknown_0x4848f444", structs.decode_BIG_f),
    0x1E710222: ("max_absorbed_phazon_shots", structs.decode_BIG_l),
    0x3AE5D1FA: ("unknown_0x3ae5d1fa", structs.decode_BIG_f),
}
