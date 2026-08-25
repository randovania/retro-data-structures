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
from retro_data_structures.properties.corruption.archetypes.PuddleControlData import PuddleControlData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PhazonPuddleDataJson(typing_extensions.TypedDict):
        state_machine: int
        health: json_util.JsonObject
        speed: float
        contact_damage: json_util.JsonObject
        unknown_0x49f4c4ee: float
        dot_damage: json_util.JsonObject
        dot_frequency: float
        dot_duration: float
        unknown_0x440da52f: int
        min_spawn_delay: float
        max_spawn_delay: float
        unknown_0xa62e602f: float
        unknown_0x85dd0b29: float
        shell_start_duration: float
        splash_delay: float
        min_splash_speed: float
        max_splash_speed: float
        unknown_0xa6bc177f: float
        unknown_0x7d034498: float
        min_wake_speed: float
        texture_align_delay: float
        normal: json_util.JsonObject
        suck_damage: float
        suck_range: float
        suck: json_util.JsonObject
        hurt: json_util.JsonObject
        puddle_control_data: json_util.JsonObject
        explosion: json_util.JsonObject
        contact: json_util.JsonObject
        blob_effect: int
        hit_normal_damage: int
        hit_heavy_damage: int
        death: int
        explosion_splash: int
        contact_splash: int
        leech_spawn: int
        ball_shell_start: int
        ball_shell_continue: int
        ball_shell_end: int
        ball_wake: int
        ball_wake_end: int
        sound_ball_shell_continue: int
        sound_ball_shell_end: int
        sound_touch: int
        sound_suck: int
        sound_spawn: int
        caud_0x49b30de2: int
        caud_0xdecd5831: int
        sound_death: int
        vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class PhazonPuddleData(BaseProperty):
    state_machine: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["FSM2"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x55744160, original_name="StateMachine"),
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
    speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6392404E, original_name="Speed"),
        },
    )
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
    unknown_0x49f4c4ee: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x49F4C4EE, original_name="Unknown"),
        },
    )
    dot_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xA7A47350,
                original_name="DotDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    dot_frequency: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x955A61EF, original_name="DotFrequency"),
        },
    )
    dot_duration: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x77A4EFB5, original_name="DotDuration"),
        },
    )
    unknown_0x440da52f: int = dataclasses.field(
        default=50,
        metadata={
            "reflection": FieldReflection[int](int, id=0x440DA52F, original_name="Unknown"),
        },
    )
    min_spawn_delay: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2646A843, original_name="MinSpawnDelay"),
        },
    )
    max_spawn_delay: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75E0B0A7, original_name="MaxSpawnDelay"),
        },
    )
    unknown_0xa62e602f: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA62E602F, original_name="Unknown"),
        },
    )
    unknown_0x85dd0b29: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x85DD0B29, original_name="Unknown"),
        },
    )
    shell_start_duration: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x45134ACE, original_name="ShellStartDuration"),
        },
    )
    splash_delay: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x308D4F23, original_name="SplashDelay"),
        },
    )
    min_splash_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x26797DF9, original_name="MinSplashSpeed"),
        },
    )
    max_splash_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x814DFD80, original_name="MaxSplashSpeed"),
        },
    )
    unknown_0xa6bc177f: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA6BC177F, original_name="Unknown"),
        },
    )
    unknown_0x7d034498: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D034498, original_name="Unknown"),
        },
    )
    min_wake_speed: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA4985156, original_name="MinWakeSpeed"),
        },
    )
    texture_align_delay: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x91D5B3CA, original_name="TextureAlignDelay"),
        },
    )
    normal: PuddleControlData = dataclasses.field(
        default_factory=PuddleControlData,
        metadata={
            "reflection": FieldReflection[PuddleControlData](
                PuddleControlData,
                id=0x5EE136E3,
                original_name="Normal",
                from_json=PuddleControlData.from_json,
                to_json=PuddleControlData.to_json,
            ),
        },
    )
    suck_damage: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC38B5712, original_name="SuckDamage"),
        },
    )
    suck_range: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4FB3C7C, original_name="SuckRange"),
        },
    )
    suck: PuddleControlData = dataclasses.field(
        default_factory=PuddleControlData,
        metadata={
            "reflection": FieldReflection[PuddleControlData](
                PuddleControlData,
                id=0xFB228140,
                original_name="Suck",
                from_json=PuddleControlData.from_json,
                to_json=PuddleControlData.to_json,
            ),
        },
    )
    hurt: PuddleControlData = dataclasses.field(
        default_factory=PuddleControlData,
        metadata={
            "reflection": FieldReflection[PuddleControlData](
                PuddleControlData,
                id=0xF2565B1B,
                original_name="Hurt",
                from_json=PuddleControlData.from_json,
                to_json=PuddleControlData.to_json,
            ),
        },
    )
    puddle_control_data: PuddleControlData = dataclasses.field(
        default_factory=PuddleControlData,
        metadata={
            "reflection": FieldReflection[PuddleControlData](
                PuddleControlData,
                id=0xB32D1B19,
                original_name="PuddleControlData",
                from_json=PuddleControlData.from_json,
                to_json=PuddleControlData.to_json,
            ),
        },
    )
    explosion: PuddleControlData = dataclasses.field(
        default_factory=PuddleControlData,
        metadata={
            "reflection": FieldReflection[PuddleControlData](
                PuddleControlData,
                id=0xFD6D2B52,
                original_name="Explosion",
                from_json=PuddleControlData.from_json,
                to_json=PuddleControlData.to_json,
            ),
        },
    )
    contact: PuddleControlData = dataclasses.field(
        default_factory=PuddleControlData,
        metadata={
            "reflection": FieldReflection[PuddleControlData](
                PuddleControlData,
                id=0x17B1C55E,
                original_name="Contact",
                from_json=PuddleControlData.from_json,
                to_json=PuddleControlData.to_json,
            ),
        },
    )
    blob_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2367F689, original_name="BlobEffect"),
        },
    )
    hit_normal_damage: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD473158D, original_name="HitNormalDamage"),
        },
    )
    hit_heavy_damage: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCCA298B4, original_name="HitHeavyDamage"),
        },
    )
    death: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB99C80D3, original_name="Death"),
        },
    )
    explosion_splash: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x96EA9F4B, original_name="ExplosionSplash"),
        },
    )
    contact_splash: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x21655924, original_name="ContactSplash"),
        },
    )
    leech_spawn: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x68261C78, original_name="LeechSpawn"),
        },
    )
    ball_shell_start: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE482BCA4, original_name="BallShellStart"),
        },
    )
    ball_shell_continue: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x812E9CC8, original_name="BallShellContinue"),
        },
    )
    ball_shell_end: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAEADE325, original_name="BallShellEnd"),
        },
    )
    ball_wake: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x10CFFAD6, original_name="BallWake"),
        },
    )
    ball_wake_end: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x78685EB2, original_name="BallWakeEnd"),
        },
    )
    sound_ball_shell_continue: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7027EE36, original_name="Sound_BallShellContinue"),
        },
    )
    sound_ball_shell_end: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8A53608D, original_name="Sound_BallShellEnd"),
        },
    )
    sound_touch: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF349BAAC, original_name="Sound_Touch"),
        },
    )
    sound_suck: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x10A4E795, original_name="Sound_Suck"),
        },
    )
    sound_spawn: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDFD54864, original_name="Sound_Spawn"),
        },
    )
    caud_0x49b30de2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x49B30DE2, original_name="CAUD"),
        },
    )
    caud_0xdecd5831: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDECD5831, original_name="CAUD"),
        },
    )
    sound_death: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1B412C4B, original_name="Sound_Death"),
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
        if property_count != 50:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55744160
        state_machine = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size, default_override={"health": 25.0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404E
        speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD756416E
        contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49F4C4EE
        unknown_0x49f4c4ee = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA7A47350
        dot_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x955A61EF
        dot_frequency = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77A4EFB5
        dot_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x440DA52F
        unknown_0x440da52f = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2646A843
        min_spawn_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75E0B0A7
        max_spawn_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA62E602F
        unknown_0xa62e602f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85DD0B29
        unknown_0x85dd0b29 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45134ACE
        shell_start_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x308D4F23
        splash_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26797DF9
        min_splash_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x814DFD80
        max_splash_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6BC177F
        unknown_0xa6bc177f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D034498
        unknown_0x7d034498 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4985156
        min_wake_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91D5B3CA
        texture_align_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5EE136E3
        normal = PuddleControlData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC38B5712
        suck_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4FB3C7C
        suck_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB228140
        suck = PuddleControlData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2565B1B
        hurt = PuddleControlData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB32D1B19
        puddle_control_data = PuddleControlData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFD6D2B52
        explosion = PuddleControlData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17B1C55E
        contact = PuddleControlData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2367F689
        blob_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD473158D
        hit_normal_damage = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCA298B4
        hit_heavy_damage = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB99C80D3
        death = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96EA9F4B
        explosion_splash = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21655924
        contact_splash = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68261C78
        leech_spawn = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE482BCA4
        ball_shell_start = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x812E9CC8
        ball_shell_continue = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAEADE325
        ball_shell_end = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10CFFAD6
        ball_wake = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78685EB2
        ball_wake_end = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7027EE36
        sound_ball_shell_continue = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A53608D
        sound_ball_shell_end = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF349BAAC
        sound_touch = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10A4E795
        sound_suck = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFD54864
        sound_spawn = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49B30DE2
        caud_0x49b30de2 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDECD5831
        caud_0xdecd5831 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B412C4B
        sound_death = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            state_machine,
            health,
            speed,
            contact_damage,
            unknown_0x49f4c4ee,
            dot_damage,
            dot_frequency,
            dot_duration,
            unknown_0x440da52f,
            min_spawn_delay,
            max_spawn_delay,
            unknown_0xa62e602f,
            unknown_0x85dd0b29,
            shell_start_duration,
            splash_delay,
            min_splash_speed,
            max_splash_speed,
            unknown_0xa6bc177f,
            unknown_0x7d034498,
            min_wake_speed,
            texture_align_delay,
            normal,
            suck_damage,
            suck_range,
            suck,
            hurt,
            puddle_control_data,
            explosion,
            contact,
            blob_effect,
            hit_normal_damage,
            hit_heavy_damage,
            death,
            explosion_splash,
            contact_splash,
            leech_spawn,
            ball_shell_start,
            ball_shell_continue,
            ball_shell_end,
            ball_wake,
            ball_wake_end,
            sound_ball_shell_continue,
            sound_ball_shell_end,
            sound_touch,
            sound_suck,
            sound_spawn,
            caud_0x49b30de2,
            caud_0xdecd5831,
            sound_death,
            vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x002")  # 50 properties

        data.write(b"UtA`")  # 0x55744160
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.state_machine))

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game, default_override={"health": 25.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"c\x92@N")  # 0x6392404e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b"\xd7VAn")  # 0xd756416e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"I\xf4\xc4\xee")  # 0x49f4c4ee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x49f4c4ee))

        data.write(b"\xa7\xa4sP")  # 0xa7a47350
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dot_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95Za\xef")  # 0x955a61ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dot_frequency))

        data.write(b"w\xa4\xef\xb5")  # 0x77a4efb5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dot_duration))

        data.write(b"D\r\xa5/")  # 0x440da52f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x440da52f))

        data.write(b"&F\xa8C")  # 0x2646a843
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_spawn_delay))

        data.write(b"u\xe0\xb0\xa7")  # 0x75e0b0a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_spawn_delay))

        data.write(b"\xa6.`/")  # 0xa62e602f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa62e602f))

        data.write(b"\x85\xdd\x0b)")  # 0x85dd0b29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x85dd0b29))

        data.write(b"E\x13J\xce")  # 0x45134ace
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell_start_duration))

        data.write(b"0\x8dO#")  # 0x308d4f23
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.splash_delay))

        data.write(b"&y}\xf9")  # 0x26797df9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_splash_speed))

        data.write(b"\x81M\xfd\x80")  # 0x814dfd80
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_splash_speed))

        data.write(b"\xa6\xbc\x17\x7f")  # 0xa6bc177f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa6bc177f))

        data.write(b"}\x03D\x98")  # 0x7d034498
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7d034498))

        data.write(b"\xa4\x98QV")  # 0xa4985156
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_wake_speed))

        data.write(b"\x91\xd5\xb3\xca")  # 0x91d5b3ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.texture_align_delay))

        data.write(b"^\xe16\xe3")  # 0x5ee136e3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.normal.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc3\x8bW\x12")  # 0xc38b5712
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.suck_damage))

        data.write(b"\xd4\xfb<|")  # 0xd4fb3c7c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.suck_range))

        data.write(b'\xfb"\x81@')  # 0xfb228140
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.suck.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf2V[\x1b")  # 0xf2565b1b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hurt.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3-\x1b\x19")  # 0xb32d1b19
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.puddle_control_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfdm+R")  # 0xfd6d2b52
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.explosion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x17\xb1\xc5^")  # 0x17b1c55e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.contact.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"#g\xf6\x89")  # 0x2367f689
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.blob_effect))

        data.write(b"\xd4s\x15\x8d")  # 0xd473158d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.hit_normal_damage))

        data.write(b"\xcc\xa2\x98\xb4")  # 0xcca298b4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.hit_heavy_damage))

        data.write(b"\xb9\x9c\x80\xd3")  # 0xb99c80d3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death))

        data.write(b"\x96\xea\x9fK")  # 0x96ea9f4b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.explosion_splash))

        data.write(b"!eY$")  # 0x21655924
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.contact_splash))

        data.write(b"h&\x1cx")  # 0x68261c78
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.leech_spawn))

        data.write(b"\xe4\x82\xbc\xa4")  # 0xe482bca4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ball_shell_start))

        data.write(b"\x81.\x9c\xc8")  # 0x812e9cc8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ball_shell_continue))

        data.write(b"\xae\xad\xe3%")  # 0xaeade325
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ball_shell_end))

        data.write(b"\x10\xcf\xfa\xd6")  # 0x10cffad6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ball_wake))

        data.write(b"xh^\xb2")  # 0x78685eb2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ball_wake_end))

        data.write(b"p'\xee6")  # 0x7027ee36
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_ball_shell_continue))

        data.write(b"\x8aS`\x8d")  # 0x8a53608d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_ball_shell_end))

        data.write(b"\xf3I\xba\xac")  # 0xf349baac
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_touch))

        data.write(b"\x10\xa4\xe7\x95")  # 0x10a4e795
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_suck))

        data.write(b"\xdf\xd5Hd")  # 0xdfd54864
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_spawn))

        data.write(b"I\xb3\r\xe2")  # 0x49b30de2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x49b30de2))

        data.write(b"\xde\xcdX1")  # 0xdecd5831
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xdecd5831))

        data.write(b"\x1bA,K")  # 0x1b412c4b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_death))

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PhazonPuddleDataJson", data)
        return cls(
            state_machine=json_data["state_machine"],
            health=HealthInfo.from_json(json_data["health"]),
            speed=json_data["speed"],
            contact_damage=DamageInfo.from_json(json_data["contact_damage"]),
            unknown_0x49f4c4ee=json_data["unknown_0x49f4c4ee"],
            dot_damage=DamageInfo.from_json(json_data["dot_damage"]),
            dot_frequency=json_data["dot_frequency"],
            dot_duration=json_data["dot_duration"],
            unknown_0x440da52f=json_data["unknown_0x440da52f"],
            min_spawn_delay=json_data["min_spawn_delay"],
            max_spawn_delay=json_data["max_spawn_delay"],
            unknown_0xa62e602f=json_data["unknown_0xa62e602f"],
            unknown_0x85dd0b29=json_data["unknown_0x85dd0b29"],
            shell_start_duration=json_data["shell_start_duration"],
            splash_delay=json_data["splash_delay"],
            min_splash_speed=json_data["min_splash_speed"],
            max_splash_speed=json_data["max_splash_speed"],
            unknown_0xa6bc177f=json_data["unknown_0xa6bc177f"],
            unknown_0x7d034498=json_data["unknown_0x7d034498"],
            min_wake_speed=json_data["min_wake_speed"],
            texture_align_delay=json_data["texture_align_delay"],
            normal=PuddleControlData.from_json(json_data["normal"]),
            suck_damage=json_data["suck_damage"],
            suck_range=json_data["suck_range"],
            suck=PuddleControlData.from_json(json_data["suck"]),
            hurt=PuddleControlData.from_json(json_data["hurt"]),
            puddle_control_data=PuddleControlData.from_json(json_data["puddle_control_data"]),
            explosion=PuddleControlData.from_json(json_data["explosion"]),
            contact=PuddleControlData.from_json(json_data["contact"]),
            blob_effect=json_data["blob_effect"],
            hit_normal_damage=json_data["hit_normal_damage"],
            hit_heavy_damage=json_data["hit_heavy_damage"],
            death=json_data["death"],
            explosion_splash=json_data["explosion_splash"],
            contact_splash=json_data["contact_splash"],
            leech_spawn=json_data["leech_spawn"],
            ball_shell_start=json_data["ball_shell_start"],
            ball_shell_continue=json_data["ball_shell_continue"],
            ball_shell_end=json_data["ball_shell_end"],
            ball_wake=json_data["ball_wake"],
            ball_wake_end=json_data["ball_wake_end"],
            sound_ball_shell_continue=json_data["sound_ball_shell_continue"],
            sound_ball_shell_end=json_data["sound_ball_shell_end"],
            sound_touch=json_data["sound_touch"],
            sound_suck=json_data["sound_suck"],
            sound_spawn=json_data["sound_spawn"],
            caud_0x49b30de2=json_data["caud_0x49b30de2"],
            caud_0xdecd5831=json_data["caud_0xdecd5831"],
            sound_death=json_data["sound_death"],
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "state_machine": self.state_machine,
            "health": self.health.to_json(),
            "speed": self.speed,
            "contact_damage": self.contact_damage.to_json(),
            "unknown_0x49f4c4ee": self.unknown_0x49f4c4ee,
            "dot_damage": self.dot_damage.to_json(),
            "dot_frequency": self.dot_frequency,
            "dot_duration": self.dot_duration,
            "unknown_0x440da52f": self.unknown_0x440da52f,
            "min_spawn_delay": self.min_spawn_delay,
            "max_spawn_delay": self.max_spawn_delay,
            "unknown_0xa62e602f": self.unknown_0xa62e602f,
            "unknown_0x85dd0b29": self.unknown_0x85dd0b29,
            "shell_start_duration": self.shell_start_duration,
            "splash_delay": self.splash_delay,
            "min_splash_speed": self.min_splash_speed,
            "max_splash_speed": self.max_splash_speed,
            "unknown_0xa6bc177f": self.unknown_0xa6bc177f,
            "unknown_0x7d034498": self.unknown_0x7d034498,
            "min_wake_speed": self.min_wake_speed,
            "texture_align_delay": self.texture_align_delay,
            "normal": self.normal.to_json(),
            "suck_damage": self.suck_damage,
            "suck_range": self.suck_range,
            "suck": self.suck.to_json(),
            "hurt": self.hurt.to_json(),
            "puddle_control_data": self.puddle_control_data.to_json(),
            "explosion": self.explosion.to_json(),
            "contact": self.contact.to_json(),
            "blob_effect": self.blob_effect,
            "hit_normal_damage": self.hit_normal_damage,
            "hit_heavy_damage": self.hit_heavy_damage,
            "death": self.death,
            "explosion_splash": self.explosion_splash,
            "contact_splash": self.contact_splash,
            "leech_spawn": self.leech_spawn,
            "ball_shell_start": self.ball_shell_start,
            "ball_shell_continue": self.ball_shell_continue,
            "ball_shell_end": self.ball_shell_end,
            "ball_wake": self.ball_wake,
            "ball_wake_end": self.ball_wake_end,
            "sound_ball_shell_continue": self.sound_ball_shell_continue,
            "sound_ball_shell_end": self.sound_ball_shell_end,
            "sound_touch": self.sound_touch,
            "sound_suck": self.sound_suck,
            "sound_spawn": self.sound_spawn,
            "caud_0x49b30de2": self.caud_0x49b30de2,
            "caud_0xdecd5831": self.caud_0xdecd5831,
            "sound_death": self.sound_death,
            "vulnerability": self.vulnerability.to_json(),
        }


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size, default_override={"health": 25.0})


def _decode_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_dot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_normal(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_suck(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_hurt(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_puddle_control_data(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_explosion(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_contact(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x55744160: ("state_machine", structs.decode_BIG_Q),
    0xCF90D15E: ("health", _decode_health),
    0x6392404E: ("speed", structs.decode_BIG_f),
    0xD756416E: ("contact_damage", _decode_contact_damage),
    0x49F4C4EE: ("unknown_0x49f4c4ee", structs.decode_BIG_f),
    0xA7A47350: ("dot_damage", _decode_dot_damage),
    0x955A61EF: ("dot_frequency", structs.decode_BIG_f),
    0x77A4EFB5: ("dot_duration", structs.decode_BIG_f),
    0x440DA52F: ("unknown_0x440da52f", structs.decode_BIG_l),
    0x2646A843: ("min_spawn_delay", structs.decode_BIG_f),
    0x75E0B0A7: ("max_spawn_delay", structs.decode_BIG_f),
    0xA62E602F: ("unknown_0xa62e602f", structs.decode_BIG_f),
    0x85DD0B29: ("unknown_0x85dd0b29", structs.decode_BIG_f),
    0x45134ACE: ("shell_start_duration", structs.decode_BIG_f),
    0x308D4F23: ("splash_delay", structs.decode_BIG_f),
    0x26797DF9: ("min_splash_speed", structs.decode_BIG_f),
    0x814DFD80: ("max_splash_speed", structs.decode_BIG_f),
    0xA6BC177F: ("unknown_0xa6bc177f", structs.decode_BIG_f),
    0x7D034498: ("unknown_0x7d034498", structs.decode_BIG_f),
    0xA4985156: ("min_wake_speed", structs.decode_BIG_f),
    0x91D5B3CA: ("texture_align_delay", structs.decode_BIG_f),
    0x5EE136E3: ("normal", _decode_normal),
    0xC38B5712: ("suck_damage", structs.decode_BIG_f),
    0xD4FB3C7C: ("suck_range", structs.decode_BIG_f),
    0xFB228140: ("suck", _decode_suck),
    0xF2565B1B: ("hurt", _decode_hurt),
    0xB32D1B19: ("puddle_control_data", _decode_puddle_control_data),
    0xFD6D2B52: ("explosion", _decode_explosion),
    0x17B1C55E: ("contact", _decode_contact),
    0x2367F689: ("blob_effect", structs.decode_BIG_Q),
    0xD473158D: ("hit_normal_damage", structs.decode_BIG_Q),
    0xCCA298B4: ("hit_heavy_damage", structs.decode_BIG_Q),
    0xB99C80D3: ("death", structs.decode_BIG_Q),
    0x96EA9F4B: ("explosion_splash", structs.decode_BIG_Q),
    0x21655924: ("contact_splash", structs.decode_BIG_Q),
    0x68261C78: ("leech_spawn", structs.decode_BIG_Q),
    0xE482BCA4: ("ball_shell_start", structs.decode_BIG_Q),
    0x812E9CC8: ("ball_shell_continue", structs.decode_BIG_Q),
    0xAEADE325: ("ball_shell_end", structs.decode_BIG_Q),
    0x10CFFAD6: ("ball_wake", structs.decode_BIG_Q),
    0x78685EB2: ("ball_wake_end", structs.decode_BIG_Q),
    0x7027EE36: ("sound_ball_shell_continue", structs.decode_BIG_Q),
    0x8A53608D: ("sound_ball_shell_end", structs.decode_BIG_Q),
    0xF349BAAC: ("sound_touch", structs.decode_BIG_Q),
    0x10A4E795: ("sound_suck", structs.decode_BIG_Q),
    0xDFD54864: ("sound_spawn", structs.decode_BIG_Q),
    0x49B30DE2: ("caud_0x49b30de2", structs.decode_BIG_Q),
    0xDECD5831: ("caud_0xdecd5831", structs.decode_BIG_Q),
    0x1B412C4B: ("sound_death", structs.decode_BIG_Q),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
}
