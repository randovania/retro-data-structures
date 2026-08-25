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
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SporbNeedleJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        model: int
        initial_speed: float
        mass: float
        attack_damage: json_util.JsonObject
        fuse_time: float
        trail_effect: int
        explosion_effect: int
        launch_sound: int
        flight_sound: int
        hit_player_sound: int
        collision_sound: int
        explosion_sound: int


@dataclasses.dataclass()
class SporbNeedle(BaseObjectType):
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
    model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC27FFA8F, original_name="Model"),
        },
    )
    initial_speed: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCB14D97C, original_name="InitialSpeed"),
        },
    )
    mass: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75DBB375, original_name="Mass"),
        },
    )
    attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x66DCAACB,
                original_name="AttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    fuse_time: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5CC14B87, original_name="FuseTime"),
        },
    )
    trail_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x36EEE791, original_name="TrailEffect"),
        },
    )
    explosion_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF8B7BA26, original_name="ExplosionEffect"),
        },
    )
    launch_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0DD66F77, original_name="LaunchSound"),
        },
    )
    flight_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x1BC7F2FC, original_name="FlightSound"),
        },
    )
    hit_player_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xDFBD90E1, original_name="HitPlayerSound"),
        },
    )
    collision_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x92CAA97D, original_name="CollisionSound"),
        },
    )
    explosion_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x6028D1CC, original_name="ExplosionSound"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SPBN"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Sporb.rel"]

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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC27FFA8F
        model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB14D97C
        initial_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75DBB375
        mass = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66DCAACB
        attack_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 9, "di_damage": 5.0, "di_knock_back_power": 2.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5CC14B87
        fuse_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36EEE791
        trail_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8B7BA26
        explosion_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0DD66F77
        launch_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1BC7F2FC
        flight_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFBD90E1
        hit_player_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92CAA97D
        collision_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6028D1CC
        explosion_sound = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            actor_information,
            model,
            initial_speed,
            mass,
            attack_damage,
            fuse_time,
            trail_effect,
            explosion_effect,
            launch_sound,
            flight_sound,
            hit_player_sound,
            collision_sound,
            explosion_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0e")  # 14 properties

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

        data.write(b"\xc2\x7f\xfa\x8f")  # 0xc27ffa8f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.model))

        data.write(b"\xcb\x14\xd9|")  # 0xcb14d97c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_speed))

        data.write(b"u\xdb\xb3u")  # 0x75dbb375
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mass))

        data.write(b"f\xdc\xaa\xcb")  # 0x66dcaacb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack_damage.to_stream(
            data, game, default_override={"di_weapon_type": 9, "di_damage": 5.0, "di_knock_back_power": 2.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\\\xc1K\x87")  # 0x5cc14b87
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fuse_time))

        data.write(b"6\xee\xe7\x91")  # 0x36eee791
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.trail_effect))

        data.write(b"\xf8\xb7\xba&")  # 0xf8b7ba26
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.explosion_effect))

        data.write(b"\r\xd6ow")  # 0xdd66f77
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.launch_sound))

        data.write(b"\x1b\xc7\xf2\xfc")  # 0x1bc7f2fc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flight_sound))

        data.write(b"\xdf\xbd\x90\xe1")  # 0xdfbd90e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.hit_player_sound))

        data.write(b"\x92\xca\xa9}")  # 0x92caa97d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.collision_sound))

        data.write(b"`(\xd1\xcc")  # 0x6028d1cc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.explosion_sound))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SporbNeedleJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            model=json_data["model"],
            initial_speed=json_data["initial_speed"],
            mass=json_data["mass"],
            attack_damage=DamageInfo.from_json(json_data["attack_damage"]),
            fuse_time=json_data["fuse_time"],
            trail_effect=json_data["trail_effect"],
            explosion_effect=json_data["explosion_effect"],
            launch_sound=json_data["launch_sound"],
            flight_sound=json_data["flight_sound"],
            hit_player_sound=json_data["hit_player_sound"],
            collision_sound=json_data["collision_sound"],
            explosion_sound=json_data["explosion_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "model": self.model,
            "initial_speed": self.initial_speed,
            "mass": self.mass,
            "attack_damage": self.attack_damage.to_json(),
            "fuse_time": self.fuse_time,
            "trail_effect": self.trail_effect,
            "explosion_effect": self.explosion_effect,
            "launch_sound": self.launch_sound,
            "flight_sound": self.flight_sound,
            "hit_player_sound": self.hit_player_sound,
            "collision_sound": self.collision_sound,
            "explosion_sound": self.explosion_sound,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_trail_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.trail_effect)

    def _dependencies_for_explosion_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.explosion_effect)

    def _dependencies_for_launch_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.launch_sound)

    def _dependencies_for_flight_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.flight_sound)

    def _dependencies_for_hit_player_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.hit_player_sound)

    def _dependencies_for_collision_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.collision_sound)

    def _dependencies_for_explosion_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.explosion_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_model, "model", "AssetId"),
            (self._dependencies_for_trail_effect, "trail_effect", "AssetId"),
            (self._dependencies_for_explosion_effect, "explosion_effect", "AssetId"),
            (self._dependencies_for_launch_sound, "launch_sound", "int"),
            (self._dependencies_for_flight_sound, "flight_sound", "int"),
            (self._dependencies_for_hit_player_sound, "hit_player_sound", "int"),
            (self._dependencies_for_collision_sound, "collision_sound", "int"),
            (self._dependencies_for_explosion_sound, "explosion_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SporbNeedle.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_weapon_type": 9, "di_damage": 5.0, "di_knock_back_power": 2.0}
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xC27FFA8F: ("model", structs.decode_BIG_L),
    0xCB14D97C: ("initial_speed", structs.decode_BIG_f),
    0x75DBB375: ("mass", structs.decode_BIG_f),
    0x66DCAACB: ("attack_damage", _decode_attack_damage),
    0x5CC14B87: ("fuse_time", structs.decode_BIG_f),
    0x36EEE791: ("trail_effect", structs.decode_BIG_L),
    0xF8B7BA26: ("explosion_effect", structs.decode_BIG_L),
    0x0DD66F77: ("launch_sound", structs.decode_BIG_l),
    0x1BC7F2FC: ("flight_sound", structs.decode_BIG_l),
    0xDFBD90E1: ("hit_player_sound", structs.decode_BIG_l),
    0x92CAA97D: ("collision_sound", structs.decode_BIG_l),
    0x6028D1CC: ("explosion_sound", structs.decode_BIG_l),
}
