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

    class FlyerSwarmDataJson(typing_extensions.TypedDict):
        unknown_0x4a85a2da: float
        unknown_0x10cccd3c: float
        unknown_0x1e8e90a4: float
        unknown_0x262e586d: float
        roll_upright_speed: float
        roll_upright_min_angle: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x4A85A2DA, 0x10CCCD3C, 0x1E8E90A4, 0x262E586D, 0x479A5727, 0xD572D1DA)


@dataclasses.dataclass()
class FlyerSwarmData(BaseProperty):
    unknown_0x4a85a2da: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A85A2DA, original_name="Unknown"),
        },
    )
    unknown_0x10cccd3c: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x10CCCD3C, original_name="Unknown"),
        },
    )
    unknown_0x1e8e90a4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E8E90A4, original_name="Unknown"),
        },
    )
    unknown_0x262e586d: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x262E586D, original_name="Unknown"),
        },
    )
    roll_upright_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x479A5727, original_name="RollUprightSpeed"),
        },
    )
    roll_upright_min_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD572D1DA, original_name="RollUprightMinAngle"),
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

        data.write(b"J\x85\xa2\xda")  # 0x4a85a2da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4a85a2da))

        data.write(b"\x10\xcc\xcd<")  # 0x10cccd3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x10cccd3c))

        data.write(b"\x1e\x8e\x90\xa4")  # 0x1e8e90a4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1e8e90a4))

        data.write(b"&.Xm")  # 0x262e586d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x262e586d))

        data.write(b"G\x9aW'")  # 0x479a5727
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.roll_upright_speed))

        data.write(b"\xd5r\xd1\xda")  # 0xd572d1da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.roll_upright_min_angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyerSwarmDataJson", data)
        return cls(
            unknown_0x4a85a2da=json_data["unknown_0x4a85a2da"],
            unknown_0x10cccd3c=json_data["unknown_0x10cccd3c"],
            unknown_0x1e8e90a4=json_data["unknown_0x1e8e90a4"],
            unknown_0x262e586d=json_data["unknown_0x262e586d"],
            roll_upright_speed=json_data["roll_upright_speed"],
            roll_upright_min_angle=json_data["roll_upright_min_angle"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x4a85a2da": self.unknown_0x4a85a2da,
            "unknown_0x10cccd3c": self.unknown_0x10cccd3c,
            "unknown_0x1e8e90a4": self.unknown_0x1e8e90a4,
            "unknown_0x262e586d": self.unknown_0x262e586d,
            "roll_upright_speed": self.roll_upright_speed,
            "roll_upright_min_angle": self.roll_upright_min_angle,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4A85A2DA: ("unknown_0x4a85a2da", structs.decode_BIG_f),
    0x10CCCD3C: ("unknown_0x10cccd3c", structs.decode_BIG_f),
    0x1E8E90A4: ("unknown_0x1e8e90a4", structs.decode_BIG_f),
    0x262E586D: ("unknown_0x262e586d", structs.decode_BIG_f),
    0x479A5727: ("roll_upright_speed", structs.decode_BIG_f),
    0xD572D1DA: ("roll_upright_min_angle", structs.decode_BIG_f),
}
