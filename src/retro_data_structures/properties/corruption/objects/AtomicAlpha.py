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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class AtomicAlphaJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        patterned: json_util.JsonObject
        bomb_weapon: int
        bomb_model: int
        bomb_damage: json_util.JsonObject
        bomb_drop_delay: float
        bomb_reappear_delay: float
        bomb_reappear_time: float
        invisible: bool
        home_while_charging: bool


@dataclasses.dataclass()
class AtomicAlpha(BaseObjectType):
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
    bomb_weapon: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1720B91F, original_name="BombWeapon"),
        },
    )
    bomb_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC75F9516, original_name="BombModel"),
        },
    )
    bomb_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB48D5FE6,
                original_name="BombDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    bomb_drop_delay: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x66BA009C, original_name="BombDropDelay"),
        },
    )
    bomb_reappear_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x79DD66A9, original_name="BombReappearDelay"),
        },
    )
    bomb_reappear_time: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBB4284EA, original_name="BombReappearTime"),
        },
    )
    invisible: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7017EDFC, original_name="Invisible"),
        },
    )
    home_while_charging: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2639F0B9, original_name="HomeWhileCharging"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "ATMA"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_AtomicAlpha.rso"]

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
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1720B91F
        bomb_weapon = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC75F9516
        bomb_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB48D5FE6
        bomb_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66BA009C
        bomb_drop_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79DD66A9
        bomb_reappear_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB4284EA
        bomb_reappear_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7017EDFC
        invisible = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2639F0B9
        home_while_charging = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            actor_information,
            patterned,
            bomb_weapon,
            bomb_model,
            bomb_damage,
            bomb_drop_delay,
            bomb_reappear_delay,
            bomb_reappear_time,
            invisible,
            home_while_charging,
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

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
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

        data.write(b"\x17 \xb9\x1f")  # 0x1720b91f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.bomb_weapon))

        data.write(b"\xc7_\x95\x16")  # 0xc75f9516
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.bomb_model))

        data.write(b"\xb4\x8d_\xe6")  # 0xb48d5fe6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.bomb_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"f\xba\x00\x9c")  # 0x66ba009c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_drop_delay))

        data.write(b"y\xddf\xa9")  # 0x79dd66a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_reappear_delay))

        data.write(b"\xbbB\x84\xea")  # 0xbb4284ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bomb_reappear_time))

        data.write(b"p\x17\xed\xfc")  # 0x7017edfc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.invisible))

        data.write(b"&9\xf0\xb9")  # 0x2639f0b9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.home_while_charging))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AtomicAlphaJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            bomb_weapon=json_data["bomb_weapon"],
            bomb_model=json_data["bomb_model"],
            bomb_damage=DamageInfo.from_json(json_data["bomb_damage"]),
            bomb_drop_delay=json_data["bomb_drop_delay"],
            bomb_reappear_delay=json_data["bomb_reappear_delay"],
            bomb_reappear_time=json_data["bomb_reappear_time"],
            invisible=json_data["invisible"],
            home_while_charging=json_data["home_while_charging"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_information": self.actor_information.to_json(),
            "patterned": self.patterned.to_json(),
            "bomb_weapon": self.bomb_weapon,
            "bomb_model": self.bomb_model,
            "bomb_damage": self.bomb_damage.to_json(),
            "bomb_drop_delay": self.bomb_drop_delay,
            "bomb_reappear_delay": self.bomb_reappear_delay,
            "bomb_reappear_time": self.bomb_reappear_time,
            "invisible": self.invisible,
            "home_while_charging": self.home_while_charging,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_bomb_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xB3774750: ("patterned", _decode_patterned),
    0x1720B91F: ("bomb_weapon", structs.decode_BIG_Q),
    0xC75F9516: ("bomb_model", structs.decode_BIG_Q),
    0xB48D5FE6: ("bomb_damage", _decode_bomb_damage),
    0x66BA009C: ("bomb_drop_delay", structs.decode_BIG_f),
    0x79DD66A9: ("bomb_reappear_delay", structs.decode_BIG_f),
    0xBB4284EA: ("bomb_reappear_time", structs.decode_BIG_f),
    0x7017EDFC: ("invisible", structs.decode_BIG_bool_),
    0x2639F0B9: ("home_while_charging", structs.decode_BIG_bool_),
}
