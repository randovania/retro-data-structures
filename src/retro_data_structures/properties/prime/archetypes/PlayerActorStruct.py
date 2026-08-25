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

    class PlayerActorStructJson(typing_extensions.TypedDict):
        suit_transition: bool
        previous_suit: bool
        force_reset: bool
        track_in_area_data: bool
        keep_in_state_manager: bool


@dataclasses.dataclass()
class PlayerActorStruct(BaseProperty):
    suit_transition: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="SuitTransition"),
        },
    )
    previous_suit: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="PreviousSuit"),
        },
    )
    force_reset: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="ForceReset"),
        },
    )
    track_in_area_data: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="TrackInAreaData"),
        },
    )
    keep_in_state_manager: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="KeepInStateManager"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        suit_transition = structs.BIG_bool_.unpack(data.read(1))[0]
        previous_suit = structs.BIG_bool_.unpack(data.read(1))[0]
        force_reset = structs.BIG_bool_.unpack(data.read(1))[0]
        track_in_area_data = structs.BIG_bool_.unpack(data.read(1))[0]
        keep_in_state_manager = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(suit_transition, previous_suit, force_reset, track_in_area_data, keep_in_state_manager)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.suit_transition))
        data.write(structs.BIG_bool_.pack(self.previous_suit))
        data.write(structs.BIG_bool_.pack(self.force_reset))
        data.write(structs.BIG_bool_.pack(self.track_in_area_data))
        data.write(structs.BIG_bool_.pack(self.keep_in_state_manager))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerActorStructJson", data)
        return cls(
            suit_transition=json_data["suit_transition"],
            previous_suit=json_data["previous_suit"],
            force_reset=json_data["force_reset"],
            track_in_area_data=json_data["track_in_area_data"],
            keep_in_state_manager=json_data["keep_in_state_manager"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "suit_transition": self.suit_transition,
            "previous_suit": self.previous_suit,
            "force_reset": self.force_reset,
            "track_in_area_data": self.track_in_area_data,
            "keep_in_state_manager": self.keep_in_state_manager,
        }
