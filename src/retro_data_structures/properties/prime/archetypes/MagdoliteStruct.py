# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class MagdoliteStructJson(typing_extensions.TypedDict):
        unknown_1: int
        particle: int
        unknown_2: int
        unknown_3: float
        unknown_4: float
        unknown_5: float


@dataclasses.dataclass()
class MagdoliteStruct(BaseProperty):
    unknown_1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000000, original_name="Unknown 1"),
        },
    )
    particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000001, original_name="Particle"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="Unknown 2"),
        },
    )
    unknown_3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Unknown 5"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown_1 = structs.BIG_l.unpack(data.read(4))[0]
        particle = structs.BIG_L.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        return cls(unknown_1, particle, unknown_2, unknown_3, unknown_4, unknown_5)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_l.pack(self.unknown_1))
        data.write(structs.BIG_L.pack(self.particle))
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_f.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MagdoliteStructJson", data)
        return cls(
            unknown_1=json_data["unknown_1"],
            particle=json_data["particle"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_1": self.unknown_1,
            "particle": self.particle,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
        }

    def _dependencies_for_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_particle(asset_manager)
