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

    class AIKeyframeJson(typing_extensions.TypedDict):
        name: str
        animation_id: int
        looping: bool
        lifetime: float
        active: bool
        fade_out: int
        playback_rate: float


@dataclasses.dataclass()
class AIKeyframe(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    animation_id: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000001, original_name="AnimationID"),
        },
    )
    looping: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000002, original_name="Looping"),
        },
    )
    lifetime: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="Lifetime"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Active"),
        },
    )
    fade_out: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000005, original_name="FadeOut"),
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
        return 0x41

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        animation_id = structs.BIG_l.unpack(data.read(4))[0]
        looping = structs.BIG_bool_.unpack(data.read(1))[0]
        lifetime = structs.BIG_f.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        fade_out = structs.BIG_l.unpack(data.read(4))[0]
        playback_rate = structs.BIG_f.unpack(data.read(4))[0]
        return cls(name, animation_id, looping, lifetime, active, fade_out, playback_rate)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x07")  # 7 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_l.pack(self.animation_id))
        data.write(structs.BIG_bool_.pack(self.looping))
        data.write(structs.BIG_f.pack(self.lifetime))
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_l.pack(self.fade_out))
        data.write(structs.BIG_f.pack(self.playback_rate))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AIKeyframeJson", data)
        return cls(
            name=json_data["name"],
            animation_id=json_data["animation_id"],
            looping=json_data["looping"],
            lifetime=json_data["lifetime"],
            active=json_data["active"],
            fade_out=json_data["fade_out"],
            playback_rate=json_data["playback_rate"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "animation_id": self.animation_id,
            "looping": self.looping,
            "lifetime": self.lifetime,
            "active": self.active,
            "fade_out": self.fade_out,
            "playback_rate": self.playback_rate,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
