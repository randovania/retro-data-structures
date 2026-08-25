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

    class RainSplashJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        splash_scale: float
        max_splashes: int
        generation_rate: int
        start_height: float
        alpha_factor: float


@dataclasses.dataclass()
class RainSplash(BaseObjectType):
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
    splash_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08231AC9, original_name="SplashScale"),
        },
    )
    max_splashes: int = dataclasses.field(
        default=20,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6248AA06, original_name="MaxSplashes"),
        },
    )
    generation_rate: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7F5A86DD, original_name="GenerationRate"),
        },
    )
    start_height: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC40527F6, original_name="StartHeight"),
        },
    )
    alpha_factor: float = dataclasses.field(
        default=0.125,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE04E0270, original_name="AlphaFactor"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "RSPL"

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
        assert property_id == 0x08231AC9
        splash_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6248AA06
        max_splashes = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F5A86DD
        generation_rate = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC40527F6
        start_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE04E0270
        alpha_factor = structs.BIG_f.unpack(data.read(4))[0]

        return cls(editor_properties, splash_scale, max_splashes, generation_rate, start_height, alpha_factor)

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

        data.write(b"\x08#\x1a\xc9")  # 0x8231ac9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.splash_scale))

        data.write(b"bH\xaa\x06")  # 0x6248aa06
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_splashes))

        data.write(b"\x7fZ\x86\xdd")  # 0x7f5a86dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.generation_rate))

        data.write(b"\xc4\x05'\xf6")  # 0xc40527f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.start_height))

        data.write(b"\xe0N\x02p")  # 0xe04e0270
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alpha_factor))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RainSplashJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            splash_scale=json_data["splash_scale"],
            max_splashes=json_data["max_splashes"],
            generation_rate=json_data["generation_rate"],
            start_height=json_data["start_height"],
            alpha_factor=json_data["alpha_factor"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "splash_scale": self.splash_scale,
            "max_splashes": self.max_splashes,
            "generation_rate": self.generation_rate,
            "start_height": self.start_height,
            "alpha_factor": self.alpha_factor,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x08231AC9: ("splash_scale", structs.decode_BIG_f),
    0x6248AA06: ("max_splashes", structs.decode_BIG_l),
    0x7F5A86DD: ("generation_rate", structs.decode_BIG_l),
    0xC40527F6: ("start_height", structs.decode_BIG_f),
    0xE04E0270: ("alpha_factor", structs.decode_BIG_f),
}
