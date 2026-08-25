# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PhazonPoolJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unknown_1: bool
        model_1: int
        model_2: int
        particle_1: int
        particle_2: int
        unknown_2: int
        unnamed: json_util.JsonObject
        force: json_util.JsonValue
        trigger_flags: int
        pool_starting_value: float
        phazon_beam_drain_per_second: float
        time_until_regeneration: float
        automatic_drain_dont_regenerate: bool
        time_until_automatic_drain: float


@dataclasses.dataclass()
class PhazonPool(BaseObjectType):
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
    unknown_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Unknown 1"),
        },
    )
    model_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000005, original_name="Model 1"),
        },
    )
    model_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000006, original_name="Model 2"),
        },
    )
    particle_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000007, original_name="Particle 1"),
        },
    )
    particle_2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="Particle 2"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Unknown 2"),
        },
    )
    unnamed: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0000000A,
                original_name="10",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    force: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x0000000B, original_name="Force", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    trigger_flags: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000C, original_name="Trigger Flags"),
        },
    )
    pool_starting_value: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Pool Starting Value"),
        },
    )
    phazon_beam_drain_per_second: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Phazon Beam Drain Per Second"),
        },
    )
    time_until_regeneration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="Time Until Regeneration"),
        },
    )
    automatic_drain_dont_regenerate: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="Automatic Drain/Don't Regenerate"),
        },
    )
    time_until_automatic_drain: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="Time Until Automatic Drain"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x87

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
        unknown_1 = structs.BIG_bool_.unpack(data.read(1))[0]
        model_1 = structs.BIG_L.unpack(data.read(4))[0]
        model_2 = structs.BIG_L.unpack(data.read(4))[0]
        particle_1 = structs.BIG_L.unpack(data.read(4))[0]
        particle_2 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unnamed = DamageInfo.from_stream(data, game, property_size)
        force = Vector.from_stream(data, game, property_size)
        trigger_flags = structs.BIG_l.unpack(data.read(4))[0]
        pool_starting_value = structs.BIG_f.unpack(data.read(4))[0]
        phazon_beam_drain_per_second = structs.BIG_f.unpack(data.read(4))[0]
        time_until_regeneration = structs.BIG_f.unpack(data.read(4))[0]
        automatic_drain_dont_regenerate = structs.BIG_bool_.unpack(data.read(1))[0]
        time_until_automatic_drain = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            scale,
            unknown_1,
            model_1,
            model_2,
            particle_1,
            particle_2,
            unknown_2,
            unnamed,
            force,
            trigger_flags,
            pool_starting_value,
            phazon_beam_drain_per_second,
            time_until_regeneration,
            automatic_drain_dont_regenerate,
            time_until_automatic_drain,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x12")  # 18 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown_1))
        data.write(structs.BIG_L.pack(self.model_1))
        data.write(structs.BIG_L.pack(self.model_2))
        data.write(structs.BIG_L.pack(self.particle_1))
        data.write(structs.BIG_L.pack(self.particle_2))
        data.write(structs.BIG_l.pack(self.unknown_2))
        self.unnamed.to_stream(data, game)
        self.force.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.trigger_flags))
        data.write(structs.BIG_f.pack(self.pool_starting_value))
        data.write(structs.BIG_f.pack(self.phazon_beam_drain_per_second))
        data.write(structs.BIG_f.pack(self.time_until_regeneration))
        data.write(structs.BIG_bool_.pack(self.automatic_drain_dont_regenerate))
        data.write(structs.BIG_f.pack(self.time_until_automatic_drain))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PhazonPoolJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            scale=Vector.from_json(json_data["scale"]),
            unknown_1=json_data["unknown_1"],
            model_1=json_data["model_1"],
            model_2=json_data["model_2"],
            particle_1=json_data["particle_1"],
            particle_2=json_data["particle_2"],
            unknown_2=json_data["unknown_2"],
            unnamed=DamageInfo.from_json(json_data["unnamed"]),
            force=Vector.from_json(json_data["force"]),
            trigger_flags=json_data["trigger_flags"],
            pool_starting_value=json_data["pool_starting_value"],
            phazon_beam_drain_per_second=json_data["phazon_beam_drain_per_second"],
            time_until_regeneration=json_data["time_until_regeneration"],
            automatic_drain_dont_regenerate=json_data["automatic_drain_dont_regenerate"],
            time_until_automatic_drain=json_data["time_until_automatic_drain"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "scale": self.scale.to_json(),
            "unknown_1": self.unknown_1,
            "model_1": self.model_1,
            "model_2": self.model_2,
            "particle_1": self.particle_1,
            "particle_2": self.particle_2,
            "unknown_2": self.unknown_2,
            "unnamed": self.unnamed.to_json(),
            "force": self.force.to_json(),
            "trigger_flags": self.trigger_flags,
            "pool_starting_value": self.pool_starting_value,
            "phazon_beam_drain_per_second": self.phazon_beam_drain_per_second,
            "time_until_regeneration": self.time_until_regeneration,
            "automatic_drain_dont_regenerate": self.automatic_drain_dont_regenerate,
            "time_until_automatic_drain": self.time_until_automatic_drain,
        }

    def _dependencies_for_model_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model_1)

    def _dependencies_for_model_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model_2)

    def _dependencies_for_particle_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_1)

    def _dependencies_for_particle_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model_1, "model_1", "AssetId"),
            (self._dependencies_for_model_2, "model_2", "AssetId"),
            (self._dependencies_for_particle_1, "particle_1", "AssetId"),
            (self._dependencies_for_particle_2, "particle_2", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PhazonPool.{field_name} ({field_type}): {e}")
