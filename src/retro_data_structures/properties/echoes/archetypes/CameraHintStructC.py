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

    class CameraHintStructCJson(typing_extensions.TypedDict):
        override: bool
        angle: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x7FF86EE2, 0x382A1973)


@dataclasses.dataclass()
class CameraHintStructC(BaseProperty):
    override: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7FF86EE2, original_name="Override"),
        },
    )
    angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x382A1973, original_name="Angle"),
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
            _FAST_FORMAT = struct.Struct(">LH?LHf")

        dec = _FAST_FORMAT.unpack(data.read(17))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\x7f\xf8n\xe2")  # 0x7ff86ee2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.override))

        data.write(b"8*\x19s")  # 0x382a1973
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraHintStructCJson", data)
        return cls(
            override=json_data["override"],
            angle=json_data["angle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "override": self.override,
            "angle": self.angle,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FF86EE2: ("override", structs.decode_BIG_bool_),
    0x382A1973: ("angle", structs.decode_BIG_f),
}
