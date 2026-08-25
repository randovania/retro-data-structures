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

    class RevolutionControl_UnknownStruct4Json(typing_extensions.TypedDict):
        center_x: float
        center_y: float
        min_radius: float
        max_radius: float
        initial_angle: float
        arc_angle: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x8C938C3F, 0x47CF5F9A, 0x7CBF27CA, 0xC599BCBB, 0x90AC8041, 0xB58890FB)


@dataclasses.dataclass()
class RevolutionControl_UnknownStruct4(BaseProperty):
    center_x: float = dataclasses.field(
        default=320.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8C938C3F, original_name="CenterX"),
        },
    )
    center_y: float = dataclasses.field(
        default=224.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47CF5F9A, original_name="CenterY"),
        },
    )
    min_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7CBF27CA, original_name="MinRadius"),
        },
    )
    max_radius: float = dataclasses.field(
        default=64.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC599BCBB, original_name="MaxRadius"),
        },
    )
    initial_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AC8041, original_name="InitialAngle"),
        },
    )
    arc_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB58890FB, original_name="ArcAngle"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(60))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"\x8c\x93\x8c?")  # 0x8c938c3f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.center_x))

        data.write(b"G\xcf_\x9a")  # 0x47cf5f9a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.center_y))

        data.write(b"|\xbf'\xca")  # 0x7cbf27ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_radius))

        data.write(b"\xc5\x99\xbc\xbb")  # 0xc599bcbb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_radius))

        data.write(b"\x90\xac\x80A")  # 0x90ac8041
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_angle))

        data.write(b"\xb5\x88\x90\xfb")  # 0xb58890fb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arc_angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RevolutionControl_UnknownStruct4Json", data)
        return cls(
            center_x=json_data["center_x"],
            center_y=json_data["center_y"],
            min_radius=json_data["min_radius"],
            max_radius=json_data["max_radius"],
            initial_angle=json_data["initial_angle"],
            arc_angle=json_data["arc_angle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "center_x": self.center_x,
            "center_y": self.center_y,
            "min_radius": self.min_radius,
            "max_radius": self.max_radius,
            "initial_angle": self.initial_angle,
            "arc_angle": self.arc_angle,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8C938C3F: ("center_x", structs.decode_BIG_f),
    0x47CF5F9A: ("center_y", structs.decode_BIG_f),
    0x7CBF27CA: ("min_radius", structs.decode_BIG_f),
    0xC599BCBB: ("max_radius", structs.decode_BIG_f),
    0x90AC8041: ("initial_angle", structs.decode_BIG_f),
    0xB58890FB: ("arc_angle", structs.decode_BIG_f),
}
