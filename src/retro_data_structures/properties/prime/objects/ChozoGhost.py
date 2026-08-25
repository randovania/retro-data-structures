# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.BehaveChance import BehaveChance
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

    class ChozoGhostJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        hearing_radius: float
        fade_out_delay: float
        attack_delay: float
        freeze_time: float
        wpsc_1: int
        damage_info_1: json_util.JsonObject
        wpsc_2: int
        damage_info_2: json_util.JsonObject
        behave_chance_1: json_util.JsonObject
        behave_chance_2: json_util.JsonObject
        behave_chance_3: json_util.JsonObject
        sound_impact: int
        unknown_1: float
        sfx_fade_in: int
        sfx_fade_out: int
        unknown_2: int
        floor_level: float
        attack_type: int
        hurl_recover_time: float
        projectile_visor_effect: int
        sound_projectile_visor: int
        lurk_delay: float
        space_warp_time: float
        near_chance: int
        mid_chance: int


@dataclasses.dataclass()
class ChozoGhost(BaseObjectType):
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
    hearing_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Hearing Radius"),
        },
    )
    fade_out_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Fade-Out Delay"),
        },
    )
    attack_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Attack Delay"),
        },
    )
    freeze_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Freeze Time"),
        },
    )
    wpsc_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="WPSC 1"),
        },
    )
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000B,
                original_name="DamageInfo 1",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    wpsc_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="WPSC 2"),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000D,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    behave_chance_1: BehaveChance = dataclasses.field(
        default_factory=BehaveChance,
        metadata={
            "reflection": FieldReflection[BehaveChance](
                BehaveChance,
                id=0x0000000E,
                original_name="BehaveChance 1",
                from_json=BehaveChance.from_json,
                to_json=BehaveChance.to_json,
            ),
        },
    )
    behave_chance_2: BehaveChance = dataclasses.field(
        default_factory=BehaveChance,
        metadata={
            "reflection": FieldReflection[BehaveChance](
                BehaveChance,
                id=0x0000000F,
                original_name="BehaveChance 2",
                from_json=BehaveChance.from_json,
                to_json=BehaveChance.to_json,
            ),
        },
    )
    behave_chance_3: BehaveChance = dataclasses.field(
        default_factory=BehaveChance,
        metadata={
            "reflection": FieldReflection[BehaveChance](
                BehaveChance,
                id=0x00000010,
                original_name="BehaveChance 3",
                from_json=BehaveChance.from_json,
                to_json=BehaveChance.to_json,
            ),
        },
    )
    sound_impact: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000011, original_name="SoundImpact"),
        },
    )
    unknown_1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="Unknown 1"),
        },
    )
    sfx_fade_in: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="SFXFadeIn"),
        },
    )
    sfx_fade_out: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000014, original_name="SFXFadeOut"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000015, original_name="Unknown 2"),
        },
    )
    floor_level: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000016, original_name="FloorLevel"),
        },
    )
    attack_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000017, original_name="AttackType"),
        },
    )
    hurl_recover_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="HurlRecoverTime"),
        },
    )
    projectile_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000019, original_name="ProjectileVisorEffect"),
        },
    )
    sound_projectile_visor: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000001A, original_name="SoundProjectileVisor"),
        },
    )
    lurk_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="LurkDelay"),
        },
    )
    space_warp_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="SpaceWarpTime"),
        },
    )
    near_chance: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001D, original_name="NearChance"),
        },
    )
    mid_chance: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001E, original_name="MidChance"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x28

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
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
        fade_out_delay = structs.BIG_f.unpack(data.read(4))[0]
        attack_delay = structs.BIG_f.unpack(data.read(4))[0]
        freeze_time = structs.BIG_f.unpack(data.read(4))[0]
        wpsc_1 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        wpsc_2 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        behave_chance_1 = BehaveChance.from_stream(data, game, property_size)
        behave_chance_2 = BehaveChance.from_stream(data, game, property_size)
        behave_chance_3 = BehaveChance.from_stream(data, game, property_size)
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]
        unknown_1 = structs.BIG_f.unpack(data.read(4))[0]
        sfx_fade_in = structs.BIG_l.unpack(data.read(4))[0]
        sfx_fade_out = structs.BIG_l.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        floor_level = structs.BIG_f.unpack(data.read(4))[0]
        attack_type = structs.BIG_l.unpack(data.read(4))[0]
        hurl_recover_time = structs.BIG_f.unpack(data.read(4))[0]
        projectile_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
        sound_projectile_visor = structs.BIG_l.unpack(data.read(4))[0]
        lurk_delay = structs.BIG_f.unpack(data.read(4))[0]
        space_warp_time = structs.BIG_f.unpack(data.read(4))[0]
        near_chance = structs.BIG_l.unpack(data.read(4))[0]
        mid_chance = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            hearing_radius,
            fade_out_delay,
            attack_delay,
            freeze_time,
            wpsc_1,
            damage_info_1,
            wpsc_2,
            damage_info_2,
            behave_chance_1,
            behave_chance_2,
            behave_chance_3,
            sound_impact,
            unknown_1,
            sfx_fade_in,
            sfx_fade_out,
            unknown_2,
            floor_level,
            attack_type,
            hurl_recover_time,
            projectile_visor_effect,
            sound_projectile_visor,
            lurk_delay,
            space_warp_time,
            near_chance,
            mid_chance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x1f")  # 31 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.hearing_radius))
        data.write(structs.BIG_f.pack(self.fade_out_delay))
        data.write(structs.BIG_f.pack(self.attack_delay))
        data.write(structs.BIG_f.pack(self.freeze_time))
        data.write(structs.BIG_L.pack(self.wpsc_1))
        self.damage_info_1.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc_2))
        self.damage_info_2.to_stream(data, game)
        self.behave_chance_1.to_stream(data, game)
        self.behave_chance_2.to_stream(data, game)
        self.behave_chance_3.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.sound_impact))
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_l.pack(self.sfx_fade_in))
        data.write(structs.BIG_l.pack(self.sfx_fade_out))
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.floor_level))
        data.write(structs.BIG_l.pack(self.attack_type))
        data.write(structs.BIG_f.pack(self.hurl_recover_time))
        data.write(structs.BIG_L.pack(self.projectile_visor_effect))
        data.write(structs.BIG_l.pack(self.sound_projectile_visor))
        data.write(structs.BIG_f.pack(self.lurk_delay))
        data.write(structs.BIG_f.pack(self.space_warp_time))
        data.write(structs.BIG_l.pack(self.near_chance))
        data.write(structs.BIG_l.pack(self.mid_chance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ChozoGhostJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            hearing_radius=json_data["hearing_radius"],
            fade_out_delay=json_data["fade_out_delay"],
            attack_delay=json_data["attack_delay"],
            freeze_time=json_data["freeze_time"],
            wpsc_1=json_data["wpsc_1"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            wpsc_2=json_data["wpsc_2"],
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
            behave_chance_1=BehaveChance.from_json(json_data["behave_chance_1"]),
            behave_chance_2=BehaveChance.from_json(json_data["behave_chance_2"]),
            behave_chance_3=BehaveChance.from_json(json_data["behave_chance_3"]),
            sound_impact=json_data["sound_impact"],
            unknown_1=json_data["unknown_1"],
            sfx_fade_in=json_data["sfx_fade_in"],
            sfx_fade_out=json_data["sfx_fade_out"],
            unknown_2=json_data["unknown_2"],
            floor_level=json_data["floor_level"],
            attack_type=json_data["attack_type"],
            hurl_recover_time=json_data["hurl_recover_time"],
            projectile_visor_effect=json_data["projectile_visor_effect"],
            sound_projectile_visor=json_data["sound_projectile_visor"],
            lurk_delay=json_data["lurk_delay"],
            space_warp_time=json_data["space_warp_time"],
            near_chance=json_data["near_chance"],
            mid_chance=json_data["mid_chance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "hearing_radius": self.hearing_radius,
            "fade_out_delay": self.fade_out_delay,
            "attack_delay": self.attack_delay,
            "freeze_time": self.freeze_time,
            "wpsc_1": self.wpsc_1,
            "damage_info_1": self.damage_info_1.to_json(),
            "wpsc_2": self.wpsc_2,
            "damage_info_2": self.damage_info_2.to_json(),
            "behave_chance_1": self.behave_chance_1.to_json(),
            "behave_chance_2": self.behave_chance_2.to_json(),
            "behave_chance_3": self.behave_chance_3.to_json(),
            "sound_impact": self.sound_impact,
            "unknown_1": self.unknown_1,
            "sfx_fade_in": self.sfx_fade_in,
            "sfx_fade_out": self.sfx_fade_out,
            "unknown_2": self.unknown_2,
            "floor_level": self.floor_level,
            "attack_type": self.attack_type,
            "hurl_recover_time": self.hurl_recover_time,
            "projectile_visor_effect": self.projectile_visor_effect,
            "sound_projectile_visor": self.sound_projectile_visor,
            "lurk_delay": self.lurk_delay,
            "space_warp_time": self.space_warp_time,
            "near_chance": self.near_chance,
            "mid_chance": self.mid_chance,
        }

    def _dependencies_for_wpsc_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_1)

    def _dependencies_for_wpsc_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_2)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sfx_fade_in(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_fade_in)

    def _dependencies_for_sfx_fade_out(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sfx_fade_out)

    def _dependencies_for_projectile_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_visor_effect)

    def _dependencies_for_sound_projectile_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile_visor)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_wpsc_1, "wpsc_1", "AssetId"),
            (self._dependencies_for_wpsc_2, "wpsc_2", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sfx_fade_in, "sfx_fade_in", "int"),
            (self._dependencies_for_sfx_fade_out, "sfx_fade_out", "int"),
            (self._dependencies_for_projectile_visor_effect, "projectile_visor_effect", "AssetId"),
            (self._dependencies_for_sound_projectile_visor, "sound_projectile_visor", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ChozoGhost.{field_name} ({field_type}): {e}")
