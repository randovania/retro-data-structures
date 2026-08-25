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
from retro_data_structures.properties.corruption.archetypes.SwarmBasicsData import SwarmBasicsData
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class WallCrawlerSwarmJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        character_animation_information: json_util.JsonObject
        active: bool
        swarm_basics_data: json_util.JsonObject
        wall_crawler_death_effect: int


@dataclasses.dataclass()
class WallCrawlerSwarm(BaseObjectType):
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
    character_animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA244C9D8,
                original_name="CharacterAnimationInformation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    active: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC6BB2F45, original_name="Active"),
        },
    )
    swarm_basics_data: SwarmBasicsData = dataclasses.field(
        default_factory=SwarmBasicsData,
        metadata={
            "reflection": FieldReflection[SwarmBasicsData](
                SwarmBasicsData,
                id=0x4CFC46FE,
                original_name="SwarmBasicsData",
                from_json=SwarmBasicsData.from_json,
                to_json=SwarmBasicsData.to_json,
            ),
        },
    )
    wall_crawler_death_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6832496F, original_name="WallCrawlerDeathEffect"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SWRM"

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
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA244C9D8
        character_animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6BB2F45
        active = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4CFC46FE
        swarm_basics_data = SwarmBasicsData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6832496F
        wall_crawler_death_effect = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            editor_properties,
            actor_information,
            character_animation_information,
            active,
            swarm_basics_data,
            wall_crawler_death_effect,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x05")  # 5 properties
        num_properties_written = 5

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

        data.write(b"\xa2D\xc9\xd8")  # 0xa244c9d8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.character_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.active != default_override.get("active", True):
            num_properties_written += 1
            data.write(b"\xc6\xbb/E")  # 0xc6bb2f45
            data.write(b"\x00\x01")  # size
            data.write(structs.BIG_bool_.pack(self.active))

        data.write(b"L\xfcF\xfe")  # 0x4cfc46fe
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_basics_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"h2Io")  # 0x6832496f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wall_crawler_death_effect))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WallCrawlerSwarmJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            character_animation_information=AnimationParameters.from_json(json_data["character_animation_information"]),
            active=json_data["active"],
            swarm_basics_data=SwarmBasicsData.from_json(json_data["swarm_basics_data"]),
            wall_crawler_death_effect=json_data["wall_crawler_death_effect"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "character_animation_information": self.character_animation_information.to_json(),
            "active": self.active,
            "swarm_basics_data": self.swarm_basics_data.to_json(),
            "wall_crawler_death_effect": self.wall_crawler_death_effect,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_character_animation_information(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_swarm_basics_data(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmBasicsData:
    return SwarmBasicsData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xA244C9D8: ("character_animation_information", _decode_character_animation_information),
    0xC6BB2F45: ("active", structs.decode_BIG_bool_),
    0x4CFC46FE: ("swarm_basics_data", _decode_swarm_basics_data),
    0x6832496F: ("wall_crawler_death_effect", structs.decode_BIG_Q),
}
