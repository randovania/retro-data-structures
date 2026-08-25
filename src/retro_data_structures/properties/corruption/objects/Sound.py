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
from retro_data_structures.properties.corruption.archetypes.SurroundPan import SurroundPan
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SoundJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        sound_effect: int
        min_audible_distance: float
        max_audible_distance: float
        delay_time: float
        volume: float
        volume_variance: float
        surround_pan: json_util.JsonObject
        pan_variance: float
        pitch: float
        ambient: bool
        auto_start: bool
        can_occlude: bool
        play_always: bool
        sound_is_music: bool
        update_velocity: bool
        ignore_generated_behavior: bool
        sound_is_ui_sound: bool
        sound_is_speech: bool


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
    sound_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x771A3176, original_name="SoundEffect"),
        },
    )
    min_audible_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25D4798A, original_name="MinAudibleDistance"),
        },
    )
    max_audible_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x214E48A0, original_name="MaxAudibleDistance"),
        },
    )
    delay_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E16E012, original_name="DelayTime"),
        },
    )
    volume: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC7A7F189, original_name="Volume"),
        },
    )
    volume_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0E44B56, original_name="VolumeVariance"),
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
    pan_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95237258, original_name="PanVariance"),
        },
    )
    pitch: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2CC5CB93, original_name="Pitch"),
        },
    )
    ambient: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8971B7A7, original_name="Ambient"),
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
    play_always: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0D7F8C7F, original_name="PlayAlways"),
        },
    )
    sound_is_music: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x76D40091, original_name="SoundIsMusic"),
        },
    )
    update_velocity: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x90145CD2, original_name="UpdateVelocity"),
        },
    )
    ignore_generated_behavior: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEBD19273, original_name="IgnoreGeneratedBehavior"),
        },
    )
    sound_is_ui_sound: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x186F6592, original_name="SoundIsUISound"),
        },
    )
    sound_is_speech: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5E096FD2, original_name="SoundIsSpeech"),
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
        if property_count != 19:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x771A3176
        sound_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25D4798A
        min_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214E48A0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E16E012
        delay_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7A7F189
        volume = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0E44B56
        volume_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BB62639
        surround_pan = SurroundPan.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95237258
        pan_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CC5CB93
        pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8971B7A7
        ambient = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3217DFF8
        auto_start = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94721163
        can_occlude = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D7F8C7F
        play_always = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76D40091
        sound_is_music = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90145CD2
        update_velocity = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBD19273
        ignore_generated_behavior = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x186F6592
        sound_is_ui_sound = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E096FD2
        sound_is_speech = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            sound_effect,
            min_audible_distance,
            max_audible_distance,
            delay_time,
            volume,
            volume_variance,
            surround_pan,
            pan_variance,
            pitch,
            ambient,
            auto_start,
            can_occlude,
            play_always,
            sound_is_music,
            update_velocity,
            ignore_generated_behavior,
            sound_is_ui_sound,
            sound_is_speech,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x13")  # 19 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\x1a1v")  # 0x771a3176
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_effect))

        data.write(b"%\xd4y\x8a")  # 0x25d4798a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_audible_distance))

        data.write(b"!NH\xa0")  # 0x214e48a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b"\x8e\x16\xe0\x12")  # 0x8e16e012
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.delay_time))

        data.write(b"\xc7\xa7\xf1\x89")  # 0xc7a7f189
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.volume))

        data.write(b"\xf0\xe4KV")  # 0xf0e44b56
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.volume_variance))

        data.write(b"\x0b\xb6&9")  # 0xbb62639
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.surround_pan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95#rX")  # 0x95237258
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pan_variance))

        data.write(b",\xc5\xcb\x93")  # 0x2cc5cb93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pitch))

        data.write(b"\x89q\xb7\xa7")  # 0x8971b7a7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ambient))

        data.write(b"2\x17\xdf\xf8")  # 0x3217dff8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_start))

        data.write(b"\x94r\x11c")  # 0x94721163
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_occlude))

        data.write(b"\r\x7f\x8c\x7f")  # 0xd7f8c7f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.play_always))

        data.write(b"v\xd4\x00\x91")  # 0x76d40091
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.sound_is_music))

        data.write(b"\x90\x14\\\xd2")  # 0x90145cd2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.update_velocity))

        data.write(b"\xeb\xd1\x92s")  # 0xebd19273
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ignore_generated_behavior))

        data.write(b"\x18oe\x92")  # 0x186f6592
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.sound_is_ui_sound))

        data.write(b"^\to\xd2")  # 0x5e096fd2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.sound_is_speech))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SoundJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            sound_effect=json_data["sound_effect"],
            min_audible_distance=json_data["min_audible_distance"],
            max_audible_distance=json_data["max_audible_distance"],
            delay_time=json_data["delay_time"],
            volume=json_data["volume"],
            volume_variance=json_data["volume_variance"],
            surround_pan=SurroundPan.from_json(json_data["surround_pan"]),
            pan_variance=json_data["pan_variance"],
            pitch=json_data["pitch"],
            ambient=json_data["ambient"],
            auto_start=json_data["auto_start"],
            can_occlude=json_data["can_occlude"],
            play_always=json_data["play_always"],
            sound_is_music=json_data["sound_is_music"],
            update_velocity=json_data["update_velocity"],
            ignore_generated_behavior=json_data["ignore_generated_behavior"],
            sound_is_ui_sound=json_data["sound_is_ui_sound"],
            sound_is_speech=json_data["sound_is_speech"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "sound_effect": self.sound_effect,
            "min_audible_distance": self.min_audible_distance,
            "max_audible_distance": self.max_audible_distance,
            "delay_time": self.delay_time,
            "volume": self.volume,
            "volume_variance": self.volume_variance,
            "surround_pan": self.surround_pan.to_json(),
            "pan_variance": self.pan_variance,
            "pitch": self.pitch,
            "ambient": self.ambient,
            "auto_start": self.auto_start,
            "can_occlude": self.can_occlude,
            "play_always": self.play_always,
            "sound_is_music": self.sound_is_music,
            "update_velocity": self.update_velocity,
            "ignore_generated_behavior": self.ignore_generated_behavior,
            "sound_is_ui_sound": self.sound_is_ui_sound,
            "sound_is_speech": self.sound_is_speech,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_surround_pan(data: typing.BinaryIO, game: Game, property_size: int) -> SurroundPan:
    return SurroundPan.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x771A3176: ("sound_effect", structs.decode_BIG_Q),
    0x25D4798A: ("min_audible_distance", structs.decode_BIG_f),
    0x214E48A0: ("max_audible_distance", structs.decode_BIG_f),
    0x8E16E012: ("delay_time", structs.decode_BIG_f),
    0xC7A7F189: ("volume", structs.decode_BIG_f),
    0xF0E44B56: ("volume_variance", structs.decode_BIG_f),
    0x0BB62639: ("surround_pan", _decode_surround_pan),
    0x95237258: ("pan_variance", structs.decode_BIG_f),
    0x2CC5CB93: ("pitch", structs.decode_BIG_f),
    0x8971B7A7: ("ambient", structs.decode_BIG_bool_),
    0x3217DFF8: ("auto_start", structs.decode_BIG_bool_),
    0x94721163: ("can_occlude", structs.decode_BIG_bool_),
    0x0D7F8C7F: ("play_always", structs.decode_BIG_bool_),
    0x76D40091: ("sound_is_music", structs.decode_BIG_bool_),
    0x90145CD2: ("update_velocity", structs.decode_BIG_bool_),
    0xEBD19273: ("ignore_generated_behavior", structs.decode_BIG_bool_),
    0x186F6592: ("sound_is_ui_sound", structs.decode_BIG_bool_),
    0x5E096FD2: ("sound_is_speech", structs.decode_BIG_bool_),
}
