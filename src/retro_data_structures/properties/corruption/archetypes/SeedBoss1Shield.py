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

    class SeedBoss1ShieldJson(typing_extensions.TypedDict):
        cmdl_0xdce1a940: int
        cmdl_0xf4c318b3: int
        cmdl_0xb3673269: int
        cmdl_0xb9196d9e: int
        important_moment: int
        cmdl_0x4d7984e6: int
        cmdl_0x8fbe621d: int
        cmdl_0x11ea2651: int
        cmdl_0x564e0c8b: int
        cmdl_0x807edcc5: int
        cmdl_0x708b0155: int
        cmdl_0xe46803dc: int
        cmdl_0x6a975cff: int
        cmdl_0x97e2b6c7: int
        cmdl_0x1176c469: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xDCE1A940,
    0xF4C318B3,
    0xB3673269,
    0xB9196D9E,
    0x8C0BEE98,
    0x4D7984E6,
    0x8FBE621D,
    0x11EA2651,
    0x564E0C8B,
    0x807EDCC5,
    0x708B0155,
    0xE46803DC,
    0x6A975CFF,
    0x97E2B6C7,
    0x1176C469,
)


@dataclasses.dataclass()
class SeedBoss1Shield(BaseProperty):
    cmdl_0xdce1a940: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDCE1A940, original_name="CMDL"),
        },
    )
    cmdl_0xf4c318b3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF4C318B3, original_name="CMDL"),
        },
    )
    cmdl_0xb3673269: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB3673269, original_name="CMDL"),
        },
    )
    cmdl_0xb9196d9e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB9196D9E, original_name="CMDL"),
        },
    )
    important_moment: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8C0BEE98, original_name="ImportantMoment"),
        },
    )
    cmdl_0x4d7984e6: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4D7984E6, original_name="CMDL"),
        },
    )
    cmdl_0x8fbe621d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8FBE621D, original_name="CMDL"),
        },
    )
    cmdl_0x11ea2651: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x11EA2651, original_name="CMDL"),
        },
    )
    cmdl_0x564e0c8b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x564E0C8B, original_name="CMDL"),
        },
    )
    cmdl_0x807edcc5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x807EDCC5, original_name="CMDL"),
        },
    )
    cmdl_0x708b0155: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x708B0155, original_name="CMDL"),
        },
    )
    cmdl_0xe46803dc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE46803DC, original_name="CMDL"),
        },
    )
    cmdl_0x6a975cff: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6A975CFF, original_name="CMDL"),
        },
    )
    cmdl_0x97e2b6c7: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x97E2B6C7, original_name="CMDL"),
        },
    )
    cmdl_0x1176c469: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1176C469, original_name="CMDL"),
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
        if property_count != 15:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQ")

        dec = _FAST_FORMAT.unpack(data.read(210))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\xdc\xe1\xa9@")  # 0xdce1a940
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xdce1a940))

        data.write(b"\xf4\xc3\x18\xb3")  # 0xf4c318b3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xf4c318b3))

        data.write(b"\xb3g2i")  # 0xb3673269
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xb3673269))

        data.write(b"\xb9\x19m\x9e")  # 0xb9196d9e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xb9196d9e))

        data.write(b"\x8c\x0b\xee\x98")  # 0x8c0bee98
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.important_moment))

        data.write(b"My\x84\xe6")  # 0x4d7984e6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x4d7984e6))

        data.write(b"\x8f\xbeb\x1d")  # 0x8fbe621d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x8fbe621d))

        data.write(b"\x11\xea&Q")  # 0x11ea2651
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x11ea2651))

        data.write(b"VN\x0c\x8b")  # 0x564e0c8b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x564e0c8b))

        data.write(b"\x80~\xdc\xc5")  # 0x807edcc5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x807edcc5))

        data.write(b"p\x8b\x01U")  # 0x708b0155
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x708b0155))

        data.write(b"\xe4h\x03\xdc")  # 0xe46803dc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0xe46803dc))

        data.write(b"j\x97\\\xff")  # 0x6a975cff
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x6a975cff))

        data.write(b"\x97\xe2\xb6\xc7")  # 0x97e2b6c7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x97e2b6c7))

        data.write(b"\x11v\xc4i")  # 0x1176c469
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.cmdl_0x1176c469))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss1ShieldJson", data)
        return cls(
            cmdl_0xdce1a940=json_data["cmdl_0xdce1a940"],
            cmdl_0xf4c318b3=json_data["cmdl_0xf4c318b3"],
            cmdl_0xb3673269=json_data["cmdl_0xb3673269"],
            cmdl_0xb9196d9e=json_data["cmdl_0xb9196d9e"],
            important_moment=json_data["important_moment"],
            cmdl_0x4d7984e6=json_data["cmdl_0x4d7984e6"],
            cmdl_0x8fbe621d=json_data["cmdl_0x8fbe621d"],
            cmdl_0x11ea2651=json_data["cmdl_0x11ea2651"],
            cmdl_0x564e0c8b=json_data["cmdl_0x564e0c8b"],
            cmdl_0x807edcc5=json_data["cmdl_0x807edcc5"],
            cmdl_0x708b0155=json_data["cmdl_0x708b0155"],
            cmdl_0xe46803dc=json_data["cmdl_0xe46803dc"],
            cmdl_0x6a975cff=json_data["cmdl_0x6a975cff"],
            cmdl_0x97e2b6c7=json_data["cmdl_0x97e2b6c7"],
            cmdl_0x1176c469=json_data["cmdl_0x1176c469"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "cmdl_0xdce1a940": self.cmdl_0xdce1a940,
            "cmdl_0xf4c318b3": self.cmdl_0xf4c318b3,
            "cmdl_0xb3673269": self.cmdl_0xb3673269,
            "cmdl_0xb9196d9e": self.cmdl_0xb9196d9e,
            "important_moment": self.important_moment,
            "cmdl_0x4d7984e6": self.cmdl_0x4d7984e6,
            "cmdl_0x8fbe621d": self.cmdl_0x8fbe621d,
            "cmdl_0x11ea2651": self.cmdl_0x11ea2651,
            "cmdl_0x564e0c8b": self.cmdl_0x564e0c8b,
            "cmdl_0x807edcc5": self.cmdl_0x807edcc5,
            "cmdl_0x708b0155": self.cmdl_0x708b0155,
            "cmdl_0xe46803dc": self.cmdl_0xe46803dc,
            "cmdl_0x6a975cff": self.cmdl_0x6a975cff,
            "cmdl_0x97e2b6c7": self.cmdl_0x97e2b6c7,
            "cmdl_0x1176c469": self.cmdl_0x1176c469,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDCE1A940: ("cmdl_0xdce1a940", structs.decode_BIG_Q),
    0xF4C318B3: ("cmdl_0xf4c318b3", structs.decode_BIG_Q),
    0xB3673269: ("cmdl_0xb3673269", structs.decode_BIG_Q),
    0xB9196D9E: ("cmdl_0xb9196d9e", structs.decode_BIG_Q),
    0x8C0BEE98: ("important_moment", structs.decode_BIG_Q),
    0x4D7984E6: ("cmdl_0x4d7984e6", structs.decode_BIG_Q),
    0x8FBE621D: ("cmdl_0x8fbe621d", structs.decode_BIG_Q),
    0x11EA2651: ("cmdl_0x11ea2651", structs.decode_BIG_Q),
    0x564E0C8B: ("cmdl_0x564e0c8b", structs.decode_BIG_Q),
    0x807EDCC5: ("cmdl_0x807edcc5", structs.decode_BIG_Q),
    0x708B0155: ("cmdl_0x708b0155", structs.decode_BIG_Q),
    0xE46803DC: ("cmdl_0xe46803dc", structs.decode_BIG_Q),
    0x6A975CFF: ("cmdl_0x6a975cff", structs.decode_BIG_Q),
    0x97E2B6C7: ("cmdl_0x97e2b6c7", structs.decode_BIG_Q),
    0x1176C469: ("cmdl_0x1176c469", structs.decode_BIG_Q),
}
