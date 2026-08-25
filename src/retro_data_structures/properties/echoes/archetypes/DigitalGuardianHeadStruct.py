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

    class DigitalGuardianHeadStructJson(typing_extensions.TypedDict):
        first_shot_type: int
        projectile_telegraph_time: float
        projectile_attack_time: float
        unknown_0xfdfca535: float
        unknown_0xcd03632c: float
        unknown_0xf1548397: float
        unknown_0xf967e246: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xD20288A4, 0x75DC92BC, 0x9E1C3F6C, 0xFDFCA535, 0xCD03632C, 0xF1548397, 0xF967E246)


@dataclasses.dataclass()
class DigitalGuardianHeadStruct(BaseProperty):
    first_shot_type: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD20288A4, original_name="FirstShotType"),
        },
    )
    projectile_telegraph_time: float = dataclasses.field(
        default=1.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75DC92BC, original_name="ProjectileTelegraphTime"),
        },
    )
    projectile_attack_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9E1C3F6C, original_name="ProjectileAttackTime"),
        },
    )
    unknown_0xfdfca535: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFDFCA535, original_name="Unknown"),
        },
    )
    unknown_0xcd03632c: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD03632C, original_name="Unknown"),
        },
    )
    unknown_0xf1548397: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1548397, original_name="Unknown"),
        },
    )
    unknown_0xf967e246: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF967E246, original_name="Unknown"),
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
        if property_count != 7:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHfLHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(70))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xd2\x02\x88\xa4")  # 0xd20288a4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.first_shot_type))

        data.write(b"u\xdc\x92\xbc")  # 0x75dc92bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_telegraph_time))

        data.write(b"\x9e\x1c?l")  # 0x9e1c3f6c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_attack_time))

        data.write(b"\xfd\xfc\xa55")  # 0xfdfca535
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfdfca535))

        data.write(b"\xcd\x03c,")  # 0xcd03632c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd03632c))

        data.write(b"\xf1T\x83\x97")  # 0xf1548397
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf1548397))

        data.write(b"\xf9g\xe2F")  # 0xf967e246
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf967e246))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DigitalGuardianHeadStructJson", data)
        return cls(
            first_shot_type=json_data["first_shot_type"],
            projectile_telegraph_time=json_data["projectile_telegraph_time"],
            projectile_attack_time=json_data["projectile_attack_time"],
            unknown_0xfdfca535=json_data["unknown_0xfdfca535"],
            unknown_0xcd03632c=json_data["unknown_0xcd03632c"],
            unknown_0xf1548397=json_data["unknown_0xf1548397"],
            unknown_0xf967e246=json_data["unknown_0xf967e246"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "first_shot_type": self.first_shot_type,
            "projectile_telegraph_time": self.projectile_telegraph_time,
            "projectile_attack_time": self.projectile_attack_time,
            "unknown_0xfdfca535": self.unknown_0xfdfca535,
            "unknown_0xcd03632c": self.unknown_0xcd03632c,
            "unknown_0xf1548397": self.unknown_0xf1548397,
            "unknown_0xf967e246": self.unknown_0xf967e246,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD20288A4: ("first_shot_type", structs.decode_BIG_l),
    0x75DC92BC: ("projectile_telegraph_time", structs.decode_BIG_f),
    0x9E1C3F6C: ("projectile_attack_time", structs.decode_BIG_f),
    0xFDFCA535: ("unknown_0xfdfca535", structs.decode_BIG_f),
    0xCD03632C: ("unknown_0xcd03632c", structs.decode_BIG_f),
    0xF1548397: ("unknown_0xf1548397", structs.decode_BIG_f),
    0xF967E246: ("unknown_0xf967e246", structs.decode_BIG_f),
}
