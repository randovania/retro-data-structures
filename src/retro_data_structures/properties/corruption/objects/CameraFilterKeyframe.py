# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraFilterKeyframeJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        filter_type: int
        filter_shape: int
        filter_stage: int
        which_filter_group: int
        color: json_util.JsonValue
        interpolate_in_time: float
        interpolate_out_time: float
        texture: int
        model: int


@dataclasses.dataclass()
class CameraFilterKeyframe(BaseObjectType):
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
    filter_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7975DB5B, original_name="FilterType"),
        },
    )
    filter_shape: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6A3E9A3D, original_name="FilterShape"),
        },
    )
    filter_stage: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x58BDBD7B, original_name="FilterStage"),
        },
    )
    which_filter_group: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3FDC4B2E, original_name="WhichFilterGroup"),
        },
    )
    color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x37C7D09D, original_name="Color", from_json=Color.from_json, to_json=Color.to_json
            ),
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
    texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD1F65872, original_name="Texture"),
        },
    )
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "FILT"

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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7975DB5B
        filter_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A3E9A3D
        filter_shape = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58BDBD7B
        filter_stage = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FDC4B2E
        which_filter_group = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37C7D09D
        color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xABD41A36
        interpolate_in_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3EAF78FE
        interpolate_out_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1F65872
        texture = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            editor_properties,
            filter_type,
            filter_shape,
            filter_stage,
            which_filter_group,
            color,
            interpolate_in_time,
            interpolate_out_time,
            texture,
            model,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\n")  # 10 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"yu\xdb[")  # 0x7975db5b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.filter_type))

        data.write(b"j>\x9a=")  # 0x6a3e9a3d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.filter_shape))

        data.write(b"X\xbd\xbd{")  # 0x58bdbd7b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.filter_stage))

        data.write(b"?\xdcK.")  # 0x3fdc4b2e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.which_filter_group))

        data.write(b"7\xc7\xd0\x9d")  # 0x37c7d09d
        data.write(b"\x00\x10")  # size
        self.color.to_stream(data, game)

        data.write(b"\xab\xd4\x1a6")  # 0xabd41a36
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.interpolate_in_time))

        data.write(b">\xafx\xfe")  # 0x3eaf78fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.interpolate_out_time))

        data.write(b"\xd1\xf6Xr")  # 0xd1f65872
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.texture))

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraFilterKeyframeJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            filter_type=json_data["filter_type"],
            filter_shape=json_data["filter_shape"],
            filter_stage=json_data["filter_stage"],
            which_filter_group=json_data["which_filter_group"],
            color=Color.from_json(json_data["color"]),
            interpolate_in_time=json_data["interpolate_in_time"],
            interpolate_out_time=json_data["interpolate_out_time"],
            texture=json_data["texture"],
            model=json_data["model"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "filter_type": self.filter_type,
            "filter_shape": self.filter_shape,
            "filter_stage": self.filter_stage,
            "which_filter_group": self.which_filter_group,
            "color": self.color.to_json(),
            "interpolate_in_time": self.interpolate_in_time,
            "interpolate_out_time": self.interpolate_out_time,
            "texture": self.texture,
            "model": self.model,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7975DB5B: ("filter_type", structs.decode_BIG_l),
    0x6A3E9A3D: ("filter_shape", structs.decode_BIG_l),
    0x58BDBD7B: ("filter_stage", structs.decode_BIG_l),
    0x3FDC4B2E: ("which_filter_group", structs.decode_BIG_l),
    0x37C7D09D: ("color", _decode_color),
    0xABD41A36: ("interpolate_in_time", structs.decode_BIG_f),
    0x3EAF78FE: ("interpolate_out_time", structs.decode_BIG_f),
    0xD1F65872: ("texture", structs.decode_BIG_Q),
    0xC27FFA8F: ("model", structs.decode_BIG_Q),
}
