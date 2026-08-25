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
from retro_data_structures.properties.echoes.archetypes.BasicSwarmProperties import BasicSwarmProperties
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PlantScarabSwarmJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        animation_information: json_util.JsonObject
        active: bool
        basic_swarm_properties: json_util.JsonObject
        unknown_0x7399abbb: int
        unknown_0x734d923b: int
        max_attack_angle: float
        into_attack_speed: float
        attack_speed: float
        grenade_mass: float
        grenade_launch_speed: float
        unknown_0xed086ce0: float
        unknown_0x454f16b1: int
        grenade_damage: json_util.JsonObject
        grenade_explosion_proximity: float
        grenade_explosion_effect: int
        part: int
        grenade_trail_effect: int
        grenade_effect: int
        grenade_bounce_sound: int
        grenade_bounce_sound_fall_off: float
        unknown_0x15e0c159: float
        grenade_explosion_sound: int
        grenade_explosion_sound_fall_off: float
        unknown_0xab84892e: float


@dataclasses.dataclass()
class PlantScarabSwarm(BaseObjectType):
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
    unknown_0x7399abbb: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7399ABBB, original_name="Unknown"),
        },
    )
    unknown_0x734d923b: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x734D923B, original_name="Unknown"),
        },
    )
    max_attack_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF11F7384, original_name="MaxAttackAngle"),
        },
    )
    into_attack_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCA761DCD, original_name="IntoAttackSpeed"),
        },
    )
    attack_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C0A2BC8, original_name="AttackSpeed"),
        },
    )
    grenade_mass: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9A6BB47F, original_name="GrenadeMass"),
        },
    )
    grenade_launch_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16962C9B, original_name="GrenadeLaunchSpeed"),
        },
    )
    unknown_0xed086ce0: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED086CE0, original_name="Unknown"),
        },
    )
    unknown_0x454f16b1: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x454F16B1, original_name="Unknown"),
        },
    )
    grenade_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x14D1A3A8,
                original_name="GrenadeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    grenade_explosion_proximity: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C7CA121, original_name="GrenadeExplosionProximity"),
        },
    )
    grenade_explosion_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEA500E8B, original_name="GrenadeExplosionEffect"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x40992D51, original_name="PART"),
        },
    )
    grenade_trail_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1140D11D, original_name="GrenadeTrailEffect"),
        },
    )
    grenade_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD207FF0F, original_name="GrenadeEffect"),
        },
    )
    grenade_bounce_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x2C1DFA22, original_name="GrenadeBounceSound"),
        },
    )
    grenade_bounce_sound_fall_off: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x285EFBD9, original_name="GrenadeBounceSoundFallOff"),
        },
    )
    unknown_0x15e0c159: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x15E0C159, original_name="Unknown"),
        },
    )
    grenade_explosion_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x30752C95, original_name="GrenadeExplosionSound"),
        },
    )
    grenade_explosion_sound_fall_off: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA66A16E, original_name="GrenadeExplosionSoundFallOff"),
        },
    )
    unknown_0xab84892e: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAB84892E, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PSSM"

    @classmethod
    def modules(cls) -> list[str]:
        return ["SwarmBasics.rel", "PlantScarabSwarm.rel"]

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
        if property_count != 26:
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
        assert property_id == 0x7399ABBB
        unknown_0x7399abbb = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x734D923B
        unknown_0x734d923b = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF11F7384
        max_attack_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCA761DCD
        into_attack_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C0A2BC8
        attack_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A6BB47F
        grenade_mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16962C9B
        grenade_launch_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED086CE0
        unknown_0xed086ce0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x454F16B1
        unknown_0x454f16b1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14D1A3A8
        grenade_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C7CA121
        grenade_explosion_proximity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA500E8B
        grenade_explosion_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40992D51
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1140D11D
        grenade_trail_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD207FF0F
        grenade_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C1DFA22
        grenade_bounce_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x285EFBD9
        grenade_bounce_sound_fall_off = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15E0C159
        unknown_0x15e0c159 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30752C95
        grenade_explosion_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA66A16E
        grenade_explosion_sound_fall_off = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB84892E
        unknown_0xab84892e = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            actor_information,
            animation_information,
            active,
            basic_swarm_properties,
            unknown_0x7399abbb,
            unknown_0x734d923b,
            max_attack_angle,
            into_attack_speed,
            attack_speed,
            grenade_mass,
            grenade_launch_speed,
            unknown_0xed086ce0,
            unknown_0x454f16b1,
            grenade_damage,
            grenade_explosion_proximity,
            grenade_explosion_effect,
            part,
            grenade_trail_effect,
            grenade_effect,
            grenade_bounce_sound,
            grenade_bounce_sound_fall_off,
            unknown_0x15e0c159,
            grenade_explosion_sound,
            grenade_explosion_sound_fall_off,
            unknown_0xab84892e,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x1a")  # 26 properties

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

        data.write(b"s\x99\xab\xbb")  # 0x7399abbb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7399abbb))

        data.write(b"sM\x92;")  # 0x734d923b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x734d923b))

        data.write(b"\xf1\x1fs\x84")  # 0xf11f7384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_angle))

        data.write(b"\xcav\x1d\xcd")  # 0xca761dcd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.into_attack_speed))

        data.write(b"l\n+\xc8")  # 0x6c0a2bc8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_speed))

        data.write(b"\x9ak\xb4\x7f")  # 0x9a6bb47f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grenade_mass))

        data.write(b"\x16\x96,\x9b")  # 0x16962c9b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grenade_launch_speed))

        data.write(b"\xed\x08l\xe0")  # 0xed086ce0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xed086ce0))

        data.write(b"EO\x16\xb1")  # 0x454f16b1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x454f16b1))

        data.write(b"\x14\xd1\xa3\xa8")  # 0x14d1a3a8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grenade_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"l|\xa1!")  # 0x6c7ca121
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grenade_explosion_proximity))

        data.write(b"\xeaP\x0e\x8b")  # 0xea500e8b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.grenade_explosion_effect))

        data.write(b"@\x99-Q")  # 0x40992d51
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b"\x11@\xd1\x1d")  # 0x1140d11d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.grenade_trail_effect))

        data.write(b"\xd2\x07\xff\x0f")  # 0xd207ff0f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.grenade_effect))

        data.write(b',\x1d\xfa"')  # 0x2c1dfa22
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grenade_bounce_sound))

        data.write(b"(^\xfb\xd9")  # 0x285efbd9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grenade_bounce_sound_fall_off))

        data.write(b"\x15\xe0\xc1Y")  # 0x15e0c159
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x15e0c159))

        data.write(b"0u,\x95")  # 0x30752c95
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grenade_explosion_sound))

        data.write(b"\xbaf\xa1n")  # 0xba66a16e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grenade_explosion_sound_fall_off))

        data.write(b"\xab\x84\x89.")  # 0xab84892e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xab84892e))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlantScarabSwarmJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            animation_information=AnimationParameters.from_json(json_data["animation_information"]),
            active=json_data["active"],
            basic_swarm_properties=BasicSwarmProperties.from_json(json_data["basic_swarm_properties"]),
            unknown_0x7399abbb=json_data["unknown_0x7399abbb"],
            unknown_0x734d923b=json_data["unknown_0x734d923b"],
            max_attack_angle=json_data["max_attack_angle"],
            into_attack_speed=json_data["into_attack_speed"],
            attack_speed=json_data["attack_speed"],
            grenade_mass=json_data["grenade_mass"],
            grenade_launch_speed=json_data["grenade_launch_speed"],
            unknown_0xed086ce0=json_data["unknown_0xed086ce0"],
            unknown_0x454f16b1=json_data["unknown_0x454f16b1"],
            grenade_damage=DamageInfo.from_json(json_data["grenade_damage"]),
            grenade_explosion_proximity=json_data["grenade_explosion_proximity"],
            grenade_explosion_effect=json_data["grenade_explosion_effect"],
            part=json_data["part"],
            grenade_trail_effect=json_data["grenade_trail_effect"],
            grenade_effect=json_data["grenade_effect"],
            grenade_bounce_sound=json_data["grenade_bounce_sound"],
            grenade_bounce_sound_fall_off=json_data["grenade_bounce_sound_fall_off"],
            unknown_0x15e0c159=json_data["unknown_0x15e0c159"],
            grenade_explosion_sound=json_data["grenade_explosion_sound"],
            grenade_explosion_sound_fall_off=json_data["grenade_explosion_sound_fall_off"],
            unknown_0xab84892e=json_data["unknown_0xab84892e"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "animation_information": self.animation_information.to_json(),
            "active": self.active,
            "basic_swarm_properties": self.basic_swarm_properties.to_json(),
            "unknown_0x7399abbb": self.unknown_0x7399abbb,
            "unknown_0x734d923b": self.unknown_0x734d923b,
            "max_attack_angle": self.max_attack_angle,
            "into_attack_speed": self.into_attack_speed,
            "attack_speed": self.attack_speed,
            "grenade_mass": self.grenade_mass,
            "grenade_launch_speed": self.grenade_launch_speed,
            "unknown_0xed086ce0": self.unknown_0xed086ce0,
            "unknown_0x454f16b1": self.unknown_0x454f16b1,
            "grenade_damage": self.grenade_damage.to_json(),
            "grenade_explosion_proximity": self.grenade_explosion_proximity,
            "grenade_explosion_effect": self.grenade_explosion_effect,
            "part": self.part,
            "grenade_trail_effect": self.grenade_trail_effect,
            "grenade_effect": self.grenade_effect,
            "grenade_bounce_sound": self.grenade_bounce_sound,
            "grenade_bounce_sound_fall_off": self.grenade_bounce_sound_fall_off,
            "unknown_0x15e0c159": self.unknown_0x15e0c159,
            "grenade_explosion_sound": self.grenade_explosion_sound,
            "grenade_explosion_sound_fall_off": self.grenade_explosion_sound_fall_off,
            "unknown_0xab84892e": self.unknown_0xab84892e,
        }

    def _dependencies_for_grenade_explosion_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_explosion_effect)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_grenade_trail_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_trail_effect)

    def _dependencies_for_grenade_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_effect)

    def _dependencies_for_grenade_bounce_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grenade_bounce_sound)

    def _dependencies_for_grenade_explosion_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grenade_explosion_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self.basic_swarm_properties.dependencies_for, "basic_swarm_properties", "BasicSwarmProperties"),
            (self._dependencies_for_grenade_explosion_effect, "grenade_explosion_effect", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self._dependencies_for_grenade_trail_effect, "grenade_trail_effect", "AssetId"),
            (self._dependencies_for_grenade_effect, "grenade_effect", "AssetId"),
            (self._dependencies_for_grenade_bounce_sound, "grenade_bounce_sound", "int"),
            (self._dependencies_for_grenade_explosion_sound, "grenade_explosion_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PlantScarabSwarm.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_basic_swarm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> BasicSwarmProperties:
    return BasicSwarmProperties.from_stream(data, game, property_size)


def _decode_grenade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xE25FB08C: ("animation_information", _decode_animation_information),
    0xC6BB2F45: ("active", structs.decode_BIG_bool_),
    0xE1EC7346: ("basic_swarm_properties", _decode_basic_swarm_properties),
    0x7399ABBB: ("unknown_0x7399abbb", structs.decode_BIG_l),
    0x734D923B: ("unknown_0x734d923b", structs.decode_BIG_l),
    0xF11F7384: ("max_attack_angle", structs.decode_BIG_f),
    0xCA761DCD: ("into_attack_speed", structs.decode_BIG_f),
    0x6C0A2BC8: ("attack_speed", structs.decode_BIG_f),
    0x9A6BB47F: ("grenade_mass", structs.decode_BIG_f),
    0x16962C9B: ("grenade_launch_speed", structs.decode_BIG_f),
    0xED086CE0: ("unknown_0xed086ce0", structs.decode_BIG_f),
    0x454F16B1: ("unknown_0x454f16b1", structs.decode_BIG_l),
    0x14D1A3A8: ("grenade_damage", _decode_grenade_damage),
    0x6C7CA121: ("grenade_explosion_proximity", structs.decode_BIG_f),
    0xEA500E8B: ("grenade_explosion_effect", structs.decode_BIG_L),
    0x40992D51: ("part", structs.decode_BIG_L),
    0x1140D11D: ("grenade_trail_effect", structs.decode_BIG_L),
    0xD207FF0F: ("grenade_effect", structs.decode_BIG_L),
    0x2C1DFA22: ("grenade_bounce_sound", structs.decode_BIG_l),
    0x285EFBD9: ("grenade_bounce_sound_fall_off", structs.decode_BIG_f),
    0x15E0C159: ("unknown_0x15e0c159", structs.decode_BIG_f),
    0x30752C95: ("grenade_explosion_sound", structs.decode_BIG_l),
    0xBA66A16E: ("grenade_explosion_sound_fall_off", structs.decode_BIG_f),
    0xAB84892E: ("unknown_0xab84892e", structs.decode_BIG_f),
}
