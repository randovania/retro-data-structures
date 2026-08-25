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
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class WispTentacleJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        wake_up_distance: float
        search_distance: float
        attack_distance: float
        detection_height: float
        attack_damage: json_util.JsonObject
        spawn_from_portal: bool
        hurt_sleep_delay: float
        grab_blend_time: float
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject


@dataclasses.dataclass()
class WispTentacle(BaseObjectType):
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
    wake_up_distance: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD82814F2, original_name="WakeUpDistance"),
        },
    )
    search_distance: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA8AC80DD, original_name="SearchDistance"),
        },
    )
    attack_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5EDA8D99, original_name="AttackDistance"),
        },
    )
    detection_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9BB6CBC7, original_name="DetectionHeight"),
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
    spawn_from_portal: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xED7421FF, original_name="SpawnFromPortal"),
        },
    )
    hurt_sleep_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9B5A4744, original_name="HurtSleepDelay"),
        },
    )
    grab_blend_time: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D5A1F1D, original_name="GrabBlendTime"),
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

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "WISP"

    @classmethod
    def modules(cls) -> list[str]:
        return ["WispTentacle.rel"]

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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD82814F2
        wake_up_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8AC80DD
        search_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5EDA8D99
        attack_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9BB6CBC7
        detection_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66DCAACB
        attack_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 9, "di_damage": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED7421FF
        spawn_from_portal = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B5A4744
        hurt_sleep_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D5A1F1D
        grab_blend_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            wake_up_distance,
            search_distance,
            attack_distance,
            detection_height,
            attack_damage,
            spawn_from_portal,
            hurt_sleep_delay,
            grab_blend_time,
            patterned,
            actor_information,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd8(\x14\xf2")  # 0xd82814f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.wake_up_distance))

        data.write(b"\xa8\xac\x80\xdd")  # 0xa8ac80dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.search_distance))

        data.write(b"^\xda\x8d\x99")  # 0x5eda8d99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_distance))

        data.write(b"\x9b\xb6\xcb\xc7")  # 0x9bb6cbc7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.detection_height))

        data.write(b"f\xdc\xaa\xcb")  # 0x66dcaacb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack_damage.to_stream(data, game, default_override={"di_weapon_type": 9, "di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xedt!\xff")  # 0xed7421ff
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.spawn_from_portal))

        data.write(b"\x9bZGD")  # 0x9b5a4744
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hurt_sleep_delay))

        data.write(b"\rZ\x1f\x1d")  # 0xd5a1f1d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grab_blend_time))

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

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WispTentacleJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            wake_up_distance=json_data["wake_up_distance"],
            search_distance=json_data["search_distance"],
            attack_distance=json_data["attack_distance"],
            detection_height=json_data["detection_height"],
            attack_damage=DamageInfo.from_json(json_data["attack_damage"]),
            spawn_from_portal=json_data["spawn_from_portal"],
            hurt_sleep_delay=json_data["hurt_sleep_delay"],
            grab_blend_time=json_data["grab_blend_time"],
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "wake_up_distance": self.wake_up_distance,
            "search_distance": self.search_distance,
            "attack_distance": self.attack_distance,
            "detection_height": self.detection_height,
            "attack_damage": self.attack_damage.to_json(),
            "spawn_from_portal": self.spawn_from_portal,
            "hurt_sleep_delay": self.hurt_sleep_delay,
            "grab_blend_time": self.grab_blend_time,
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for WispTentacle.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 9, "di_damage": 5.0})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xD82814F2: ("wake_up_distance", structs.decode_BIG_f),
    0xA8AC80DD: ("search_distance", structs.decode_BIG_f),
    0x5EDA8D99: ("attack_distance", structs.decode_BIG_f),
    0x9BB6CBC7: ("detection_height", structs.decode_BIG_f),
    0x66DCAACB: ("attack_damage", _decode_attack_damage),
    0xED7421FF: ("spawn_from_portal", structs.decode_BIG_bool_),
    0x9B5A4744: ("hurt_sleep_delay", structs.decode_BIG_f),
    0x0D5A1F1D: ("grab_blend_time", structs.decode_BIG_f),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
}
