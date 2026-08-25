# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GrappleBlock import GrappleBlock
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct9Json(typing_extensions.TypedDict):
        scan_info: int
        unknown_0xead66dd7: float
        unknown_0x7a74aa86: float
        unknown_0x959c653f: float
        unknown_0x0ee58566: float
        grapple_angle_threshold: float
        min_fall_angle: float
        max_fall_angle: float
        unknown_0xb34e89ae: float
        unknown_0xb7d4b884: float
        stunned_grapple_block: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct9(BaseProperty):
    scan_info: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x276A4FC5, original_name="ScanInfo"),
        },
    )
    unknown_0xead66dd7: float = dataclasses.field(
        default=13.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEAD66DD7, original_name="Unknown"),
        },
    )
    unknown_0x7a74aa86: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A74AA86, original_name="Unknown"),
        },
    )
    unknown_0x959c653f: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x959C653F, original_name="Unknown"),
        },
    )
    unknown_0x0ee58566: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0EE58566, original_name="Unknown"),
        },
    )
    grapple_angle_threshold: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x137EF87B, original_name="GrappleAngleThreshold"),
        },
    )
    min_fall_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0B48027B, original_name="MinFallAngle"),
        },
    )
    max_fall_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1EC3D689, original_name="MaxFallAngle"),
        },
    )
    unknown_0xb34e89ae: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB34E89AE, original_name="Unknown"),
        },
    )
    unknown_0xb7d4b884: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB7D4B884, original_name="Unknown"),
        },
    )
    stunned_grapple_block: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0x85543E4E,
                original_name="StunnedGrappleBlock",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x276A4FC5
        scan_info = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEAD66DD7
        unknown_0xead66dd7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A74AA86
        unknown_0x7a74aa86 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x959C653F
        unknown_0x959c653f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0EE58566
        unknown_0x0ee58566 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x137EF87B
        grapple_angle_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B48027B
        min_fall_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1EC3D689
        max_fall_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB34E89AE
        unknown_0xb34e89ae = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7D4B884
        unknown_0xb7d4b884 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85543E4E
        stunned_grapple_block = GrappleBlock.from_stream(data, game, property_size)

        return cls(
            scan_info,
            unknown_0xead66dd7,
            unknown_0x7a74aa86,
            unknown_0x959c653f,
            unknown_0x0ee58566,
            grapple_angle_threshold,
            min_fall_angle,
            max_fall_angle,
            unknown_0xb34e89ae,
            unknown_0xb7d4b884,
            stunned_grapple_block,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"'jO\xc5")  # 0x276a4fc5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_info))

        data.write(b"\xea\xd6m\xd7")  # 0xead66dd7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xead66dd7))

        data.write(b"zt\xaa\x86")  # 0x7a74aa86
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7a74aa86))

        data.write(b"\x95\x9ce?")  # 0x959c653f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x959c653f))

        data.write(b"\x0e\xe5\x85f")  # 0xee58566
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0ee58566))

        data.write(b"\x13~\xf8{")  # 0x137ef87b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_angle_threshold))

        data.write(b"\x0bH\x02{")  # 0xb48027b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_fall_angle))

        data.write(b"\x1e\xc3\xd6\x89")  # 0x1ec3d689
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_fall_angle))

        data.write(b"\xb3N\x89\xae")  # 0xb34e89ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb34e89ae))

        data.write(b"\xb7\xd4\xb8\x84")  # 0xb7d4b884
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb7d4b884))

        data.write(b"\x85T>N")  # 0x85543e4e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stunned_grapple_block.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct9Json", data)
        return cls(
            scan_info=json_data["scan_info"],
            unknown_0xead66dd7=json_data["unknown_0xead66dd7"],
            unknown_0x7a74aa86=json_data["unknown_0x7a74aa86"],
            unknown_0x959c653f=json_data["unknown_0x959c653f"],
            unknown_0x0ee58566=json_data["unknown_0x0ee58566"],
            grapple_angle_threshold=json_data["grapple_angle_threshold"],
            min_fall_angle=json_data["min_fall_angle"],
            max_fall_angle=json_data["max_fall_angle"],
            unknown_0xb34e89ae=json_data["unknown_0xb34e89ae"],
            unknown_0xb7d4b884=json_data["unknown_0xb7d4b884"],
            stunned_grapple_block=GrappleBlock.from_json(json_data["stunned_grapple_block"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan_info": self.scan_info,
            "unknown_0xead66dd7": self.unknown_0xead66dd7,
            "unknown_0x7a74aa86": self.unknown_0x7a74aa86,
            "unknown_0x959c653f": self.unknown_0x959c653f,
            "unknown_0x0ee58566": self.unknown_0x0ee58566,
            "grapple_angle_threshold": self.grapple_angle_threshold,
            "min_fall_angle": self.min_fall_angle,
            "max_fall_angle": self.max_fall_angle,
            "unknown_0xb34e89ae": self.unknown_0xb34e89ae,
            "unknown_0xb7d4b884": self.unknown_0xb7d4b884,
            "stunned_grapple_block": self.stunned_grapple_block.to_json(),
        }


def _decode_stunned_grapple_block(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x276A4FC5: ("scan_info", structs.decode_BIG_Q),
    0xEAD66DD7: ("unknown_0xead66dd7", structs.decode_BIG_f),
    0x7A74AA86: ("unknown_0x7a74aa86", structs.decode_BIG_f),
    0x959C653F: ("unknown_0x959c653f", structs.decode_BIG_f),
    0x0EE58566: ("unknown_0x0ee58566", structs.decode_BIG_f),
    0x137EF87B: ("grapple_angle_threshold", structs.decode_BIG_f),
    0x0B48027B: ("min_fall_angle", structs.decode_BIG_f),
    0x1EC3D689: ("max_fall_angle", structs.decode_BIG_f),
    0xB34E89AE: ("unknown_0xb34e89ae", structs.decode_BIG_f),
    0xB7D4B884: ("unknown_0xb7d4b884", structs.decode_BIG_f),
    0x85543E4E: ("stunned_grapple_block", _decode_stunned_grapple_block),
}
