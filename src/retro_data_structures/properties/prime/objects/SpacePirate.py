# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SpacePirateJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        aggression_check: float
        cover_check: float
        search_radius: float
        fallback_check: float
        fallback_radius: float
        hearing_radius: float
        flags: int
        unknown_8: bool
        projectile: int
        projectile_damage: json_util.JsonObject
        sound_projectile: int
        blade_damage: json_util.JsonObject
        kneel_attack_chance: float
        kneel_attack_shot: int
        kneel_attack_damage: json_util.JsonObject
        dodge_check: float
        sound_impact: int
        average_next_shot_time: float
        next_shot_time_variation: float
        sound_alert: int
        gun_track_delay: float
        first_burst_count: int
        cloak_opacity: float
        max_cloak_opacity: float
        dodge_delay_time_min: float
        dodge_delay_time_max: float
        sound_hurled: int
        sound_death: int
        unknown_19: float
        avoid_distance: float


class Flags(enum.IntFlag):
    PendingAmbush = 1
    CeilingAmbush = 2
    NonAggressive = 4
    Melee = 8
    NoShuffleCloseCheck = 16
    OnlyAttackInRange = 32
    Unknown = 64
    NoKnockbackImpulseReset = 128
    NoMeleeAttack = 512
    BreakAttack = 1024
    Seated = 4096
    ShadowPirate = 8192
    AlertBeforeCloak = 16384
    NoBreakDamage = 32768
    FloatingCorpse = 65536
    RagdollNoAiCollision = 131072
    Trooper = 262144

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class SpacePirate(BaseObjectType):
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
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unnamed_0x00000004: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000004,
                original_name="4",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    unnamed_0x00000005: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000005,
                original_name="5",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    aggression_check: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="AggressionCheck"),
        },
    )
    cover_check: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="CoverCheck"),
        },
    )
    search_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="SearchRadius"),
        },
    )
    fallback_check: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="FallbackCheck"),
        },
    )
    fallback_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="FallbackRadius"),
        },
    )
    hearing_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="HearingRadius"),
        },
    )
    flags: Flags = dataclasses.field(
        default=Flags(0),
        metadata={
            "reflection": FieldReflection[Flags](
                Flags, id=0x0000000C, original_name="Flags", from_json=Flags.from_json, to_json=Flags.to_json
            ),
        },
    )
    unknown_8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="Unknown 8"),
        },
    )
    projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000E, original_name="Projectile"),
        },
    )
    projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000F,
                original_name="ProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_projectile: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000010, original_name="Sound_Projectile"),
        },
    )
    blade_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000011,
                original_name="BladeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    kneel_attack_chance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="KneelAttackChance"),
        },
    )
    kneel_attack_shot: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000013, original_name="KneelAttackShot"),
        },
    )
    kneel_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000014,
                original_name="KneelAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    dodge_check: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="DodgeCheck"),
        },
    )
    sound_impact: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000016, original_name="Sound_Impact"),
        },
    )
    average_next_shot_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="AverageNextShotTime"),
        },
    )
    next_shot_time_variation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="NextShotTimeVariation"),
        },
    )
    sound_alert: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000019, original_name="Sound_Alert"),
        },
    )
    gun_track_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001A, original_name="GunTrackDelay"),
        },
    )
    first_burst_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001B, original_name="FirstBurstCount"),
        },
    )
    cloak_opacity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="CloakOpacity"),
        },
    )
    max_cloak_opacity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="MaxCloakOpacity"),
        },
    )
    dodge_delay_time_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="DodgeDelayTimeMin"),
        },
    )
    dodge_delay_time_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001F, original_name="DodgeDelayTimeMax"),
        },
    )
    sound_hurled: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000020, original_name="Sound_Hurled"),
        },
    )
    sound_death: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000021, original_name="Sound_Death"),
        },
    )
    unknown_19: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000022, original_name="Unknown 19"),
        },
    )
    avoid_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000023, original_name="AvoidDistance"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x24

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000004 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000005 = ActorParameters.from_stream(data, game, property_size)
        aggression_check = structs.BIG_f.unpack(data.read(4))[0]
        cover_check = structs.BIG_f.unpack(data.read(4))[0]
        search_radius = structs.BIG_f.unpack(data.read(4))[0]
        fallback_check = structs.BIG_f.unpack(data.read(4))[0]
        fallback_radius = structs.BIG_f.unpack(data.read(4))[0]
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
        flags = Flags.from_stream(data, game)
        unknown_8 = structs.BIG_bool_.unpack(data.read(1))[0]
        projectile = structs.BIG_L.unpack(data.read(4))[0]
        projectile_damage = DamageInfo.from_stream(data, game, property_size)
        sound_projectile = structs.BIG_l.unpack(data.read(4))[0]
        blade_damage = DamageInfo.from_stream(data, game, property_size)
        kneel_attack_chance = structs.BIG_f.unpack(data.read(4))[0]
        kneel_attack_shot = structs.BIG_L.unpack(data.read(4))[0]
        kneel_attack_damage = DamageInfo.from_stream(data, game, property_size)
        dodge_check = structs.BIG_f.unpack(data.read(4))[0]
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]
        average_next_shot_time = structs.BIG_f.unpack(data.read(4))[0]
        next_shot_time_variation = structs.BIG_f.unpack(data.read(4))[0]
        sound_alert = structs.BIG_l.unpack(data.read(4))[0]
        gun_track_delay = structs.BIG_f.unpack(data.read(4))[0]
        first_burst_count = structs.BIG_l.unpack(data.read(4))[0]
        cloak_opacity = structs.BIG_f.unpack(data.read(4))[0]
        max_cloak_opacity = structs.BIG_f.unpack(data.read(4))[0]
        dodge_delay_time_min = structs.BIG_f.unpack(data.read(4))[0]
        dodge_delay_time_max = structs.BIG_f.unpack(data.read(4))[0]
        sound_hurled = structs.BIG_l.unpack(data.read(4))[0]
        sound_death = structs.BIG_l.unpack(data.read(4))[0]
        unknown_19 = structs.BIG_f.unpack(data.read(4))[0]
        avoid_distance = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            aggression_check,
            cover_check,
            search_radius,
            fallback_check,
            fallback_radius,
            hearing_radius,
            flags,
            unknown_8,
            projectile,
            projectile_damage,
            sound_projectile,
            blade_damage,
            kneel_attack_chance,
            kneel_attack_shot,
            kneel_attack_damage,
            dodge_check,
            sound_impact,
            average_next_shot_time,
            next_shot_time_variation,
            sound_alert,
            gun_track_delay,
            first_burst_count,
            cloak_opacity,
            max_cloak_opacity,
            dodge_delay_time_min,
            dodge_delay_time_max,
            sound_hurled,
            sound_death,
            unknown_19,
            avoid_distance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00$")  # 36 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.aggression_check))
        data.write(structs.BIG_f.pack(self.cover_check))
        data.write(structs.BIG_f.pack(self.search_radius))
        data.write(structs.BIG_f.pack(self.fallback_check))
        data.write(structs.BIG_f.pack(self.fallback_radius))
        data.write(structs.BIG_f.pack(self.hearing_radius))
        self.flags.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown_8))
        data.write(structs.BIG_L.pack(self.projectile))
        self.projectile_damage.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.sound_projectile))
        self.blade_damage.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.kneel_attack_chance))
        data.write(structs.BIG_L.pack(self.kneel_attack_shot))
        self.kneel_attack_damage.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.dodge_check))
        data.write(structs.BIG_l.pack(self.sound_impact))
        data.write(structs.BIG_f.pack(self.average_next_shot_time))
        data.write(structs.BIG_f.pack(self.next_shot_time_variation))
        data.write(structs.BIG_l.pack(self.sound_alert))
        data.write(structs.BIG_f.pack(self.gun_track_delay))
        data.write(structs.BIG_l.pack(self.first_burst_count))
        data.write(structs.BIG_f.pack(self.cloak_opacity))
        data.write(structs.BIG_f.pack(self.max_cloak_opacity))
        data.write(structs.BIG_f.pack(self.dodge_delay_time_min))
        data.write(structs.BIG_f.pack(self.dodge_delay_time_max))
        data.write(structs.BIG_l.pack(self.sound_hurled))
        data.write(structs.BIG_l.pack(self.sound_death))
        data.write(structs.BIG_f.pack(self.unknown_19))
        data.write(structs.BIG_f.pack(self.avoid_distance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpacePirateJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            aggression_check=json_data["aggression_check"],
            cover_check=json_data["cover_check"],
            search_radius=json_data["search_radius"],
            fallback_check=json_data["fallback_check"],
            fallback_radius=json_data["fallback_radius"],
            hearing_radius=json_data["hearing_radius"],
            flags=Flags.from_json(json_data["flags"]),
            unknown_8=json_data["unknown_8"],
            projectile=json_data["projectile"],
            projectile_damage=DamageInfo.from_json(json_data["projectile_damage"]),
            sound_projectile=json_data["sound_projectile"],
            blade_damage=DamageInfo.from_json(json_data["blade_damage"]),
            kneel_attack_chance=json_data["kneel_attack_chance"],
            kneel_attack_shot=json_data["kneel_attack_shot"],
            kneel_attack_damage=DamageInfo.from_json(json_data["kneel_attack_damage"]),
            dodge_check=json_data["dodge_check"],
            sound_impact=json_data["sound_impact"],
            average_next_shot_time=json_data["average_next_shot_time"],
            next_shot_time_variation=json_data["next_shot_time_variation"],
            sound_alert=json_data["sound_alert"],
            gun_track_delay=json_data["gun_track_delay"],
            first_burst_count=json_data["first_burst_count"],
            cloak_opacity=json_data["cloak_opacity"],
            max_cloak_opacity=json_data["max_cloak_opacity"],
            dodge_delay_time_min=json_data["dodge_delay_time_min"],
            dodge_delay_time_max=json_data["dodge_delay_time_max"],
            sound_hurled=json_data["sound_hurled"],
            sound_death=json_data["sound_death"],
            unknown_19=json_data["unknown_19"],
            avoid_distance=json_data["avoid_distance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "aggression_check": self.aggression_check,
            "cover_check": self.cover_check,
            "search_radius": self.search_radius,
            "fallback_check": self.fallback_check,
            "fallback_radius": self.fallback_radius,
            "hearing_radius": self.hearing_radius,
            "flags": self.flags.to_json(),
            "unknown_8": self.unknown_8,
            "projectile": self.projectile,
            "projectile_damage": self.projectile_damage.to_json(),
            "sound_projectile": self.sound_projectile,
            "blade_damage": self.blade_damage.to_json(),
            "kneel_attack_chance": self.kneel_attack_chance,
            "kneel_attack_shot": self.kneel_attack_shot,
            "kneel_attack_damage": self.kneel_attack_damage.to_json(),
            "dodge_check": self.dodge_check,
            "sound_impact": self.sound_impact,
            "average_next_shot_time": self.average_next_shot_time,
            "next_shot_time_variation": self.next_shot_time_variation,
            "sound_alert": self.sound_alert,
            "gun_track_delay": self.gun_track_delay,
            "first_burst_count": self.first_burst_count,
            "cloak_opacity": self.cloak_opacity,
            "max_cloak_opacity": self.max_cloak_opacity,
            "dodge_delay_time_min": self.dodge_delay_time_min,
            "dodge_delay_time_max": self.dodge_delay_time_max,
            "sound_hurled": self.sound_hurled,
            "sound_death": self.sound_death,
            "unknown_19": self.unknown_19,
            "avoid_distance": self.avoid_distance,
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_sound_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile)

    def _dependencies_for_kneel_attack_shot(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.kneel_attack_shot)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sound_alert(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_alert)

    def _dependencies_for_sound_hurled(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_hurled)

    def _dependencies_for_sound_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_death)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_sound_projectile, "sound_projectile", "int"),
            (self._dependencies_for_kneel_attack_shot, "kneel_attack_shot", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sound_alert, "sound_alert", "int"),
            (self._dependencies_for_sound_hurled, "sound_hurled", "int"),
            (self._dependencies_for_sound_death, "sound_death", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SpacePirate.{field_name} ({field_type}): {e}")
