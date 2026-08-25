# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.SwarmSoundData import SwarmSoundData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SwarmBasicsDataJson(typing_extensions.TypedDict):
        contact_damage: json_util.JsonObject
        damage_wait_time: float
        collision_radius: float
        unknown_0xed999133: float
        touch_radius: float
        damage_radius: float
        speed: float
        count: int
        max_count: int
        influence_radius: float
        unknown_0x61959f0d: float
        alignment_priority: float
        separation_priority: float
        path_following_priority: float
        repulsor_avoidance_priority: float
        player_attract_priority: float
        player_attract_distance: float
        spawn_speed: float
        attacker_count: int
        attack_proximity: float
        attack_timer: float
        health: json_util.JsonObject
        damage_vulnerability: json_util.JsonObject
        death_particle_effect: int
        unknown_0x84f81f55: int
        attack_death_particle_effect: int
        unknown_0x90610f1a: int
        turn_rate: float
        unknown_0x7eb5d9e8: bool
        is_orbitable: bool
        unknown_0xbc01a28e: bool
        life_time: float
        locomotion_looped_sound: json_util.JsonObject
        attack_looped_sound: json_util.JsonObject
        swarm_sound_data_0x2646819a: json_util.JsonObject
        swarm_sound_data_0x373bebe3: json_util.JsonObject
        swarm_sound_data_0x9c417339: json_util.JsonObject
        swarm_sound_data_0x8d3c1940: json_util.JsonObject
        death_sound: int
        unknown_0x56c0d040: int


@dataclasses.dataclass()
class SwarmBasicsData(BaseProperty):
    contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xD756416E,
                original_name="ContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_wait_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE0CDC7E3, original_name="DamageWaitTime"),
        },
    )
    collision_radius: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A6AB139, original_name="CollisionRadius"),
        },
    )
    unknown_0xed999133: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED999133, original_name="Unknown"),
        },
    )
    touch_radius: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x068C8E81, original_name="TouchRadius"),
        },
    )
    damage_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0F598739, original_name="DamageRadius"),
        },
    )
    speed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6392404E, original_name="Speed"),
        },
    )
    count: int = dataclasses.field(
        default=50,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3291B8A2, original_name="Count"),
        },
    )
    max_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x54B68C4C, original_name="MaxCount"),
        },
    )
    influence_radius: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB160450E, original_name="InfluenceRadius"),
        },
    )
    unknown_0x61959f0d: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61959F0D, original_name="Unknown"),
        },
    )
    alignment_priority: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4841F1DE, original_name="AlignmentPriority"),
        },
    )
    separation_priority: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD293EBC4, original_name="SeparationPriority"),
        },
    )
    path_following_priority: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAE11F975, original_name="PathFollowingPriority"),
        },
    )
    repulsor_avoidance_priority: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA9322755, original_name="RepulsorAvoidancePriority"),
        },
    )
    player_attract_priority: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x87EDBCF1, original_name="PlayerAttractPriority"),
        },
    )
    player_attract_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x542BC812, original_name="PlayerAttractDistance"),
        },
    )
    spawn_speed: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA355C04F, original_name="SpawnSpeed"),
        },
    )
    attacker_count: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x523A405C, original_name="AttackerCount"),
        },
    )
    attack_proximity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1CA0E760, original_name="AttackProximity"),
        },
    )
    attack_timer: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88DF3EA8, original_name="AttackTimer"),
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
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x382E406E,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    death_particle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7D462930, original_name="DeathParticleEffect"),
        },
    )
    unknown_0x84f81f55: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x84F81F55, original_name="Unknown"),
        },
    )
    attack_death_particle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x16E6E8BD, original_name="AttackDeathParticleEffect"),
        },
    )
    unknown_0x90610f1a: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x90610F1A, original_name="Unknown"),
        },
    )
    turn_rate: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE34DC703, original_name="TurnRate"),
        },
    )
    unknown_0x7eb5d9e8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7EB5D9E8, original_name="Unknown"),
        },
    )
    is_orbitable: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x826BEC80, original_name="IsOrbitable"),
        },
    )
    unknown_0xbc01a28e: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBC01A28E, original_name="Unknown"),
        },
    )
    life_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB02DE555, original_name="LifeTime"),
        },
    )
    locomotion_looped_sound: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x80BBA072,
                original_name="LocomotionLoopedSound",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    attack_looped_sound: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x49CFBA93,
                original_name="AttackLoopedSound",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    swarm_sound_data_0x2646819a: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x2646819A,
                original_name="SwarmSoundData",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    swarm_sound_data_0x373bebe3: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x373BEBE3,
                original_name="SwarmSoundData",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    swarm_sound_data_0x9c417339: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x9C417339,
                original_name="SwarmSoundData",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    swarm_sound_data_0x8d3c1940: SwarmSoundData = dataclasses.field(
        default_factory=SwarmSoundData,
        metadata={
            "reflection": FieldReflection[SwarmSoundData](
                SwarmSoundData,
                id=0x8D3C1940,
                original_name="SwarmSoundData",
                from_json=SwarmSoundData.from_json,
                to_json=SwarmSoundData.to_json,
            ),
        },
    )
    death_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC7C3F610, original_name="DeathSound"),
        },
    )
    unknown_0x56c0d040: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x56C0D040, original_name="Unknown"),
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
        if property_count != 40:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD756416E
        contact_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_radius": 5.0, "di_knock_back_power": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0CDC7E3
        damage_wait_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A6AB139
        collision_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED999133
        unknown_0xed999133 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x068C8E81
        touch_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F598739
        damage_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404E
        speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3291B8A2
        count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54B68C4C
        max_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB160450E
        influence_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61959F0D
        unknown_0x61959f0d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4841F1DE
        alignment_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD293EBC4
        separation_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE11F975
        path_following_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9322755
        repulsor_avoidance_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87EDBCF1
        player_attract_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x542BC812
        player_attract_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA355C04F
        spawn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x523A405C
        attacker_count = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CA0E760
        attack_proximity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88DF3EA8
        attack_timer = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(
            data, game, property_size, default_override={"health": 2.0, "hi_knock_back_resistance": 2.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x382E406E
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D462930
        death_particle_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84F81F55
        unknown_0x84f81f55 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16E6E8BD
        attack_death_particle_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90610F1A
        unknown_0x90610f1a = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE34DC703
        turn_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7EB5D9E8
        unknown_0x7eb5d9e8 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x826BEC80
        is_orbitable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC01A28E
        unknown_0xbc01a28e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB02DE555
        life_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80BBA072
        locomotion_looped_sound = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49CFBA93
        attack_looped_sound = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2646819A
        swarm_sound_data_0x2646819a = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x373BEBE3
        swarm_sound_data_0x373bebe3 = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C417339
        swarm_sound_data_0x9c417339 = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D3C1940
        swarm_sound_data_0x8d3c1940 = SwarmSoundData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7C3F610
        death_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56C0D040
        unknown_0x56c0d040 = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            contact_damage,
            damage_wait_time,
            collision_radius,
            unknown_0xed999133,
            touch_radius,
            damage_radius,
            speed,
            count,
            max_count,
            influence_radius,
            unknown_0x61959f0d,
            alignment_priority,
            separation_priority,
            path_following_priority,
            repulsor_avoidance_priority,
            player_attract_priority,
            player_attract_distance,
            spawn_speed,
            attacker_count,
            attack_proximity,
            attack_timer,
            health,
            damage_vulnerability,
            death_particle_effect,
            unknown_0x84f81f55,
            attack_death_particle_effect,
            unknown_0x90610f1a,
            turn_rate,
            unknown_0x7eb5d9e8,
            is_orbitable,
            unknown_0xbc01a28e,
            life_time,
            locomotion_looped_sound,
            attack_looped_sound,
            swarm_sound_data_0x2646819a,
            swarm_sound_data_0x373bebe3,
            swarm_sound_data_0x9c417339,
            swarm_sound_data_0x8d3c1940,
            death_sound,
            unknown_0x56c0d040,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00(")  # 40 properties

        data.write(b"\xd7VAn")  # 0xd756416e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.contact_damage.to_stream(data, game, default_override={"di_radius": 5.0, "di_knock_back_power": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe0\xcd\xc7\xe3")  # 0xe0cdc7e3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_wait_time))

        data.write(b"\x8aj\xb19")  # 0x8a6ab139
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.collision_radius))

        data.write(b"\xed\x99\x913")  # 0xed999133
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xed999133))

        data.write(b"\x06\x8c\x8e\x81")  # 0x68c8e81
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.touch_radius))

        data.write(b"\x0fY\x879")  # 0xf598739
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_radius))

        data.write(b"c\x92@N")  # 0x6392404e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b"2\x91\xb8\xa2")  # 0x3291b8a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.count))

        data.write(b"T\xb6\x8cL")  # 0x54b68c4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_count))

        data.write(b"\xb1`E\x0e")  # 0xb160450e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.influence_radius))

        data.write(b"a\x95\x9f\r")  # 0x61959f0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x61959f0d))

        data.write(b"HA\xf1\xde")  # 0x4841f1de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alignment_priority))

        data.write(b"\xd2\x93\xeb\xc4")  # 0xd293ebc4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.separation_priority))

        data.write(b"\xae\x11\xf9u")  # 0xae11f975
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.path_following_priority))

        data.write(b"\xa92'U")  # 0xa9322755
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.repulsor_avoidance_priority))

        data.write(b"\x87\xed\xbc\xf1")  # 0x87edbcf1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_attract_priority))

        data.write(b"T+\xc8\x12")  # 0x542bc812
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_attract_distance))

        data.write(b"\xa3U\xc0O")  # 0xa355c04f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.spawn_speed))

        data.write(b"R:@\\")  # 0x523a405c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.attacker_count))

        data.write(b"\x1c\xa0\xe7`")  # 0x1ca0e760
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_proximity))

        data.write(b"\x88\xdf>\xa8")  # 0x88df3ea8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_timer))

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game, default_override={"health": 2.0, "hi_knock_back_resistance": 2.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"8.@n")  # 0x382e406e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"}F)0")  # 0x7d462930
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death_particle_effect))

        data.write(b"\x84\xf8\x1fU")  # 0x84f81f55
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x84f81f55))

        data.write(b"\x16\xe6\xe8\xbd")  # 0x16e6e8bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.attack_death_particle_effect))

        data.write(b"\x90a\x0f\x1a")  # 0x90610f1a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x90610f1a))

        data.write(b"\xe3M\xc7\x03")  # 0xe34dc703
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_rate))

        data.write(b"~\xb5\xd9\xe8")  # 0x7eb5d9e8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7eb5d9e8))

        data.write(b"\x82k\xec\x80")  # 0x826bec80
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_orbitable))

        data.write(b"\xbc\x01\xa2\x8e")  # 0xbc01a28e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbc01a28e))

        data.write(b"\xb0-\xe5U")  # 0xb02de555
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.life_time))

        data.write(b"\x80\xbb\xa0r")  # 0x80bba072
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.locomotion_looped_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"I\xcf\xba\x93")  # 0x49cfba93
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack_looped_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&F\x81\x9a")  # 0x2646819a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_sound_data_0x2646819a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"7;\xeb\xe3")  # 0x373bebe3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_sound_data_0x373bebe3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9cAs9")  # 0x9c417339
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_sound_data_0x9c417339.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8d<\x19@")  # 0x8d3c1940
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_sound_data_0x8d3c1940.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc7\xc3\xf6\x10")  # 0xc7c3f610
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death_sound))

        data.write(b"V\xc0\xd0@")  # 0x56c0d040
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x56c0d040))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwarmBasicsDataJson", data)
        return cls(
            contact_damage=DamageInfo.from_json(json_data["contact_damage"]),
            damage_wait_time=json_data["damage_wait_time"],
            collision_radius=json_data["collision_radius"],
            unknown_0xed999133=json_data["unknown_0xed999133"],
            touch_radius=json_data["touch_radius"],
            damage_radius=json_data["damage_radius"],
            speed=json_data["speed"],
            count=json_data["count"],
            max_count=json_data["max_count"],
            influence_radius=json_data["influence_radius"],
            unknown_0x61959f0d=json_data["unknown_0x61959f0d"],
            alignment_priority=json_data["alignment_priority"],
            separation_priority=json_data["separation_priority"],
            path_following_priority=json_data["path_following_priority"],
            repulsor_avoidance_priority=json_data["repulsor_avoidance_priority"],
            player_attract_priority=json_data["player_attract_priority"],
            player_attract_distance=json_data["player_attract_distance"],
            spawn_speed=json_data["spawn_speed"],
            attacker_count=json_data["attacker_count"],
            attack_proximity=json_data["attack_proximity"],
            attack_timer=json_data["attack_timer"],
            health=HealthInfo.from_json(json_data["health"]),
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
            death_particle_effect=json_data["death_particle_effect"],
            unknown_0x84f81f55=json_data["unknown_0x84f81f55"],
            attack_death_particle_effect=json_data["attack_death_particle_effect"],
            unknown_0x90610f1a=json_data["unknown_0x90610f1a"],
            turn_rate=json_data["turn_rate"],
            unknown_0x7eb5d9e8=json_data["unknown_0x7eb5d9e8"],
            is_orbitable=json_data["is_orbitable"],
            unknown_0xbc01a28e=json_data["unknown_0xbc01a28e"],
            life_time=json_data["life_time"],
            locomotion_looped_sound=SwarmSoundData.from_json(json_data["locomotion_looped_sound"]),
            attack_looped_sound=SwarmSoundData.from_json(json_data["attack_looped_sound"]),
            swarm_sound_data_0x2646819a=SwarmSoundData.from_json(json_data["swarm_sound_data_0x2646819a"]),
            swarm_sound_data_0x373bebe3=SwarmSoundData.from_json(json_data["swarm_sound_data_0x373bebe3"]),
            swarm_sound_data_0x9c417339=SwarmSoundData.from_json(json_data["swarm_sound_data_0x9c417339"]),
            swarm_sound_data_0x8d3c1940=SwarmSoundData.from_json(json_data["swarm_sound_data_0x8d3c1940"]),
            death_sound=json_data["death_sound"],
            unknown_0x56c0d040=json_data["unknown_0x56c0d040"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "contact_damage": self.contact_damage.to_json(),
            "damage_wait_time": self.damage_wait_time,
            "collision_radius": self.collision_radius,
            "unknown_0xed999133": self.unknown_0xed999133,
            "touch_radius": self.touch_radius,
            "damage_radius": self.damage_radius,
            "speed": self.speed,
            "count": self.count,
            "max_count": self.max_count,
            "influence_radius": self.influence_radius,
            "unknown_0x61959f0d": self.unknown_0x61959f0d,
            "alignment_priority": self.alignment_priority,
            "separation_priority": self.separation_priority,
            "path_following_priority": self.path_following_priority,
            "repulsor_avoidance_priority": self.repulsor_avoidance_priority,
            "player_attract_priority": self.player_attract_priority,
            "player_attract_distance": self.player_attract_distance,
            "spawn_speed": self.spawn_speed,
            "attacker_count": self.attacker_count,
            "attack_proximity": self.attack_proximity,
            "attack_timer": self.attack_timer,
            "health": self.health.to_json(),
            "damage_vulnerability": self.damage_vulnerability.to_json(),
            "death_particle_effect": self.death_particle_effect,
            "unknown_0x84f81f55": self.unknown_0x84f81f55,
            "attack_death_particle_effect": self.attack_death_particle_effect,
            "unknown_0x90610f1a": self.unknown_0x90610f1a,
            "turn_rate": self.turn_rate,
            "unknown_0x7eb5d9e8": self.unknown_0x7eb5d9e8,
            "is_orbitable": self.is_orbitable,
            "unknown_0xbc01a28e": self.unknown_0xbc01a28e,
            "life_time": self.life_time,
            "locomotion_looped_sound": self.locomotion_looped_sound.to_json(),
            "attack_looped_sound": self.attack_looped_sound.to_json(),
            "swarm_sound_data_0x2646819a": self.swarm_sound_data_0x2646819a.to_json(),
            "swarm_sound_data_0x373bebe3": self.swarm_sound_data_0x373bebe3.to_json(),
            "swarm_sound_data_0x9c417339": self.swarm_sound_data_0x9c417339.to_json(),
            "swarm_sound_data_0x8d3c1940": self.swarm_sound_data_0x8d3c1940.to_json(),
            "death_sound": self.death_sound,
            "unknown_0x56c0d040": self.unknown_0x56c0d040,
        }


def _decode_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_radius": 5.0, "di_knock_back_power": 5.0}
    )


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(
        data, game, property_size, default_override={"health": 2.0, "hi_knock_back_resistance": 2.0}
    )


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_locomotion_looped_sound(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_attack_looped_sound(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_swarm_sound_data_0x2646819a(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_swarm_sound_data_0x373bebe3(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_swarm_sound_data_0x9c417339(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_swarm_sound_data_0x8d3c1940(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD756416E: ("contact_damage", _decode_contact_damage),
    0xE0CDC7E3: ("damage_wait_time", structs.decode_BIG_f),
    0x8A6AB139: ("collision_radius", structs.decode_BIG_f),
    0xED999133: ("unknown_0xed999133", structs.decode_BIG_f),
    0x068C8E81: ("touch_radius", structs.decode_BIG_f),
    0x0F598739: ("damage_radius", structs.decode_BIG_f),
    0x6392404E: ("speed", structs.decode_BIG_f),
    0x3291B8A2: ("count", structs.decode_BIG_l),
    0x54B68C4C: ("max_count", structs.decode_BIG_l),
    0xB160450E: ("influence_radius", structs.decode_BIG_f),
    0x61959F0D: ("unknown_0x61959f0d", structs.decode_BIG_f),
    0x4841F1DE: ("alignment_priority", structs.decode_BIG_f),
    0xD293EBC4: ("separation_priority", structs.decode_BIG_f),
    0xAE11F975: ("path_following_priority", structs.decode_BIG_f),
    0xA9322755: ("repulsor_avoidance_priority", structs.decode_BIG_f),
    0x87EDBCF1: ("player_attract_priority", structs.decode_BIG_f),
    0x542BC812: ("player_attract_distance", structs.decode_BIG_f),
    0xA355C04F: ("spawn_speed", structs.decode_BIG_f),
    0x523A405C: ("attacker_count", structs.decode_BIG_l),
    0x1CA0E760: ("attack_proximity", structs.decode_BIG_f),
    0x88DF3EA8: ("attack_timer", structs.decode_BIG_f),
    0xCF90D15E: ("health", _decode_health),
    0x382E406E: ("damage_vulnerability", _decode_damage_vulnerability),
    0x7D462930: ("death_particle_effect", structs.decode_BIG_Q),
    0x84F81F55: ("unknown_0x84f81f55", structs.decode_BIG_l),
    0x16E6E8BD: ("attack_death_particle_effect", structs.decode_BIG_Q),
    0x90610F1A: ("unknown_0x90610f1a", structs.decode_BIG_l),
    0xE34DC703: ("turn_rate", structs.decode_BIG_f),
    0x7EB5D9E8: ("unknown_0x7eb5d9e8", structs.decode_BIG_bool_),
    0x826BEC80: ("is_orbitable", structs.decode_BIG_bool_),
    0xBC01A28E: ("unknown_0xbc01a28e", structs.decode_BIG_bool_),
    0xB02DE555: ("life_time", structs.decode_BIG_f),
    0x80BBA072: ("locomotion_looped_sound", _decode_locomotion_looped_sound),
    0x49CFBA93: ("attack_looped_sound", _decode_attack_looped_sound),
    0x2646819A: ("swarm_sound_data_0x2646819a", _decode_swarm_sound_data_0x2646819a),
    0x373BEBE3: ("swarm_sound_data_0x373bebe3", _decode_swarm_sound_data_0x373bebe3),
    0x9C417339: ("swarm_sound_data_0x9c417339", _decode_swarm_sound_data_0x9c417339),
    0x8D3C1940: ("swarm_sound_data_0x8d3c1940", _decode_swarm_sound_data_0x8d3c1940),
    0xC7C3F610: ("death_sound", structs.decode_BIG_Q),
    0x56C0D040: ("unknown_0x56c0d040", structs.decode_BIG_l),
}
