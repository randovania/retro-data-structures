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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class AmbientAIJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        mass: float
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        character_animation_information: json_util.JsonObject
        actor_information: json_util.JsonObject
        detect_radius: float
        explode_radius: float
        unknown_0x6c3b5f38: int
        unknown_0xe9bf2240: int


@dataclasses.dataclass()
class AmbientAI(BaseObjectType):
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
    collision_box: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xF344C0B0, original_name="CollisionBox", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x2E686C2A,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    mass: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75DBB375, original_name="Mass"),
        },
    )
    health: HealthInfo = dataclasses.field(
        default_factory=HealthInfo,
        metadata={
            "reflection": FieldReflection[HealthInfo](
                HealthInfo,
                id=0xCF90D15E,
                original_name="Health",
                from_json=HealthInfo.from_json,
                to_json=HealthInfo.to_json,
            ),
        },
    )
    vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x7B71AE90,
                original_name="Vulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
    detect_radius: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA7D00780, original_name="DetectRadius"),
        },
    )
    explode_radius: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4D52631, original_name="ExplodeRadius"),
        },
    )
    unknown_0x6c3b5f38: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6C3B5F38, original_name="Unknown"),
        },
    )
    unknown_0xe9bf2240: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE9BF2240, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "AMIA"

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
        if property_count != 12:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF344C0B0
        collision_box = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E686C2A
        collision_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75DBB375
        mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF90D15E
        health = HealthInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B71AE90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA244C9D8
        character_animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA7D00780
        detect_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4D52631
        explode_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C3B5F38
        unknown_0x6c3b5f38 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9BF2240
        unknown_0xe9bf2240 = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            collision_box,
            collision_offset,
            mass,
            health,
            vulnerability,
            character_animation_information,
            actor_information,
            detect_radius,
            explode_radius,
            unknown_0x6c3b5f38,
            unknown_0xe9bf2240,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0c")  # 12 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3D\xc0\xb0")  # 0xf344c0b0
        data.write(b"\x00\x0c")  # size
        self.collision_box.to_stream(data, game)

        data.write(b".hl*")  # 0x2e686c2a
        data.write(b"\x00\x0c")  # size
        self.collision_offset.to_stream(data, game)

        data.write(b"u\xdb\xb3u")  # 0x75dbb375
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mass))

        data.write(b"\xcf\x90\xd1^")  # 0xcf90d15e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{q\xae\x90")  # 0x7b71ae90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vulnerability.to_stream(data, game)
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

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa7\xd0\x07\x80")  # 0xa7d00780
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.detect_radius))

        data.write(b"\xd4\xd5&1")  # 0xd4d52631
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.explode_radius))

        data.write(b"l;_8")  # 0x6c3b5f38
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6c3b5f38))

        data.write(b'\xe9\xbf"@')  # 0xe9bf2240
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe9bf2240))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AmbientAIJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            collision_box=Vector.from_json(json_data["collision_box"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            mass=json_data["mass"],
            health=HealthInfo.from_json(json_data["health"]),
            vulnerability=DamageVulnerability.from_json(json_data["vulnerability"]),
            character_animation_information=AnimationParameters.from_json(json_data["character_animation_information"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            detect_radius=json_data["detect_radius"],
            explode_radius=json_data["explode_radius"],
            unknown_0x6c3b5f38=json_data["unknown_0x6c3b5f38"],
            unknown_0xe9bf2240=json_data["unknown_0xe9bf2240"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "collision_box": self.collision_box.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "mass": self.mass,
            "health": self.health.to_json(),
            "vulnerability": self.vulnerability.to_json(),
            "character_animation_information": self.character_animation_information.to_json(),
            "actor_information": self.actor_information.to_json(),
            "detect_radius": self.detect_radius,
            "explode_radius": self.explode_radius,
            "unknown_0x6c3b5f38": self.unknown_0x6c3b5f38,
            "unknown_0xe9bf2240": self.unknown_0xe9bf2240,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_character_animation_information(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xF344C0B0: ("collision_box", _decode_collision_box),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0x75DBB375: ("mass", structs.decode_BIG_f),
    0xCF90D15E: ("health", _decode_health),
    0x7B71AE90: ("vulnerability", _decode_vulnerability),
    0xA244C9D8: ("character_animation_information", _decode_character_animation_information),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xA7D00780: ("detect_radius", structs.decode_BIG_f),
    0xD4D52631: ("explode_radius", structs.decode_BIG_f),
    0x6C3B5F38: ("unknown_0x6c3b5f38", structs.decode_BIG_l),
    0xE9BF2240: ("unknown_0xe9bf2240", structs.decode_BIG_l),
}
