# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class StreamedAudioJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        song_file: int
        default_audio: bool
        fade_in_time: float
        fade_out_time: float
        volume: float
        pan: float
        memory_stream: bool
        positional: bool
        min_audible_distance: float
        max_audible_distance: float
        fall_off: float
        use_room_acoustics: bool
        volume_type: int


class VolumeType(enum.IntEnum):
    Unknown1 = 2487228356
    Unknown2 = 3796633071
    Unknown3 = 4268377914

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
class StreamedAudio(BaseObjectType):
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
    song_file: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRM"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9D1A67A8, original_name="SongFile"),
        },
    )
    default_audio: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x34B152C4, original_name="DefaultAudio"),
        },
    )
    fade_in_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AA341F, original_name="FadeInTime"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7C269EBC, original_name="FadeOutTime"),
        },
    )
    volume: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC7A7F189, original_name="Volume"),
        },
    )
    pan: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDF4353A3, original_name="Pan"),
        },
    )
    memory_stream: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x042BA4D5, original_name="MemoryStream"),
        },
    )
    positional: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6E0E81F8, original_name="Positional"),
        },
    )
    min_audible_distance: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25D4798A, original_name="MinAudibleDistance"),
        },
    )
    max_audible_distance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x214E48A0, original_name="MaxAudibleDistance"),
        },
    )
    fall_off: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72531867, original_name="FallOff"),
        },
    )
    use_room_acoustics: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x85707354, original_name="UseRoomAcoustics"),
        },
    )
    volume_type: VolumeType = dataclasses.field(
        default=VolumeType.Unknown3,
        metadata={
            "reflection": FieldReflection[VolumeType](
                VolumeType,
                id=0x9558711E,
                original_name="VolumeType",
                from_json=VolumeType.from_json,
                to_json=VolumeType.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "STAU"

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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D1A67A8
        song_file = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34B152C4
        default_audio = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90AA341F
        fade_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C269EBC
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7A7F189
        volume = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF4353A3
        pan = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x042BA4D5
        memory_stream = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E0E81F8
        positional = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25D4798A
        min_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214E48A0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72531867
        fall_off = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85707354
        use_room_acoustics = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9558711E
        volume_type = VolumeType.from_stream(data, game)

        return cls(
            editor_properties,
            song_file,
            default_audio,
            fade_in_time,
            fade_out_time,
            volume,
            pan,
            memory_stream,
            positional,
            min_audible_distance,
            max_audible_distance,
            fall_off,
            use_room_acoustics,
            volume_type,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9d\x1ag\xa8")  # 0x9d1a67a8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.song_file))

        data.write(b"4\xb1R\xc4")  # 0x34b152c4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.default_audio))

        data.write(b"\x90\xaa4\x1f")  # 0x90aa341f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_in_time))

        data.write(b"|&\x9e\xbc")  # 0x7c269ebc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

        data.write(b"\xc7\xa7\xf1\x89")  # 0xc7a7f189
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.volume))

        data.write(b"\xdfCS\xa3")  # 0xdf4353a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pan))

        data.write(b"\x04+\xa4\xd5")  # 0x42ba4d5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.memory_stream))

        data.write(b"n\x0e\x81\xf8")  # 0x6e0e81f8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.positional))

        data.write(b"%\xd4y\x8a")  # 0x25d4798a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_audible_distance))

        data.write(b"!NH\xa0")  # 0x214e48a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b"rS\x18g")  # 0x72531867
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fall_off))

        data.write(b"\x85psT")  # 0x85707354
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_room_acoustics))

        data.write(b"\x95Xq\x1e")  # 0x9558711e
        data.write(b"\x00\x04")  # size
        self.volume_type.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("StreamedAudioJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            song_file=json_data["song_file"],
            default_audio=json_data["default_audio"],
            fade_in_time=json_data["fade_in_time"],
            fade_out_time=json_data["fade_out_time"],
            volume=json_data["volume"],
            pan=json_data["pan"],
            memory_stream=json_data["memory_stream"],
            positional=json_data["positional"],
            min_audible_distance=json_data["min_audible_distance"],
            max_audible_distance=json_data["max_audible_distance"],
            fall_off=json_data["fall_off"],
            use_room_acoustics=json_data["use_room_acoustics"],
            volume_type=VolumeType.from_json(json_data["volume_type"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "song_file": self.song_file,
            "default_audio": self.default_audio,
            "fade_in_time": self.fade_in_time,
            "fade_out_time": self.fade_out_time,
            "volume": self.volume,
            "pan": self.pan,
            "memory_stream": self.memory_stream,
            "positional": self.positional,
            "min_audible_distance": self.min_audible_distance,
            "max_audible_distance": self.max_audible_distance,
            "fall_off": self.fall_off,
            "use_room_acoustics": self.use_room_acoustics,
            "volume_type": self.volume_type.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_volume_type(data: typing.BinaryIO, game: Game, property_size: int) -> VolumeType:
    return VolumeType.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x9D1A67A8: ("song_file", structs.decode_BIG_Q),
    0x34B152C4: ("default_audio", structs.decode_BIG_bool_),
    0x90AA341F: ("fade_in_time", structs.decode_BIG_f),
    0x7C269EBC: ("fade_out_time", structs.decode_BIG_f),
    0xC7A7F189: ("volume", structs.decode_BIG_f),
    0xDF4353A3: ("pan", structs.decode_BIG_f),
    0x042BA4D5: ("memory_stream", structs.decode_BIG_bool_),
    0x6E0E81F8: ("positional", structs.decode_BIG_bool_),
    0x25D4798A: ("min_audible_distance", structs.decode_BIG_f),
    0x214E48A0: ("max_audible_distance", structs.decode_BIG_f),
    0x72531867: ("fall_off", structs.decode_BIG_f),
    0x85707354: ("use_room_acoustics", structs.decode_BIG_bool_),
    0x9558711E: ("volume_type", _decode_volume_type),
}
