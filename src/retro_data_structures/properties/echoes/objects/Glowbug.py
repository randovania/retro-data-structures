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
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class GlowbugJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        death_flash_effect: int
        part: int
        attack_effect: int
        attack_telegraph_effect: int
        attack_echo_effect: int
        attack_duration: float
        attack_telegraph_duration: float
        attack_aim_offset: json_util.JsonValue
        attack_telegraph_sound: int
        attack_sound: int
        scan_model: int
        is_in_light_world: bool


@dataclasses.dataclass()
class Glowbug(BaseObjectType):
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
    death_flash_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD75426F9, original_name="DeathFlashEffect"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8985B339, original_name="PART"),
        },
    )
    attack_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART", "ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB258D3E8, original_name="AttackEffect"),
        },
    )
    attack_telegraph_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB06815B3, original_name="AttackTelegraphEffect"),
        },
    )
    attack_echo_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAB378A64, original_name="AttackEchoEffect"),
        },
    )
    attack_duration: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16342C18, original_name="AttackDuration"),
        },
    )
    attack_telegraph_duration: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3D7CCD32, original_name="AttackTelegraphDuration"),
        },
    )
    attack_aim_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x540C1F87,
                original_name="AttackAimOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    attack_telegraph_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0DB10F6B, original_name="AttackTelegraphSound"),
        },
    )
    attack_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x50E45EA8, original_name="AttackSound"),
        },
    )
    scan_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA9482EB1, original_name="ScanModel"),
        },
    )
    is_in_light_world: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1917A180, original_name="IsInLightWorld"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "GBUG"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Glowbug.rel"]

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
        if property_count != 15:
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
        assert property_id == 0xD75426F9
        death_flash_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8985B339
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB258D3E8
        attack_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB06815B3
        attack_telegraph_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB378A64
        attack_echo_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16342C18
        attack_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D7CCD32
        attack_telegraph_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x540C1F87
        attack_aim_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0DB10F6B
        attack_telegraph_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50E45EA8
        attack_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9482EB1
        scan_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1917A180
        is_in_light_world = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            death_flash_effect,
            part,
            attack_effect,
            attack_telegraph_effect,
            attack_echo_effect,
            attack_duration,
            attack_telegraph_duration,
            attack_aim_offset,
            attack_telegraph_sound,
            attack_sound,
            scan_model,
            is_in_light_world,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0f")  # 15 properties

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

        data.write(b"\xd7T&\xf9")  # 0xd75426f9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.death_flash_effect))

        data.write(b"\x89\x85\xb39")  # 0x8985b339
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b"\xb2X\xd3\xe8")  # 0xb258d3e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.attack_effect))

        data.write(b"\xb0h\x15\xb3")  # 0xb06815b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.attack_telegraph_effect))

        data.write(b"\xab7\x8ad")  # 0xab378a64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.attack_echo_effect))

        data.write(b"\x164,\x18")  # 0x16342c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_duration))

        data.write(b"=|\xcd2")  # 0x3d7ccd32
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_telegraph_duration))

        data.write(b"T\x0c\x1f\x87")  # 0x540c1f87
        data.write(b"\x00\x0c")  # size
        self.attack_aim_offset.to_stream(data, game)

        data.write(b"\r\xb1\x0fk")  # 0xdb10f6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.attack_telegraph_sound))

        data.write(b"P\xe4^\xa8")  # 0x50e45ea8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.attack_sound))

        data.write(b"\xa9H.\xb1")  # 0xa9482eb1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scan_model))

        data.write(b"\x19\x17\xa1\x80")  # 0x1917a180
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_in_light_world))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GlowbugJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            death_flash_effect=json_data["death_flash_effect"],
            part=json_data["part"],
            attack_effect=json_data["attack_effect"],
            attack_telegraph_effect=json_data["attack_telegraph_effect"],
            attack_echo_effect=json_data["attack_echo_effect"],
            attack_duration=json_data["attack_duration"],
            attack_telegraph_duration=json_data["attack_telegraph_duration"],
            attack_aim_offset=Vector.from_json(json_data["attack_aim_offset"]),
            attack_telegraph_sound=json_data["attack_telegraph_sound"],
            attack_sound=json_data["attack_sound"],
            scan_model=json_data["scan_model"],
            is_in_light_world=json_data["is_in_light_world"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "death_flash_effect": self.death_flash_effect,
            "part": self.part,
            "attack_effect": self.attack_effect,
            "attack_telegraph_effect": self.attack_telegraph_effect,
            "attack_echo_effect": self.attack_echo_effect,
            "attack_duration": self.attack_duration,
            "attack_telegraph_duration": self.attack_telegraph_duration,
            "attack_aim_offset": self.attack_aim_offset.to_json(),
            "attack_telegraph_sound": self.attack_telegraph_sound,
            "attack_sound": self.attack_sound,
            "scan_model": self.scan_model,
            "is_in_light_world": self.is_in_light_world,
        }

    def _dependencies_for_death_flash_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_flash_effect)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_attack_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.attack_effect)

    def _dependencies_for_attack_telegraph_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.attack_telegraph_effect)

    def _dependencies_for_attack_echo_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.attack_echo_effect)

    def _dependencies_for_attack_telegraph_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.attack_telegraph_sound)

    def _dependencies_for_attack_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.attack_sound)

    def _dependencies_for_scan_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_death_flash_effect, "death_flash_effect", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self._dependencies_for_attack_effect, "attack_effect", "AssetId"),
            (self._dependencies_for_attack_telegraph_effect, "attack_telegraph_effect", "AssetId"),
            (self._dependencies_for_attack_echo_effect, "attack_echo_effect", "AssetId"),
            (self._dependencies_for_attack_telegraph_sound, "attack_telegraph_sound", "int"),
            (self._dependencies_for_attack_sound, "attack_sound", "int"),
            (self._dependencies_for_scan_model, "scan_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Glowbug.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_attack_aim_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xD75426F9: ("death_flash_effect", structs.decode_BIG_L),
    0x8985B339: ("part", structs.decode_BIG_L),
    0xB258D3E8: ("attack_effect", structs.decode_BIG_L),
    0xB06815B3: ("attack_telegraph_effect", structs.decode_BIG_L),
    0xAB378A64: ("attack_echo_effect", structs.decode_BIG_L),
    0x16342C18: ("attack_duration", structs.decode_BIG_f),
    0x3D7CCD32: ("attack_telegraph_duration", structs.decode_BIG_f),
    0x540C1F87: ("attack_aim_offset", _decode_attack_aim_offset),
    0x0DB10F6B: ("attack_telegraph_sound", structs.decode_BIG_l),
    0x50E45EA8: ("attack_sound", structs.decode_BIG_l),
    0xA9482EB1: ("scan_model", structs.decode_BIG_L),
    0x1917A180: ("is_in_light_world", structs.decode_BIG_bool_),
}
