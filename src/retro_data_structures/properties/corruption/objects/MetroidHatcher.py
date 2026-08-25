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
from retro_data_structures.properties.corruption.archetypes.MetroidHatcherData import MetroidHatcherData
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MetroidHatcherJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        patterned_ai_0x5c056cef: json_util.JsonObject
        patterned_ai_0x8be7ecb7: json_util.JsonObject
        metroid_hatcher_data_0x42e95705: json_util.JsonObject
        metroid_hatcher_data_0x266b7d6b: json_util.JsonObject
        metroid_hatcher_data_0xf189fd33: json_util.JsonObject
        actor_information: json_util.JsonObject


@dataclasses.dataclass()
class MetroidHatcher(BaseObjectType):
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
    patterned_ai_0x5c056cef: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x5C056CEF,
                original_name="PatternedAI",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    patterned_ai_0x8be7ecb7: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0x8BE7ECB7,
                original_name="PatternedAI",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    metroid_hatcher_data_0x42e95705: MetroidHatcherData = dataclasses.field(
        default_factory=MetroidHatcherData,
        metadata={
            "reflection": FieldReflection[MetroidHatcherData](
                MetroidHatcherData,
                id=0x42E95705,
                original_name="MetroidHatcherData",
                from_json=MetroidHatcherData.from_json,
                to_json=MetroidHatcherData.to_json,
            ),
        },
    )
    metroid_hatcher_data_0x266b7d6b: MetroidHatcherData = dataclasses.field(
        default_factory=MetroidHatcherData,
        metadata={
            "reflection": FieldReflection[MetroidHatcherData](
                MetroidHatcherData,
                id=0x266B7D6B,
                original_name="MetroidHatcherData",
                from_json=MetroidHatcherData.from_json,
                to_json=MetroidHatcherData.to_json,
            ),
        },
    )
    metroid_hatcher_data_0xf189fd33: MetroidHatcherData = dataclasses.field(
        default_factory=MetroidHatcherData,
        metadata={
            "reflection": FieldReflection[MetroidHatcherData](
                MetroidHatcherData,
                id=0xF189FD33,
                original_name="MetroidHatcherData",
                from_json=MetroidHatcherData.from_json,
                to_json=MetroidHatcherData.to_json,
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

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "MHAT"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_MetroidHatcher.rso"]

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
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "mass": 1000.0,
                "collision_radius": 3.0,
                "collision_height": 9.0,
                "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
                "step_up_height": 1.0,
                "creature_size": 2,
                "leash_radius": 100.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C056CEF
        patterned_ai_0x5c056cef = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "mass": 1000.0,
                "collision_radius": 3.0,
                "collision_height": 9.0,
                "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
                "step_up_height": 1.0,
                "creature_size": 2,
                "leash_radius": 100.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8BE7ECB7
        patterned_ai_0x8be7ecb7 = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "mass": 1000.0,
                "collision_radius": 3.0,
                "collision_height": 9.0,
                "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
                "step_up_height": 1.0,
                "creature_size": 2,
                "leash_radius": 100.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42E95705
        metroid_hatcher_data_0x42e95705 = MetroidHatcherData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x266B7D6B
        metroid_hatcher_data_0x266b7d6b = MetroidHatcherData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF189FD33
        metroid_hatcher_data_0xf189fd33 = MetroidHatcherData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            patterned,
            patterned_ai_0x5c056cef,
            patterned_ai_0x8be7ecb7,
            metroid_hatcher_data_0x42e95705,
            metroid_hatcher_data_0x266b7d6b,
            metroid_hatcher_data_0xf189fd33,
            actor_information,
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

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(
            data,
            game,
            default_override={
                "mass": 1000.0,
                "collision_radius": 3.0,
                "collision_height": 9.0,
                "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
                "step_up_height": 1.0,
                "creature_size": 2,
                "leash_radius": 100.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\\\x05l\xef")  # 0x5c056cef
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned_ai_0x5c056cef.to_stream(
            data,
            game,
            default_override={
                "mass": 1000.0,
                "collision_radius": 3.0,
                "collision_height": 9.0,
                "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
                "step_up_height": 1.0,
                "creature_size": 2,
                "leash_radius": 100.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\xe7\xec\xb7")  # 0x8be7ecb7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned_ai_0x8be7ecb7.to_stream(
            data,
            game,
            default_override={
                "mass": 1000.0,
                "collision_radius": 3.0,
                "collision_height": 9.0,
                "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
                "step_up_height": 1.0,
                "creature_size": 2,
                "leash_radius": 100.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"B\xe9W\x05")  # 0x42e95705
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_hatcher_data_0x42e95705.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"&k}k")  # 0x266b7d6b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_hatcher_data_0x266b7d6b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf1\x89\xfd3")  # 0xf189fd33
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.metroid_hatcher_data_0xf189fd33.to_stream(data, game)
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

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidHatcherJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            patterned_ai_0x5c056cef=PatternedAITypedef.from_json(json_data["patterned_ai_0x5c056cef"]),
            patterned_ai_0x8be7ecb7=PatternedAITypedef.from_json(json_data["patterned_ai_0x8be7ecb7"]),
            metroid_hatcher_data_0x42e95705=MetroidHatcherData.from_json(json_data["metroid_hatcher_data_0x42e95705"]),
            metroid_hatcher_data_0x266b7d6b=MetroidHatcherData.from_json(json_data["metroid_hatcher_data_0x266b7d6b"]),
            metroid_hatcher_data_0xf189fd33=MetroidHatcherData.from_json(json_data["metroid_hatcher_data_0xf189fd33"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "patterned_ai_0x5c056cef": self.patterned_ai_0x5c056cef.to_json(),
            "patterned_ai_0x8be7ecb7": self.patterned_ai_0x8be7ecb7.to_json(),
            "metroid_hatcher_data_0x42e95705": self.metroid_hatcher_data_0x42e95705.to_json(),
            "metroid_hatcher_data_0x266b7d6b": self.metroid_hatcher_data_0x266b7d6b.to_json(),
            "metroid_hatcher_data_0xf189fd33": self.metroid_hatcher_data_0xf189fd33.to_json(),
            "actor_information": self.actor_information.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "mass": 1000.0,
            "collision_radius": 3.0,
            "collision_height": 9.0,
            "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
            "step_up_height": 1.0,
            "creature_size": 2,
            "leash_radius": 100.0,
        },
    )


def _decode_patterned_ai_0x5c056cef(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "mass": 1000.0,
            "collision_radius": 3.0,
            "collision_height": 9.0,
            "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
            "step_up_height": 1.0,
            "creature_size": 2,
            "leash_radius": 100.0,
        },
    )


def _decode_patterned_ai_0x8be7ecb7(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "mass": 1000.0,
            "collision_radius": 3.0,
            "collision_height": 9.0,
            "collision_offset": Vector(x=0.0, y=0.0, z=-1.7999999523162842),
            "step_up_height": 1.0,
            "creature_size": 2,
            "leash_radius": 100.0,
        },
    )


def _decode_metroid_hatcher_data_0x42e95705(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidHatcherData:
    return MetroidHatcherData.from_stream(data, game, property_size)


def _decode_metroid_hatcher_data_0x266b7d6b(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidHatcherData:
    return MetroidHatcherData.from_stream(data, game, property_size)


def _decode_metroid_hatcher_data_0xf189fd33(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MetroidHatcherData:
    return MetroidHatcherData.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x5C056CEF: ("patterned_ai_0x5c056cef", _decode_patterned_ai_0x5c056cef),
    0x8BE7ECB7: ("patterned_ai_0x8be7ecb7", _decode_patterned_ai_0x8be7ecb7),
    0x42E95705: ("metroid_hatcher_data_0x42e95705", _decode_metroid_hatcher_data_0x42e95705),
    0x266B7D6B: ("metroid_hatcher_data_0x266b7d6b", _decode_metroid_hatcher_data_0x266b7d6b),
    0xF189FD33: ("metroid_hatcher_data_0xf189fd33", _decode_metroid_hatcher_data_0xf189fd33),
    0x7E397FED: ("actor_information", _decode_actor_information),
}
