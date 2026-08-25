# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SwarmSoundDataJson(typing_extensions.TypedDict):
        sound_asset: int
        max_count: int
        min_delay: float
        max_delay: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xFC0D589E, 0x54B68C4C, 0xB5F9C71A, 0xF5B6BF6C)


@dataclasses.dataclass()
class SwarmSoundData(BaseProperty):
    sound_asset: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFC0D589E, original_name="SoundAsset"),
        },
    )
    max_count: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x54B68C4C, original_name="MaxCount"),
        },
    )
    min_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5F9C71A, original_name="MinDelay"),
        },
    )
    max_delay: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF5B6BF6C, original_name="MaxDelay"),
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
            _FAST_FORMAT = struct.Struct(">LHQLHlLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(44))
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

        data.write(b"\xfc\rX\x9e")  # 0xfc0d589e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_asset))

        data.write(b"T\xb6\x8cL")  # 0x54b68c4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_count))

        data.write(b"\xb5\xf9\xc7\x1a")  # 0xb5f9c71a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_delay))

        data.write(b"\xf5\xb6\xbfl")  # 0xf5b6bf6c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_delay))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwarmSoundDataJson", data)
        return cls(
            sound_asset=json_data["sound_asset"],
            max_count=json_data["max_count"],
            min_delay=json_data["min_delay"],
            max_delay=json_data["max_delay"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "sound_asset": self.sound_asset,
            "max_count": self.max_count,
            "min_delay": self.min_delay,
            "max_delay": self.max_delay,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFC0D589E: ("sound_asset", structs.decode_BIG_Q),
    0x54B68C4C: ("max_count", structs.decode_BIG_l),
    0xB5F9C71A: ("min_delay", structs.decode_BIG_f),
    0xF5B6BF6C: ("max_delay", structs.decode_BIG_f),
}
