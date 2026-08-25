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

    class VisorsJson(typing_extensions.TypedDict):
        scan_visor: bool
        command_visor: bool
        x_ray_visor: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x586A8F75, 0x4FCA2A9, 0xF55DD02C)


@dataclasses.dataclass()
class Visors(BaseProperty):
    scan_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x586A8F75, original_name="ScanVisor"),
        },
    )
    command_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x04FCA2A9, original_name="CommandVisor"),
        },
    )
    x_ray_visor: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF55DD02C, original_name="XRayVisor"),
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
        if property_count != 3:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LH?LH?")

        dec = _FAST_FORMAT.unpack(data.read(21))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"Xj\x8fu")  # 0x586a8f75
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scan_visor))

        data.write(b"\x04\xfc\xa2\xa9")  # 0x4fca2a9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.command_visor))

        data.write(b"\xf5]\xd0,")  # 0xf55dd02c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.x_ray_visor))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VisorsJson", data)
        return cls(
            scan_visor=json_data["scan_visor"],
            command_visor=json_data["command_visor"],
            x_ray_visor=json_data["x_ray_visor"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan_visor": self.scan_visor,
            "command_visor": self.command_visor,
            "x_ray_visor": self.x_ray_visor,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x586A8F75: ("scan_visor", structs.decode_BIG_bool_),
    0x04FCA2A9: ("command_visor", structs.decode_BIG_bool_),
    0xF55DD02C: ("x_ray_visor", structs.decode_BIG_bool_),
}
