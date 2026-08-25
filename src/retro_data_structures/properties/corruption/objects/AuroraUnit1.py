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
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.AuroraUnit1Data import AuroraUnit1Data
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class AuroraUnit1Json(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        aurora_unit1_data_0x93aedac3: json_util.JsonObject
        aurora_unit1_data_0x867ab15e: json_util.JsonObject
        aurora_unit1_data_0xb3c5f11b: json_util.JsonObject


@dataclasses.dataclass()
class AuroraUnit1(BaseObjectType):
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
    patterned: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0xB3774750,
                original_name="Patterned",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    aurora_unit1_data_0x93aedac3: AuroraUnit1Data = dataclasses.field(
        default_factory=AuroraUnit1Data,
        metadata={
            "reflection": FieldReflection[AuroraUnit1Data](
                AuroraUnit1Data,
                id=0x93AEDAC3,
                original_name="AuroraUnit1Data",
                from_json=AuroraUnit1Data.from_json,
                to_json=AuroraUnit1Data.to_json,
            ),
        },
    )
    aurora_unit1_data_0x867ab15e: AuroraUnit1Data = dataclasses.field(
        default_factory=AuroraUnit1Data,
        metadata={
            "reflection": FieldReflection[AuroraUnit1Data](
                AuroraUnit1Data,
                id=0x867AB15E,
                original_name="AuroraUnit1Data",
                from_json=AuroraUnit1Data.from_json,
                to_json=AuroraUnit1Data.to_json,
            ),
        },
    )
    aurora_unit1_data_0xb3c5f11b: AuroraUnit1Data = dataclasses.field(
        default_factory=AuroraUnit1Data,
        metadata={
            "reflection": FieldReflection[AuroraUnit1Data](
                AuroraUnit1Data,
                id=0xB3C5F11B,
                original_name="AuroraUnit1Data",
                from_json=AuroraUnit1Data.from_json,
                to_json=AuroraUnit1Data.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "AUR1"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_AuroraUnit1.rso"]

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
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={"turn_speed": 360.0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93AEDAC3
        aurora_unit1_data_0x93aedac3 = AuroraUnit1Data.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x867AB15E
        aurora_unit1_data_0x867ab15e = AuroraUnit1Data.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3C5F11B
        aurora_unit1_data_0xb3c5f11b = AuroraUnit1Data.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            patterned,
            actor_information,
            aurora_unit1_data_0x93aedac3,
            aurora_unit1_data_0x867ab15e,
            aurora_unit1_data_0xb3c5f11b,
        )

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

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(data, game, default_override={"turn_speed": 360.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x93\xae\xda\xc3")  # 0x93aedac3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.aurora_unit1_data_0x93aedac3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x86z\xb1^")  # 0x867ab15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.aurora_unit1_data_0x867ab15e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3\xc5\xf1\x1b")  # 0xb3c5f11b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.aurora_unit1_data_0xb3c5f11b.to_stream(data, game)
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
        json_data = typing.cast("AuroraUnit1Json", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            aurora_unit1_data_0x93aedac3=AuroraUnit1Data.from_json(json_data["aurora_unit1_data_0x93aedac3"]),
            aurora_unit1_data_0x867ab15e=AuroraUnit1Data.from_json(json_data["aurora_unit1_data_0x867ab15e"]),
            aurora_unit1_data_0xb3c5f11b=AuroraUnit1Data.from_json(json_data["aurora_unit1_data_0xb3c5f11b"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "aurora_unit1_data_0x93aedac3": self.aurora_unit1_data_0x93aedac3.to_json(),
            "aurora_unit1_data_0x867ab15e": self.aurora_unit1_data_0x867ab15e.to_json(),
            "aurora_unit1_data_0xb3c5f11b": self.aurora_unit1_data_0xb3c5f11b.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={"turn_speed": 360.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_aurora_unit1_data_0x93aedac3(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit1Data:
    return AuroraUnit1Data.from_stream(data, game, property_size)


def _decode_aurora_unit1_data_0x867ab15e(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit1Data:
    return AuroraUnit1Data.from_stream(data, game, property_size)


def _decode_aurora_unit1_data_0xb3c5f11b(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit1Data:
    return AuroraUnit1Data.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x93AEDAC3: ("aurora_unit1_data_0x93aedac3", _decode_aurora_unit1_data_0x93aedac3),
    0x867AB15E: ("aurora_unit1_data_0x867ab15e", _decode_aurora_unit1_data_0x867ab15e),
    0xB3C5F11B: ("aurora_unit1_data_0xb3c5f11b", _decode_aurora_unit1_data_0xb3c5f11b),
}
