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
from retro_data_structures.properties.prime.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MetroidAlphaJson(typing_extensions.TypedDict):
        name: str
        unknown_1: int
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000005: json_util.JsonObject
        unnamed_0x00000006: json_util.JsonObject
        damage_vulnerability_1: json_util.JsonObject
        damage_vulnerability_2: json_util.JsonObject
        unknown_2: float
        unknown_3: float
        unknown_4: float
        unknown_5: float
        unknown_6: float
        unknown_7: float
        animation_parameters_1: json_util.JsonObject
        animation_parameters_2: json_util.JsonObject
        animation_parameters_3: json_util.JsonObject
        animation_parameters_4: json_util.JsonObject
        unknown_8: bool


@dataclasses.dataclass()
class MetroidAlpha(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Unknown 1"),
        },
    )
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
    damage_vulnerability_1: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00000007,
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
                id=0x00000008,
                original_name="DamageVulnerability 2",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="Unknown 2"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Unknown 6"),
        },
    )
    unknown_7: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Unknown 7"),
        },
    )
    animation_parameters_1: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x0000000F,
                original_name="AnimationParameters 1",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    animation_parameters_2: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000010,
                original_name="AnimationParameters 2",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    animation_parameters_3: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000011,
                original_name="AnimationParameters 3",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    animation_parameters_4: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x00000012,
                original_name="AnimationParameters 4",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000013, original_name="Unknown 8"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x44

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000005 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000006 = ActorParameters.from_stream(data, game, property_size)
        damage_vulnerability_1 = DamageVulnerability.from_stream(data, game, property_size)
        damage_vulnerability_2 = DamageVulnerability.from_stream(data, game, property_size)
        unknown_2 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_f.unpack(data.read(4))[0]
        animation_parameters_1 = AnimationParameters.from_stream(data, game, property_size)
        animation_parameters_2 = AnimationParameters.from_stream(data, game, property_size)
        animation_parameters_3 = AnimationParameters.from_stream(data, game, property_size)
        animation_parameters_4 = AnimationParameters.from_stream(data, game, property_size)
        unknown_8 = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            unknown_1,
            position,
            rotation,
            scale,
            unnamed_0x00000005,
            unnamed_0x00000006,
            damage_vulnerability_1,
            damage_vulnerability_2,
            unknown_2,
            unknown_3,
            unknown_4,
            unknown_5,
            unknown_6,
            unknown_7,
            animation_parameters_1,
            animation_parameters_2,
            animation_parameters_3,
            animation_parameters_4,
            unknown_8,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x14")  # 20 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.unknown_1))
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        self.unnamed_0x00000006.to_stream(data, game)
        self.damage_vulnerability_1.to_stream(data, game)
        self.damage_vulnerability_2.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_f.pack(self.unknown_7))
        self.animation_parameters_1.to_stream(data, game)
        self.animation_parameters_2.to_stream(data, game)
        self.animation_parameters_3.to_stream(data, game)
        self.animation_parameters_4.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown_8))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidAlphaJson", data)
        return cls(
            name=json_data["name"],
            unknown_1=json_data["unknown_1"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000005=PatternedAITypedef.from_json(json_data["unnamed_0x00000005"]),
            unnamed_0x00000006=ActorParameters.from_json(json_data["unnamed_0x00000006"]),
            damage_vulnerability_1=DamageVulnerability.from_json(json_data["damage_vulnerability_1"]),
            damage_vulnerability_2=DamageVulnerability.from_json(json_data["damage_vulnerability_2"]),
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            animation_parameters_1=AnimationParameters.from_json(json_data["animation_parameters_1"]),
            animation_parameters_2=AnimationParameters.from_json(json_data["animation_parameters_2"]),
            animation_parameters_3=AnimationParameters.from_json(json_data["animation_parameters_3"]),
            animation_parameters_4=AnimationParameters.from_json(json_data["animation_parameters_4"]),
            unknown_8=json_data["unknown_8"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "unknown_1": self.unknown_1,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000005": self.unnamed_0x00000005.to_json(),
            "unnamed_0x00000006": self.unnamed_0x00000006.to_json(),
            "damage_vulnerability_1": self.damage_vulnerability_1.to_json(),
            "damage_vulnerability_2": self.damage_vulnerability_2.to_json(),
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "animation_parameters_1": self.animation_parameters_1.to_json(),
            "animation_parameters_2": self.animation_parameters_2.to_json(),
            "animation_parameters_3": self.animation_parameters_3.to_json(),
            "animation_parameters_4": self.animation_parameters_4.to_json(),
            "unknown_8": self.unknown_8,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "PatternedAITypedef"),
            (self.unnamed_0x00000006.dependencies_for, "unnamed_0x00000006", "ActorParameters"),
            (self.animation_parameters_1.dependencies_for, "animation_parameters_1", "AnimationParameters"),
            (self.animation_parameters_2.dependencies_for, "animation_parameters_2", "AnimationParameters"),
            (self.animation_parameters_3.dependencies_for, "animation_parameters_3", "AnimationParameters"),
            (self.animation_parameters_4.dependencies_for, "animation_parameters_4", "AnimationParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for MetroidAlpha.{field_name} ({field_type}): {e}")
