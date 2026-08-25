# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.BasicSwarmProperties import BasicSwarmProperties
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage3StructA import EmperorIngStage3StructA
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage3StructB import EmperorIngStage3StructB
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.echoes.archetypes.UnknownStruct26 import UnknownStruct26
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class EmperorIngStage3DataJson(typing_extensions.TypedDict):
        taunt_frequency: float
        yellow_health: json_util.JsonObject
        health: json_util.JsonObject
        vulnerable_time: float
        vulnerable_damage_threshold: float
        red_vulnerability: json_util.JsonObject
        light_vulnerability: json_util.JsonObject
        dark_vulnerability: json_util.JsonObject
        melee_damage: json_util.JsonObject
        damage_info: json_util.JsonObject
        jump_slide_damage: json_util.JsonObject
        ground_pound_damage: json_util.JsonObject
        emperor_ing_stage3_struct_a_0x98e311c1: json_util.JsonObject
        emperor_ing_stage3_struct_a_0x93dae216: json_util.JsonObject
        light_swarm_effect: int
        light_swarm_properties: json_util.JsonObject
        light_swarm_death_sound: json_util.JsonObject
        audio_playback_parms: json_util.JsonObject
        unknown_struct26: json_util.JsonObject
        jump_attack_shock_wave_info: json_util.JsonObject
        sound: int
        emperor_ing_stage3_struct_b_0xe843417f: json_util.JsonObject
        emperor_ing_stage3_struct_b_0xd13bec3f: json_util.JsonObject
        emperor_ing_stage3_struct_b_0xc61388ff: json_util.JsonObject
        emperor_ing_stage3_struct_b_0xa3cab6bf: json_util.JsonObject


@dataclasses.dataclass()
class EmperorIngStage3Data(BaseProperty):
    taunt_frequency: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x293A0C19, original_name="TauntFrequency"),
        },
    )
    yellow_health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x8A3F760C,
                original_name="YellowHealth",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
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
    vulnerable_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x69BC5CD4, original_name="VulnerableTime"),
        },
    )
    vulnerable_damage_threshold: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB110E539, original_name="VulnerableDamageThreshold"),
        },
    )
    red_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x8D70D67A,
                original_name="RedVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    light_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x89C142F7,
                original_name="LightVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    dark_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x8855C118,
                original_name="DarkVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    melee_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xC9416034,
                original_name="MeleeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1440D152,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    jump_slide_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xEF582BD6,
                original_name="JumpSlideDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    ground_pound_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4738C321,
                original_name="GroundPoundDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    emperor_ing_stage3_struct_a_0x98e311c1: EmperorIngStage3StructA = dataclasses.field(
        default_factory=EmperorIngStage3StructA,
        metadata={
            "reflection": FieldReflection[EmperorIngStage3StructA](
                EmperorIngStage3StructA,
                id=0x98E311C1,
                original_name="EmperorIngStage3StructA",
                from_json=EmperorIngStage3StructA.from_json,
                to_json=EmperorIngStage3StructA.to_json,
            ),
        },
    )
    emperor_ing_stage3_struct_a_0x93dae216: EmperorIngStage3StructA = dataclasses.field(
        default_factory=EmperorIngStage3StructA,
        metadata={
            "reflection": FieldReflection[EmperorIngStage3StructA](
                EmperorIngStage3StructA,
                id=0x93DAE216,
                original_name="EmperorIngStage3StructA",
                from_json=EmperorIngStage3StructA.from_json,
                to_json=EmperorIngStage3StructA.to_json,
            ),
        },
    )
    light_swarm_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4F82B9E5, original_name="LightSwarmEffect"),
        },
    )
    light_swarm_properties: BasicSwarmProperties = dataclasses.field(
        default_factory=BasicSwarmProperties,
        metadata={
            "reflection": FieldReflection[BasicSwarmProperties](
                BasicSwarmProperties,
                id=0x043E9C2E,
                original_name="LightSwarmProperties",
                from_json=BasicSwarmProperties.from_json,
                to_json=BasicSwarmProperties.to_json,
            ),
        },
    )
    light_swarm_death_sound: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x91001508,
                original_name="LightSwarmDeathSound",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x03552953,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_struct26: UnknownStruct26 = dataclasses.field(
        default_factory=UnknownStruct26,
        metadata={
            "reflection": FieldReflection[UnknownStruct26](
                UnknownStruct26,
                id=0xAF7E3033,
                original_name="UnknownStruct26",
                from_json=UnknownStruct26.from_json,
                to_json=UnknownStruct26.to_json,
            ),
        },
    )
    jump_attack_shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0xAB4ED456,
                original_name="JumpAttackShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x985F72FD, original_name="Sound"),
        },
    )
    emperor_ing_stage3_struct_b_0xe843417f: EmperorIngStage3StructB = dataclasses.field(
        default_factory=EmperorIngStage3StructB,
        metadata={
            "reflection": FieldReflection[EmperorIngStage3StructB](
                EmperorIngStage3StructB,
                id=0xE843417F,
                original_name="EmperorIngStage3StructB",
                from_json=EmperorIngStage3StructB.from_json,
                to_json=EmperorIngStage3StructB.to_json,
            ),
        },
    )
    emperor_ing_stage3_struct_b_0xd13bec3f: EmperorIngStage3StructB = dataclasses.field(
        default_factory=EmperorIngStage3StructB,
        metadata={
            "reflection": FieldReflection[EmperorIngStage3StructB](
                EmperorIngStage3StructB,
                id=0xD13BEC3F,
                original_name="EmperorIngStage3StructB",
                from_json=EmperorIngStage3StructB.from_json,
                to_json=EmperorIngStage3StructB.to_json,
            ),
        },
    )
    emperor_ing_stage3_struct_b_0xc61388ff: EmperorIngStage3StructB = dataclasses.field(
        default_factory=EmperorIngStage3StructB,
        metadata={
            "reflection": FieldReflection[EmperorIngStage3StructB](
                EmperorIngStage3StructB,
                id=0xC61388FF,
                original_name="EmperorIngStage3StructB",
                from_json=EmperorIngStage3StructB.from_json,
                to_json=EmperorIngStage3StructB.to_json,
            ),
        },
    )
    emperor_ing_stage3_struct_b_0xa3cab6bf: EmperorIngStage3StructB = dataclasses.field(
        default_factory=EmperorIngStage3StructB,
        metadata={
            "reflection": FieldReflection[EmperorIngStage3StructB](
                EmperorIngStage3StructB,
                id=0xA3CAB6BF,
                original_name="EmperorIngStage3StructB",
                from_json=EmperorIngStage3StructB.from_json,
                to_json=EmperorIngStage3StructB.to_json,
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
        if property_count != 25:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x293A0C19
        taunt_frequency = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A3F760C
        yellow_health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69BC5CD4
        vulnerable_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB110E539
        vulnerable_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D70D67A
        red_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89C142F7
        light_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8855C118
        dark_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9416034
        melee_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1440D152
        damage_info = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF582BD6
        jump_slide_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4738C321
        ground_pound_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98E311C1
        emperor_ing_stage3_struct_a_0x98e311c1 = EmperorIngStage3StructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93DAE216
        emperor_ing_stage3_struct_a_0x93dae216 = EmperorIngStage3StructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F82B9E5
        light_swarm_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x043E9C2E
        light_swarm_properties = BasicSwarmProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91001508
        light_swarm_death_sound = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03552953
        audio_playback_parms = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF7E3033
        unknown_struct26 = UnknownStruct26.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB4ED456
        jump_attack_shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x985F72FD
        sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE843417F
        emperor_ing_stage3_struct_b_0xe843417f = EmperorIngStage3StructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD13BEC3F
        emperor_ing_stage3_struct_b_0xd13bec3f = EmperorIngStage3StructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC61388FF
        emperor_ing_stage3_struct_b_0xc61388ff = EmperorIngStage3StructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3CAB6BF
        emperor_ing_stage3_struct_b_0xa3cab6bf = EmperorIngStage3StructB.from_stream(data, game, property_size)

        return cls(
            taunt_frequency,
            yellow_health,
            health,
            vulnerable_time,
            vulnerable_damage_threshold,
            red_vulnerability,
            light_vulnerability,
            dark_vulnerability,
            melee_damage,
            damage_info,
            jump_slide_damage,
            ground_pound_damage,
            emperor_ing_stage3_struct_a_0x98e311c1,
            emperor_ing_stage3_struct_a_0x93dae216,
            light_swarm_effect,
            light_swarm_properties,
            light_swarm_death_sound,
            audio_playback_parms,
            unknown_struct26,
            jump_attack_shock_wave_info,
            sound,
            emperor_ing_stage3_struct_b_0xe843417f,
            emperor_ing_stage3_struct_b_0xd13bec3f,
            emperor_ing_stage3_struct_b_0xc61388ff,
            emperor_ing_stage3_struct_b_0xa3cab6bf,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x19")  # 25 properties

        data.write(b"):\x0c\x19")  # 0x293a0c19
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.taunt_frequency))

        data.write(b"\x8a?v\x0c")  # 0x8a3f760c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.yellow_health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"i\xbc\\\xd4")  # 0x69bc5cd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vulnerable_time))

        data.write(b"\xb1\x10\xe59")  # 0xb110e539
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.vulnerable_damage_threshold))

        data.write(b"\x8dp\xd6z")  # 0x8d70d67a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.red_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x89\xc1B\xf7")  # 0x89c142f7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.light_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x88U\xc1\x18")  # 0x8855c118
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dark_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc9A`4")  # 0xc9416034
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x14@\xd1R")  # 0x1440d152
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xefX+\xd6")  # 0xef582bd6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.jump_slide_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"G8\xc3!")  # 0x4738c321
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ground_pound_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x98\xe3\x11\xc1")  # 0x98e311c1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.emperor_ing_stage3_struct_a_0x98e311c1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x93\xda\xe2\x16")  # 0x93dae216
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.emperor_ing_stage3_struct_a_0x93dae216.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"O\x82\xb9\xe5")  # 0x4f82b9e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.light_swarm_effect))

        data.write(b"\x04>\x9c.")  # 0x43e9c2e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.light_swarm_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x91\x00\x15\x08")  # 0x91001508
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.light_swarm_death_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x03U)S")  # 0x3552953
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaf~03")  # 0xaf7e3033
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct26.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xabN\xd4V")  # 0xab4ed456
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.jump_attack_shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x98_r\xfd")  # 0x985f72fd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound))

        data.write(b"\xe8CA\x7f")  # 0xe843417f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.emperor_ing_stage3_struct_b_0xe843417f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd1;\xec?")  # 0xd13bec3f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.emperor_ing_stage3_struct_b_0xd13bec3f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\x13\x88\xff")  # 0xc61388ff
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.emperor_ing_stage3_struct_b_0xc61388ff.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa3\xca\xb6\xbf")  # 0xa3cab6bf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.emperor_ing_stage3_struct_b_0xa3cab6bf.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EmperorIngStage3DataJson", data)
        return cls(
            taunt_frequency=json_data["taunt_frequency"],
            yellow_health=HealthInfo.from_json(json_data["yellow_health"]),
            health=HealthInfo.from_json(json_data["health"]),
            vulnerable_time=json_data["vulnerable_time"],
            vulnerable_damage_threshold=json_data["vulnerable_damage_threshold"],
            red_vulnerability=DamageVulnerability.from_json(json_data["red_vulnerability"]),
            light_vulnerability=DamageVulnerability.from_json(json_data["light_vulnerability"]),
            dark_vulnerability=DamageVulnerability.from_json(json_data["dark_vulnerability"]),
            melee_damage=DamageInfo.from_json(json_data["melee_damage"]),
            damage_info=DamageInfo.from_json(json_data["damage_info"]),
            jump_slide_damage=DamageInfo.from_json(json_data["jump_slide_damage"]),
            ground_pound_damage=DamageInfo.from_json(json_data["ground_pound_damage"]),
            emperor_ing_stage3_struct_a_0x98e311c1=EmperorIngStage3StructA.from_json(
                json_data["emperor_ing_stage3_struct_a_0x98e311c1"]
            ),
            emperor_ing_stage3_struct_a_0x93dae216=EmperorIngStage3StructA.from_json(
                json_data["emperor_ing_stage3_struct_a_0x93dae216"]
            ),
            light_swarm_effect=json_data["light_swarm_effect"],
            light_swarm_properties=BasicSwarmProperties.from_json(json_data["light_swarm_properties"]),
            light_swarm_death_sound=AudioPlaybackParms.from_json(json_data["light_swarm_death_sound"]),
            audio_playback_parms=AudioPlaybackParms.from_json(json_data["audio_playback_parms"]),
            unknown_struct26=UnknownStruct26.from_json(json_data["unknown_struct26"]),
            jump_attack_shock_wave_info=ShockWaveInfo.from_json(json_data["jump_attack_shock_wave_info"]),
            sound=json_data["sound"],
            emperor_ing_stage3_struct_b_0xe843417f=EmperorIngStage3StructB.from_json(
                json_data["emperor_ing_stage3_struct_b_0xe843417f"]
            ),
            emperor_ing_stage3_struct_b_0xd13bec3f=EmperorIngStage3StructB.from_json(
                json_data["emperor_ing_stage3_struct_b_0xd13bec3f"]
            ),
            emperor_ing_stage3_struct_b_0xc61388ff=EmperorIngStage3StructB.from_json(
                json_data["emperor_ing_stage3_struct_b_0xc61388ff"]
            ),
            emperor_ing_stage3_struct_b_0xa3cab6bf=EmperorIngStage3StructB.from_json(
                json_data["emperor_ing_stage3_struct_b_0xa3cab6bf"]
            ),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "taunt_frequency": self.taunt_frequency,
            "yellow_health": self.yellow_health.to_json(),
            "health": self.health.to_json(),
            "vulnerable_time": self.vulnerable_time,
            "vulnerable_damage_threshold": self.vulnerable_damage_threshold,
            "red_vulnerability": self.red_vulnerability.to_json(),
            "light_vulnerability": self.light_vulnerability.to_json(),
            "dark_vulnerability": self.dark_vulnerability.to_json(),
            "melee_damage": self.melee_damage.to_json(),
            "damage_info": self.damage_info.to_json(),
            "jump_slide_damage": self.jump_slide_damage.to_json(),
            "ground_pound_damage": self.ground_pound_damage.to_json(),
            "emperor_ing_stage3_struct_a_0x98e311c1": self.emperor_ing_stage3_struct_a_0x98e311c1.to_json(),
            "emperor_ing_stage3_struct_a_0x93dae216": self.emperor_ing_stage3_struct_a_0x93dae216.to_json(),
            "light_swarm_effect": self.light_swarm_effect,
            "light_swarm_properties": self.light_swarm_properties.to_json(),
            "light_swarm_death_sound": self.light_swarm_death_sound.to_json(),
            "audio_playback_parms": self.audio_playback_parms.to_json(),
            "unknown_struct26": self.unknown_struct26.to_json(),
            "jump_attack_shock_wave_info": self.jump_attack_shock_wave_info.to_json(),
            "sound": self.sound,
            "emperor_ing_stage3_struct_b_0xe843417f": self.emperor_ing_stage3_struct_b_0xe843417f.to_json(),
            "emperor_ing_stage3_struct_b_0xd13bec3f": self.emperor_ing_stage3_struct_b_0xd13bec3f.to_json(),
            "emperor_ing_stage3_struct_b_0xc61388ff": self.emperor_ing_stage3_struct_b_0xc61388ff.to_json(),
            "emperor_ing_stage3_struct_b_0xa3cab6bf": self.emperor_ing_stage3_struct_b_0xa3cab6bf.to_json(),
        }

    def _dependencies_for_light_swarm_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.light_swarm_effect)

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (
                self.emperor_ing_stage3_struct_a_0x98e311c1.dependencies_for,
                "emperor_ing_stage3_struct_a_0x98e311c1",
                "EmperorIngStage3StructA",
            ),
            (
                self.emperor_ing_stage3_struct_a_0x93dae216.dependencies_for,
                "emperor_ing_stage3_struct_a_0x93dae216",
                "EmperorIngStage3StructA",
            ),
            (self._dependencies_for_light_swarm_effect, "light_swarm_effect", "AssetId"),
            (self.light_swarm_properties.dependencies_for, "light_swarm_properties", "BasicSwarmProperties"),
            (self.light_swarm_death_sound.dependencies_for, "light_swarm_death_sound", "AudioPlaybackParms"),
            (self.audio_playback_parms.dependencies_for, "audio_playback_parms", "AudioPlaybackParms"),
            (self.unknown_struct26.dependencies_for, "unknown_struct26", "UnknownStruct26"),
            (self.jump_attack_shock_wave_info.dependencies_for, "jump_attack_shock_wave_info", "ShockWaveInfo"),
            (self._dependencies_for_sound, "sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for EmperorIngStage3Data.{field_name} ({field_type}): {e}")


def _decode_yellow_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_red_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_light_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_dark_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_jump_slide_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ground_pound_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_emperor_ing_stage3_struct_a_0x98e311c1(
    data: typing.BinaryIO, game: Game, property_size: int
) -> EmperorIngStage3StructA:
    return EmperorIngStage3StructA.from_stream(data, game, property_size)


def _decode_emperor_ing_stage3_struct_a_0x93dae216(
    data: typing.BinaryIO, game: Game, property_size: int
) -> EmperorIngStage3StructA:
    return EmperorIngStage3StructA.from_stream(data, game, property_size)


def _decode_light_swarm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> BasicSwarmProperties:
    return BasicSwarmProperties.from_stream(data, game, property_size)


def _decode_light_swarm_death_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_unknown_struct26(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct26:
    return UnknownStruct26.from_stream(data, game, property_size)


def _decode_jump_attack_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_emperor_ing_stage3_struct_b_0xe843417f(
    data: typing.BinaryIO, game: Game, property_size: int
) -> EmperorIngStage3StructB:
    return EmperorIngStage3StructB.from_stream(data, game, property_size)


def _decode_emperor_ing_stage3_struct_b_0xd13bec3f(
    data: typing.BinaryIO, game: Game, property_size: int
) -> EmperorIngStage3StructB:
    return EmperorIngStage3StructB.from_stream(data, game, property_size)


def _decode_emperor_ing_stage3_struct_b_0xc61388ff(
    data: typing.BinaryIO, game: Game, property_size: int
) -> EmperorIngStage3StructB:
    return EmperorIngStage3StructB.from_stream(data, game, property_size)


def _decode_emperor_ing_stage3_struct_b_0xa3cab6bf(
    data: typing.BinaryIO, game: Game, property_size: int
) -> EmperorIngStage3StructB:
    return EmperorIngStage3StructB.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x293A0C19: ("taunt_frequency", structs.decode_BIG_f),
    0x8A3F760C: ("yellow_health", _decode_yellow_health),
    0xCF90D15E: ("health", _decode_health),
    0x69BC5CD4: ("vulnerable_time", structs.decode_BIG_f),
    0xB110E539: ("vulnerable_damage_threshold", structs.decode_BIG_f),
    0x8D70D67A: ("red_vulnerability", _decode_red_vulnerability),
    0x89C142F7: ("light_vulnerability", _decode_light_vulnerability),
    0x8855C118: ("dark_vulnerability", _decode_dark_vulnerability),
    0xC9416034: ("melee_damage", _decode_melee_damage),
    0x1440D152: ("damage_info", _decode_damage_info),
    0xEF582BD6: ("jump_slide_damage", _decode_jump_slide_damage),
    0x4738C321: ("ground_pound_damage", _decode_ground_pound_damage),
    0x98E311C1: ("emperor_ing_stage3_struct_a_0x98e311c1", _decode_emperor_ing_stage3_struct_a_0x98e311c1),
    0x93DAE216: ("emperor_ing_stage3_struct_a_0x93dae216", _decode_emperor_ing_stage3_struct_a_0x93dae216),
    0x4F82B9E5: ("light_swarm_effect", structs.decode_BIG_L),
    0x043E9C2E: ("light_swarm_properties", _decode_light_swarm_properties),
    0x91001508: ("light_swarm_death_sound", _decode_light_swarm_death_sound),
    0x03552953: ("audio_playback_parms", _decode_audio_playback_parms),
    0xAF7E3033: ("unknown_struct26", _decode_unknown_struct26),
    0xAB4ED456: ("jump_attack_shock_wave_info", _decode_jump_attack_shock_wave_info),
    0x985F72FD: ("sound", structs.decode_BIG_l),
    0xE843417F: ("emperor_ing_stage3_struct_b_0xe843417f", _decode_emperor_ing_stage3_struct_b_0xe843417f),
    0xD13BEC3F: ("emperor_ing_stage3_struct_b_0xd13bec3f", _decode_emperor_ing_stage3_struct_b_0xd13bec3f),
    0xC61388FF: ("emperor_ing_stage3_struct_b_0xc61388ff", _decode_emperor_ing_stage3_struct_b_0xc61388ff),
    0xA3CAB6BF: ("emperor_ing_stage3_struct_b_0xa3cab6bf", _decode_emperor_ing_stage3_struct_b_0xa3cab6bf),
}
