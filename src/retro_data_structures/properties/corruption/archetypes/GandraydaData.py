# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct30 import UnknownStruct30
from retro_data_structures.properties.corruption.archetypes.UnknownStruct31 import UnknownStruct31
from retro_data_structures.properties.corruption.archetypes.UnknownStruct32 import UnknownStruct32
from retro_data_structures.properties.corruption.archetypes.UnknownStruct33 import UnknownStruct33
from retro_data_structures.properties.corruption.archetypes.UnknownStruct34 import UnknownStruct34
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GandraydaDataJson(typing_extensions.TypedDict):
        unknown_0x538d71cb: float
        unknown_0xd42bba88: float
        unknown_0xf4b9c6c3: float
        unknown_0x4d4d934b: float
        min_navigation_time: float
        max_navigation_time: float
        unknown_0x32dd1ed4: float
        unknown_0x4ba741d5: float
        unknown_0x1eebf378: float
        melee_weapon: int
        melee_damage: json_util.JsonObject
        radial_melee_damage: json_util.JsonObject
        unknown_0x587fa387: float
        unknown_0x3e9ac5f3: float
        thrown_projectile: int
        thrown_projectile_damage: json_util.JsonObject
        thrown_projectile_visor_effect: int
        caud: int
        energy_wave_chance: float
        unknown_0x61f74274: int
        unknown_0x51a1ae4d: float
        unknown_0xb2fc1097: float
        unknown_0xd89e391a: float
        unknown_0x8f906959: float
        energy_wave_jump_apex: float
        unknown_0x8b354dc6: float
        energy_wave_projectile: int
        energy_wave_projectile_damage: json_util.JsonObject
        grapple_attack_chance: float
        unknown_0x24c6cdcf: float
        unknown_0x1a730547: float
        unknown_0x2684b001: float
        grapple_offset: json_util.JsonValue
        grapple_turn_speed: float
        unknown_0x776db913: float
        unknown_0x49d8719b: float
        grapple_mount_jump_apex: float
        grapple_dismount_jump_apex: float
        grapple_connected_visor_effect: int
        elsc_0x323f59c3: int
        elsc_0xe4f90605: int
        part: int
        grapple_pull_damage: json_util.JsonObject
        grapple_damage: json_util.JsonObject
        grapple_shake_sound: int
        unknown_0xc2b3754e: float
        unknown_0x21eecb94: float
        unknown_0xb5fdc280: float
        unknown_0x41d8c39c: float
        unknown_struct30: json_util.JsonObject
        unknown_struct31: json_util.JsonObject
        unknown_struct32: json_util.JsonObject
        unknown_struct33: json_util.JsonObject
        unknown_struct34: json_util.JsonObject


@dataclasses.dataclass()
class GandraydaData(BaseProperty):
    unknown_0x538d71cb: float = dataclasses.field(
        default=75.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x538D71CB, original_name="Unknown"),
        },
    )
    unknown_0xd42bba88: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD42BBA88, original_name="Unknown"),
        },
    )
    unknown_0xf4b9c6c3: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4B9C6C3, original_name="Unknown"),
        },
    )
    unknown_0x4d4d934b: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4D4D934B, original_name="Unknown"),
        },
    )
    min_navigation_time: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x20651830, original_name="MinNavigationTime"),
        },
    )
    max_navigation_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x617227B6, original_name="MaxNavigationTime"),
        },
    )
    unknown_0x32dd1ed4: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32DD1ED4, original_name="Unknown"),
        },
    )
    unknown_0x4ba741d5: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4BA741D5, original_name="Unknown"),
        },
    )
    unknown_0x1eebf378: float = dataclasses.field(
        default=13.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1EEBF378, original_name="Unknown"),
        },
    )
    melee_weapon: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4A426BB3, original_name="MeleeWeapon"),
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
    radial_melee_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x5F11893B,
                original_name="RadialMeleeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x587fa387: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x587FA387, original_name="Unknown"),
        },
    )
    unknown_0x3e9ac5f3: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E9AC5F3, original_name="Unknown"),
        },
    )
    thrown_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2697E437, original_name="ThrownProjectile"),
        },
    )
    thrown_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xAC187FA7,
                original_name="ThrownProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    thrown_projectile_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x76AF083E, original_name="ThrownProjectileVisorEffect"),
        },
    )
    caud: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x723A9398, original_name="CAUD"),
        },
    )
    energy_wave_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x79BC753E, original_name="EnergyWaveChance"),
        },
    )
    unknown_0x61f74274: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x61F74274, original_name="Unknown"),
        },
    )
    unknown_0x51a1ae4d: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x51A1AE4D, original_name="Unknown"),
        },
    )
    unknown_0xb2fc1097: float = dataclasses.field(
        default=18.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB2FC1097, original_name="Unknown"),
        },
    )
    unknown_0xd89e391a: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD89E391A, original_name="Unknown"),
        },
    )
    unknown_0x8f906959: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8F906959, original_name="Unknown"),
        },
    )
    energy_wave_jump_apex: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB281F490, original_name="EnergyWaveJumpApex"),
        },
    )
    unknown_0x8b354dc6: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B354DC6, original_name="Unknown"),
        },
    )
    energy_wave_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x76C64459, original_name="EnergyWaveProjectile"),
        },
    )
    energy_wave_projectile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x37ED6EBB,
                original_name="EnergyWaveProjectileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    grapple_attack_chance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD20CECF7, original_name="GrappleAttackChance"),
        },
    )
    unknown_0x24c6cdcf: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24C6CDCF, original_name="Unknown"),
        },
    )
    unknown_0x1a730547: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A730547, original_name="Unknown"),
        },
    )
    unknown_0x2684b001: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2684B001, original_name="Unknown"),
        },
    )
    grapple_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.4000000059604645, z=-1.600000023841858),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xB49D657D, original_name="GrappleOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    grapple_turn_speed: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4D1C792, original_name="GrappleTurnSpeed"),
        },
    )
    unknown_0x776db913: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x776DB913, original_name="Unknown"),
        },
    )
    unknown_0x49d8719b: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x49D8719B, original_name="Unknown"),
        },
    )
    grapple_mount_jump_apex: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC97CDBB, original_name="GrappleMountJumpApex"),
        },
    )
    grapple_dismount_jump_apex: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D5796EF, original_name="GrappleDismountJumpApex"),
        },
    )
    grapple_connected_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x98E19187, original_name="GrappleConnectedVisorEffect"),
        },
    )
    elsc_0x323f59c3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x323F59C3, original_name="ELSC"),
        },
    )
    elsc_0xe4f90605: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE4F90605, original_name="ELSC"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x96805AFD, original_name="PART"),
        },
    )
    grapple_pull_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x89E7495B,
                original_name="GrapplePullDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    grapple_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x2CE7520F,
                original_name="GrappleDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    grapple_shake_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x58066C47, original_name="GrappleShakeSound"),
        },
    )
    unknown_0xc2b3754e: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC2B3754E, original_name="Unknown"),
        },
    )
    unknown_0x21eecb94: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x21EECB94, original_name="Unknown"),
        },
    )
    unknown_0xb5fdc280: float = dataclasses.field(
        default=2.6666998863220215,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5FDC280, original_name="Unknown"),
        },
    )
    unknown_0x41d8c39c: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x41D8C39C, original_name="Unknown"),
        },
    )
    unknown_struct30: UnknownStruct30 = dataclasses.field(
        default_factory=UnknownStruct30,
        metadata={
            "reflection": FieldReflection[UnknownStruct30](
                UnknownStruct30,
                id=0xAF8984B2,
                original_name="UnknownStruct30",
                from_json=UnknownStruct30.from_json,
                to_json=UnknownStruct30.to_json,
            ),
        },
    )
    unknown_struct31: UnknownStruct31 = dataclasses.field(
        default_factory=UnknownStruct31,
        metadata={
            "reflection": FieldReflection[UnknownStruct31](
                UnknownStruct31,
                id=0xDCB5B112,
                original_name="UnknownStruct31",
                from_json=UnknownStruct31.from_json,
                to_json=UnknownStruct31.to_json,
            ),
        },
    )
    unknown_struct32: UnknownStruct32 = dataclasses.field(
        default_factory=UnknownStruct32,
        metadata={
            "reflection": FieldReflection[UnknownStruct32](
                UnknownStruct32,
                id=0xC30B62EA,
                original_name="UnknownStruct32",
                from_json=UnknownStruct32.from_json,
                to_json=UnknownStruct32.to_json,
            ),
        },
    )
    unknown_struct33: UnknownStruct33 = dataclasses.field(
        default_factory=UnknownStruct33,
        metadata={
            "reflection": FieldReflection[UnknownStruct33](
                UnknownStruct33,
                id=0x7F4E2E7D,
                original_name="UnknownStruct33",
                from_json=UnknownStruct33.from_json,
                to_json=UnknownStruct33.to_json,
            ),
        },
    )
    unknown_struct34: UnknownStruct34 = dataclasses.field(
        default_factory=UnknownStruct34,
        metadata={
            "reflection": FieldReflection[UnknownStruct34](
                UnknownStruct34,
                id=0xFC76C51A,
                original_name="UnknownStruct34",
                from_json=UnknownStruct34.from_json,
                to_json=UnknownStruct34.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 54:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x538D71CB
        unknown_0x538d71cb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD42BBA88
        unknown_0xd42bba88 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4B9C6C3
        unknown_0xf4b9c6c3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D4D934B
        unknown_0x4d4d934b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20651830
        min_navigation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x617227B6
        max_navigation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32DD1ED4
        unknown_0x32dd1ed4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4BA741D5
        unknown_0x4ba741d5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1EEBF378
        unknown_0x1eebf378 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A426BB3
        melee_weapon = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9416034
        melee_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F11893B
        radial_melee_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x587FA387
        unknown_0x587fa387 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E9AC5F3
        unknown_0x3e9ac5f3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2697E437
        thrown_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC187FA7
        thrown_projectile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76AF083E
        thrown_projectile_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723A9398
        caud = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79BC753E
        energy_wave_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61F74274
        unknown_0x61f74274 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51A1AE4D
        unknown_0x51a1ae4d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2FC1097
        unknown_0xb2fc1097 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD89E391A
        unknown_0xd89e391a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F906959
        unknown_0x8f906959 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB281F490
        energy_wave_jump_apex = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B354DC6
        unknown_0x8b354dc6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76C64459
        energy_wave_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37ED6EBB
        energy_wave_projectile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD20CECF7
        grapple_attack_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24C6CDCF
        unknown_0x24c6cdcf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A730547
        unknown_0x1a730547 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2684B001
        unknown_0x2684b001 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB49D657D
        grapple_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4D1C792
        grapple_turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x776DB913
        unknown_0x776db913 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49D8719B
        unknown_0x49d8719b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC97CDBB
        grapple_mount_jump_apex = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D5796EF
        grapple_dismount_jump_apex = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98E19187
        grapple_connected_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x323F59C3
        elsc_0x323f59c3 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE4F90605
        elsc_0xe4f90605 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96805AFD
        part = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89E7495B
        grapple_pull_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CE7520F
        grapple_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58066C47
        grapple_shake_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2B3754E
        unknown_0xc2b3754e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21EECB94
        unknown_0x21eecb94 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5FDC280
        unknown_0xb5fdc280 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41D8C39C
        unknown_0x41d8c39c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF8984B2
        unknown_struct30 = UnknownStruct30.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCB5B112
        unknown_struct31 = UnknownStruct31.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC30B62EA
        unknown_struct32 = UnknownStruct32.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F4E2E7D
        unknown_struct33 = UnknownStruct33.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC76C51A
        unknown_struct34 = UnknownStruct34.from_stream(data, game, property_size)

        return cls(
            unknown_0x538d71cb,
            unknown_0xd42bba88,
            unknown_0xf4b9c6c3,
            unknown_0x4d4d934b,
            min_navigation_time,
            max_navigation_time,
            unknown_0x32dd1ed4,
            unknown_0x4ba741d5,
            unknown_0x1eebf378,
            melee_weapon,
            melee_damage,
            radial_melee_damage,
            unknown_0x587fa387,
            unknown_0x3e9ac5f3,
            thrown_projectile,
            thrown_projectile_damage,
            thrown_projectile_visor_effect,
            caud,
            energy_wave_chance,
            unknown_0x61f74274,
            unknown_0x51a1ae4d,
            unknown_0xb2fc1097,
            unknown_0xd89e391a,
            unknown_0x8f906959,
            energy_wave_jump_apex,
            unknown_0x8b354dc6,
            energy_wave_projectile,
            energy_wave_projectile_damage,
            grapple_attack_chance,
            unknown_0x24c6cdcf,
            unknown_0x1a730547,
            unknown_0x2684b001,
            grapple_offset,
            grapple_turn_speed,
            unknown_0x776db913,
            unknown_0x49d8719b,
            grapple_mount_jump_apex,
            grapple_dismount_jump_apex,
            grapple_connected_visor_effect,
            elsc_0x323f59c3,
            elsc_0xe4f90605,
            part,
            grapple_pull_damage,
            grapple_damage,
            grapple_shake_sound,
            unknown_0xc2b3754e,
            unknown_0x21eecb94,
            unknown_0xb5fdc280,
            unknown_0x41d8c39c,
            unknown_struct30,
            unknown_struct31,
            unknown_struct32,
            unknown_struct33,
            unknown_struct34,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x006")  # 54 properties

        data.write(b"S\x8dq\xcb")  # 0x538d71cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x538d71cb))

        data.write(b"\xd4+\xba\x88")  # 0xd42bba88
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd42bba88))

        data.write(b"\xf4\xb9\xc6\xc3")  # 0xf4b9c6c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf4b9c6c3))

        data.write(b"MM\x93K")  # 0x4d4d934b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4d4d934b))

        data.write(b" e\x180")  # 0x20651830
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_navigation_time))

        data.write(b"ar'\xb6")  # 0x617227b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_navigation_time))

        data.write(b"2\xdd\x1e\xd4")  # 0x32dd1ed4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x32dd1ed4))

        data.write(b"K\xa7A\xd5")  # 0x4ba741d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4ba741d5))

        data.write(b"\x1e\xeb\xf3x")  # 0x1eebf378
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1eebf378))

        data.write(b"JBk\xb3")  # 0x4a426bb3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.melee_weapon))

        data.write(b"\xc9A`4")  # 0xc9416034
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_\x11\x89;")  # 0x5f11893b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.radial_melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\x7f\xa3\x87")  # 0x587fa387
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x587fa387))

        data.write(b">\x9a\xc5\xf3")  # 0x3e9ac5f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3e9ac5f3))

        data.write(b"&\x97\xe47")  # 0x2697e437
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.thrown_projectile))

        data.write(b"\xac\x18\x7f\xa7")  # 0xac187fa7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.thrown_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"v\xaf\x08>")  # 0x76af083e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.thrown_projectile_visor_effect))

        data.write(b"r:\x93\x98")  # 0x723a9398
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b"y\xbcu>")  # 0x79bc753e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.energy_wave_chance))

        data.write(b"a\xf7Bt")  # 0x61f74274
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x61f74274))

        data.write(b"Q\xa1\xaeM")  # 0x51a1ae4d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x51a1ae4d))

        data.write(b"\xb2\xfc\x10\x97")  # 0xb2fc1097
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb2fc1097))

        data.write(b"\xd8\x9e9\x1a")  # 0xd89e391a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd89e391a))

        data.write(b"\x8f\x90iY")  # 0x8f906959
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8f906959))

        data.write(b"\xb2\x81\xf4\x90")  # 0xb281f490
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.energy_wave_jump_apex))

        data.write(b"\x8b5M\xc6")  # 0x8b354dc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8b354dc6))

        data.write(b"v\xc6DY")  # 0x76c64459
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.energy_wave_projectile))

        data.write(b"7\xedn\xbb")  # 0x37ed6ebb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.energy_wave_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd2\x0c\xec\xf7")  # 0xd20cecf7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_attack_chance))

        data.write(b"$\xc6\xcd\xcf")  # 0x24c6cdcf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x24c6cdcf))

        data.write(b"\x1as\x05G")  # 0x1a730547
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1a730547))

        data.write(b"&\x84\xb0\x01")  # 0x2684b001
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2684b001))

        data.write(b"\xb4\x9de}")  # 0xb49d657d
        data.write(b"\x00\x0c")  # size
        self.grapple_offset.to_stream(data, game)

        data.write(b"\xf4\xd1\xc7\x92")  # 0xf4d1c792
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_turn_speed))

        data.write(b"wm\xb9\x13")  # 0x776db913
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x776db913))

        data.write(b"I\xd8q\x9b")  # 0x49d8719b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x49d8719b))

        data.write(b"\xec\x97\xcd\xbb")  # 0xec97cdbb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_mount_jump_apex))

        data.write(b"mW\x96\xef")  # 0x6d5796ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_dismount_jump_apex))

        data.write(b"\x98\xe1\x91\x87")  # 0x98e19187
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.grapple_connected_visor_effect))

        data.write(b"2?Y\xc3")  # 0x323f59c3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc_0x323f59c3))

        data.write(b"\xe4\xf9\x06\x05")  # 0xe4f90605
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc_0xe4f90605))

        data.write(b"\x96\x80Z\xfd")  # 0x96805afd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part))

        data.write(b"\x89\xe7I[")  # 0x89e7495b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_pull_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b",\xe7R\x0f")  # 0x2ce7520f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\x06lG")  # 0x58066c47
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.grapple_shake_sound))

        data.write(b"\xc2\xb3uN")  # 0xc2b3754e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc2b3754e))

        data.write(b"!\xee\xcb\x94")  # 0x21eecb94
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x21eecb94))

        data.write(b"\xb5\xfd\xc2\x80")  # 0xb5fdc280
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5fdc280))

        data.write(b"A\xd8\xc3\x9c")  # 0x41d8c39c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x41d8c39c))

        data.write(b"\xaf\x89\x84\xb2")  # 0xaf8984b2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct30.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdc\xb5\xb1\x12")  # 0xdcb5b112
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct31.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc3\x0bb\xea")  # 0xc30b62ea
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct32.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x7fN.}")  # 0x7f4e2e7d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct33.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfcv\xc5\x1a")  # 0xfc76c51a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct34.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GandraydaDataJson", data)
        return cls(
            unknown_0x538d71cb=json_data["unknown_0x538d71cb"],
            unknown_0xd42bba88=json_data["unknown_0xd42bba88"],
            unknown_0xf4b9c6c3=json_data["unknown_0xf4b9c6c3"],
            unknown_0x4d4d934b=json_data["unknown_0x4d4d934b"],
            min_navigation_time=json_data["min_navigation_time"],
            max_navigation_time=json_data["max_navigation_time"],
            unknown_0x32dd1ed4=json_data["unknown_0x32dd1ed4"],
            unknown_0x4ba741d5=json_data["unknown_0x4ba741d5"],
            unknown_0x1eebf378=json_data["unknown_0x1eebf378"],
            melee_weapon=json_data["melee_weapon"],
            melee_damage=DamageInfo.from_json(json_data["melee_damage"]),
            radial_melee_damage=DamageInfo.from_json(json_data["radial_melee_damage"]),
            unknown_0x587fa387=json_data["unknown_0x587fa387"],
            unknown_0x3e9ac5f3=json_data["unknown_0x3e9ac5f3"],
            thrown_projectile=json_data["thrown_projectile"],
            thrown_projectile_damage=DamageInfo.from_json(json_data["thrown_projectile_damage"]),
            thrown_projectile_visor_effect=json_data["thrown_projectile_visor_effect"],
            caud=json_data["caud"],
            energy_wave_chance=json_data["energy_wave_chance"],
            unknown_0x61f74274=json_data["unknown_0x61f74274"],
            unknown_0x51a1ae4d=json_data["unknown_0x51a1ae4d"],
            unknown_0xb2fc1097=json_data["unknown_0xb2fc1097"],
            unknown_0xd89e391a=json_data["unknown_0xd89e391a"],
            unknown_0x8f906959=json_data["unknown_0x8f906959"],
            energy_wave_jump_apex=json_data["energy_wave_jump_apex"],
            unknown_0x8b354dc6=json_data["unknown_0x8b354dc6"],
            energy_wave_projectile=json_data["energy_wave_projectile"],
            energy_wave_projectile_damage=DamageInfo.from_json(json_data["energy_wave_projectile_damage"]),
            grapple_attack_chance=json_data["grapple_attack_chance"],
            unknown_0x24c6cdcf=json_data["unknown_0x24c6cdcf"],
            unknown_0x1a730547=json_data["unknown_0x1a730547"],
            unknown_0x2684b001=json_data["unknown_0x2684b001"],
            grapple_offset=Vector.from_json(json_data["grapple_offset"]),
            grapple_turn_speed=json_data["grapple_turn_speed"],
            unknown_0x776db913=json_data["unknown_0x776db913"],
            unknown_0x49d8719b=json_data["unknown_0x49d8719b"],
            grapple_mount_jump_apex=json_data["grapple_mount_jump_apex"],
            grapple_dismount_jump_apex=json_data["grapple_dismount_jump_apex"],
            grapple_connected_visor_effect=json_data["grapple_connected_visor_effect"],
            elsc_0x323f59c3=json_data["elsc_0x323f59c3"],
            elsc_0xe4f90605=json_data["elsc_0xe4f90605"],
            part=json_data["part"],
            grapple_pull_damage=DamageInfo.from_json(json_data["grapple_pull_damage"]),
            grapple_damage=DamageInfo.from_json(json_data["grapple_damage"]),
            grapple_shake_sound=json_data["grapple_shake_sound"],
            unknown_0xc2b3754e=json_data["unknown_0xc2b3754e"],
            unknown_0x21eecb94=json_data["unknown_0x21eecb94"],
            unknown_0xb5fdc280=json_data["unknown_0xb5fdc280"],
            unknown_0x41d8c39c=json_data["unknown_0x41d8c39c"],
            unknown_struct30=UnknownStruct30.from_json(json_data["unknown_struct30"]),
            unknown_struct31=UnknownStruct31.from_json(json_data["unknown_struct31"]),
            unknown_struct32=UnknownStruct32.from_json(json_data["unknown_struct32"]),
            unknown_struct33=UnknownStruct33.from_json(json_data["unknown_struct33"]),
            unknown_struct34=UnknownStruct34.from_json(json_data["unknown_struct34"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x538d71cb": self.unknown_0x538d71cb,
            "unknown_0xd42bba88": self.unknown_0xd42bba88,
            "unknown_0xf4b9c6c3": self.unknown_0xf4b9c6c3,
            "unknown_0x4d4d934b": self.unknown_0x4d4d934b,
            "min_navigation_time": self.min_navigation_time,
            "max_navigation_time": self.max_navigation_time,
            "unknown_0x32dd1ed4": self.unknown_0x32dd1ed4,
            "unknown_0x4ba741d5": self.unknown_0x4ba741d5,
            "unknown_0x1eebf378": self.unknown_0x1eebf378,
            "melee_weapon": self.melee_weapon,
            "melee_damage": self.melee_damage.to_json(),
            "radial_melee_damage": self.radial_melee_damage.to_json(),
            "unknown_0x587fa387": self.unknown_0x587fa387,
            "unknown_0x3e9ac5f3": self.unknown_0x3e9ac5f3,
            "thrown_projectile": self.thrown_projectile,
            "thrown_projectile_damage": self.thrown_projectile_damage.to_json(),
            "thrown_projectile_visor_effect": self.thrown_projectile_visor_effect,
            "caud": self.caud,
            "energy_wave_chance": self.energy_wave_chance,
            "unknown_0x61f74274": self.unknown_0x61f74274,
            "unknown_0x51a1ae4d": self.unknown_0x51a1ae4d,
            "unknown_0xb2fc1097": self.unknown_0xb2fc1097,
            "unknown_0xd89e391a": self.unknown_0xd89e391a,
            "unknown_0x8f906959": self.unknown_0x8f906959,
            "energy_wave_jump_apex": self.energy_wave_jump_apex,
            "unknown_0x8b354dc6": self.unknown_0x8b354dc6,
            "energy_wave_projectile": self.energy_wave_projectile,
            "energy_wave_projectile_damage": self.energy_wave_projectile_damage.to_json(),
            "grapple_attack_chance": self.grapple_attack_chance,
            "unknown_0x24c6cdcf": self.unknown_0x24c6cdcf,
            "unknown_0x1a730547": self.unknown_0x1a730547,
            "unknown_0x2684b001": self.unknown_0x2684b001,
            "grapple_offset": self.grapple_offset.to_json(),
            "grapple_turn_speed": self.grapple_turn_speed,
            "unknown_0x776db913": self.unknown_0x776db913,
            "unknown_0x49d8719b": self.unknown_0x49d8719b,
            "grapple_mount_jump_apex": self.grapple_mount_jump_apex,
            "grapple_dismount_jump_apex": self.grapple_dismount_jump_apex,
            "grapple_connected_visor_effect": self.grapple_connected_visor_effect,
            "elsc_0x323f59c3": self.elsc_0x323f59c3,
            "elsc_0xe4f90605": self.elsc_0xe4f90605,
            "part": self.part,
            "grapple_pull_damage": self.grapple_pull_damage.to_json(),
            "grapple_damage": self.grapple_damage.to_json(),
            "grapple_shake_sound": self.grapple_shake_sound,
            "unknown_0xc2b3754e": self.unknown_0xc2b3754e,
            "unknown_0x21eecb94": self.unknown_0x21eecb94,
            "unknown_0xb5fdc280": self.unknown_0xb5fdc280,
            "unknown_0x41d8c39c": self.unknown_0x41d8c39c,
            "unknown_struct30": self.unknown_struct30.to_json(),
            "unknown_struct31": self.unknown_struct31.to_json(),
            "unknown_struct32": self.unknown_struct32.to_json(),
            "unknown_struct33": self.unknown_struct33.to_json(),
            "unknown_struct34": self.unknown_struct34.to_json(),
        }


def _decode_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_radial_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_thrown_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_energy_wave_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grapple_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_grapple_pull_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grapple_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_unknown_struct30(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct30:
    return UnknownStruct30.from_stream(data, game, property_size)


def _decode_unknown_struct31(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct31:
    return UnknownStruct31.from_stream(data, game, property_size)


def _decode_unknown_struct32(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct32:
    return UnknownStruct32.from_stream(data, game, property_size)


def _decode_unknown_struct33(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct33:
    return UnknownStruct33.from_stream(data, game, property_size)


def _decode_unknown_struct34(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct34:
    return UnknownStruct34.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x538D71CB: ("unknown_0x538d71cb", structs.decode_BIG_f),
    0xD42BBA88: ("unknown_0xd42bba88", structs.decode_BIG_f),
    0xF4B9C6C3: ("unknown_0xf4b9c6c3", structs.decode_BIG_f),
    0x4D4D934B: ("unknown_0x4d4d934b", structs.decode_BIG_f),
    0x20651830: ("min_navigation_time", structs.decode_BIG_f),
    0x617227B6: ("max_navigation_time", structs.decode_BIG_f),
    0x32DD1ED4: ("unknown_0x32dd1ed4", structs.decode_BIG_f),
    0x4BA741D5: ("unknown_0x4ba741d5", structs.decode_BIG_f),
    0x1EEBF378: ("unknown_0x1eebf378", structs.decode_BIG_f),
    0x4A426BB3: ("melee_weapon", structs.decode_BIG_Q),
    0xC9416034: ("melee_damage", _decode_melee_damage),
    0x5F11893B: ("radial_melee_damage", _decode_radial_melee_damage),
    0x587FA387: ("unknown_0x587fa387", structs.decode_BIG_f),
    0x3E9AC5F3: ("unknown_0x3e9ac5f3", structs.decode_BIG_f),
    0x2697E437: ("thrown_projectile", structs.decode_BIG_Q),
    0xAC187FA7: ("thrown_projectile_damage", _decode_thrown_projectile_damage),
    0x76AF083E: ("thrown_projectile_visor_effect", structs.decode_BIG_Q),
    0x723A9398: ("caud", structs.decode_BIG_Q),
    0x79BC753E: ("energy_wave_chance", structs.decode_BIG_f),
    0x61F74274: ("unknown_0x61f74274", structs.decode_BIG_l),
    0x51A1AE4D: ("unknown_0x51a1ae4d", structs.decode_BIG_f),
    0xB2FC1097: ("unknown_0xb2fc1097", structs.decode_BIG_f),
    0xD89E391A: ("unknown_0xd89e391a", structs.decode_BIG_f),
    0x8F906959: ("unknown_0x8f906959", structs.decode_BIG_f),
    0xB281F490: ("energy_wave_jump_apex", structs.decode_BIG_f),
    0x8B354DC6: ("unknown_0x8b354dc6", structs.decode_BIG_f),
    0x76C64459: ("energy_wave_projectile", structs.decode_BIG_Q),
    0x37ED6EBB: ("energy_wave_projectile_damage", _decode_energy_wave_projectile_damage),
    0xD20CECF7: ("grapple_attack_chance", structs.decode_BIG_f),
    0x24C6CDCF: ("unknown_0x24c6cdcf", structs.decode_BIG_f),
    0x1A730547: ("unknown_0x1a730547", structs.decode_BIG_f),
    0x2684B001: ("unknown_0x2684b001", structs.decode_BIG_f),
    0xB49D657D: ("grapple_offset", _decode_grapple_offset),
    0xF4D1C792: ("grapple_turn_speed", structs.decode_BIG_f),
    0x776DB913: ("unknown_0x776db913", structs.decode_BIG_f),
    0x49D8719B: ("unknown_0x49d8719b", structs.decode_BIG_f),
    0xEC97CDBB: ("grapple_mount_jump_apex", structs.decode_BIG_f),
    0x6D5796EF: ("grapple_dismount_jump_apex", structs.decode_BIG_f),
    0x98E19187: ("grapple_connected_visor_effect", structs.decode_BIG_Q),
    0x323F59C3: ("elsc_0x323f59c3", structs.decode_BIG_Q),
    0xE4F90605: ("elsc_0xe4f90605", structs.decode_BIG_Q),
    0x96805AFD: ("part", structs.decode_BIG_Q),
    0x89E7495B: ("grapple_pull_damage", _decode_grapple_pull_damage),
    0x2CE7520F: ("grapple_damage", _decode_grapple_damage),
    0x58066C47: ("grapple_shake_sound", structs.decode_BIG_Q),
    0xC2B3754E: ("unknown_0xc2b3754e", structs.decode_BIG_f),
    0x21EECB94: ("unknown_0x21eecb94", structs.decode_BIG_f),
    0xB5FDC280: ("unknown_0xb5fdc280", structs.decode_BIG_f),
    0x41D8C39C: ("unknown_0x41d8c39c", structs.decode_BIG_f),
    0xAF8984B2: ("unknown_struct30", _decode_unknown_struct30),
    0xDCB5B112: ("unknown_struct31", _decode_unknown_struct31),
    0xC30B62EA: ("unknown_struct32", _decode_unknown_struct32),
    0x7F4E2E7D: ("unknown_struct33", _decode_unknown_struct33),
    0xFC76C51A: ("unknown_struct34", _decode_unknown_struct34),
}
