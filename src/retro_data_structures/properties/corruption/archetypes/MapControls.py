# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MapControlsJson(typing_extensions.TypedDict):
        unknown_0xfed78da3: json_util.JsonObject
        unknown_0x74e647c1: json_util.JsonObject
        unknown_0xdccf07b6: json_util.JsonObject
        unknown_0x56ae8c3b: json_util.JsonObject
        unknown_0xbbd5fc52: json_util.JsonObject
        unknown_0x19a0c4cb: json_util.JsonObject
        unknown_0x827c4e63: json_util.JsonObject
        unknown_0x0001f679: json_util.JsonObject
        unknown_0xfb5628fa: json_util.JsonObject
        unknown_0x571bf6d0: json_util.JsonObject
        unknown_0xcfaa0627: json_util.JsonObject
        unknown_0x385cbd2f: json_util.JsonObject
        unknown_0x5f55ccca: json_util.JsonObject
        unknown_0x85e1418d: json_util.JsonObject
        unknown_0xb5f75bfb: json_util.JsonObject
        unknown_0x31c2d282: json_util.JsonObject
        unknown_0xfaa6abe5: json_util.JsonObject
        unknown_0xdda39041: json_util.JsonObject
        unknown_0x705876ab: json_util.JsonObject
        unknown_0x1203801f: json_util.JsonObject
        unknown_0x98620b92: json_util.JsonObject
        unknown_0x14112b99: json_util.JsonObject


@dataclasses.dataclass()
class MapControls(BaseProperty):
    unknown_0xfed78da3: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xFED78DA3,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x74e647c1: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x74E647C1,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xdccf07b6: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xDCCF07B6,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x56ae8c3b: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x56AE8C3B,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xbbd5fc52: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xBBD5FC52,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x19a0c4cb: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x19A0C4CB,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x827c4e63: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x827C4E63,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x0001f679: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x0001F679,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xfb5628fa: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xFB5628FA,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x571bf6d0: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x571BF6D0,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xcfaa0627: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xCFAA0627,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x385cbd2f: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x385CBD2F,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x5f55ccca: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x5F55CCCA,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x85e1418d: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x85E1418D,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xb5f75bfb: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xB5F75BFB,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x31c2d282: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x31C2D282,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xfaa6abe5: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xFAA6ABE5,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xdda39041: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xDDA39041,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x705876ab: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x705876AB,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x1203801f: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x1203801F,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x98620b92: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x98620B92,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x14112b99: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x14112B99,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
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
        if property_count != 22:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFED78DA3
        unknown_0xfed78da3 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74E647C1
        unknown_0x74e647c1 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCCF07B6
        unknown_0xdccf07b6 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56AE8C3B
        unknown_0x56ae8c3b = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBBD5FC52
        unknown_0xbbd5fc52 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19A0C4CB
        unknown_0x19a0c4cb = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x827C4E63
        unknown_0x827c4e63 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0001F679
        unknown_0x0001f679 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB5628FA
        unknown_0xfb5628fa = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x571BF6D0
        unknown_0x571bf6d0 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFAA0627
        unknown_0xcfaa0627 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385CBD2F
        unknown_0x385cbd2f = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F55CCCA
        unknown_0x5f55ccca = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85E1418D
        unknown_0x85e1418d = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5F75BFB
        unknown_0xb5f75bfb = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31C2D282
        unknown_0x31c2d282 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFAA6ABE5
        unknown_0xfaa6abe5 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDDA39041
        unknown_0xdda39041 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x705876AB
        unknown_0x705876ab = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1203801F
        unknown_0x1203801f = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98620B92
        unknown_0x98620b92 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14112B99
        unknown_0x14112b99 = RevolutionControl.from_stream(data, game, property_size)

        return cls(
            unknown_0xfed78da3,
            unknown_0x74e647c1,
            unknown_0xdccf07b6,
            unknown_0x56ae8c3b,
            unknown_0xbbd5fc52,
            unknown_0x19a0c4cb,
            unknown_0x827c4e63,
            unknown_0x0001f679,
            unknown_0xfb5628fa,
            unknown_0x571bf6d0,
            unknown_0xcfaa0627,
            unknown_0x385cbd2f,
            unknown_0x5f55ccca,
            unknown_0x85e1418d,
            unknown_0xb5f75bfb,
            unknown_0x31c2d282,
            unknown_0xfaa6abe5,
            unknown_0xdda39041,
            unknown_0x705876ab,
            unknown_0x1203801f,
            unknown_0x98620b92,
            unknown_0x14112b99,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x16")  # 22 properties

        data.write(b"\xfe\xd7\x8d\xa3")  # 0xfed78da3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xfed78da3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"t\xe6G\xc1")  # 0x74e647c1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x74e647c1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdc\xcf\x07\xb6")  # 0xdccf07b6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xdccf07b6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"V\xae\x8c;")  # 0x56ae8c3b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x56ae8c3b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbb\xd5\xfcR")  # 0xbbd5fc52
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xbbd5fc52.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\xa0\xc4\xcb")  # 0x19a0c4cb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x19a0c4cb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x82|Nc")  # 0x827c4e63
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x827c4e63.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\x01\xf6y")  # 0x1f679
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x0001f679.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfbV(\xfa")  # 0xfb5628fa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xfb5628fa.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"W\x1b\xf6\xd0")  # 0x571bf6d0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x571bf6d0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcf\xaa\x06'")  # 0xcfaa0627
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xcfaa0627.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"8\\\xbd/")  # 0x385cbd2f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x385cbd2f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_U\xcc\xca")  # 0x5f55ccca
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x5f55ccca.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x85\xe1A\x8d")  # 0x85e1418d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x85e1418d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb5\xf7[\xfb")  # 0xb5f75bfb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xb5f75bfb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"1\xc2\xd2\x82")  # 0x31c2d282
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x31c2d282.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfa\xa6\xab\xe5")  # 0xfaa6abe5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xfaa6abe5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdd\xa3\x90A")  # 0xdda39041
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xdda39041.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"pXv\xab")  # 0x705876ab
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x705876ab.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x12\x03\x80\x1f")  # 0x1203801f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x1203801f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x98b\x0b\x92")  # 0x98620b92
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x98620b92.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x14\x11+\x99")  # 0x14112b99
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x14112b99.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MapControlsJson", data)
        return cls(
            unknown_0xfed78da3=RevolutionControl.from_json(json_data["unknown_0xfed78da3"]),
            unknown_0x74e647c1=RevolutionControl.from_json(json_data["unknown_0x74e647c1"]),
            unknown_0xdccf07b6=RevolutionControl.from_json(json_data["unknown_0xdccf07b6"]),
            unknown_0x56ae8c3b=RevolutionControl.from_json(json_data["unknown_0x56ae8c3b"]),
            unknown_0xbbd5fc52=RevolutionControl.from_json(json_data["unknown_0xbbd5fc52"]),
            unknown_0x19a0c4cb=RevolutionControl.from_json(json_data["unknown_0x19a0c4cb"]),
            unknown_0x827c4e63=RevolutionControl.from_json(json_data["unknown_0x827c4e63"]),
            unknown_0x0001f679=RevolutionControl.from_json(json_data["unknown_0x0001f679"]),
            unknown_0xfb5628fa=RevolutionControl.from_json(json_data["unknown_0xfb5628fa"]),
            unknown_0x571bf6d0=RevolutionControl.from_json(json_data["unknown_0x571bf6d0"]),
            unknown_0xcfaa0627=RevolutionControl.from_json(json_data["unknown_0xcfaa0627"]),
            unknown_0x385cbd2f=RevolutionControl.from_json(json_data["unknown_0x385cbd2f"]),
            unknown_0x5f55ccca=RevolutionControl.from_json(json_data["unknown_0x5f55ccca"]),
            unknown_0x85e1418d=RevolutionControl.from_json(json_data["unknown_0x85e1418d"]),
            unknown_0xb5f75bfb=RevolutionControl.from_json(json_data["unknown_0xb5f75bfb"]),
            unknown_0x31c2d282=RevolutionControl.from_json(json_data["unknown_0x31c2d282"]),
            unknown_0xfaa6abe5=RevolutionControl.from_json(json_data["unknown_0xfaa6abe5"]),
            unknown_0xdda39041=RevolutionControl.from_json(json_data["unknown_0xdda39041"]),
            unknown_0x705876ab=RevolutionControl.from_json(json_data["unknown_0x705876ab"]),
            unknown_0x1203801f=RevolutionControl.from_json(json_data["unknown_0x1203801f"]),
            unknown_0x98620b92=RevolutionControl.from_json(json_data["unknown_0x98620b92"]),
            unknown_0x14112b99=RevolutionControl.from_json(json_data["unknown_0x14112b99"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xfed78da3": self.unknown_0xfed78da3.to_json(),
            "unknown_0x74e647c1": self.unknown_0x74e647c1.to_json(),
            "unknown_0xdccf07b6": self.unknown_0xdccf07b6.to_json(),
            "unknown_0x56ae8c3b": self.unknown_0x56ae8c3b.to_json(),
            "unknown_0xbbd5fc52": self.unknown_0xbbd5fc52.to_json(),
            "unknown_0x19a0c4cb": self.unknown_0x19a0c4cb.to_json(),
            "unknown_0x827c4e63": self.unknown_0x827c4e63.to_json(),
            "unknown_0x0001f679": self.unknown_0x0001f679.to_json(),
            "unknown_0xfb5628fa": self.unknown_0xfb5628fa.to_json(),
            "unknown_0x571bf6d0": self.unknown_0x571bf6d0.to_json(),
            "unknown_0xcfaa0627": self.unknown_0xcfaa0627.to_json(),
            "unknown_0x385cbd2f": self.unknown_0x385cbd2f.to_json(),
            "unknown_0x5f55ccca": self.unknown_0x5f55ccca.to_json(),
            "unknown_0x85e1418d": self.unknown_0x85e1418d.to_json(),
            "unknown_0xb5f75bfb": self.unknown_0xb5f75bfb.to_json(),
            "unknown_0x31c2d282": self.unknown_0x31c2d282.to_json(),
            "unknown_0xfaa6abe5": self.unknown_0xfaa6abe5.to_json(),
            "unknown_0xdda39041": self.unknown_0xdda39041.to_json(),
            "unknown_0x705876ab": self.unknown_0x705876ab.to_json(),
            "unknown_0x1203801f": self.unknown_0x1203801f.to_json(),
            "unknown_0x98620b92": self.unknown_0x98620b92.to_json(),
            "unknown_0x14112b99": self.unknown_0x14112b99.to_json(),
        }


def _decode_unknown_0xfed78da3(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x74e647c1(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xdccf07b6(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x56ae8c3b(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xbbd5fc52(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x19a0c4cb(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x827c4e63(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x0001f679(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xfb5628fa(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x571bf6d0(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xcfaa0627(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x385cbd2f(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x5f55ccca(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x85e1418d(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xb5f75bfb(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x31c2d282(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xfaa6abe5(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xdda39041(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x705876ab(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x1203801f(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x98620b92(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x14112b99(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFED78DA3: ("unknown_0xfed78da3", _decode_unknown_0xfed78da3),
    0x74E647C1: ("unknown_0x74e647c1", _decode_unknown_0x74e647c1),
    0xDCCF07B6: ("unknown_0xdccf07b6", _decode_unknown_0xdccf07b6),
    0x56AE8C3B: ("unknown_0x56ae8c3b", _decode_unknown_0x56ae8c3b),
    0xBBD5FC52: ("unknown_0xbbd5fc52", _decode_unknown_0xbbd5fc52),
    0x19A0C4CB: ("unknown_0x19a0c4cb", _decode_unknown_0x19a0c4cb),
    0x827C4E63: ("unknown_0x827c4e63", _decode_unknown_0x827c4e63),
    0x0001F679: ("unknown_0x0001f679", _decode_unknown_0x0001f679),
    0xFB5628FA: ("unknown_0xfb5628fa", _decode_unknown_0xfb5628fa),
    0x571BF6D0: ("unknown_0x571bf6d0", _decode_unknown_0x571bf6d0),
    0xCFAA0627: ("unknown_0xcfaa0627", _decode_unknown_0xcfaa0627),
    0x385CBD2F: ("unknown_0x385cbd2f", _decode_unknown_0x385cbd2f),
    0x5F55CCCA: ("unknown_0x5f55ccca", _decode_unknown_0x5f55ccca),
    0x85E1418D: ("unknown_0x85e1418d", _decode_unknown_0x85e1418d),
    0xB5F75BFB: ("unknown_0xb5f75bfb", _decode_unknown_0xb5f75bfb),
    0x31C2D282: ("unknown_0x31c2d282", _decode_unknown_0x31c2d282),
    0xFAA6ABE5: ("unknown_0xfaa6abe5", _decode_unknown_0xfaa6abe5),
    0xDDA39041: ("unknown_0xdda39041", _decode_unknown_0xdda39041),
    0x705876AB: ("unknown_0x705876ab", _decode_unknown_0x705876ab),
    0x1203801F: ("unknown_0x1203801f", _decode_unknown_0x1203801f),
    0x98620B92: ("unknown_0x98620b92", _decode_unknown_0x98620b92),
    0x14112B99: ("unknown_0x14112b99", _decode_unknown_0x14112b99),
}
