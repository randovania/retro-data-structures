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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class BrizgeeJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        waypoint_approach_distance: float
        wall_turn_speed: float
        floor_turn_speed: float
        down_turn_speed: float
        visible_distance: float
        forward_moving_priority: float
        no_shell_model: int
        no_shell_skin: int
        shell_vulnerability: json_util.JsonObject
        shell_health: float
        shell_contact_damage: json_util.JsonObject
        unknown: float
        poison_damage: json_util.JsonObject
        poison_time: float
        shell_break_sound: int
        poison_hit_sound: int
        player_poison_sound: int


@dataclasses.dataclass()
class Brizgee(BaseObjectType):
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
        default=720.0,
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
    visible_distance: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA72530E8, original_name="VisibleDistance"),
        },
    )
    forward_moving_priority: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E6A54B8, original_name="ForwardMovingPriority"),
        },
    )
    no_shell_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x07F947F4, original_name="NoShellModel"),
        },
    )
    no_shell_skin: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0B7325EA, original_name="NoShellSkin"),
        },
    )
    shell_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xF573E11C,
                original_name="ShellVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    shell_health: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAA13253A, original_name="ShellHealth"),
        },
    )
    shell_contact_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB482E5DD,
                original_name="ShellContactDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x80DA8053, original_name="Unknown"),
        },
    )
    poison_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x143D18C6,
                original_name="PoisonDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    poison_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF78947D4, original_name="PoisonTime"),
        },
    )
    shell_break_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x6A942A60, original_name="ShellBreakSound"),
        },
    )
    poison_hit_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x808392EC, original_name="PoisonHitSound"),
        },
    )
    player_poison_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xDF2D8017, original_name="PlayerPoisonSound"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "BRZG"

    @classmethod
    def modules(cls) -> list[str]:
        return ["WallCrawler.rel", "Parasite.rel"]

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
        if property_count != 20:
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
        assert property_id == 0xA72530E8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E6A54B8
        forward_moving_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07F947F4
        no_shell_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B7325EA
        no_shell_skin = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF573E11C
        shell_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA13253A
        shell_health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB482E5DD
        shell_contact_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80DA8053
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x143D18C6
        poison_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF78947D4
        poison_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A942A60
        shell_break_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x808392EC
        poison_hit_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF2D8017
        player_poison_sound = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            waypoint_approach_distance,
            wall_turn_speed,
            floor_turn_speed,
            down_turn_speed,
            visible_distance,
            forward_moving_priority,
            no_shell_model,
            no_shell_skin,
            shell_vulnerability,
            shell_health,
            shell_contact_damage,
            unknown,
            poison_damage,
            poison_time,
            shell_break_sound,
            poison_hit_sound,
            player_poison_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x14")  # 20 properties

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

        data.write(b"\xa7%0\xe8")  # 0xa72530e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b"^jT\xb8")  # 0x5e6a54b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_moving_priority))

        data.write(b"\x07\xf9G\xf4")  # 0x7f947f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.no_shell_model))

        data.write(b"\x0bs%\xea")  # 0xb7325ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.no_shell_skin))

        data.write(b"\xf5s\xe1\x1c")  # 0xf573e11c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shell_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaa\x13%:")  # 0xaa13253a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell_health))

        data.write(b"\xb4\x82\xe5\xdd")  # 0xb482e5dd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shell_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x80\xda\x80S")  # 0x80da8053
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x14=\x18\xc6")  # 0x143d18c6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.poison_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf7\x89G\xd4")  # 0xf78947d4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.poison_time))

        data.write(b"j\x94*`")  # 0x6a942a60
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.shell_break_sound))

        data.write(b"\x80\x83\x92\xec")  # 0x808392ec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.poison_hit_sound))

        data.write(b"\xdf-\x80\x17")  # 0xdf2d8017
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.player_poison_sound))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BrizgeeJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            waypoint_approach_distance=json_data["waypoint_approach_distance"],
            wall_turn_speed=json_data["wall_turn_speed"],
            floor_turn_speed=json_data["floor_turn_speed"],
            down_turn_speed=json_data["down_turn_speed"],
            visible_distance=json_data["visible_distance"],
            forward_moving_priority=json_data["forward_moving_priority"],
            no_shell_model=json_data["no_shell_model"],
            no_shell_skin=json_data["no_shell_skin"],
            shell_vulnerability=DamageVulnerability.from_json(json_data["shell_vulnerability"]),
            shell_health=json_data["shell_health"],
            shell_contact_damage=DamageInfo.from_json(json_data["shell_contact_damage"]),
            unknown=json_data["unknown"],
            poison_damage=DamageInfo.from_json(json_data["poison_damage"]),
            poison_time=json_data["poison_time"],
            shell_break_sound=json_data["shell_break_sound"],
            poison_hit_sound=json_data["poison_hit_sound"],
            player_poison_sound=json_data["player_poison_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "waypoint_approach_distance": self.waypoint_approach_distance,
            "wall_turn_speed": self.wall_turn_speed,
            "floor_turn_speed": self.floor_turn_speed,
            "down_turn_speed": self.down_turn_speed,
            "visible_distance": self.visible_distance,
            "forward_moving_priority": self.forward_moving_priority,
            "no_shell_model": self.no_shell_model,
            "no_shell_skin": self.no_shell_skin,
            "shell_vulnerability": self.shell_vulnerability.to_json(),
            "shell_health": self.shell_health,
            "shell_contact_damage": self.shell_contact_damage.to_json(),
            "unknown": self.unknown,
            "poison_damage": self.poison_damage.to_json(),
            "poison_time": self.poison_time,
            "shell_break_sound": self.shell_break_sound,
            "poison_hit_sound": self.poison_hit_sound,
            "player_poison_sound": self.player_poison_sound,
        }

    def _dependencies_for_no_shell_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.no_shell_model)

    def _dependencies_for_no_shell_skin(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.no_shell_skin)

    def _dependencies_for_shell_break_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shell_break_sound)

    def _dependencies_for_poison_hit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.poison_hit_sound)

    def _dependencies_for_player_poison_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.player_poison_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_no_shell_model, "no_shell_model", "AssetId"),
            (self._dependencies_for_no_shell_skin, "no_shell_skin", "AssetId"),
            (self._dependencies_for_shell_break_sound, "shell_break_sound", "int"),
            (self._dependencies_for_poison_hit_sound, "poison_hit_sound", "int"),
            (self._dependencies_for_player_poison_sound, "player_poison_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Brizgee.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_shell_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_shell_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_poison_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x733BD27C: ("waypoint_approach_distance", structs.decode_BIG_f),
    0xAC47C628: ("wall_turn_speed", structs.decode_BIG_f),
    0x8E4F7B29: ("floor_turn_speed", structs.decode_BIG_f),
    0x3D3C1B76: ("down_turn_speed", structs.decode_BIG_f),
    0xA72530E8: ("visible_distance", structs.decode_BIG_f),
    0x5E6A54B8: ("forward_moving_priority", structs.decode_BIG_f),
    0x07F947F4: ("no_shell_model", structs.decode_BIG_L),
    0x0B7325EA: ("no_shell_skin", structs.decode_BIG_L),
    0xF573E11C: ("shell_vulnerability", _decode_shell_vulnerability),
    0xAA13253A: ("shell_health", structs.decode_BIG_f),
    0xB482E5DD: ("shell_contact_damage", _decode_shell_contact_damage),
    0x80DA8053: ("unknown", structs.decode_BIG_f),
    0x143D18C6: ("poison_damage", _decode_poison_damage),
    0xF78947D4: ("poison_time", structs.decode_BIG_f),
    0x6A942A60: ("shell_break_sound", structs.decode_BIG_l),
    0x808392EC: ("poison_hit_sound", structs.decode_BIG_l),
    0xDF2D8017: ("player_poison_sound", structs.decode_BIG_l),
}
