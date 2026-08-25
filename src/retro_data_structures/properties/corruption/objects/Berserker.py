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
from retro_data_structures.properties.corruption.archetypes.BerserkerData import BerserkerData
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.corruption.archetypes.UnknownStruct21 import UnknownStruct21
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BerserkerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        patterned_info: json_util.JsonObject
        berserker_info: json_util.JsonObject
        berserker_info_hard: json_util.JsonObject
        berserker_info_elite: json_util.JsonObject
        unknown_struct21: json_util.JsonObject


@dataclasses.dataclass()
class Berserker(BaseObjectType):
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
    patterned_info: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x43BBB1DD,
                original_name="PatternedInfo",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    berserker_info: BerserkerData = dataclasses.field(
        default_factory=BerserkerData,
        metadata={
            "reflection": FieldReflection[BerserkerData](
                BerserkerData,
                id=0x54F9FFA5,
                original_name="BerserkerInfo",
                from_json=BerserkerData.from_json,
                to_json=BerserkerData.to_json,
            ),
        },
    )
    berserker_info_hard: BerserkerData = dataclasses.field(
        default_factory=BerserkerData,
        metadata={
            "reflection": FieldReflection[BerserkerData](
                BerserkerData,
                id=0x2D8DC0AF,
                original_name="BerserkerInfoHard",
                from_json=BerserkerData.from_json,
                to_json=BerserkerData.to_json,
            ),
        },
    )
    berserker_info_elite: BerserkerData = dataclasses.field(
        default_factory=BerserkerData,
        metadata={
            "reflection": FieldReflection[BerserkerData](
                BerserkerData,
                id=0xE10CE828,
                original_name="BerserkerInfoElite",
                from_json=BerserkerData.from_json,
                to_json=BerserkerData.to_json,
            ),
        },
    )
    unknown_struct21: UnknownStruct21 = dataclasses.field(
        default_factory=UnknownStruct21,
        metadata={
            "reflection": FieldReflection[UnknownStruct21](
                UnknownStruct21,
                id=0x7B8C48C7,
                original_name="UnknownStruct21",
                from_json=UnknownStruct21.from_json,
                to_json=UnknownStruct21.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "BSKR"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_Berserker.rso"]

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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43BBB1DD
        patterned_info = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "damage_wait_time": 3.0,
                "step_up_height": 1.0,
                "creature_size": 2,
                "turn_speed": 180.0,
                "detection_range": 50.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "average_attack_time": 1.0,
                "attack_time_variation": 0.5,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54F9FFA5
        berserker_info = BerserkerData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D8DC0AF
        berserker_info_hard = BerserkerData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE10CE828
        berserker_info_elite = BerserkerData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B8C48C7
        unknown_struct21 = UnknownStruct21.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            actor_information,
            patterned_info,
            berserker_info,
            berserker_info_hard,
            berserker_info_elite,
            unknown_struct21,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
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

        data.write(b"C\xbb\xb1\xdd")  # 0x43bbb1dd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned_info.to_stream(
            data,
            game,
            default_override={
                "damage_wait_time": 3.0,
                "step_up_height": 1.0,
                "creature_size": 2,
                "turn_speed": 180.0,
                "detection_range": 50.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "average_attack_time": 1.0,
                "attack_time_variation": 0.5,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"T\xf9\xff\xa5")  # 0x54f9ffa5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.berserker_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"-\x8d\xc0\xaf")  # 0x2d8dc0af
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.berserker_info_hard.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe1\x0c\xe8(")  # 0xe10ce828
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.berserker_info_elite.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{\x8cH\xc7")  # 0x7b8c48c7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct21.to_stream(data, game)
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
        json_data = typing.cast("BerserkerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            patterned_info=PatternedAITypedef.from_json(json_data["patterned_info"]),
            berserker_info=BerserkerData.from_json(json_data["berserker_info"]),
            berserker_info_hard=BerserkerData.from_json(json_data["berserker_info_hard"]),
            berserker_info_elite=BerserkerData.from_json(json_data["berserker_info_elite"]),
            unknown_struct21=UnknownStruct21.from_json(json_data["unknown_struct21"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "patterned_info": self.patterned_info.to_json(),
            "berserker_info": self.berserker_info.to_json(),
            "berserker_info_hard": self.berserker_info_hard.to_json(),
            "berserker_info_elite": self.berserker_info_elite.to_json(),
            "unknown_struct21": self.unknown_struct21.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_patterned_info(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "damage_wait_time": 3.0,
            "step_up_height": 1.0,
            "creature_size": 2,
            "turn_speed": 180.0,
            "detection_range": 50.0,
            "detection_angle": 90.0,
            "min_attack_range": 4.0,
            "average_attack_time": 1.0,
            "attack_time_variation": 0.5,
        },
    )


def _decode_berserker_info(data: typing.BinaryIO, game: Game, property_size: int) -> BerserkerData:
    return BerserkerData.from_stream(data, game, property_size)


def _decode_berserker_info_hard(data: typing.BinaryIO, game: Game, property_size: int) -> BerserkerData:
    return BerserkerData.from_stream(data, game, property_size)


def _decode_berserker_info_elite(data: typing.BinaryIO, game: Game, property_size: int) -> BerserkerData:
    return BerserkerData.from_stream(data, game, property_size)


def _decode_unknown_struct21(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct21:
    return UnknownStruct21.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x43BBB1DD: ("patterned_info", _decode_patterned_info),
    0x54F9FFA5: ("berserker_info", _decode_berserker_info),
    0x2D8DC0AF: ("berserker_info_hard", _decode_berserker_info_hard),
    0xE10CE828: ("berserker_info_elite", _decode_berserker_info_elite),
    0x7B8C48C7: ("unknown_struct21", _decode_unknown_struct21),
}
