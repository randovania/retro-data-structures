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

    class VisorParametersJson(typing_extensions.TypedDict):
        scan_through: bool
        visor_flags: int
        unknown: int
        visor_zoom_distance: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xFE9DC266, 0xCA19E8C6, 0x46175A3D, 0xCA6E30B1)


@dataclasses.dataclass()
class VisorParameters(BaseProperty):
    scan_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFE9DC266, original_name="ScanThrough"),
        },
    )
    visor_flags: int = dataclasses.field(
        default=15,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCA19E8C6, original_name="VisorFlags"),
        },
    )  # Flagset
    unknown: int = dataclasses.field(
        default=15,
        metadata={
            "reflection": FieldReflection[int](int, id=0x46175A3D, original_name="Unknown"),
        },
    )
    visor_zoom_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCA6E30B1, original_name="VisorZoomDistance"),
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
            _FAST_FORMAT = struct.Struct(">LH?LHLLHlLHf")

        dec = _FAST_FORMAT.unpack(data.read(37))
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

        data.write(b"\xfe\x9d\xc2f")  # 0xfe9dc266
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scan_through))

        data.write(b"\xca\x19\xe8\xc6")  # 0xca19e8c6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.visor_flags))

        data.write(b"F\x17Z=")  # 0x46175a3d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b"\xcan0\xb1")  # 0xca6e30b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.visor_zoom_distance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VisorParametersJson", data)
        return cls(
            scan_through=json_data["scan_through"],
            visor_flags=json_data["visor_flags"],
            unknown=json_data["unknown"],
            visor_zoom_distance=json_data["visor_zoom_distance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan_through": self.scan_through,
            "visor_flags": self.visor_flags,
            "unknown": self.unknown,
            "visor_zoom_distance": self.visor_zoom_distance,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFE9DC266: ("scan_through", structs.decode_BIG_bool_),
    0xCA19E8C6: ("visor_flags", structs.decode_BIG_L),
    0x46175A3D: ("unknown", structs.decode_BIG_l),
    0xCA6E30B1: ("visor_zoom_distance", structs.decode_BIG_f),
}
