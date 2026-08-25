# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.SurroundPan import SurroundPan
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SoundJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        sound: int
        max_audible_distance: float
        drop_off: float
        delay_time: float
        min_volume: int
        max_volume: int
        priority: int
        surround_pan: json_util.JsonObject
        loop: bool
        ambient: bool
        unknown: bool
        auto_start: bool
        can_occlude: bool
        use_room_acoustics: bool
        persistent: bool
        play_always: bool
        all_area: bool
        sound_is_music: bool
        pitch: int
        echo_visor_max_volume: int


@dataclasses.dataclass()
class Sound(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x5F7C352E, original_name="Sound"),
        },
    )
    max_audible_distance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x214E48A0, original_name="MaxAudibleDistance"),
        },
    )
    drop_off: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08BF2E54, original_name="DropOff"),
        },
    )
    delay_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E16E012, original_name="DelayTime"),
        },
    )
    min_volume: int = dataclasses.field(
        default=20,
        metadata={
            "reflection": FieldReflection[int](int, id=0x57619496, original_name="MinVolume"),
        },
    )
    max_volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC712847C, original_name="MaxVolume"),
        },
    )
    priority: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42087650, original_name="Priority"),
        },
    )
    surround_pan: SurroundPan = dataclasses.field(
        default_factory=SurroundPan,
        metadata={
            "reflection": FieldReflection[SurroundPan](
                SurroundPan,
                id=0x0BB62639,
                original_name="SurroundPan",
                from_json=SurroundPan.from_json,
                to_json=SurroundPan.to_json,
            ),
        },
    )
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEDA47FF6, original_name="Loop"),
        },
    )
    ambient: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8971B7A7, original_name="Ambient"),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x84F3AC3D, original_name="Unknown"),
        },
    )
    auto_start: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3217DFF8, original_name="AutoStart"),
        },
    )
    can_occlude: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x94721163, original_name="CanOcclude"),
        },
    )
    use_room_acoustics: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x85707354, original_name="UseRoomAcoustics"),
        },
    )
    persistent: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEA03E258, original_name="Persistent"),
        },
    )
    play_always: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0D7F8C7F, original_name="PlayAlways"),
        },
    )
    all_area: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE45C3499, original_name="AllArea"),
        },
    )
    sound_is_music: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x76D40091, original_name="SoundIsMusic"),
        },
    )
    pitch: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8A764463, original_name="Pitch"),
        },
    )
    echo_visor_max_volume: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x69EC9107, original_name="EchoVisorMaxVolume"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SOND"

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F7C352E
        sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214E48A0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08BF2E54
        drop_off = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E16E012
        delay_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57619496
        min_volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC712847C
        max_volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42087650
        priority = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BB62639
        surround_pan = SurroundPan.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA47FF6
        loop = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8971B7A7
        ambient = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84F3AC3D
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3217DFF8
        auto_start = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94721163
        can_occlude = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85707354
        use_room_acoustics = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA03E258
        persistent = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D7F8C7F
        play_always = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE45C3499
        all_area = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76D40091
        sound_is_music = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A764463
        pitch = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69EC9107
        echo_visor_max_volume = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            sound,
            max_audible_distance,
            drop_off,
            delay_time,
            min_volume,
            max_volume,
            priority,
            surround_pan,
            loop,
            ambient,
            unknown,
            auto_start,
            can_occlude,
            use_room_acoustics,
            persistent,
            play_always,
            all_area,
            sound_is_music,
            pitch,
            echo_visor_max_volume,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_|5.")  # 0x5f7c352e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound))

        data.write(b"!NH\xa0")  # 0x214e48a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b"\x08\xbf.T")  # 0x8bf2e54
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.drop_off))

        data.write(b"\x8e\x16\xe0\x12")  # 0x8e16e012
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.delay_time))

        data.write(b"Wa\x94\x96")  # 0x57619496
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.min_volume))

        data.write(b"\xc7\x12\x84|")  # 0xc712847c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_volume))

        data.write(b"B\x08vP")  # 0x42087650
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.priority))

        data.write(b"\x0b\xb6&9")  # 0xbb62639
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.surround_pan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\xa4\x7f\xf6")  # 0xeda47ff6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.loop))

        data.write(b"\x89q\xb7\xa7")  # 0x8971b7a7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ambient))

        data.write(b"\x84\xf3\xac=")  # 0x84f3ac3d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b"2\x17\xdf\xf8")  # 0x3217dff8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_start))

        data.write(b"\x94r\x11c")  # 0x94721163
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_occlude))

        data.write(b"\x85psT")  # 0x85707354
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_room_acoustics))

        data.write(b"\xea\x03\xe2X")  # 0xea03e258
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.persistent))

        data.write(b"\r\x7f\x8c\x7f")  # 0xd7f8c7f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.play_always))

        data.write(b"\xe4\\4\x99")  # 0xe45c3499
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.all_area))

        data.write(b"v\xd4\x00\x91")  # 0x76d40091
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.sound_is_music))

        data.write(b"\x8avDc")  # 0x8a764463
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.pitch))

        data.write(b"i\xec\x91\x07")  # 0x69ec9107
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.echo_visor_max_volume))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SoundJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            sound=json_data["sound"],
            max_audible_distance=json_data["max_audible_distance"],
            drop_off=json_data["drop_off"],
            delay_time=json_data["delay_time"],
            min_volume=json_data["min_volume"],
            max_volume=json_data["max_volume"],
            priority=json_data["priority"],
            surround_pan=SurroundPan.from_json(json_data["surround_pan"]),
            loop=json_data["loop"],
            ambient=json_data["ambient"],
            unknown=json_data["unknown"],
            auto_start=json_data["auto_start"],
            can_occlude=json_data["can_occlude"],
            use_room_acoustics=json_data["use_room_acoustics"],
            persistent=json_data["persistent"],
            play_always=json_data["play_always"],
            all_area=json_data["all_area"],
            sound_is_music=json_data["sound_is_music"],
            pitch=json_data["pitch"],
            echo_visor_max_volume=json_data["echo_visor_max_volume"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "sound": self.sound,
            "max_audible_distance": self.max_audible_distance,
            "drop_off": self.drop_off,
            "delay_time": self.delay_time,
            "min_volume": self.min_volume,
            "max_volume": self.max_volume,
            "priority": self.priority,
            "surround_pan": self.surround_pan.to_json(),
            "loop": self.loop,
            "ambient": self.ambient,
            "unknown": self.unknown,
            "auto_start": self.auto_start,
            "can_occlude": self.can_occlude,
            "use_room_acoustics": self.use_room_acoustics,
            "persistent": self.persistent,
            "play_always": self.play_always,
            "all_area": self.all_area,
            "sound_is_music": self.sound_is_music,
            "pitch": self.pitch,
            "echo_visor_max_volume": self.echo_visor_max_volume,
        }

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_sound(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_surround_pan(data: typing.BinaryIO, game: Game, property_size: int) -> SurroundPan:
    return SurroundPan.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x5F7C352E: ("sound", structs.decode_BIG_l),
    0x214E48A0: ("max_audible_distance", structs.decode_BIG_f),
    0x08BF2E54: ("drop_off", structs.decode_BIG_f),
    0x8E16E012: ("delay_time", structs.decode_BIG_f),
    0x57619496: ("min_volume", structs.decode_BIG_l),
    0xC712847C: ("max_volume", structs.decode_BIG_l),
    0x42087650: ("priority", structs.decode_BIG_l),
    0x0BB62639: ("surround_pan", _decode_surround_pan),
    0xEDA47FF6: ("loop", structs.decode_BIG_bool_),
    0x8971B7A7: ("ambient", structs.decode_BIG_bool_),
    0x84F3AC3D: ("unknown", structs.decode_BIG_bool_),
    0x3217DFF8: ("auto_start", structs.decode_BIG_bool_),
    0x94721163: ("can_occlude", structs.decode_BIG_bool_),
    0x85707354: ("use_room_acoustics", structs.decode_BIG_bool_),
    0xEA03E258: ("persistent", structs.decode_BIG_bool_),
    0x0D7F8C7F: ("play_always", structs.decode_BIG_bool_),
    0xE45C3499: ("all_area", structs.decode_BIG_bool_),
    0x76D40091: ("sound_is_music", structs.decode_BIG_bool_),
    0x8A764463: ("pitch", structs.decode_BIG_l),
    0x69EC9107: ("echo_visor_max_volume", structs.decode_BIG_l),
}
