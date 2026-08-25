# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayerRes_MapScreenIconsJson(typing_extensions.TypedDict):
        l_stick_n: str
        l_stick_u: str
        l_stick_ul: str
        l_stick_l: str
        l_stick_dl: str
        l_stick_d: str
        l_stick_dr: str
        l_stick_r: str
        l_stick_ur: str
        c_stick_n: str
        c_stick_u: str
        c_stick_ul: str
        c_stick_l: str
        c_stick_dl: str
        c_stick_d: str
        c_stick_dr: str
        c_stick_r: str
        c_stick_ur: str
        l_trigger_out: str
        l_trigger_in: str
        r_trigger_out: str
        r_trigger_in: str
        start_button_out: str
        start_button_in: str
        a_button_out: str
        a_button_in: str
        b_button_out: str
        b_button_in: str
        x_button_out: str
        x_button_in: str
        y_button_out: str
        y_button_in: str


@dataclasses.dataclass()
class TweakPlayerRes_MapScreenIcons(BaseProperty):
    l_stick_n: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x2C770BB8, original_name="LStickN"),
        },
    )
    l_stick_u: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x49AEC38C, original_name="LStickU"),
        },
    )
    l_stick_ul: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xA86AF8C2, original_name="LStickUL"),
        },
    )
    l_stick_l: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xBBE81A91, original_name="LStickL"),
        },
    )
    l_stick_dl: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x187BC977, original_name="LStickDL"),
        },
    )
    l_stick_d: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x880754F6, original_name="LStickD"),
        },
    )
    l_stick_dr: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x2F9A2EE4, original_name="LStickDR"),
        },
    )
    l_stick_r: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x8C09FD02, original_name="LStickR"),
        },
    )
    l_stick_ur: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x9F8B1F51, original_name="LStickUR"),
        },
    )
    c_stick_n: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x0B07DE8D, original_name="CStickN"),
        },
    )
    c_stick_u: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x6EDE16B9, original_name="CStickU"),
        },
    )
    c_stick_ul: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xFEFE4C34, original_name="CStickUL"),
        },
    )
    c_stick_l: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x9C98CFA4, original_name="CStickL"),
        },
    )
    c_stick_dl: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x4EEF7D81, original_name="CStickDL"),
        },
    )
    c_stick_d: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xAF7781C3, original_name="CStickD"),
        },
    )
    c_stick_dr: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x790E9A12, original_name="CStickDR"),
        },
    )
    c_stick_r: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xAB792837, original_name="CStickR"),
        },
    )
    c_stick_ur: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xC91FABA7, original_name="CStickUR"),
        },
    )
    l_trigger_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x40C21E1E, original_name="LTriggerOut"),
        },
    )
    l_trigger_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x120368B8, original_name="LTriggerIn"),
        },
    )
    r_trigger_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x16B77FF5, original_name="RTriggerOut"),
        },
    )
    r_trigger_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xD4A6A08D, original_name="RTriggerIn"),
        },
    )
    start_button_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x272F08B4, original_name="StartButtonOut"),
        },
    )
    start_button_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x225F0E23, original_name="StartButtonIn"),
        },
    )
    a_button_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x1C208AB1, original_name="AButtonOut"),
        },
    )
    a_button_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x43FDC303, original_name="AButtonIn"),
        },
    )
    b_button_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x35E83E43, original_name="BButtonOut"),
        },
    )
    b_button_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5280A97A, original_name="BButtonIn"),
        },
    )
    x_button_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x277CBAF1, original_name="XButtonOut"),
        },
    )
    x_button_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x71ED4B23, original_name="XButtonIn"),
        },
    )
    y_button_out: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x89142B60, original_name="YButtonOut"),
        },
    )
    y_button_in: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xC81690CB, original_name="YButtonIn"),
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
        if property_count != 32:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C770BB8
        l_stick_n = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49AEC38C
        l_stick_u = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA86AF8C2
        l_stick_ul = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBBE81A91
        l_stick_l = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x187BC977
        l_stick_dl = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x880754F6
        l_stick_d = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F9A2EE4
        l_stick_dr = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8C09FD02
        l_stick_r = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F8B1F51
        l_stick_ur = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B07DE8D
        c_stick_n = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6EDE16B9
        c_stick_u = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFEFE4C34
        c_stick_ul = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C98CFA4
        c_stick_l = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EEF7D81
        c_stick_dl = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF7781C3
        c_stick_d = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x790E9A12
        c_stick_dr = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB792837
        c_stick_r = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC91FABA7
        c_stick_ur = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40C21E1E
        l_trigger_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x120368B8
        l_trigger_in = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16B77FF5
        r_trigger_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4A6A08D
        r_trigger_in = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x272F08B4
        start_button_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x225F0E23
        start_button_in = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C208AB1
        a_button_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43FDC303
        a_button_in = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35E83E43
        b_button_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5280A97A
        b_button_in = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x277CBAF1
        x_button_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71ED4B23
        x_button_in = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89142B60
        y_button_out = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC81690CB
        y_button_in = data.read(property_size)[:-1].decode("utf-8")

        return cls(
            l_stick_n,
            l_stick_u,
            l_stick_ul,
            l_stick_l,
            l_stick_dl,
            l_stick_d,
            l_stick_dr,
            l_stick_r,
            l_stick_ur,
            c_stick_n,
            c_stick_u,
            c_stick_ul,
            c_stick_l,
            c_stick_dl,
            c_stick_d,
            c_stick_dr,
            c_stick_r,
            c_stick_ur,
            l_trigger_out,
            l_trigger_in,
            r_trigger_out,
            r_trigger_in,
            start_button_out,
            start_button_in,
            a_button_out,
            a_button_in,
            b_button_out,
            b_button_in,
            x_button_out,
            x_button_in,
            y_button_out,
            y_button_in,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00 ")  # 32 properties

        data.write(b",w\x0b\xb8")  # 0x2c770bb8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_n.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"I\xae\xc3\x8c")  # 0x49aec38c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_u.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa8j\xf8\xc2")  # 0xa86af8c2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_ul.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbb\xe8\x1a\x91")  # 0xbbe81a91
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_l.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x18{\xc9w")  # 0x187bc977
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_dl.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x88\x07T\xf6")  # 0x880754f6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_d.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"/\x9a.\xe4")  # 0x2f9a2ee4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_dr.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8c\t\xfd\x02")  # 0x8c09fd02
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_r.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9f\x8b\x1fQ")  # 0x9f8b1f51
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_stick_ur.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0b\x07\xde\x8d")  # 0xb07de8d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_n.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"n\xde\x16\xb9")  # 0x6ede16b9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_u.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfe\xfeL4")  # 0xfefe4c34
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_ul.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9c\x98\xcf\xa4")  # 0x9c98cfa4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_l.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"N\xef}\x81")  # 0x4eef7d81
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_dl.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xafw\x81\xc3")  # 0xaf7781c3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_d.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"y\x0e\x9a\x12")  # 0x790e9a12
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_dr.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaby(7")  # 0xab792837
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_r.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc9\x1f\xab\xa7")  # 0xc91faba7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.c_stick_ur.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"@\xc2\x1e\x1e")  # 0x40c21e1e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_trigger_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x12\x03h\xb8")  # 0x120368b8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.l_trigger_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x16\xb7\x7f\xf5")  # 0x16b77ff5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.r_trigger_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd4\xa6\xa0\x8d")  # 0xd4a6a08d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.r_trigger_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'/\x08\xb4")  # 0x272f08b4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.start_button_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'"_\x0e#')  # 0x225f0e23
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.start_button_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1c \x8a\xb1")  # 0x1c208ab1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.a_button_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"C\xfd\xc3\x03")  # 0x43fdc303
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.a_button_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"5\xe8>C")  # 0x35e83e43
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.b_button_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"R\x80\xa9z")  # 0x5280a97a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.b_button_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'|\xba\xf1")  # 0x277cbaf1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.x_button_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"q\xedK#")  # 0x71ed4b23
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.x_button_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x89\x14+`")  # 0x89142b60
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.y_button_out.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc8\x16\x90\xcb")  # 0xc81690cb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.y_button_in.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerRes_MapScreenIconsJson", data)
        return cls(
            l_stick_n=json_data["l_stick_n"],
            l_stick_u=json_data["l_stick_u"],
            l_stick_ul=json_data["l_stick_ul"],
            l_stick_l=json_data["l_stick_l"],
            l_stick_dl=json_data["l_stick_dl"],
            l_stick_d=json_data["l_stick_d"],
            l_stick_dr=json_data["l_stick_dr"],
            l_stick_r=json_data["l_stick_r"],
            l_stick_ur=json_data["l_stick_ur"],
            c_stick_n=json_data["c_stick_n"],
            c_stick_u=json_data["c_stick_u"],
            c_stick_ul=json_data["c_stick_ul"],
            c_stick_l=json_data["c_stick_l"],
            c_stick_dl=json_data["c_stick_dl"],
            c_stick_d=json_data["c_stick_d"],
            c_stick_dr=json_data["c_stick_dr"],
            c_stick_r=json_data["c_stick_r"],
            c_stick_ur=json_data["c_stick_ur"],
            l_trigger_out=json_data["l_trigger_out"],
            l_trigger_in=json_data["l_trigger_in"],
            r_trigger_out=json_data["r_trigger_out"],
            r_trigger_in=json_data["r_trigger_in"],
            start_button_out=json_data["start_button_out"],
            start_button_in=json_data["start_button_in"],
            a_button_out=json_data["a_button_out"],
            a_button_in=json_data["a_button_in"],
            b_button_out=json_data["b_button_out"],
            b_button_in=json_data["b_button_in"],
            x_button_out=json_data["x_button_out"],
            x_button_in=json_data["x_button_in"],
            y_button_out=json_data["y_button_out"],
            y_button_in=json_data["y_button_in"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "l_stick_n": self.l_stick_n,
            "l_stick_u": self.l_stick_u,
            "l_stick_ul": self.l_stick_ul,
            "l_stick_l": self.l_stick_l,
            "l_stick_dl": self.l_stick_dl,
            "l_stick_d": self.l_stick_d,
            "l_stick_dr": self.l_stick_dr,
            "l_stick_r": self.l_stick_r,
            "l_stick_ur": self.l_stick_ur,
            "c_stick_n": self.c_stick_n,
            "c_stick_u": self.c_stick_u,
            "c_stick_ul": self.c_stick_ul,
            "c_stick_l": self.c_stick_l,
            "c_stick_dl": self.c_stick_dl,
            "c_stick_d": self.c_stick_d,
            "c_stick_dr": self.c_stick_dr,
            "c_stick_r": self.c_stick_r,
            "c_stick_ur": self.c_stick_ur,
            "l_trigger_out": self.l_trigger_out,
            "l_trigger_in": self.l_trigger_in,
            "r_trigger_out": self.r_trigger_out,
            "r_trigger_in": self.r_trigger_in,
            "start_button_out": self.start_button_out,
            "start_button_in": self.start_button_in,
            "a_button_out": self.a_button_out,
            "a_button_in": self.a_button_in,
            "b_button_out": self.b_button_out,
            "b_button_in": self.b_button_in,
            "x_button_out": self.x_button_out,
            "x_button_in": self.x_button_in,
            "y_button_out": self.y_button_out,
            "y_button_in": self.y_button_in,
        }


def _decode_l_stick_n(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_u(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_ul(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_l(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_dl(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_d(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_dr(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_r(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_stick_ur(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_n(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_u(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_ul(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_l(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_dl(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_d(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_dr(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_r(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_c_stick_ur(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_trigger_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_l_trigger_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_r_trigger_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_r_trigger_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_start_button_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_start_button_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_a_button_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_a_button_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_b_button_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_b_button_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_x_button_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_x_button_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_y_button_out(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_y_button_in(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2C770BB8: ("l_stick_n", _decode_l_stick_n),
    0x49AEC38C: ("l_stick_u", _decode_l_stick_u),
    0xA86AF8C2: ("l_stick_ul", _decode_l_stick_ul),
    0xBBE81A91: ("l_stick_l", _decode_l_stick_l),
    0x187BC977: ("l_stick_dl", _decode_l_stick_dl),
    0x880754F6: ("l_stick_d", _decode_l_stick_d),
    0x2F9A2EE4: ("l_stick_dr", _decode_l_stick_dr),
    0x8C09FD02: ("l_stick_r", _decode_l_stick_r),
    0x9F8B1F51: ("l_stick_ur", _decode_l_stick_ur),
    0x0B07DE8D: ("c_stick_n", _decode_c_stick_n),
    0x6EDE16B9: ("c_stick_u", _decode_c_stick_u),
    0xFEFE4C34: ("c_stick_ul", _decode_c_stick_ul),
    0x9C98CFA4: ("c_stick_l", _decode_c_stick_l),
    0x4EEF7D81: ("c_stick_dl", _decode_c_stick_dl),
    0xAF7781C3: ("c_stick_d", _decode_c_stick_d),
    0x790E9A12: ("c_stick_dr", _decode_c_stick_dr),
    0xAB792837: ("c_stick_r", _decode_c_stick_r),
    0xC91FABA7: ("c_stick_ur", _decode_c_stick_ur),
    0x40C21E1E: ("l_trigger_out", _decode_l_trigger_out),
    0x120368B8: ("l_trigger_in", _decode_l_trigger_in),
    0x16B77FF5: ("r_trigger_out", _decode_r_trigger_out),
    0xD4A6A08D: ("r_trigger_in", _decode_r_trigger_in),
    0x272F08B4: ("start_button_out", _decode_start_button_out),
    0x225F0E23: ("start_button_in", _decode_start_button_in),
    0x1C208AB1: ("a_button_out", _decode_a_button_out),
    0x43FDC303: ("a_button_in", _decode_a_button_in),
    0x35E83E43: ("b_button_out", _decode_b_button_out),
    0x5280A97A: ("b_button_in", _decode_b_button_in),
    0x277CBAF1: ("x_button_out", _decode_x_button_out),
    0x71ED4B23: ("x_button_in", _decode_x_button_in),
    0x89142B60: ("y_button_out", _decode_y_button_out),
    0xC81690CB: ("y_button_in", _decode_y_button_in),
}
