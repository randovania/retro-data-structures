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
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ShadowProjectorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        shadow_scale: float
        shadow_offset: json_util.JsonValue
        shadow_height: float
        shadow_alpha: float
        shadow_fade_time: float
        unknown_0xbca8b742: bool
        unknown_0x606e341c: int


@dataclasses.dataclass()
class ShadowProjector(BaseObjectType):
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
    shadow_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1D011A39, original_name="ShadowScale"),
        },
    )
    shadow_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF371ED59, original_name="ShadowOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    shadow_height: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24EC0FB0, original_name="ShadowHeight"),
        },
    )
    shadow_alpha: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E2CD38D, original_name="ShadowAlpha"),
        },
    )
    shadow_fade_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8CCF36C0, original_name="ShadowFadeTime"),
        },
    )
    unknown_0xbca8b742: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xBCA8B742, original_name="Unknown"),
        },
    )
    unknown_0x606e341c: int = dataclasses.field(
        default=128,
        metadata={
            "reflection": FieldReflection[int](int, id=0x606E341C, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SHDW"

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
        if property_count != 8:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D011A39
        shadow_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF371ED59
        shadow_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24EC0FB0
        shadow_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E2CD38D
        shadow_alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8CCF36C0
        shadow_fade_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBCA8B742
        unknown_0xbca8b742 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x606E341C
        unknown_0x606e341c = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            shadow_scale,
            shadow_offset,
            shadow_height,
            shadow_alpha,
            shadow_fade_time,
            unknown_0xbca8b742,
            unknown_0x606e341c,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1d\x01\x1a9")  # 0x1d011a39
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_scale))

        data.write(b"\xf3q\xedY")  # 0xf371ed59
        data.write(b"\x00\x0c")  # size
        self.shadow_offset.to_stream(data, game)

        data.write(b"$\xec\x0f\xb0")  # 0x24ec0fb0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_height))

        data.write(b">,\xd3\x8d")  # 0x3e2cd38d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_alpha))

        data.write(b"\x8c\xcf6\xc0")  # 0x8ccf36c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_fade_time))

        data.write(b"\xbc\xa8\xb7B")  # 0xbca8b742
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbca8b742))

        data.write(b"`n4\x1c")  # 0x606e341c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x606e341c))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShadowProjectorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            shadow_scale=json_data["shadow_scale"],
            shadow_offset=Vector.from_json(json_data["shadow_offset"]),
            shadow_height=json_data["shadow_height"],
            shadow_alpha=json_data["shadow_alpha"],
            shadow_fade_time=json_data["shadow_fade_time"],
            unknown_0xbca8b742=json_data["unknown_0xbca8b742"],
            unknown_0x606e341c=json_data["unknown_0x606e341c"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "shadow_scale": self.shadow_scale,
            "shadow_offset": self.shadow_offset.to_json(),
            "shadow_height": self.shadow_height,
            "shadow_alpha": self.shadow_alpha,
            "shadow_fade_time": self.shadow_fade_time,
            "unknown_0xbca8b742": self.unknown_0xbca8b742,
            "unknown_0x606e341c": self.unknown_0x606e341c,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_shadow_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x1D011A39: ("shadow_scale", structs.decode_BIG_f),
    0xF371ED59: ("shadow_offset", _decode_shadow_offset),
    0x24EC0FB0: ("shadow_height", structs.decode_BIG_f),
    0x3E2CD38D: ("shadow_alpha", structs.decode_BIG_f),
    0x8CCF36C0: ("shadow_fade_time", structs.decode_BIG_f),
    0xBCA8B742: ("unknown_0xbca8b742", structs.decode_BIG_bool_),
    0x606E341C: ("unknown_0x606e341c", structs.decode_BIG_l),
}
