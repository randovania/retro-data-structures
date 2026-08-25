# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class InterpolationMethodJson(typing_extensions.TypedDict):
        interpolation_control_type: int
        control_spline: json_util.JsonObject
        ease_in: float
        ease_out: float
        duration: float


class InterpolationControlType(enum.IntEnum):
    Unknown1 = 1464541212
    Unknown2 = 3715904643
    Unknown3 = 3342922233
    Unknown4 = 4055225324
    Unknown5 = 3980215693
    Unknown6 = 1935003390
    Unknown7 = 881774861

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


@dataclasses.dataclass()
class InterpolationMethod(BaseProperty):
    interpolation_control_type: InterpolationControlType = dataclasses.field(
        default=InterpolationControlType.Unknown2,
        metadata={
            "reflection": FieldReflection[InterpolationControlType](
                InterpolationControlType,
                id=0x09B5957D,
                original_name="InterpolationControlType",
                from_json=InterpolationControlType.from_json,
                to_json=InterpolationControlType.to_json,
            ),
        },
    )
    control_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x15567FE7, original_name="ControlSpline", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    ease_in: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB08D3237, original_name="EaseIn"),
        },
    )
    ease_out: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x67E3836A, original_name="EaseOut"),
        },
    )
    duration: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09B5957D
        interpolation_control_type = InterpolationControlType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15567FE7
        control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB08D3237
        ease_in = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67E3836A
        ease_out = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B51E23F
        duration = structs.BIG_f.unpack(data.read(4))[0]

        return cls(interpolation_control_type, control_spline, ease_in, ease_out, duration)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"\t\xb5\x95}")  # 0x9b5957d
        data.write(b"\x00\x04")  # size
        self.interpolation_control_type.to_stream(data, game)

        data.write(b"\x15V\x7f\xe7")  # 0x15567fe7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb0\x8d27")  # 0xb08d3237
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ease_in))

        data.write(b"g\xe3\x83j")  # 0x67e3836a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ease_out))

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("InterpolationMethodJson", data)
        return cls(
            interpolation_control_type=InterpolationControlType.from_json(json_data["interpolation_control_type"]),
            control_spline=Spline.from_json(json_data["control_spline"]),
            ease_in=json_data["ease_in"],
            ease_out=json_data["ease_out"],
            duration=json_data["duration"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "interpolation_control_type": self.interpolation_control_type.to_json(),
            "control_spline": self.control_spline.to_json(),
            "ease_in": self.ease_in,
            "ease_out": self.ease_out,
            "duration": self.duration,
        }


def _decode_interpolation_control_type(
    data: typing.BinaryIO, game: Game, property_size: int
) -> InterpolationControlType:
    return InterpolationControlType.from_stream(data, game)


def _decode_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x09B5957D: ("interpolation_control_type", _decode_interpolation_control_type),
    0x15567FE7: ("control_spline", _decode_control_spline),
    0xB08D3237: ("ease_in", structs.decode_BIG_f),
    0x67E3836A: ("ease_out", structs.decode_BIG_f),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
}
