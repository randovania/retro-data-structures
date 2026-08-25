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
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MetroidPrimeStage2Json(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        particle_1: int
        unnamed_0x00000007: json_util.JsonObject
        elsc: int
        unknown_1: int
        particle_2: int


@dataclasses.dataclass()
class MetroidPrimeStage2(BaseObjectType):
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
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="Particle 1"),
        },
    )
    unnamed_0x00000007: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo, id=0x00000007, original_name="7", from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
            ),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="ELSC"),
        },
    )
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Unknown 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="Particle 2"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x83

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
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        unnamed_0x00000007 = DamageInfo.from_stream(data, game, property_size)
        elsc = structs.BIG_L.unpack(data.read(4))[0]
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            particle_1,
            unnamed_0x00000007,
            elsc,
            unknown_1,
            particle_2,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0b")  # 11 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.particle_1))
        self.unnamed_0x00000007.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.elsc))
        data.write(structs.BIG_l.pack(self.unknown_1))
        data.write(structs.BIG_L.pack(self.particle_2))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidPrimeStage2Json", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            particle_1=json_data["particle_1"],
            unnamed_0x00000007=DamageInfo.from_json(json_data["unnamed_0x00000007"]),
            elsc=json_data["elsc"],
            unknown_1=json_data["unknown_1"],
            particle_2=json_data["particle_2"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000004": self.unnamed_0x00000004.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "particle_1": self.particle_1,
            "unnamed_0x00000007": self.unnamed_0x00000007.to_json(),
            "elsc": self.elsc,
            "unknown_1": self.unknown_1,
            "particle_2": self.particle_2,
        }

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_elsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.elsc)

    def _dependencies_for_unknown_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_elsc, "elsc", "AssetId"),
            (self._dependencies_for_unknown_1, "unknown_1", "int"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for MetroidPrimeStage2.{field_name} ({field_type}): {e}")
