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

    class BehaveChanceJson(typing_extensions.TypedDict):
        lurk: float
        taunt: float
        attack: float
        move: float
        lurk_time: float
        charge_attack: float
        num_bolts: int


@dataclasses.dataclass()
class BehaveChance(BaseProperty):
    lurk: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000000, original_name="Lurk"),
        },
    )
    taunt: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Taunt"),
        },
    )
    attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000002, original_name="Attack"),
        },
    )
    move: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Move"),
        },
    )
    lurk_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Lurk Time"),
        },
    )
    charge_attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Charge Attack"),
        },
    )
    num_bolts: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="numBolts"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        lurk = structs.BIG_f.unpack(data.read(4))[0]
        taunt = structs.BIG_f.unpack(data.read(4))[0]
        attack = structs.BIG_f.unpack(data.read(4))[0]
        move = structs.BIG_f.unpack(data.read(4))[0]
        lurk_time = structs.BIG_f.unpack(data.read(4))[0]
        charge_attack = structs.BIG_f.unpack(data.read(4))[0]
        num_bolts = structs.BIG_l.unpack(data.read(4))[0]
        return cls(lurk, taunt, attack, move, lurk_time, charge_attack, num_bolts)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_f.pack(self.lurk))
        data.write(structs.BIG_f.pack(self.taunt))
        data.write(structs.BIG_f.pack(self.attack))
        data.write(structs.BIG_f.pack(self.move))
        data.write(structs.BIG_f.pack(self.lurk_time))
        data.write(structs.BIG_f.pack(self.charge_attack))
        data.write(structs.BIG_l.pack(self.num_bolts))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BehaveChanceJson", data)
        return cls(
            lurk=json_data["lurk"],
            taunt=json_data["taunt"],
            attack=json_data["attack"],
            move=json_data["move"],
            lurk_time=json_data["lurk_time"],
            charge_attack=json_data["charge_attack"],
            num_bolts=json_data["num_bolts"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "lurk": self.lurk,
            "taunt": self.taunt,
            "attack": self.attack,
            "move": self.move,
            "lurk_time": self.lurk_time,
            "charge_attack": self.charge_attack,
            "num_bolts": self.num_bolts,
        }
