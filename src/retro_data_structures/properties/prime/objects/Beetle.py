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

    class BeetleJson(typing_extensions.TypedDict):
        name: str
        unknown: int
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000005: json_util.JsonObject
        unnamed_0x00000006: json_util.JsonObject
        unnamed_0x00000007: json_util.JsonObject
        orbit_offset: json_util.JsonValue
        unused: float
        abdomen_vulnerability: json_util.JsonObject
        armor_vulnerability: json_util.JsonObject
        abdomen_model: int
        entrance_type: int
        initial_attack_delay: float
        retreat_time: float


@dataclasses.dataclass()
class Beetle(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    unknown: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Unknown"),
        },
    )  # Choice
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000003, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unnamed_0x00000005: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x00000005,
                original_name="5",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    unnamed_0x00000006: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x00000006,
                original_name="6",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
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
    orbit_offset: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000008, original_name="OrbitOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unused: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unused"),
        },
    )
    abdomen_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000A,
                original_name="AbdomenVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    armor_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x0000000B,
                original_name="ArmorVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    abdomen_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="AbdomenModel"),
        },
    )
    entrance_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="EntranceType"),
        },
    )
    initial_attack_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="InitialAttackDelay"),
        },
    )
    retreat_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="RetreatTime"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x16

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        unknown = structs.BIG_L.unpack(data.read(4))[0]
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000005 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000006 = ActorParameters.from_stream(data, game, property_size)
        unnamed_0x00000007 = DamageInfo.from_stream(data, game, property_size)
        orbit_offset = Vector.from_stream(data, game, property_size)
        unused = structs.BIG_f.unpack(data.read(4))[0]
        abdomen_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
        armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
        abdomen_model = structs.BIG_L.unpack(data.read(4))[0]
        entrance_type = structs.BIG_l.unpack(data.read(4))[0]
        initial_attack_delay = structs.BIG_f.unpack(data.read(4))[0]
        retreat_time = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            unknown,
            position,
            rotation,
            scale,
            unnamed_0x00000005,
            unnamed_0x00000006,
            unnamed_0x00000007,
            orbit_offset,
            unused,
            abdomen_vulnerability,
            armor_vulnerability,
            abdomen_model,
            entrance_type,
            initial_attack_delay,
            retreat_time,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x10")  # 16 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_L.pack(self.unknown))
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        self.unnamed_0x00000006.to_stream(data, game)
        self.unnamed_0x00000007.to_stream(data, game)
        self.orbit_offset.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unused))
        self.abdomen_vulnerability.to_stream(data, game)
        self.armor_vulnerability.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.abdomen_model))
        data.write(structs.BIG_l.pack(self.entrance_type))
        data.write(structs.BIG_f.pack(self.initial_attack_delay))
        data.write(structs.BIG_f.pack(self.retreat_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BeetleJson", data)
        return cls(
            name=json_data["name"],
            unknown=json_data["unknown"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000005=PatternedAITypedef.from_json(json_data["unnamed_0x00000005"]),
            unnamed_0x00000006=ActorParameters.from_json(json_data["unnamed_0x00000006"]),
            unnamed_0x00000007=DamageInfo.from_json(json_data["unnamed_0x00000007"]),
            orbit_offset=Vector.from_json(json_data["orbit_offset"]),
            unused=json_data["unused"],
            abdomen_vulnerability=DamageVulnerability.from_json(json_data["abdomen_vulnerability"]),
            armor_vulnerability=DamageVulnerability.from_json(json_data["armor_vulnerability"]),
            abdomen_model=json_data["abdomen_model"],
            entrance_type=json_data["entrance_type"],
            initial_attack_delay=json_data["initial_attack_delay"],
            retreat_time=json_data["retreat_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "unknown": self.unknown,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unnamed_0x00000006": self.unnamed_0x00000006.to_json(),
            "unnamed_0x00000007": self.unnamed_0x00000007.to_json(),
            "orbit_offset": self.orbit_offset.to_json(),
            "unused": self.unused,
            "abdomen_vulnerability": self.abdomen_vulnerability.to_json(),
            "armor_vulnerability": self.armor_vulnerability.to_json(),
            "abdomen_model": self.abdomen_model,
            "entrance_type": self.entrance_type,
            "initial_attack_delay": self.initial_attack_delay,
            "retreat_time": self.retreat_time,
        }

    def _dependencies_for_abdomen_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.abdomen_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "PatternedAITypedef"),
            (self.unnamed_0x00000006.dependencies_for, "unnamed_0x00000006", "ActorParameters"),
            (self._dependencies_for_abdomen_model, "abdomen_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Beetle.{field_name} ({field_type}): {e}")
