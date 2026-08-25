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
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class HUDHintJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        hud_texture: int
        unknown_0x6078a651: float
        unknown_0xf00bb6bb: float
        icon_scale: float
        animation_time: float
        animation_frames: int
        unknown_0xd993f97b: int


@dataclasses.dataclass()
class HUDHint(BaseObjectType):
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
    hud_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD80447E0, original_name="HudTexture"),
        },
    )
    unknown_0x6078a651: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6078A651, original_name="Unknown"),
        },
    )
    unknown_0xf00bb6bb: float = dataclasses.field(
        default=16.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF00BB6BB, original_name="Unknown"),
        },
    )
    icon_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AD247A1, original_name="IconScale"),
        },
    )
    animation_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2A53245A, original_name="AnimationTime"),
        },
    )
    animation_frames: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6E88D6AD, original_name="AnimationFrames"),
        },
    )
    unknown_0xd993f97b: int = dataclasses.field(
        default=15,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD993F97B, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "HHNT"

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
        assert property_id == 0xD80447E0
        hud_texture = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6078A651
        unknown_0x6078a651 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF00BB6BB
        unknown_0xf00bb6bb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AD247A1
        icon_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2A53245A
        animation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E88D6AD
        animation_frames = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD993F97B
        unknown_0xd993f97b = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            hud_texture,
            unknown_0x6078a651,
            unknown_0xf00bb6bb,
            icon_scale,
            animation_time,
            animation_frames,
            unknown_0xd993f97b,
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

        data.write(b"\xd8\x04G\xe0")  # 0xd80447e0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.hud_texture))

        data.write(b"`x\xa6Q")  # 0x6078a651
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6078a651))

        data.write(b"\xf0\x0b\xb6\xbb")  # 0xf00bb6bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf00bb6bb))

        data.write(b"\x1a\xd2G\xa1")  # 0x1ad247a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.icon_scale))

        data.write(b"*S$Z")  # 0x2a53245a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.animation_time))

        data.write(b"n\x88\xd6\xad")  # 0x6e88d6ad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.animation_frames))

        data.write(b"\xd9\x93\xf9{")  # 0xd993f97b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd993f97b))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("HUDHintJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            hud_texture=json_data["hud_texture"],
            unknown_0x6078a651=json_data["unknown_0x6078a651"],
            unknown_0xf00bb6bb=json_data["unknown_0xf00bb6bb"],
            icon_scale=json_data["icon_scale"],
            animation_time=json_data["animation_time"],
            animation_frames=json_data["animation_frames"],
            unknown_0xd993f97b=json_data["unknown_0xd993f97b"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "hud_texture": self.hud_texture,
            "unknown_0x6078a651": self.unknown_0x6078a651,
            "unknown_0xf00bb6bb": self.unknown_0xf00bb6bb,
            "icon_scale": self.icon_scale,
            "animation_time": self.animation_time,
            "animation_frames": self.animation_frames,
            "unknown_0xd993f97b": self.unknown_0xd993f97b,
        }

    def _dependencies_for_hud_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hud_texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_hud_texture(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xD80447E0: ("hud_texture", structs.decode_BIG_L),
    0x6078A651: ("unknown_0x6078a651", structs.decode_BIG_f),
    0xF00BB6BB: ("unknown_0xf00bb6bb", structs.decode_BIG_f),
    0x1AD247A1: ("icon_scale", structs.decode_BIG_f),
    0x2A53245A: ("animation_time", structs.decode_BIG_f),
    0x6E88D6AD: ("animation_frames", structs.decode_BIG_l),
    0xD993F97B: ("unknown_0xd993f97b", structs.decode_BIG_l),
}
