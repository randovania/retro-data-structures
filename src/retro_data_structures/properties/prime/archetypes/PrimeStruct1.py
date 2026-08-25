# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PrimeStruct1Json(typing_extensions.TypedDict):
        unknown_1: float
        unknown_2: float
        unknown_3: float
        unknown_4: float
        unknown_5: float
        unknown_6: float
        unknown_7: float
        unknown_8: float
        unknown_9: float
        unknown_10: float
        unknown_11: float
        unknown_12: float
        unknown_13: float
        unknown_14: float


@dataclasses.dataclass()
class PrimeStruct1(BaseProperty):
    unknown_1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Unknown 1"),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Unknown 2"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Unknown 6"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Unknown 8"),
        },
    )
    unknown_9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown 9"),
        },
    )
    unknown_10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 10"),
        },
    )
    unknown_11: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="Unknown 11"),
        },
    )
    unknown_12: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="Unknown 12"),
        },
    )
    unknown_13: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="Unknown 13"),
        },
    )
    unknown_14: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Unknown 14"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown_1 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_12 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_13 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_14 = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            unknown_1,
            unknown_2,
            unknown_3,
            unknown_4,
            unknown_5,
            unknown_6,
            unknown_7,
            unknown_8,
            unknown_9,
            unknown_10,
            unknown_11,
            unknown_12,
            unknown_13,
            unknown_14,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_f.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        data.write(structs.BIG_f.pack(self.unknown_9))
        data.write(structs.BIG_f.pack(self.unknown_10))
        data.write(structs.BIG_f.pack(self.unknown_11))
        data.write(structs.BIG_f.pack(self.unknown_12))
        data.write(structs.BIG_f.pack(self.unknown_13))
        data.write(structs.BIG_f.pack(self.unknown_14))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PrimeStruct1Json", data)
        return cls(
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            unknown_11=json_data["unknown_11"],
            unknown_12=json_data["unknown_12"],
            unknown_13=json_data["unknown_13"],
            unknown_14=json_data["unknown_14"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "unknown_11": self.unknown_11,
            "unknown_12": self.unknown_12,
            "unknown_13": self.unknown_13,
            "unknown_14": self.unknown_14,
        }
