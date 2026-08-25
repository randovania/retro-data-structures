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
from retro_data_structures.properties.common.archetypes.SplineType import SplineType
from retro_data_structures.properties.echoes.archetypes.SpindleCameraStruct import SpindleCameraStruct
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SpindleCameraJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags_spindle_camera: int
        spindle_camera_struct_0xe56495fb: json_util.JsonObject
        spindle_camera_struct_0x239debfc: json_util.JsonObject
        spindle_camera_struct_0x27e8d703: json_util.JsonObject
        spindle_camera_struct_0x2f914525: json_util.JsonObject
        spindle_camera_struct_0x23aa31b7: json_util.JsonObject
        spindle_camera_struct_0xe9e388af: json_util.JsonObject
        spindle_camera_struct_0xde5a2c87: json_util.JsonObject
        spindle_camera_struct_0x1b3b2394: json_util.JsonObject
        spindle_camera_struct_0xf5666b6e: json_util.JsonObject
        spindle_camera_struct_0x66c618aa: json_util.JsonObject
        spindle_camera_struct_0xb36d0fb6: json_util.JsonObject
        spindle_camera_struct_0xcbb013cb: json_util.JsonObject
        spindle_camera_struct_0x4abfb789: json_util.JsonObject
        spindle_camera_struct_0xfb6a407a: json_util.JsonObject
        spindle_camera_struct_0x3ae66f80: json_util.JsonObject
        spindle_camera_struct_0x6654ae92: json_util.JsonObject
        target_spline_type: json_util.JsonObject
        unknown_0x33b4f106: bool
        target_control_spline: json_util.JsonObject
        spline_type: json_util.JsonObject
        unknown_0x431769c6: bool


@dataclasses.dataclass()
class SpindleCamera(BaseObjectType):
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
    flags_spindle_camera: int = dataclasses.field(
        default=6400,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3BF4EBA8, original_name="FlagsSpindleCamera"),
        },
    )
    spindle_camera_struct_0xe56495fb: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xE56495FB,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x239debfc: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x239DEBFC,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x27e8d703: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x27E8D703,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x2f914525: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x2F914525,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x23aa31b7: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x23AA31B7,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0xe9e388af: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xE9E388AF,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0xde5a2c87: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xDE5A2C87,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x1b3b2394: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x1B3B2394,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0xf5666b6e: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xF5666B6E,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x66c618aa: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x66C618AA,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0xb36d0fb6: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xB36D0FB6,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0xcbb013cb: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xCBB013CB,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x4abfb789: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x4ABFB789,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0xfb6a407a: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0xFB6A407A,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x3ae66f80: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x3AE66F80,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    spindle_camera_struct_0x6654ae92: SpindleCameraStruct = dataclasses.field(
        default_factory=SpindleCameraStruct,
        metadata={
            "reflection": FieldReflection[SpindleCameraStruct](
                SpindleCameraStruct,
                id=0x6654AE92,
                original_name="SpindleCameraStruct",
                from_json=SpindleCameraStruct.from_json,
                to_json=SpindleCameraStruct.to_json,
            ),
        },
    )
    target_spline_type: SplineType = dataclasses.field(
        default_factory=SplineType,
        metadata={
            "reflection": FieldReflection[SplineType](
                SplineType,
                id=0x5604D304,
                original_name="TargetSplineType",
                from_json=SplineType.from_json,
                to_json=SplineType.to_json,
            ),
        },
    )
    unknown_0x33b4f106: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x33B4F106, original_name="Unknown"),
        },
    )
    target_control_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xC4DFBFA7,
                original_name="TargetControlSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    spline_type: SplineType = dataclasses.field(
        default_factory=SplineType,
        metadata={
            "reflection": FieldReflection[SplineType](
                SplineType,
                id=0x33E4685B,
                original_name="SplineType",
                from_json=SplineType.from_json,
                to_json=SplineType.to_json,
            ),
        },
    )
    unknown_0x431769c6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x431769C6, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SPND"

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
        if property_count != 23:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3BF4EBA8
        flags_spindle_camera = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE56495FB
        spindle_camera_struct_0xe56495fb = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x239DEBFC
        spindle_camera_struct_0x239debfc = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27E8D703
        spindle_camera_struct_0x27e8d703 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F914525
        spindle_camera_struct_0x2f914525 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23AA31B7
        spindle_camera_struct_0x23aa31b7 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9E388AF
        spindle_camera_struct_0xe9e388af = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE5A2C87
        spindle_camera_struct_0xde5a2c87 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B3B2394
        spindle_camera_struct_0x1b3b2394 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5666B6E
        spindle_camera_struct_0xf5666b6e = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66C618AA
        spindle_camera_struct_0x66c618aa = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB36D0FB6
        spindle_camera_struct_0xb36d0fb6 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCBB013CB
        spindle_camera_struct_0xcbb013cb = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ABFB789
        spindle_camera_struct_0x4abfb789 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB6A407A
        spindle_camera_struct_0xfb6a407a = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AE66F80
        spindle_camera_struct_0x3ae66f80 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6654AE92
        spindle_camera_struct_0x6654ae92 = SpindleCameraStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5604D304
        target_spline_type = SplineType.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33B4F106
        unknown_0x33b4f106 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4DFBFA7
        target_control_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33E4685B
        spline_type = SplineType.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x431769C6
        unknown_0x431769c6 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            flags_spindle_camera,
            spindle_camera_struct_0xe56495fb,
            spindle_camera_struct_0x239debfc,
            spindle_camera_struct_0x27e8d703,
            spindle_camera_struct_0x2f914525,
            spindle_camera_struct_0x23aa31b7,
            spindle_camera_struct_0xe9e388af,
            spindle_camera_struct_0xde5a2c87,
            spindle_camera_struct_0x1b3b2394,
            spindle_camera_struct_0xf5666b6e,
            spindle_camera_struct_0x66c618aa,
            spindle_camera_struct_0xb36d0fb6,
            spindle_camera_struct_0xcbb013cb,
            spindle_camera_struct_0x4abfb789,
            spindle_camera_struct_0xfb6a407a,
            spindle_camera_struct_0x3ae66f80,
            spindle_camera_struct_0x6654ae92,
            target_spline_type,
            unknown_0x33b4f106,
            target_control_spline,
            spline_type,
            unknown_0x431769c6,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x17")  # 23 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b";\xf4\xeb\xa8")  # 0x3bf4eba8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flags_spindle_camera))

        data.write(b"\xe5d\x95\xfb")  # 0xe56495fb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xe56495fb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"#\x9d\xeb\xfc")  # 0x239debfc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x239debfc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'\xe8\xd7\x03")  # 0x27e8d703
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x27e8d703.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"/\x91E%")  # 0x2f914525
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x2f914525.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"#\xaa1\xb7")  # 0x23aa31b7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x23aa31b7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe9\xe3\x88\xaf")  # 0xe9e388af
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xe9e388af.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdeZ,\x87")  # 0xde5a2c87
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xde5a2c87.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1b;#\x94")  # 0x1b3b2394
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x1b3b2394.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf5fkn")  # 0xf5666b6e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xf5666b6e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"f\xc6\x18\xaa")  # 0x66c618aa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x66c618aa.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3m\x0f\xb6")  # 0xb36d0fb6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xb36d0fb6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcb\xb0\x13\xcb")  # 0xcbb013cb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xcbb013cb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"J\xbf\xb7\x89")  # 0x4abfb789
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x4abfb789.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfbj@z")  # 0xfb6a407a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0xfb6a407a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b":\xe6o\x80")  # 0x3ae66f80
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x3ae66f80.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"fT\xae\x92")  # 0x6654ae92
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spindle_camera_struct_0x6654ae92.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"V\x04\xd3\x04")  # 0x5604d304
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.target_spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\xb4\xf1\x06")  # 0x33b4f106
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x33b4f106))

        data.write(b"\xc4\xdf\xbf\xa7")  # 0xc4dfbfa7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.target_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\xe4h[")  # 0x33e4685b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"C\x17i\xc6")  # 0x431769c6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x431769c6))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpindleCameraJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            flags_spindle_camera=json_data["flags_spindle_camera"],
            spindle_camera_struct_0xe56495fb=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xe56495fb"]
            ),
            spindle_camera_struct_0x239debfc=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x239debfc"]
            ),
            spindle_camera_struct_0x27e8d703=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x27e8d703"]
            ),
            spindle_camera_struct_0x2f914525=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x2f914525"]
            ),
            spindle_camera_struct_0x23aa31b7=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x23aa31b7"]
            ),
            spindle_camera_struct_0xe9e388af=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xe9e388af"]
            ),
            spindle_camera_struct_0xde5a2c87=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xde5a2c87"]
            ),
            spindle_camera_struct_0x1b3b2394=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x1b3b2394"]
            ),
            spindle_camera_struct_0xf5666b6e=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xf5666b6e"]
            ),
            spindle_camera_struct_0x66c618aa=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x66c618aa"]
            ),
            spindle_camera_struct_0xb36d0fb6=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xb36d0fb6"]
            ),
            spindle_camera_struct_0xcbb013cb=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xcbb013cb"]
            ),
            spindle_camera_struct_0x4abfb789=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x4abfb789"]
            ),
            spindle_camera_struct_0xfb6a407a=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0xfb6a407a"]
            ),
            spindle_camera_struct_0x3ae66f80=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x3ae66f80"]
            ),
            spindle_camera_struct_0x6654ae92=SpindleCameraStruct.from_json(
                json_data["spindle_camera_struct_0x6654ae92"]
            ),
            target_spline_type=SplineType.from_json(json_data["target_spline_type"]),
            unknown_0x33b4f106=json_data["unknown_0x33b4f106"],
            target_control_spline=Spline.from_json(json_data["target_control_spline"]),
            spline_type=SplineType.from_json(json_data["spline_type"]),
            unknown_0x431769c6=json_data["unknown_0x431769c6"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "flags_spindle_camera": self.flags_spindle_camera,
            "spindle_camera_struct_0xe56495fb": self.spindle_camera_struct_0xe56495fb.to_json(),
            "spindle_camera_struct_0x239debfc": self.spindle_camera_struct_0x239debfc.to_json(),
            "spindle_camera_struct_0x27e8d703": self.spindle_camera_struct_0x27e8d703.to_json(),
            "spindle_camera_struct_0x2f914525": self.spindle_camera_struct_0x2f914525.to_json(),
            "spindle_camera_struct_0x23aa31b7": self.spindle_camera_struct_0x23aa31b7.to_json(),
            "spindle_camera_struct_0xe9e388af": self.spindle_camera_struct_0xe9e388af.to_json(),
            "spindle_camera_struct_0xde5a2c87": self.spindle_camera_struct_0xde5a2c87.to_json(),
            "spindle_camera_struct_0x1b3b2394": self.spindle_camera_struct_0x1b3b2394.to_json(),
            "spindle_camera_struct_0xf5666b6e": self.spindle_camera_struct_0xf5666b6e.to_json(),
            "spindle_camera_struct_0x66c618aa": self.spindle_camera_struct_0x66c618aa.to_json(),
            "spindle_camera_struct_0xb36d0fb6": self.spindle_camera_struct_0xb36d0fb6.to_json(),
            "spindle_camera_struct_0xcbb013cb": self.spindle_camera_struct_0xcbb013cb.to_json(),
            "spindle_camera_struct_0x4abfb789": self.spindle_camera_struct_0x4abfb789.to_json(),
            "spindle_camera_struct_0xfb6a407a": self.spindle_camera_struct_0xfb6a407a.to_json(),
            "spindle_camera_struct_0x3ae66f80": self.spindle_camera_struct_0x3ae66f80.to_json(),
            "spindle_camera_struct_0x6654ae92": self.spindle_camera_struct_0x6654ae92.to_json(),
            "target_spline_type": self.target_spline_type.to_json(),
            "unknown_0x33b4f106": self.unknown_0x33b4f106,
            "target_control_spline": self.target_control_spline.to_json(),
            "spline_type": self.spline_type.to_json(),
            "unknown_0x431769c6": self.unknown_0x431769c6,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xe56495fb(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x239debfc(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x27e8d703(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x2f914525(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x23aa31b7(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xe9e388af(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xde5a2c87(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x1b3b2394(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xf5666b6e(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x66c618aa(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xb36d0fb6(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xcbb013cb(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x4abfb789(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0xfb6a407a(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x3ae66f80(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_spindle_camera_struct_0x6654ae92(
    data: typing.BinaryIO, game: Game, property_size: int
) -> SpindleCameraStruct:
    return SpindleCameraStruct.from_stream(data, game, property_size)


def _decode_target_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x3BF4EBA8: ("flags_spindle_camera", structs.decode_BIG_l),
    0xE56495FB: ("spindle_camera_struct_0xe56495fb", _decode_spindle_camera_struct_0xe56495fb),
    0x239DEBFC: ("spindle_camera_struct_0x239debfc", _decode_spindle_camera_struct_0x239debfc),
    0x27E8D703: ("spindle_camera_struct_0x27e8d703", _decode_spindle_camera_struct_0x27e8d703),
    0x2F914525: ("spindle_camera_struct_0x2f914525", _decode_spindle_camera_struct_0x2f914525),
    0x23AA31B7: ("spindle_camera_struct_0x23aa31b7", _decode_spindle_camera_struct_0x23aa31b7),
    0xE9E388AF: ("spindle_camera_struct_0xe9e388af", _decode_spindle_camera_struct_0xe9e388af),
    0xDE5A2C87: ("spindle_camera_struct_0xde5a2c87", _decode_spindle_camera_struct_0xde5a2c87),
    0x1B3B2394: ("spindle_camera_struct_0x1b3b2394", _decode_spindle_camera_struct_0x1b3b2394),
    0xF5666B6E: ("spindle_camera_struct_0xf5666b6e", _decode_spindle_camera_struct_0xf5666b6e),
    0x66C618AA: ("spindle_camera_struct_0x66c618aa", _decode_spindle_camera_struct_0x66c618aa),
    0xB36D0FB6: ("spindle_camera_struct_0xb36d0fb6", _decode_spindle_camera_struct_0xb36d0fb6),
    0xCBB013CB: ("spindle_camera_struct_0xcbb013cb", _decode_spindle_camera_struct_0xcbb013cb),
    0x4ABFB789: ("spindle_camera_struct_0x4abfb789", _decode_spindle_camera_struct_0x4abfb789),
    0xFB6A407A: ("spindle_camera_struct_0xfb6a407a", _decode_spindle_camera_struct_0xfb6a407a),
    0x3AE66F80: ("spindle_camera_struct_0x3ae66f80", _decode_spindle_camera_struct_0x3ae66f80),
    0x6654AE92: ("spindle_camera_struct_0x6654ae92", _decode_spindle_camera_struct_0x6654ae92),
    0x5604D304: ("target_spline_type", _decode_target_spline_type),
    0x33B4F106: ("unknown_0x33b4f106", structs.decode_BIG_bool_),
    0xC4DFBFA7: ("target_control_spline", _decode_target_control_spline),
    0x33E4685B: ("spline_type", _decode_spline_type),
    0x431769C6: ("unknown_0x431769c6", structs.decode_BIG_bool_),
}
