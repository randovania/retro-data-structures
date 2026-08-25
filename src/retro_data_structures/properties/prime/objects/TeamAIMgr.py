# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TeamAIMgrJson(typing_extensions.TypedDict):
        name: str
        ai_count: int
        melee_count: int
        ranged_count: int
        unknown_count: int
        max_melee_attacker_count: int
        max_ranged_attacker_count: int
        position_mode: int
        melee_time_interval: float
        ranged_time_interval: float


@dataclasses.dataclass()
class TeamAIMgr(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    ai_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="AICount"),
        },
    )
    melee_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="MeleeCount"),
        },
    )
    ranged_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="RangedCount"),
        },
    )
    unknown_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="UnknownCount"),
        },
    )
    max_melee_attacker_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="MaxMeleeAttackerCount"),
        },
    )
    max_ranged_attacker_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="MaxRangedAttackerCount"),
        },
    )
    position_mode: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="PositionMode"),
        },
    )
    melee_time_interval: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="MeleeTimeInterval"),
        },
    )
    ranged_time_interval: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="RangedTimeInterval"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x6C

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        ai_count = structs.BIG_l.unpack(data.read(4))[0]
        melee_count = structs.BIG_l.unpack(data.read(4))[0]
        ranged_count = structs.BIG_l.unpack(data.read(4))[0]
        unknown_count = structs.BIG_l.unpack(data.read(4))[0]
        max_melee_attacker_count = structs.BIG_l.unpack(data.read(4))[0]
        max_ranged_attacker_count = structs.BIG_l.unpack(data.read(4))[0]
        position_mode = structs.BIG_l.unpack(data.read(4))[0]
        melee_time_interval = structs.BIG_f.unpack(data.read(4))[0]
        ranged_time_interval = structs.BIG_f.unpack(data.read(4))[0]
        return cls(
            name,
            ai_count,
            melee_count,
            ranged_count,
            unknown_count,
            max_melee_attacker_count,
            max_ranged_attacker_count,
            position_mode,
            melee_time_interval,
            ranged_time_interval,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\n")  # 10 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.ai_count))
        data.write(structs.BIG_l.pack(self.melee_count))
        data.write(structs.BIG_l.pack(self.ranged_count))
        data.write(structs.BIG_l.pack(self.unknown_count))
        data.write(structs.BIG_l.pack(self.max_melee_attacker_count))
        data.write(structs.BIG_l.pack(self.max_ranged_attacker_count))
        data.write(structs.BIG_l.pack(self.position_mode))
        data.write(structs.BIG_f.pack(self.melee_time_interval))
        data.write(structs.BIG_f.pack(self.ranged_time_interval))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TeamAIMgrJson", data)
        return cls(
            name=json_data["name"],
            ai_count=json_data["ai_count"],
            melee_count=json_data["melee_count"],
            ranged_count=json_data["ranged_count"],
            unknown_count=json_data["unknown_count"],
            max_melee_attacker_count=json_data["max_melee_attacker_count"],
            max_ranged_attacker_count=json_data["max_ranged_attacker_count"],
            position_mode=json_data["position_mode"],
            melee_time_interval=json_data["melee_time_interval"],
            ranged_time_interval=json_data["ranged_time_interval"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "ai_count": self.ai_count,
            "melee_count": self.melee_count,
            "ranged_count": self.ranged_count,
            "unknown_count": self.unknown_count,
            "max_melee_attacker_count": self.max_melee_attacker_count,
            "max_ranged_attacker_count": self.max_ranged_attacker_count,
            "position_mode": self.position_mode,
            "melee_time_interval": self.melee_time_interval,
            "ranged_time_interval": self.ranged_time_interval,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
