# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class EmperorIngStage1TentacleDataJson(typing_extensions.TypedDict):
        health: json_util.JsonObject
        normal_vulnerability: json_util.JsonObject
        warp_attack_vulnerability: json_util.JsonObject
        melee_attack_vulnerability: json_util.JsonObject
        projectile_attack_vulnerability: json_util.JsonObject
        stay_retracted_time: float
        tentacle_damaged_sound: int


@dataclasses.dataclass()
class EmperorIngStage1TentacleData(BaseProperty):
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
    normal_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x29DF61E1,
                original_name="NormalVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    warp_attack_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x8D7378A4,
                original_name="WarpAttackVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    melee_attack_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x6C79054F,
                original_name="MeleeAttackVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    projectile_attack_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x3C2D2492,
                original_name="ProjectileAttackVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    stay_retracted_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x491C2657, original_name="StayRetractedTime"),
        },
    )
    tentacle_damaged_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE19F4608, original_name="TentacleDamagedSound"),
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
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29DF61E1
        normal_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D7378A4
        warp_attack_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C79054F
        melee_attack_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C2D2492
        projectile_attack_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x491C2657
        stay_retracted_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE19F4608
        tentacle_damaged_sound = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            health,
            normal_vulnerability,
            warp_attack_vulnerability,
            melee_attack_vulnerability,
            projectile_attack_vulnerability,
            stay_retracted_time,
            tentacle_damaged_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")\xdfa\xe1")  # 0x29df61e1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.normal_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8dsx\xa4")  # 0x8d7378a4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.warp_attack_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"ly\x05O")  # 0x6c79054f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.melee_attack_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"<-$\x92")  # 0x3c2d2492
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_attack_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"I\x1c&W")  # 0x491c2657
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stay_retracted_time))

        data.write(b"\xe1\x9fF\x08")  # 0xe19f4608
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.tentacle_damaged_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EmperorIngStage1TentacleDataJson", data)
        return cls(
            health=HealthInfo.from_json(json_data["health"]),
            normal_vulnerability=DamageVulnerability.from_json(json_data["normal_vulnerability"]),
            warp_attack_vulnerability=DamageVulnerability.from_json(json_data["warp_attack_vulnerability"]),
            melee_attack_vulnerability=DamageVulnerability.from_json(json_data["melee_attack_vulnerability"]),
            projectile_attack_vulnerability=DamageVulnerability.from_json(json_data["projectile_attack_vulnerability"]),
            stay_retracted_time=json_data["stay_retracted_time"],
            tentacle_damaged_sound=json_data["tentacle_damaged_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "health": self.health.to_json(),
            "normal_vulnerability": self.normal_vulnerability.to_json(),
            "warp_attack_vulnerability": self.warp_attack_vulnerability.to_json(),
            "melee_attack_vulnerability": self.melee_attack_vulnerability.to_json(),
            "projectile_attack_vulnerability": self.projectile_attack_vulnerability.to_json(),
            "stay_retracted_time": self.stay_retracted_time,
            "tentacle_damaged_sound": self.tentacle_damaged_sound,
        }

    def _dependencies_for_tentacle_damaged_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tentacle_damaged_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_tentacle_damaged_sound(asset_manager)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_normal_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_warp_attack_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_melee_attack_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_projectile_attack_vulnerability(
    data: typing.BinaryIO, game: Game, property_size: int
) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCF90D15E: ("health", _decode_health),
    0x29DF61E1: ("normal_vulnerability", _decode_normal_vulnerability),
    0x8D7378A4: ("warp_attack_vulnerability", _decode_warp_attack_vulnerability),
    0x6C79054F: ("melee_attack_vulnerability", _decode_melee_attack_vulnerability),
    0x3C2D2492: ("projectile_attack_vulnerability", _decode_projectile_attack_vulnerability),
    0x491C2657: ("stay_retracted_time", structs.decode_BIG_f),
    0xE19F4608: ("tentacle_damaged_sound", structs.decode_BIG_l),
}
