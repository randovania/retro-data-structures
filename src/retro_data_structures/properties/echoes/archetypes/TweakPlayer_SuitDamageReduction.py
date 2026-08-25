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

    class TweakPlayer_SuitDamageReductionJson(typing_extensions.TypedDict):
        varia: float
        dark: float
        light: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xDF131ECD, 0x908A8E6C, 0x95700A27)


@dataclasses.dataclass()
class TweakPlayer_SuitDamageReduction(BaseProperty):
    varia: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDF131ECD, original_name="Varia"),
        },
    )
    dark: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x908A8E6C, original_name="Dark"),
        },
    )
    light: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95700A27, original_name="Light"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(30))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\xdf\x13\x1e\xcd")  # 0xdf131ecd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.varia))

        data.write(b"\x90\x8a\x8el")  # 0x908a8e6c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dark))

        data.write(b"\x95p\n'")  # 0x95700a27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.light))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_SuitDamageReductionJson", data)
        return cls(
            varia=json_data["varia"],
            dark=json_data["dark"],
            light=json_data["light"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "varia": self.varia,
            "dark": self.dark,
            "light": self.light,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDF131ECD: ("varia", structs.decode_BIG_f),
    0x908A8E6C: ("dark", structs.decode_BIG_f),
    0x95700A27: ("light", structs.decode_BIG_f),
}
