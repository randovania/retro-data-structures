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

    class TweakPlayer_FirstPersonCameraJson(typing_extensions.TypedDict):
        unknown_0xba5eb7f5: float
        camera_elevation: float
        unknown_0xb400ebd6: float
        unknown_0xfd26b7b9: float
        unknown_0x97b14dc6: float
        unknown_0xeb59925a: float
        unknown_0xa1d73380: float
        unknown_0xc8e8344a: float
        unknown_0xd40c480e: float
        unknown_0x7960c3a0: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xBA5EB7F5,
    0xD41E3BA,
    0xB400EBD6,
    0xFD26B7B9,
    0x97B14DC6,
    0xEB59925A,
    0xA1D73380,
    0xC8E8344A,
    0xD40C480E,
    0x7960C3A0,
)


@dataclasses.dataclass()
class TweakPlayer_FirstPersonCamera(BaseProperty):
    unknown_0xba5eb7f5: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA5EB7F5, original_name="Unknown"),
        },
    )
    camera_elevation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D41E3BA, original_name="CameraElevation"),
        },
    )
    unknown_0xb400ebd6: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB400EBD6, original_name="Unknown"),
        },
    )
    unknown_0xfd26b7b9: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFD26B7B9, original_name="Unknown"),
        },
    )
    unknown_0x97b14dc6: float = dataclasses.field(
        default=73.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x97B14DC6, original_name="Unknown"),
        },
    )
    unknown_0xeb59925a: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEB59925A, original_name="Unknown"),
        },
    )
    unknown_0xa1d73380: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1D73380, original_name="Unknown"),
        },
    )
    unknown_0xc8e8344a: float = dataclasses.field(
        default=73.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC8E8344A, original_name="Unknown"),
        },
    )
    unknown_0xd40c480e: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD40C480E, original_name="Unknown"),
        },
    )
    unknown_0x7960c3a0: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x7960C3A0, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
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
        if property_count != 10:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfff")

        dec = _FAST_FORMAT.unpack(data.read(108))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27]) == _FAST_IDS
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
            Vector(*dec[29:32]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\xba^\xb7\xf5")  # 0xba5eb7f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xba5eb7f5))

        data.write(b"\rA\xe3\xba")  # 0xd41e3ba
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.camera_elevation))

        data.write(b"\xb4\x00\xeb\xd6")  # 0xb400ebd6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb400ebd6))

        data.write(b"\xfd&\xb7\xb9")  # 0xfd26b7b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfd26b7b9))

        data.write(b"\x97\xb1M\xc6")  # 0x97b14dc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x97b14dc6))

        data.write(b"\xebY\x92Z")  # 0xeb59925a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeb59925a))

        data.write(b"\xa1\xd73\x80")  # 0xa1d73380
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa1d73380))

        data.write(b"\xc8\xe84J")  # 0xc8e8344a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc8e8344a))

        data.write(b"\xd4\x0cH\x0e")  # 0xd40c480e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd40c480e))

        data.write(b"y`\xc3\xa0")  # 0x7960c3a0
        data.write(b"\x00\x0c")  # size
        self.unknown_0x7960c3a0.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_FirstPersonCameraJson", data)
        return cls(
            unknown_0xba5eb7f5=json_data["unknown_0xba5eb7f5"],
            camera_elevation=json_data["camera_elevation"],
            unknown_0xb400ebd6=json_data["unknown_0xb400ebd6"],
            unknown_0xfd26b7b9=json_data["unknown_0xfd26b7b9"],
            unknown_0x97b14dc6=json_data["unknown_0x97b14dc6"],
            unknown_0xeb59925a=json_data["unknown_0xeb59925a"],
            unknown_0xa1d73380=json_data["unknown_0xa1d73380"],
            unknown_0xc8e8344a=json_data["unknown_0xc8e8344a"],
            unknown_0xd40c480e=json_data["unknown_0xd40c480e"],
            unknown_0x7960c3a0=Vector.from_json(json_data["unknown_0x7960c3a0"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xba5eb7f5": self.unknown_0xba5eb7f5,
            "camera_elevation": self.camera_elevation,
            "unknown_0xb400ebd6": self.unknown_0xb400ebd6,
            "unknown_0xfd26b7b9": self.unknown_0xfd26b7b9,
            "unknown_0x97b14dc6": self.unknown_0x97b14dc6,
            "unknown_0xeb59925a": self.unknown_0xeb59925a,
            "unknown_0xa1d73380": self.unknown_0xa1d73380,
            "unknown_0xc8e8344a": self.unknown_0xc8e8344a,
            "unknown_0xd40c480e": self.unknown_0xd40c480e,
            "unknown_0x7960c3a0": self.unknown_0x7960c3a0.to_json(),
        }


def _decode_unknown_0x7960c3a0(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xBA5EB7F5: ("unknown_0xba5eb7f5", structs.decode_BIG_f),
    0x0D41E3BA: ("camera_elevation", structs.decode_BIG_f),
    0xB400EBD6: ("unknown_0xb400ebd6", structs.decode_BIG_f),
    0xFD26B7B9: ("unknown_0xfd26b7b9", structs.decode_BIG_f),
    0x97B14DC6: ("unknown_0x97b14dc6", structs.decode_BIG_f),
    0xEB59925A: ("unknown_0xeb59925a", structs.decode_BIG_f),
    0xA1D73380: ("unknown_0xa1d73380", structs.decode_BIG_f),
    0xC8E8344A: ("unknown_0xc8e8344a", structs.decode_BIG_f),
    0xD40C480E: ("unknown_0xd40c480e", structs.decode_BIG_f),
    0x7960C3A0: ("unknown_0x7960c3a0", _decode_unknown_0x7960c3a0),
}
