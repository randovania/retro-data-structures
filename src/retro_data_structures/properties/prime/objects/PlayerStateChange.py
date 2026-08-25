# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.prime as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PlayerStateChangeJson(typing_extensions.TypedDict):
        name: str
        active: bool
        unnamed: int
        amount: int
        capacity: int
        unknown_4: int
        unknown_5: int


@dataclasses.dataclass()
class PlayerStateChange(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Active"),
        },
    )
    unnamed: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0x00000002,
                original_name="2",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    amount: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="Amount"),
        },
    )
    capacity: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000004, original_name="Capacity"),
        },
    )
    unknown_4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="Unknown 4"),
        },
    )
    unknown_5: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="Unknown 5"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x57

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        unnamed = enums.PlayerItemEnum.from_stream(data, game)
        amount = structs.BIG_l.unpack(data.read(4))[0]
        capacity = structs.BIG_l.unpack(data.read(4))[0]
        unknown_4 = structs.BIG_l.unpack(data.read(4))[0]
        unknown_5 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(name, active, unnamed, amount, capacity, unknown_4, unknown_5)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        self.unnamed.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.amount))
        data.write(structs.BIG_l.pack(self.capacity))
        data.write(structs.BIG_l.pack(self.unknown_4))
        data.write(structs.BIG_l.pack(self.unknown_5))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerStateChangeJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            unnamed=enums.PlayerItemEnum.from_json(json_data["unnamed"]),
            amount=json_data["amount"],
            capacity=json_data["capacity"],
            unknown_4=json_data["unknown_4"],
            unknown_5=json_data["unknown_5"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "unnamed": self.unnamed.to_json(),
            "amount": self.amount,
            "capacity": self.capacity,
            "unknown_4": self.unknown_4,
            "unknown_5": self.unknown_5,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
