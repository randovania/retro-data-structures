# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.Vector2f import Vector2f
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SafeZoneStructAJson(typing_extensions.TypedDict):
        enabled: bool
        mode: int
        color: json_util.JsonValue
        near_far_plane: json_util.JsonObject
        color_rate: float
        distance_rate: json_util.JsonObject


@dataclasses.dataclass()
class SafeZoneStructA(BaseProperty):
    enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x29C77D27, original_name="Enabled"),
        },
    )
    mode: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x09AD63DE, original_name="Mode"),
        },
    )
    color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x37C7D09D, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    near_far_plane: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0x652008DA,
                original_name="NearFarPlane",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        },
    )
    color_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x29AB4727, original_name="ColorRate"),
        },
    )
    distance_rate: Vector2f = dataclasses.field(
        default_factory=Vector2f,
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0xCC8E0F98,
                original_name="DistanceRate",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
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
        if property_count != 6:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29C77D27
        enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09AD63DE
        mode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37C7D09D
        color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x652008DA
        near_far_plane = Vector2f.from_stream(data, game, property_size, default_override={"x": 1.0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29AB4727
        color_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC8E0F98
        distance_rate = Vector2f.from_stream(data, game, property_size)

        return cls(enabled, mode, color, near_far_plane, color_rate, distance_rate)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b")\xc7}'")  # 0x29c77d27
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.enabled))

        data.write(b"\t\xadc\xde")  # 0x9ad63de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.mode))

        data.write(b"7\xc7\xd0\x9d")  # 0x37c7d09d
        data.write(b"\x00\x10")  # size
        self.color.to_stream(data, game)

        data.write(b"e \x08\xda")  # 0x652008da
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.near_far_plane.to_stream(data, game, default_override={"x": 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")\xabG'")  # 0x29ab4727
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.color_rate))

        data.write(b"\xcc\x8e\x0f\x98")  # 0xcc8e0f98
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.distance_rate.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SafeZoneStructAJson", data)
        return cls(
            enabled=json_data["enabled"],
            mode=json_data["mode"],
            color=Color.from_json(json_data["color"]),
            near_far_plane=Vector2f.from_json(json_data["near_far_plane"]),
            color_rate=json_data["color_rate"],
            distance_rate=Vector2f.from_json(json_data["distance_rate"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "enabled": self.enabled,
            "mode": self.mode,
            "color": self.color.to_json(),
            "near_far_plane": self.near_far_plane.to_json(),
            "color_rate": self.color_rate,
            "distance_rate": self.distance_rate.to_json(),
        }


def _decode_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_near_far_plane(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size, default_override={"x": 1.0})


def _decode_distance_rate(data: typing.BinaryIO, game: Game, property_size: int) -> Vector2f:
    return Vector2f.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x29C77D27: ("enabled", structs.decode_BIG_bool_),
    0x09AD63DE: ("mode", structs.decode_BIG_l),
    0x37C7D09D: ("color", _decode_color),
    0x652008DA: ("near_far_plane", _decode_near_far_plane),
    0x29AB4727: ("color_rate", structs.decode_BIG_f),
    0xCC8E0F98: ("distance_rate", _decode_distance_rate),
}
