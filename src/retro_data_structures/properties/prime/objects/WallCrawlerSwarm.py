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
from retro_data_structures.properties.prime.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class WallCrawlerSwarmJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        active: bool
        unnamed_0x00000005: json_util.JsonObject
        unknown_1: int
        animation_parameters: json_util.JsonObject
        unknown_2: int
        unknown_3: int
        particle_1: int
        particle_2: int
        always_ffffffff_1: int
        always_ffffffff_2: int
        damage_info_1: json_util.JsonObject
        unknown_4: float
        damage_info_2: json_util.JsonObject
        unknown_5: float
        unknown_6: float
        unknown_7: float
        unknown_8: float
        unknown_9: int
        unknown_10: int
        unknown_11: float
        unknown_12: float
        unknown_13: float
        unknown_14: float
        unknown_15: float
        unknown_16: float
        unknown_17: float
        unknown_18: float
        unknown_19: int
        unknown_20: float
        unknown_21: float
        unknown_22: float
        unnamed_0x00000023: json_util.JsonObject
        unnamed_0x00000024: json_util.JsonObject
        sound_1: int
        sound_2: int


@dataclasses.dataclass()
class WallCrawlerSwarm(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Active"),
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
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="Unknown 1"),
        },
    )
    animation_parameters: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000007,
                original_name="AnimationParameters",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="Unknown 2"),
        },
    )
    unknown_3: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Unknown 3"),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="Particle 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="Particle 2"),
        },
    )
    always_ffffffff_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000C, original_name="Always FFFFFFFF 1"),
        },
    )
    always_ffffffff_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="Always FFFFFFFF 2"),
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
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="Unknown 4"),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000010,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="Unknown 6"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="Unknown 7"),
        },
    )
    unknown_8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Unknown 8"),
        },
    )
    unknown_9: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000015, original_name="Unknown 9"),
        },
    )
    unknown_10: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000016, original_name="Unknown 10"),
        },
    )
    unknown_11: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="Unknown 11"),
        },
    )
    unknown_12: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="Unknown 12"),
        },
    )
    unknown_13: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000019, original_name="Unknown 13"),
        },
    )
    unknown_14: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001A, original_name="Unknown 14"),
        },
    )
    unknown_15: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="Unknown 15"),
        },
    )
    unknown_16: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="Unknown 16"),
        },
    )
    unknown_17: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="Unknown 17"),
        },
    )
    unknown_18: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="Unknown 18"),
        },
    )
    unknown_19: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="Unknown 19"),
        },
    )
    unknown_20: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000020, original_name="Unknown 20"),
        },
    )
    unknown_21: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000021, original_name="Unknown 21"),
        },
    )
    unknown_22: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000022, original_name="Unknown 22"),
        },
    )
    unnamed_0x00000023: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0x00000023,
                original_name="35",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    unnamed_0x00000024: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000024,
                original_name="36",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    sound_1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000025, original_name="Sound 1"),
        },
    )
    sound_2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000026, original_name="Sound 2"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x5A

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
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed_0x00000005 = ActorParameters.from_stream(data, game, property_size)
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        animation_parameters = AnimationParameters.from_stream(data, game, property_size)
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_l.unpack(data.read(4))[0]
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        always_ffffffff_1 = structs.BIG_l.unpack(data.read(4))[0]
        always_ffffffff_2 = structs.BIG_l.unpack(data.read(4))[0]
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_9 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_10 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_11 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_12 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_13 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_14 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_15 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_16 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_17 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_18 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_19 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_20 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_21 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_22 = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000023 = HealthInfo.from_stream(data, game, property_size)
        unnamed_0x00000024 = DamageVulnerability.from_stream(data, game, property_size)
        sound_1 = structs.BIG_l.unpack(data.read(4))[0]
        sound_2 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            active,
            unnamed_0x00000005,
            unknown_1,
            animation_parameters,
            unknown_2,
            unknown_3,
            particle_1,
            particle_2,
            always_ffffffff_1,
            always_ffffffff_2,
            damage_info_1,
            unknown_4,
            damage_info_2,
            unknown_5,
            unknown_6,
            unknown_7,
            unknown_8,
            unknown_9,
            unknown_10,
            unknown_11,
            unknown_12,
            unknown_13,
            unknown_14,
            unknown_15,
            unknown_16,
            unknown_17,
            unknown_18,
            unknown_19,
            unknown_20,
            unknown_21,
            unknown_22,
            unnamed_0x00000023,
            unnamed_0x00000024,
            sound_1,
            sound_2,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00'")  # 39 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_1))
        self.animation_parameters.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_l.pack(self.unknown_3))
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_l.pack(self.always_ffffffff_1))
        data.write(structs.BIG_l.pack(self.always_ffffffff_2))
        self.damage_info_1.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_4))
        self.damage_info_2.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_f.pack(self.unknown_7))
        data.write(structs.BIG_f.pack(self.unknown_8))
        data.write(structs.BIG_l.pack(self.unknown_9))
        data.write(structs.BIG_l.pack(self.unknown_10))
        data.write(structs.BIG_f.pack(self.unknown_11))
        data.write(structs.BIG_f.pack(self.unknown_12))
        data.write(structs.BIG_f.pack(self.unknown_13))
        data.write(structs.BIG_f.pack(self.unknown_14))
        data.write(structs.BIG_f.pack(self.unknown_15))
        data.write(structs.BIG_f.pack(self.unknown_16))
        data.write(structs.BIG_f.pack(self.unknown_17))
        data.write(structs.BIG_f.pack(self.unknown_18))
        data.write(structs.BIG_l.pack(self.unknown_19))
        data.write(structs.BIG_f.pack(self.unknown_20))
        data.write(structs.BIG_f.pack(self.unknown_21))
        data.write(structs.BIG_f.pack(self.unknown_22))
        self.unnamed_0x00000023.to_stream(data, game)
        self.unnamed_0x00000024.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.sound_1))
        data.write(structs.BIG_l.pack(self.sound_2))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WallCrawlerSwarmJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            active=json_data["active"],
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            unknown_1=json_data["unknown_1"],
            animation_parameters=AnimationParameters.from_json(json_data["animation_parameters"]),
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            particle_1=json_data["particle_1"],
            particle_2=json_data["particle_2"],
            always_ffffffff_1=json_data["always_ffffffff_1"],
            always_ffffffff_2=json_data["always_ffffffff_2"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            unknown_4=json_data["unknown_4"],
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
            unknown_9=json_data["unknown_9"],
            unknown_10=json_data["unknown_10"],
            unknown_11=json_data["unknown_11"],
            unknown_12=json_data["unknown_12"],
            unknown_13=json_data["unknown_13"],
            unknown_14=json_data["unknown_14"],
            unknown_15=json_data["unknown_15"],
            unknown_16=json_data["unknown_16"],
            unknown_17=json_data["unknown_17"],
            unknown_18=json_data["unknown_18"],
            unknown_19=json_data["unknown_19"],
            unknown_20=json_data["unknown_20"],
            unknown_21=json_data["unknown_21"],
            unknown_22=json_data["unknown_22"],
            unnamed_0x00000023=HealthInfo.from_json(json_data["unnamed_0x00000023"]),
            unnamed_0x00000024=DamageVulnerability.from_json(json_data["unnamed_0x00000024"]),
            sound_1=json_data["sound_1"],
            sound_2=json_data["sound_2"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "active": self.active,
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unknown_1": self.unknown_1,
            "animation_parameters": self.animation_parameters.to_json(),
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "particle_1": self.particle_1,
            "particle_2": self.particle_2,
            "always_ffffffff_1": self.always_ffffffff_1,
            "always_ffffffff_2": self.always_ffffffff_2,
            "damage_info_1": self.damage_info_1.to_json(),
            "unknown_4": self.unknown_4,
            "damage_info_2": self.damage_info_2.to_json(),
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
            "unknown_9": self.unknown_9,
            "unknown_10": self.unknown_10,
            "unknown_11": self.unknown_11,
            "unknown_12": self.unknown_12,
            "unknown_13": self.unknown_13,
            "unknown_14": self.unknown_14,
            "unknown_15": self.unknown_15,
            "unknown_16": self.unknown_16,
            "unknown_17": self.unknown_17,
            "unknown_18": self.unknown_18,
            "unknown_19": self.unknown_19,
            "unknown_20": self.unknown_20,
            "unknown_21": self.unknown_21,
            "unknown_22": self.unknown_22,
            "unnamed_0x00000023": self.unnamed_0x00000023.to_json(),
            "unnamed_0x00000024": self.unnamed_0x00000024.to_json(),
            "sound_1": self.sound_1,
            "sound_2": self.sound_2,
        }

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def _dependencies_for_sound_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_1)

    def _dependencies_for_sound_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self.animation_parameters.dependencies_for, "animation_parameters", "AnimationParameters"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
            (self._dependencies_for_sound_1, "sound_1", "int"),
            (self._dependencies_for_sound_2, "sound_2", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for WallCrawlerSwarm.{field_name} ({field_type}): {e}")
