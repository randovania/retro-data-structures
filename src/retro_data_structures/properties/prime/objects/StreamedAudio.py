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

    class StreamedAudioJson(typing_extensions.TypedDict):
        name: str
        active: bool
        file_name: str
        no_stop_on_deactivate: bool
        fade_in: float
        fade_out: float
        volume: int
        one_shot: int
        music: bool


@dataclasses.dataclass()
class StreamedAudio(BaseObjectType):
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
    file_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000002, original_name="FileName"),
        },
    )
    no_stop_on_deactivate: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="NoStopOnDeactivate"),
        },
    )
    fade_in: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="FadeIn"),
        },
    )
    fade_out: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="FadeOut"),
        },
    )
    volume: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000006, original_name="Volume"),
        },
    )
    one_shot: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000007, original_name="OneShot"),
        },
    )
    music: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000008, original_name="Music"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x61

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        file_name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        no_stop_on_deactivate = structs.BIG_bool_.unpack(data.read(1))[0]
        fade_in = structs.BIG_f.unpack(data.read(4))[0]
        fade_out = structs.BIG_f.unpack(data.read(4))[0]
        volume = structs.BIG_l.unpack(data.read(4))[0]
        one_shot = structs.BIG_l.unpack(data.read(4))[0]
        music = structs.BIG_bool_.unpack(data.read(1))[0]
        return cls(name, active, file_name, no_stop_on_deactivate, fade_in, fade_out, volume, one_shot, music)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\t")  # 9 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(self.file_name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.no_stop_on_deactivate))
        data.write(structs.BIG_f.pack(self.fade_in))
        data.write(structs.BIG_f.pack(self.fade_out))
        data.write(structs.BIG_l.pack(self.volume))
        data.write(structs.BIG_l.pack(self.one_shot))
        data.write(structs.BIG_bool_.pack(self.music))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("StreamedAudioJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            file_name=json_data["file_name"],
            no_stop_on_deactivate=json_data["no_stop_on_deactivate"],
            fade_in=json_data["fade_in"],
            fade_out=json_data["fade_out"],
            volume=json_data["volume"],
            one_shot=json_data["one_shot"],
            music=json_data["music"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "file_name": self.file_name,
            "no_stop_on_deactivate": self.no_stop_on_deactivate,
            "fade_in": self.fade_in,
            "fade_out": self.fade_out,
            "volume": self.volume,
            "one_shot": self.one_shot,
            "music": self.music,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
