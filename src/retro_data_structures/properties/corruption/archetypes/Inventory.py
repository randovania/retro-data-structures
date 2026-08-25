# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.Abilities import Abilities
from retro_data_structures.properties.corruption.archetypes.Ball import Ball
from retro_data_structures.properties.corruption.archetypes.HyperMode import HyperMode
from retro_data_structures.properties.corruption.archetypes.Misc import Misc
from retro_data_structures.properties.corruption.archetypes.Ship import Ship
from retro_data_structures.properties.corruption.archetypes.Visors import Visors
from retro_data_structures.properties.corruption.archetypes.Weapons import Weapons
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class InventoryJson(typing_extensions.TypedDict):
        misc: json_util.JsonObject
        weapons: json_util.JsonObject
        visors: json_util.JsonObject
        ball: json_util.JsonObject
        abilities: json_util.JsonObject
        hyper_mode: json_util.JsonObject
        ship: json_util.JsonObject


@dataclasses.dataclass()
class Inventory(BaseProperty):
    misc: Misc = dataclasses.field(
        default_factory=Misc,
        metadata={
            "reflection": FieldReflection[Misc](
                Misc, id=0x52C779C0, original_name="Misc", from_json=Misc.from_json, to_json=Misc.to_json
            ),
        },
    )
    weapons: Weapons = dataclasses.field(
        default_factory=Weapons,
        metadata={
            "reflection": FieldReflection[Weapons](
                Weapons, id=0xEF43B845, original_name="Weapons", from_json=Weapons.from_json, to_json=Weapons.to_json
            ),
        },
    )
    visors: Visors = dataclasses.field(
        default_factory=Visors,
        metadata={
            "reflection": FieldReflection[Visors](
                Visors, id=0x317D45BB, original_name="Visors", from_json=Visors.from_json, to_json=Visors.to_json
            ),
        },
    )
    ball: Ball = dataclasses.field(
        default_factory=Ball,
        metadata={
            "reflection": FieldReflection[Ball](
                Ball, id=0xED7F3B4A, original_name="Ball", from_json=Ball.from_json, to_json=Ball.to_json
            ),
        },
    )
    abilities: Abilities = dataclasses.field(
        default_factory=Abilities,
        metadata={
            "reflection": FieldReflection[Abilities](
                Abilities,
                id=0x267F91E5,
                original_name="Abilities",
                from_json=Abilities.from_json,
                to_json=Abilities.to_json,
            ),
        },
    )
    hyper_mode: HyperMode = dataclasses.field(
        default_factory=HyperMode,
        metadata={
            "reflection": FieldReflection[HyperMode](
                HyperMode,
                id=0x378E02B2,
                original_name="HyperMode",
                from_json=HyperMode.from_json,
                to_json=HyperMode.to_json,
            ),
        },
    )
    ship: Ship = dataclasses.field(
        default_factory=Ship,
        metadata={
            "reflection": FieldReflection[Ship](
                Ship, id=0xE9C4A786, original_name="Ship", from_json=Ship.from_json, to_json=Ship.to_json
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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52C779C0
        misc = Misc.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF43B845
        weapons = Weapons.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x317D45BB
        visors = Visors.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED7F3B4A
        ball = Ball.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x267F91E5
        abilities = Abilities.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x378E02B2
        hyper_mode = HyperMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9C4A786
        ship = Ship.from_stream(data, game, property_size)

        return cls(misc, weapons, visors, ball, abilities, hyper_mode, ship)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"R\xc7y\xc0")  # 0x52c779c0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xefC\xb8E")  # 0xef43b845
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapons.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"1}E\xbb")  # 0x317d45bb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.visors.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\x7f;J")  # 0xed7f3b4a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&\x7f\x91\xe5")  # 0x267f91e5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.abilities.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"7\x8e\x02\xb2")  # 0x378e02b2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe9\xc4\xa7\x86")  # 0xe9c4a786
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ship.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("InventoryJson", data)
        return cls(
            misc=Misc.from_json(json_data["misc"]),
            weapons=Weapons.from_json(json_data["weapons"]),
            visors=Visors.from_json(json_data["visors"]),
            ball=Ball.from_json(json_data["ball"]),
            abilities=Abilities.from_json(json_data["abilities"]),
            hyper_mode=HyperMode.from_json(json_data["hyper_mode"]),
            ship=Ship.from_json(json_data["ship"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "misc": self.misc.to_json(),
            "weapons": self.weapons.to_json(),
            "visors": self.visors.to_json(),
            "ball": self.ball.to_json(),
            "abilities": self.abilities.to_json(),
            "hyper_mode": self.hyper_mode.to_json(),
            "ship": self.ship.to_json(),
        }


def _decode_misc(data: typing.BinaryIO, game: Game, property_size: int) -> Misc:
    return Misc.from_stream(data, game, property_size)


def _decode_weapons(data: typing.BinaryIO, game: Game, property_size: int) -> Weapons:
    return Weapons.from_stream(data, game, property_size)


def _decode_visors(data: typing.BinaryIO, game: Game, property_size: int) -> Visors:
    return Visors.from_stream(data, game, property_size)


def _decode_ball(data: typing.BinaryIO, game: Game, property_size: int) -> Ball:
    return Ball.from_stream(data, game, property_size)


def _decode_abilities(data: typing.BinaryIO, game: Game, property_size: int) -> Abilities:
    return Abilities.from_stream(data, game, property_size)


def _decode_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> HyperMode:
    return HyperMode.from_stream(data, game, property_size)


def _decode_ship(data: typing.BinaryIO, game: Game, property_size: int) -> Ship:
    return Ship.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x52C779C0: ("misc", _decode_misc),
    0xEF43B845: ("weapons", _decode_weapons),
    0x317D45BB: ("visors", _decode_visors),
    0xED7F3B4A: ("ball", _decode_ball),
    0x267F91E5: ("abilities", _decode_abilities),
    0x378E02B2: ("hyper_mode", _decode_hyper_mode),
    0xE9C4A786: ("ship", _decode_ship),
}
