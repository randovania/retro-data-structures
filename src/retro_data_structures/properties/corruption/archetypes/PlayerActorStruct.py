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

    class PlayerActorStructJson(typing_extensions.TypedDict):
        suit_model: int
        suit_skin_rules: int
        gun_model: int
        fade_in_time: float
        fade_out_time: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xF7FFBD07, 0xB616BAA, 0x50340852, 0x90AA341F, 0x7C269EBC)


@dataclasses.dataclass()
class PlayerActorStruct(BaseProperty):
    suit_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF7FFBD07, original_name="SuitModel"),
        },
    )
    suit_skin_rules: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0B616BAA, original_name="SuitSkinRules"),
        },
    )
    gun_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x50340852, original_name="GunModel"),
        },
    )
    fade_in_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AA341F, original_name="FadeInTime"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7C269EBC, original_name="FadeOutTime"),
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
            _FAST_FORMAT = struct.Struct(">LHQLHQLHQLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(62))
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

        data.write(b"\xf7\xff\xbd\x07")  # 0xf7ffbd07
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.suit_model))

        data.write(b"\x0bak\xaa")  # 0xb616baa
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.suit_skin_rules))

        data.write(b"P4\x08R")  # 0x50340852
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.gun_model))

        data.write(b"\x90\xaa4\x1f")  # 0x90aa341f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_time))

        data.write(b"|&\x9e\xbc")  # 0x7c269ebc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerActorStructJson", data)
        return cls(
            suit_model=json_data["suit_model"],
            suit_skin_rules=json_data["suit_skin_rules"],
            gun_model=json_data["gun_model"],
            fade_in_time=json_data["fade_in_time"],
            fade_out_time=json_data["fade_out_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "suit_model": self.suit_model,
            "suit_skin_rules": self.suit_skin_rules,
            "gun_model": self.gun_model,
            "fade_in_time": self.fade_in_time,
            "fade_out_time": self.fade_out_time,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF7FFBD07: ("suit_model", structs.decode_BIG_Q),
    0x0B616BAA: ("suit_skin_rules", structs.decode_BIG_Q),
    0x50340852: ("gun_model", structs.decode_BIG_Q),
    0x90AA341F: ("fade_in_time", structs.decode_BIG_f),
    0x7C269EBC: ("fade_out_time", structs.decode_BIG_f),
}
