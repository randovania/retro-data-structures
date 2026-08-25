# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DynamicLightFalloffJson(typing_extensions.TypedDict):
        falloff_type: int
        falloff_rate: json_util.JsonObject
        falloff_rate_duration: float
        falloff_rate_loops: bool


@dataclasses.dataclass()
class DynamicLightFalloff(BaseProperty):
    falloff_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x456DF20C, original_name="FalloffType"),
        },
    )
    falloff_rate: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x2F7C63A3, original_name="FalloffRate", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    falloff_rate_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1F6813F1, original_name="FalloffRateDuration"),
        },
    )
    falloff_rate_loops: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6D323EA3, original_name="FalloffRateLoops"),
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x456DF20C
        falloff_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F7C63A3
        falloff_rate = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F6813F1
        falloff_rate_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D323EA3
        falloff_rate_loops = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(falloff_type, falloff_rate, falloff_rate_duration, falloff_rate_loops)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"Em\xf2\x0c")  # 0x456df20c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.falloff_type))

        data.write(b"/|c\xa3")  # 0x2f7c63a3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.falloff_rate.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1fh\x13\xf1")  # 0x1f6813f1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.falloff_rate_duration))

        data.write(b"m2>\xa3")  # 0x6d323ea3
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.falloff_rate_loops))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DynamicLightFalloffJson", data)
        return cls(
            falloff_type=json_data["falloff_type"],
            falloff_rate=Spline.from_json(json_data["falloff_rate"]),
            falloff_rate_duration=json_data["falloff_rate_duration"],
            falloff_rate_loops=json_data["falloff_rate_loops"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "falloff_type": self.falloff_type,
            "falloff_rate": self.falloff_rate.to_json(),
            "falloff_rate_duration": self.falloff_rate_duration,
            "falloff_rate_loops": self.falloff_rate_loops,
        }


def _decode_falloff_rate(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x456DF20C: ("falloff_type", structs.decode_BIG_l),
    0x2F7C63A3: ("falloff_rate", _decode_falloff_rate),
    0x1F6813F1: ("falloff_rate_duration", structs.decode_BIG_f),
    0x6D323EA3: ("falloff_rate_loops", structs.decode_BIG_bool_),
}
