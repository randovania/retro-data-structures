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

    class DynamicLightIntensityJson(typing_extensions.TypedDict):
        intensity: json_util.JsonObject
        intensity_duration: float
        intensity_loops: bool


@dataclasses.dataclass()
class DynamicLightIntensity(BaseProperty):
    intensity: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x239D0D2B, original_name="Intensity", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    intensity_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC90D8899, original_name="IntensityDuration"),
        },
    )
    intensity_loops: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAE67E050, original_name="IntensityLoops"),
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x239D0D2B
        intensity = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC90D8899
        intensity_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE67E050
        intensity_loops = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(intensity, intensity_duration, intensity_loops)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"#\x9d\r+")  # 0x239d0d2b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.intensity.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc9\r\x88\x99")  # 0xc90d8899
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.intensity_duration))

        data.write(b"\xaeg\xe0P")  # 0xae67e050
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.intensity_loops))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DynamicLightIntensityJson", data)
        return cls(
            intensity=Spline.from_json(json_data["intensity"]),
            intensity_duration=json_data["intensity_duration"],
            intensity_loops=json_data["intensity_loops"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "intensity": self.intensity.to_json(),
            "intensity_duration": self.intensity_duration,
            "intensity_loops": self.intensity_loops,
        }


def _decode_intensity(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x239D0D2B: ("intensity", _decode_intensity),
    0xC90D8899: ("intensity_duration", structs.decode_BIG_f),
    0xAE67E050: ("intensity_loops", structs.decode_BIG_bool_),
}
