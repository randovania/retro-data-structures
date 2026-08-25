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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GeneratorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        min_number_objects_to_generate: int
        max_number_objects_to_generate: int
        unique_objects: bool
        unique_locations: bool
        keep_orientation: bool
        use_originator_transform: bool
        offset: json_util.JsonValue
        offset_is_local_space: bool
        random_scale_min: float
        random_scale_max: float


@dataclasses.dataclass()
class Generator(BaseObjectType):
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
    min_number_objects_to_generate: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6BDD56D6, original_name="MinNumberObjectsToGenerate"),
        },
    )
    max_number_objects_to_generate: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x845F48AC, original_name="MaxNumberObjectsToGenerate"),
        },
    )
    unique_objects: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE4D247E4, original_name="UniqueObjects"),
        },
    )
    unique_locations: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x88978E49, original_name="UniqueLocations"),
        },
    )
    keep_orientation: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1EB8E254, original_name="KeepOrientation"),
        },
    )
    use_originator_transform: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x035A5E10, original_name="UseOriginatorTransform"),
        },
    )
    offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x46477064, original_name="Offset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    offset_is_local_space: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x72BBE7A6, original_name="OffsetIsLocalSpace"),
        },
    )
    random_scale_min: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3861B64, original_name="RandomScaleMin"),
        },
    )
    random_scale_max: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25E6B485, original_name="RandomScaleMax"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "GENR"

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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BDD56D6
        min_number_objects_to_generate = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x845F48AC
        max_number_objects_to_generate = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE4D247E4
        unique_objects = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88978E49
        unique_locations = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1EB8E254
        keep_orientation = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x035A5E10
        use_originator_transform = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46477064
        offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72BBE7A6
        offset_is_local_space = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3861B64
        random_scale_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25E6B485
        random_scale_max = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            min_number_objects_to_generate,
            max_number_objects_to_generate,
            unique_objects,
            unique_locations,
            keep_orientation,
            use_originator_transform,
            offset,
            offset_is_local_space,
            random_scale_min,
            random_scale_max,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"k\xddV\xd6")  # 0x6bdd56d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.min_number_objects_to_generate))

        data.write(b"\x84_H\xac")  # 0x845f48ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_number_objects_to_generate))

        data.write(b"\xe4\xd2G\xe4")  # 0xe4d247e4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unique_objects))

        data.write(b"\x88\x97\x8eI")  # 0x88978e49
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unique_locations))

        data.write(b"\x1e\xb8\xe2T")  # 0x1eb8e254
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.keep_orientation))

        data.write(b"\x03Z^\x10")  # 0x35a5e10
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_originator_transform))

        data.write(b"FGpd")  # 0x46477064
        data.write(b"\x00\x0c")  # size
        self.offset.to_stream(data, game)

        data.write(b"r\xbb\xe7\xa6")  # 0x72bbe7a6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.offset_is_local_space))

        data.write(b"\xc3\x86\x1bd")  # 0xc3861b64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.random_scale_min))

        data.write(b"%\xe6\xb4\x85")  # 0x25e6b485
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.random_scale_max))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GeneratorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            min_number_objects_to_generate=json_data["min_number_objects_to_generate"],
            max_number_objects_to_generate=json_data["max_number_objects_to_generate"],
            unique_objects=json_data["unique_objects"],
            unique_locations=json_data["unique_locations"],
            keep_orientation=json_data["keep_orientation"],
            use_originator_transform=json_data["use_originator_transform"],
            offset=Vector.from_json(json_data["offset"]),
            offset_is_local_space=json_data["offset_is_local_space"],
            random_scale_min=json_data["random_scale_min"],
            random_scale_max=json_data["random_scale_max"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "min_number_objects_to_generate": self.min_number_objects_to_generate,
            "max_number_objects_to_generate": self.max_number_objects_to_generate,
            "unique_objects": self.unique_objects,
            "unique_locations": self.unique_locations,
            "keep_orientation": self.keep_orientation,
            "use_originator_transform": self.use_originator_transform,
            "offset": self.offset.to_json(),
            "offset_is_local_space": self.offset_is_local_space,
            "random_scale_min": self.random_scale_min,
            "random_scale_max": self.random_scale_max,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x6BDD56D6: ("min_number_objects_to_generate", structs.decode_BIG_l),
    0x845F48AC: ("max_number_objects_to_generate", structs.decode_BIG_l),
    0xE4D247E4: ("unique_objects", structs.decode_BIG_bool_),
    0x88978E49: ("unique_locations", structs.decode_BIG_bool_),
    0x1EB8E254: ("keep_orientation", structs.decode_BIG_bool_),
    0x035A5E10: ("use_originator_transform", structs.decode_BIG_bool_),
    0x46477064: ("offset", _decode_offset),
    0x72BBE7A6: ("offset_is_local_space", structs.decode_BIG_bool_),
    0xC3861B64: ("random_scale_min", structs.decode_BIG_f),
    0x25E6B485: ("random_scale_max", structs.decode_BIG_f),
}
