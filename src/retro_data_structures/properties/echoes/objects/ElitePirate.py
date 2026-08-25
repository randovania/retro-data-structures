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
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class ElitePirateJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        melee_damage: json_util.JsonObject
        max_melee_range: float
        min_shockwave_range: float
        max_shockwave_range: float
        min_rocket_range: float
        max_rocket_range: float
        unknown_0x5236c2b6: float
        unknown_0x01eaab17: float
        shielded_model: int
        shielded_skin_rules: int
        dark_shield: int
        dark_shield_sound: int
        dark_shield_pop: int
        light_shield: int
        light_shield_sound: int
        light_shield_pop: int
        taunt_interval: float
        taunt_variance: float
        single_shock_wave_info: json_util.JsonObject
        double_shock_wave_info: json_util.JsonObject
        unknown_0x28b39197: float
        unknown_0xe27de71b: float
        unknown_0x665e7ace: float
        unknown_0xacd4d06d: float
        rocket: int
        rocket_damage: json_util.JsonObject
        unknown_0x624222f8: int
        unknown_0x31e43a1c: int
        repeated_attack_chance: float
        energy_absorb_duration: float
        unknown_0xe47334ae: float
        unknown_0x3dad897b: float
        always_ff_0x06cf4324: int
        always_ff_0x23f5e1ee: int
        rocket_launcher_actor_info: json_util.JsonObject
        rocket_launcher_anim_info: json_util.JsonObject
        unknown_0x7e6e0d38: json_util.JsonObject
        visor_electric_effect: int
        sound_visor_electric: int
        ing_possession_data: json_util.JsonObject


@dataclasses.dataclass()
class ElitePirate(BaseObjectType):
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
    melee_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xC9416034,
                original_name="MeleeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    max_melee_range: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9873A1C1, original_name="MaxMeleeRange"),
        },
    )
    min_shockwave_range: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x28095CE6, original_name="MinShockwaveRange"),
        },
    )
    max_shockwave_range: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x691E6360, original_name="MaxShockwaveRange"),
        },
    )
    min_rocket_range: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE6299FAC, original_name="MinRocketRange"),
        },
    )
    max_rocket_range: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x411D1FD5, original_name="MaxRocketRange"),
        },
    )
    unknown_0x5236c2b6: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5236C2B6, original_name="Unknown"),
        },
    )
    unknown_0x01eaab17: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x01EAAB17, original_name="Unknown"),
        },
    )
    shielded_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00AE9C61, original_name="ShieldedModel"),
        },
    )
    shielded_skin_rules: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CSKR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xACDAE408, original_name="ShieldedSkinRules"),
        },
    )
    dark_shield: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAA482D8D, original_name="DarkShield"),
        },
    )
    dark_shield_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xEEAF03C4, original_name="DarkShieldSound"),
        },
    )
    dark_shield_pop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAF4FAE74, original_name="DarkShieldPop"),
        },
    )
    light_shield: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x64A1F558, original_name="LightShield"),
        },
    )
    light_shield_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xBF107374, original_name="LightShieldSound"),
        },
    )
    light_shield_pop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB43A4CAA, original_name="LightShieldPop"),
        },
    )
    taunt_interval: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x61C4C0EA, original_name="TauntInterval"),
        },
    )
    taunt_variance: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF82D1272, original_name="TauntVariance"),
        },
    )
    single_shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0xB2EBBFC6,
                original_name="SingleShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    double_shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x09250DB2,
                original_name="DoubleShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    unknown_0x28b39197: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x28B39197, original_name="Unknown"),
        },
    )
    unknown_0xe27de71b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE27DE71B, original_name="Unknown"),
        },
    )
    unknown_0x665e7ace: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x665E7ACE, original_name="Unknown"),
        },
    )
    unknown_0xacd4d06d: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xACD4D06D, original_name="Unknown"),
        },
    )
    rocket: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF199F553, original_name="Rocket"),
        },
    )
    rocket_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4063D45C,
                original_name="RocketDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x624222f8: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x624222F8, original_name="Unknown"),
        },
    )
    unknown_0x31e43a1c: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x31E43A1C, original_name="Unknown"),
        },
    )
    repeated_attack_chance: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD6469119, original_name="RepeatedAttackChance"),
        },
    )
    energy_absorb_duration: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D1425D8, original_name="EnergyAbsorbDuration"),
        },
    )
    unknown_0xe47334ae: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE47334AE, original_name="Unknown"),
        },
    )
    unknown_0x3dad897b: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3DAD897B, original_name="Unknown"),
        },
    )
    always_ff_0x06cf4324: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x06CF4324, original_name="Always FF"),
        },
    )
    always_ff_0x23f5e1ee: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x23F5E1EE, original_name="Always FF"),
        },
    )
    rocket_launcher_actor_info: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x62C744CD,
                original_name="RocketLauncherActorInfo",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    rocket_launcher_anim_info: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xB92B481D,
                original_name="RocketLauncherAnimInfo",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_0x7e6e0d38: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x7E6E0D38,
                original_name="Unknown",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    visor_electric_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBD321538, original_name="VisorElectricEffect"),
        },
    )
    sound_visor_electric: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x58A492EF, original_name="Sound_VisorElectric"),
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

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "EPRT"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ElitePirate.rel"]

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
        if property_count != 43:
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
            default_override={"average_attack_time": 3.5, "attack_time_variation": 2.0, "creature_size": 2},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9416034
        melee_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9873A1C1
        max_melee_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28095CE6
        min_shockwave_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x691E6360
        max_shockwave_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE6299FAC
        min_rocket_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x411D1FD5
        max_rocket_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5236C2B6
        unknown_0x5236c2b6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01EAAB17
        unknown_0x01eaab17 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00AE9C61
        shielded_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACDAE408
        shielded_skin_rules = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA482D8D
        dark_shield = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEEAF03C4
        dark_shield_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF4FAE74
        dark_shield_pop = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64A1F558
        light_shield = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF107374
        light_shield_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB43A4CAA
        light_shield_pop = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61C4C0EA
        taunt_interval = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF82D1272
        taunt_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2EBBFC6
        single_shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09250DB2
        double_shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28B39197
        unknown_0x28b39197 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE27DE71B
        unknown_0xe27de71b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x665E7ACE
        unknown_0x665e7ace = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACD4D06D
        unknown_0xacd4d06d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF199F553
        rocket = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4063D45C
        rocket_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x624222F8
        unknown_0x624222f8 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31E43A1C
        unknown_0x31e43a1c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6469119
        repeated_attack_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D1425D8
        energy_absorb_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE47334AE
        unknown_0xe47334ae = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DAD897B
        unknown_0x3dad897b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06CF4324
        always_ff_0x06cf4324 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23F5E1EE
        always_ff_0x23f5e1ee = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62C744CD
        rocket_launcher_actor_info = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB92B481D
        rocket_launcher_anim_info = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E6E0D38
        unknown_0x7e6e0d38 = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD321538
        visor_electric_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58A492EF
        sound_visor_electric = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE61748ED
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            patterned,
            actor_information,
            melee_damage,
            max_melee_range,
            min_shockwave_range,
            max_shockwave_range,
            min_rocket_range,
            max_rocket_range,
            unknown_0x5236c2b6,
            unknown_0x01eaab17,
            shielded_model,
            shielded_skin_rules,
            dark_shield,
            dark_shield_sound,
            dark_shield_pop,
            light_shield,
            light_shield_sound,
            light_shield_pop,
            taunt_interval,
            taunt_variance,
            single_shock_wave_info,
            double_shock_wave_info,
            unknown_0x28b39197,
            unknown_0xe27de71b,
            unknown_0x665e7ace,
            unknown_0xacd4d06d,
            rocket,
            rocket_damage,
            unknown_0x624222f8,
            unknown_0x31e43a1c,
            repeated_attack_chance,
            energy_absorb_duration,
            unknown_0xe47334ae,
            unknown_0x3dad897b,
            always_ff_0x06cf4324,
            always_ff_0x23f5e1ee,
            rocket_launcher_actor_info,
            rocket_launcher_anim_info,
            unknown_0x7e6e0d38,
            visor_electric_effect,
            sound_visor_electric,
            ing_possession_data,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00+")  # 43 properties

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
            data, game, default_override={"average_attack_time": 3.5, "attack_time_variation": 2.0, "creature_size": 2}
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

        data.write(b"\xc9A`4")  # 0xc9416034
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x98s\xa1\xc1")  # 0x9873a1c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_melee_range))

        data.write(b"(\t\\\xe6")  # 0x28095ce6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_shockwave_range))

        data.write(b"i\x1ec`")  # 0x691e6360
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_shockwave_range))

        data.write(b"\xe6)\x9f\xac")  # 0xe6299fac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_rocket_range))

        data.write(b"A\x1d\x1f\xd5")  # 0x411d1fd5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_rocket_range))

        data.write(b"R6\xc2\xb6")  # 0x5236c2b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5236c2b6))

        data.write(b"\x01\xea\xab\x17")  # 0x1eaab17
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x01eaab17))

        data.write(b"\x00\xae\x9ca")  # 0xae9c61
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shielded_model))

        data.write(b"\xac\xda\xe4\x08")  # 0xacdae408
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shielded_skin_rules))

        data.write(b"\xaaH-\x8d")  # 0xaa482d8d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_shield))

        data.write(b"\xee\xaf\x03\xc4")  # 0xeeaf03c4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.dark_shield_sound))

        data.write(b"\xafO\xaet")  # 0xaf4fae74
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_shield_pop))

        data.write(b"d\xa1\xf5X")  # 0x64a1f558
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.light_shield))

        data.write(b"\xbf\x10st")  # 0xbf107374
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.light_shield_sound))

        data.write(b"\xb4:L\xaa")  # 0xb43a4caa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.light_shield_pop))

        data.write(b"a\xc4\xc0\xea")  # 0x61c4c0ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.taunt_interval))

        data.write(b"\xf8-\x12r")  # 0xf82d1272
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.taunt_variance))

        data.write(b"\xb2\xeb\xbf\xc6")  # 0xb2ebbfc6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.single_shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\t%\r\xb2")  # 0x9250db2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.double_shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"(\xb3\x91\x97")  # 0x28b39197
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x28b39197))

        data.write(b"\xe2}\xe7\x1b")  # 0xe27de71b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe27de71b))

        data.write(b"f^z\xce")  # 0x665e7ace
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x665e7ace))

        data.write(b"\xac\xd4\xd0m")  # 0xacd4d06d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xacd4d06d))

        data.write(b"\xf1\x99\xf5S")  # 0xf199f553
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.rocket))

        data.write(b"@c\xd4\\")  # 0x4063d45c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.rocket_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 5.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'bB"\xf8')  # 0x624222f8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x624222f8))

        data.write(b"1\xe4:\x1c")  # 0x31e43a1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x31e43a1c))

        data.write(b"\xd6F\x91\x19")  # 0xd6469119
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.repeated_attack_chance))

        data.write(b"m\x14%\xd8")  # 0x6d1425d8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.energy_absorb_duration))

        data.write(b"\xe4s4\xae")  # 0xe47334ae
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe47334ae))

        data.write(b"=\xad\x89{")  # 0x3dad897b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3dad897b))

        data.write(b"\x06\xcfC$")  # 0x6cf4324
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.always_ff_0x06cf4324))

        data.write(b"#\xf5\xe1\xee")  # 0x23f5e1ee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.always_ff_0x23f5e1ee))

        data.write(b"b\xc7D\xcd")  # 0x62c744cd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.rocket_launcher_actor_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb9+H\x1d")  # 0xb92b481d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.rocket_launcher_anim_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~n\r8")  # 0x7e6e0d38
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x7e6e0d38.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbd2\x158")  # 0xbd321538
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.visor_electric_effect))

        data.write(b"X\xa4\x92\xef")  # 0x58a492ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_visor_electric))

        data.write(b"\xe6\x17H\xed")  # 0xe61748ed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possession_data.to_stream(data, game)
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
        json_data = typing.cast("ElitePirateJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            melee_damage=DamageInfo.from_json(json_data["melee_damage"]),
            max_melee_range=json_data["max_melee_range"],
            min_shockwave_range=json_data["min_shockwave_range"],
            max_shockwave_range=json_data["max_shockwave_range"],
            min_rocket_range=json_data["min_rocket_range"],
            max_rocket_range=json_data["max_rocket_range"],
            unknown_0x5236c2b6=json_data["unknown_0x5236c2b6"],
            unknown_0x01eaab17=json_data["unknown_0x01eaab17"],
            shielded_model=json_data["shielded_model"],
            shielded_skin_rules=json_data["shielded_skin_rules"],
            dark_shield=json_data["dark_shield"],
            dark_shield_sound=json_data["dark_shield_sound"],
            dark_shield_pop=json_data["dark_shield_pop"],
            light_shield=json_data["light_shield"],
            light_shield_sound=json_data["light_shield_sound"],
            light_shield_pop=json_data["light_shield_pop"],
            taunt_interval=json_data["taunt_interval"],
            taunt_variance=json_data["taunt_variance"],
            single_shock_wave_info=ShockWaveInfo.from_json(json_data["single_shock_wave_info"]),
            double_shock_wave_info=ShockWaveInfo.from_json(json_data["double_shock_wave_info"]),
            unknown_0x28b39197=json_data["unknown_0x28b39197"],
            unknown_0xe27de71b=json_data["unknown_0xe27de71b"],
            unknown_0x665e7ace=json_data["unknown_0x665e7ace"],
            unknown_0xacd4d06d=json_data["unknown_0xacd4d06d"],
            rocket=json_data["rocket"],
            rocket_damage=DamageInfo.from_json(json_data["rocket_damage"]),
            unknown_0x624222f8=json_data["unknown_0x624222f8"],
            unknown_0x31e43a1c=json_data["unknown_0x31e43a1c"],
            repeated_attack_chance=json_data["repeated_attack_chance"],
            energy_absorb_duration=json_data["energy_absorb_duration"],
            unknown_0xe47334ae=json_data["unknown_0xe47334ae"],
            unknown_0x3dad897b=json_data["unknown_0x3dad897b"],
            always_ff_0x06cf4324=json_data["always_ff_0x06cf4324"],
            always_ff_0x23f5e1ee=json_data["always_ff_0x23f5e1ee"],
            rocket_launcher_actor_info=ActorParameters.from_json(json_data["rocket_launcher_actor_info"]),
            rocket_launcher_anim_info=AnimationParameters.from_json(json_data["rocket_launcher_anim_info"]),
            unknown_0x7e6e0d38=AnimationParameters.from_json(json_data["unknown_0x7e6e0d38"]),
            visor_electric_effect=json_data["visor_electric_effect"],
            sound_visor_electric=json_data["sound_visor_electric"],
            ing_possession_data=IngPossessionData.from_json(json_data["ing_possession_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "melee_damage": self.melee_damage.to_json(),
            "max_melee_range": self.max_melee_range,
            "min_shockwave_range": self.min_shockwave_range,
            "max_shockwave_range": self.max_shockwave_range,
            "min_rocket_range": self.min_rocket_range,
            "max_rocket_range": self.max_rocket_range,
            "unknown_0x5236c2b6": self.unknown_0x5236c2b6,
            "unknown_0x01eaab17": self.unknown_0x01eaab17,
            "shielded_model": self.shielded_model,
            "shielded_skin_rules": self.shielded_skin_rules,
            "dark_shield": self.dark_shield,
            "dark_shield_sound": self.dark_shield_sound,
            "dark_shield_pop": self.dark_shield_pop,
            "light_shield": self.light_shield,
            "light_shield_sound": self.light_shield_sound,
            "light_shield_pop": self.light_shield_pop,
            "taunt_interval": self.taunt_interval,
            "taunt_variance": self.taunt_variance,
            "single_shock_wave_info": self.single_shock_wave_info.to_json(),
            "double_shock_wave_info": self.double_shock_wave_info.to_json(),
            "unknown_0x28b39197": self.unknown_0x28b39197,
            "unknown_0xe27de71b": self.unknown_0xe27de71b,
            "unknown_0x665e7ace": self.unknown_0x665e7ace,
            "unknown_0xacd4d06d": self.unknown_0xacd4d06d,
            "rocket": self.rocket,
            "rocket_damage": self.rocket_damage.to_json(),
            "unknown_0x624222f8": self.unknown_0x624222f8,
            "unknown_0x31e43a1c": self.unknown_0x31e43a1c,
            "repeated_attack_chance": self.repeated_attack_chance,
            "energy_absorb_duration": self.energy_absorb_duration,
            "unknown_0xe47334ae": self.unknown_0xe47334ae,
            "unknown_0x3dad897b": self.unknown_0x3dad897b,
            "always_ff_0x06cf4324": self.always_ff_0x06cf4324,
            "always_ff_0x23f5e1ee": self.always_ff_0x23f5e1ee,
            "rocket_launcher_actor_info": self.rocket_launcher_actor_info.to_json(),
            "rocket_launcher_anim_info": self.rocket_launcher_anim_info.to_json(),
            "unknown_0x7e6e0d38": self.unknown_0x7e6e0d38.to_json(),
            "visor_electric_effect": self.visor_electric_effect,
            "sound_visor_electric": self.sound_visor_electric,
            "ing_possession_data": self.ing_possession_data.to_json(),
        }

    def _dependencies_for_shielded_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shielded_model)

    def _dependencies_for_shielded_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shielded_skin_rules)

    def _dependencies_for_dark_shield(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_shield)

    def _dependencies_for_dark_shield_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.dark_shield_sound)

    def _dependencies_for_dark_shield_pop(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_shield_pop)

    def _dependencies_for_light_shield(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.light_shield)

    def _dependencies_for_light_shield_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.light_shield_sound)

    def _dependencies_for_light_shield_pop(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.light_shield_pop)

    def _dependencies_for_rocket(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rocket)

    def _dependencies_for_visor_electric_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_electric_effect)

    def _dependencies_for_sound_visor_electric(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_visor_electric)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_shielded_model, "shielded_model", "AssetId"),
            (self._dependencies_for_shielded_skin_rules, "shielded_skin_rules", "AssetId"),
            (self._dependencies_for_dark_shield, "dark_shield", "AssetId"),
            (self._dependencies_for_dark_shield_sound, "dark_shield_sound", "int"),
            (self._dependencies_for_dark_shield_pop, "dark_shield_pop", "AssetId"),
            (self._dependencies_for_light_shield, "light_shield", "AssetId"),
            (self._dependencies_for_light_shield_sound, "light_shield_sound", "int"),
            (self._dependencies_for_light_shield_pop, "light_shield_pop", "AssetId"),
            (self.single_shock_wave_info.dependencies_for, "single_shock_wave_info", "ShockWaveInfo"),
            (self.double_shock_wave_info.dependencies_for, "double_shock_wave_info", "ShockWaveInfo"),
            (self._dependencies_for_rocket, "rocket", "AssetId"),
            (self.rocket_launcher_actor_info.dependencies_for, "rocket_launcher_actor_info", "ActorParameters"),
            (self.rocket_launcher_anim_info.dependencies_for, "rocket_launcher_anim_info", "AnimationParameters"),
            (self.unknown_0x7e6e0d38.dependencies_for, "unknown_0x7e6e0d38", "AnimationParameters"),
            (self._dependencies_for_visor_electric_effect, "visor_electric_effect", "AssetId"),
            (self._dependencies_for_sound_visor_electric, "sound_visor_electric", "int"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for ElitePirate.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={"average_attack_time": 3.5, "attack_time_variation": 2.0, "creature_size": 2},
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_single_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_double_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_rocket_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_radius": 5.0}
    )


def _decode_rocket_launcher_actor_info(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_rocket_launcher_anim_info(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_unknown_0x7e6e0d38(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xC9416034: ("melee_damage", _decode_melee_damage),
    0x9873A1C1: ("max_melee_range", structs.decode_BIG_f),
    0x28095CE6: ("min_shockwave_range", structs.decode_BIG_f),
    0x691E6360: ("max_shockwave_range", structs.decode_BIG_f),
    0xE6299FAC: ("min_rocket_range", structs.decode_BIG_f),
    0x411D1FD5: ("max_rocket_range", structs.decode_BIG_f),
    0x5236C2B6: ("unknown_0x5236c2b6", structs.decode_BIG_f),
    0x01EAAB17: ("unknown_0x01eaab17", structs.decode_BIG_f),
    0x00AE9C61: ("shielded_model", structs.decode_BIG_L),
    0xACDAE408: ("shielded_skin_rules", structs.decode_BIG_L),
    0xAA482D8D: ("dark_shield", structs.decode_BIG_L),
    0xEEAF03C4: ("dark_shield_sound", structs.decode_BIG_l),
    0xAF4FAE74: ("dark_shield_pop", structs.decode_BIG_L),
    0x64A1F558: ("light_shield", structs.decode_BIG_L),
    0xBF107374: ("light_shield_sound", structs.decode_BIG_l),
    0xB43A4CAA: ("light_shield_pop", structs.decode_BIG_L),
    0x61C4C0EA: ("taunt_interval", structs.decode_BIG_f),
    0xF82D1272: ("taunt_variance", structs.decode_BIG_f),
    0xB2EBBFC6: ("single_shock_wave_info", _decode_single_shock_wave_info),
    0x09250DB2: ("double_shock_wave_info", _decode_double_shock_wave_info),
    0x28B39197: ("unknown_0x28b39197", structs.decode_BIG_f),
    0xE27DE71B: ("unknown_0xe27de71b", structs.decode_BIG_f),
    0x665E7ACE: ("unknown_0x665e7ace", structs.decode_BIG_f),
    0xACD4D06D: ("unknown_0xacd4d06d", structs.decode_BIG_f),
    0xF199F553: ("rocket", structs.decode_BIG_L),
    0x4063D45C: ("rocket_damage", _decode_rocket_damage),
    0x624222F8: ("unknown_0x624222f8", structs.decode_BIG_l),
    0x31E43A1C: ("unknown_0x31e43a1c", structs.decode_BIG_l),
    0xD6469119: ("repeated_attack_chance", structs.decode_BIG_f),
    0x6D1425D8: ("energy_absorb_duration", structs.decode_BIG_f),
    0xE47334AE: ("unknown_0xe47334ae", structs.decode_BIG_f),
    0x3DAD897B: ("unknown_0x3dad897b", structs.decode_BIG_f),
    0x06CF4324: ("always_ff_0x06cf4324", structs.decode_BIG_l),
    0x23F5E1EE: ("always_ff_0x23f5e1ee", structs.decode_BIG_l),
    0x62C744CD: ("rocket_launcher_actor_info", _decode_rocket_launcher_actor_info),
    0xB92B481D: ("rocket_launcher_anim_info", _decode_rocket_launcher_anim_info),
    0x7E6E0D38: ("unknown_0x7e6e0d38", _decode_unknown_0x7e6e0d38),
    0xBD321538: ("visor_electric_effect", structs.decode_BIG_L),
    0x58A492EF: ("sound_visor_electric", structs.decode_BIG_l),
    0xE61748ED: ("ing_possession_data", _decode_ing_possession_data),
}
