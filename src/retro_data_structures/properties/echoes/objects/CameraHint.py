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
from retro_data_structures.properties.echoes.archetypes.CameraHintStructA import CameraHintStructA
from retro_data_structures.properties.echoes.archetypes.CameraHintStructB import CameraHintStructB
from retro_data_structures.properties.echoes.archetypes.CameraHintStructC import CameraHintStructC
from retro_data_structures.properties.echoes.archetypes.UnknownStruct4 import UnknownStruct4
from retro_data_structures.properties.echoes.archetypes.UnknownStruct5 import UnknownStruct5
from retro_data_structures.properties.echoes.archetypes.UnknownStruct6 import UnknownStruct6
from retro_data_structures.properties.echoes.archetypes.UnknownStruct7 import UnknownStruct7
from retro_data_structures.properties.echoes.archetypes.UnknownStruct8 import UnknownStruct8
from retro_data_structures.properties.echoes.archetypes.UnknownStruct9 import UnknownStruct9
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraHintJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        priority: int
        timer: float
        unknown_struct4: json_util.JsonObject
        flags_camera_hint: int
        camera_hint_struct_a_0x456d05c6: json_util.JsonObject
        camera_hint_struct_a_0xf5521ffa: json_util.JsonObject
        camera_hint_struct_a_0x89658a06: json_util.JsonObject
        unknown_struct5: json_util.JsonObject
        world_offset: json_util.JsonValue
        unknown_struct6: json_util.JsonObject
        camera_hint_struct_b_0x664c450a: json_util.JsonObject
        camera_hint_struct_b_0xc82395fa: json_util.JsonObject
        unknown_struct7: json_util.JsonObject
        unknown_struct8: json_util.JsonObject
        unknown_0x2ae08be1: float
        unknown_0x4361d075: float
        unknown_0xc91ef813: float
        camera_hint_struct_a1: json_util.JsonObject
        unknown_struct9: json_util.JsonObject
        camera_hint_struct_a_0x138729a7: json_util.JsonObject


@dataclasses.dataclass()
class CameraHint(BaseObjectType):
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
    priority: int = dataclasses.field(
        default=50,
        metadata={
            "reflection": FieldReflection[int](int, id=0x42087650, original_name="Priority"),
        },
    )
    timer: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8747552E, original_name="Timer"),
        },
    )
    unknown_struct4: UnknownStruct4 = dataclasses.field(
        default_factory=UnknownStruct4,
        metadata={
            "reflection": FieldReflection[UnknownStruct4](
                UnknownStruct4,
                id=0x380585EC,
                original_name="UnknownStruct4",
                from_json=UnknownStruct4.from_json,
                to_json=UnknownStruct4.to_json,
            ),
        },
    )
    flags_camera_hint: int = dataclasses.field(
        default=286,
        metadata={
            "reflection": FieldReflection[int](int, id=0x21D720A9, original_name="FlagsCameraHint"),
        },
    )
    camera_hint_struct_a_0x456d05c6: CameraHintStructB = dataclasses.field(
        default_factory=CameraHintStructB,
        metadata={
            "reflection": FieldReflection[CameraHintStructB](
                CameraHintStructB,
                id=0x456D05C6,
                original_name="CameraHintStructA",
                from_json=CameraHintStructB.from_json,
                to_json=CameraHintStructB.to_json,
            ),
        },
    )
    camera_hint_struct_a_0xf5521ffa: CameraHintStructB = dataclasses.field(
        default_factory=CameraHintStructB,
        metadata={
            "reflection": FieldReflection[CameraHintStructB](
                CameraHintStructB,
                id=0xF5521FFA,
                original_name="CameraHintStructA",
                from_json=CameraHintStructB.from_json,
                to_json=CameraHintStructB.to_json,
            ),
        },
    )
    camera_hint_struct_a_0x89658a06: CameraHintStructB = dataclasses.field(
        default_factory=CameraHintStructB,
        metadata={
            "reflection": FieldReflection[CameraHintStructB](
                CameraHintStructB,
                id=0x89658A06,
                original_name="CameraHintStructA",
                from_json=CameraHintStructB.from_json,
                to_json=CameraHintStructB.to_json,
            ),
        },
    )
    unknown_struct5: UnknownStruct5 = dataclasses.field(
        default_factory=UnknownStruct5,
        metadata={
            "reflection": FieldReflection[UnknownStruct5](
                UnknownStruct5,
                id=0x8D0A9113,
                original_name="UnknownStruct5",
                from_json=UnknownStruct5.from_json,
                to_json=UnknownStruct5.to_json,
            ),
        },
    )
    world_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xEFEBE838, original_name="WorldOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_struct6: UnknownStruct6 = dataclasses.field(
        default_factory=UnknownStruct6,
        metadata={
            "reflection": FieldReflection[UnknownStruct6](
                UnknownStruct6,
                id=0xF71C36F2,
                original_name="UnknownStruct6",
                from_json=UnknownStruct6.from_json,
                to_json=UnknownStruct6.to_json,
            ),
        },
    )
    camera_hint_struct_b_0x664c450a: CameraHintStructC = dataclasses.field(
        default_factory=CameraHintStructC,
        metadata={
            "reflection": FieldReflection[CameraHintStructC](
                CameraHintStructC,
                id=0x664C450A,
                original_name="CameraHintStructB",
                from_json=CameraHintStructC.from_json,
                to_json=CameraHintStructC.to_json,
            ),
        },
    )
    camera_hint_struct_b_0xc82395fa: CameraHintStructC = dataclasses.field(
        default_factory=CameraHintStructC,
        metadata={
            "reflection": FieldReflection[CameraHintStructC](
                CameraHintStructC,
                id=0xC82395FA,
                original_name="CameraHintStructB",
                from_json=CameraHintStructC.from_json,
                to_json=CameraHintStructC.to_json,
            ),
        },
    )
    unknown_struct7: UnknownStruct7 = dataclasses.field(
        default_factory=UnknownStruct7,
        metadata={
            "reflection": FieldReflection[UnknownStruct7](
                UnknownStruct7,
                id=0x645EB009,
                original_name="UnknownStruct7",
                from_json=UnknownStruct7.from_json,
                to_json=UnknownStruct7.to_json,
            ),
        },
    )
    unknown_struct8: UnknownStruct8 = dataclasses.field(
        default_factory=UnknownStruct8,
        metadata={
            "reflection": FieldReflection[UnknownStruct8](
                UnknownStruct8,
                id=0x80CFBB54,
                original_name="UnknownStruct8",
                from_json=UnknownStruct8.from_json,
                to_json=UnknownStruct8.to_json,
            ),
        },
    )
    unknown_0x2ae08be1: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2AE08BE1, original_name="Unknown"),
        },
    )
    unknown_0x4361d075: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4361D075, original_name="Unknown"),
        },
    )
    unknown_0xc91ef813: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC91EF813, original_name="Unknown"),
        },
    )
    camera_hint_struct_a1: CameraHintStructA = dataclasses.field(
        default_factory=CameraHintStructA,
        metadata={
            "reflection": FieldReflection[CameraHintStructA](
                CameraHintStructA,
                id=0x934E392C,
                original_name="CameraHintStructA1",
                from_json=CameraHintStructA.from_json,
                to_json=CameraHintStructA.to_json,
            ),
        },
    )
    unknown_struct9: UnknownStruct9 = dataclasses.field(
        default_factory=UnknownStruct9,
        metadata={
            "reflection": FieldReflection[UnknownStruct9](
                UnknownStruct9,
                id=0x9E8631F1,
                original_name="UnknownStruct9",
                from_json=UnknownStruct9.from_json,
                to_json=UnknownStruct9.to_json,
            ),
        },
    )
    camera_hint_struct_a_0x138729a7: CameraHintStructA = dataclasses.field(
        default_factory=CameraHintStructA,
        metadata={
            "reflection": FieldReflection[CameraHintStructA](
                CameraHintStructA,
                id=0x138729A7,
                original_name="CameraHintStructA",
                from_json=CameraHintStructA.from_json,
                to_json=CameraHintStructA.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CAMH"

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
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42087650
        priority = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8747552E
        timer = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x380585EC
        unknown_struct4 = UnknownStruct4.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21D720A9
        flags_camera_hint = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x456D05C6
        camera_hint_struct_a_0x456d05c6 = CameraHintStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5521FFA
        camera_hint_struct_a_0xf5521ffa = CameraHintStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89658A06
        camera_hint_struct_a_0x89658a06 = CameraHintStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D0A9113
        unknown_struct5 = UnknownStruct5.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEFEBE838
        world_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF71C36F2
        unknown_struct6 = UnknownStruct6.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x664C450A
        camera_hint_struct_b_0x664c450a = CameraHintStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC82395FA
        camera_hint_struct_b_0xc82395fa = CameraHintStructC.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x645EB009
        unknown_struct7 = UnknownStruct7.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80CFBB54
        unknown_struct8 = UnknownStruct8.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AE08BE1
        unknown_0x2ae08be1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4361D075
        unknown_0x4361d075 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC91EF813
        unknown_0xc91ef813 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x934E392C
        camera_hint_struct_a1 = CameraHintStructA.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9E8631F1
        unknown_struct9 = UnknownStruct9.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x138729A7
        camera_hint_struct_a_0x138729a7 = CameraHintStructA.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            priority,
            timer,
            unknown_struct4,
            flags_camera_hint,
            camera_hint_struct_a_0x456d05c6,
            camera_hint_struct_a_0xf5521ffa,
            camera_hint_struct_a_0x89658a06,
            unknown_struct5,
            world_offset,
            unknown_struct6,
            camera_hint_struct_b_0x664c450a,
            camera_hint_struct_b_0xc82395fa,
            unknown_struct7,
            unknown_struct8,
            unknown_0x2ae08be1,
            unknown_0x4361d075,
            unknown_0xc91ef813,
            camera_hint_struct_a1,
            unknown_struct9,
            camera_hint_struct_a_0x138729a7,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"B\x08vP")  # 0x42087650
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.priority))

        data.write(b"\x87GU.")  # 0x8747552e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.timer))

        data.write(b"8\x05\x85\xec")  # 0x380585ec
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"!\xd7 \xa9")  # 0x21d720a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flags_camera_hint))

        data.write(b"Em\x05\xc6")  # 0x456d05c6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_a_0x456d05c6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf5R\x1f\xfa")  # 0xf5521ffa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_a_0xf5521ffa.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x89e\x8a\x06")  # 0x89658a06
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_a_0x89658a06.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8d\n\x91\x13")  # 0x8d0a9113
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xef\xeb\xe88")  # 0xefebe838
        data.write(b"\x00\x0c")  # size
        self.world_offset.to_stream(data, game)

        data.write(b"\xf7\x1c6\xf2")  # 0xf71c36f2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"fLE\n")  # 0x664c450a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_b_0x664c450a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc8#\x95\xfa")  # 0xc82395fa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_b_0xc82395fa.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"d^\xb0\t")  # 0x645eb009
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x80\xcf\xbbT")  # 0x80cfbb54
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct8.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"*\xe0\x8b\xe1")  # 0x2ae08be1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2ae08be1))

        data.write(b"Ca\xd0u")  # 0x4361d075
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4361d075))

        data.write(b"\xc9\x1e\xf8\x13")  # 0xc91ef813
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc91ef813))

        data.write(b"\x93N9,")  # 0x934e392c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_a1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9e\x861\xf1")  # 0x9e8631f1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x13\x87)\xa7")  # 0x138729a7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_hint_struct_a_0x138729a7.to_stream(data, game)
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
        json_data = typing.cast("CameraHintJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            priority=json_data["priority"],
            timer=json_data["timer"],
            unknown_struct4=UnknownStruct4.from_json(json_data["unknown_struct4"]),
            flags_camera_hint=json_data["flags_camera_hint"],
            camera_hint_struct_a_0x456d05c6=CameraHintStructB.from_json(json_data["camera_hint_struct_a_0x456d05c6"]),
            camera_hint_struct_a_0xf5521ffa=CameraHintStructB.from_json(json_data["camera_hint_struct_a_0xf5521ffa"]),
            camera_hint_struct_a_0x89658a06=CameraHintStructB.from_json(json_data["camera_hint_struct_a_0x89658a06"]),
            unknown_struct5=UnknownStruct5.from_json(json_data["unknown_struct5"]),
            world_offset=Vector.from_json(json_data["world_offset"]),
            unknown_struct6=UnknownStruct6.from_json(json_data["unknown_struct6"]),
            camera_hint_struct_b_0x664c450a=CameraHintStructC.from_json(json_data["camera_hint_struct_b_0x664c450a"]),
            camera_hint_struct_b_0xc82395fa=CameraHintStructC.from_json(json_data["camera_hint_struct_b_0xc82395fa"]),
            unknown_struct7=UnknownStruct7.from_json(json_data["unknown_struct7"]),
            unknown_struct8=UnknownStruct8.from_json(json_data["unknown_struct8"]),
            unknown_0x2ae08be1=json_data["unknown_0x2ae08be1"],
            unknown_0x4361d075=json_data["unknown_0x4361d075"],
            unknown_0xc91ef813=json_data["unknown_0xc91ef813"],
            camera_hint_struct_a1=CameraHintStructA.from_json(json_data["camera_hint_struct_a1"]),
            unknown_struct9=UnknownStruct9.from_json(json_data["unknown_struct9"]),
            camera_hint_struct_a_0x138729a7=CameraHintStructA.from_json(json_data["camera_hint_struct_a_0x138729a7"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "priority": self.priority,
            "timer": self.timer,
            "unknown_struct4": self.unknown_struct4.to_json(),
            "flags_camera_hint": self.flags_camera_hint,
            "camera_hint_struct_a_0x456d05c6": self.camera_hint_struct_a_0x456d05c6.to_json(),
            "camera_hint_struct_a_0xf5521ffa": self.camera_hint_struct_a_0xf5521ffa.to_json(),
            "camera_hint_struct_a_0x89658a06": self.camera_hint_struct_a_0x89658a06.to_json(),
            "unknown_struct5": self.unknown_struct5.to_json(),
            "world_offset": self.world_offset.to_json(),
            "unknown_struct6": self.unknown_struct6.to_json(),
            "camera_hint_struct_b_0x664c450a": self.camera_hint_struct_b_0x664c450a.to_json(),
            "camera_hint_struct_b_0xc82395fa": self.camera_hint_struct_b_0xc82395fa.to_json(),
            "unknown_struct7": self.unknown_struct7.to_json(),
            "unknown_struct8": self.unknown_struct8.to_json(),
            "unknown_0x2ae08be1": self.unknown_0x2ae08be1,
            "unknown_0x4361d075": self.unknown_0x4361d075,
            "unknown_0xc91ef813": self.unknown_0xc91ef813,
            "camera_hint_struct_a1": self.camera_hint_struct_a1.to_json(),
            "unknown_struct9": self.unknown_struct9.to_json(),
            "camera_hint_struct_a_0x138729a7": self.camera_hint_struct_a_0x138729a7.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_unknown_struct4(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct4:
    return UnknownStruct4.from_stream(data, game, property_size)


def _decode_camera_hint_struct_a_0x456d05c6(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructB:
    return CameraHintStructB.from_stream(data, game, property_size)


def _decode_camera_hint_struct_a_0xf5521ffa(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructB:
    return CameraHintStructB.from_stream(data, game, property_size)


def _decode_camera_hint_struct_a_0x89658a06(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructB:
    return CameraHintStructB.from_stream(data, game, property_size)


def _decode_unknown_struct5(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct5:
    return UnknownStruct5.from_stream(data, game, property_size)


def _decode_world_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_struct6(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct6:
    return UnknownStruct6.from_stream(data, game, property_size)


def _decode_camera_hint_struct_b_0x664c450a(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructC:
    return CameraHintStructC.from_stream(data, game, property_size)


def _decode_camera_hint_struct_b_0xc82395fa(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructC:
    return CameraHintStructC.from_stream(data, game, property_size)


def _decode_unknown_struct7(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct7:
    return UnknownStruct7.from_stream(data, game, property_size)


def _decode_unknown_struct8(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct8:
    return UnknownStruct8.from_stream(data, game, property_size)


def _decode_camera_hint_struct_a1(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructA:
    return CameraHintStructA.from_stream(data, game, property_size)


def _decode_unknown_struct9(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct9:
    return UnknownStruct9.from_stream(data, game, property_size)


def _decode_camera_hint_struct_a_0x138729a7(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintStructA:
    return CameraHintStructA.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x42087650: ("priority", structs.decode_BIG_l),
    0x8747552E: ("timer", structs.decode_BIG_f),
    0x380585EC: ("unknown_struct4", _decode_unknown_struct4),
    0x21D720A9: ("flags_camera_hint", structs.decode_BIG_l),
    0x456D05C6: ("camera_hint_struct_a_0x456d05c6", _decode_camera_hint_struct_a_0x456d05c6),
    0xF5521FFA: ("camera_hint_struct_a_0xf5521ffa", _decode_camera_hint_struct_a_0xf5521ffa),
    0x89658A06: ("camera_hint_struct_a_0x89658a06", _decode_camera_hint_struct_a_0x89658a06),
    0x8D0A9113: ("unknown_struct5", _decode_unknown_struct5),
    0xEFEBE838: ("world_offset", _decode_world_offset),
    0xF71C36F2: ("unknown_struct6", _decode_unknown_struct6),
    0x664C450A: ("camera_hint_struct_b_0x664c450a", _decode_camera_hint_struct_b_0x664c450a),
    0xC82395FA: ("camera_hint_struct_b_0xc82395fa", _decode_camera_hint_struct_b_0xc82395fa),
    0x645EB009: ("unknown_struct7", _decode_unknown_struct7),
    0x80CFBB54: ("unknown_struct8", _decode_unknown_struct8),
    0x2AE08BE1: ("unknown_0x2ae08be1", structs.decode_BIG_f),
    0x4361D075: ("unknown_0x4361d075", structs.decode_BIG_f),
    0xC91EF813: ("unknown_0xc91ef813", structs.decode_BIG_f),
    0x934E392C: ("camera_hint_struct_a1", _decode_camera_hint_struct_a1),
    0x9E8631F1: ("unknown_struct9", _decode_unknown_struct9),
    0x138729A7: ("camera_hint_struct_a_0x138729a7", _decode_camera_hint_struct_a_0x138729a7),
}
