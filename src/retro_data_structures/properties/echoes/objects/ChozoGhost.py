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
from retro_data_structures.properties.echoes.archetypes.BehaveChance import BehaveChance
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

    class ChozoGhostJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        hearing_radius: float
        fade_out_delay: float
        attack_delay: float
        freeze_time: float
        unknown_0x54151870: int
        damage_info_0xffcda1f8: json_util.JsonObject
        unknown_0x3a58089c: int
        damage_info_0x1ff047a9: json_util.JsonObject
        behave_chance_0xe832241f: json_util.JsonObject
        behave_chance_0x1e2c8483: json_util.JsonObject
        behave_chance_0x78d76034: json_util.JsonObject
        sound_impact: int
        unknown_0xc87d7ec7: float
        right_disappear_crossfade: int
        sound: int
        unknown_0xec76940c: int
        unknown_0x723542bb: float
        unknown_0xfe9eac26: int
        hurl_recover_time: float
        projectile_visor_effect: int
        sound_projectile_visor: int
        unknown_0x61e511b3: float
        unknown_0x2369607a: float
        near_chance: int
        mid_chance: int


@dataclasses.dataclass()
class ChozoGhost(BaseObjectType):
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
    hearing_radius: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xED69488F, original_name="HearingRadius"),
        },
    )
    fade_out_delay: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB12F672, original_name="FadeOutDelay"),
        },
    )
    attack_delay: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1B67981A, original_name="AttackDelay"),
        },
    )
    freeze_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E8722C7, original_name="FreezeTime"),
        },
    )
    unknown_0x54151870: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x54151870, original_name="Unknown"),
        },
    )
    damage_info_0xffcda1f8: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xFFCDA1F8,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x3a58089c: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3A58089C, original_name="Unknown"),
        },
    )
    damage_info_0x1ff047a9: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x1FF047A9,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    behave_chance_0xe832241f: BehaveChance = dataclasses.field(
        default_factory=BehaveChance,
        metadata={
            "reflection": FieldReflection[BehaveChance](
                BehaveChance,
                id=0xE832241F,
                original_name="BehaveChance",
                from_json=BehaveChance.from_json,
                to_json=BehaveChance.to_json,
            ),
        },
    )
    behave_chance_0x1e2c8483: BehaveChance = dataclasses.field(
        default_factory=BehaveChance,
        metadata={
            "reflection": FieldReflection[BehaveChance](
                BehaveChance,
                id=0x1E2C8483,
                original_name="BehaveChance",
                from_json=BehaveChance.from_json,
                to_json=BehaveChance.to_json,
            ),
        },
    )
    behave_chance_0x78d76034: BehaveChance = dataclasses.field(
        default_factory=BehaveChance,
        metadata={
            "reflection": FieldReflection[BehaveChance](
                BehaveChance,
                id=0x78D76034,
                original_name="BehaveChance",
                from_json=BehaveChance.from_json,
                to_json=BehaveChance.to_json,
            ),
        },
    )
    sound_impact: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x1BB16EA5, original_name="Sound_Impact"),
        },
    )
    unknown_0xc87d7ec7: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC87D7EC7, original_name="Unknown"),
        },
    )
    right_disappear_crossfade: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x2ADCBB2E, original_name="RightDisappearCrossfade"),
        },
    )
    sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x58B8EC5D, original_name="Sound"),
        },
    )
    unknown_0xec76940c: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEC76940C, original_name="Unknown"),
        },
    )
    unknown_0x723542bb: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x723542BB, original_name="Unknown"),
        },
    )
    unknown_0xfe9eac26: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFE9EAC26, original_name="Unknown"),
        },
    )
    hurl_recover_time: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x96FEB75D, original_name="HurlRecoverTime"),
        },
    )
    projectile_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8F8C64A0, original_name="ProjectileVisorEffect"),
        },
    )
    sound_projectile_visor: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE15B4F4A, original_name="Sound_ProjectileVisor"),
        },
    )
    unknown_0x61e511b3: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61E511B3, original_name="Unknown"),
        },
    )
    unknown_0x2369607a: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2369607A, original_name="Unknown"),
        },
    )
    near_chance: int = dataclasses.field(
        default=40,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA6A3879B, original_name="NearChance"),
        },
    )
    mid_chance: int = dataclasses.field(
        default=40,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1B272781, original_name="MidChance"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CHOG"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ChozoGhost.rel"]

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
        if property_count != 28:
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
                "turn_speed": 720.0,
                "detection_range": 25.0,
                "min_attack_range": 8.0,
                "max_attack_range": 70.0,
                "leash_radius": 70.0,
                "collision_height": 4.5,
                "creature_size": 1,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED69488F
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB12F672
        fade_out_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B67981A
        attack_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E8722C7
        freeze_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54151870
        unknown_0x54151870 = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFFCDA1F8
        damage_info_0xffcda1f8 = DamageInfo.from_stream(data, game, property_size, default_override={"di_damage": 10.0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A58089C
        unknown_0x3a58089c = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1FF047A9
        damage_info_0x1ff047a9 = DamageInfo.from_stream(data, game, property_size, default_override={"di_damage": 5.0})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE832241F
        behave_chance_0xe832241f = BehaveChance.from_stream(
            data,
            game,
            property_size,
            default_override={"lurk": 20.0, "attack": 60.0, "move": 20.0, "lurk_time": 2.0, "num_bolts": 1},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E2C8483
        behave_chance_0x1e2c8483 = BehaveChance.from_stream(
            data,
            game,
            property_size,
            default_override={
                "lurk": 20.0,
                "attack": 60.0,
                "move": 10.0,
                "lurk_time": 2.0,
                "charge_attack": 20.0,
                "num_bolts": 3,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78D76034
        behave_chance_0x78d76034 = BehaveChance.from_stream(
            data,
            game,
            property_size,
            default_override={"attack": 100.0, "lurk_time": 2.0, "charge_attack": 50.0, "num_bolts": 2},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1BB16EA5
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC87D7EC7
        unknown_0xc87d7ec7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ADCBB2E
        right_disappear_crossfade = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58B8EC5D
        sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC76940C
        unknown_0xec76940c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723542BB
        unknown_0x723542bb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE9EAC26
        unknown_0xfe9eac26 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96FEB75D
        hurl_recover_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F8C64A0
        projectile_visor_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE15B4F4A
        sound_projectile_visor = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61E511B3
        unknown_0x61e511b3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2369607A
        unknown_0x2369607a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6A3879B
        near_chance = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B272781
        mid_chance = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            hearing_radius,
            fade_out_delay,
            attack_delay,
            freeze_time,
            unknown_0x54151870,
            damage_info_0xffcda1f8,
            unknown_0x3a58089c,
            damage_info_0x1ff047a9,
            behave_chance_0xe832241f,
            behave_chance_0x1e2c8483,
            behave_chance_0x78d76034,
            sound_impact,
            unknown_0xc87d7ec7,
            right_disappear_crossfade,
            sound,
            unknown_0xec76940c,
            unknown_0x723542bb,
            unknown_0xfe9eac26,
            hurl_recover_time,
            projectile_visor_effect,
            sound_projectile_visor,
            unknown_0x61e511b3,
            unknown_0x2369607a,
            near_chance,
            mid_chance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x1c")  # 28 properties

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
                "turn_speed": 720.0,
                "detection_range": 25.0,
                "min_attack_range": 8.0,
                "max_attack_range": 70.0,
                "leash_radius": 70.0,
                "collision_height": 4.5,
                "creature_size": 1,
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

        data.write(b"\xediH\x8f")  # 0xed69488f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b"\xfb\x12\xf6r")  # 0xfb12f672
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_out_delay))

        data.write(b"\x1bg\x98\x1a")  # 0x1b67981a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_delay))

        data.write(b'\x1e\x87"\xc7')  # 0x1e8722c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.freeze_time))

        data.write(b"T\x15\x18p")  # 0x54151870
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x54151870))

        data.write(b"\xff\xcd\xa1\xf8")  # 0xffcda1f8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0xffcda1f8.to_stream(data, game, default_override={"di_damage": 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b":X\x08\x9c")  # 0x3a58089c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x3a58089c))

        data.write(b"\x1f\xf0G\xa9")  # 0x1ff047a9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x1ff047a9.to_stream(data, game, default_override={"di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe82$\x1f")  # 0xe832241f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.behave_chance_0xe832241f.to_stream(
            data, game, default_override={"lurk": 20.0, "attack": 60.0, "move": 20.0, "lurk_time": 2.0, "num_bolts": 1}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1e,\x84\x83")  # 0x1e2c8483
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.behave_chance_0x1e2c8483.to_stream(
            data,
            game,
            default_override={
                "lurk": 20.0,
                "attack": 60.0,
                "move": 10.0,
                "lurk_time": 2.0,
                "charge_attack": 20.0,
                "num_bolts": 3,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"x\xd7`4")  # 0x78d76034
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.behave_chance_0x78d76034.to_stream(
            data, game, default_override={"attack": 100.0, "lurk_time": 2.0, "charge_attack": 50.0, "num_bolts": 2}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1b\xb1n\xa5")  # 0x1bb16ea5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_impact))

        data.write(b"\xc8}~\xc7")  # 0xc87d7ec7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc87d7ec7))

        data.write(b"*\xdc\xbb.")  # 0x2adcbb2e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.right_disappear_crossfade))

        data.write(b"X\xb8\xec]")  # 0x58b8ec5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound))

        data.write(b"\xecv\x94\x0c")  # 0xec76940c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xec76940c))

        data.write(b"r5B\xbb")  # 0x723542bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x723542bb))

        data.write(b"\xfe\x9e\xac&")  # 0xfe9eac26
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfe9eac26))

        data.write(b"\x96\xfe\xb7]")  # 0x96feb75d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hurl_recover_time))

        data.write(b"\x8f\x8cd\xa0")  # 0x8f8c64a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.projectile_visor_effect))

        data.write(b"\xe1[OJ")  # 0xe15b4f4a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_projectile_visor))

        data.write(b"a\xe5\x11\xb3")  # 0x61e511b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x61e511b3))

        data.write(b"#i`z")  # 0x2369607a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2369607a))

        data.write(b"\xa6\xa3\x87\x9b")  # 0xa6a3879b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.near_chance))

        data.write(b"\x1b''\x81")  # 0x1b272781
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.mid_chance))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ChozoGhostJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            hearing_radius=json_data["hearing_radius"],
            fade_out_delay=json_data["fade_out_delay"],
            attack_delay=json_data["attack_delay"],
            freeze_time=json_data["freeze_time"],
            unknown_0x54151870=json_data["unknown_0x54151870"],
            damage_info_0xffcda1f8=DamageInfo.from_json(json_data["damage_info_0xffcda1f8"]),
            unknown_0x3a58089c=json_data["unknown_0x3a58089c"],
            damage_info_0x1ff047a9=DamageInfo.from_json(json_data["damage_info_0x1ff047a9"]),
            behave_chance_0xe832241f=BehaveChance.from_json(json_data["behave_chance_0xe832241f"]),
            behave_chance_0x1e2c8483=BehaveChance.from_json(json_data["behave_chance_0x1e2c8483"]),
            behave_chance_0x78d76034=BehaveChance.from_json(json_data["behave_chance_0x78d76034"]),
            sound_impact=json_data["sound_impact"],
            unknown_0xc87d7ec7=json_data["unknown_0xc87d7ec7"],
            right_disappear_crossfade=json_data["right_disappear_crossfade"],
            sound=json_data["sound"],
            unknown_0xec76940c=json_data["unknown_0xec76940c"],
            unknown_0x723542bb=json_data["unknown_0x723542bb"],
            unknown_0xfe9eac26=json_data["unknown_0xfe9eac26"],
            hurl_recover_time=json_data["hurl_recover_time"],
            projectile_visor_effect=json_data["projectile_visor_effect"],
            sound_projectile_visor=json_data["sound_projectile_visor"],
            unknown_0x61e511b3=json_data["unknown_0x61e511b3"],
            unknown_0x2369607a=json_data["unknown_0x2369607a"],
            near_chance=json_data["near_chance"],
            mid_chance=json_data["mid_chance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "hearing_radius": self.hearing_radius,
            "fade_out_delay": self.fade_out_delay,
            "attack_delay": self.attack_delay,
            "freeze_time": self.freeze_time,
            "unknown_0x54151870": self.unknown_0x54151870,
            "damage_info_0xffcda1f8": self.damage_info_0xffcda1f8.to_json(),
            "unknown_0x3a58089c": self.unknown_0x3a58089c,
            "damage_info_0x1ff047a9": self.damage_info_0x1ff047a9.to_json(),
            "behave_chance_0xe832241f": self.behave_chance_0xe832241f.to_json(),
            "behave_chance_0x1e2c8483": self.behave_chance_0x1e2c8483.to_json(),
            "behave_chance_0x78d76034": self.behave_chance_0x78d76034.to_json(),
            "sound_impact": self.sound_impact,
            "unknown_0xc87d7ec7": self.unknown_0xc87d7ec7,
            "right_disappear_crossfade": self.right_disappear_crossfade,
            "sound": self.sound,
            "unknown_0xec76940c": self.unknown_0xec76940c,
            "unknown_0x723542bb": self.unknown_0x723542bb,
            "unknown_0xfe9eac26": self.unknown_0xfe9eac26,
            "hurl_recover_time": self.hurl_recover_time,
            "projectile_visor_effect": self.projectile_visor_effect,
            "sound_projectile_visor": self.sound_projectile_visor,
            "unknown_0x61e511b3": self.unknown_0x61e511b3,
            "unknown_0x2369607a": self.unknown_0x2369607a,
            "near_chance": self.near_chance,
            "mid_chance": self.mid_chance,
        }

    def _dependencies_for_unknown_0x54151870(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x54151870)

    def _dependencies_for_unknown_0x3a58089c(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x3a58089c)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_right_disappear_crossfade(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.right_disappear_crossfade)

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def _dependencies_for_projectile_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_visor_effect)

    def _dependencies_for_sound_projectile_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile_visor)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_unknown_0x54151870, "unknown_0x54151870", "AssetId"),
            (self._dependencies_for_unknown_0x3a58089c, "unknown_0x3a58089c", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_right_disappear_crossfade, "right_disappear_crossfade", "int"),
            (self._dependencies_for_sound, "sound", "int"),
            (self._dependencies_for_projectile_visor_effect, "projectile_visor_effect", "AssetId"),
            (self._dependencies_for_sound_projectile_visor, "sound_projectile_visor", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ChozoGhost.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "turn_speed": 720.0,
            "detection_range": 25.0,
            "min_attack_range": 8.0,
            "max_attack_range": 70.0,
            "leash_radius": 70.0,
            "collision_height": 4.5,
            "creature_size": 1,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_damage_info_0xffcda1f8(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_damage": 10.0})


def _decode_damage_info_0x1ff047a9(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_damage": 5.0})


def _decode_behave_chance_0xe832241f(data: typing.BinaryIO, game: Game, property_size: int) -> BehaveChance:
    return BehaveChance.from_stream(
        data,
        game,
        property_size,
        default_override={"lurk": 20.0, "attack": 60.0, "move": 20.0, "lurk_time": 2.0, "num_bolts": 1},
    )


def _decode_behave_chance_0x1e2c8483(data: typing.BinaryIO, game: Game, property_size: int) -> BehaveChance:
    return BehaveChance.from_stream(
        data,
        game,
        property_size,
        default_override={
            "lurk": 20.0,
            "attack": 60.0,
            "move": 10.0,
            "lurk_time": 2.0,
            "charge_attack": 20.0,
            "num_bolts": 3,
        },
    )


def _decode_behave_chance_0x78d76034(data: typing.BinaryIO, game: Game, property_size: int) -> BehaveChance:
    return BehaveChance.from_stream(
        data,
        game,
        property_size,
        default_override={"attack": 100.0, "lurk_time": 2.0, "charge_attack": 50.0, "num_bolts": 2},
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xED69488F: ("hearing_radius", structs.decode_BIG_f),
    0xFB12F672: ("fade_out_delay", structs.decode_BIG_f),
    0x1B67981A: ("attack_delay", structs.decode_BIG_f),
    0x1E8722C7: ("freeze_time", structs.decode_BIG_f),
    0x54151870: ("unknown_0x54151870", structs.decode_BIG_L),
    0xFFCDA1F8: ("damage_info_0xffcda1f8", _decode_damage_info_0xffcda1f8),
    0x3A58089C: ("unknown_0x3a58089c", structs.decode_BIG_L),
    0x1FF047A9: ("damage_info_0x1ff047a9", _decode_damage_info_0x1ff047a9),
    0xE832241F: ("behave_chance_0xe832241f", _decode_behave_chance_0xe832241f),
    0x1E2C8483: ("behave_chance_0x1e2c8483", _decode_behave_chance_0x1e2c8483),
    0x78D76034: ("behave_chance_0x78d76034", _decode_behave_chance_0x78d76034),
    0x1BB16EA5: ("sound_impact", structs.decode_BIG_l),
    0xC87D7EC7: ("unknown_0xc87d7ec7", structs.decode_BIG_f),
    0x2ADCBB2E: ("right_disappear_crossfade", structs.decode_BIG_l),
    0x58B8EC5D: ("sound", structs.decode_BIG_l),
    0xEC76940C: ("unknown_0xec76940c", structs.decode_BIG_l),
    0x723542BB: ("unknown_0x723542bb", structs.decode_BIG_f),
    0xFE9EAC26: ("unknown_0xfe9eac26", structs.decode_BIG_l),
    0x96FEB75D: ("hurl_recover_time", structs.decode_BIG_f),
    0x8F8C64A0: ("projectile_visor_effect", structs.decode_BIG_L),
    0xE15B4F4A: ("sound_projectile_visor", structs.decode_BIG_l),
    0x61E511B3: ("unknown_0x61e511b3", structs.decode_BIG_f),
    0x2369607A: ("unknown_0x2369607a", structs.decode_BIG_f),
    0xA6A3879B: ("near_chance", structs.decode_BIG_l),
    0x1B272781: ("mid_chance", structs.decode_BIG_l),
}
