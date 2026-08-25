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
from retro_data_structures.properties.prime.archetypes.MagdoliteStruct import MagdoliteStruct
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MagdoliteJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        unknown_1: float
        unknown_2: float
        damage_info_1: json_util.JsonObject
        damage_info_2: json_util.JsonObject
        damage_vulnerability_1: json_util.JsonObject
        damage_vulnerability_2: json_util.JsonObject
        model: int
        cskr: int
        unknown_3: float
        unknown_4: float
        unknown_5: float
        unknown_6: float
        unnamed_0x00000012: json_util.JsonObject
        unknown_12: float
        unknown_13: float
        unknown_14: float


@dataclasses.dataclass()
class Magdolite(BaseObjectType):
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
    damage_info_1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000008,
                original_name="DamageInfo 1",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_2: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x00000009,
                original_name="DamageInfo 2",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
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
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="Model"),
        },
    )
    cskr: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="CSKR"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="Unknown 6"),
        },
    )
    unnamed_0x00000012: MagdoliteStruct = dataclasses.field(
        default_factory=MagdoliteStruct,
        metadata={
            "reflection": FieldReflection[MagdoliteStruct](
                MagdoliteStruct,
                id=0x00000012,
                original_name="18",
                from_json=MagdoliteStruct.from_json,
                to_json=MagdoliteStruct.to_json,
            ),
        },
    )
    unknown_12: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="Unknown 12"),
        },
    )
    unknown_13: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="Unknown 13"),
        },
    )
    unknown_14: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="Unknown 14"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x6B

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
        damage_info_1 = DamageInfo.from_stream(data, game, property_size)
        damage_info_2 = DamageInfo.from_stream(data, game, property_size)
        damage_vulnerability_1 = DamageVulnerability.from_stream(data, game, property_size)
        damage_vulnerability_2 = DamageVulnerability.from_stream(data, game, property_size)
        model = structs.BIG_L.unpack(data.read(4))[0]
        cskr = structs.BIG_L.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000012 = MagdoliteStruct.from_stream(data, game, property_size)
        unknown_12 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_13 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_14 = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unnamed_0x00000004,
            unnamed_0x00000005,
            unknown_1,
            unknown_2,
            damage_info_1,
            damage_info_2,
            damage_vulnerability_1,
            damage_vulnerability_2,
            model,
            cskr,
            unknown_3,
            unknown_4,
            unknown_5,
            unknown_6,
            unnamed_0x00000012,
            unknown_12,
            unknown_13,
            unknown_14,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x16")  # 22 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_1))
        data.write(structs.BIG_f.pack(self.unknown_2))
        self.damage_info_1.to_stream(data, game)
        self.damage_info_2.to_stream(data, game)
        self.damage_vulnerability_1.to_stream(data, game)
        self.damage_vulnerability_2.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.model))
        data.write(structs.BIG_L.pack(self.cskr))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        self.unnamed_0x00000012.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_12))
        data.write(structs.BIG_f.pack(self.unknown_13))
        data.write(structs.BIG_f.pack(self.unknown_14))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MagdoliteJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            damage_info_1=DamageInfo.from_json(json_data["damage_info_1"]),
            damage_info_2=DamageInfo.from_json(json_data["damage_info_2"]),
            damage_vulnerability_1=DamageVulnerability.from_json(json_data["damage_vulnerability_1"]),
            damage_vulnerability_2=DamageVulnerability.from_json(json_data["damage_vulnerability_2"]),
            model=json_data["model"],
            cskr=json_data["cskr"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unnamed_0x00000012=MagdoliteStruct.from_json(json_data["unnamed_0x00000012"]),
            unknown_12=json_data["unknown_12"],
            unknown_13=json_data["unknown_13"],
            unknown_14=json_data["unknown_14"],
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
            "damage_info_1": self.damage_info_1.to_json(),
            "damage_info_2": self.damage_info_2.to_json(),
            "damage_vulnerability_1": self.damage_vulnerability_1.to_json(),
            "damage_vulnerability_2": self.damage_vulnerability_2.to_json(),
            "model": self.model,
            "cskr": self.cskr,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unnamed_0x00000012": self.unnamed_0x00000012.to_json(),
            "unknown_12": self.unknown_12,
            "unknown_13": self.unknown_13,
            "unknown_14": self.unknown_14,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_cskr(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cskr)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_model, "model", "AssetId"),
            (self._dependencies_for_cskr, "cskr", "AssetId"),
            (self.unnamed_0x00000012.dependencies_for, "unnamed_0x00000012", "MagdoliteStruct"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Magdolite.{field_name} ({field_type}): {e}")
