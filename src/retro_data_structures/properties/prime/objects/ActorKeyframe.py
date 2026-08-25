# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
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

    class ActorKeyframeJson(typing_extensions.TypedDict):
        name: str
        animation_index: int
        loop: bool
        loop_duration: float
        active: bool
        fade_out: int
        playback_rate: float


class FadeOut(enum.IntEnum):
    Zero = 0
    One = 1

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class ActorKeyframe(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    animation_index: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="AnimationIndex"),
        },
    )
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="Loop"),
        },
    )
    loop_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="LoopDuration"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Active"),
        },
    )
    fade_out: FadeOut = dataclasses.field(
        default=FadeOut.Zero,
        metadata={
            "reflection": FieldReflection[FadeOut](
                FadeOut, id=0x00000005, original_name="FadeOut", from_json=FadeOut.from_json, to_json=FadeOut.to_json
            ),
        },
    )
    playback_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="PlaybackRate"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x1D

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        animation_index = structs.BIG_l.unpack(data.read(4))[0]
        loop = structs.BIG_bool_.unpack(data.read(1))[0]
        loop_duration = structs.BIG_f.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        fade_out = FadeOut.from_stream(data, game)
        playback_rate = structs.BIG_f.unpack(data.read(4))[0]
        return cls(name, animation_index, loop, loop_duration, active, fade_out, playback_rate)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.animation_index))
        data.write(structs.BIG_bool_.pack(self.loop))
        data.write(structs.BIG_f.pack(self.loop_duration))
        data.write(structs.BIG_bool_.pack(self.active))
        self.fade_out.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.playback_rate))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorKeyframeJson", data)
        return cls(
            name=json_data["name"],
            animation_index=json_data["animation_index"],
            loop=json_data["loop"],
            loop_duration=json_data["loop_duration"],
            active=json_data["active"],
            fade_out=FadeOut.from_json(json_data["fade_out"]),
            playback_rate=json_data["playback_rate"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "animation_index": self.animation_index,
            "loop": self.loop,
            "loop_duration": self.loop_duration,
            "active": self.active,
            "fade_out": self.fade_out.to_json(),
            "playback_rate": self.playback_rate,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
