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
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PlayerUserAnimPointJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        animation: json_util.JsonObject
        attach_dist: float
        unknown_0xad2d4f53: float
        unknown_0x285b4540: float
        unknown_0x6806d0b3: float
        unknown_0x1ce620a7: int


@dataclasses.dataclass()
class PlayerUserAnimPoint(BaseObjectType):
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
    animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA3D63F44,
                original_name="Animation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    attach_dist: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x643D2769, original_name="AttachDist"),
        },
    )
    unknown_0xad2d4f53: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD2D4F53, original_name="Unknown"),
        },
    )
    unknown_0x285b4540: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x285B4540, original_name="Unknown"),
        },
    )
    unknown_0x6806d0b3: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6806D0B3, original_name="Unknown"),
        },
    )
    unknown_0x1ce620a7: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1CE620A7, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PUAP"

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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3D63F44
        animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x643D2769
        attach_dist = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD2D4F53
        unknown_0xad2d4f53 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x285B4540
        unknown_0x285b4540 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6806D0B3
        unknown_0x6806d0b3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CE620A7
        unknown_0x1ce620a7 = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            animation,
            attach_dist,
            unknown_0xad2d4f53,
            unknown_0x285b4540,
            unknown_0x6806d0b3,
            unknown_0x1ce620a7,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa3\xd6?D")  # 0xa3d63f44
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"d='i")  # 0x643d2769
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attach_dist))

        data.write(b"\xad-OS")  # 0xad2d4f53
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xad2d4f53))

        data.write(b"([E@")  # 0x285b4540
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x285b4540))

        data.write(b"h\x06\xd0\xb3")  # 0x6806d0b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6806d0b3))

        data.write(b"\x1c\xe6 \xa7")  # 0x1ce620a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x1ce620a7))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerUserAnimPointJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            animation=AnimationParameters.from_json(json_data["animation"]),
            attach_dist=json_data["attach_dist"],
            unknown_0xad2d4f53=json_data["unknown_0xad2d4f53"],
            unknown_0x285b4540=json_data["unknown_0x285b4540"],
            unknown_0x6806d0b3=json_data["unknown_0x6806d0b3"],
            unknown_0x1ce620a7=json_data["unknown_0x1ce620a7"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "animation": self.animation.to_json(),
            "attach_dist": self.attach_dist,
            "unknown_0xad2d4f53": self.unknown_0xad2d4f53,
            "unknown_0x285b4540": self.unknown_0x285b4540,
            "unknown_0x6806d0b3": self.unknown_0x6806d0b3,
            "unknown_0x1ce620a7": self.unknown_0x1ce620a7,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xA3D63F44: ("animation", _decode_animation),
    0x643D2769: ("attach_dist", structs.decode_BIG_f),
    0xAD2D4F53: ("unknown_0xad2d4f53", structs.decode_BIG_f),
    0x285B4540: ("unknown_0x285b4540", structs.decode_BIG_f),
    0x6806D0B3: ("unknown_0x6806d0b3", structs.decode_BIG_f),
    0x1CE620A7: ("unknown_0x1ce620a7", structs.decode_BIG_l),
}
