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
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct20Json(typing_extensions.TypedDict):
        health: float
        animation_speed: float
        heart_vulnerability: json_util.JsonObject
        body_vulnerability: json_util.JsonObject
        mouth_vulnerability: json_util.JsonObject
        stun_threshold: float
        stun_decay: float
        unknown_0x7d185e91: float
        unknown_0x9b78f170: float
        damage_info: json_util.JsonObject
        unknown_0x93b08ac8: float
        dash_delay_maximum: float
        dash_delay_minimum: float
        dash_delay_variance: float
        wander_distance: float
        too_far_distance: float
        berserk_distance: float
        shock_wave_info: json_util.JsonObject
        bomb: json_util.JsonObject
        unknown_0x54cfed2a: float
        unknown_0x94a19a8b: float
        unknown_0x72c1356a: float
        unknown_0xe291a671: int
        unknown_0xa793e5f3: int
        unknown_0x19774dec: int
        circle_chance: float
        circle_right_chance: float
        circle_left_chance: float
        circle_north_chance: float
        circle_south_chance: float
        circle_pause_chance: float
        bomb_chance: float
        fade_out_target_alpha: float
        fade_out_delta: float
        fade_in_target_alpha: float
        fade_in_delta: float
        unknown_0x20dc1c96: float


@dataclasses.dataclass()
class UnknownStruct20(BaseProperty):
    health: float = dataclasses.field(
        default=750.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0668919, original_name="Health"),
        },
    )
    animation_speed: float = dataclasses.field(
        default=1.100000023841858,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC5407757, original_name="AnimationSpeed"),
        },
    )
    heart_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xF064B3BC,
                original_name="HeartVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    body_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0D9230D1,
                original_name="BodyVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    mouth_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xED7EDCA3,
                original_name="MouthVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    stun_threshold: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BDD1E4C, original_name="StunThreshold"),
        },
    )
    stun_decay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6082430F, original_name="StunDecay"),
        },
    )
    unknown_0x7d185e91: float = dataclasses.field(
        default=7.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D185E91, original_name="Unknown"),
        },
    )
    unknown_0x9b78f170: float = dataclasses.field(
        default=11.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9B78F170, original_name="Unknown"),
        },
    )
    damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x24B933D3,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x93b08ac8: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x93B08AC8, original_name="Unknown"),
        },
    )
    dash_delay_maximum: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B37EDA7, original_name="DashDelayMaximum"),
        },
    )
    dash_delay_minimum: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B44FD4D, original_name="DashDelayMinimum"),
        },
    )
    dash_delay_variance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDAC05EB5, original_name="DashDelayVariance"),
        },
    )
    wander_distance: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAF270C93, original_name="WanderDistance"),
        },
    )
    too_far_distance: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8819688D, original_name="TooFarDistance"),
        },
    )
    berserk_distance: float = dataclasses.field(
        default=44.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC9BBAF9, original_name="BerserkDistance"),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x9C32D0A0,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    bomb: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x4EA6C6A9,
                original_name="Bomb",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    unknown_0x54cfed2a: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54CFED2A, original_name="Unknown"),
        },
    )
    unknown_0x94a19a8b: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x94A19A8B, original_name="Unknown"),
        },
    )
    unknown_0x72c1356a: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72C1356A, original_name="Unknown"),
        },
    )
    unknown_0xe291a671: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE291A671, original_name="Unknown"),
        },
    )
    unknown_0xa793e5f3: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA793E5F3, original_name="Unknown"),
        },
    )
    unknown_0x19774dec: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x19774DEC, original_name="Unknown"),
        },
    )
    circle_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x482B7704, original_name="CircleChance"),
        },
    )
    circle_right_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3544D67, original_name="CircleRightChance"),
        },
    )
    circle_left_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA247C47C, original_name="CircleLeftChance"),
        },
    )
    circle_north_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6515999E, original_name="CircleNorthChance"),
        },
    )
    circle_south_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEFB54F99, original_name="CircleSouthChance"),
        },
    )
    circle_pause_chance: float = dataclasses.field(
        default=200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC8D2E4A8, original_name="CirclePauseChance"),
        },
    )
    bomb_chance: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF3AD3881, original_name="BombChance"),
        },
    )
    fade_out_target_alpha: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x036E3C74, original_name="FadeOutTargetAlpha"),
        },
    )
    fade_out_delta: float = dataclasses.field(
        default=-0.02500000037252903,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2171C5ED, original_name="FadeOutDelta"),
        },
    )
    fade_in_target_alpha: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2515641C, original_name="FadeInTargetAlpha"),
        },
    )
    fade_in_delta: float = dataclasses.field(
        default=0.02500000037252903,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6E42BB15, original_name="FadeInDelta"),
        },
    )
    unknown_0x20dc1c96: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x20DC1C96, original_name="Unknown"),
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
        if property_count != 37:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0668919
        health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5407757
        animation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF064B3BC
        heart_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D9230D1
        body_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED7EDCA3
        mouth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BDD1E4C
        stun_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6082430F
        stun_decay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D185E91
        unknown_0x7d185e91 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B78F170
        unknown_0x9b78f170 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24B933D3
        damage_info = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_damage": 3.0, "di_radius": 1.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93B08AC8
        unknown_0x93b08ac8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B37EDA7
        dash_delay_maximum = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B44FD4D
        dash_delay_minimum = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDAC05EB5
        dash_delay_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF270C93
        wander_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8819688D
        too_far_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC9BBAF9
        berserk_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C32D0A0
        shock_wave_info = ShockWaveInfo.from_stream(
            data, game, property_size, default_override={"duration": 5.0, "height": 2.0, "radial_velocity": 45.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EA6C6A9
        bomb = LaunchProjectileData.from_stream(
            data,
            game,
            property_size,
            default_override={
                "delay": 0.20000000298023224,
                "delay_variance": 0.10000000149011612,
                "stop_homing_range": 30.0,
                "generate_pickup_chance": 1.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54CFED2A
        unknown_0x54cfed2a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94A19A8B
        unknown_0x94a19a8b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72C1356A
        unknown_0x72c1356a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE291A671
        unknown_0xe291a671 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA793E5F3
        unknown_0xa793e5f3 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19774DEC
        unknown_0x19774dec = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x482B7704
        circle_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3544D67
        circle_right_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA247C47C
        circle_left_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6515999E
        circle_north_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEFB54F99
        circle_south_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8D2E4A8
        circle_pause_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3AD3881
        bomb_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x036E3C74
        fade_out_target_alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2171C5ED
        fade_out_delta = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2515641C
        fade_in_target_alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E42BB15
        fade_in_delta = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20DC1C96
        unknown_0x20dc1c96 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            health,
            animation_speed,
            heart_vulnerability,
            body_vulnerability,
            mouth_vulnerability,
            stun_threshold,
            stun_decay,
            unknown_0x7d185e91,
            unknown_0x9b78f170,
            damage_info,
            unknown_0x93b08ac8,
            dash_delay_maximum,
            dash_delay_minimum,
            dash_delay_variance,
            wander_distance,
            too_far_distance,
            berserk_distance,
            shock_wave_info,
            bomb,
            unknown_0x54cfed2a,
            unknown_0x94a19a8b,
            unknown_0x72c1356a,
            unknown_0xe291a671,
            unknown_0xa793e5f3,
            unknown_0x19774dec,
            circle_chance,
            circle_right_chance,
            circle_left_chance,
            circle_north_chance,
            circle_south_chance,
            circle_pause_chance,
            bomb_chance,
            fade_out_target_alpha,
            fade_out_delta,
            fade_in_target_alpha,
            fade_in_delta,
            unknown_0x20dc1c96,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00%")  # 37 properties

        data.write(b"\xf0f\x89\x19")  # 0xf0668919
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.health))

        data.write(b"\xc5@wW")  # 0xc5407757
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.animation_speed))

        data.write(b"\xf0d\xb3\xbc")  # 0xf064b3bc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.heart_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\r\x920\xd1")  # 0xd9230d1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.body_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed~\xdc\xa3")  # 0xed7edca3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.mouth_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"[\xdd\x1eL")  # 0x5bdd1e4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_threshold))

        data.write(b"`\x82C\x0f")  # 0x6082430f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stun_decay))

        data.write(b"}\x18^\x91")  # 0x7d185e91
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7d185e91))

        data.write(b"\x9bx\xf1p")  # 0x9b78f170
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9b78f170))

        data.write(b"$\xb93\xd3")  # 0x24b933d3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info.to_stream(
            data, game, default_override={"di_damage": 3.0, "di_radius": 1.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x93\xb0\x8a\xc8")  # 0x93b08ac8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x93b08ac8))

        data.write(b"\x1b7\xed\xa7")  # 0x1b37eda7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_delay_maximum))

        data.write(b"\x8bD\xfdM")  # 0x8b44fd4d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_delay_minimum))

        data.write(b"\xda\xc0^\xb5")  # 0xdac05eb5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dash_delay_variance))

        data.write(b"\xaf'\x0c\x93")  # 0xaf270c93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wander_distance))

        data.write(b"\x88\x19h\x8d")  # 0x8819688d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.too_far_distance))

        data.write(b"\xbc\x9b\xba\xf9")  # 0xbc9bbaf9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.berserk_distance))

        data.write(b"\x9c2\xd0\xa0")  # 0x9c32d0a0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(
            data, game, default_override={"duration": 5.0, "height": 2.0, "radial_velocity": 45.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"N\xa6\xc6\xa9")  # 0x4ea6c6a9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.bomb.to_stream(
            data,
            game,
            default_override={
                "delay": 0.20000000298023224,
                "delay_variance": 0.10000000149011612,
                "stop_homing_range": 30.0,
                "generate_pickup_chance": 1.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"T\xcf\xed*")  # 0x54cfed2a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x54cfed2a))

        data.write(b"\x94\xa1\x9a\x8b")  # 0x94a19a8b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x94a19a8b))

        data.write(b"r\xc15j")  # 0x72c1356a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x72c1356a))

        data.write(b"\xe2\x91\xa6q")  # 0xe291a671
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe291a671))

        data.write(b"\xa7\x93\xe5\xf3")  # 0xa793e5f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa793e5f3))

        data.write(b"\x19wM\xec")  # 0x19774dec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x19774dec))

        data.write(b"H+w\x04")  # 0x482b7704
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.circle_chance))

        data.write(b"\xc3TMg")  # 0xc3544d67
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.circle_right_chance))

        data.write(b"\xa2G\xc4|")  # 0xa247c47c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.circle_left_chance))

        data.write(b"e\x15\x99\x9e")  # 0x6515999e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.circle_north_chance))

        data.write(b"\xef\xb5O\x99")  # 0xefb54f99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.circle_south_chance))

        data.write(b"\xc8\xd2\xe4\xa8")  # 0xc8d2e4a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.circle_pause_chance))

        data.write(b"\xf3\xad8\x81")  # 0xf3ad3881
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_chance))

        data.write(b"\x03n<t")  # 0x36e3c74
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_target_alpha))

        data.write(b"!q\xc5\xed")  # 0x2171c5ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_delta))

        data.write(b"%\x15d\x1c")  # 0x2515641c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_target_alpha))

        data.write(b"nB\xbb\x15")  # 0x6e42bb15
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_delta))

        data.write(b" \xdc\x1c\x96")  # 0x20dc1c96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x20dc1c96))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct20Json", data)
        return cls(
            health=json_data["health"],
            animation_speed=json_data["animation_speed"],
            heart_vulnerability=DamageVulnerability.from_json(json_data["heart_vulnerability"]),
            body_vulnerability=DamageVulnerability.from_json(json_data["body_vulnerability"]),
            mouth_vulnerability=DamageVulnerability.from_json(json_data["mouth_vulnerability"]),
            stun_threshold=json_data["stun_threshold"],
            stun_decay=json_data["stun_decay"],
            unknown_0x7d185e91=json_data["unknown_0x7d185e91"],
            unknown_0x9b78f170=json_data["unknown_0x9b78f170"],
            damage_info=DamageInfo.from_json(json_data["damage_info"]),
            unknown_0x93b08ac8=json_data["unknown_0x93b08ac8"],
            dash_delay_maximum=json_data["dash_delay_maximum"],
            dash_delay_minimum=json_data["dash_delay_minimum"],
            dash_delay_variance=json_data["dash_delay_variance"],
            wander_distance=json_data["wander_distance"],
            too_far_distance=json_data["too_far_distance"],
            berserk_distance=json_data["berserk_distance"],
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            bomb=LaunchProjectileData.from_json(json_data["bomb"]),
            unknown_0x54cfed2a=json_data["unknown_0x54cfed2a"],
            unknown_0x94a19a8b=json_data["unknown_0x94a19a8b"],
            unknown_0x72c1356a=json_data["unknown_0x72c1356a"],
            unknown_0xe291a671=json_data["unknown_0xe291a671"],
            unknown_0xa793e5f3=json_data["unknown_0xa793e5f3"],
            unknown_0x19774dec=json_data["unknown_0x19774dec"],
            circle_chance=json_data["circle_chance"],
            circle_right_chance=json_data["circle_right_chance"],
            circle_left_chance=json_data["circle_left_chance"],
            circle_north_chance=json_data["circle_north_chance"],
            circle_south_chance=json_data["circle_south_chance"],
            circle_pause_chance=json_data["circle_pause_chance"],
            bomb_chance=json_data["bomb_chance"],
            fade_out_target_alpha=json_data["fade_out_target_alpha"],
            fade_out_delta=json_data["fade_out_delta"],
            fade_in_target_alpha=json_data["fade_in_target_alpha"],
            fade_in_delta=json_data["fade_in_delta"],
            unknown_0x20dc1c96=json_data["unknown_0x20dc1c96"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "health": self.health,
            "animation_speed": self.animation_speed,
            "heart_vulnerability": self.heart_vulnerability.to_json(),
            "body_vulnerability": self.body_vulnerability.to_json(),
            "mouth_vulnerability": self.mouth_vulnerability.to_json(),
            "stun_threshold": self.stun_threshold,
            "stun_decay": self.stun_decay,
            "unknown_0x7d185e91": self.unknown_0x7d185e91,
            "unknown_0x9b78f170": self.unknown_0x9b78f170,
            "damage_info": self.damage_info.to_json(),
            "unknown_0x93b08ac8": self.unknown_0x93b08ac8,
            "dash_delay_maximum": self.dash_delay_maximum,
            "dash_delay_minimum": self.dash_delay_minimum,
            "dash_delay_variance": self.dash_delay_variance,
            "wander_distance": self.wander_distance,
            "too_far_distance": self.too_far_distance,
            "berserk_distance": self.berserk_distance,
            "shock_wave_info": self.shock_wave_info.to_json(),
            "bomb": self.bomb.to_json(),
            "unknown_0x54cfed2a": self.unknown_0x54cfed2a,
            "unknown_0x94a19a8b": self.unknown_0x94a19a8b,
            "unknown_0x72c1356a": self.unknown_0x72c1356a,
            "unknown_0xe291a671": self.unknown_0xe291a671,
            "unknown_0xa793e5f3": self.unknown_0xa793e5f3,
            "unknown_0x19774dec": self.unknown_0x19774dec,
            "circle_chance": self.circle_chance,
            "circle_right_chance": self.circle_right_chance,
            "circle_left_chance": self.circle_left_chance,
            "circle_north_chance": self.circle_north_chance,
            "circle_south_chance": self.circle_south_chance,
            "circle_pause_chance": self.circle_pause_chance,
            "bomb_chance": self.bomb_chance,
            "fade_out_target_alpha": self.fade_out_target_alpha,
            "fade_out_delta": self.fade_out_delta,
            "fade_in_target_alpha": self.fade_in_target_alpha,
            "fade_in_delta": self.fade_in_delta,
            "unknown_0x20dc1c96": self.unknown_0x20dc1c96,
        }


def _decode_heart_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_body_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_mouth_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_damage": 3.0, "di_radius": 1.0, "di_knock_back_power": 10.0}
    )


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(
        data, game, property_size, default_override={"duration": 5.0, "height": 2.0, "radial_velocity": 45.0}
    )


def _decode_bomb(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(
        data,
        game,
        property_size,
        default_override={
            "delay": 0.20000000298023224,
            "delay_variance": 0.10000000149011612,
            "stop_homing_range": 30.0,
            "generate_pickup_chance": 1.0,
        },
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF0668919: ("health", structs.decode_BIG_f),
    0xC5407757: ("animation_speed", structs.decode_BIG_f),
    0xF064B3BC: ("heart_vulnerability", _decode_heart_vulnerability),
    0x0D9230D1: ("body_vulnerability", _decode_body_vulnerability),
    0xED7EDCA3: ("mouth_vulnerability", _decode_mouth_vulnerability),
    0x5BDD1E4C: ("stun_threshold", structs.decode_BIG_f),
    0x6082430F: ("stun_decay", structs.decode_BIG_f),
    0x7D185E91: ("unknown_0x7d185e91", structs.decode_BIG_f),
    0x9B78F170: ("unknown_0x9b78f170", structs.decode_BIG_f),
    0x24B933D3: ("damage_info", _decode_damage_info),
    0x93B08AC8: ("unknown_0x93b08ac8", structs.decode_BIG_f),
    0x1B37EDA7: ("dash_delay_maximum", structs.decode_BIG_f),
    0x8B44FD4D: ("dash_delay_minimum", structs.decode_BIG_f),
    0xDAC05EB5: ("dash_delay_variance", structs.decode_BIG_f),
    0xAF270C93: ("wander_distance", structs.decode_BIG_f),
    0x8819688D: ("too_far_distance", structs.decode_BIG_f),
    0xBC9BBAF9: ("berserk_distance", structs.decode_BIG_f),
    0x9C32D0A0: ("shock_wave_info", _decode_shock_wave_info),
    0x4EA6C6A9: ("bomb", _decode_bomb),
    0x54CFED2A: ("unknown_0x54cfed2a", structs.decode_BIG_f),
    0x94A19A8B: ("unknown_0x94a19a8b", structs.decode_BIG_f),
    0x72C1356A: ("unknown_0x72c1356a", structs.decode_BIG_f),
    0xE291A671: ("unknown_0xe291a671", structs.decode_BIG_l),
    0xA793E5F3: ("unknown_0xa793e5f3", structs.decode_BIG_l),
    0x19774DEC: ("unknown_0x19774dec", structs.decode_BIG_l),
    0x482B7704: ("circle_chance", structs.decode_BIG_f),
    0xC3544D67: ("circle_right_chance", structs.decode_BIG_f),
    0xA247C47C: ("circle_left_chance", structs.decode_BIG_f),
    0x6515999E: ("circle_north_chance", structs.decode_BIG_f),
    0xEFB54F99: ("circle_south_chance", structs.decode_BIG_f),
    0xC8D2E4A8: ("circle_pause_chance", structs.decode_BIG_f),
    0xF3AD3881: ("bomb_chance", structs.decode_BIG_f),
    0x036E3C74: ("fade_out_target_alpha", structs.decode_BIG_f),
    0x2171C5ED: ("fade_out_delta", structs.decode_BIG_f),
    0x2515641C: ("fade_in_target_alpha", structs.decode_BIG_f),
    0x6E42BB15: ("fade_in_delta", structs.decode_BIG_f),
    0x20DC1C96: ("unknown_0x20dc1c96", structs.decode_BIG_f),
}
