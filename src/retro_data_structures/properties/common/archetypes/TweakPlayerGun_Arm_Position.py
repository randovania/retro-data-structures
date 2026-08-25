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

    class TweakPlayerGun_Arm_PositionJson(typing_extensions.TypedDict):
        normal: json_util.JsonValue
        grappling: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x3C9366AC, 0x66B1D066)


@dataclasses.dataclass()
class TweakPlayerGun_Arm_Position(BaseProperty):
    normal: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x3C9366AC, original_name="Normal", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    grappling: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x66B1D066, original_name="Grappling", from_json=Vector.from_json, to_json=Vector.to_json
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
            _FAST_FORMAT = struct.Struct(">LHfffLHfff")

        dec = _FAST_FORMAT.unpack(data.read(36))
        assert (dec[0], dec[5]) == _FAST_IDS
        return cls(
            Vector(*dec[2:5]),
            Vector(*dec[7:10]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"<\x93f\xac")  # 0x3c9366ac
        data.write(b"\x00\x0c")  # size
        self.normal.to_stream(data, game)

        data.write(b"f\xb1\xd0f")  # 0x66b1d066
        data.write(b"\x00\x0c")  # size
        self.grappling.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_Arm_PositionJson", data)
        return cls(
            normal=Vector.from_json(json_data["normal"]),
            grappling=Vector.from_json(json_data["grappling"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "normal": self.normal.to_json(),
            "grappling": self.grappling.to_json(),
        }


def _decode_normal(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_grappling(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3C9366AC: ("normal", _decode_normal),
    0x66B1D066: ("grappling", _decode_grappling),
}
