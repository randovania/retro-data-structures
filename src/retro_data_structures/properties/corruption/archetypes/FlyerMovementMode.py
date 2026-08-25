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

    class FlyerMovementModeJson(typing_extensions.TypedDict):
        speed: float
        acceleration: float
        turn_rate: float
        facing_turn_rate: float
        turn_threshold: float
        use_avoidance: bool
        avoidance_range: float
        unknown: float
        height_variation_max: float
        height_variation_min: float
        floor_buffer: float
        ceiling_buffer: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x6392404E,
    0x39FB7978,
    0xE34DC703,
    0x6C6426C8,
    0xC0AC271E,
    0x9699FA45,
    0x50A9BD0D,
    0x1A7B77AB,
    0xDCD1597D,
    0x3AB1F69C,
    0x6581358C,
    0x115BB38C,
)


@dataclasses.dataclass()
class FlyerMovementMode(BaseProperty):
    speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6392404E, original_name="Speed"),
        },
    )
    acceleration: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39FB7978, original_name="Acceleration"),
        },
    )
    turn_rate: float = dataclasses.field(
        default=1080.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE34DC703, original_name="TurnRate"),
        },
    )
    facing_turn_rate: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C6426C8, original_name="FacingTurnRate"),
        },
    )
    turn_threshold: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC0AC271E, original_name="TurnThreshold"),
        },
    )
    use_avoidance: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9699FA45, original_name="UseAvoidance"),
        },
    )
    avoidance_range: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50A9BD0D, original_name="AvoidanceRange"),
        },
    )
    unknown: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A7B77AB, original_name="Unknown"),
        },
    )
    height_variation_max: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDCD1597D, original_name="HeightVariationMax"),
        },
    )
    height_variation_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3AB1F69C, original_name="HeightVariationMin"),
        },
    )
    floor_buffer: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6581358C, original_name="FloorBuffer"),
        },
    )
    ceiling_buffer: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x115BB38C, original_name="CeilingBuffer"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLH?LHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(117))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0c")  # 12 properties

        data.write(b"c\x92@N")  # 0x6392404e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b"9\xfbyx")  # 0x39fb7978
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.acceleration))

        data.write(b"\xe3M\xc7\x03")  # 0xe34dc703
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_rate))

        data.write(b"ld&\xc8")  # 0x6c6426c8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.facing_turn_rate))

        data.write(b"\xc0\xac'\x1e")  # 0xc0ac271e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_threshold))

        data.write(b"\x96\x99\xfaE")  # 0x9699fa45
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_avoidance))

        data.write(b"P\xa9\xbd\r")  # 0x50a9bd0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b"\x1a{w\xab")  # 0x1a7b77ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xdc\xd1Y}")  # 0xdcd1597d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.height_variation_max))

        data.write(b":\xb1\xf6\x9c")  # 0x3ab1f69c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.height_variation_min))

        data.write(b"e\x815\x8c")  # 0x6581358c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.floor_buffer))

        data.write(b"\x11[\xb3\x8c")  # 0x115bb38c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ceiling_buffer))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyerMovementModeJson", data)
        return cls(
            speed=json_data["speed"],
            acceleration=json_data["acceleration"],
            turn_rate=json_data["turn_rate"],
            facing_turn_rate=json_data["facing_turn_rate"],
            turn_threshold=json_data["turn_threshold"],
            use_avoidance=json_data["use_avoidance"],
            avoidance_range=json_data["avoidance_range"],
            unknown=json_data["unknown"],
            height_variation_max=json_data["height_variation_max"],
            height_variation_min=json_data["height_variation_min"],
            floor_buffer=json_data["floor_buffer"],
            ceiling_buffer=json_data["ceiling_buffer"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "speed": self.speed,
            "acceleration": self.acceleration,
            "turn_rate": self.turn_rate,
            "facing_turn_rate": self.facing_turn_rate,
            "turn_threshold": self.turn_threshold,
            "use_avoidance": self.use_avoidance,
            "avoidance_range": self.avoidance_range,
            "unknown": self.unknown,
            "height_variation_max": self.height_variation_max,
            "height_variation_min": self.height_variation_min,
            "floor_buffer": self.floor_buffer,
            "ceiling_buffer": self.ceiling_buffer,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6392404E: ("speed", structs.decode_BIG_f),
    0x39FB7978: ("acceleration", structs.decode_BIG_f),
    0xE34DC703: ("turn_rate", structs.decode_BIG_f),
    0x6C6426C8: ("facing_turn_rate", structs.decode_BIG_f),
    0xC0AC271E: ("turn_threshold", structs.decode_BIG_f),
    0x9699FA45: ("use_avoidance", structs.decode_BIG_bool_),
    0x50A9BD0D: ("avoidance_range", structs.decode_BIG_f),
    0x1A7B77AB: ("unknown", structs.decode_BIG_f),
    0xDCD1597D: ("height_variation_max", structs.decode_BIG_f),
    0x3AB1F69C: ("height_variation_min", structs.decode_BIG_f),
    0x6581358C: ("floor_buffer", structs.decode_BIG_f),
    0x115BB38C: ("ceiling_buffer", structs.decode_BIG_f),
}
