# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
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

    class KrocussJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flavor: int
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        waypoint_approach_distance: float
        visible_distance: float
        wall_turn_speed: float
        floor_turn_speed: float
        down_turn_speed: float
        unknown_0xd5c25506: float
        projectile_bounds_multiplier: float
        collision_look_ahead: float
        anim_speed_scalar: float
        initially_paused: bool
        unknown_0xf04cadca: float
        unknown_0x497d54e8: float
        unknown_0x3371c963: float
        unknown_0x22d37771: float
        unknown_0xbbebed9e: float
        shell_closed_vulnerability: json_util.JsonObject
        wing_light_color: json_util.JsonValue
        dpsc: int
        shell_open_sound: int
        shell_close_sound: int
        max_audible_distance: float


@dataclasses.dataclass()
class Krocuss(BaseObjectType):
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
    waypoint_approach_distance: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x733BD27C, original_name="WaypointApproachDistance"),
        },
    )
    visible_distance: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA72530E8, original_name="VisibleDistance"),
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
    unknown_0xd5c25506: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5C25506, original_name="Unknown"),
        },
    )
    projectile_bounds_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x742EAB20, original_name="ProjectileBoundsMultiplier"),
        },
    )
    collision_look_ahead: float = dataclasses.field(
        default=0.019999999552965164,
        metadata={
            "reflection": FieldReflection[float](float, id=0x80A81909, original_name="CollisionLookAhead"),
        },
    )
    anim_speed_scalar: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8590483B, original_name="AnimSpeedScalar"),
        },
    )
    initially_paused: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC3CC437F, original_name="InitiallyPaused"),
        },
    )
    unknown_0xf04cadca: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF04CADCA, original_name="Unknown"),
        },
    )
    unknown_0x497d54e8: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x497D54E8, original_name="Unknown"),
        },
    )
    unknown_0x3371c963: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3371C963, original_name="Unknown"),
        },
    )
    unknown_0x22d37771: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x22D37771, original_name="Unknown"),
        },
    )
    unknown_0xbbebed9e: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBBEBED9E, original_name="Unknown"),
        },
    )
    shell_closed_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x6BD144C8,
                original_name="ShellClosedVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    wing_light_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x4D20624B, original_name="WingLightColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    dpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["DPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC3566114, original_name="DPSC"),
        },
    )
    shell_open_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x6A11338F, original_name="ShellOpenSound"),
        },
    )
    shell_close_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xF64CA627, original_name="ShellCloseSound"),
        },
    )
    max_audible_distance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x214E48A0, original_name="MaxAudibleDistance"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "KROC"

    @classmethod
    def modules(cls) -> list[str]:
        return ["WallCrawler.rel", "Krocuss.rel"]

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
        if property_count != 25:
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
                "speed": 3.0,
                "turn_speed": 720.0,
                "detection_range": 5.0,
                "detection_height_range": 5.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "max_attack_range": 20.0,
                "damage_wait_time": 3.0,
                "collision_radius": 0.20000000298023224,
                "collision_height": 5.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733BD27C
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA72530E8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]

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
        assert property_id == 0xD5C25506
        unknown_0xd5c25506 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742EAB20
        projectile_bounds_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80A81909
        collision_look_ahead = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8590483B
        anim_speed_scalar = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3CC437F
        initially_paused = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF04CADCA
        unknown_0xf04cadca = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x497D54E8
        unknown_0x497d54e8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3371C963
        unknown_0x3371c963 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22D37771
        unknown_0x22d37771 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBBEBED9E
        unknown_0xbbebed9e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BD144C8
        shell_closed_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D20624B
        wing_light_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3566114
        dpsc = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A11338F
        shell_open_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF64CA627
        shell_close_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214E48A0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            flavor,
            patterned,
            actor_information,
            waypoint_approach_distance,
            visible_distance,
            wall_turn_speed,
            floor_turn_speed,
            down_turn_speed,
            unknown_0xd5c25506,
            projectile_bounds_multiplier,
            collision_look_ahead,
            anim_speed_scalar,
            initially_paused,
            unknown_0xf04cadca,
            unknown_0x497d54e8,
            unknown_0x3371c963,
            unknown_0x22d37771,
            unknown_0xbbebed9e,
            shell_closed_vulnerability,
            wing_light_color,
            dpsc,
            shell_open_sound,
            shell_close_sound,
            max_audible_distance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x19")  # 25 properties

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
                "speed": 3.0,
                "turn_speed": 720.0,
                "detection_range": 5.0,
                "detection_height_range": 5.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "max_attack_range": 20.0,
                "damage_wait_time": 3.0,
                "collision_radius": 0.20000000298023224,
                "collision_height": 5.0,
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

        data.write(b"s;\xd2|")  # 0x733bd27c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b"\xa7%0\xe8")  # 0xa72530e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b"\xacG\xc6(")  # 0xac47c628
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wall_turn_speed))

        data.write(b"\x8eO{)")  # 0x8e4f7b29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b"=<\x1bv")  # 0x3d3c1b76
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.down_turn_speed))

        data.write(b"\xd5\xc2U\x06")  # 0xd5c25506
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd5c25506))

        data.write(b"t.\xab ")  # 0x742eab20
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_bounds_multiplier))

        data.write(b"\x80\xa8\x19\t")  # 0x80a81909
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.collision_look_ahead))

        data.write(b"\x85\x90H;")  # 0x8590483b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.anim_speed_scalar))

        data.write(b"\xc3\xccC\x7f")  # 0xc3cc437f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.initially_paused))

        data.write(b"\xf0L\xad\xca")  # 0xf04cadca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf04cadca))

        data.write(b"I}T\xe8")  # 0x497d54e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x497d54e8))

        data.write(b"3q\xc9c")  # 0x3371c963
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3371c963))

        data.write(b'"\xd3wq')  # 0x22d37771
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x22d37771))

        data.write(b"\xbb\xeb\xed\x9e")  # 0xbbebed9e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbbebed9e))

        data.write(b"k\xd1D\xc8")  # 0x6bd144c8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shell_closed_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"M bK")  # 0x4d20624b
        data.write(b"\x00\x10")  # size
        self.wing_light_color.to_stream(data, game)

        data.write(b"\xc3Va\x14")  # 0xc3566114
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dpsc))

        data.write(b"j\x113\x8f")  # 0x6a11338f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.shell_open_sound))

        data.write(b"\xf6L\xa6'")  # 0xf64ca627
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.shell_close_sound))

        data.write(b"!NH\xa0")  # 0x214e48a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KrocussJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            flavor=json_data["flavor"],
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            waypoint_approach_distance=json_data["waypoint_approach_distance"],
            visible_distance=json_data["visible_distance"],
            wall_turn_speed=json_data["wall_turn_speed"],
            floor_turn_speed=json_data["floor_turn_speed"],
            down_turn_speed=json_data["down_turn_speed"],
            unknown_0xd5c25506=json_data["unknown_0xd5c25506"],
            projectile_bounds_multiplier=json_data["projectile_bounds_multiplier"],
            collision_look_ahead=json_data["collision_look_ahead"],
            anim_speed_scalar=json_data["anim_speed_scalar"],
            initially_paused=json_data["initially_paused"],
            unknown_0xf04cadca=json_data["unknown_0xf04cadca"],
            unknown_0x497d54e8=json_data["unknown_0x497d54e8"],
            unknown_0x3371c963=json_data["unknown_0x3371c963"],
            unknown_0x22d37771=json_data["unknown_0x22d37771"],
            unknown_0xbbebed9e=json_data["unknown_0xbbebed9e"],
            shell_closed_vulnerability=DamageVulnerability.from_json(json_data["shell_closed_vulnerability"]),
            wing_light_color=Color.from_json(json_data["wing_light_color"]),
            dpsc=json_data["dpsc"],
            shell_open_sound=json_data["shell_open_sound"],
            shell_close_sound=json_data["shell_close_sound"],
            max_audible_distance=json_data["max_audible_distance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "flavor": self.flavor,
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "waypoint_approach_distance": self.waypoint_approach_distance,
            "visible_distance": self.visible_distance,
            "wall_turn_speed": self.wall_turn_speed,
            "floor_turn_speed": self.floor_turn_speed,
            "down_turn_speed": self.down_turn_speed,
            "unknown_0xd5c25506": self.unknown_0xd5c25506,
            "projectile_bounds_multiplier": self.projectile_bounds_multiplier,
            "collision_look_ahead": self.collision_look_ahead,
            "anim_speed_scalar": self.anim_speed_scalar,
            "initially_paused": self.initially_paused,
            "unknown_0xf04cadca": self.unknown_0xf04cadca,
            "unknown_0x497d54e8": self.unknown_0x497d54e8,
            "unknown_0x3371c963": self.unknown_0x3371c963,
            "unknown_0x22d37771": self.unknown_0x22d37771,
            "unknown_0xbbebed9e": self.unknown_0xbbebed9e,
            "shell_closed_vulnerability": self.shell_closed_vulnerability.to_json(),
            "wing_light_color": self.wing_light_color.to_json(),
            "dpsc": self.dpsc,
            "shell_open_sound": self.shell_open_sound,
            "shell_close_sound": self.shell_close_sound,
            "max_audible_distance": self.max_audible_distance,
        }

    def _dependencies_for_dpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dpsc)

    def _dependencies_for_shell_open_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shell_open_sound)

    def _dependencies_for_shell_close_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shell_close_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_dpsc, "dpsc", "AssetId"),
            (self._dependencies_for_shell_open_sound, "shell_open_sound", "int"),
            (self._dependencies_for_shell_close_sound, "shell_close_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Krocuss.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "mass": 25.0,
            "speed": 3.0,
            "turn_speed": 720.0,
            "detection_range": 5.0,
            "detection_height_range": 5.0,
            "detection_angle": 90.0,
            "min_attack_range": 4.0,
            "max_attack_range": 20.0,
            "damage_wait_time": 3.0,
            "collision_radius": 0.20000000298023224,
            "collision_height": 5.0,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_shell_closed_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wing_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xBE73724A: ("flavor", structs.decode_BIG_l),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x733BD27C: ("waypoint_approach_distance", structs.decode_BIG_f),
    0xA72530E8: ("visible_distance", structs.decode_BIG_f),
    0xAC47C628: ("wall_turn_speed", structs.decode_BIG_f),
    0x8E4F7B29: ("floor_turn_speed", structs.decode_BIG_f),
    0x3D3C1B76: ("down_turn_speed", structs.decode_BIG_f),
    0xD5C25506: ("unknown_0xd5c25506", structs.decode_BIG_f),
    0x742EAB20: ("projectile_bounds_multiplier", structs.decode_BIG_f),
    0x80A81909: ("collision_look_ahead", structs.decode_BIG_f),
    0x8590483B: ("anim_speed_scalar", structs.decode_BIG_f),
    0xC3CC437F: ("initially_paused", structs.decode_BIG_bool_),
    0xF04CADCA: ("unknown_0xf04cadca", structs.decode_BIG_f),
    0x497D54E8: ("unknown_0x497d54e8", structs.decode_BIG_f),
    0x3371C963: ("unknown_0x3371c963", structs.decode_BIG_f),
    0x22D37771: ("unknown_0x22d37771", structs.decode_BIG_f),
    0xBBEBED9E: ("unknown_0xbbebed9e", structs.decode_BIG_f),
    0x6BD144C8: ("shell_closed_vulnerability", _decode_shell_closed_vulnerability),
    0x4D20624B: ("wing_light_color", _decode_wing_light_color),
    0xC3566114: ("dpsc", structs.decode_BIG_L),
    0x6A11338F: ("shell_open_sound", structs.decode_BIG_l),
    0xF64CA627: ("shell_close_sound", structs.decode_BIG_l),
    0x214E48A0: ("max_audible_distance", structs.decode_BIG_f),
}
