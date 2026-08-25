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
from retro_data_structures.properties.echoes.archetypes.BasicSwarmProperties import BasicSwarmProperties
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class BacteriaSwarmJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        animation_information: json_util.JsonObject
        active: bool
        basic_swarm_properties: json_util.JsonObject
        unknown_0x4a85a2da: float
        containment_priority: float
        bacteria_patrol_speed: float
        unknown_0x7de56d56: float
        unknown_0x39098c47: float
        bacteria_acceleration: float
        bacteria_deceleration: float
        patrol_turn_speed: float
        unknown_0xbdcdb9c0: float
        bacteria_particle_effect: int
        bacteria_patrol_color: json_util.JsonValue
        bacteria_player_pursuit_color: json_util.JsonValue
        color_change_time: float
        patrol_sound: int
        pursuit_sound: int
        unknown_0xad4ce8f3: float
        unknown_0xa9d6d9d9: float
        patrol_sound_weight: float
        unknown_0x90f8e29f: float
        unknown_0x4b47b178: float
        pursuit_sound_weight: float
        unknown_0xd2986c43: float
        max_audible_distance: float
        min_volume: int
        max_volume: int
        bacteria_scan_model: int
        spawn_instantly: bool


@dataclasses.dataclass()
class BacteriaSwarm(BaseObjectType):
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
    animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xE25FB08C,
                original_name="AnimationInformation",
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
    basic_swarm_properties: BasicSwarmProperties = dataclasses.field(
        default_factory=BasicSwarmProperties,
        metadata={
            "reflection": FieldReflection[BasicSwarmProperties](
                BasicSwarmProperties,
                id=0xE1EC7346,
                original_name="BasicSwarmProperties",
                from_json=BasicSwarmProperties.from_json,
                to_json=BasicSwarmProperties.to_json,
            ),
        },
    )
    unknown_0x4a85a2da: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4A85A2DA, original_name="Unknown"),
        },
    )
    containment_priority: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FF1469E, original_name="ContainmentPriority"),
        },
    )
    bacteria_patrol_speed: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF87FD6A9, original_name="BacteriaPatrolSpeed"),
        },
    )
    unknown_0x7de56d56: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7DE56D56, original_name="Unknown"),
        },
    )
    unknown_0x39098c47: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x39098C47, original_name="Unknown"),
        },
    )
    bacteria_acceleration: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFBA2A53E, original_name="BacteriaAcceleration"),
        },
    )
    bacteria_deceleration: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5C9D2056, original_name="BacteriaDeceleration"),
        },
    )
    patrol_turn_speed: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x771A90E6, original_name="PatrolTurnSpeed"),
        },
    )
    unknown_0xbdcdb9c0: float = dataclasses.field(
        default=1440.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBDCDB9C0, original_name="Unknown"),
        },
    )
    bacteria_particle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2301294A, original_name="BacteriaParticleEffect"),
        },
    )
    bacteria_patrol_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0xAC2A467A,
                original_name="BacteriaPatrolColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    bacteria_player_pursuit_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x6D5C1C94,
                original_name="BacteriaPlayerPursuitColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    color_change_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x311B0750, original_name="ColorChangeTime"),
        },
    )
    patrol_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x4AB24275, original_name="PatrolSound"),
        },
    )
    pursuit_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xFE3E7BBF, original_name="PursuitSound"),
        },
    )
    unknown_0xad4ce8f3: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD4CE8F3, original_name="Unknown"),
        },
    )
    unknown_0xa9d6d9d9: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA9D6D9D9, original_name="Unknown"),
        },
    )
    patrol_sound_weight: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9FE253A5, original_name="PatrolSoundWeight"),
        },
    )
    unknown_0x90f8e29f: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x90F8E29F, original_name="Unknown"),
        },
    )
    unknown_0x4b47b178: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B47B178, original_name="Unknown"),
        },
    )
    pursuit_sound_weight: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE678EBCF, original_name="PursuitSoundWeight"),
        },
    )
    unknown_0xd2986c43: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD2986C43, original_name="Unknown"),
        },
    )
    max_audible_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x214E48A0, original_name="MaxAudibleDistance"),
        },
    )
    min_volume: int = dataclasses.field(
        default=20,
        metadata={
            "reflection": FieldReflection[int](int, id=0x57619496, original_name="MinVolume"),
        },
    )
    max_volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC712847C, original_name="MaxVolume"),
        },
    )
    bacteria_scan_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x757A1C34, original_name="BacteriaScanModel"),
        },
    )
    spawn_instantly: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC5BC5ED0, original_name="SpawnInstantly"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "BSWM"

    @classmethod
    def modules(cls) -> list[str]:
        return ["BacteriaSwarm.rel"]

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
        if property_count != 32:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE25FB08C
        animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6BB2F45
        active = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1EC7346
        basic_swarm_properties = BasicSwarmProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A85A2DA
        unknown_0x4a85a2da = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FF1469E
        containment_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF87FD6A9
        bacteria_patrol_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DE56D56
        unknown_0x7de56d56 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39098C47
        unknown_0x39098c47 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBA2A53E
        bacteria_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C9D2056
        bacteria_deceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x771A90E6
        patrol_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBDCDB9C0
        unknown_0xbdcdb9c0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2301294A
        bacteria_particle_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC2A467A
        bacteria_patrol_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D5C1C94
        bacteria_player_pursuit_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x311B0750
        color_change_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AB24275
        patrol_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE3E7BBF
        pursuit_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD4CE8F3
        unknown_0xad4ce8f3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9D6D9D9
        unknown_0xa9d6d9d9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9FE253A5
        patrol_sound_weight = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90F8E29F
        unknown_0x90f8e29f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B47B178
        unknown_0x4b47b178 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE678EBCF
        pursuit_sound_weight = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD2986C43
        unknown_0xd2986c43 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214E48A0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57619496
        min_volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC712847C
        max_volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x757A1C34
        bacteria_scan_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5BC5ED0
        spawn_instantly = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            actor_information,
            animation_information,
            active,
            basic_swarm_properties,
            unknown_0x4a85a2da,
            containment_priority,
            bacteria_patrol_speed,
            unknown_0x7de56d56,
            unknown_0x39098c47,
            bacteria_acceleration,
            bacteria_deceleration,
            patrol_turn_speed,
            unknown_0xbdcdb9c0,
            bacteria_particle_effect,
            bacteria_patrol_color,
            bacteria_player_pursuit_color,
            color_change_time,
            patrol_sound,
            pursuit_sound,
            unknown_0xad4ce8f3,
            unknown_0xa9d6d9d9,
            patrol_sound_weight,
            unknown_0x90f8e29f,
            unknown_0x4b47b178,
            pursuit_sound_weight,
            unknown_0xd2986c43,
            max_audible_distance,
            min_volume,
            max_volume,
            bacteria_scan_model,
            spawn_instantly,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00 ")  # 32 properties

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

        data.write(b"\xe2_\xb0\x8c")  # 0xe25fb08c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\xbb/E")  # 0xc6bb2f45
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.active))

        data.write(b"\xe1\xecsF")  # 0xe1ec7346
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.basic_swarm_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"J\x85\xa2\xda")  # 0x4a85a2da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4a85a2da))

        data.write(b"\x7f\xf1F\x9e")  # 0x7ff1469e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.containment_priority))

        data.write(b"\xf8\x7f\xd6\xa9")  # 0xf87fd6a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bacteria_patrol_speed))

        data.write(b"}\xe5mV")  # 0x7de56d56
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7de56d56))

        data.write(b"9\t\x8cG")  # 0x39098c47
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x39098c47))

        data.write(b"\xfb\xa2\xa5>")  # 0xfba2a53e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bacteria_acceleration))

        data.write(b"\\\x9d V")  # 0x5c9d2056
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bacteria_deceleration))

        data.write(b"w\x1a\x90\xe6")  # 0x771a90e6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.patrol_turn_speed))

        data.write(b"\xbd\xcd\xb9\xc0")  # 0xbdcdb9c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbdcdb9c0))

        data.write(b"#\x01)J")  # 0x2301294a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.bacteria_particle_effect))

        data.write(b"\xac*Fz")  # 0xac2a467a
        data.write(b"\x00\x10")  # size
        self.bacteria_patrol_color.to_stream(data, game)

        data.write(b"m\\\x1c\x94")  # 0x6d5c1c94
        data.write(b"\x00\x10")  # size
        self.bacteria_player_pursuit_color.to_stream(data, game)

        data.write(b"1\x1b\x07P")  # 0x311b0750
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.color_change_time))

        data.write(b"J\xb2Bu")  # 0x4ab24275
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.patrol_sound))

        data.write(b"\xfe>{\xbf")  # 0xfe3e7bbf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.pursuit_sound))

        data.write(b"\xadL\xe8\xf3")  # 0xad4ce8f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xad4ce8f3))

        data.write(b"\xa9\xd6\xd9\xd9")  # 0xa9d6d9d9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa9d6d9d9))

        data.write(b"\x9f\xe2S\xa5")  # 0x9fe253a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.patrol_sound_weight))

        data.write(b"\x90\xf8\xe2\x9f")  # 0x90f8e29f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x90f8e29f))

        data.write(b"KG\xb1x")  # 0x4b47b178
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4b47b178))

        data.write(b"\xe6x\xeb\xcf")  # 0xe678ebcf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pursuit_sound_weight))

        data.write(b"\xd2\x98lC")  # 0xd2986c43
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd2986c43))

        data.write(b"!NH\xa0")  # 0x214e48a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b"Wa\x94\x96")  # 0x57619496
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.min_volume))

        data.write(b"\xc7\x12\x84|")  # 0xc712847c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_volume))

        data.write(b"uz\x1c4")  # 0x757a1c34
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.bacteria_scan_model))

        data.write(b"\xc5\xbc^\xd0")  # 0xc5bc5ed0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.spawn_instantly))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BacteriaSwarmJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            active=json_data["active"],
            basic_swarm_properties=BasicSwarmProperties.from_json(json_data["basic_swarm_properties"]),
            unknown_0x4a85a2da=json_data["unknown_0x4a85a2da"],
            containment_priority=json_data["containment_priority"],
            bacteria_patrol_speed=json_data["bacteria_patrol_speed"],
            unknown_0x7de56d56=json_data["unknown_0x7de56d56"],
            unknown_0x39098c47=json_data["unknown_0x39098c47"],
            bacteria_acceleration=json_data["bacteria_acceleration"],
            bacteria_deceleration=json_data["bacteria_deceleration"],
            patrol_turn_speed=json_data["patrol_turn_speed"],
            unknown_0xbdcdb9c0=json_data["unknown_0xbdcdb9c0"],
            bacteria_particle_effect=json_data["bacteria_particle_effect"],
            bacteria_patrol_color=Color.from_json(json_data["bacteria_patrol_color"]),
            bacteria_player_pursuit_color=Color.from_json(json_data["bacteria_player_pursuit_color"]),
            color_change_time=json_data["color_change_time"],
            patrol_sound=json_data["patrol_sound"],
            pursuit_sound=json_data["pursuit_sound"],
            unknown_0xad4ce8f3=json_data["unknown_0xad4ce8f3"],
            unknown_0xa9d6d9d9=json_data["unknown_0xa9d6d9d9"],
            patrol_sound_weight=json_data["patrol_sound_weight"],
            unknown_0x90f8e29f=json_data["unknown_0x90f8e29f"],
            unknown_0x4b47b178=json_data["unknown_0x4b47b178"],
            pursuit_sound_weight=json_data["pursuit_sound_weight"],
            unknown_0xd2986c43=json_data["unknown_0xd2986c43"],
            max_audible_distance=json_data["max_audible_distance"],
            min_volume=json_data["min_volume"],
            max_volume=json_data["max_volume"],
            bacteria_scan_model=json_data["bacteria_scan_model"],
            spawn_instantly=json_data["spawn_instantly"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "animation_information": self.animation_information.to_json(),
            "active": self.active,
            "basic_swarm_properties": self.basic_swarm_properties.to_json(),
            "unknown_0x4a85a2da": self.unknown_0x4a85a2da,
            "containment_priority": self.containment_priority,
            "bacteria_patrol_speed": self.bacteria_patrol_speed,
            "unknown_0x7de56d56": self.unknown_0x7de56d56,
            "unknown_0x39098c47": self.unknown_0x39098c47,
            "bacteria_acceleration": self.bacteria_acceleration,
            "bacteria_deceleration": self.bacteria_deceleration,
            "patrol_turn_speed": self.patrol_turn_speed,
            "unknown_0xbdcdb9c0": self.unknown_0xbdcdb9c0,
            "bacteria_particle_effect": self.bacteria_particle_effect,
            "bacteria_patrol_color": self.bacteria_patrol_color.to_json(),
            "bacteria_player_pursuit_color": self.bacteria_player_pursuit_color.to_json(),
            "color_change_time": self.color_change_time,
            "patrol_sound": self.patrol_sound,
            "pursuit_sound": self.pursuit_sound,
            "unknown_0xad4ce8f3": self.unknown_0xad4ce8f3,
            "unknown_0xa9d6d9d9": self.unknown_0xa9d6d9d9,
            "patrol_sound_weight": self.patrol_sound_weight,
            "unknown_0x90f8e29f": self.unknown_0x90f8e29f,
            "unknown_0x4b47b178": self.unknown_0x4b47b178,
            "pursuit_sound_weight": self.pursuit_sound_weight,
            "unknown_0xd2986c43": self.unknown_0xd2986c43,
            "max_audible_distance": self.max_audible_distance,
            "min_volume": self.min_volume,
            "max_volume": self.max_volume,
            "bacteria_scan_model": self.bacteria_scan_model,
            "spawn_instantly": self.spawn_instantly,
        }

    def _dependencies_for_bacteria_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bacteria_particle_effect)

    def _dependencies_for_patrol_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.patrol_sound)

    def _dependencies_for_pursuit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.pursuit_sound)

    def _dependencies_for_bacteria_scan_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bacteria_scan_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.basic_swarm_properties.dependencies_for, "basic_swarm_properties", "BasicSwarmProperties"),
            (self._dependencies_for_bacteria_particle_effect, "bacteria_particle_effect", "AssetId"),
            (self._dependencies_for_patrol_sound, "patrol_sound", "int"),
            (self._dependencies_for_pursuit_sound, "pursuit_sound", "int"),
            (self._dependencies_for_bacteria_scan_model, "bacteria_scan_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for BacteriaSwarm.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_basic_swarm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> BasicSwarmProperties:
    return BasicSwarmProperties.from_stream(data, game, property_size)


def _decode_bacteria_patrol_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_bacteria_player_pursuit_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0xC6BB2F45: ("active", structs.decode_BIG_bool_),
    0xE1EC7346: ("basic_swarm_properties", _decode_basic_swarm_properties),
    0x4A85A2DA: ("unknown_0x4a85a2da", structs.decode_BIG_f),
    0x7FF1469E: ("containment_priority", structs.decode_BIG_f),
    0xF87FD6A9: ("bacteria_patrol_speed", structs.decode_BIG_f),
    0x7DE56D56: ("unknown_0x7de56d56", structs.decode_BIG_f),
    0x39098C47: ("unknown_0x39098c47", structs.decode_BIG_f),
    0xFBA2A53E: ("bacteria_acceleration", structs.decode_BIG_f),
    0x5C9D2056: ("bacteria_deceleration", structs.decode_BIG_f),
    0x771A90E6: ("patrol_turn_speed", structs.decode_BIG_f),
    0xBDCDB9C0: ("unknown_0xbdcdb9c0", structs.decode_BIG_f),
    0x2301294A: ("bacteria_particle_effect", structs.decode_BIG_L),
    0xAC2A467A: ("bacteria_patrol_color", _decode_bacteria_patrol_color),
    0x6D5C1C94: ("bacteria_player_pursuit_color", _decode_bacteria_player_pursuit_color),
    0x311B0750: ("color_change_time", structs.decode_BIG_f),
    0x4AB24275: ("patrol_sound", structs.decode_BIG_l),
    0xFE3E7BBF: ("pursuit_sound", structs.decode_BIG_l),
    0xAD4CE8F3: ("unknown_0xad4ce8f3", structs.decode_BIG_f),
    0xA9D6D9D9: ("unknown_0xa9d6d9d9", structs.decode_BIG_f),
    0x9FE253A5: ("patrol_sound_weight", structs.decode_BIG_f),
    0x90F8E29F: ("unknown_0x90f8e29f", structs.decode_BIG_f),
    0x4B47B178: ("unknown_0x4b47b178", structs.decode_BIG_f),
    0xE678EBCF: ("pursuit_sound_weight", structs.decode_BIG_f),
    0xD2986C43: ("unknown_0xd2986c43", structs.decode_BIG_f),
    0x214E48A0: ("max_audible_distance", structs.decode_BIG_f),
    0x57619496: ("min_volume", structs.decode_BIG_l),
    0xC712847C: ("max_volume", structs.decode_BIG_l),
    0x757A1C34: ("bacteria_scan_model", structs.decode_BIG_L),
    0xC5BC5ED0: ("spawn_instantly", structs.decode_BIG_bool_),
}
