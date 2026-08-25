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

    class TweakGame_CoinLimitChoicesJson(typing_extensions.TypedDict):
        coin_limit0: int
        coin_limit1: int
        coin_limit2: int
        coin_limit3: int
        coin_limit4: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x6B4CAE26, 0xD3F0C943, 0xC14566AD, 0x79F901C8, 0xE42E3971)


@dataclasses.dataclass()
class TweakGame_CoinLimitChoices(BaseProperty):
    coin_limit0: int = dataclasses.field(
        default=200,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6B4CAE26, original_name="CoinLimit0"),
        },
    )
    coin_limit1: int = dataclasses.field(
        default=400,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD3F0C943, original_name="CoinLimit1"),
        },
    )
    coin_limit2: int = dataclasses.field(
        default=600,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC14566AD, original_name="CoinLimit2"),
        },
    )
    coin_limit3: int = dataclasses.field(
        default=800,
        metadata={
            "reflection": FieldReflection[int](int, id=0x79F901C8, original_name="CoinLimit3"),
        },
    )
    coin_limit4: int = dataclasses.field(
        default=1000,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE42E3971, original_name="CoinLimit4"),
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

        data.write(b"kL\xae&")  # 0x6b4cae26
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_limit0))

        data.write(b"\xd3\xf0\xc9C")  # 0xd3f0c943
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_limit1))

        data.write(b"\xc1Ef\xad")  # 0xc14566ad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_limit2))

        data.write(b"y\xf9\x01\xc8")  # 0x79f901c8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_limit3))

        data.write(b"\xe4.9q")  # 0xe42e3971
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.coin_limit4))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGame_CoinLimitChoicesJson", data)
        return cls(
            coin_limit0=json_data["coin_limit0"],
            coin_limit1=json_data["coin_limit1"],
            coin_limit2=json_data["coin_limit2"],
            coin_limit3=json_data["coin_limit3"],
            coin_limit4=json_data["coin_limit4"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "coin_limit0": self.coin_limit0,
            "coin_limit1": self.coin_limit1,
            "coin_limit2": self.coin_limit2,
            "coin_limit3": self.coin_limit3,
            "coin_limit4": self.coin_limit4,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6B4CAE26: ("coin_limit0", structs.decode_BIG_l),
    0xD3F0C943: ("coin_limit1", structs.decode_BIG_l),
    0xC14566AD: ("coin_limit2", structs.decode_BIG_l),
    0x79F901C8: ("coin_limit3", structs.decode_BIG_l),
    0xE42E3971: ("coin_limit4", structs.decode_BIG_l),
}
