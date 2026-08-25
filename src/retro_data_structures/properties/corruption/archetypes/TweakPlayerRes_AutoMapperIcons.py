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

    class TweakPlayerRes_AutoMapperIconsJson(typing_extensions.TypedDict):
        landing_site: str
        unknown_0xdd1b0445: str
        warp_portal: str
        save_station: str
        map_station: str
        unknown_0xdfac0db1: str
        unknown_0xb838c9c0: str
        unknown_0x5096bfa5: str
        unknown_0x5291eb5f: str
        unknown_0xf4e6e0eb: str
        unknown_0x65700ccc: str
        unknown_0xa0d73242: str


@dataclasses.dataclass()
class TweakPlayerRes_AutoMapperIcons(BaseProperty):
    landing_site: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x1EBA4BD8, original_name="LandingSite"),
        },
    )
    unknown_0xdd1b0445: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xDD1B0445, original_name="Unknown"),
        },
    )
    warp_portal: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xB35B7BEC, original_name="WarpPortal"),
        },
    )
    save_station: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x64667637, original_name="SaveStation"),
        },
    )
    map_station: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xD5D00133, original_name="MapStation"),
        },
    )
    unknown_0xdfac0db1: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xDFAC0DB1, original_name="Unknown"),
        },
    )
    unknown_0xb838c9c0: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xB838C9C0, original_name="Unknown"),
        },
    )
    unknown_0x5096bfa5: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5096BFA5, original_name="Unknown"),
        },
    )
    unknown_0x5291eb5f: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5291EB5F, original_name="Unknown"),
        },
    )
    unknown_0xf4e6e0eb: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xF4E6E0EB, original_name="Unknown"),
        },
    )
    unknown_0x65700ccc: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x65700CCC, original_name="Unknown"),
        },
    )
    unknown_0xa0d73242: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xA0D73242, original_name="Unknown"),
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
        if property_count != 12:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1EBA4BD8
        landing_site = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD1B0445
        unknown_0xdd1b0445 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB35B7BEC
        warp_portal = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64667637
        save_station = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5D00133
        map_station = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFAC0DB1
        unknown_0xdfac0db1 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB838C9C0
        unknown_0xb838c9c0 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5096BFA5
        unknown_0x5096bfa5 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5291EB5F
        unknown_0x5291eb5f = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4E6E0EB
        unknown_0xf4e6e0eb = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65700CCC
        unknown_0x65700ccc = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0D73242
        unknown_0xa0d73242 = data.read(property_size)[:-1].decode("utf-8")

        return cls(
            landing_site,
            unknown_0xdd1b0445,
            warp_portal,
            save_station,
            map_station,
            unknown_0xdfac0db1,
            unknown_0xb838c9c0,
            unknown_0x5096bfa5,
            unknown_0x5291eb5f,
            unknown_0xf4e6e0eb,
            unknown_0x65700ccc,
            unknown_0xa0d73242,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0c")  # 12 properties

        data.write(b"\x1e\xbaK\xd8")  # 0x1eba4bd8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.landing_site.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdd\x1b\x04E")  # 0xdd1b0445
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xdd1b0445.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3[{\xec")  # 0xb35b7bec
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.warp_portal.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"dfv7")  # 0x64667637
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.save_station.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd5\xd0\x013")  # 0xd5d00133
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.map_station.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdf\xac\r\xb1")  # 0xdfac0db1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xdfac0db1.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb88\xc9\xc0")  # 0xb838c9c0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xb838c9c0.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"P\x96\xbf\xa5")  # 0x5096bfa5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x5096bfa5.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"R\x91\xeb_")  # 0x5291eb5f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x5291eb5f.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xe6\xe0\xeb")  # 0xf4e6e0eb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xf4e6e0eb.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"ep\x0c\xcc")  # 0x65700ccc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x65700ccc.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa0\xd72B")  # 0xa0d73242
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xa0d73242.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerRes_AutoMapperIconsJson", data)
        return cls(
            landing_site=json_data["landing_site"],
            unknown_0xdd1b0445=json_data["unknown_0xdd1b0445"],
            warp_portal=json_data["warp_portal"],
            save_station=json_data["save_station"],
            map_station=json_data["map_station"],
            unknown_0xdfac0db1=json_data["unknown_0xdfac0db1"],
            unknown_0xb838c9c0=json_data["unknown_0xb838c9c0"],
            unknown_0x5096bfa5=json_data["unknown_0x5096bfa5"],
            unknown_0x5291eb5f=json_data["unknown_0x5291eb5f"],
            unknown_0xf4e6e0eb=json_data["unknown_0xf4e6e0eb"],
            unknown_0x65700ccc=json_data["unknown_0x65700ccc"],
            unknown_0xa0d73242=json_data["unknown_0xa0d73242"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "landing_site": self.landing_site,
            "unknown_0xdd1b0445": self.unknown_0xdd1b0445,
            "warp_portal": self.warp_portal,
            "save_station": self.save_station,
            "map_station": self.map_station,
            "unknown_0xdfac0db1": self.unknown_0xdfac0db1,
            "unknown_0xb838c9c0": self.unknown_0xb838c9c0,
            "unknown_0x5096bfa5": self.unknown_0x5096bfa5,
            "unknown_0x5291eb5f": self.unknown_0x5291eb5f,
            "unknown_0xf4e6e0eb": self.unknown_0xf4e6e0eb,
            "unknown_0x65700ccc": self.unknown_0x65700ccc,
            "unknown_0xa0d73242": self.unknown_0xa0d73242,
        }


def _decode_landing_site(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xdd1b0445(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_warp_portal(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_save_station(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_map_station(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xdfac0db1(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xb838c9c0(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x5096bfa5(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x5291eb5f(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xf4e6e0eb(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x65700ccc(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xa0d73242(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1EBA4BD8: ("landing_site", _decode_landing_site),
    0xDD1B0445: ("unknown_0xdd1b0445", _decode_unknown_0xdd1b0445),
    0xB35B7BEC: ("warp_portal", _decode_warp_portal),
    0x64667637: ("save_station", _decode_save_station),
    0xD5D00133: ("map_station", _decode_map_station),
    0xDFAC0DB1: ("unknown_0xdfac0db1", _decode_unknown_0xdfac0db1),
    0xB838C9C0: ("unknown_0xb838c9c0", _decode_unknown_0xb838c9c0),
    0x5096BFA5: ("unknown_0x5096bfa5", _decode_unknown_0x5096bfa5),
    0x5291EB5F: ("unknown_0x5291eb5f", _decode_unknown_0x5291eb5f),
    0xF4E6E0EB: ("unknown_0xf4e6e0eb", _decode_unknown_0xf4e6e0eb),
    0x65700CCC: ("unknown_0x65700ccc", _decode_unknown_0x65700ccc),
    0xA0D73242: ("unknown_0xa0d73242", _decode_unknown_0xa0d73242),
}
