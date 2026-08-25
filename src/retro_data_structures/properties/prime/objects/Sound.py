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

    class SoundJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        sound_id: int
        active: bool
        max_distance: float
        dist_comp: float
        start_delay: float
        min_volume: int
        volume: int
        priority: int
        pan: int
        loop: bool
        non_emitter: bool
        auto_start: bool
        occlusion_test: bool
        acoustics: bool
        world_sfx: bool
        allow_duplicates: bool
        pitch: int


@dataclasses.dataclass()
class Sound(BaseObjectType):
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
    sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000003, original_name="SoundID"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="Active"),
        },
    )
    max_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="MaxDistance"),
        },
    )
    dist_comp: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="DistComp"),
        },
    )
    start_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="StartDelay"),
        },
    )
    min_volume: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000008, original_name="MinVolume"),
        },
    )
    volume: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000009, original_name="Volume"),
        },
    )
    priority: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000A, original_name="Priority"),
        },
    )
    pan: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="Pan"),
        },
    )
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000C, original_name="Loop"),
        },
    )
    non_emitter: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000D, original_name="NonEmitter"),
        },
    )
    auto_start: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000E, original_name="AutoStart"),
        },
    )
    occlusion_test: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="OcclusionTest"),
        },
    )
    acoustics: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="Acoustics"),
        },
    )
    world_sfx: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000011, original_name="WorldSFX"),
        },
    )
    allow_duplicates: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000012, original_name="AllowDuplicates"),
        },
    )
    pitch: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000013, original_name="Pitch"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x9

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        sound_id = structs.BIG_l.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        max_distance = structs.BIG_f.unpack(data.read(4))[0]
        dist_comp = structs.BIG_f.unpack(data.read(4))[0]
        start_delay = structs.BIG_f.unpack(data.read(4))[0]
        min_volume = structs.BIG_l.unpack(data.read(4))[0]
        volume = structs.BIG_l.unpack(data.read(4))[0]
        priority = structs.BIG_l.unpack(data.read(4))[0]
        pan = structs.BIG_l.unpack(data.read(4))[0]
        loop = structs.BIG_bool_.unpack(data.read(1))[0]
        non_emitter = structs.BIG_bool_.unpack(data.read(1))[0]
        auto_start = structs.BIG_bool_.unpack(data.read(1))[0]
        occlusion_test = structs.BIG_bool_.unpack(data.read(1))[0]
        acoustics = structs.BIG_bool_.unpack(data.read(1))[0]
        world_sfx = structs.BIG_bool_.unpack(data.read(1))[0]
        allow_duplicates = structs.BIG_bool_.unpack(data.read(1))[0]
        pitch = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            sound_id,
            active,
            max_distance,
            dist_comp,
            start_delay,
            min_volume,
            volume,
            priority,
            pan,
            loop,
            non_emitter,
            auto_start,
            occlusion_test,
            acoustics,
            world_sfx,
            allow_duplicates,
            pitch,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x14")  # 20 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.sound_id))
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.max_distance))
        data.write(structs.BIG_f.pack(self.dist_comp))
        data.write(structs.BIG_f.pack(self.start_delay))
        data.write(structs.BIG_l.pack(self.min_volume))
        data.write(structs.BIG_l.pack(self.volume))
        data.write(structs.BIG_l.pack(self.priority))
        data.write(structs.BIG_l.pack(self.pan))
        data.write(structs.BIG_bool_.pack(self.loop))
        data.write(structs.BIG_bool_.pack(self.non_emitter))
        data.write(structs.BIG_bool_.pack(self.auto_start))
        data.write(structs.BIG_bool_.pack(self.occlusion_test))
        data.write(structs.BIG_bool_.pack(self.acoustics))
        data.write(structs.BIG_bool_.pack(self.world_sfx))
        data.write(structs.BIG_bool_.pack(self.allow_duplicates))
        data.write(structs.BIG_l.pack(self.pitch))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SoundJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            sound_id=json_data["sound_id"],
            active=json_data["active"],
            max_distance=json_data["max_distance"],
            dist_comp=json_data["dist_comp"],
            start_delay=json_data["start_delay"],
            min_volume=json_data["min_volume"],
            volume=json_data["volume"],
            priority=json_data["priority"],
            pan=json_data["pan"],
            loop=json_data["loop"],
            non_emitter=json_data["non_emitter"],
            auto_start=json_data["auto_start"],
            occlusion_test=json_data["occlusion_test"],
            acoustics=json_data["acoustics"],
            world_sfx=json_data["world_sfx"],
            allow_duplicates=json_data["allow_duplicates"],
            pitch=json_data["pitch"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "sound_id": self.sound_id,
            "active": self.active,
            "max_distance": self.max_distance,
            "dist_comp": self.dist_comp,
            "start_delay": self.start_delay,
            "min_volume": self.min_volume,
            "volume": self.volume,
            "priority": self.priority,
            "pan": self.pan,
            "loop": self.loop,
            "non_emitter": self.non_emitter,
            "auto_start": self.auto_start,
            "occlusion_test": self.occlusion_test,
            "acoustics": self.acoustics,
            "world_sfx": self.world_sfx,
            "allow_duplicates": self.allow_duplicates,
            "pitch": self.pitch,
        }

    def _dependencies_for_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_sound_id(asset_manager)
