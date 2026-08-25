# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BoolFloatJson(typing_extensions.TypedDict):
        override: bool
        value: float


@dataclasses.dataclass()
class BoolFloat(BaseProperty):
    override: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="Override"),
        },
    )
    value: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="Value"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        override = structs.BIG_bool_.unpack(data.read(1))[0]
        value = structs.BIG_f.unpack(data.read(4))[0]
        return cls(override, value)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.override))
        data.write(structs.BIG_f.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BoolFloatJson", data)
        return cls(
            override=json_data["override"],
            value=json_data["value"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "override": self.override,
            "value": self.value,
        }
