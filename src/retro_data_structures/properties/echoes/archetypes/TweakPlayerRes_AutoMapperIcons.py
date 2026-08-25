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

    class TweakPlayerRes_AutoMapperIconsJson(typing_extensions.TypedDict):
        save_station_icon: str
        missile_station_icon: str
        elevator_icon_icon: str
        portal_icon: str
        unknown_0xfbf479ec: str
        unknown_0x5566b6e4: str
        unknown_0x51fe3f1f: str
        unknown_0xa4127a5a: str
        translator_door_icon: str
        unknown_0x5096bfa5: str
        unknown_0xf4e6e0eb: str
        unknown_0x65700ccc: str
        unknown_0xa0d73242: str


@dataclasses.dataclass()
class TweakPlayerRes_AutoMapperIcons(BaseProperty):
    save_station_icon: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xE7014CDA, original_name="SaveStationIcon"),
        },
    )
    missile_station_icon: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x33C94749, original_name="MissileStationIcon"),
        },
    )
    elevator_icon_icon: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x9B36949E, original_name="ElevatorIconIcon"),
        },
    )
    portal_icon: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xAFA1B87C, original_name="PortalIcon"),
        },
    )
    unknown_0xfbf479ec: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xFBF479EC, original_name="Unknown"),
        },
    )
    unknown_0x5566b6e4: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5566B6E4, original_name="Unknown"),
        },
    )
    unknown_0x51fe3f1f: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x51FE3F1F, original_name="Unknown"),
        },
    )
    unknown_0xa4127a5a: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xA4127A5A, original_name="Unknown"),
        },
    )
    translator_door_icon: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0xF8403D18, original_name="TranslatorDoorIcon"),
        },
    )
    unknown_0x5096bfa5: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x5096BFA5, original_name="Unknown"),
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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7014CDA
        save_station_icon = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33C94749
        missile_station_icon = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B36949E
        elevator_icon_icon = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFA1B87C
        portal_icon = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBF479EC
        unknown_0xfbf479ec = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5566B6E4
        unknown_0x5566b6e4 = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51FE3F1F
        unknown_0x51fe3f1f = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4127A5A
        unknown_0xa4127a5a = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8403D18
        translator_door_icon = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5096BFA5
        unknown_0x5096bfa5 = data.read(property_size)[:-1].decode("utf-8")

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
            save_station_icon,
            missile_station_icon,
            elevator_icon_icon,
            portal_icon,
            unknown_0xfbf479ec,
            unknown_0x5566b6e4,
            unknown_0x51fe3f1f,
            unknown_0xa4127a5a,
            translator_door_icon,
            unknown_0x5096bfa5,
            unknown_0xf4e6e0eb,
            unknown_0x65700ccc,
            unknown_0xa0d73242,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x00\t")  # 9 properties
        num_properties_written = 9

        data.write(b"\xe7\x01L\xda")  # 0xe7014cda
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.save_station_icon.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\xc9GI")  # 0x33c94749
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.missile_station_icon.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9b6\x94\x9e")  # 0x9b36949e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.elevator_icon_icon.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaf\xa1\xb8|")  # 0xafa1b87c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.portal_icon.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfb\xf4y\xec")  # 0xfbf479ec
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xfbf479ec.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Uf\xb6\xe4")  # 0x5566b6e4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x5566b6e4.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Q\xfe?\x1f")  # 0x51fe3f1f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0x51fe3f1f.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa4\x12zZ")  # 0xa4127a5a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.unknown_0xa4127a5a.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf8@=\x18")  # 0xf8403d18
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.translator_door_icon.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.unknown_0x5096bfa5 != default_override.get("unknown_0x5096bfa5", ""):
            num_properties_written += 1
            data.write(b"P\x96\xbf\xa5")  # 0x5096bfa5
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            data.write(self.unknown_0x5096bfa5.encode("utf-8"))
            data.write(b"\x00")
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.unknown_0xf4e6e0eb != default_override.get("unknown_0xf4e6e0eb", ""):
            num_properties_written += 1
            data.write(b"\xf4\xe6\xe0\xeb")  # 0xf4e6e0eb
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            data.write(self.unknown_0xf4e6e0eb.encode("utf-8"))
            data.write(b"\x00")
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.unknown_0x65700ccc != default_override.get("unknown_0x65700ccc", ""):
            num_properties_written += 1
            data.write(b"ep\x0c\xcc")  # 0x65700ccc
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            data.write(self.unknown_0x65700ccc.encode("utf-8"))
            data.write(b"\x00")
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.unknown_0xa0d73242 != default_override.get("unknown_0xa0d73242", ""):
            num_properties_written += 1
            data.write(b"\xa0\xd72B")  # 0xa0d73242
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            data.write(self.unknown_0xa0d73242.encode("utf-8"))
            data.write(b"\x00")
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if num_properties_written != 9:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerRes_AutoMapperIconsJson", data)
        return cls(
            save_station_icon=json_data["save_station_icon"],
            missile_station_icon=json_data["missile_station_icon"],
            elevator_icon_icon=json_data["elevator_icon_icon"],
            portal_icon=json_data["portal_icon"],
            unknown_0xfbf479ec=json_data["unknown_0xfbf479ec"],
            unknown_0x5566b6e4=json_data["unknown_0x5566b6e4"],
            unknown_0x51fe3f1f=json_data["unknown_0x51fe3f1f"],
            unknown_0xa4127a5a=json_data["unknown_0xa4127a5a"],
            translator_door_icon=json_data["translator_door_icon"],
            unknown_0x5096bfa5=json_data["unknown_0x5096bfa5"],
            unknown_0xf4e6e0eb=json_data["unknown_0xf4e6e0eb"],
            unknown_0x65700ccc=json_data["unknown_0x65700ccc"],
            unknown_0xa0d73242=json_data["unknown_0xa0d73242"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "save_station_icon": self.save_station_icon,
            "missile_station_icon": self.missile_station_icon,
            "elevator_icon_icon": self.elevator_icon_icon,
            "portal_icon": self.portal_icon,
            "unknown_0xfbf479ec": self.unknown_0xfbf479ec,
            "unknown_0x5566b6e4": self.unknown_0x5566b6e4,
            "unknown_0x51fe3f1f": self.unknown_0x51fe3f1f,
            "unknown_0xa4127a5a": self.unknown_0xa4127a5a,
            "translator_door_icon": self.translator_door_icon,
            "unknown_0x5096bfa5": self.unknown_0x5096bfa5,
            "unknown_0xf4e6e0eb": self.unknown_0xf4e6e0eb,
            "unknown_0x65700ccc": self.unknown_0x65700ccc,
            "unknown_0xa0d73242": self.unknown_0xa0d73242,
        }


def _decode_save_station_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_missile_station_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_elevator_icon_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_portal_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xfbf479ec(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x5566b6e4(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x51fe3f1f(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xa4127a5a(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_translator_door_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x5096bfa5(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xf4e6e0eb(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0x65700ccc(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_unknown_0xa0d73242(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xE7014CDA: ("save_station_icon", _decode_save_station_icon),
    0x33C94749: ("missile_station_icon", _decode_missile_station_icon),
    0x9B36949E: ("elevator_icon_icon", _decode_elevator_icon_icon),
    0xAFA1B87C: ("portal_icon", _decode_portal_icon),
    0xFBF479EC: ("unknown_0xfbf479ec", _decode_unknown_0xfbf479ec),
    0x5566B6E4: ("unknown_0x5566b6e4", _decode_unknown_0x5566b6e4),
    0x51FE3F1F: ("unknown_0x51fe3f1f", _decode_unknown_0x51fe3f1f),
    0xA4127A5A: ("unknown_0xa4127a5a", _decode_unknown_0xa4127a5a),
    0xF8403D18: ("translator_door_icon", _decode_translator_door_icon),
    0x5096BFA5: ("unknown_0x5096bfa5", _decode_unknown_0x5096bfa5),
    0xF4E6E0EB: ("unknown_0xf4e6e0eb", _decode_unknown_0xf4e6e0eb),
    0x65700CCC: ("unknown_0x65700ccc", _decode_unknown_0x65700ccc),
    0xA0D73242: ("unknown_0xa0d73242", _decode_unknown_0xa0d73242),
}
