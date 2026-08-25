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
from retro_data_structures.properties.echoes.archetypes.BloggStruct import BloggStruct
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class BloggJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        min_attack_angle: float
        max_attack_angle: float
        unknown_0x32455774: float
        unknown_0xc1c8d862: float
        unknown_0xa19d5f62: int
        projectile_particle_effect: int
        projectile_damage: json_util.JsonObject
        body_damage_multiplier: float
        mouth_damage_multiplier: float
        mouth_damage_angle: float
        armor_vulnerability: json_util.JsonObject
        charge_damage_radius: float
        charge_damage: float
        bite_damage: float
        ball_spit_damage: float
        charge_turn_speed: float
        fish_attraction_radius: float
        fish_attraction_priority: float
        aggressiveness: float
        unknown_0x479ccc37: float
        unknown_0x689a803f: float
        unknown_0x800a2b0d: float
        charge_speed_multiplier: float
        max_melee_range: float
        unknown_0x6a78c607: float
        unknown_0x2c8d9fc4: float
        unknown_0xd1f82f92: float
        unknown_0x5109fb4e: float
        max_collision_time: float
        mouth_open_sound: int
        ing_possession_data: json_util.JsonObject
        ing_possessed_armor_vulnerability: json_util.JsonObject
        is_mega_blogg: bool
        projectile_blur_radius: float
        projectile_blur_time: float
        blogg_struct_0x3874576d: json_util.JsonObject
        blogg_struct_0x97dd1aa7: json_util.JsonObject
        blogg_struct_0xf2ba21e1: json_util.JsonObject


@dataclasses.dataclass()
class Blogg(BaseObjectType):
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
    min_attack_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x562BF3FD, original_name="MinAttackAngle"),
        },
    )
    max_attack_angle: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF11F7384, original_name="MaxAttackAngle"),
        },
    )
    unknown_0x32455774: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32455774, original_name="Unknown"),
        },
    )
    unknown_0xc1c8d862: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC1C8D862, original_name="Unknown"),
        },
    )
    unknown_0xa19d5f62: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA19D5F62, original_name="Unknown"),
        },
    )
    projectile_particle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x02D1176E, original_name="ProjectileParticleEffect"),
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
    body_damage_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7F8C4C69, original_name="BodyDamageMultiplier"),
        },
    )
    mouth_damage_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C36A6DD, original_name="MouthDamageMultiplier"),
        },
    )
    mouth_damage_angle: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x10FFE760, original_name="MouthDamageAngle"),
        },
    )
    armor_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x896D5BD9,
                original_name="ArmorVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    charge_damage_radius: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7D79B0A, original_name="ChargeDamageRadius"),
        },
    )
    charge_damage: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB15D8AF8, original_name="ChargeDamage"),
        },
    )
    bite_damage: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5210CD68, original_name="BiteDamage"),
        },
    )
    ball_spit_damage: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x479B1224, original_name="BallSpitDamage"),
        },
    )
    charge_turn_speed: float = dataclasses.field(
        default=900.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x290E5E0B, original_name="ChargeTurnSpeed"),
        },
    )
    fish_attraction_radius: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3FFCD8AE, original_name="FishAttractionRadius"),
        },
    )
    fish_attraction_priority: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B1B0461, original_name="FishAttractionPriority"),
        },
    )
    aggressiveness: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9579B1F2, original_name="Aggressiveness"),
        },
    )
    unknown_0x479ccc37: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0x479CCC37, original_name="Unknown"),
        },
    )
    unknown_0x689a803f: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x689A803F, original_name="Unknown"),
        },
    )
    unknown_0x800a2b0d: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x800A2B0D, original_name="Unknown"),
        },
    )
    charge_speed_multiplier: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x82DF77A1, original_name="ChargeSpeedMultiplier"),
        },
    )
    max_melee_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9873A1C1, original_name="MaxMeleeRange"),
        },
    )
    unknown_0x6a78c607: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6A78C607, original_name="Unknown"),
        },
    )
    unknown_0x2c8d9fc4: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C8D9FC4, original_name="Unknown"),
        },
    )
    unknown_0xd1f82f92: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD1F82F92, original_name="Unknown"),
        },
    )
    unknown_0x5109fb4e: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5109FB4E, original_name="Unknown"),
        },
    )
    max_collision_time: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x648A2486, original_name="MaxCollisionTime"),
        },
    )
    mouth_open_sound: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x041949B8, original_name="MouthOpenSound"),
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
    ing_possessed_armor_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x2AF6FF25,
                original_name="IngPossessedArmorVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    is_mega_blogg: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4FC9DFE4, original_name="IsMegaBlogg"),
        },
    )
    projectile_blur_radius: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DD3662E, original_name="ProjectileBlurRadius"),
        },
    )
    projectile_blur_time: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6F41BBE7, original_name="ProjectileBlurTime"),
        },
    )
    blogg_struct_0x3874576d: BloggStruct = dataclasses.field(
        default_factory=BloggStruct,
        metadata={
            "reflection": FieldReflection[BloggStruct](
                BloggStruct,
                id=0x3874576D,
                original_name="BloggStruct",
                from_json=BloggStruct.from_json,
                to_json=BloggStruct.to_json,
            ),
        },
    )
    blogg_struct_0x97dd1aa7: BloggStruct = dataclasses.field(
        default_factory=BloggStruct,
        metadata={
            "reflection": FieldReflection[BloggStruct](
                BloggStruct,
                id=0x97DD1AA7,
                original_name="BloggStruct",
                from_json=BloggStruct.from_json,
                to_json=BloggStruct.to_json,
            ),
        },
    )
    blogg_struct_0xf2ba21e1: BloggStruct = dataclasses.field(
        default_factory=BloggStruct,
        metadata={
            "reflection": FieldReflection[BloggStruct](
                BloggStruct,
                id=0xF2BA21E1,
                original_name="BloggStruct",
                from_json=BloggStruct.from_json,
                to_json=BloggStruct.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "BLOG"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Blogg.rel"]

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
        if property_count != 41:
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
        assert property_id == 0x562BF3FD
        min_attack_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF11F7384
        max_attack_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32455774
        unknown_0x32455774 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC1C8D862
        unknown_0xc1c8d862 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA19D5F62
        unknown_0xa19d5f62 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02D1176E
        projectile_particle_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553B1339
        projectile_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 5.0, "di_knock_back_power": 2.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F8C4C69
        body_damage_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C36A6DD
        mouth_damage_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10FFE760
        mouth_damage_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x896D5BD9
        armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7D79B0A
        charge_damage_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB15D8AF8
        charge_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5210CD68
        bite_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x479B1224
        ball_spit_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x290E5E0B
        charge_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FFCD8AE
        fish_attraction_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B1B0461
        fish_attraction_priority = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9579B1F2
        aggressiveness = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x479CCC37
        unknown_0x479ccc37 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x689A803F
        unknown_0x689a803f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x800A2B0D
        unknown_0x800a2b0d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82DF77A1
        charge_speed_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9873A1C1
        max_melee_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A78C607
        unknown_0x6a78c607 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C8D9FC4
        unknown_0x2c8d9fc4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1F82F92
        unknown_0xd1f82f92 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5109FB4E
        unknown_0x5109fb4e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x648A2486
        max_collision_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041949B8
        mouth_open_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE61748ED
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AF6FF25
        ing_possessed_armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4FC9DFE4
        is_mega_blogg = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DD3662E
        projectile_blur_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6F41BBE7
        projectile_blur_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3874576D
        blogg_struct_0x3874576d = BloggStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97DD1AA7
        blogg_struct_0x97dd1aa7 = BloggStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2BA21E1
        blogg_struct_0xf2ba21e1 = BloggStruct.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            patterned,
            actor_information,
            min_attack_angle,
            max_attack_angle,
            unknown_0x32455774,
            unknown_0xc1c8d862,
            unknown_0xa19d5f62,
            projectile_particle_effect,
            projectile_damage,
            body_damage_multiplier,
            mouth_damage_multiplier,
            mouth_damage_angle,
            armor_vulnerability,
            charge_damage_radius,
            charge_damage,
            bite_damage,
            ball_spit_damage,
            charge_turn_speed,
            fish_attraction_radius,
            fish_attraction_priority,
            aggressiveness,
            unknown_0x479ccc37,
            unknown_0x689a803f,
            unknown_0x800a2b0d,
            charge_speed_multiplier,
            max_melee_range,
            unknown_0x6a78c607,
            unknown_0x2c8d9fc4,
            unknown_0xd1f82f92,
            unknown_0x5109fb4e,
            max_collision_time,
            mouth_open_sound,
            ing_possession_data,
            ing_possessed_armor_vulnerability,
            is_mega_blogg,
            projectile_blur_radius,
            projectile_blur_time,
            blogg_struct_0x3874576d,
            blogg_struct_0x97dd1aa7,
            blogg_struct_0xf2ba21e1,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00)")  # 41 properties

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

        data.write(b"V+\xf3\xfd")  # 0x562bf3fd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_angle))

        data.write(b"\xf1\x1fs\x84")  # 0xf11f7384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_angle))

        data.write(b"2EWt")  # 0x32455774
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x32455774))

        data.write(b"\xc1\xc8\xd8b")  # 0xc1c8d862
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc1c8d862))

        data.write(b"\xa1\x9d_b")  # 0xa19d5f62
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa19d5f62))

        data.write(b"\x02\xd1\x17n")  # 0x2d1176e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.projectile_particle_effect))

        data.write(b"U;\x139")  # 0x553b1339
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0, "di_knock_back_power": 2.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x7f\x8cLi")  # 0x7f8c4c69
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.body_damage_multiplier))

        data.write(b"l6\xa6\xdd")  # 0x6c36a6dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mouth_damage_multiplier))

        data.write(b"\x10\xff\xe7`")  # 0x10ffe760
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.mouth_damage_angle))

        data.write(b"\x89m[\xd9")  # 0x896d5bd9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.armor_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7\xd7\x9b\n")  # 0xe7d79b0a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.charge_damage_radius))

        data.write(b"\xb1]\x8a\xf8")  # 0xb15d8af8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.charge_damage))

        data.write(b"R\x10\xcdh")  # 0x5210cd68
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bite_damage))

        data.write(b"G\x9b\x12$")  # 0x479b1224
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ball_spit_damage))

        data.write(b")\x0e^\x0b")  # 0x290e5e0b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.charge_turn_speed))

        data.write(b"?\xfc\xd8\xae")  # 0x3ffcd8ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fish_attraction_radius))

        data.write(b"\x8b\x1b\x04a")  # 0x8b1b0461
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fish_attraction_priority))

        data.write(b"\x95y\xb1\xf2")  # 0x9579b1f2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.aggressiveness))

        data.write(b"G\x9c\xcc7")  # 0x479ccc37
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x479ccc37))

        data.write(b"h\x9a\x80?")  # 0x689a803f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x689a803f))

        data.write(b"\x80\n+\r")  # 0x800a2b0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x800a2b0d))

        data.write(b"\x82\xdfw\xa1")  # 0x82df77a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.charge_speed_multiplier))

        data.write(b"\x98s\xa1\xc1")  # 0x9873a1c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_melee_range))

        data.write(b"jx\xc6\x07")  # 0x6a78c607
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6a78c607))

        data.write(b",\x8d\x9f\xc4")  # 0x2c8d9fc4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2c8d9fc4))

        data.write(b"\xd1\xf8/\x92")  # 0xd1f82f92
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd1f82f92))

        data.write(b"Q\t\xfbN")  # 0x5109fb4e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5109fb4e))

        data.write(b"d\x8a$\x86")  # 0x648a2486
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_collision_time))

        data.write(b"\x04\x19I\xb8")  # 0x41949b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.mouth_open_sound))

        data.write(b"\xe6\x17H\xed")  # 0xe61748ed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"*\xf6\xff%")  # 0x2af6ff25
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possessed_armor_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"O\xc9\xdf\xe4")  # 0x4fc9dfe4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_mega_blogg))

        data.write(b"-\xd3f.")  # 0x2dd3662e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_blur_radius))

        data.write(b"oA\xbb\xe7")  # 0x6f41bbe7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.projectile_blur_time))

        data.write(b"8tWm")  # 0x3874576d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blogg_struct_0x3874576d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x97\xdd\x1a\xa7")  # 0x97dd1aa7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blogg_struct_0x97dd1aa7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf2\xba!\xe1")  # 0xf2ba21e1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blogg_struct_0xf2ba21e1.to_stream(data, game)
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
        json_data = typing.cast("BloggJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            min_attack_angle=json_data["min_attack_angle"],
            max_attack_angle=json_data["max_attack_angle"],
            unknown_0x32455774=json_data["unknown_0x32455774"],
            unknown_0xc1c8d862=json_data["unknown_0xc1c8d862"],
            unknown_0xa19d5f62=json_data["unknown_0xa19d5f62"],
            projectile_particle_effect=json_data["projectile_particle_effect"],
            projectile_damage=DamageInfo.from_json(json_data["projectile_damage"]),
            body_damage_multiplier=json_data["body_damage_multiplier"],
            mouth_damage_multiplier=json_data["mouth_damage_multiplier"],
            mouth_damage_angle=json_data["mouth_damage_angle"],
            armor_vulnerability=DamageVulnerability.from_json(json_data["armor_vulnerability"]),
            charge_damage_radius=json_data["charge_damage_radius"],
            charge_damage=json_data["charge_damage"],
            bite_damage=json_data["bite_damage"],
            ball_spit_damage=json_data["ball_spit_damage"],
            charge_turn_speed=json_data["charge_turn_speed"],
            fish_attraction_radius=json_data["fish_attraction_radius"],
            fish_attraction_priority=json_data["fish_attraction_priority"],
            aggressiveness=json_data["aggressiveness"],
            unknown_0x479ccc37=json_data["unknown_0x479ccc37"],
            unknown_0x689a803f=json_data["unknown_0x689a803f"],
            unknown_0x800a2b0d=json_data["unknown_0x800a2b0d"],
            charge_speed_multiplier=json_data["charge_speed_multiplier"],
            max_melee_range=json_data["max_melee_range"],
            unknown_0x6a78c607=json_data["unknown_0x6a78c607"],
            unknown_0x2c8d9fc4=json_data["unknown_0x2c8d9fc4"],
            unknown_0xd1f82f92=json_data["unknown_0xd1f82f92"],
            unknown_0x5109fb4e=json_data["unknown_0x5109fb4e"],
            max_collision_time=json_data["max_collision_time"],
            mouth_open_sound=json_data["mouth_open_sound"],
            ing_possession_data=IngPossessionData.from_json(json_data["ing_possession_data"]),
            ing_possessed_armor_vulnerability=DamageVulnerability.from_json(
                json_data["ing_possessed_armor_vulnerability"]
            ),
            is_mega_blogg=json_data["is_mega_blogg"],
            projectile_blur_radius=json_data["projectile_blur_radius"],
            projectile_blur_time=json_data["projectile_blur_time"],
            blogg_struct_0x3874576d=BloggStruct.from_json(json_data["blogg_struct_0x3874576d"]),
            blogg_struct_0x97dd1aa7=BloggStruct.from_json(json_data["blogg_struct_0x97dd1aa7"]),
            blogg_struct_0xf2ba21e1=BloggStruct.from_json(json_data["blogg_struct_0xf2ba21e1"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "min_attack_angle": self.min_attack_angle,
            "max_attack_angle": self.max_attack_angle,
            "unknown_0x32455774": self.unknown_0x32455774,
            "unknown_0xc1c8d862": self.unknown_0xc1c8d862,
            "unknown_0xa19d5f62": self.unknown_0xa19d5f62,
            "projectile_particle_effect": self.projectile_particle_effect,
            "projectile_damage": self.projectile_damage.to_json(),
            "body_damage_multiplier": self.body_damage_multiplier,
            "mouth_damage_multiplier": self.mouth_damage_multiplier,
            "mouth_damage_angle": self.mouth_damage_angle,
            "armor_vulnerability": self.armor_vulnerability.to_json(),
            "charge_damage_radius": self.charge_damage_radius,
            "charge_damage": self.charge_damage,
            "bite_damage": self.bite_damage,
            "ball_spit_damage": self.ball_spit_damage,
            "charge_turn_speed": self.charge_turn_speed,
            "fish_attraction_radius": self.fish_attraction_radius,
            "fish_attraction_priority": self.fish_attraction_priority,
            "aggressiveness": self.aggressiveness,
            "unknown_0x479ccc37": self.unknown_0x479ccc37,
            "unknown_0x689a803f": self.unknown_0x689a803f,
            "unknown_0x800a2b0d": self.unknown_0x800a2b0d,
            "charge_speed_multiplier": self.charge_speed_multiplier,
            "max_melee_range": self.max_melee_range,
            "unknown_0x6a78c607": self.unknown_0x6a78c607,
            "unknown_0x2c8d9fc4": self.unknown_0x2c8d9fc4,
            "unknown_0xd1f82f92": self.unknown_0xd1f82f92,
            "unknown_0x5109fb4e": self.unknown_0x5109fb4e,
            "max_collision_time": self.max_collision_time,
            "mouth_open_sound": self.mouth_open_sound,
            "ing_possession_data": self.ing_possession_data.to_json(),
            "ing_possessed_armor_vulnerability": self.ing_possessed_armor_vulnerability.to_json(),
            "is_mega_blogg": self.is_mega_blogg,
            "projectile_blur_radius": self.projectile_blur_radius,
            "projectile_blur_time": self.projectile_blur_time,
            "blogg_struct_0x3874576d": self.blogg_struct_0x3874576d.to_json(),
            "blogg_struct_0x97dd1aa7": self.blogg_struct_0x97dd1aa7.to_json(),
            "blogg_struct_0xf2ba21e1": self.blogg_struct_0xf2ba21e1.to_json(),
        }

    def _dependencies_for_projectile_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_particle_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_projectile_particle_effect, "projectile_particle_effect", "AssetId"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Blogg.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={"creature_size": 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0, "di_knock_back_power": 2.0}
    )


def _decode_armor_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_ing_possessed_armor_vulnerability(
    data: typing.BinaryIO, game: Game, property_size: int
) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_blogg_struct_0x3874576d(data: typing.BinaryIO, game: Game, property_size: int) -> BloggStruct:
    return BloggStruct.from_stream(data, game, property_size)


def _decode_blogg_struct_0x97dd1aa7(data: typing.BinaryIO, game: Game, property_size: int) -> BloggStruct:
    return BloggStruct.from_stream(data, game, property_size)


def _decode_blogg_struct_0xf2ba21e1(data: typing.BinaryIO, game: Game, property_size: int) -> BloggStruct:
    return BloggStruct.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x562BF3FD: ("min_attack_angle", structs.decode_BIG_f),
    0xF11F7384: ("max_attack_angle", structs.decode_BIG_f),
    0x32455774: ("unknown_0x32455774", structs.decode_BIG_f),
    0xC1C8D862: ("unknown_0xc1c8d862", structs.decode_BIG_f),
    0xA19D5F62: ("unknown_0xa19d5f62", structs.decode_BIG_l),
    0x02D1176E: ("projectile_particle_effect", structs.decode_BIG_L),
    0x553B1339: ("projectile_damage", _decode_projectile_damage),
    0x7F8C4C69: ("body_damage_multiplier", structs.decode_BIG_f),
    0x6C36A6DD: ("mouth_damage_multiplier", structs.decode_BIG_f),
    0x10FFE760: ("mouth_damage_angle", structs.decode_BIG_f),
    0x896D5BD9: ("armor_vulnerability", _decode_armor_vulnerability),
    0xE7D79B0A: ("charge_damage_radius", structs.decode_BIG_f),
    0xB15D8AF8: ("charge_damage", structs.decode_BIG_f),
    0x5210CD68: ("bite_damage", structs.decode_BIG_f),
    0x479B1224: ("ball_spit_damage", structs.decode_BIG_f),
    0x290E5E0B: ("charge_turn_speed", structs.decode_BIG_f),
    0x3FFCD8AE: ("fish_attraction_radius", structs.decode_BIG_f),
    0x8B1B0461: ("fish_attraction_priority", structs.decode_BIG_f),
    0x9579B1F2: ("aggressiveness", structs.decode_BIG_f),
    0x479CCC37: ("unknown_0x479ccc37", structs.decode_BIG_f),
    0x689A803F: ("unknown_0x689a803f", structs.decode_BIG_f),
    0x800A2B0D: ("unknown_0x800a2b0d", structs.decode_BIG_f),
    0x82DF77A1: ("charge_speed_multiplier", structs.decode_BIG_f),
    0x9873A1C1: ("max_melee_range", structs.decode_BIG_f),
    0x6A78C607: ("unknown_0x6a78c607", structs.decode_BIG_f),
    0x2C8D9FC4: ("unknown_0x2c8d9fc4", structs.decode_BIG_f),
    0xD1F82F92: ("unknown_0xd1f82f92", structs.decode_BIG_f),
    0x5109FB4E: ("unknown_0x5109fb4e", structs.decode_BIG_f),
    0x648A2486: ("max_collision_time", structs.decode_BIG_f),
    0x041949B8: ("mouth_open_sound", structs.decode_BIG_l),
    0xE61748ED: ("ing_possession_data", _decode_ing_possession_data),
    0x2AF6FF25: ("ing_possessed_armor_vulnerability", _decode_ing_possessed_armor_vulnerability),
    0x4FC9DFE4: ("is_mega_blogg", structs.decode_BIG_bool_),
    0x2DD3662E: ("projectile_blur_radius", structs.decode_BIG_f),
    0x6F41BBE7: ("projectile_blur_time", structs.decode_BIG_f),
    0x3874576D: ("blogg_struct_0x3874576d", _decode_blogg_struct_0x3874576d),
    0x97DD1AA7: ("blogg_struct_0x97dd1aa7", _decode_blogg_struct_0x97dd1aa7),
    0xF2BA21E1: ("blogg_struct_0xf2ba21e1", _decode_blogg_struct_0xf2ba21e1),
}
