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
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PillBugJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        unknown_0xde7e9f94: int
        floor_turn_speed: float
        stick_radius: float
        waypoint_approach_distance: float
        visible_distance: float
        damage_vulnerability: json_util.JsonObject
        wander_vulnerability: json_util.JsonObject
        crawl_radius: float
        roll_radius: float
        unknown_0x519c7197: float
        unknown_0xa265383c: float
        forward_priority: float
        unknown_0x558c0692: float
        unknown_0x0f991bf1: float
        unknown_0x385a1bed: float
        unknown_0xcf4ea141: float


@dataclasses.dataclass()
class PillBug(BaseObjectType):
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
    unknown_0xde7e9f94: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDE7E9F94, original_name="Unknown"),
        },
    )
    floor_turn_speed: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E4F7B29, original_name="FloorTurnSpeed"),
        },
    )
    stick_radius: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5A3A30F4, original_name="StickRadius"),
        },
    )
    waypoint_approach_distance: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x733BD27C, original_name="WaypointApproachDistance"),
        },
    )
    visible_distance: float = dataclasses.field(
        default=200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA72530E8, original_name="VisibleDistance"),
        },
    )
    damage_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x5D84ED71,
                original_name="DamageVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    wander_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xF382DFF7,
                original_name="WanderVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    crawl_radius: float = dataclasses.field(
        default=0.3499999940395355,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD98E16D, original_name="CrawlRadius"),
        },
    )
    roll_radius: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x81D699B0, original_name="RollRadius"),
        },
    )
    unknown_0x519c7197: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x519C7197, original_name="Unknown"),
        },
    )
    unknown_0xa265383c: float = dataclasses.field(
        default=0.019999999552965164,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA265383C, original_name="Unknown"),
        },
    )
    forward_priority: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD08E189, original_name="ForwardPriority"),
        },
    )
    unknown_0x558c0692: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x558C0692, original_name="Unknown"),
        },
    )
    unknown_0x0f991bf1: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0F991BF1, original_name="Unknown"),
        },
    )
    unknown_0x385a1bed: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x385A1BED, original_name="Unknown"),
        },
    )
    unknown_0xcf4ea141: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF4EA141, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PILB"

    @classmethod
    def modules(cls) -> list[str]:
        return ["WallCrawler.rel", "PillBug.rel"]

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
        if property_count != 19:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE7E9F94
        unknown_0xde7e9f94 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E4F7B29
        floor_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5A3A30F4
        stick_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733BD27C
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA72530E8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D84ED71
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF382DFF7
        wander_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD98E16D
        crawl_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81D699B0
        roll_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x519C7197
        unknown_0x519c7197 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA265383C
        unknown_0xa265383c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD08E189
        forward_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x558C0692
        unknown_0x558c0692 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F991BF1
        unknown_0x0f991bf1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385A1BED
        unknown_0x385a1bed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF4EA141
        unknown_0xcf4ea141 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            unknown_0xde7e9f94,
            floor_turn_speed,
            stick_radius,
            waypoint_approach_distance,
            visible_distance,
            damage_vulnerability,
            wander_vulnerability,
            crawl_radius,
            roll_radius,
            unknown_0x519c7197,
            unknown_0xa265383c,
            forward_priority,
            unknown_0x558c0692,
            unknown_0x0f991bf1,
            unknown_0x385a1bed,
            unknown_0xcf4ea141,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x13")  # 19 properties

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
        self.patterned.to_stream(data, game)
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

        data.write(b"\xde~\x9f\x94")  # 0xde7e9f94
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xde7e9f94))

        data.write(b"\x8eO{)")  # 0x8e4f7b29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b"Z:0\xf4")  # 0x5a3a30f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stick_radius))

        data.write(b"s;\xd2|")  # 0x733bd27c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b"\xa7%0\xe8")  # 0xa72530e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b"]\x84\xedq")  # 0x5d84ed71
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3\x82\xdf\xf7")  # 0xf382dff7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.wander_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xad\x98\xe1m")  # 0xad98e16d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.crawl_radius))

        data.write(b"\x81\xd6\x99\xb0")  # 0x81d699b0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.roll_radius))

        data.write(b"Q\x9cq\x97")  # 0x519c7197
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x519c7197))

        data.write(b"\xa2e8<")  # 0xa265383c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa265383c))

        data.write(b"\xad\x08\xe1\x89")  # 0xad08e189
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_priority))

        data.write(b"U\x8c\x06\x92")  # 0x558c0692
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x558c0692))

        data.write(b"\x0f\x99\x1b\xf1")  # 0xf991bf1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0f991bf1))

        data.write(b"8Z\x1b\xed")  # 0x385a1bed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x385a1bed))

        data.write(b"\xcfN\xa1A")  # 0xcf4ea141
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcf4ea141))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PillBugJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            unknown_0xde7e9f94=json_data["unknown_0xde7e9f94"],
            floor_turn_speed=json_data["floor_turn_speed"],
            stick_radius=json_data["stick_radius"],
            waypoint_approach_distance=json_data["waypoint_approach_distance"],
            visible_distance=json_data["visible_distance"],
            damage_vulnerability=DamageVulnerability.from_json(json_data["damage_vulnerability"]),
            wander_vulnerability=DamageVulnerability.from_json(json_data["wander_vulnerability"]),
            crawl_radius=json_data["crawl_radius"],
            roll_radius=json_data["roll_radius"],
            unknown_0x519c7197=json_data["unknown_0x519c7197"],
            unknown_0xa265383c=json_data["unknown_0xa265383c"],
            forward_priority=json_data["forward_priority"],
            unknown_0x558c0692=json_data["unknown_0x558c0692"],
            unknown_0x0f991bf1=json_data["unknown_0x0f991bf1"],
            unknown_0x385a1bed=json_data["unknown_0x385a1bed"],
            unknown_0xcf4ea141=json_data["unknown_0xcf4ea141"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "unknown_0xde7e9f94": self.unknown_0xde7e9f94,
            "floor_turn_speed": self.floor_turn_speed,
            "stick_radius": self.stick_radius,
            "waypoint_approach_distance": self.waypoint_approach_distance,
            "visible_distance": self.visible_distance,
            "damage_vulnerability": self.damage_vulnerability.to_json(),
            "wander_vulnerability": self.wander_vulnerability.to_json(),
            "crawl_radius": self.crawl_radius,
            "roll_radius": self.roll_radius,
            "unknown_0x519c7197": self.unknown_0x519c7197,
            "unknown_0xa265383c": self.unknown_0xa265383c,
            "forward_priority": self.forward_priority,
            "unknown_0x558c0692": self.unknown_0x558c0692,
            "unknown_0x0f991bf1": self.unknown_0x0f991bf1,
            "unknown_0x385a1bed": self.unknown_0x385a1bed,
            "unknown_0xcf4ea141": self.unknown_0xcf4ea141,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PillBug.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wander_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xDE7E9F94: ("unknown_0xde7e9f94", structs.decode_BIG_l),
    0x8E4F7B29: ("floor_turn_speed", structs.decode_BIG_f),
    0x5A3A30F4: ("stick_radius", structs.decode_BIG_f),
    0x733BD27C: ("waypoint_approach_distance", structs.decode_BIG_f),
    0xA72530E8: ("visible_distance", structs.decode_BIG_f),
    0x5D84ED71: ("damage_vulnerability", _decode_damage_vulnerability),
    0xF382DFF7: ("wander_vulnerability", _decode_wander_vulnerability),
    0xAD98E16D: ("crawl_radius", structs.decode_BIG_f),
    0x81D699B0: ("roll_radius", structs.decode_BIG_f),
    0x519C7197: ("unknown_0x519c7197", structs.decode_BIG_f),
    0xA265383C: ("unknown_0xa265383c", structs.decode_BIG_f),
    0xAD08E189: ("forward_priority", structs.decode_BIG_f),
    0x558C0692: ("unknown_0x558c0692", structs.decode_BIG_f),
    0x0F991BF1: ("unknown_0x0f991bf1", structs.decode_BIG_f),
    0x385A1BED: ("unknown_0x385a1bed", structs.decode_BIG_f),
    0xCF4EA141: ("unknown_0xcf4ea141", structs.decode_BIG_f),
}
