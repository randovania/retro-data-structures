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
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.corruption.archetypes.WallCrawlerData import WallCrawlerData
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ParasiteJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flavor: int
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        telegraph_distance: float
        waypoint_approach_distance: float
        wall_turn_speed: float
        floor_turn_speed: float
        down_turn_speed: float
        stuck_time: float
        unknown_0xd5c25506: float
        behavior_influence_radius: float
        separation_distance: float
        separation_priority: float
        alignment_priority: float
        unknown_0x61959f0d: float
        path_following_priority: float
        forward_moving_priority: float
        player_avoidance_distance: float
        player_avoidance_priority: float
        parasite_visible_distance: float
        initially_paused: bool
        wall_crawler_properties: json_util.JsonObject


@dataclasses.dataclass()
class Parasite(BaseObjectType):
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
    flavor: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBE73724A, original_name="Flavor"),
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
    telegraph_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8458B003, original_name="TelegraphDistance"),
        },
    )
    waypoint_approach_distance: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x733BD27C, original_name="WaypointApproachDistance"),
        },
    )
    wall_turn_speed: float = dataclasses.field(
        default=360.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAC47C628, original_name="WallTurnSpeed"),
        },
    )
    floor_turn_speed: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E4F7B29, original_name="FloorTurnSpeed"),
        },
    )
    down_turn_speed: float = dataclasses.field(
        default=120.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3D3C1B76, original_name="DownTurnSpeed"),
        },
    )
    stuck_time: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0E7E3698, original_name="StuckTime"),
        },
    )
    unknown_0xd5c25506: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5C25506, original_name="Unknown"),
        },
    )
    behavior_influence_radius: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x280361AA, original_name="BehaviorInfluenceRadius"),
        },
    )
    separation_distance: float = dataclasses.field(
        default=2.5999999046325684,
        metadata={
            "reflection": FieldReflection[float](float, id=0x01559F27, original_name="SeparationDistance"),
        },
    )
    separation_priority: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD293EBC4, original_name="SeparationPriority"),
        },
    )
    alignment_priority: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4841F1DE, original_name="AlignmentPriority"),
        },
    )
    unknown_0x61959f0d: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61959F0D, original_name="Unknown"),
        },
    )
    path_following_priority: float = dataclasses.field(
        default=0.8999999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAE11F975, original_name="PathFollowingPriority"),
        },
    )
    forward_moving_priority: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E6A54B8, original_name="ForwardMovingPriority"),
        },
    )
    player_avoidance_distance: float = dataclasses.field(
        default=1.2999999523162842,
        metadata={
            "reflection": FieldReflection[float](float, id=0x956A1248, original_name="PlayerAvoidanceDistance"),
        },
    )
    player_avoidance_priority: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x46AC66AB, original_name="PlayerAvoidancePriority"),
        },
    )
    parasite_visible_distance: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4EEEC785, original_name="ParasiteVisibleDistance"),
        },
    )
    initially_paused: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC3CC437F, original_name="InitiallyPaused"),
        },
    )
    wall_crawler_properties: WallCrawlerData = dataclasses.field(
        default_factory=WallCrawlerData,
        metadata={
            "reflection": FieldReflection[WallCrawlerData](
                WallCrawlerData,
                id=0xB718B831,
                original_name="WallCrawlerProperties",
                from_json=WallCrawlerData.from_json,
                to_json=WallCrawlerData.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PARA"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_Parasite.rso"]

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
        if property_count != 23:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE73724A
        flavor = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "mass": 25.0,
                "damage_wait_time": 3.0,
                "collision_radius": 0.20000000298023224,
                "speed": 3.0,
                "turn_speed": 720.0,
                "detection_range": 5.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "max_attack_range": 20.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8458B003
        telegraph_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733BD27C
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC47C628
        wall_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E4F7B29
        floor_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D3C1B76
        down_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0E7E3698
        stuck_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5C25506
        unknown_0xd5c25506 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x280361AA
        behavior_influence_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01559F27
        separation_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD293EBC4
        separation_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4841F1DE
        alignment_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61959F0D
        unknown_0x61959f0d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE11F975
        path_following_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E6A54B8
        forward_moving_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x956A1248
        player_avoidance_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46AC66AB
        player_avoidance_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EEEC785
        parasite_visible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3CC437F
        initially_paused = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB718B831
        wall_crawler_properties = WallCrawlerData.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            flavor,
            patterned,
            actor_information,
            telegraph_distance,
            waypoint_approach_distance,
            wall_turn_speed,
            floor_turn_speed,
            down_turn_speed,
            stuck_time,
            unknown_0xd5c25506,
            behavior_influence_radius,
            separation_distance,
            separation_priority,
            alignment_priority,
            unknown_0x61959f0d,
            path_following_priority,
            forward_moving_priority,
            player_avoidance_distance,
            player_avoidance_priority,
            parasite_visible_distance,
            initially_paused,
            wall_crawler_properties,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x17")  # 23 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbesrJ")  # 0xbe73724a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flavor))

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(
            data,
            game,
            default_override={
                "mass": 25.0,
                "damage_wait_time": 3.0,
                "collision_radius": 0.20000000298023224,
                "speed": 3.0,
                "turn_speed": 720.0,
                "detection_range": 5.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "max_attack_range": 20.0,
            },
        )
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

        data.write(b"\x84X\xb0\x03")  # 0x8458b003
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.telegraph_distance))

        data.write(b"s;\xd2|")  # 0x733bd27c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b"\xacG\xc6(")  # 0xac47c628
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wall_turn_speed))

        data.write(b"\x8eO{)")  # 0x8e4f7b29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b"=<\x1bv")  # 0x3d3c1b76
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.down_turn_speed))

        data.write(b"\x0e~6\x98")  # 0xe7e3698
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stuck_time))

        data.write(b"\xd5\xc2U\x06")  # 0xd5c25506
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd5c25506))

        data.write(b"(\x03a\xaa")  # 0x280361aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.behavior_influence_radius))

        data.write(b"\x01U\x9f'")  # 0x1559f27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.separation_distance))

        data.write(b"\xd2\x93\xeb\xc4")  # 0xd293ebc4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.separation_priority))

        data.write(b"HA\xf1\xde")  # 0x4841f1de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alignment_priority))

        data.write(b"a\x95\x9f\r")  # 0x61959f0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x61959f0d))

        data.write(b"\xae\x11\xf9u")  # 0xae11f975
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.path_following_priority))

        data.write(b"^jT\xb8")  # 0x5e6a54b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_moving_priority))

        data.write(b"\x95j\x12H")  # 0x956a1248
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_avoidance_distance))

        data.write(b"F\xacf\xab")  # 0x46ac66ab
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_avoidance_priority))

        data.write(b"N\xee\xc7\x85")  # 0x4eeec785
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.parasite_visible_distance))

        data.write(b"\xc3\xccC\x7f")  # 0xc3cc437f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.initially_paused))

        data.write(b"\xb7\x18\xb81")  # 0xb718b831
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.wall_crawler_properties.to_stream(data, game)
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
        json_data = typing.cast("ParasiteJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            flavor=json_data["flavor"],
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            telegraph_distance=json_data["telegraph_distance"],
            waypoint_approach_distance=json_data["waypoint_approach_distance"],
            wall_turn_speed=json_data["wall_turn_speed"],
            floor_turn_speed=json_data["floor_turn_speed"],
            down_turn_speed=json_data["down_turn_speed"],
            stuck_time=json_data["stuck_time"],
            unknown_0xd5c25506=json_data["unknown_0xd5c25506"],
            behavior_influence_radius=json_data["behavior_influence_radius"],
            separation_distance=json_data["separation_distance"],
            separation_priority=json_data["separation_priority"],
            alignment_priority=json_data["alignment_priority"],
            unknown_0x61959f0d=json_data["unknown_0x61959f0d"],
            path_following_priority=json_data["path_following_priority"],
            forward_moving_priority=json_data["forward_moving_priority"],
            player_avoidance_distance=json_data["player_avoidance_distance"],
            player_avoidance_priority=json_data["player_avoidance_priority"],
            parasite_visible_distance=json_data["parasite_visible_distance"],
            initially_paused=json_data["initially_paused"],
            wall_crawler_properties=WallCrawlerData.from_json(json_data["wall_crawler_properties"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "flavor": self.flavor,
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "telegraph_distance": self.telegraph_distance,
            "waypoint_approach_distance": self.waypoint_approach_distance,
            "wall_turn_speed": self.wall_turn_speed,
            "floor_turn_speed": self.floor_turn_speed,
            "down_turn_speed": self.down_turn_speed,
            "stuck_time": self.stuck_time,
            "unknown_0xd5c25506": self.unknown_0xd5c25506,
            "behavior_influence_radius": self.behavior_influence_radius,
            "separation_distance": self.separation_distance,
            "separation_priority": self.separation_priority,
            "alignment_priority": self.alignment_priority,
            "unknown_0x61959f0d": self.unknown_0x61959f0d,
            "path_following_priority": self.path_following_priority,
            "forward_moving_priority": self.forward_moving_priority,
            "player_avoidance_distance": self.player_avoidance_distance,
            "player_avoidance_priority": self.player_avoidance_priority,
            "parasite_visible_distance": self.parasite_visible_distance,
            "initially_paused": self.initially_paused,
            "wall_crawler_properties": self.wall_crawler_properties.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "mass": 25.0,
            "damage_wait_time": 3.0,
            "collision_radius": 0.20000000298023224,
            "speed": 3.0,
            "turn_speed": 720.0,
            "detection_range": 5.0,
            "detection_angle": 90.0,
            "min_attack_range": 4.0,
            "max_attack_range": 20.0,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_wall_crawler_properties(data: typing.BinaryIO, game: Game, property_size: int) -> WallCrawlerData:
    return WallCrawlerData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xBE73724A: ("flavor", structs.decode_BIG_l),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x8458B003: ("telegraph_distance", structs.decode_BIG_f),
    0x733BD27C: ("waypoint_approach_distance", structs.decode_BIG_f),
    0xAC47C628: ("wall_turn_speed", structs.decode_BIG_f),
    0x8E4F7B29: ("floor_turn_speed", structs.decode_BIG_f),
    0x3D3C1B76: ("down_turn_speed", structs.decode_BIG_f),
    0x0E7E3698: ("stuck_time", structs.decode_BIG_f),
    0xD5C25506: ("unknown_0xd5c25506", structs.decode_BIG_f),
    0x280361AA: ("behavior_influence_radius", structs.decode_BIG_f),
    0x01559F27: ("separation_distance", structs.decode_BIG_f),
    0xD293EBC4: ("separation_priority", structs.decode_BIG_f),
    0x4841F1DE: ("alignment_priority", structs.decode_BIG_f),
    0x61959F0D: ("unknown_0x61959f0d", structs.decode_BIG_f),
    0xAE11F975: ("path_following_priority", structs.decode_BIG_f),
    0x5E6A54B8: ("forward_moving_priority", structs.decode_BIG_f),
    0x956A1248: ("player_avoidance_distance", structs.decode_BIG_f),
    0x46AC66AB: ("player_avoidance_priority", structs.decode_BIG_f),
    0x4EEEC785: ("parasite_visible_distance", structs.decode_BIG_f),
    0xC3CC437F: ("initially_paused", structs.decode_BIG_bool_),
    0xB718B831: ("wall_crawler_properties", _decode_wall_crawler_properties),
}
