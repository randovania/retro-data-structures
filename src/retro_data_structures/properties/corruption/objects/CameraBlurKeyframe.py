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
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraBlurKeyframeJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        blur_type: int
        blur_radius: float
        which_filter_group: int
        interpolate_in_time: float
        interpolate_out_time: float


@dataclasses.dataclass()
class CameraBlurKeyframe(BaseObjectType):
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
    blur_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE9359148, original_name="BlurType"),
        },
    )
    blur_radius: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6F6EB1F4, original_name="BlurRadius"),
        },
    )
    which_filter_group: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3FDC4B2E, original_name="WhichFilterGroup"),
        },
    )
    interpolate_in_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xABD41A36, original_name="InterpolateInTime"),
        },
    )
    interpolate_out_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3EAF78FE, original_name="InterpolateOutTime"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "BLUR"

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
        if property_count != 6:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9359148
        blur_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6F6EB1F4
        blur_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FDC4B2E
        which_filter_group = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xABD41A36
        interpolate_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3EAF78FE
        interpolate_out_time = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties, blur_type, blur_radius, which_filter_group, interpolate_in_time, interpolate_out_time
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe95\x91H")  # 0xe9359148
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.blur_type))

        data.write(b"on\xb1\xf4")  # 0x6f6eb1f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.blur_radius))

        data.write(b"?\xdcK.")  # 0x3fdc4b2e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.which_filter_group))

        data.write(b"\xab\xd4\x1a6")  # 0xabd41a36
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.interpolate_in_time))

        data.write(b">\xafx\xfe")  # 0x3eaf78fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.interpolate_out_time))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraBlurKeyframeJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            blur_type=json_data["blur_type"],
            blur_radius=json_data["blur_radius"],
            which_filter_group=json_data["which_filter_group"],
            interpolate_in_time=json_data["interpolate_in_time"],
            interpolate_out_time=json_data["interpolate_out_time"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "blur_type": self.blur_type,
            "blur_radius": self.blur_radius,
            "which_filter_group": self.which_filter_group,
            "interpolate_in_time": self.interpolate_in_time,
            "interpolate_out_time": self.interpolate_out_time,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xE9359148: ("blur_type", structs.decode_BIG_l),
    0x6F6EB1F4: ("blur_radius", structs.decode_BIG_f),
    0x3FDC4B2E: ("which_filter_group", structs.decode_BIG_l),
    0xABD41A36: ("interpolate_in_time", structs.decode_BIG_f),
    0x3EAF78FE: ("interpolate_out_time", structs.decode_BIG_f),
}
