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
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class FlaahgraJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        actor_parameters_1: json_util.JsonObject
        unknown_1: float
        unknown_2: float
        unknown_3: float
        faint_duration: float
        unnamed_0x0000000a: json_util.JsonObject
        wpsc_1: int
        damage_info_1: json_util.JsonObject
        wpsc_2: int
        damage_info_2: json_util.JsonObject
        plants_particle_gen_desc_id: int
        damage_info_3: json_util.JsonObject
        actor_parameters_2: json_util.JsonObject
        unknown_5: float
        unknown_6: float
        unknown_7: float
        animation_parameters: json_util.JsonObject
        dgrp: int


@dataclasses.dataclass()
class Flaahgra(BaseObjectType):
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
    actor_parameters_1: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000005,
                original_name="ActorParameters 1",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Unknown 1"),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Unknown 2"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown 3"),
        },
    )
    faint_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="FaintDuration"),
        },
    )
    unnamed_0x0000000a: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000A,
                original_name="10",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    wpsc_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="WPSC 1"),
        },
    )
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000C,
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
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="WPSC 2"),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000E,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    plants_particle_gen_desc_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000F, original_name="PlantsParticleGenDescID"),
        },
    )
    damage_info_3: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000010,
                original_name="DamageInfo 3",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    actor_parameters_2: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000011,
                original_name="ActorParameters 2",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="Unknown 6"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Unknown 7"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000015,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    dgrp: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["DGRP"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000016, original_name="DGRP"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x4D

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
        actor_parameters_1 = ActorParameters.from_stream(data, game, property_size)
        unknown_1 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        faint_duration = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x0000000a = DamageVulnerability.from_stream(data, game, property_size)
        wpsc_1 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        wpsc_2 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        plants_particle_gen_desc_id = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_3 = DamageInfo.from_stream(data, game, property_size)
        actor_parameters_2 = ActorParameters.from_stream(data, game, property_size)
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        dgrp = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            actor_parameters_1,
            unknown_1,
            unknown_2,
            unknown_3,
            faint_duration,
            unnamed_0x0000000a,
            wpsc_1,
            damage_info_1,
            wpsc_2,
            damage_info_2,
            plants_particle_gen_desc_id,
            damage_info_3,
            actor_parameters_2,
            unknown_5,
            unknown_6,
            unknown_7,
            animation_parameters,
            dgrp,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x17")  # 23 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.actor_parameters_1.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_f.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.faint_duration))
        self.unnamed_0x0000000a.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc_1))
        self.damage_info_1.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc_2))
        self.damage_info_2.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.plants_particle_gen_desc_id))
        self.damage_info_3.to_stream(data, game)
        self.actor_parameters_2.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_f.pack(self.unknown_7))
        self.animation_parameters.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.dgrp))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlaahgraJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            actor_parameters_1=ActorParameters.from_json(json_data["actor_parameters_1"]),
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            faint_duration=json_data["faint_duration"],
            unnamed_0x0000000a=DamageVulnerability.from_json(json_data["unnamed_0x0000000a"]),
            wpsc_1=json_data["wpsc_1"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            wpsc_2=json_data["wpsc_2"],
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
            plants_particle_gen_desc_id=json_data["plants_particle_gen_desc_id"],
            damage_info_3=DamageInfo.from_json(json_data["damage_info_3"]),
            actor_parameters_2=ActorParameters.from_json(json_data["actor_parameters_2"]),
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            dgrp=json_data["dgrp"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "actor_parameters_1": self.actor_parameters_1.to_json(),
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "faint_duration": self.faint_duration,
            "unnamed_0x0000000a": self.unnamed_0x0000000a.to_json(),
            "wpsc_1": self.wpsc_1,
            "damage_info_1": self.damage_info_1.to_json(),
            "wpsc_2": self.wpsc_2,
            "damage_info_2": self.damage_info_2.to_json(),
            "plants_particle_gen_desc_id": self.plants_particle_gen_desc_id,
            "damage_info_3": self.damage_info_3.to_json(),
            "actor_parameters_2": self.actor_parameters_2.to_json(),
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "animation_parameters": self.animation_parameters.to_json(),
            "dgrp": self.dgrp,
        }

    def _dependencies_for_wpsc_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_1)

    def _dependencies_for_wpsc_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_2)

    def _dependencies_for_plants_particle_gen_desc_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.plants_particle_gen_desc_id)

    def _dependencies_for_dgrp(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dgrp)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.actor_parameters_1.dependencies_for, "actor_parameters_1", "ActorParameters"),
            (self._dependencies_for_wpsc_1, "wpsc_1", "AssetId"),
            (self._dependencies_for_wpsc_2, "wpsc_2", "AssetId"),
            (self._dependencies_for_plants_particle_gen_desc_id, "plants_particle_gen_desc_id", "AssetId"),
            (self.actor_parameters_2.dependencies_for, "actor_parameters_2", "ActorParameters"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self._dependencies_for_dgrp, "dgrp", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Flaahgra.{field_name} ({field_type}): {e}")
