# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SpawnPointJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        power_beam: int
        ice_beam: int
        wave_beam: int
        plasma_beam: int
        missiles: int
        scan_visor: int
        morph_ball_bomb: int
        power_bombs: int
        flamethrower: int
        thermal_visor: int
        charge_beam: int
        super_missile: int
        grapple_beam: int
        x_ray_visor: int
        ice_spreader: int
        space_jump_boots: int
        morph_ball: int
        combat_visor: int
        boost_ball: int
        spider_ball: int
        power_suit: int
        gravity_suit: int
        varia_suit: int
        phazon_suit: int
        energy_tanks: int
        unknown_item_1: int
        health_refill: int
        unknown_item_2: int
        wavebuster: int
        default_spawn: bool
        active: bool
        morphed: bool


@dataclasses.dataclass()
class SpawnPoint(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000001, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    power_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="Power Beam"),
        },
    )
    ice_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="Ice Beam"),
        },
    )
    wave_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="Wave Beam"),
        },
    )
    plasma_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="Plasma Beam"),
        },
    )
    missiles: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="Missiles"),
        },
    )
    scan_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="Scan Visor"),
        },
    )
    morph_ball_bomb: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Morph Ball Bomb"),
        },
    )
    power_bombs: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000A, original_name="Power Bombs"),
        },
    )
    flamethrower: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="Flamethrower"),
        },
    )
    thermal_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000C, original_name="Thermal Visor"),
        },
    )
    charge_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="Charge Beam"),
        },
    )
    super_missile: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000E, original_name="Super Missile"),
        },
    )
    grapple_beam: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000F, original_name="Grapple Beam"),
        },
    )
    x_ray_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000010, original_name="X-Ray Visor"),
        },
    )
    ice_spreader: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000011, original_name="Ice Spreader"),
        },
    )
    space_jump_boots: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000012, original_name="Space Jump Boots"),
        },
    )
    morph_ball: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="Morph Ball"),
        },
    )
    combat_visor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000014, original_name="Combat Visor"),
        },
    )
    boost_ball: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000015, original_name="Boost Ball"),
        },
    )
    spider_ball: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000016, original_name="Spider Ball"),
        },
    )
    power_suit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000017, original_name="Power Suit?"),
        },
    )
    gravity_suit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000018, original_name="Gravity Suit"),
        },
    )
    varia_suit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000019, original_name="Varia Suit"),
        },
    )
    phazon_suit: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001A, original_name="Phazon Suit"),
        },
    )
    energy_tanks: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001B, original_name="Energy Tanks"),
        },
    )
    unknown_item_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001C, original_name="Unknown Item 1"),
        },
    )
    health_refill: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001D, original_name="Health Refill"),
        },
    )
    unknown_item_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001E, original_name="Unknown Item 2"),
        },
    )
    wavebuster: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="Wavebuster"),
        },
    )
    default_spawn: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000020, original_name="Default Spawn"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000021, original_name="Active"),
        },
    )
    morphed: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000022, original_name="Morphed"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0xF

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        power_beam = structs.BIG_l.unpack(data.read(4))[0]
        ice_beam = structs.BIG_l.unpack(data.read(4))[0]
        wave_beam = structs.BIG_l.unpack(data.read(4))[0]
        plasma_beam = structs.BIG_l.unpack(data.read(4))[0]
        missiles = structs.BIG_l.unpack(data.read(4))[0]
        scan_visor = structs.BIG_l.unpack(data.read(4))[0]
        morph_ball_bomb = structs.BIG_l.unpack(data.read(4))[0]
        power_bombs = structs.BIG_l.unpack(data.read(4))[0]
        flamethrower = structs.BIG_l.unpack(data.read(4))[0]
        thermal_visor = structs.BIG_l.unpack(data.read(4))[0]
        charge_beam = structs.BIG_l.unpack(data.read(4))[0]
        super_missile = structs.BIG_l.unpack(data.read(4))[0]
        grapple_beam = structs.BIG_l.unpack(data.read(4))[0]
        x_ray_visor = structs.BIG_l.unpack(data.read(4))[0]
        ice_spreader = structs.BIG_l.unpack(data.read(4))[0]
        space_jump_boots = structs.BIG_l.unpack(data.read(4))[0]
        morph_ball = structs.BIG_l.unpack(data.read(4))[0]
        combat_visor = structs.BIG_l.unpack(data.read(4))[0]
        boost_ball = structs.BIG_l.unpack(data.read(4))[0]
        spider_ball = structs.BIG_l.unpack(data.read(4))[0]
        power_suit = structs.BIG_l.unpack(data.read(4))[0]
        gravity_suit = structs.BIG_l.unpack(data.read(4))[0]
        varia_suit = structs.BIG_l.unpack(data.read(4))[0]
        phazon_suit = structs.BIG_l.unpack(data.read(4))[0]
        energy_tanks = structs.BIG_l.unpack(data.read(4))[0]
        unknown_item_1 = structs.BIG_l.unpack(data.read(4))[0]
        health_refill = structs.BIG_l.unpack(data.read(4))[0]
        unknown_item_2 = structs.BIG_l.unpack(data.read(4))[0]
        wavebuster = structs.BIG_l.unpack(data.read(4))[0]
        default_spawn = structs.BIG_bool_.unpack(data.read(1))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        morphed = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            power_beam,
            ice_beam,
            wave_beam,
            plasma_beam,
            missiles,
            scan_visor,
            morph_ball_bomb,
            power_bombs,
            flamethrower,
            thermal_visor,
            charge_beam,
            super_missile,
            grapple_beam,
            x_ray_visor,
            ice_spreader,
            space_jump_boots,
            morph_ball,
            combat_visor,
            boost_ball,
            spider_ball,
            power_suit,
            gravity_suit,
            varia_suit,
            phazon_suit,
            energy_tanks,
            unknown_item_1,
            health_refill,
            unknown_item_2,
            wavebuster,
            default_spawn,
            active,
            morphed,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00#")  # 35 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.power_beam))
        data.write(structs.BIG_l.pack(self.ice_beam))
        data.write(structs.BIG_l.pack(self.wave_beam))
        data.write(structs.BIG_l.pack(self.plasma_beam))
        data.write(structs.BIG_l.pack(self.missiles))
        data.write(structs.BIG_l.pack(self.scan_visor))
        data.write(structs.BIG_l.pack(self.morph_ball_bomb))
        data.write(structs.BIG_l.pack(self.power_bombs))
        data.write(structs.BIG_l.pack(self.flamethrower))
        data.write(structs.BIG_l.pack(self.thermal_visor))
        data.write(structs.BIG_l.pack(self.charge_beam))
        data.write(structs.BIG_l.pack(self.super_missile))
        data.write(structs.BIG_l.pack(self.grapple_beam))
        data.write(structs.BIG_l.pack(self.x_ray_visor))
        data.write(structs.BIG_l.pack(self.ice_spreader))
        data.write(structs.BIG_l.pack(self.space_jump_boots))
        data.write(structs.BIG_l.pack(self.morph_ball))
        data.write(structs.BIG_l.pack(self.combat_visor))
        data.write(structs.BIG_l.pack(self.boost_ball))
        data.write(structs.BIG_l.pack(self.spider_ball))
        data.write(structs.BIG_l.pack(self.power_suit))
        data.write(structs.BIG_l.pack(self.gravity_suit))
        data.write(structs.BIG_l.pack(self.varia_suit))
        data.write(structs.BIG_l.pack(self.phazon_suit))
        data.write(structs.BIG_l.pack(self.energy_tanks))
        data.write(structs.BIG_l.pack(self.unknown_item_1))
        data.write(structs.BIG_l.pack(self.health_refill))
        data.write(structs.BIG_l.pack(self.unknown_item_2))
        data.write(structs.BIG_l.pack(self.wavebuster))
        data.write(structs.BIG_bool_.pack(self.default_spawn))
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_bool_.pack(self.morphed))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpawnPointJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            power_beam=json_data["power_beam"],
            ice_beam=json_data["ice_beam"],
            wave_beam=json_data["wave_beam"],
            plasma_beam=json_data["plasma_beam"],
            missiles=json_data["missiles"],
            scan_visor=json_data["scan_visor"],
            morph_ball_bomb=json_data["morph_ball_bomb"],
            power_bombs=json_data["power_bombs"],
            flamethrower=json_data["flamethrower"],
            thermal_visor=json_data["thermal_visor"],
            charge_beam=json_data["charge_beam"],
            super_missile=json_data["super_missile"],
            grapple_beam=json_data["grapple_beam"],
            x_ray_visor=json_data["x_ray_visor"],
            ice_spreader=json_data["ice_spreader"],
            space_jump_boots=json_data["space_jump_boots"],
            morph_ball=json_data["morph_ball"],
            combat_visor=json_data["combat_visor"],
            boost_ball=json_data["boost_ball"],
            spider_ball=json_data["spider_ball"],
            power_suit=json_data["power_suit"],
            gravity_suit=json_data["gravity_suit"],
            varia_suit=json_data["varia_suit"],
            phazon_suit=json_data["phazon_suit"],
            energy_tanks=json_data["energy_tanks"],
            unknown_item_1=json_data["unknown_item_1"],
            health_refill=json_data["health_refill"],
            unknown_item_2=json_data["unknown_item_2"],
            wavebuster=json_data["wavebuster"],
            default_spawn=json_data["default_spawn"],
            active=json_data["active"],
            morphed=json_data["morphed"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "power_beam": self.power_beam,
            "ice_beam": self.ice_beam,
            "wave_beam": self.wave_beam,
            "plasma_beam": self.plasma_beam,
            "missiles": self.missiles,
            "scan_visor": self.scan_visor,
            "morph_ball_bomb": self.morph_ball_bomb,
            "power_bombs": self.power_bombs,
            "flamethrower": self.flamethrower,
            "thermal_visor": self.thermal_visor,
            "charge_beam": self.charge_beam,
            "super_missile": self.super_missile,
            "grapple_beam": self.grapple_beam,
            "x_ray_visor": self.x_ray_visor,
            "ice_spreader": self.ice_spreader,
            "space_jump_boots": self.space_jump_boots,
            "morph_ball": self.morph_ball,
            "combat_visor": self.combat_visor,
            "boost_ball": self.boost_ball,
            "spider_ball": self.spider_ball,
            "power_suit": self.power_suit,
            "gravity_suit": self.gravity_suit,
            "varia_suit": self.varia_suit,
            "phazon_suit": self.phazon_suit,
            "energy_tanks": self.energy_tanks,
            "unknown_item_1": self.unknown_item_1,
            "health_refill": self.health_refill,
            "unknown_item_2": self.unknown_item_2,
            "wavebuster": self.wavebuster,
            "default_spawn": self.default_spawn,
            "active": self.active,
            "morphed": self.morphed,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
