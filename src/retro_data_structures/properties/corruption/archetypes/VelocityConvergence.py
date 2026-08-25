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

    class VelocityConvergenceJson(typing_extensions.TypedDict):
        max_speed: float
        acceleration: float
        dampening_range: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x82DB0CBE, 0x39FB7978, 0x1A111725)


@dataclasses.dataclass()
class VelocityConvergence(BaseProperty):
    max_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x82DB0CBE, original_name="MaxSpeed"),
        },
    )
    acceleration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39FB7978, original_name="Acceleration"),
        },
    )
    dampening_range: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A111725, original_name="DampeningRange"),
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
            _FAST_FORMAT = struct.Struct(">LHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(30))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\x82\xdb\x0c\xbe")  # 0x82db0cbe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_speed))

        data.write(b"9\xfbyx")  # 0x39fb7978
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.acceleration))

        data.write(b"\x1a\x11\x17%")  # 0x1a111725
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dampening_range))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VelocityConvergenceJson", data)
        return cls(
            max_speed=json_data["max_speed"],
            acceleration=json_data["acceleration"],
            dampening_range=json_data["dampening_range"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "max_speed": self.max_speed,
            "acceleration": self.acceleration,
            "dampening_range": self.dampening_range,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x82DB0CBE: ("max_speed", structs.decode_BIG_f),
    0x39FB7978: ("acceleration", structs.decode_BIG_f),
    0x1A111725: ("dampening_range", structs.decode_BIG_f),
}
