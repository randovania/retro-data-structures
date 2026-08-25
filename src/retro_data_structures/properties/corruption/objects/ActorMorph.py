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

    class ActorMorphJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0xc60575f5: float
        unknown_0xe9fe0baa: float
        unknown_0x8e79a0fb: float
        unknown_0xa182dea4: float
        key_points: str
        unknown_0x8bd0e337: float
        unknown_0x39427691: bool


@dataclasses.dataclass()
class ActorMorph(BaseObjectType):
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
    unknown_0xc60575f5: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC60575F5, original_name="Unknown"),
        },
    )
    unknown_0xe9fe0baa: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9FE0BAA, original_name="Unknown"),
        },
    )
    unknown_0x8e79a0fb: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E79A0FB, original_name="Unknown"),
        },
    )
    unknown_0xa182dea4: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA182DEA4, original_name="Unknown"),
        },
    )
    key_points: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x95DEBD1B, original_name="KeyPoints"),
        },
    )
    unknown_0x8bd0e337: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8BD0E337, original_name="Unknown"),
        },
    )
    unknown_0x39427691: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x39427691, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "AMOR"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_ScriptActorMorph.rso"]

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
        assert property_id == 0xC60575F5
        unknown_0xc60575f5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9FE0BAA
        unknown_0xe9fe0baa = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E79A0FB
        unknown_0x8e79a0fb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA182DEA4
        unknown_0xa182dea4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95DEBD1B
        key_points = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8BD0E337
        unknown_0x8bd0e337 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39427691
        unknown_0x39427691 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            unknown_0xc60575f5,
            unknown_0xe9fe0baa,
            unknown_0x8e79a0fb,
            unknown_0xa182dea4,
            key_points,
            unknown_0x8bd0e337,
            unknown_0x39427691,
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

        data.write(b"\xc6\x05u\xf5")  # 0xc60575f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc60575f5))

        data.write(b"\xe9\xfe\x0b\xaa")  # 0xe9fe0baa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe9fe0baa))

        data.write(b"\x8ey\xa0\xfb")  # 0x8e79a0fb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8e79a0fb))

        data.write(b"\xa1\x82\xde\xa4")  # 0xa182dea4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa182dea4))

        data.write(b"\x95\xde\xbd\x1b")  # 0x95debd1b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.key_points.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\xd0\xe37")  # 0x8bd0e337
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8bd0e337))

        data.write(b"9Bv\x91")  # 0x39427691
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x39427691))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ActorMorphJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_0xc60575f5=json_data["unknown_0xc60575f5"],
            unknown_0xe9fe0baa=json_data["unknown_0xe9fe0baa"],
            unknown_0x8e79a0fb=json_data["unknown_0x8e79a0fb"],
            unknown_0xa182dea4=json_data["unknown_0xa182dea4"],
            key_points=json_data["key_points"],
            unknown_0x8bd0e337=json_data["unknown_0x8bd0e337"],
            unknown_0x39427691=json_data["unknown_0x39427691"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_0xc60575f5": self.unknown_0xc60575f5,
            "unknown_0xe9fe0baa": self.unknown_0xe9fe0baa,
            "unknown_0x8e79a0fb": self.unknown_0x8e79a0fb,
            "unknown_0xa182dea4": self.unknown_0xa182dea4,
            "key_points": self.key_points,
            "unknown_0x8bd0e337": self.unknown_0x8bd0e337,
            "unknown_0x39427691": self.unknown_0x39427691,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_key_points(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xC60575F5: ("unknown_0xc60575f5", structs.decode_BIG_f),
    0xE9FE0BAA: ("unknown_0xe9fe0baa", structs.decode_BIG_f),
    0x8E79A0FB: ("unknown_0x8e79a0fb", structs.decode_BIG_f),
    0xA182DEA4: ("unknown_0xa182dea4", structs.decode_BIG_f),
    0x95DEBD1B: ("key_points", _decode_key_points),
    0x8BD0E337: ("unknown_0x8bd0e337", structs.decode_BIG_f),
    0x39427691: ("unknown_0x39427691", structs.decode_BIG_bool_),
}
