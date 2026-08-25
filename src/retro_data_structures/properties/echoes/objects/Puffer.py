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
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class PufferJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        hover_speed: float
        cloud_effect: int
        cloud_damage: json_util.JsonObject
        cloud_steam: int
        cloud_steam_alpha: float
        orbit_interpolant_followed: bool
        cloud_in_dark: bool
        cloud_in_echo: bool
        explosion_damage: json_util.JsonObject
        sound_turn: int


@dataclasses.dataclass()
class Puffer(BaseObjectType):
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
    hover_speed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x845EF489, original_name="HoverSpeed"),
        },
    )
    cloud_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x670B9A1F, original_name="CloudEffect"),
        },
    )
    cloud_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xE8619082,
                original_name="CloudDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    cloud_steam: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1AA418F4, original_name="CloudSteam"),
        },
    )
    cloud_steam_alpha: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC9A55479, original_name="CloudSteamAlpha"),
        },
    )
    orbit_interpolant_followed: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x98647F20, original_name="OrbitInterpolantFollowed?"),
        },
    )
    cloud_in_dark: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8A30112F, original_name="CloudInDark"),
        },
    )
    cloud_in_echo: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x86C887A5, original_name="CloudInEcho"),
        },
    )
    explosion_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xDEFF74EA,
                original_name="ExplosionDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_turn: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x1F80154D, original_name="Sound_Turn"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "PUFR"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Puffer.rel"]

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
        if property_count != 13:
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
                "mass": 25.0,
                "turn_speed": 720.0,
                "detection_range": 5.0,
                "detection_height_range": 5.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "max_attack_range": 20.0,
                "damage_wait_time": 1.0,
                "collision_radius": 0.5,
                "collision_height": 1.5,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x845EF489
        hover_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x670B9A1F
        cloud_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8619082
        cloud_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AA418F4
        cloud_steam = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9A55479
        cloud_steam_alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98647F20
        orbit_interpolant_followed = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A30112F
        cloud_in_dark = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86C887A5
        cloud_in_echo = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDEFF74EA
        explosion_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F80154D
        sound_turn = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            hover_speed,
            cloud_effect,
            cloud_damage,
            cloud_steam,
            cloud_steam_alpha,
            orbit_interpolant_followed,
            cloud_in_dark,
            cloud_in_echo,
            explosion_damage,
            sound_turn,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\r")  # 13 properties

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
                "mass": 25.0,
                "turn_speed": 720.0,
                "detection_range": 5.0,
                "detection_height_range": 5.0,
                "detection_angle": 90.0,
                "min_attack_range": 4.0,
                "max_attack_range": 20.0,
                "damage_wait_time": 1.0,
                "collision_radius": 0.5,
                "collision_height": 1.5,
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

        data.write(b"\x84^\xf4\x89")  # 0x845ef489
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hover_speed))

        data.write(b"g\x0b\x9a\x1f")  # 0x670b9a1f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.cloud_effect))

        data.write(b"\xe8a\x90\x82")  # 0xe8619082
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.cloud_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1a\xa4\x18\xf4")  # 0x1aa418f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.cloud_steam))

        data.write(b"\xc9\xa5Ty")  # 0xc9a55479
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cloud_steam_alpha))

        data.write(b"\x98d\x7f ")  # 0x98647f20
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.orbit_interpolant_followed))

        data.write(b"\x8a0\x11/")  # 0x8a30112f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.cloud_in_dark))

        data.write(b"\x86\xc8\x87\xa5")  # 0x86c887a5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.cloud_in_echo))

        data.write(b"\xde\xfft\xea")  # 0xdeff74ea
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.explosion_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1f\x80\x15M")  # 0x1f80154d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_turn))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PufferJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            hover_speed=json_data["hover_speed"],
            cloud_effect=json_data["cloud_effect"],
            cloud_damage=DamageInfo.from_json(json_data["cloud_damage"]),
            cloud_steam=json_data["cloud_steam"],
            cloud_steam_alpha=json_data["cloud_steam_alpha"],
            orbit_interpolant_followed=json_data["orbit_interpolant_followed"],
            cloud_in_dark=json_data["cloud_in_dark"],
            cloud_in_echo=json_data["cloud_in_echo"],
            explosion_damage=DamageInfo.from_json(json_data["explosion_damage"]),
            sound_turn=json_data["sound_turn"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "hover_speed": self.hover_speed,
            "cloud_effect": self.cloud_effect,
            "cloud_damage": self.cloud_damage.to_json(),
            "cloud_steam": self.cloud_steam,
            "cloud_steam_alpha": self.cloud_steam_alpha,
            "orbit_interpolant_followed": self.orbit_interpolant_followed,
            "cloud_in_dark": self.cloud_in_dark,
            "cloud_in_echo": self.cloud_in_echo,
            "explosion_damage": self.explosion_damage.to_json(),
            "sound_turn": self.sound_turn,
        }

    def _dependencies_for_cloud_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cloud_effect)

    def _dependencies_for_cloud_steam(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cloud_steam)

    def _dependencies_for_sound_turn(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_turn)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_cloud_effect, "cloud_effect", "AssetId"),
            (self._dependencies_for_cloud_steam, "cloud_steam", "AssetId"),
            (self._dependencies_for_sound_turn, "sound_turn", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Puffer.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "mass": 25.0,
            "turn_speed": 720.0,
            "detection_range": 5.0,
            "detection_height_range": 5.0,
            "detection_angle": 90.0,
            "min_attack_range": 4.0,
            "max_attack_range": 20.0,
            "damage_wait_time": 1.0,
            "collision_radius": 0.5,
            "collision_height": 1.5,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_cloud_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_explosion_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x845EF489: ("hover_speed", structs.decode_BIG_f),
    0x670B9A1F: ("cloud_effect", structs.decode_BIG_L),
    0xE8619082: ("cloud_damage", _decode_cloud_damage),
    0x1AA418F4: ("cloud_steam", structs.decode_BIG_L),
    0xC9A55479: ("cloud_steam_alpha", structs.decode_BIG_f),
    0x98647F20: ("orbit_interpolant_followed", structs.decode_BIG_bool_),
    0x8A30112F: ("cloud_in_dark", structs.decode_BIG_bool_),
    0x86C887A5: ("cloud_in_echo", structs.decode_BIG_bool_),
    0xDEFF74EA: ("explosion_damage", _decode_explosion_damage),
    0x1F80154D: ("sound_turn", structs.decode_BIG_l),
}
