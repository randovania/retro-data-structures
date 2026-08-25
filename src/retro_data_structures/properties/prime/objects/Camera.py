# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        active: bool
        shot_duration: float
        look_at_player: bool
        out_of_player_eye: bool
        into_player_eye: bool
        draw_player: bool
        disable_input: bool
        unknown: bool
        finish_cinematic_skip: bool
        field_of_view: float
        check_failsafe: bool
        disable_out_of_into: bool


@dataclasses.dataclass()
class Camera(BaseObjectType):
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
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="Active"),
        },
    )
    shot_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="ShotDuration"),
        },
    )
    look_at_player: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000005, original_name="LookAtPlayer"),
        },
    )
    out_of_player_eye: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="OutOfPlayerEye"),
        },
    )
    into_player_eye: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="IntoPlayerEye"),
        },
    )
    draw_player: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="DrawPlayer"),
        },
    )
    disable_input: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000009, original_name="DisableInput"),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="Unknown"),
        },
    )
    finish_cinematic_skip: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="FinishCinematicSkip"),
        },
    )
    field_of_view: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="FieldOfView"),
        },
    )
    check_failsafe: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="CheckFailsafe"),
        },
    )
    disable_out_of_into: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="DisableOutOfInto"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0xC

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        shot_duration = structs.BIG_f.unpack(data.read(4))[0]
        look_at_player = structs.BIG_bool_.unpack(data.read(1))[0]
        out_of_player_eye = structs.BIG_bool_.unpack(data.read(1))[0]
        into_player_eye = structs.BIG_bool_.unpack(data.read(1))[0]
        draw_player = structs.BIG_bool_.unpack(data.read(1))[0]
        disable_input = structs.BIG_bool_.unpack(data.read(1))[0]
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
        finish_cinematic_skip = structs.BIG_bool_.unpack(data.read(1))[0]
        field_of_view = structs.BIG_f.unpack(data.read(4))[0]
        check_failsafe = structs.BIG_bool_.unpack(data.read(1))[0]
        disable_out_of_into = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(
            name,
            position,
            rotation,
            active,
            shot_duration,
            look_at_player,
            out_of_player_eye,
            into_player_eye,
            draw_player,
            disable_input,
            unknown,
            finish_cinematic_skip,
            field_of_view,
            check_failsafe,
            disable_out_of_into,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0f")  # 15 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.shot_duration))
        data.write(structs.BIG_bool_.pack(self.look_at_player))
        data.write(structs.BIG_bool_.pack(self.out_of_player_eye))
        data.write(structs.BIG_bool_.pack(self.into_player_eye))
        data.write(structs.BIG_bool_.pack(self.draw_player))
        data.write(structs.BIG_bool_.pack(self.disable_input))
        data.write(structs.BIG_bool_.pack(self.unknown))
        data.write(structs.BIG_bool_.pack(self.finish_cinematic_skip))
        data.write(structs.BIG_f.pack(self.field_of_view))
        data.write(structs.BIG_bool_.pack(self.check_failsafe))
        data.write(structs.BIG_bool_.pack(self.disable_out_of_into))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            active=json_data["active"],
            shot_duration=json_data["shot_duration"],
            look_at_player=json_data["look_at_player"],
            out_of_player_eye=json_data["out_of_player_eye"],
            into_player_eye=json_data["into_player_eye"],
            draw_player=json_data["draw_player"],
            disable_input=json_data["disable_input"],
            unknown=json_data["unknown"],
            finish_cinematic_skip=json_data["finish_cinematic_skip"],
            field_of_view=json_data["field_of_view"],
            check_failsafe=json_data["check_failsafe"],
            disable_out_of_into=json_data["disable_out_of_into"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "active": self.active,
            "shot_duration": self.shot_duration,
            "look_at_player": self.look_at_player,
            "out_of_player_eye": self.out_of_player_eye,
            "into_player_eye": self.into_player_eye,
            "draw_player": self.draw_player,
            "disable_input": self.disable_input,
            "unknown": self.unknown,
            "finish_cinematic_skip": self.finish_cinematic_skip,
            "field_of_view": self.field_of_view,
            "check_failsafe": self.check_failsafe,
            "disable_out_of_into": self.disable_out_of_into,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
