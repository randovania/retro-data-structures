# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class VisorParametersJson(typing_extensions.TypedDict):
        scan_through: bool
        visor_flags: int


class VisorFlags(enum.IntFlag):
    Combat = 1
    Scan = 2
    Dark = 4
    Echo = 8

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xFE9DC266, 0xCA19E8C6)


@dataclasses.dataclass()
class VisorParameters(BaseProperty):
    scan_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFE9DC266, original_name="ScanThrough"),
        },
    )
    visor_flags: VisorFlags = dataclasses.field(
        default=VisorFlags(15),
        metadata={
            "reflection": FieldReflection[VisorFlags](
                VisorFlags,
                id=0xCA19E8C6,
                original_name="VisorFlags",
                from_json=VisorFlags.from_json,
                to_json=VisorFlags.to_json,
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
        if property_count != 2:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LHL")

        dec = _FAST_FORMAT.unpack(data.read(17))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            dec[2],
            VisorFlags(dec[5]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\xfe\x9d\xc2f")  # 0xfe9dc266
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scan_through))

        data.write(b"\xca\x19\xe8\xc6")  # 0xca19e8c6
        data.write(b"\x00\x04")  # size
        self.visor_flags.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VisorParametersJson", data)
        return cls(
            scan_through=json_data["scan_through"],
            visor_flags=VisorFlags.from_json(json_data["visor_flags"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan_through": self.scan_through,
            "visor_flags": self.visor_flags.to_json(),
        }


def _decode_visor_flags(data: typing.BinaryIO, game: Game, property_size: int) -> VisorFlags:
    return VisorFlags.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFE9DC266: ("scan_through", structs.decode_BIG_bool_),
    0xCA19E8C6: ("visor_flags", _decode_visor_flags),
}
