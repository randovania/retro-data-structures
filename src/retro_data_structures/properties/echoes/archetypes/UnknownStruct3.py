# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct3Json(typing_extensions.TypedDict):
        unknown_0x17cd8b2a: float
        unknown_0x1473dad2: float
        unknown_0x3650ce75: float
        unknown_0x78520e6e: float
        damage_angle: float
        horiz_speed: float
        vert_speed: float
        fire_rate: float
        unknown_0xf9bd253e: float
        max_attack_angle: float
        max_attack_range: float
        start_attack_range: float
        attack_leash_timer: float
        weapon_damage: json_util.JsonObject
        weapon_effect: int
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        state_machine: int
        telegraph_effect: int


@dataclasses.dataclass()
class UnknownStruct3(BaseProperty):
    unknown_0x17cd8b2a: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x17CD8B2A, original_name="Unknown"),
        },
    )
    unknown_0x1473dad2: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1473DAD2, original_name="Unknown"),
        },
    )
    unknown_0x3650ce75: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3650CE75, original_name="Unknown"),
        },
    )
    unknown_0x78520e6e: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78520E6E, original_name="Unknown"),
        },
    )
    damage_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA39A5D72, original_name="DamageAngle"),
        },
    )
    horiz_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB2E32DB, original_name="HorizSpeed"),
        },
    )
    vert_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B3C8683, original_name="VertSpeed"),
        },
    )
    fire_rate: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6E48F18, original_name="FireRate"),
        },
    )
    unknown_0xf9bd253e: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF9BD253E, original_name="Unknown"),
        },
    )
    max_attack_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF11F7384, original_name="MaxAttackAngle"),
        },
    )
    max_attack_range: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFF77C96F, original_name="MaxAttackRange"),
        },
    )
    start_attack_range: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB63F274C, original_name="StartAttackRange"),
        },
    )
    attack_leash_timer: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8D1EA77, original_name="AttackLeashTimer"),
        },
    )
    weapon_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8E5F7E96,
                original_name="WeaponDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    weapon_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC43360A7, original_name="WeaponEffect"),
        },
    )
    health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xCF90D15E,
                original_name="Health",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x7B71AE90,
                original_name="Vulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    state_machine: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["AFSM", "FSM2"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x55744160, original_name="StateMachine"),
        },
    )
    telegraph_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8F68AC21, original_name="TelegraphEffect"),
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
        if property_count != 19:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17CD8B2A
        unknown_0x17cd8b2a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1473DAD2
        unknown_0x1473dad2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3650CE75
        unknown_0x3650ce75 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78520E6E
        unknown_0x78520e6e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA39A5D72
        damage_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB2E32DB
        horiz_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B3C8683
        vert_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6E48F18
        fire_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9BD253E
        unknown_0xf9bd253e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF11F7384
        max_attack_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF77C96F
        max_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB63F274C
        start_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8D1EA77
        attack_leash_timer = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E5F7E96
        weapon_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC43360A7
        weapon_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55744160
        state_machine = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F68AC21
        telegraph_effect = structs.BIG_L.unpack(data.read(4))[0]

        return cls(
            unknown_0x17cd8b2a,
            unknown_0x1473dad2,
            unknown_0x3650ce75,
            unknown_0x78520e6e,
            damage_angle,
            horiz_speed,
            vert_speed,
            fire_rate,
            unknown_0xf9bd253e,
            max_attack_angle,
            max_attack_range,
            start_attack_range,
            attack_leash_timer,
            weapon_damage,
            weapon_effect,
            health,
            vulnerability,
            state_machine,
            telegraph_effect,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x13")  # 19 properties

        data.write(b"\x17\xcd\x8b*")  # 0x17cd8b2a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x17cd8b2a))

        data.write(b"\x14s\xda\xd2")  # 0x1473dad2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1473dad2))

        data.write(b"6P\xceu")  # 0x3650ce75
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3650ce75))

        data.write(b"xR\x0en")  # 0x78520e6e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78520e6e))

        data.write(b"\xa3\x9a]r")  # 0xa39a5d72
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_angle))

        data.write(b"\xfb.2\xdb")  # 0xfb2e32db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.horiz_speed))

        data.write(b"\x1b<\x86\x83")  # 0x1b3c8683
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vert_speed))

        data.write(b"\xc6\xe4\x8f\x18")  # 0xc6e48f18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fire_rate))

        data.write(b"\xf9\xbd%>")  # 0xf9bd253e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf9bd253e))

        data.write(b"\xf1\x1fs\x84")  # 0xf11f7384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_angle))

        data.write(b"\xffw\xc9o")  # 0xff77c96f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_range))

        data.write(b"\xb6?'L")  # 0xb63f274c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.start_attack_range))

        data.write(b"\xf8\xd1\xeaw")  # 0xf8d1ea77
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_leash_timer))

        data.write(b"\x8e_~\x96")  # 0x8e5f7e96
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc43`\xa7")  # 0xc43360a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.weapon_effect))

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"UtA`")  # 0x55744160
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.state_machine))

        data.write(b"\x8fh\xac!")  # 0x8f68ac21
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.telegraph_effect))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct3Json", data)
        return cls(
            unknown_0x17cd8b2a=json_data["unknown_0x17cd8b2a"],
            unknown_0x1473dad2=json_data["unknown_0x1473dad2"],
            unknown_0x3650ce75=json_data["unknown_0x3650ce75"],
            unknown_0x78520e6e=json_data["unknown_0x78520e6e"],
            damage_angle=json_data["damage_angle"],
            horiz_speed=json_data["horiz_speed"],
            vert_speed=json_data["vert_speed"],
            fire_rate=json_data["fire_rate"],
            unknown_0xf9bd253e=json_data["unknown_0xf9bd253e"],
            max_attack_angle=json_data["max_attack_angle"],
            max_attack_range=json_data["max_attack_range"],
            start_attack_range=json_data["start_attack_range"],
            attack_leash_timer=json_data["attack_leash_timer"],
            weapon_damage=DamageInfo.from_json(json_data["weapon_damage"]),
            weapon_effect=json_data["weapon_effect"],
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            state_machine=json_data["state_machine"],
            telegraph_effect=json_data["telegraph_effect"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x17cd8b2a": self.unknown_0x17cd8b2a,
            "unknown_0x1473dad2": self.unknown_0x1473dad2,
            "unknown_0x3650ce75": self.unknown_0x3650ce75,
            "unknown_0x78520e6e": self.unknown_0x78520e6e,
            "damage_angle": self.damage_angle,
            "horiz_speed": self.horiz_speed,
            "vert_speed": self.vert_speed,
            "fire_rate": self.fire_rate,
            "unknown_0xf9bd253e": self.unknown_0xf9bd253e,
            "max_attack_angle": self.max_attack_angle,
            "max_attack_range": self.max_attack_range,
            "start_attack_range": self.start_attack_range,
            "attack_leash_timer": self.attack_leash_timer,
            "weapon_damage": self.weapon_damage.to_json(),
            "weapon_effect": self.weapon_effect,
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "state_machine": self.state_machine,
            "telegraph_effect": self.telegraph_effect,
        }

    def _dependencies_for_weapon_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_effect)

    def _dependencies_for_state_machine(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.state_machine)

    def _dependencies_for_telegraph_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.telegraph_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_weapon_effect, "weapon_effect", "AssetId"),
            (self._dependencies_for_state_machine, "state_machine", "AssetId"),
            (self._dependencies_for_telegraph_effect, "telegraph_effect", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct3.{field_name} ({field_type}): {e}")


def _decode_weapon_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x17CD8B2A: ("unknown_0x17cd8b2a", structs.decode_BIG_f),
    0x1473DAD2: ("unknown_0x1473dad2", structs.decode_BIG_f),
    0x3650CE75: ("unknown_0x3650ce75", structs.decode_BIG_f),
    0x78520E6E: ("unknown_0x78520e6e", structs.decode_BIG_f),
    0xA39A5D72: ("damage_angle", structs.decode_BIG_f),
    0xFB2E32DB: ("horiz_speed", structs.decode_BIG_f),
    0x1B3C8683: ("vert_speed", structs.decode_BIG_f),
    0xC6E48F18: ("fire_rate", structs.decode_BIG_f),
    0xF9BD253E: ("unknown_0xf9bd253e", structs.decode_BIG_f),
    0xF11F7384: ("max_attack_angle", structs.decode_BIG_f),
    0xFF77C96F: ("max_attack_range", structs.decode_BIG_f),
    0xB63F274C: ("start_attack_range", structs.decode_BIG_f),
    0xF8D1EA77: ("attack_leash_timer", structs.decode_BIG_f),
    0x8E5F7E96: ("weapon_damage", _decode_weapon_damage),
    0xC43360A7: ("weapon_effect", structs.decode_BIG_L),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0x55744160: ("state_machine", structs.decode_BIG_L),
    0x8F68AC21: ("telegraph_effect", structs.decode_BIG_L),
}
