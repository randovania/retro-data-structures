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

    class LayerInfoJson(typing_extensions.TypedDict):
        motion_type: int
        unknown: float
        rotation: float
        amplitude: float
        texture_scale: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x948AF571, 0x3C5B0C98, 0x912954E6, 0x89E3D294, 0x80C7499)


@dataclasses.dataclass()
class LayerInfo(BaseProperty):
    motion_type: int = dataclasses.field(
        default=864275068,
        metadata={
            "reflection": FieldReflection[int](int, id=0x948AF571, original_name="MotionType"),
        },
    )  # Choice
    unknown: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3C5B0C98, original_name="Unknown"),
        },
    )
    rotation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x912954E6, original_name="Rotation"),
        },
    )
    amplitude: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0x89E3D294, original_name="Amplitude"),
        },
    )
    texture_scale: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x080C7499, original_name="TextureScale"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHLLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(50))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"\x94\x8a\xf5q")  # 0x948af571
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.motion_type))

        data.write(b"<[\x0c\x98")  # 0x3c5b0c98
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x91)T\xe6")  # 0x912954e6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation))

        data.write(b"\x89\xe3\xd2\x94")  # 0x89e3d294
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.amplitude))

        data.write(b"\x08\x0ct\x99")  # 0x80c7499
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.texture_scale))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LayerInfoJson", data)
        return cls(
            motion_type=json_data["motion_type"],
            unknown=json_data["unknown"],
            rotation=json_data["rotation"],
            amplitude=json_data["amplitude"],
            texture_scale=json_data["texture_scale"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "motion_type": self.motion_type,
            "unknown": self.unknown,
            "rotation": self.rotation,
            "amplitude": self.amplitude,
            "texture_scale": self.texture_scale,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x948AF571: ("motion_type", structs.decode_BIG_L),
    0x3C5B0C98: ("unknown", structs.decode_BIG_f),
    0x912954E6: ("rotation", structs.decode_BIG_f),
    0x89E3D294: ("amplitude", structs.decode_BIG_f),
    0x080C7499: ("texture_scale", structs.decode_BIG_f),
}
