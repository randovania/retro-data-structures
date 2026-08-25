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
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ThardusRockProjectileJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        unknown_1: bool
        unknown_2: bool
        unknown_3: float
        model: int
        afsm: int


@dataclasses.dataclass()
class ThardusRockProjectile(BaseObjectType):
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
    unknown_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="Unknown 1"),
        },
    )
    unknown_2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="Unknown 2"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="Unknown 3"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="Model"),
        },
    )
    afsm: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["AFSM"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="AFSM"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x5F

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
        unknown_1 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_2 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        model = structs.BIG_L.unpack(data.read(4))[0]
        afsm = structs.BIG_L.unpack(data.read(4))[0]
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
            model,
            afsm,
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
        data.write(structs.BIG_bool_.pack(self.unknown_1))
        data.write(structs.BIG_bool_.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_L.pack(self.model))
        data.write(structs.BIG_L.pack(self.afsm))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ThardusRockProjectileJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data["unnamed_0x00000004"]),
            unnamed_0x00000005=ActorParameters.from_json(json_data["unnamed_0x00000005"]),
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            model=json_data["model"],
            afsm=json_data["afsm"],
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
            "unknown_3": self.unknown_3,
            "model": self.model,
            "afsm": self.afsm,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_afsm(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.afsm)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_model, "model", "AssetId"),
            (self._dependencies_for_afsm, "afsm", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ThardusRockProjectile.{field_name} ({field_type}): {e}"
                )
