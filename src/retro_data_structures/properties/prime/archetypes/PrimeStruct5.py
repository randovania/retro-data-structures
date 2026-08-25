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

    class PrimeStruct5Json(typing_extensions.TypedDict):
        unknown_1: int
        unknown_2: int
        unknown_3: int
        unknown_4: int
        unknown_5: int
        unknown_6: int
        unknown_7: int
        unknown_8: int


@dataclasses.dataclass()
class PrimeStruct5(BaseProperty):
    unknown_1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000000, original_name="Unknown 1"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="Unknown 2"),
        },
    )
    unknown_3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000002, original_name="Unknown 3"),
        },
    )
    unknown_4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000003, original_name="Unknown 4"),
        },
    )
    unknown_5: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="Unknown 5"),
        },
    )
    unknown_6: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="Unknown 6"),
        },
    )
    unknown_7: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="Unknown 7"),
        },
    )
    unknown_8: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="Unknown 8"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown_1 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_L.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_8 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(unknown_1, unknown_2, unknown_3, unknown_4, unknown_5, unknown_6, unknown_7, unknown_8)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_L.pack(self.unknown_1))
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_L.pack(self.unknown_3))
        data.write(structs.BIG_L.pack(self.unknown_4))
        data.write(structs.BIG_l.pack(self.unknown_5))
        data.write(structs.BIG_l.pack(self.unknown_6))
        data.write(structs.BIG_l.pack(self.unknown_7))
        data.write(structs.BIG_l.pack(self.unknown_8))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PrimeStruct5Json", data)
        return cls(
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            unknown_8=json_data["unknown_8"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "unknown_8": self.unknown_8,
        }

    def _dependencies_for_unknown_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_1)

    def _dependencies_for_unknown_3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_3)

    def _dependencies_for_unknown_4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_4)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_unknown_1, "unknown_1", "AssetId"),
            (self._dependencies_for_unknown_3, "unknown_3", "AssetId"),
            (self._dependencies_for_unknown_4, "unknown_4", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PrimeStruct5.{field_name} ({field_type}): {e}")
