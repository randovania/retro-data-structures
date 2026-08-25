# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.archetypes.PowerBombGuardianStageProperties import (
    PowerBombGuardianStageProperties,
)
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SporbBaseJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0x3eb2de35: float
        unknown_0xe50d8dd2: float
        unknown_0x64d482d5: int
        unknown_0xc3e002ac: int
        shot_angle_variance: float
        attack_aim_offset: json_util.JsonValue
        tendril_particle_effect: int
        unknown_0x35557a83: float
        grabber_out_acceleration: float
        grabber_in_acceleration: float
        unknown_0xbfddabd4: float
        unknown_0x62bfaa35: float
        grabber_attach_time: float
        unknown_0xed82c56a: float
        unknown_0xe918f440: float
        spit_force: float
        spit_damage: float
        grab_damage: float
        unknown_0x2cfade2c: float
        unknown_0xb68e75cc: float
        unknown_0x6d31262b: float
        is_power_bomb_guardian: bool
        wpsc: int
        power_bomb_projectile_damage: json_util.JsonObject
        unknown_0x03a76d35: float
        unknown_0x6d4e0f5a: float
        unknown_0x3538d49b: float
        unknown_0xe89c7707: float
        unknown_0x738d1f51: float
        sound_0x9480c6d7: int
        unknown_0x48df4182: float
        unknown_0xe39482ad: float
        unknown_0xdd8502cc: float
        unknown_0x4ab8cf7d: float
        unknown_0xf5e28404: float
        grabber_fire_sound: int
        grabber_flight_sound: int
        grabber_hit_player_sound: int
        grabber_hit_world_sound: int
        grabber_retract_sound: int
        sound_0x64e9152d: int
        morphball_spit_sound: int
        grabber_explosion_sound: int
        ball_escape_sound: int
        needle_telegraph_sound: int
        grabber_telegraph_sound: int
        power_bomb_guardian_stage_properties_0x510dba97: json_util.JsonObject
        power_bomb_guardian_stage_properties_0x0b6c85f7: json_util.JsonObject
        power_bomb_guardian_stage_properties_0x8b9c92e8: json_util.JsonObject
        power_bomb_guardian_stage_properties_0xbfaefb37: json_util.JsonObject


@dataclasses.dataclass()
class SporbBase(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    patterned: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0xB3774750,
                original_name="Patterned",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0x3eb2de35: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3EB2DE35, original_name="Unknown"),
        },
    )
    unknown_0xe50d8dd2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE50D8DD2, original_name="Unknown"),
        },
    )
    unknown_0x64d482d5: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x64D482D5, original_name="Unknown"),
        },
    )
    unknown_0xc3e002ac: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC3E002AC, original_name="Unknown"),
        },
    )
    shot_angle_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD75F9CF2, original_name="ShotAngleVariance"),
        },
    )
    attack_aim_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x540C1F87,
                original_name="AttackAimOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    tendril_particle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x33868C8F, original_name="TendrilParticleEffect"),
        },
    )
    unknown_0x35557a83: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x35557A83, original_name="Unknown"),
        },
    )
    grabber_out_acceleration: float = dataclasses.field(
        default=-10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23BD3943, original_name="GrabberOutAcceleration"),
        },
    )
    grabber_in_acceleration: float = dataclasses.field(
        default=-100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD92F485D, original_name="GrabberInAcceleration"),
        },
    )
    unknown_0xbfddabd4: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBFDDABD4, original_name="Unknown"),
        },
    )
    unknown_0x62bfaa35: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x62BFAA35, original_name="Unknown"),
        },
    )
    grabber_attach_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x433B5E30, original_name="GrabberAttachTime"),
        },
    )
    unknown_0xed82c56a: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED82C56A, original_name="Unknown"),
        },
    )
    unknown_0xe918f440: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE918F440, original_name="Unknown"),
        },
    )
    spit_force: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2731AD74, original_name="SpitForce"),
        },
    )
    spit_damage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03FB2DD4, original_name="SpitDamage"),
        },
    )
    grab_damage: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95AD8824, original_name="GrabDamage"),
        },
    )
    unknown_0x2cfade2c: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2CFADE2C, original_name="Unknown"),
        },
    )
    unknown_0xb68e75cc: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB68E75CC, original_name="Unknown"),
        },
    )
    unknown_0x6d31262b: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D31262B, original_name="Unknown"),
        },
    )
    is_power_bomb_guardian: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB628855A, original_name="IsPowerBombGuardian"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x990745DD, original_name="WPSC"),
        },
    )
    power_bomb_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x5F3C27C6,
                original_name="PowerBombProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x03a76d35: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03A76D35, original_name="Unknown"),
        },
    )
    unknown_0x6d4e0f5a: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D4E0F5A, original_name="Unknown"),
        },
    )
    unknown_0x3538d49b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3538D49B, original_name="Unknown"),
        },
    )
    unknown_0xe89c7707: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE89C7707, original_name="Unknown"),
        },
    )
    unknown_0x738d1f51: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x738D1F51, original_name="Unknown"),
        },
    )
    sound_0x9480c6d7: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9480C6D7, original_name="Sound"),
        },
    )
    unknown_0x48df4182: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x48DF4182, original_name="Unknown"),
        },
    )
    unknown_0xe39482ad: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE39482AD, original_name="Unknown"),
        },
    )
    unknown_0xdd8502cc: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDD8502CC, original_name="Unknown"),
        },
    )
    unknown_0x4ab8cf7d: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4AB8CF7D, original_name="Unknown"),
        },
    )
    unknown_0xf5e28404: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF5E28404, original_name="Unknown"),
        },
    )
    grabber_fire_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xA87D72FC, original_name="GrabberFireSound"),
        },
    )
    grabber_flight_sound: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8661285E, original_name="GrabberFlightSound"),
        },
    )
    grabber_hit_player_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x4123323A, original_name="GrabberHitPlayerSound"),
        },
    )
    grabber_hit_world_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x4D2EC538, original_name="GrabberHitWorldSound"),
        },
    )
    grabber_retract_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xD51CA051, original_name="GrabberRetractSound"),
        },
    )
    sound_0x64e9152d: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x64E9152D, original_name="Sound"),
        },
    )
    morphball_spit_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x3ACD0ECC, original_name="MorphballSpitSound"),
        },
    )
    grabber_explosion_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xFEB67317, original_name="GrabberExplosionSound"),
        },
    )
    ball_escape_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x88A20DB0, original_name="BallEscapeSound"),
        },
    )
    needle_telegraph_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x95C1257F, original_name="NeedleTelegraphSound"),
        },
    )
    grabber_telegraph_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x2690E216, original_name="GrabberTelegraphSound"),
        },
    )
    power_bomb_guardian_stage_properties_0x510dba97: PowerBombGuardianStageProperties = dataclasses.field(
        default_factory=PowerBombGuardianStageProperties,
        metadata={
            "reflection": FieldReflection[PowerBombGuardianStageProperties](
                PowerBombGuardianStageProperties,
                id=0x510DBA97,
                original_name="PowerBombGuardianStageProperties",
                from_json=PowerBombGuardianStageProperties.from_json,
                to_json=PowerBombGuardianStageProperties.to_json,
            ),
        },
    )
    power_bomb_guardian_stage_properties_0x0b6c85f7: PowerBombGuardianStageProperties = dataclasses.field(
        default_factory=PowerBombGuardianStageProperties,
        metadata={
            "reflection": FieldReflection[PowerBombGuardianStageProperties](
                PowerBombGuardianStageProperties,
                id=0x0B6C85F7,
                original_name="PowerBombGuardianStageProperties",
                from_json=PowerBombGuardianStageProperties.from_json,
                to_json=PowerBombGuardianStageProperties.to_json,
            ),
        },
    )
    power_bomb_guardian_stage_properties_0x8b9c92e8: PowerBombGuardianStageProperties = dataclasses.field(
        default_factory=PowerBombGuardianStageProperties,
        metadata={
            "reflection": FieldReflection[PowerBombGuardianStageProperties](
                PowerBombGuardianStageProperties,
                id=0x8B9C92E8,
                original_name="PowerBombGuardianStageProperties",
                from_json=PowerBombGuardianStageProperties.from_json,
                to_json=PowerBombGuardianStageProperties.to_json,
            ),
        },
    )
    power_bomb_guardian_stage_properties_0xbfaefb37: PowerBombGuardianStageProperties = dataclasses.field(
        default_factory=PowerBombGuardianStageProperties,
        metadata={
            "reflection": FieldReflection[PowerBombGuardianStageProperties](
                PowerBombGuardianStageProperties,
                id=0xBFAEFB37,
                original_name="PowerBombGuardianStageProperties",
                from_json=PowerBombGuardianStageProperties.from_json,
                to_json=PowerBombGuardianStageProperties.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SPBB"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Sporb.rel"]

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 55:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95E7A2C2
        unknown_0x95e7a2c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76BA1C18
        unknown_0x76ba1c18 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3EB2DE35
        unknown_0x3eb2de35 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE50D8DD2
        unknown_0xe50d8dd2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64D482D5
        unknown_0x64d482d5 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3E002AC
        unknown_0xc3e002ac = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD75F9CF2
        shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x540C1F87
        attack_aim_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33868C8F
        tendril_particle_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35557A83
        unknown_0x35557a83 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23BD3943
        grabber_out_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD92F485D
        grabber_in_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFDDABD4
        unknown_0xbfddabd4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62BFAA35
        unknown_0x62bfaa35 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x433B5E30
        grabber_attach_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED82C56A
        unknown_0xed82c56a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE918F440
        unknown_0xe918f440 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2731AD74
        spit_force = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03FB2DD4
        spit_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95AD8824
        grab_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CFADE2C
        unknown_0x2cfade2c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB68E75CC
        unknown_0xb68e75cc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D31262B
        unknown_0x6d31262b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB628855A
        is_power_bomb_guardian = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x990745DD
        wpsc = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F3C27C6
        power_bomb_projectile_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 5.0, "di_knock_back_power": 2.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03A76D35
        unknown_0x03a76d35 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D4E0F5A
        unknown_0x6d4e0f5a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3538D49B
        unknown_0x3538d49b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE89C7707
        unknown_0xe89c7707 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x738D1F51
        unknown_0x738d1f51 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9480C6D7
        sound_0x9480c6d7 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48DF4182
        unknown_0x48df4182 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE39482AD
        unknown_0xe39482ad = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD8502CC
        unknown_0xdd8502cc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AB8CF7D
        unknown_0x4ab8cf7d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5E28404
        unknown_0xf5e28404 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA87D72FC
        grabber_fire_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8661285E
        grabber_flight_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4123323A
        grabber_hit_player_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D2EC538
        grabber_hit_world_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD51CA051
        grabber_retract_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64E9152D
        sound_0x64e9152d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ACD0ECC
        morphball_spit_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFEB67317
        grabber_explosion_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88A20DB0
        ball_escape_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95C1257F
        needle_telegraph_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2690E216
        grabber_telegraph_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x510DBA97
        power_bomb_guardian_stage_properties_0x510dba97 = PowerBombGuardianStageProperties.from_stream(
            data, game, property_size
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B6C85F7
        power_bomb_guardian_stage_properties_0x0b6c85f7 = PowerBombGuardianStageProperties.from_stream(
            data, game, property_size
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B9C92E8
        power_bomb_guardian_stage_properties_0x8b9c92e8 = PowerBombGuardianStageProperties.from_stream(
            data, game, property_size
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFAEFB37
        power_bomb_guardian_stage_properties_0xbfaefb37 = PowerBombGuardianStageProperties.from_stream(
            data, game, property_size
        )

        return cls(
            editor_properties,
            patterned,
            actor_information,
            unknown_0x95e7a2c2,
            unknown_0x76ba1c18,
            unknown_0x3eb2de35,
            unknown_0xe50d8dd2,
            unknown_0x64d482d5,
            unknown_0xc3e002ac,
            shot_angle_variance,
            attack_aim_offset,
            tendril_particle_effect,
            unknown_0x35557a83,
            grabber_out_acceleration,
            grabber_in_acceleration,
            unknown_0xbfddabd4,
            unknown_0x62bfaa35,
            grabber_attach_time,
            unknown_0xed82c56a,
            unknown_0xe918f440,
            spit_force,
            spit_damage,
            grab_damage,
            unknown_0x2cfade2c,
            unknown_0xb68e75cc,
            unknown_0x6d31262b,
            is_power_bomb_guardian,
            wpsc,
            power_bomb_projectile_damage,
            unknown_0x03a76d35,
            unknown_0x6d4e0f5a,
            unknown_0x3538d49b,
            unknown_0xe89c7707,
            unknown_0x738d1f51,
            sound_0x9480c6d7,
            unknown_0x48df4182,
            unknown_0xe39482ad,
            unknown_0xdd8502cc,
            unknown_0x4ab8cf7d,
            unknown_0xf5e28404,
            grabber_fire_sound,
            grabber_flight_sound,
            grabber_hit_player_sound,
            grabber_hit_world_sound,
            grabber_retract_sound,
            sound_0x64e9152d,
            morphball_spit_sound,
            grabber_explosion_sound,
            ball_escape_sound,
            needle_telegraph_sound,
            grabber_telegraph_sound,
            power_bomb_guardian_stage_properties_0x510dba97,
            power_bomb_guardian_stage_properties_0x0b6c85f7,
            power_bomb_guardian_stage_properties_0x8b9c92e8,
            power_bomb_guardian_stage_properties_0xbfaefb37,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x007")  # 55 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b">\xb2\xde5")  # 0x3eb2de35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3eb2de35))

        data.write(b"\xe5\r\x8d\xd2")  # 0xe50d8dd2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe50d8dd2))

        data.write(b"d\xd4\x82\xd5")  # 0x64d482d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x64d482d5))

        data.write(b"\xc3\xe0\x02\xac")  # 0xc3e002ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc3e002ac))

        data.write(b"\xd7_\x9c\xf2")  # 0xd75f9cf2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shot_angle_variance))

        data.write(b"T\x0c\x1f\x87")  # 0x540c1f87
        data.write(b"\x00\x0c")  # size
        self.attack_aim_offset.to_stream(data, game)

        data.write(b"3\x86\x8c\x8f")  # 0x33868c8f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.tendril_particle_effect))

        data.write(b"5Uz\x83")  # 0x35557a83
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x35557a83))

        data.write(b"#\xbd9C")  # 0x23bd3943
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grabber_out_acceleration))

        data.write(b"\xd9/H]")  # 0xd92f485d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grabber_in_acceleration))

        data.write(b"\xbf\xdd\xab\xd4")  # 0xbfddabd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbfddabd4))

        data.write(b"b\xbf\xaa5")  # 0x62bfaa35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x62bfaa35))

        data.write(b"C;^0")  # 0x433b5e30
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grabber_attach_time))

        data.write(b"\xed\x82\xc5j")  # 0xed82c56a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xed82c56a))

        data.write(b"\xe9\x18\xf4@")  # 0xe918f440
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe918f440))

        data.write(b"'1\xadt")  # 0x2731ad74
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.spit_force))

        data.write(b"\x03\xfb-\xd4")  # 0x3fb2dd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.spit_damage))

        data.write(b"\x95\xad\x88$")  # 0x95ad8824
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grab_damage))

        data.write(b",\xfa\xde,")  # 0x2cfade2c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2cfade2c))

        data.write(b"\xb6\x8eu\xcc")  # 0xb68e75cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb68e75cc))

        data.write(b"m1&+")  # 0x6d31262b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6d31262b))

        data.write(b"\xb6(\x85Z")  # 0xb628855a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_power_bomb_guardian))

        data.write(b"\x99\x07E\xdd")  # 0x990745dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.wpsc))

        data.write(b"_<'\xc6")  # 0x5f3c27c6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_bomb_projectile_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0, "di_knock_back_power": 2.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x03\xa7m5")  # 0x3a76d35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x03a76d35))

        data.write(b"mN\x0fZ")  # 0x6d4e0f5a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6d4e0f5a))

        data.write(b"58\xd4\x9b")  # 0x3538d49b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3538d49b))

        data.write(b"\xe8\x9cw\x07")  # 0xe89c7707
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe89c7707))

        data.write(b"s\x8d\x1fQ")  # 0x738d1f51
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x738d1f51))

        data.write(b"\x94\x80\xc6\xd7")  # 0x9480c6d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0x9480c6d7))

        data.write(b"H\xdfA\x82")  # 0x48df4182
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x48df4182))

        data.write(b"\xe3\x94\x82\xad")  # 0xe39482ad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe39482ad))

        data.write(b"\xdd\x85\x02\xcc")  # 0xdd8502cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdd8502cc))

        data.write(b"J\xb8\xcf}")  # 0x4ab8cf7d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4ab8cf7d))

        data.write(b"\xf5\xe2\x84\x04")  # 0xf5e28404
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf5e28404))

        data.write(b"\xa8}r\xfc")  # 0xa87d72fc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_fire_sound))

        data.write(b"\x86a(^")  # 0x8661285e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_flight_sound))

        data.write(b"A#2:")  # 0x4123323a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_hit_player_sound))

        data.write(b"M.\xc58")  # 0x4d2ec538
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_hit_world_sound))

        data.write(b"\xd5\x1c\xa0Q")  # 0xd51ca051
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_retract_sound))

        data.write(b"d\xe9\x15-")  # 0x64e9152d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0x64e9152d))

        data.write(b":\xcd\x0e\xcc")  # 0x3acd0ecc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.morphball_spit_sound))

        data.write(b"\xfe\xb6s\x17")  # 0xfeb67317
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_explosion_sound))

        data.write(b"\x88\xa2\r\xb0")  # 0x88a20db0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.ball_escape_sound))

        data.write(b"\x95\xc1%\x7f")  # 0x95c1257f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.needle_telegraph_sound))

        data.write(b"&\x90\xe2\x16")  # 0x2690e216
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grabber_telegraph_sound))

        data.write(b"Q\r\xba\x97")  # 0x510dba97
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_bomb_guardian_stage_properties_0x510dba97.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0bl\x85\xf7")  # 0xb6c85f7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_bomb_guardian_stage_properties_0x0b6c85f7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\x9c\x92\xe8")  # 0x8b9c92e8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_bomb_guardian_stage_properties_0x8b9c92e8.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbf\xae\xfb7")  # 0xbfaefb37
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.power_bomb_guardian_stage_properties_0xbfaefb37.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SporbBaseJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0x3eb2de35=json_data["unknown_0x3eb2de35"],
            unknown_0xe50d8dd2=json_data["unknown_0xe50d8dd2"],
            unknown_0x64d482d5=json_data["unknown_0x64d482d5"],
            unknown_0xc3e002ac=json_data["unknown_0xc3e002ac"],
            shot_angle_variance=json_data["shot_angle_variance"],
            attack_aim_offset=Vector.from_json(json_data["attack_aim_offset"]),
            tendril_particle_effect=json_data["tendril_particle_effect"],
            unknown_0x35557a83=json_data["unknown_0x35557a83"],
            grabber_out_acceleration=json_data["grabber_out_acceleration"],
            grabber_in_acceleration=json_data["grabber_in_acceleration"],
            unknown_0xbfddabd4=json_data["unknown_0xbfddabd4"],
            unknown_0x62bfaa35=json_data["unknown_0x62bfaa35"],
            grabber_attach_time=json_data["grabber_attach_time"],
            unknown_0xed82c56a=json_data["unknown_0xed82c56a"],
            unknown_0xe918f440=json_data["unknown_0xe918f440"],
            spit_force=json_data["spit_force"],
            spit_damage=json_data["spit_damage"],
            grab_damage=json_data["grab_damage"],
            unknown_0x2cfade2c=json_data["unknown_0x2cfade2c"],
            unknown_0xb68e75cc=json_data["unknown_0xb68e75cc"],
            unknown_0x6d31262b=json_data["unknown_0x6d31262b"],
            is_power_bomb_guardian=json_data["is_power_bomb_guardian"],
            wpsc=json_data["wpsc"],
            power_bomb_projectile_damage=DamageInfo.from_json(json_data["power_bomb_projectile_damage"]),
            unknown_0x03a76d35=json_data["unknown_0x03a76d35"],
            unknown_0x6d4e0f5a=json_data["unknown_0x6d4e0f5a"],
            unknown_0x3538d49b=json_data["unknown_0x3538d49b"],
            unknown_0xe89c7707=json_data["unknown_0xe89c7707"],
            unknown_0x738d1f51=json_data["unknown_0x738d1f51"],
            sound_0x9480c6d7=json_data["sound_0x9480c6d7"],
            unknown_0x48df4182=json_data["unknown_0x48df4182"],
            unknown_0xe39482ad=json_data["unknown_0xe39482ad"],
            unknown_0xdd8502cc=json_data["unknown_0xdd8502cc"],
            unknown_0x4ab8cf7d=json_data["unknown_0x4ab8cf7d"],
            unknown_0xf5e28404=json_data["unknown_0xf5e28404"],
            grabber_fire_sound=json_data["grabber_fire_sound"],
            grabber_flight_sound=json_data["grabber_flight_sound"],
            grabber_hit_player_sound=json_data["grabber_hit_player_sound"],
            grabber_hit_world_sound=json_data["grabber_hit_world_sound"],
            grabber_retract_sound=json_data["grabber_retract_sound"],
            sound_0x64e9152d=json_data["sound_0x64e9152d"],
            morphball_spit_sound=json_data["morphball_spit_sound"],
            grabber_explosion_sound=json_data["grabber_explosion_sound"],
            ball_escape_sound=json_data["ball_escape_sound"],
            needle_telegraph_sound=json_data["needle_telegraph_sound"],
            grabber_telegraph_sound=json_data["grabber_telegraph_sound"],
            power_bomb_guardian_stage_properties_0x510dba97=PowerBombGuardianStageProperties.from_json(
                json_data["power_bomb_guardian_stage_properties_0x510dba97"]
            ),
            power_bomb_guardian_stage_properties_0x0b6c85f7=PowerBombGuardianStageProperties.from_json(
                json_data["power_bomb_guardian_stage_properties_0x0b6c85f7"]
            ),
            power_bomb_guardian_stage_properties_0x8b9c92e8=PowerBombGuardianStageProperties.from_json(
                json_data["power_bomb_guardian_stage_properties_0x8b9c92e8"]
            ),
            power_bomb_guardian_stage_properties_0xbfaefb37=PowerBombGuardianStageProperties.from_json(
                json_data["power_bomb_guardian_stage_properties_0xbfaefb37"]
            ),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0x3eb2de35": self.unknown_0x3eb2de35,
            "unknown_0xe50d8dd2": self.unknown_0xe50d8dd2,
            "unknown_0x64d482d5": self.unknown_0x64d482d5,
            "unknown_0xc3e002ac": self.unknown_0xc3e002ac,
            "shot_angle_variance": self.shot_angle_variance,
            "attack_aim_offset": self.attack_aim_offset.to_json(),
            "tendril_particle_effect": self.tendril_particle_effect,
            "unknown_0x35557a83": self.unknown_0x35557a83,
            "grabber_out_acceleration": self.grabber_out_acceleration,
            "grabber_in_acceleration": self.grabber_in_acceleration,
            "unknown_0xbfddabd4": self.unknown_0xbfddabd4,
            "unknown_0x62bfaa35": self.unknown_0x62bfaa35,
            "grabber_attach_time": self.grabber_attach_time,
            "unknown_0xed82c56a": self.unknown_0xed82c56a,
            "unknown_0xe918f440": self.unknown_0xe918f440,
            "spit_force": self.spit_force,
            "spit_damage": self.spit_damage,
            "grab_damage": self.grab_damage,
            "unknown_0x2cfade2c": self.unknown_0x2cfade2c,
            "unknown_0xb68e75cc": self.unknown_0xb68e75cc,
            "unknown_0x6d31262b": self.unknown_0x6d31262b,
            "is_power_bomb_guardian": self.is_power_bomb_guardian,
            "wpsc": self.wpsc,
            "power_bomb_projectile_damage": self.power_bomb_projectile_damage.to_json(),
            "unknown_0x03a76d35": self.unknown_0x03a76d35,
            "unknown_0x6d4e0f5a": self.unknown_0x6d4e0f5a,
            "unknown_0x3538d49b": self.unknown_0x3538d49b,
            "unknown_0xe89c7707": self.unknown_0xe89c7707,
            "unknown_0x738d1f51": self.unknown_0x738d1f51,
            "sound_0x9480c6d7": self.sound_0x9480c6d7,
            "unknown_0x48df4182": self.unknown_0x48df4182,
            "unknown_0xe39482ad": self.unknown_0xe39482ad,
            "unknown_0xdd8502cc": self.unknown_0xdd8502cc,
            "unknown_0x4ab8cf7d": self.unknown_0x4ab8cf7d,
            "unknown_0xf5e28404": self.unknown_0xf5e28404,
            "grabber_fire_sound": self.grabber_fire_sound,
            "grabber_flight_sound": self.grabber_flight_sound,
            "grabber_hit_player_sound": self.grabber_hit_player_sound,
            "grabber_hit_world_sound": self.grabber_hit_world_sound,
            "grabber_retract_sound": self.grabber_retract_sound,
            "sound_0x64e9152d": self.sound_0x64e9152d,
            "morphball_spit_sound": self.morphball_spit_sound,
            "grabber_explosion_sound": self.grabber_explosion_sound,
            "ball_escape_sound": self.ball_escape_sound,
            "needle_telegraph_sound": self.needle_telegraph_sound,
            "grabber_telegraph_sound": self.grabber_telegraph_sound,
            "power_bomb_guardian_stage_properties_0x510dba97": self.power_bomb_guardian_stage_properties_0x510dba97.to_json(),
            "power_bomb_guardian_stage_properties_0x0b6c85f7": self.power_bomb_guardian_stage_properties_0x0b6c85f7.to_json(),
            "power_bomb_guardian_stage_properties_0x8b9c92e8": self.power_bomb_guardian_stage_properties_0x8b9c92e8.to_json(),
            "power_bomb_guardian_stage_properties_0xbfaefb37": self.power_bomb_guardian_stage_properties_0xbfaefb37.to_json(),
        }

    def _dependencies_for_tendril_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tendril_particle_effect)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_grabber_fire_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_fire_sound)

    def _dependencies_for_grabber_hit_player_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_hit_player_sound)

    def _dependencies_for_grabber_hit_world_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_hit_world_sound)

    def _dependencies_for_grabber_retract_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_retract_sound)

    def _dependencies_for_sound_0x64e9152d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0x64e9152d)

    def _dependencies_for_morphball_spit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.morphball_spit_sound)

    def _dependencies_for_grabber_explosion_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_explosion_sound)

    def _dependencies_for_ball_escape_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.ball_escape_sound)

    def _dependencies_for_needle_telegraph_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.needle_telegraph_sound)

    def _dependencies_for_grabber_telegraph_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_telegraph_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_tendril_particle_effect, "tendril_particle_effect", "AssetId"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_grabber_fire_sound, "grabber_fire_sound", "int"),
            (self._dependencies_for_grabber_hit_player_sound, "grabber_hit_player_sound", "int"),
            (self._dependencies_for_grabber_hit_world_sound, "grabber_hit_world_sound", "int"),
            (self._dependencies_for_grabber_retract_sound, "grabber_retract_sound", "int"),
            (self._dependencies_for_sound_0x64e9152d, "sound_0x64e9152d", "int"),
            (self._dependencies_for_morphball_spit_sound, "morphball_spit_sound", "int"),
            (self._dependencies_for_grabber_explosion_sound, "grabber_explosion_sound", "int"),
            (self._dependencies_for_ball_escape_sound, "ball_escape_sound", "int"),
            (self._dependencies_for_needle_telegraph_sound, "needle_telegraph_sound", "int"),
            (self._dependencies_for_grabber_telegraph_sound, "grabber_telegraph_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SporbBase.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_attack_aim_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_power_bomb_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0, "di_knock_back_power": 2.0}
    )


def _decode_power_bomb_guardian_stage_properties_0x510dba97(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


def _decode_power_bomb_guardian_stage_properties_0x0b6c85f7(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


def _decode_power_bomb_guardian_stage_properties_0x8b9c92e8(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


def _decode_power_bomb_guardian_stage_properties_0xbfaefb37(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0x3EB2DE35: ("unknown_0x3eb2de35", structs.decode_BIG_f),
    0xE50D8DD2: ("unknown_0xe50d8dd2", structs.decode_BIG_f),
    0x64D482D5: ("unknown_0x64d482d5", structs.decode_BIG_l),
    0xC3E002AC: ("unknown_0xc3e002ac", structs.decode_BIG_l),
    0xD75F9CF2: ("shot_angle_variance", structs.decode_BIG_f),
    0x540C1F87: ("attack_aim_offset", _decode_attack_aim_offset),
    0x33868C8F: ("tendril_particle_effect", structs.decode_BIG_L),
    0x35557A83: ("unknown_0x35557a83", structs.decode_BIG_f),
    0x23BD3943: ("grabber_out_acceleration", structs.decode_BIG_f),
    0xD92F485D: ("grabber_in_acceleration", structs.decode_BIG_f),
    0xBFDDABD4: ("unknown_0xbfddabd4", structs.decode_BIG_f),
    0x62BFAA35: ("unknown_0x62bfaa35", structs.decode_BIG_f),
    0x433B5E30: ("grabber_attach_time", structs.decode_BIG_f),
    0xED82C56A: ("unknown_0xed82c56a", structs.decode_BIG_f),
    0xE918F440: ("unknown_0xe918f440", structs.decode_BIG_f),
    0x2731AD74: ("spit_force", structs.decode_BIG_f),
    0x03FB2DD4: ("spit_damage", structs.decode_BIG_f),
    0x95AD8824: ("grab_damage", structs.decode_BIG_f),
    0x2CFADE2C: ("unknown_0x2cfade2c", structs.decode_BIG_f),
    0xB68E75CC: ("unknown_0xb68e75cc", structs.decode_BIG_f),
    0x6D31262B: ("unknown_0x6d31262b", structs.decode_BIG_f),
    0xB628855A: ("is_power_bomb_guardian", structs.decode_BIG_bool_),
    0x990745DD: ("wpsc", structs.decode_BIG_L),
    0x5F3C27C6: ("power_bomb_projectile_damage", _decode_power_bomb_projectile_damage),
    0x03A76D35: ("unknown_0x03a76d35", structs.decode_BIG_f),
    0x6D4E0F5A: ("unknown_0x6d4e0f5a", structs.decode_BIG_f),
    0x3538D49B: ("unknown_0x3538d49b", structs.decode_BIG_f),
    0xE89C7707: ("unknown_0xe89c7707", structs.decode_BIG_f),
    0x738D1F51: ("unknown_0x738d1f51", structs.decode_BIG_f),
    0x9480C6D7: ("sound_0x9480c6d7", structs.decode_BIG_l),
    0x48DF4182: ("unknown_0x48df4182", structs.decode_BIG_f),
    0xE39482AD: ("unknown_0xe39482ad", structs.decode_BIG_f),
    0xDD8502CC: ("unknown_0xdd8502cc", structs.decode_BIG_f),
    0x4AB8CF7D: ("unknown_0x4ab8cf7d", structs.decode_BIG_f),
    0xF5E28404: ("unknown_0xf5e28404", structs.decode_BIG_f),
    0xA87D72FC: ("grabber_fire_sound", structs.decode_BIG_l),
    0x8661285E: ("grabber_flight_sound", structs.decode_BIG_l),
    0x4123323A: ("grabber_hit_player_sound", structs.decode_BIG_l),
    0x4D2EC538: ("grabber_hit_world_sound", structs.decode_BIG_l),
    0xD51CA051: ("grabber_retract_sound", structs.decode_BIG_l),
    0x64E9152D: ("sound_0x64e9152d", structs.decode_BIG_l),
    0x3ACD0ECC: ("morphball_spit_sound", structs.decode_BIG_l),
    0xFEB67317: ("grabber_explosion_sound", structs.decode_BIG_l),
    0x88A20DB0: ("ball_escape_sound", structs.decode_BIG_l),
    0x95C1257F: ("needle_telegraph_sound", structs.decode_BIG_l),
    0x2690E216: ("grabber_telegraph_sound", structs.decode_BIG_l),
    0x510DBA97: (
        "power_bomb_guardian_stage_properties_0x510dba97",
        _decode_power_bomb_guardian_stage_properties_0x510dba97,
    ),
    0x0B6C85F7: (
        "power_bomb_guardian_stage_properties_0x0b6c85f7",
        _decode_power_bomb_guardian_stage_properties_0x0b6c85f7,
    ),
    0x8B9C92E8: (
        "power_bomb_guardian_stage_properties_0x8b9c92e8",
        _decode_power_bomb_guardian_stage_properties_0x8b9c92e8,
    ),
    0xBFAEFB37: (
        "power_bomb_guardian_stage_properties_0xbfaefb37",
        _decode_power_bomb_guardian_stage_properties_0xbfaefb37,
    ),
}
