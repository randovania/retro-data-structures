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

    class IngSpiderballGuardianStructJson(typing_extensions.TypedDict):
        min_patrol_speed: float
        max_patrol_speed: float
        linear_acceleration: float
        angular_speed: float
        unknown: float
        stunned_speed: float
        stunned_time: float
        max_charge_time: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x17C5B61D, 0xB0F13664, 0xAF9B05F4, 0xBCD7333F, 0xD1D9D8BD, 0x8D5917D4, 0x8105ECFD, 0xE5065EA8)


@dataclasses.dataclass()
class IngSpiderballGuardianStruct(BaseProperty):
    min_patrol_speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17C5B61D, original_name="MinPatrolSpeed"),
        },
    )
    max_patrol_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB0F13664, original_name="MaxPatrolSpeed"),
        },
    )
    linear_acceleration: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAF9B05F4, original_name="LinearAcceleration"),
        },
    )
    angular_speed: float = dataclasses.field(
        default=720.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBCD7333F, original_name="AngularSpeed"),
        },
    )
    unknown: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD1D9D8BD, original_name="Unknown"),
        },
    )
    stunned_speed: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D5917D4, original_name="StunnedSpeed"),
        },
    )
    stunned_time: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8105ECFD, original_name="StunnedTime"),
        },
    )
    max_charge_time: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE5065EA8, original_name="MaxChargeTime"),
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
        if property_count != 8:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(80))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\x17\xc5\xb6\x1d")  # 0x17c5b61d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_patrol_speed))

        data.write(b"\xb0\xf16d")  # 0xb0f13664
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_patrol_speed))

        data.write(b"\xaf\x9b\x05\xf4")  # 0xaf9b05f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.linear_acceleration))

        data.write(b"\xbc\xd73?")  # 0xbcd7333f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.angular_speed))

        data.write(b"\xd1\xd9\xd8\xbd")  # 0xd1d9d8bd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x8dY\x17\xd4")  # 0x8d5917d4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stunned_speed))

        data.write(b"\x81\x05\xec\xfd")  # 0x8105ecfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stunned_time))

        data.write(b"\xe5\x06^\xa8")  # 0xe5065ea8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_charge_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("IngSpiderballGuardianStructJson", data)
        return cls(
            min_patrol_speed=json_data["min_patrol_speed"],
            max_patrol_speed=json_data["max_patrol_speed"],
            linear_acceleration=json_data["linear_acceleration"],
            angular_speed=json_data["angular_speed"],
            unknown=json_data["unknown"],
            stunned_speed=json_data["stunned_speed"],
            stunned_time=json_data["stunned_time"],
            max_charge_time=json_data["max_charge_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "min_patrol_speed": self.min_patrol_speed,
            "max_patrol_speed": self.max_patrol_speed,
            "linear_acceleration": self.linear_acceleration,
            "angular_speed": self.angular_speed,
            "unknown": self.unknown,
            "stunned_speed": self.stunned_speed,
            "stunned_time": self.stunned_time,
            "max_charge_time": self.max_charge_time,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x17C5B61D: ("min_patrol_speed", structs.decode_BIG_f),
    0xB0F13664: ("max_patrol_speed", structs.decode_BIG_f),
    0xAF9B05F4: ("linear_acceleration", structs.decode_BIG_f),
    0xBCD7333F: ("angular_speed", structs.decode_BIG_f),
    0xD1D9D8BD: ("unknown", structs.decode_BIG_f),
    0x8D5917D4: ("stunned_speed", structs.decode_BIG_f),
    0x8105ECFD: ("stunned_time", structs.decode_BIG_f),
    0xE5065EA8: ("max_charge_time", structs.decode_BIG_f),
}
