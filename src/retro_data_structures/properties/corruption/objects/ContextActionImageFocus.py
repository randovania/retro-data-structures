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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ContextActionImageFocusJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        initial_angle: float
        min_angle: float
        max_angle: float
        fudge_angle: float
        lock_angle: float
        lock_time: float
        drift_angle: float
        drift_period: float
        rotation_scale: float
        movement_distance: float
        rotation_sound: int
        animation: int


@dataclasses.dataclass()
class ContextActionImageFocus(BaseObjectType):
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
    initial_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90AC8041, original_name="InitialAngle"),
        },
    )
    min_angle: float = dataclasses.field(
        default=-90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x992C2DF5, original_name="MinAngle"),
        },
    )
    max_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD9635583, original_name="MaxAngle"),
        },
    )
    fudge_angle: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39BD0F70, original_name="FudgeAngle"),
        },
    )
    lock_angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x64EDCEF1, original_name="LockAngle"),
        },
    )
    lock_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x308EDC44, original_name="LockTime"),
        },
    )
    drift_angle: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4707233B, original_name="DriftAngle"),
        },
    )
    drift_period: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x539D3090, original_name="DriftPeriod"),
        },
    )
    rotation_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E0EE157, original_name="RotationScale"),
        },
    )
    movement_distance: float = dataclasses.field(
        default=0.07500000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A8A45FE, original_name="MovementDistance"),
        },
    )
    rotation_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD702EBD7, original_name="RotationSound"),
        },
    )
    animation: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAACDB11C, original_name="Animation"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CAIF"

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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90AC8041
        initial_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x992C2DF5
        min_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD9635583
        max_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39BD0F70
        fudge_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64EDCEF1
        lock_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x308EDC44
        lock_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4707233B
        drift_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x539D3090
        drift_period = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E0EE157
        rotation_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A8A45FE
        movement_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD702EBD7
        rotation_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAACDB11C
        animation = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            initial_angle,
            min_angle,
            max_angle,
            fudge_angle,
            lock_angle,
            lock_time,
            drift_angle,
            drift_period,
            rotation_scale,
            movement_distance,
            rotation_sound,
            animation,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\r")  # 13 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x90\xac\x80A")  # 0x90ac8041
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_angle))

        data.write(b"\x99,-\xf5")  # 0x992c2df5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_angle))

        data.write(b"\xd9cU\x83")  # 0xd9635583
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_angle))

        data.write(b"9\xbd\x0fp")  # 0x39bd0f70
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fudge_angle))

        data.write(b"d\xed\xce\xf1")  # 0x64edcef1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lock_angle))

        data.write(b"0\x8e\xdcD")  # 0x308edc44
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lock_time))

        data.write(b"G\x07#;")  # 0x4707233b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.drift_angle))

        data.write(b"S\x9d0\x90")  # 0x539d3090
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.drift_period))

        data.write(b"^\x0e\xe1W")  # 0x5e0ee157
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotation_scale))

        data.write(b"\x1a\x8aE\xfe")  # 0x1a8a45fe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_distance))

        data.write(b"\xd7\x02\xeb\xd7")  # 0xd702ebd7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.rotation_sound))

        data.write(b"\xaa\xcd\xb1\x1c")  # 0xaacdb11c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.animation))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ContextActionImageFocusJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            initial_angle=json_data["initial_angle"],
            min_angle=json_data["min_angle"],
            max_angle=json_data["max_angle"],
            fudge_angle=json_data["fudge_angle"],
            lock_angle=json_data["lock_angle"],
            lock_time=json_data["lock_time"],
            drift_angle=json_data["drift_angle"],
            drift_period=json_data["drift_period"],
            rotation_scale=json_data["rotation_scale"],
            movement_distance=json_data["movement_distance"],
            rotation_sound=json_data["rotation_sound"],
            animation=json_data["animation"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "initial_angle": self.initial_angle,
            "min_angle": self.min_angle,
            "max_angle": self.max_angle,
            "fudge_angle": self.fudge_angle,
            "lock_angle": self.lock_angle,
            "lock_time": self.lock_time,
            "drift_angle": self.drift_angle,
            "drift_period": self.drift_period,
            "rotation_scale": self.rotation_scale,
            "movement_distance": self.movement_distance,
            "rotation_sound": self.rotation_sound,
            "animation": self.animation,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x90AC8041: ("initial_angle", structs.decode_BIG_f),
    0x992C2DF5: ("min_angle", structs.decode_BIG_f),
    0xD9635583: ("max_angle", structs.decode_BIG_f),
    0x39BD0F70: ("fudge_angle", structs.decode_BIG_f),
    0x64EDCEF1: ("lock_angle", structs.decode_BIG_f),
    0x308EDC44: ("lock_time", structs.decode_BIG_f),
    0x4707233B: ("drift_angle", structs.decode_BIG_f),
    0x539D3090: ("drift_period", structs.decode_BIG_f),
    0x5E0EE157: ("rotation_scale", structs.decode_BIG_f),
    0x1A8A45FE: ("movement_distance", structs.decode_BIG_f),
    0xD702EBD7: ("rotation_sound", structs.decode_BIG_Q),
    0xAACDB11C: ("animation", structs.decode_BIG_l),
}
