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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct5Json(typing_extensions.TypedDict):
        override: bool
        offset: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x7FF86EE2, 0x46477064)


@dataclasses.dataclass()
class UnknownStruct5(BaseProperty):
    override: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7FF86EE2, original_name="Override"),
        },
    )
    offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x46477064, original_name="Offset", from_json=Vector.from_json, to_json=Vector.to_json
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
            _FAST_FORMAT = struct.Struct(">LH?LHfff")

        dec = _FAST_FORMAT.unpack(data.read(25))
        assert (dec[0], dec[3]) == _FAST_IDS
        return cls(
            dec[2],
            Vector(*dec[5:8]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\x7f\xf8n\xe2")  # 0x7ff86ee2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.override))

        data.write(b"FGpd")  # 0x46477064
        data.write(b"\x00\x0c")  # size
        self.offset.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct5Json", data)
        return cls(
            override=json_data["override"],
            offset=Vector.from_json(json_data["offset"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "override": self.override,
            "offset": self.offset.to_json(),
        }


def _decode_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FF86EE2: ("override", structs.decode_BIG_bool_),
    0x46477064: ("offset", _decode_offset),
}
