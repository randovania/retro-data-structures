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
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ContextSensitiveActivatorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        player_distance: float
        face_angle: float
        screen_center_distance: float
        unknown: bool
        reticule_type: int


class ReticuleType(enum.IntEnum):
    Unknown1 = 1652108937
    Unknown2 = 1286894661
    Unknown3 = 3349492343
    Unknown4 = 1604604469
    Unknown5 = 2885722417

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
class ContextSensitiveActivator(BaseObjectType):
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
    player_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3F5D0721, original_name="PlayerDistance"),
        },
    )
    face_angle: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E4A33DC, original_name="FaceAngle"),
        },
    )
    screen_center_distance: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7E3E19F, original_name="ScreenCenterDistance"),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF2E23F30, original_name="Unknown"),
        },
    )
    reticule_type: ReticuleType = dataclasses.field(
        default=ReticuleType.Unknown1,
        metadata={
            "reflection": FieldReflection[ReticuleType](
                ReticuleType,
                id=0x87A1C204,
                original_name="ReticuleType",
                from_json=ReticuleType.from_json,
                to_json=ReticuleType.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CSAT"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_ScriptContextSensitiveActivator.rso"]

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
        assert property_id == 0x3F5D0721
        player_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E4A33DC
        face_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7E3E19F
        screen_center_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2E23F30
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87A1C204
        reticule_type = ReticuleType.from_stream(data, game)

        return cls(editor_properties, player_distance, face_angle, screen_center_distance, unknown, reticule_type)

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

        data.write(b"?]\x07!")  # 0x3f5d0721
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_distance))

        data.write(b"\x1eJ3\xdc")  # 0x1e4a33dc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.face_angle))

        data.write(b"\xe7\xe3\xe1\x9f")  # 0xe7e3e19f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.screen_center_distance))

        data.write(b"\xf2\xe2?0")  # 0xf2e23f30
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b"\x87\xa1\xc2\x04")  # 0x87a1c204
        data.write(b"\x00\x04")  # size
        self.reticule_type.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ContextSensitiveActivatorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            player_distance=json_data["player_distance"],
            face_angle=json_data["face_angle"],
            screen_center_distance=json_data["screen_center_distance"],
            unknown=json_data["unknown"],
            reticule_type=ReticuleType.from_json(json_data["reticule_type"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "player_distance": self.player_distance,
            "face_angle": self.face_angle,
            "screen_center_distance": self.screen_center_distance,
            "unknown": self.unknown,
            "reticule_type": self.reticule_type.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_reticule_type(data: typing.BinaryIO, game: Game, property_size: int) -> ReticuleType:
    return ReticuleType.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x3F5D0721: ("player_distance", structs.decode_BIG_f),
    0x1E4A33DC: ("face_angle", structs.decode_BIG_f),
    0xE7E3E19F: ("screen_center_distance", structs.decode_BIG_f),
    0xF2E23F30: ("unknown", structs.decode_BIG_bool_),
    0x87A1C204: ("reticule_type", _decode_reticule_type),
}
