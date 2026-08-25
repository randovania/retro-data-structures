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
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class IceSheegothJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        unknown_1: float
        unknown_2: float
        unknown_3: json_util.JsonValue
        unknown_4: float
        damage_vulnerability_1: json_util.JsonObject
        damage_vulnerability_2: json_util.JsonObject
        damage_vulnerability_3: json_util.JsonObject
        wpsc_1: int
        damage_info_1: json_util.JsonObject
        unknown_5: float
        unknown_6: float
        wpsc_2: int
        fire_breath_res_id: int
        fire_breath_damage: json_util.JsonObject
        particle_2: int
        particle_3: int
        particle_4: int
        particle_5: int
        elsc: int
        unknown_7: float
        unknown_8: float
        damage_info_3: json_util.JsonObject
        sound_id_1: int
        unknown_9: float
        unknown_10: float
        max_interest_time: float
        texture: int
        sound_id_2: int
        particle_6: int
        unknown_11: bool
        unknown_12: bool


@dataclasses.dataclass()
class IceSheegoth(BaseObjectType):
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
    unknown_3: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000008, original_name="Unknown 3", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 4"),
        },
    )
    damage_vulnerability_1: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000A,
                original_name="DamageVulnerability 1",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    damage_vulnerability_2: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000B,
                original_name="DamageVulnerability 2",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    damage_vulnerability_3: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000C,
                original_name="DamageVulnerability 3",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    wpsc_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="WPSC 1"),
        },
    )
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000E,
                original_name="DamageInfo 1",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="Unknown 6"),
        },
    )
    wpsc_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000011, original_name="WPSC 2"),
        },
    )
    fire_breath_res_id: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000012, original_name="FireBreathResID"),
        },
    )
    fire_breath_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000013,
                original_name="FireBreathDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000014, original_name="Particle 2"),
        },
    )
    particle_3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000015, original_name="Particle 3"),
        },
    )
    particle_4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000016, original_name="Particle 4"),
        },
    )
    particle_5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000017, original_name="Particle 5"),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000018, original_name="ELSC"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000019, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001A, original_name="Unknown 8"),
        },
    )
    damage_info_3: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000001B,
                original_name="DamageInfo 3",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_id_1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000001C, original_name="Sound ID 1"),
        },
    )
    unknown_9: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="Unknown 9"),
        },
    )
    unknown_10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="Unknown 10"),
        },
    )
    max_interest_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001F, original_name="MaxInterestTime"),
        },
    )
    texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000020, original_name="Texture"),
        },
    )
    sound_id_2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000021, original_name="Sound ID 2"),
        },
    )
    particle_6: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000022, original_name="Particle 6"),
        },
    )
    unknown_11: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000023, original_name="Unknown 11"),
        },
    )
    unknown_12: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000024, original_name="Unknown 12"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x4B

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
        unknown_1 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_3 = Vector.from_stream(data, game, property_size)
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        damage_vulnerability_1 = DamageVulnerability.from_stream(data, game, property_size)
        damage_vulnerability_2 = DamageVulnerability.from_stream(data, game, property_size)
        damage_vulnerability_3 = DamageVulnerability.from_stream(data, game, property_size)
        wpsc_1 = structs.BIG_L.unpack(data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        wpsc_2 = structs.BIG_L.unpack(data.read(4))[0]
        fire_breath_res_id = structs.BIG_L.unpack(data.read(4))[0]
        fire_breath_damage = DamageInfo.from_stream(data, game, property_size)
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        particle_3 = structs.BIG_L.unpack(data.read(4))[0]
        particle_4 = structs.BIG_L.unpack(data.read(4))[0]
        particle_5 = structs.BIG_L.unpack(data.read(4))[0]
        elsc = structs.BIG_L.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        damage_info_3 = DamageInfo.from_stream(data, game, property_size)
        sound_id_1 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_f.unpack(data.read(4))[0]
        max_interest_time = structs.BIG_f.unpack(data.read(4))[0]
        texture = structs.BIG_L.unpack(data.read(4))[0]
        sound_id_2 = structs.BIG_l.unpack(data.read(4))[0]
        particle_6 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_12 = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            unknown_1,
            unknown_2,
            unknown_3,
            unknown_4,
            damage_vulnerability_1,
            damage_vulnerability_2,
            damage_vulnerability_3,
            wpsc_1,
            damage_info_1,
            unknown_5,
            unknown_6,
            wpsc_2,
            fire_breath_res_id,
            fire_breath_damage,
            particle_2,
            particle_3,
            particle_4,
            particle_5,
            elsc,
            unknown_7,
            unknown_8,
            damage_info_3,
            sound_id_1,
            unknown_9,
            unknown_10,
            max_interest_time,
            texture,
            sound_id_2,
            particle_6,
            unknown_11,
            unknown_12,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00%")  # 37 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_f.pack(self.unknown_2))
        self.unknown_3.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_4))
        self.damage_vulnerability_1.to_stream(data, game)
        self.damage_vulnerability_2.to_stream(data, game)
        self.damage_vulnerability_3.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.wpsc_1))
        self.damage_info_1.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_L.pack(self.wpsc_2))
        data.write(structs.BIG_L.pack(self.fire_breath_res_id))
        self.fire_breath_damage.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_L.pack(self.particle_3))
        data.write(structs.BIG_L.pack(self.particle_4))
        data.write(structs.BIG_L.pack(self.particle_5))
        data.write(structs.BIG_L.pack(self.elsc))
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        self.damage_info_3.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.sound_id_1))
        data.write(structs.BIG_f.pack(self.unknown_9))
        data.write(structs.BIG_f.pack(self.unknown_10))
        data.write(structs.BIG_f.pack(self.max_interest_time))
        data.write(structs.BIG_L.pack(self.texture))
        data.write(structs.BIG_l.pack(self.sound_id_2))
        data.write(structs.BIG_L.pack(self.particle_6))
        data.write(structs.BIG_bool_.pack(self.unknown_11))
        data.write(structs.BIG_bool_.pack(self.unknown_12))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("IceSheegothJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=Vector.from_json(json_data["unknown_3"]),
            unknown_4=json_data["unknown_4"],
            damage_vulnerability_1=DamageVulnerability.from_json(json_data["damage_vulnerability_1"]),
            damage_vulnerability_2=DamageVulnerability.from_json(json_data["damage_vulnerability_2"]),
            damage_vulnerability_3=DamageVulnerability.from_json(json_data["damage_vulnerability_3"]),
            wpsc_1=json_data["wpsc_1"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            wpsc_2=json_data["wpsc_2"],
            fire_breath_res_id=json_data["fire_breath_res_id"],
            fire_breath_damage=DamageInfo.from_json(json_data["fire_breath_damage"]),
            particle_2=json_data["particle_2"],
            particle_3=json_data["particle_3"],
            particle_4=json_data["particle_4"],
            particle_5=json_data["particle_5"],
            elsc=json_data["elsc"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            damage_info_3=DamageInfo.from_json(json_data["damage_info_3"]),
            sound_id_1=json_data["sound_id_1"],
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            max_interest_time=json_data["max_interest_time"],
            texture=json_data["texture"],
            sound_id_2=json_data["sound_id_2"],
            particle_6=json_data["particle_6"],
            unknown_11=json_data["unknown_11"],
            unknown_12=json_data["unknown_12"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3.to_json(),
            "unknown_4": self.unknown_4,
            "damage_vulnerability_1": self.damage_vulnerability_1.to_json(),
            "damage_vulnerability_2": self.damage_vulnerability_2.to_json(),
            "damage_vulnerability_3": self.damage_vulnerability_3.to_json(),
            "wpsc_1": self.wpsc_1,
            "damage_info_1": self.damage_info_1.to_json(),
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "wpsc_2": self.wpsc_2,
            "fire_breath_res_id": self.fire_breath_res_id,
            "fire_breath_damage": self.fire_breath_damage.to_json(),
            "particle_2": self.particle_2,
            "particle_3": self.particle_3,
            "particle_4": self.particle_4,
            "particle_5": self.particle_5,
            "elsc": self.elsc,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "damage_info_3": self.damage_info_3.to_json(),
            "sound_id_1": self.sound_id_1,
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "max_interest_time": self.max_interest_time,
            "texture": self.texture,
            "sound_id_2": self.sound_id_2,
            "particle_6": self.particle_6,
            "unknown_11": self.unknown_11,
            "unknown_12": self.unknown_12,
        }

    def _dependencies_for_wpsc_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_1)

    def _dependencies_for_wpsc_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc_2)

    def _dependencies_for_fire_breath_res_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fire_breath_res_id)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_particle_3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_3)

    def _dependencies_for_particle_4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_4)

    def _dependencies_for_particle_5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_5)

    def _dependencies_for_elsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.elsc)

    def _dependencies_for_sound_id_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_id_1)

    def _dependencies_for_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.texture)

    def _dependencies_for_sound_id_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_id_2)

    def _dependencies_for_particle_6(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_6)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_wpsc_1, "wpsc_1", "AssetId"),
            (self._dependencies_for_wpsc_2, "wpsc_2", "AssetId"),
            (self._dependencies_for_fire_breath_res_id, "fire_breath_res_id", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_particle_3, "particle_3", "AssetId"),
            (self._dependencies_for_particle_4, "particle_4", "AssetId"),
            (self._dependencies_for_particle_5, "particle_5", "AssetId"),
            (self._dependencies_for_elsc, "elsc", "AssetId"),
            (self._dependencies_for_sound_id_1, "sound_id_1", "int"),
            (self._dependencies_for_texture, "texture", "AssetId"),
            (self._dependencies_for_sound_id_2, "sound_id_2", "int"),
            (self._dependencies_for_particle_6, "particle_6", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for IceSheegoth.{field_name} ({field_type}): {e}")
