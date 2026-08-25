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
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SplinterJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        unknown_0x72edeb7d: float
        unknown_0xb8ed9ffa: float
        unknown_0x5e8d301b: float
        unknown_0xb98bb88f: float
        unknown_0x5feb176e: float
        unknown_0x726cd31d: int
        unknown_0x376e909f: int
        attack_damage: json_util.JsonObject
        unknown_0xb63b810c: int
        unknown_0x6d752efc: json_util.JsonObject
        unknown_0x0d6ab7b5: json_util.JsonObject
        part_0x630d93a1: int
        damage_info_0x4436a388: json_util.JsonObject
        ing_possession_data: json_util.JsonObject
        is_mega_splinter: bool
        wpsc: int
        damage_info_0x02fd0913: json_util.JsonObject
        part_0x496f191b: int
        unknown_0x51be00d3: float
        unknown_0xb7deaf32: float


@dataclasses.dataclass()
class Splinter(BaseObjectType):
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
    unknown_0x72edeb7d: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72EDEB7D, original_name="Unknown"),
        },
    )
    unknown_0xb8ed9ffa: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB8ED9FFA, original_name="Unknown"),
        },
    )
    unknown_0x5e8d301b: float = dataclasses.field(
        default=18.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E8D301B, original_name="Unknown"),
        },
    )
    unknown_0xb98bb88f: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB98BB88F, original_name="Unknown"),
        },
    )
    unknown_0x5feb176e: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5FEB176E, original_name="Unknown"),
        },
    )
    unknown_0x726cd31d: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x726CD31D, original_name="Unknown"),
        },
    )
    unknown_0x376e909f: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x376E909F, original_name="Unknown"),
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
    unknown_0xb63b810c: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB63B810C, original_name="Unknown"),
        },
    )
    unknown_0x6d752efc: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x6D752EFC,
                original_name="Unknown",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_0x0d6ab7b5: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x0D6AB7B5,
                original_name="Unknown",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    part_0x630d93a1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x630D93A1, original_name="PART"),
        },
    )
    damage_info_0x4436a388: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4436A388,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    ing_possession_data: IngPossessionData = dataclasses.field(
        default_factory=IngPossessionData,
        metadata={
            "reflection": FieldReflection[IngPossessionData](
                IngPossessionData,
                id=0xE61748ED,
                original_name="IngPossessionData",
                from_json=IngPossessionData.from_json,
                to_json=IngPossessionData.to_json,
            ),
        },
    )
    is_mega_splinter: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7DC82F46, original_name="IsMegaSplinter"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x42518359, original_name="WPSC"),
        },
    )
    damage_info_0x02fd0913: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x02FD0913,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    part_0x496f191b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x496F191B, original_name="PART"),
        },
    )
    unknown_0x51be00d3: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x51BE00D3, original_name="Unknown"),
        },
    )
    unknown_0xb7deaf32: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB7DEAF32, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SPTR"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Splinter.rel"]

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
        patterned = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "detection_range": 32.0,
                "min_attack_range": 7.0,
                "max_attack_range": 17.0,
                "collision_radius": 0.5,
                "collision_height": 1.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72EDEB7D
        unknown_0x72edeb7d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8ED9FFA
        unknown_0xb8ed9ffa = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E8D301B
        unknown_0x5e8d301b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB98BB88F
        unknown_0xb98bb88f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FEB176E
        unknown_0x5feb176e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x726CD31D
        unknown_0x726cd31d = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x376E909F
        unknown_0x376e909f = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66DCAACB
        attack_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB63B810C
        unknown_0xb63b810c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D752EFC
        unknown_0x6d752efc = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D6AB7B5
        unknown_0x0d6ab7b5 = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x630D93A1
        part_0x630d93a1 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4436A388
        damage_info_0x4436a388 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE61748ED
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DC82F46
        is_mega_splinter = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42518359
        wpsc = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02FD0913
        damage_info_0x02fd0913 = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x496F191B
        part_0x496f191b = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51BE00D3
        unknown_0x51be00d3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7DEAF32
        unknown_0xb7deaf32 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            unknown_0x72edeb7d,
            unknown_0xb8ed9ffa,
            unknown_0x5e8d301b,
            unknown_0xb98bb88f,
            unknown_0x5feb176e,
            unknown_0x726cd31d,
            unknown_0x376e909f,
            attack_damage,
            unknown_0xb63b810c,
            unknown_0x6d752efc,
            unknown_0x0d6ab7b5,
            part_0x630d93a1,
            damage_info_0x4436a388,
            ing_possession_data,
            is_mega_splinter,
            wpsc,
            damage_info_0x02fd0913,
            part_0x496f191b,
            unknown_0x51be00d3,
            unknown_0xb7deaf32,
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
        self.patterned.to_stream(
            data,
            game,
            default_override={
                "detection_range": 32.0,
                "min_attack_range": 7.0,
                "max_attack_range": 17.0,
                "collision_radius": 0.5,
                "collision_height": 1.0,
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

        data.write(b"r\xed\xeb}")  # 0x72edeb7d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x72edeb7d))

        data.write(b"\xb8\xed\x9f\xfa")  # 0xb8ed9ffa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb8ed9ffa))

        data.write(b"^\x8d0\x1b")  # 0x5e8d301b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5e8d301b))

        data.write(b"\xb9\x8b\xb8\x8f")  # 0xb98bb88f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb98bb88f))

        data.write(b"_\xeb\x17n")  # 0x5feb176e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5feb176e))

        data.write(b"rl\xd3\x1d")  # 0x726cd31d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x726cd31d))

        data.write(b"7n\x90\x9f")  # 0x376e909f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x376e909f))

        data.write(b"f\xdc\xaa\xcb")  # 0x66dcaacb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.attack_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb6;\x81\x0c")  # 0xb63b810c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb63b810c))

        data.write(b"mu.\xfc")  # 0x6d752efc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x6d752efc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\rj\xb7\xb5")  # 0xd6ab7b5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x0d6ab7b5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"c\r\x93\xa1")  # 0x630d93a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x630d93a1))

        data.write(b"D6\xa3\x88")  # 0x4436a388
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x4436a388.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe6\x17H\xed")  # 0xe61748ed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"}\xc8/F")  # 0x7dc82f46
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_mega_splinter))

        data.write(b"BQ\x83Y")  # 0x42518359
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.wpsc))

        data.write(b"\x02\xfd\t\x13")  # 0x2fd0913
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x02fd0913.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Io\x19\x1b")  # 0x496f191b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part_0x496f191b))

        data.write(b"Q\xbe\x00\xd3")  # 0x51be00d3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x51be00d3))

        data.write(b"\xb7\xde\xaf2")  # 0xb7deaf32
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb7deaf32))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SplinterJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            unknown_0x72edeb7d=json_data["unknown_0x72edeb7d"],
            unknown_0xb8ed9ffa=json_data["unknown_0xb8ed9ffa"],
            unknown_0x5e8d301b=json_data["unknown_0x5e8d301b"],
            unknown_0xb98bb88f=json_data["unknown_0xb98bb88f"],
            unknown_0x5feb176e=json_data["unknown_0x5feb176e"],
            unknown_0x726cd31d=json_data["unknown_0x726cd31d"],
            unknown_0x376e909f=json_data["unknown_0x376e909f"],
            attack_damage=DamageInfo.from_json(json_data["attack_damage"]),
            unknown_0xb63b810c=json_data["unknown_0xb63b810c"],
            unknown_0x6d752efc=AnimationParameters.from_json(json_data["unknown_0x6d752efc"]),
            unknown_0x0d6ab7b5=AnimationParameters.from_json(json_data["unknown_0x0d6ab7b5"]),
            part_0x630d93a1=json_data["part_0x630d93a1"],
            damage_info_0x4436a388=DamageInfo.from_json(json_data["damage_info_0x4436a388"]),
            ing_possession_data=IngPossessionData.from_json(json_data["ing_possession_data"]),
            is_mega_splinter=json_data["is_mega_splinter"],
            wpsc=json_data["wpsc"],
            damage_info_0x02fd0913=DamageInfo.from_json(json_data["damage_info_0x02fd0913"]),
            part_0x496f191b=json_data["part_0x496f191b"],
            unknown_0x51be00d3=json_data["unknown_0x51be00d3"],
            unknown_0xb7deaf32=json_data["unknown_0xb7deaf32"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "unknown_0x72edeb7d": self.unknown_0x72edeb7d,
            "unknown_0xb8ed9ffa": self.unknown_0xb8ed9ffa,
            "unknown_0x5e8d301b": self.unknown_0x5e8d301b,
            "unknown_0xb98bb88f": self.unknown_0xb98bb88f,
            "unknown_0x5feb176e": self.unknown_0x5feb176e,
            "unknown_0x726cd31d": self.unknown_0x726cd31d,
            "unknown_0x376e909f": self.unknown_0x376e909f,
            "attack_damage": self.attack_damage.to_json(),
            "unknown_0xb63b810c": self.unknown_0xb63b810c,
            "unknown_0x6d752efc": self.unknown_0x6d752efc.to_json(),
            "unknown_0x0d6ab7b5": self.unknown_0x0d6ab7b5.to_json(),
            "part_0x630d93a1": self.part_0x630d93a1,
            "damage_info_0x4436a388": self.damage_info_0x4436a388.to_json(),
            "ing_possession_data": self.ing_possession_data.to_json(),
            "is_mega_splinter": self.is_mega_splinter,
            "wpsc": self.wpsc,
            "damage_info_0x02fd0913": self.damage_info_0x02fd0913.to_json(),
            "part_0x496f191b": self.part_0x496f191b,
            "unknown_0x51be00d3": self.unknown_0x51be00d3,
            "unknown_0xb7deaf32": self.unknown_0xb7deaf32,
        }

    def _dependencies_for_part_0x630d93a1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x630d93a1)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_part_0x496f191b(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x496f191b)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.unknown_0x6d752efc.dependencies_for, "unknown_0x6d752efc", "AnimationParameters"),
            (self.unknown_0x0d6ab7b5.dependencies_for, "unknown_0x0d6ab7b5", "AnimationParameters"),
            (self._dependencies_for_part_0x630d93a1, "part_0x630d93a1", "AssetId"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_part_0x496f191b, "part_0x496f191b", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Splinter.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "detection_range": 32.0,
            "min_attack_range": 7.0,
            "max_attack_range": 17.0,
            "collision_radius": 0.5,
            "collision_height": 1.0,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0})


def _decode_unknown_0x6d752efc(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_unknown_0x0d6ab7b5(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_damage_info_0x4436a388(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_damage_info_0x02fd0913(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x72EDEB7D: ("unknown_0x72edeb7d", structs.decode_BIG_f),
    0xB8ED9FFA: ("unknown_0xb8ed9ffa", structs.decode_BIG_f),
    0x5E8D301B: ("unknown_0x5e8d301b", structs.decode_BIG_f),
    0xB98BB88F: ("unknown_0xb98bb88f", structs.decode_BIG_f),
    0x5FEB176E: ("unknown_0x5feb176e", structs.decode_BIG_f),
    0x726CD31D: ("unknown_0x726cd31d", structs.decode_BIG_l),
    0x376E909F: ("unknown_0x376e909f", structs.decode_BIG_l),
    0x66DCAACB: ("attack_damage", _decode_attack_damage),
    0xB63B810C: ("unknown_0xb63b810c", structs.decode_BIG_l),
    0x6D752EFC: ("unknown_0x6d752efc", _decode_unknown_0x6d752efc),
    0x0D6AB7B5: ("unknown_0x0d6ab7b5", _decode_unknown_0x0d6ab7b5),
    0x630D93A1: ("part_0x630d93a1", structs.decode_BIG_L),
    0x4436A388: ("damage_info_0x4436a388", _decode_damage_info_0x4436a388),
    0xE61748ED: ("ing_possession_data", _decode_ing_possession_data),
    0x7DC82F46: ("is_mega_splinter", structs.decode_BIG_bool_),
    0x42518359: ("wpsc", structs.decode_BIG_L),
    0x02FD0913: ("damage_info_0x02fd0913", _decode_damage_info_0x02fd0913),
    0x496F191B: ("part_0x496f191b", structs.decode_BIG_L),
    0x51BE00D3: ("unknown_0x51be00d3", structs.decode_BIG_f),
    0xB7DEAF32: ("unknown_0xb7deaf32", structs.decode_BIG_f),
}
