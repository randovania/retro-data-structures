# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakGui_UnknownStruct1Json(typing_extensions.TypedDict):
        background_blend_color: json_util.JsonValue
        unknown_0x10f17007: json_util.JsonValue
        ship_model_scale: float
        ship_model_base_pitch: float
        ship_model_base_yaw: float
        ship_model_pitch_limit: float
        ship_model_yaw_limit: float
        ship_ambient_color: json_util.JsonValue
        ship_light_color: json_util.JsonValue
        ship_light_position: json_util.JsonValue
        unknown_0x37e62f14: json_util.JsonObject
        unknown_0x3287fcad: json_util.JsonObject


@dataclasses.dataclass()
class TweakGui_UnknownStruct1(BaseProperty):
    background_blend_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xDFD3CFF0,
                original_name="BackgroundBlendColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    unknown_0x10f17007: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x10F17007, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    ship_model_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1DA9CDF3, original_name="ShipModelScale"),
        },
    )
    ship_model_base_pitch: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0CAF8A9C, original_name="ShipModelBasePitch"),
        },
    )
    ship_model_base_yaw: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x203E7D1C, original_name="ShipModelBaseYaw"),
        },
    )
    ship_model_pitch_limit: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1DB1573C, original_name="ShipModelPitchLimit"),
        },
    )
    ship_model_yaw_limit: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76597839, original_name="ShipModelYawLimit"),
        },
    )
    ship_ambient_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x21B607C0, original_name="ShipAmbientColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    ship_light_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x705663E8, original_name="ShipLightColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    ship_light_position: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x33BABD84,
                original_name="ShipLightPosition",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    unknown_0x37e62f14: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x37E62F14, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x3287fcad: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x3287FCAD, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 12:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFD3CFF0
        background_blend_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10F17007
        unknown_0x10f17007 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1DA9CDF3
        ship_model_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CAF8A9C
        ship_model_base_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x203E7D1C
        ship_model_base_yaw = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1DB1573C
        ship_model_pitch_limit = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76597839
        ship_model_yaw_limit = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21B607C0
        ship_ambient_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x705663E8
        ship_light_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33BABD84
        ship_light_position = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37E62F14
        unknown_0x37e62f14 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3287FCAD
        unknown_0x3287fcad = Spline.from_stream(data, game, property_size)

        return cls(
            background_blend_color,
            unknown_0x10f17007,
            ship_model_scale,
            ship_model_base_pitch,
            ship_model_base_yaw,
            ship_model_pitch_limit,
            ship_model_yaw_limit,
            ship_ambient_color,
            ship_light_color,
            ship_light_position,
            unknown_0x37e62f14,
            unknown_0x3287fcad,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0c")  # 12 properties

        data.write(b"\xdf\xd3\xcf\xf0")  # 0xdfd3cff0
        data.write(b"\x00\x10")  # size
        self.background_blend_color.to_stream(data, game)

        data.write(b"\x10\xf1p\x07")  # 0x10f17007
        data.write(b"\x00\x10")  # size
        self.unknown_0x10f17007.to_stream(data, game)

        data.write(b"\x1d\xa9\xcd\xf3")  # 0x1da9cdf3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ship_model_scale))

        data.write(b"\x0c\xaf\x8a\x9c")  # 0xcaf8a9c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ship_model_base_pitch))

        data.write(b" >}\x1c")  # 0x203e7d1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ship_model_base_yaw))

        data.write(b"\x1d\xb1W<")  # 0x1db1573c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ship_model_pitch_limit))

        data.write(b"vYx9")  # 0x76597839
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ship_model_yaw_limit))

        data.write(b"!\xb6\x07\xc0")  # 0x21b607c0
        data.write(b"\x00\x10")  # size
        self.ship_ambient_color.to_stream(data, game)

        data.write(b"pVc\xe8")  # 0x705663e8
        data.write(b"\x00\x10")  # size
        self.ship_light_color.to_stream(data, game)

        data.write(b"3\xba\xbd\x84")  # 0x33babd84
        data.write(b"\x00\x0c")  # size
        self.ship_light_position.to_stream(data, game)

        data.write(b"7\xe6/\x14")  # 0x37e62f14
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x37e62f14.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"2\x87\xfc\xad")  # 0x3287fcad
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x3287fcad.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_UnknownStruct1Json", data)
        return cls(
            background_blend_color=Color.from_json(json_data["background_blend_color"]),
            unknown_0x10f17007=Color.from_json(json_data["unknown_0x10f17007"]),
            ship_model_scale=json_data["ship_model_scale"],
            ship_model_base_pitch=json_data["ship_model_base_pitch"],
            ship_model_base_yaw=json_data["ship_model_base_yaw"],
            ship_model_pitch_limit=json_data["ship_model_pitch_limit"],
            ship_model_yaw_limit=json_data["ship_model_yaw_limit"],
            ship_ambient_color=Color.from_json(json_data["ship_ambient_color"]),
            ship_light_color=Color.from_json(json_data["ship_light_color"]),
            ship_light_position=Vector.from_json(json_data["ship_light_position"]),
            unknown_0x37e62f14=Spline.from_json(json_data["unknown_0x37e62f14"]),
            unknown_0x3287fcad=Spline.from_json(json_data["unknown_0x3287fcad"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "background_blend_color": self.background_blend_color.to_json(),
            "unknown_0x10f17007": self.unknown_0x10f17007.to_json(),
            "ship_model_scale": self.ship_model_scale,
            "ship_model_base_pitch": self.ship_model_base_pitch,
            "ship_model_base_yaw": self.ship_model_base_yaw,
            "ship_model_pitch_limit": self.ship_model_pitch_limit,
            "ship_model_yaw_limit": self.ship_model_yaw_limit,
            "ship_ambient_color": self.ship_ambient_color.to_json(),
            "ship_light_color": self.ship_light_color.to_json(),
            "ship_light_position": self.ship_light_position.to_json(),
            "unknown_0x37e62f14": self.unknown_0x37e62f14.to_json(),
            "unknown_0x3287fcad": self.unknown_0x3287fcad.to_json(),
        }


def _decode_background_blend_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x10f17007(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ship_ambient_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ship_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ship_light_position(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0x37e62f14(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x3287fcad(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDFD3CFF0: ("background_blend_color", _decode_background_blend_color),
    0x10F17007: ("unknown_0x10f17007", _decode_unknown_0x10f17007),
    0x1DA9CDF3: ("ship_model_scale", structs.decode_BIG_f),
    0x0CAF8A9C: ("ship_model_base_pitch", structs.decode_BIG_f),
    0x203E7D1C: ("ship_model_base_yaw", structs.decode_BIG_f),
    0x1DB1573C: ("ship_model_pitch_limit", structs.decode_BIG_f),
    0x76597839: ("ship_model_yaw_limit", structs.decode_BIG_f),
    0x21B607C0: ("ship_ambient_color", _decode_ship_ambient_color),
    0x705663E8: ("ship_light_color", _decode_ship_light_color),
    0x33BABD84: ("ship_light_position", _decode_ship_light_position),
    0x37E62F14: ("unknown_0x37e62f14", _decode_unknown_0x37e62f14),
    0x3287FCAD: ("unknown_0x3287fcad", _decode_unknown_0x3287fcad),
}
