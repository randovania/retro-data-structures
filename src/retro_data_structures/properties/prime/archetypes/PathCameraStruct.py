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

    class PathCameraStructJson(typing_extensions.TypedDict):
        is_closed_loop: bool
        fixed_look_pos: bool
        side_view: bool
        camera_height_from_hint: bool
        clamp_to_closed_door: bool
        unused: bool


@dataclasses.dataclass()
class PathCameraStruct(BaseProperty):
    is_closed_loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="IsClosedLoop"),
        },
    )
    fixed_look_pos: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="FixedLookPos"),
        },
    )
    side_view: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="SideView"),
        },
    )
    camera_height_from_hint: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="CameraHeightFromHint"),
        },
    )
    clamp_to_closed_door: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="ClampToClosedDoor"),
        },
    )
    unused: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000005, original_name="Unused"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        is_closed_loop = structs.BIG_bool_.unpack(data.read(1))[0]
        fixed_look_pos = structs.BIG_bool_.unpack(data.read(1))[0]
        side_view = structs.BIG_bool_.unpack(data.read(1))[0]
        camera_height_from_hint = structs.BIG_bool_.unpack(data.read(1))[0]
        clamp_to_closed_door = structs.BIG_bool_.unpack(data.read(1))[0]
        unused = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(is_closed_loop, fixed_look_pos, side_view, camera_height_from_hint, clamp_to_closed_door, unused)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.is_closed_loop))
        data.write(structs.BIG_bool_.pack(self.fixed_look_pos))
        data.write(structs.BIG_bool_.pack(self.side_view))
        data.write(structs.BIG_bool_.pack(self.camera_height_from_hint))
        data.write(structs.BIG_bool_.pack(self.clamp_to_closed_door))
        data.write(structs.BIG_bool_.pack(self.unused))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PathCameraStructJson", data)
        return cls(
            is_closed_loop=json_data["is_closed_loop"],
            fixed_look_pos=json_data["fixed_look_pos"],
            side_view=json_data["side_view"],
            camera_height_from_hint=json_data["camera_height_from_hint"],
            clamp_to_closed_door=json_data["clamp_to_closed_door"],
            unused=json_data["unused"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "is_closed_loop": self.is_closed_loop,
            "fixed_look_pos": self.fixed_look_pos,
            "side_view": self.side_view,
            "camera_height_from_hint": self.camera_height_from_hint,
            "clamp_to_closed_door": self.clamp_to_closed_door,
            "unused": self.unused,
        }
