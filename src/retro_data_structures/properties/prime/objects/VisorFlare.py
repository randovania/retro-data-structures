# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.FlareDef import FlareDef
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class VisorFlareJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        unknown_1: bool
        unknown_2: int
        unknown_3: bool
        unknown_4: float
        unknown_5: float
        unknown_6: float
        unknown_7: int
        flare_def_1: json_util.JsonObject
        flare_def_2: json_util.JsonObject
        flare_def_3: json_util.JsonObject
        flare_def_4: json_util.JsonObject
        flare_def_5: json_util.JsonObject


@dataclasses.dataclass()
class VisorFlare(BaseObjectType):
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
    unknown_1: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="Unknown 1"),
        },
    )
    unknown_2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="Unknown 2"),
        },
    )
    unknown_3: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Unknown 3"),
        },
    )
    unknown_4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="Unknown 4"),
        },
    )
    unknown_5: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="Unknown 5"),
        },
    )
    unknown_6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="Unknown 6"),
        },
    )
    unknown_7: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="Unknown 7"),
        },
    )
    flare_def_1: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x00000009,
                original_name="FlareDef 1",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_2: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x0000000A,
                original_name="FlareDef 2",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_3: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x0000000B,
                original_name="FlareDef 3",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_4: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x0000000C,
                original_name="FlareDef 4",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )
    flare_def_5: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef,
                id=0x0000000D,
                original_name="FlareDef 5",
                from_json=FlareDef.from_json,
                to_json=FlareDef.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x51

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        unknown_1 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_2 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_3 = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown_4 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_6 = structs.BIG_f.unpack(data.read(4))[0]
        unknown_7 = structs.BIG_l.unpack(data.read(4))[0]
        flare_def_1 = FlareDef.from_stream(data, game, property_size)
        flare_def_2 = FlareDef.from_stream(data, game, property_size)
        flare_def_3 = FlareDef.from_stream(data, game, property_size)
        flare_def_4 = FlareDef.from_stream(data, game, property_size)
        flare_def_5 = FlareDef.from_stream(data, game, property_size)
        return cls(
            name,
            position,
            unknown_1,
            unknown_2,
            unknown_3,
            unknown_4,
            unknown_5,
            unknown_6,
            unknown_7,
            flare_def_1,
            flare_def_2,
            flare_def_3,
            flare_def_4,
            flare_def_5,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0e")  # 14 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown_1))
        data.write(structs.BIG_l.pack(self.unknown_2))
        data.write(structs.BIG_bool_.pack(self.unknown_3))
        data.write(structs.BIG_f.pack(self.unknown_4))
        data.write(structs.BIG_f.pack(self.unknown_5))
        data.write(structs.BIG_f.pack(self.unknown_6))
        data.write(structs.BIG_l.pack(self.unknown_7))
        self.flare_def_1.to_stream(data, game)
        self.flare_def_2.to_stream(data, game)
        self.flare_def_3.to_stream(data, game)
        self.flare_def_4.to_stream(data, game)
        self.flare_def_5.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VisorFlareJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            unknown_1=json_data["unknown_1"],
            unknown_2=json_data["unknown_2"],
            unknown_3=json_data["unknown_3"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
            unknown_6=json_data["unknown_6"],
            unknown_7=json_data["unknown_7"],
            flare_def_1=FlareDef.from_json(json_data["flare_def_1"]),
            flare_def_2=FlareDef.from_json(json_data["flare_def_2"]),
            flare_def_3=FlareDef.from_json(json_data["flare_def_3"]),
            flare_def_4=FlareDef.from_json(json_data["flare_def_4"]),
            flare_def_5=FlareDef.from_json(json_data["flare_def_5"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "unknown_1": self.unknown_1,
            "unknown_2": self.unknown_2,
            "unknown_3": self.unknown_3,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
            "unknown_6": self.unknown_6,
            "unknown_7": self.unknown_7,
            "flare_def_1": self.flare_def_1.to_json(),
            "flare_def_2": self.flare_def_2.to_json(),
            "flare_def_3": self.flare_def_3.to_json(),
            "flare_def_4": self.flare_def_4.to_json(),
            "flare_def_5": self.flare_def_5.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.flare_def_1.dependencies_for, "flare_def_1", "FlareDef"),
            (self.flare_def_2.dependencies_for, "flare_def_2", "FlareDef"),
            (self.flare_def_3.dependencies_for, "flare_def_3", "FlareDef"),
            (self.flare_def_4.dependencies_for, "flare_def_4", "FlareDef"),
            (self.flare_def_5.dependencies_for, "flare_def_5", "FlareDef"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for VisorFlare.{field_name} ({field_type}): {e}")
