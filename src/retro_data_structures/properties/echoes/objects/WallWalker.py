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
from retro_data_structures.properties.echoes.archetypes.CameraShakerData import CameraShakerData
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

    class WallWalkerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        leg_vulnerability: json_util.JsonObject
        waypoint_approach_distance: float
        floor_turn_speed: float
        unknown_0xd5c25506: float
        visible_distance: float
        explode_damage: json_util.JsonObject
        grenade_explosion: int
        grenade_effect: int
        grenade_trail: int
        grenade_mass: float
        unknown_0xed086ce0: float
        unknown_0x454f16b1: int
        unknown_0x7f1613b7: int
        unknown_0x7050d866: int
        projectile_interval: float
        unknown_0x723542bb: float
        projectile: int
        projectile_damage: json_util.JsonObject
        part: int
        camera_shaker_data: json_util.JsonObject


@dataclasses.dataclass()
class WallWalker(BaseObjectType):
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
    leg_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x9F0FF852,
                original_name="LegVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    waypoint_approach_distance: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x733BD27C, original_name="WaypointApproachDistance"),
        },
    )
    floor_turn_speed: float = dataclasses.field(
        default=1080.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E4F7B29, original_name="FloorTurnSpeed"),
        },
    )
    unknown_0xd5c25506: float = dataclasses.field(
        default=0.4000000059604645,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5C25506, original_name="Unknown"),
        },
    )
    visible_distance: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA72530E8, original_name="VisibleDistance"),
        },
    )
    explode_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xF6206A12,
                original_name="ExplodeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    grenade_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1319E077, original_name="GrenadeExplosion"),
        },
    )
    grenade_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD207FF0F, original_name="GrenadeEffect"),
        },
    )
    grenade_trail: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2B31C882, original_name="GrenadeTrail"),
        },
    )
    grenade_mass: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9A6BB47F, original_name="GrenadeMass"),
        },
    )
    unknown_0xed086ce0: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED086CE0, original_name="Unknown"),
        },
    )
    unknown_0x454f16b1: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0x454F16B1, original_name="Unknown"),
        },
    )
    unknown_0x7f1613b7: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x7F1613B7, original_name="Unknown"),
        },
    )
    unknown_0x7050d866: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x7050D866, original_name="Unknown"),
        },
    )
    projectile_interval: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4903C98, original_name="ProjectileInterval"),
        },
    )
    unknown_0x723542bb: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x723542BB, original_name="Unknown"),
        },
    )
    projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEF485DB9, original_name="Projectile"),
        },
    )
    projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x553B1339,
                original_name="ProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x68DC4D11, original_name="PART"),
        },
    )
    camera_shaker_data: CameraShakerData = dataclasses.field(
        default_factory=CameraShakerData,
        metadata={
            "reflection": FieldReflection[CameraShakerData](
                CameraShakerData,
                id=0x22BBDD0A,
                original_name="CameraShakerData",
                from_json=CameraShakerData.from_json,
                to_json=CameraShakerData.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "WLWK"

    @classmethod
    def modules(cls) -> list[str]:
        return ["WallCrawler.rel", "WallWalker.rel"]

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
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={"creature_size": 1})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F0FF852
        leg_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733BD27C
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E4F7B29
        floor_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5C25506
        unknown_0xd5c25506 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA72530E8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF6206A12
        explode_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1319E077
        grenade_explosion = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD207FF0F
        grenade_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B31C882
        grenade_trail = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A6BB47F
        grenade_mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED086CE0
        unknown_0xed086ce0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x454F16B1
        unknown_0x454f16b1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F1613B7
        unknown_0x7f1613b7 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7050D866
        unknown_0x7050d866 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4903C98
        projectile_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723542BB
        unknown_0x723542bb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553B1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68DC4D11
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22BBDD0A
        camera_shaker_data = CameraShakerData.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            patterned,
            actor_information,
            leg_vulnerability,
            waypoint_approach_distance,
            floor_turn_speed,
            unknown_0xd5c25506,
            visible_distance,
            explode_damage,
            grenade_explosion,
            grenade_effect,
            grenade_trail,
            grenade_mass,
            unknown_0xed086ce0,
            unknown_0x454f16b1,
            unknown_0x7f1613b7,
            unknown_0x7050d866,
            projectile_interval,
            unknown_0x723542bb,
            projectile,
            projectile_damage,
            part,
            camera_shaker_data,
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

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(data, game, default_override={"creature_size": 1})
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

        data.write(b"\x9f\x0f\xf8R")  # 0x9f0ff852
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.leg_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"s;\xd2|")  # 0x733bd27c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b"\x8eO{)")  # 0x8e4f7b29
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b"\xd5\xc2U\x06")  # 0xd5c25506
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd5c25506))

        data.write(b"\xa7%0\xe8")  # 0xa72530e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b"\xf6 j\x12")  # 0xf6206a12
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.explode_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x13\x19\xe0w")  # 0x1319e077
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.grenade_explosion))

        data.write(b"\xd2\x07\xff\x0f")  # 0xd207ff0f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.grenade_effect))

        data.write(b"+1\xc8\x82")  # 0x2b31c882
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.grenade_trail))

        data.write(b"\x9ak\xb4\x7f")  # 0x9a6bb47f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grenade_mass))

        data.write(b"\xed\x08l\xe0")  # 0xed086ce0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xed086ce0))

        data.write(b"EO\x16\xb1")  # 0x454f16b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x454f16b1))

        data.write(b"\x7f\x16\x13\xb7")  # 0x7f1613b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7f1613b7))

        data.write(b"pP\xd8f")  # 0x7050d866
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7050d866))

        data.write(b"\xd4\x90<\x98")  # 0xd4903c98
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_interval))

        data.write(b"r5B\xbb")  # 0x723542bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x723542bb))

        data.write(b"\xefH]\xb9")  # 0xef485db9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b"U;\x139")  # 0x553b1339
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"h\xdcM\x11")  # 0x68dc4d11
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b'"\xbb\xdd\n')  # 0x22bbdd0a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_shaker_data.to_stream(data, game)
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
        json_data = typing.cast("WallWalkerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            leg_vulnerability=DamageVulnerability.from_json(json_data["leg_vulnerability"]),
            waypoint_approach_distance=json_data["waypoint_approach_distance"],
            floor_turn_speed=json_data["floor_turn_speed"],
            unknown_0xd5c25506=json_data["unknown_0xd5c25506"],
            visible_distance=json_data["visible_distance"],
            explode_damage=DamageInfo.from_json(json_data["explode_damage"]),
            grenade_explosion=json_data["grenade_explosion"],
            grenade_effect=json_data["grenade_effect"],
            grenade_trail=json_data["grenade_trail"],
            grenade_mass=json_data["grenade_mass"],
            unknown_0xed086ce0=json_data["unknown_0xed086ce0"],
            unknown_0x454f16b1=json_data["unknown_0x454f16b1"],
            unknown_0x7f1613b7=json_data["unknown_0x7f1613b7"],
            unknown_0x7050d866=json_data["unknown_0x7050d866"],
            projectile_interval=json_data["projectile_interval"],
            unknown_0x723542bb=json_data["unknown_0x723542bb"],
            projectile=json_data["projectile"],
            projectile_damage=DamageInfo.from_json(json_data["projectile_damage"]),
            part=json_data["part"],
            camera_shaker_data=CameraShakerData.from_json(json_data["camera_shaker_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "leg_vulnerability": self.leg_vulnerability.to_json(),
            "waypoint_approach_distance": self.waypoint_approach_distance,
            "floor_turn_speed": self.floor_turn_speed,
            "unknown_0xd5c25506": self.unknown_0xd5c25506,
            "visible_distance": self.visible_distance,
            "explode_damage": self.explode_damage.to_json(),
            "grenade_explosion": self.grenade_explosion,
            "grenade_effect": self.grenade_effect,
            "grenade_trail": self.grenade_trail,
            "grenade_mass": self.grenade_mass,
            "unknown_0xed086ce0": self.unknown_0xed086ce0,
            "unknown_0x454f16b1": self.unknown_0x454f16b1,
            "unknown_0x7f1613b7": self.unknown_0x7f1613b7,
            "unknown_0x7050d866": self.unknown_0x7050d866,
            "projectile_interval": self.projectile_interval,
            "unknown_0x723542bb": self.unknown_0x723542bb,
            "projectile": self.projectile,
            "projectile_damage": self.projectile_damage.to_json(),
            "part": self.part,
            "camera_shaker_data": self.camera_shaker_data.to_json(),
        }

    def _dependencies_for_grenade_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_explosion)

    def _dependencies_for_grenade_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_effect)

    def _dependencies_for_grenade_trail(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_trail)

    def _dependencies_for_unknown_0x7f1613b7(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0x7f1613b7)

    def _dependencies_for_unknown_0x7050d866(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unknown_0x7050d866)

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_grenade_explosion, "grenade_explosion", "AssetId"),
            (self._dependencies_for_grenade_effect, "grenade_effect", "AssetId"),
            (self._dependencies_for_grenade_trail, "grenade_trail", "AssetId"),
            (self._dependencies_for_unknown_0x7f1613b7, "unknown_0x7f1613b7", "int"),
            (self._dependencies_for_unknown_0x7050d866, "unknown_0x7050d866", "int"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self.camera_shaker_data.dependencies_for, "camera_shaker_data", "CameraShakerData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for WallWalker.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={"creature_size": 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_leg_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_explode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_camera_shaker_data(data: typing.BinaryIO, game: Game, property_size: int) -> CameraShakerData:
    return CameraShakerData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x9F0FF852: ("leg_vulnerability", _decode_leg_vulnerability),
    0x733BD27C: ("waypoint_approach_distance", structs.decode_BIG_f),
    0x8E4F7B29: ("floor_turn_speed", structs.decode_BIG_f),
    0xD5C25506: ("unknown_0xd5c25506", structs.decode_BIG_f),
    0xA72530E8: ("visible_distance", structs.decode_BIG_f),
    0xF6206A12: ("explode_damage", _decode_explode_damage),
    0x1319E077: ("grenade_explosion", structs.decode_BIG_L),
    0xD207FF0F: ("grenade_effect", structs.decode_BIG_L),
    0x2B31C882: ("grenade_trail", structs.decode_BIG_L),
    0x9A6BB47F: ("grenade_mass", structs.decode_BIG_f),
    0xED086CE0: ("unknown_0xed086ce0", structs.decode_BIG_f),
    0x454F16B1: ("unknown_0x454f16b1", structs.decode_BIG_l),
    0x7F1613B7: ("unknown_0x7f1613b7", structs.decode_BIG_l),
    0x7050D866: ("unknown_0x7050d866", structs.decode_BIG_l),
    0xD4903C98: ("projectile_interval", structs.decode_BIG_f),
    0x723542BB: ("unknown_0x723542bb", structs.decode_BIG_f),
    0xEF485DB9: ("projectile", structs.decode_BIG_L),
    0x553B1339: ("projectile_damage", _decode_projectile_damage),
    0x68DC4D11: ("part", structs.decode_BIG_L),
    0x22BBDD0A: ("camera_shaker_data", _decode_camera_shaker_data),
}
