# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.SpacePirateWeaponData import SpacePirateWeaponData
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct3Json(typing_extensions.TypedDict):
        min_attack_range: float
        max_attack_range: float
        unknown_0xef6d8f65: float
        unknown_0xdb93d177: float
        unknown_0x0d49855c: float
        unknown_0x9dce6b35: float
        min_attack_time: float
        max_attack_time: float
        pickup_chance: float
        weapon_data: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct3(BaseProperty):
    min_attack_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x58434916, original_name="MinAttackRange"),
        },
    )
    max_attack_range: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF77C96F, original_name="MaxAttackRange"),
        },
    )
    unknown_0xef6d8f65: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEF6D8F65, original_name="Unknown"),
        },
    )
    unknown_0xdb93d177: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDB93D177, original_name="Unknown"),
        },
    )
    unknown_0x0d49855c: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D49855C, original_name="Unknown"),
        },
    )
    unknown_0x9dce6b35: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9DCE6B35, original_name="Unknown"),
        },
    )
    min_attack_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2EDF3368, original_name="MinAttackTime"),
        },
    )
    max_attack_time: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D792B8C, original_name="MaxAttackTime"),
        },
    )
    pickup_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6509D9B2, original_name="PickupChance"),
        },
    )
    weapon_data: SpacePirateWeaponData = dataclasses.field(
        default_factory=SpacePirateWeaponData,
        metadata={
            "reflection": FieldReflection[SpacePirateWeaponData](
                SpacePirateWeaponData,
                id=0xDC89CC3C,
                original_name="WeaponData",
                from_json=SpacePirateWeaponData.from_json,
                to_json=SpacePirateWeaponData.to_json,
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58434916
        min_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF77C96F
        max_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF6D8F65
        unknown_0xef6d8f65 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDB93D177
        unknown_0xdb93d177 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D49855C
        unknown_0x0d49855c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9DCE6B35
        unknown_0x9dce6b35 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2EDF3368
        min_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D792B8C
        max_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6509D9B2
        pickup_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC89CC3C
        weapon_data = SpacePirateWeaponData.from_stream(data, game, property_size)

        return cls(
            min_attack_range,
            max_attack_range,
            unknown_0xef6d8f65,
            unknown_0xdb93d177,
            unknown_0x0d49855c,
            unknown_0x9dce6b35,
            min_attack_time,
            max_attack_time,
            pickup_chance,
            weapon_data,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"XCI\x16")  # 0x58434916
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_range))

        data.write(b"\xffw\xc9o")  # 0xff77c96f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_range))

        data.write(b"\xefm\x8fe")  # 0xef6d8f65
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xef6d8f65))

        data.write(b"\xdb\x93\xd1w")  # 0xdb93d177
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdb93d177))

        data.write(b"\rI\x85\\")  # 0xd49855c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0d49855c))

        data.write(b"\x9d\xcek5")  # 0x9dce6b35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9dce6b35))

        data.write(b".\xdf3h")  # 0x2edf3368
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_time))

        data.write(b"}y+\x8c")  # 0x7d792b8c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_time))

        data.write(b"e\t\xd9\xb2")  # 0x6509d9b2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pickup_chance))

        data.write(b"\xdc\x89\xcc<")  # 0xdc89cc3c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct3Json", data)
        return cls(
            min_attack_range=json_data["min_attack_range"],
            max_attack_range=json_data["max_attack_range"],
            unknown_0xef6d8f65=json_data["unknown_0xef6d8f65"],
            unknown_0xdb93d177=json_data["unknown_0xdb93d177"],
            unknown_0x0d49855c=json_data["unknown_0x0d49855c"],
            unknown_0x9dce6b35=json_data["unknown_0x9dce6b35"],
            min_attack_time=json_data["min_attack_time"],
            max_attack_time=json_data["max_attack_time"],
            pickup_chance=json_data["pickup_chance"],
            weapon_data=SpacePirateWeaponData.from_json(json_data["weapon_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "min_attack_range": self.min_attack_range,
            "max_attack_range": self.max_attack_range,
            "unknown_0xef6d8f65": self.unknown_0xef6d8f65,
            "unknown_0xdb93d177": self.unknown_0xdb93d177,
            "unknown_0x0d49855c": self.unknown_0x0d49855c,
            "unknown_0x9dce6b35": self.unknown_0x9dce6b35,
            "min_attack_time": self.min_attack_time,
            "max_attack_time": self.max_attack_time,
            "pickup_chance": self.pickup_chance,
            "weapon_data": self.weapon_data.to_json(),
        }


def _decode_weapon_data(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateWeaponData:
    return SpacePirateWeaponData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x58434916: ("min_attack_range", structs.decode_BIG_f),
    0xFF77C96F: ("max_attack_range", structs.decode_BIG_f),
    0xEF6D8F65: ("unknown_0xef6d8f65", structs.decode_BIG_f),
    0xDB93D177: ("unknown_0xdb93d177", structs.decode_BIG_f),
    0x0D49855C: ("unknown_0x0d49855c", structs.decode_BIG_f),
    0x9DCE6B35: ("unknown_0x9dce6b35", structs.decode_BIG_f),
    0x2EDF3368: ("min_attack_time", structs.decode_BIG_f),
    0x7D792B8C: ("max_attack_time", structs.decode_BIG_f),
    0x6509D9B2: ("pickup_chance", structs.decode_BIG_f),
    0xDC89CC3C: ("weapon_data", _decode_weapon_data),
}
