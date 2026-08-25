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
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class StreamedMovieJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        movie_file: str
        loop: bool
        video_filter_enabled: bool
        unknown: int
        volume: int
        volume_type: int
        cache_length: float
        fade_out_time: float


@dataclasses.dataclass()
class StreamedMovie(BaseObjectType):
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
    movie_file: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x582B84A8, original_name="MovieFile"),
        },
    )
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEDA47FF6, original_name="Loop"),
        },
    )
    video_filter_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x36963BCC, original_name="VideoFilterEnabled"),
        },
    )
    unknown: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA78AC0C0, original_name="Unknown"),
        },
    )
    volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x80C66C37, original_name="Volume"),
        },
    )
    volume_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE1FF4F04, original_name="VolumeType"),
        },
    )
    cache_length: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD9EB77F, original_name="CacheLength"),
        },
    )
    fade_out_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7C269EBC, original_name="FadeOutTime"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "MOVI"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptStreamedMovie.rel"]

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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x582B84A8
        movie_file = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA47FF6
        loop = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36963BCC
        video_filter_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA78AC0C0
        unknown = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80C66C37
        volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1FF4F04
        volume_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD9EB77F
        cache_length = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C269EBC
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            movie_file,
            loop,
            video_filter_enabled,
            unknown,
            volume,
            volume_type,
            cache_length,
            fade_out_time,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\t")  # 9 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X+\x84\xa8")  # 0x582b84a8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.movie_file.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\xa4\x7f\xf6")  # 0xeda47ff6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.loop))

        data.write(b"6\x96;\xcc")  # 0x36963bcc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.video_filter_enabled))

        data.write(b"\xa7\x8a\xc0\xc0")  # 0xa78ac0c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b"\x80\xc6l7")  # 0x80c66c37
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.volume))

        data.write(b"\xe1\xffO\x04")  # 0xe1ff4f04
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.volume_type))

        data.write(b"\xad\x9e\xb7\x7f")  # 0xad9eb77f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cache_length))

        data.write(b"|&\x9e\xbc")  # 0x7c269ebc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("StreamedMovieJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            movie_file=json_data["movie_file"],
            loop=json_data["loop"],
            video_filter_enabled=json_data["video_filter_enabled"],
            unknown=json_data["unknown"],
            volume=json_data["volume"],
            volume_type=json_data["volume_type"],
            cache_length=json_data["cache_length"],
            fade_out_time=json_data["fade_out_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "movie_file": self.movie_file,
            "loop": self.loop,
            "video_filter_enabled": self.video_filter_enabled,
            "unknown": self.unknown,
            "volume": self.volume,
            "volume_type": self.volume_type,
            "cache_length": self.cache_length,
            "fade_out_time": self.fade_out_time,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_movie_file(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x582B84A8: ("movie_file", _decode_movie_file),
    0xEDA47FF6: ("loop", structs.decode_BIG_bool_),
    0x36963BCC: ("video_filter_enabled", structs.decode_BIG_bool_),
    0xA78AC0C0: ("unknown", structs.decode_BIG_l),
    0x80C66C37: ("volume", structs.decode_BIG_l),
    0xE1FF4F04: ("volume_type", structs.decode_BIG_l),
    0xAD9EB77F: ("cache_length", structs.decode_BIG_f),
    0x7C269EBC: ("fade_out_time", structs.decode_BIG_f),
}
