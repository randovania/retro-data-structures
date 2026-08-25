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
from retro_data_structures.properties.echoes.archetypes.UnknownStruct3 import UnknownStruct3
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class AIMannedTurretJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_struct3: json_util.JsonObject
        patrol_horiz_spline: json_util.JsonObject
        patrol_vertical_spline: json_util.JsonObject


@dataclasses.dataclass()
class AIMannedTurret(BaseObjectType):
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
    unknown_struct3: UnknownStruct3 = dataclasses.field(
        default_factory=UnknownStruct3,
        metadata={
            "reflection": FieldReflection[UnknownStruct3](
                UnknownStruct3,
                id=0xB15DEC6F,
                original_name="UnknownStruct3",
                from_json=UnknownStruct3.from_json,
                to_json=UnknownStruct3.to_json,
            ),
        },
    )
    patrol_horiz_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x260792CF,
                original_name="PatrolHorizSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    patrol_vertical_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x84284B1C,
                original_name="PatrolVerticalSpline",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "AIMT"

    @classmethod
    def modules(cls) -> list[str]:
        return ["AIMannedTurret.rel"]

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
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={"active": False})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB15DEC6F
        unknown_struct3 = UnknownStruct3.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x260792CF
        patrol_horiz_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84284B1C
        patrol_vertical_spline = Spline.from_stream(data, game, property_size)

        return cls(editor_properties, unknown_struct3, patrol_horiz_spline, patrol_vertical_spline)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={"active": False})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb1]\xeco")  # 0xb15dec6f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&\x07\x92\xcf")  # 0x260792cf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patrol_horiz_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x84(K\x1c")  # 0x84284b1c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patrol_vertical_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AIMannedTurretJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_struct3=UnknownStruct3.from_json(json_data["unknown_struct3"]),
            patrol_horiz_spline=Spline.from_json(json_data["patrol_horiz_spline"]),
            patrol_vertical_spline=Spline.from_json(json_data["patrol_vertical_spline"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_struct3": self.unknown_struct3.to_json(),
            "patrol_horiz_spline": self.patrol_horiz_spline.to_json(),
            "patrol_vertical_spline": self.patrol_vertical_spline.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self.unknown_struct3.dependencies_for(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={"active": False})


def _decode_unknown_struct3(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct3:
    return UnknownStruct3.from_stream(data, game, property_size)


def _decode_patrol_horiz_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_patrol_vertical_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB15DEC6F: ("unknown_struct3", _decode_unknown_struct3),
    0x260792CF: ("patrol_horiz_spline", _decode_patrol_horiz_spline),
    0x84284B1C: ("patrol_vertical_spline", _decode_patrol_vertical_spline),
}
