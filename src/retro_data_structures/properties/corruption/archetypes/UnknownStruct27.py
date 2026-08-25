# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct27Json(typing_extensions.TypedDict):
        unknown_0xb5049bbb: float
        unknown_0x3390e915: float
        unknown_0xf8cc3ab0: float
        unknown_0xe5c90a08: float
        unknown_0x2e95d9ad: float
        scan: int
        unknown_0x00d1aa67: int
        unknown_0xa57b4fac: int
        unknown_0x8836c426: int
        unknown_0xb87c5139: int
        unknown_0x9f566db4: int
        unknown_0xa2aac8e7: int
        unknown_0xf8aca397: int
        unknown_0x80a0b2cb: int
        unknown_0x69ed492e: int
        unknown_0x90419a55: int
        unknown_0x761db727: int
        unknown_0xdcb8af1c: int
        unknown_0x9cfddba8: int
        wpsc_0xf5056d9d: int
        wpsc_0x58dbcc52: int
        part_0x3a6d3a64: int
        pillar_base: int
        pillar_explosion_effect: int
        part_0xe8706e6e: int
        plasma_beam_info_0x6cc7412a: json_util.JsonObject
        homing_missile_projectile: int
        hover_then_home_projectile: json_util.JsonObject
        echo_animation_information: json_util.JsonObject
        echo_explosion: int
        echo_scan: int
        energy_wave_projectile: int
        plasma_beam_info_0xec493f59: json_util.JsonObject
        super_loop_projectile: int
        part_0x8e96e5e4: int
        txtr: int
        unknown_0x4f6e81a8: float
        unknown_0xe8f323f9: int
        caud: int
        unknown_0x8b8b33d9: int
        unknown_0x09133ecd: int
        is_dash_automatically: int
        sound_invulnerable_loop: int
        sound_shockwave: int


@dataclasses.dataclass()
class UnknownStruct27(BaseProperty):
    unknown_0xb5049bbb: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5049BBB, original_name="Unknown"),
        },
    )
    unknown_0x3390e915: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3390E915, original_name="Unknown"),
        },
    )
    unknown_0xf8cc3ab0: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8CC3AB0, original_name="Unknown"),
        },
    )
    unknown_0xe5c90a08: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE5C90A08, original_name="Unknown"),
        },
    )
    unknown_0x2e95d9ad: float = dataclasses.field(
        default=-1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2E95D9AD, original_name="Unknown"),
        },
    )
    scan: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x21E4D323, original_name="SCAN"),
        },
    )
    unknown_0x00d1aa67: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00D1AA67, original_name="Unknown"),
        },
    )
    unknown_0xa57b4fac: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA57B4FAC, original_name="Unknown"),
        },
    )
    unknown_0x8836c426: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8836C426, original_name="Unknown"),
        },
    )
    unknown_0xb87c5139: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB87C5139, original_name="Unknown"),
        },
    )
    unknown_0x9f566db4: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9F566DB4, original_name="Unknown"),
        },
    )
    unknown_0xa2aac8e7: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA2AAC8E7, original_name="Unknown"),
        },
    )
    unknown_0xf8aca397: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF8ACA397, original_name="Unknown"),
        },
    )
    unknown_0x80a0b2cb: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x80A0B2CB, original_name="Unknown"),
        },
    )
    unknown_0x69ed492e: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x69ED492E, original_name="Unknown"),
        },
    )
    unknown_0x90419a55: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x90419A55, original_name="Unknown"),
        },
    )
    unknown_0x761db727: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x761DB727, original_name="Unknown"),
        },
    )
    unknown_0xdcb8af1c: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDCB8AF1C, original_name="Unknown"),
        },
    )
    unknown_0x9cfddba8: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9CFDDBA8, original_name="Unknown"),
        },
    )
    wpsc_0xf5056d9d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF5056D9D, original_name="WPSC"),
        },
    )
    wpsc_0x58dbcc52: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x58DBCC52, original_name="WPSC"),
        },
    )
    part_0x3a6d3a64: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3A6D3A64, original_name="PART"),
        },
    )
    pillar_base: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF3D84488, original_name="PillarBase"),
        },
    )
    pillar_explosion_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x49BE8A11, original_name="PillarExplosionEffect"),
        },
    )
    part_0xe8706e6e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE8706E6E, original_name="PART"),
        },
    )
    plasma_beam_info_0x6cc7412a: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x6CC7412A,
                original_name="PlasmaBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    homing_missile_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xACFD8EA8, original_name="HomingMissileProjectile"),
        },
    )
    hover_then_home_projectile: HoverThenHomeProjectile = dataclasses.field(
        default_factory=HoverThenHomeProjectile,
        metadata={
            "reflection": FieldReflection[HoverThenHomeProjectile](
                HoverThenHomeProjectile,
                id=0xE8FC7798,
                original_name="HoverThenHomeProjectile",
                from_json=HoverThenHomeProjectile.from_json,
                to_json=HoverThenHomeProjectile.to_json,
            ),
        },
    )
    echo_animation_information: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x5377D4B5,
                original_name="EchoAnimationInformation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    echo_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4C8AEE6D, original_name="EchoExplosion"),
        },
    )
    echo_scan: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0B17536C, original_name="EchoScan"),
        },
    )
    energy_wave_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x76C64459, original_name="EnergyWaveProjectile"),
        },
    )
    plasma_beam_info_0xec493f59: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0xEC493F59,
                original_name="PlasmaBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    super_loop_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD1D51E35, original_name="SuperLoopProjectile"),
        },
    )
    part_0x8e96e5e4: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8E96E5E4, original_name="PART"),
        },
    )
    txtr: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5B67A4E7, original_name="TXTR"),
        },
    )
    unknown_0x4f6e81a8: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4F6E81A8, original_name="Unknown"),
        },
    )
    unknown_0xe8f323f9: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE8F323F9, original_name="Unknown"),
        },
    )
    caud: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9049A2FB, original_name="CAUD"),
        },
    )
    unknown_0x8b8b33d9: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8B8B33D9, original_name="Unknown"),
        },
    )
    unknown_0x09133ecd: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x09133ECD, original_name="Unknown"),
        },
    )
    is_dash_automatically: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3C67B14E, original_name="IsDashAutomatically"),
        },
    )
    sound_invulnerable_loop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAF6889B0, original_name="Sound_InvulnerableLoop"),
        },
    )
    sound_shockwave: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA47E51D3, original_name="Sound_Shockwave"),
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
        if property_count != 44:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5049BBB
        unknown_0xb5049bbb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3390E915
        unknown_0x3390e915 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8CC3AB0
        unknown_0xf8cc3ab0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE5C90A08
        unknown_0xe5c90a08 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E95D9AD
        unknown_0x2e95d9ad = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21E4D323
        scan = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00D1AA67
        unknown_0x00d1aa67 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA57B4FAC
        unknown_0xa57b4fac = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8836C426
        unknown_0x8836c426 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB87C5139
        unknown_0xb87c5139 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F566DB4
        unknown_0x9f566db4 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA2AAC8E7
        unknown_0xa2aac8e7 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8ACA397
        unknown_0xf8aca397 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80A0B2CB
        unknown_0x80a0b2cb = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69ED492E
        unknown_0x69ed492e = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90419A55
        unknown_0x90419a55 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x761DB727
        unknown_0x761db727 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCB8AF1C
        unknown_0xdcb8af1c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9CFDDBA8
        unknown_0x9cfddba8 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5056D9D
        wpsc_0xf5056d9d = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58DBCC52
        wpsc_0x58dbcc52 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A6D3A64
        part_0x3a6d3a64 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3D84488
        pillar_base = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49BE8A11
        pillar_explosion_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8706E6E
        part_0xe8706e6e = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6CC7412A
        plasma_beam_info_0x6cc7412a = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACFD8EA8
        homing_missile_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8FC7798
        hover_then_home_projectile = HoverThenHomeProjectile.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5377D4B5
        echo_animation_information = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C8AEE6D
        echo_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B17536C
        echo_scan = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76C64459
        energy_wave_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC493F59
        plasma_beam_info_0xec493f59 = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1D51E35
        super_loop_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E96E5E4
        part_0x8e96e5e4 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B67A4E7
        txtr = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F6E81A8
        unknown_0x4f6e81a8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8F323F9
        unknown_0xe8f323f9 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9049A2FB
        caud = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B8B33D9
        unknown_0x8b8b33d9 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09133ECD
        unknown_0x09133ecd = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C67B14E
        is_dash_automatically = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF6889B0
        sound_invulnerable_loop = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA47E51D3
        sound_shockwave = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            unknown_0xb5049bbb,
            unknown_0x3390e915,
            unknown_0xf8cc3ab0,
            unknown_0xe5c90a08,
            unknown_0x2e95d9ad,
            scan,
            unknown_0x00d1aa67,
            unknown_0xa57b4fac,
            unknown_0x8836c426,
            unknown_0xb87c5139,
            unknown_0x9f566db4,
            unknown_0xa2aac8e7,
            unknown_0xf8aca397,
            unknown_0x80a0b2cb,
            unknown_0x69ed492e,
            unknown_0x90419a55,
            unknown_0x761db727,
            unknown_0xdcb8af1c,
            unknown_0x9cfddba8,
            wpsc_0xf5056d9d,
            wpsc_0x58dbcc52,
            part_0x3a6d3a64,
            pillar_base,
            pillar_explosion_effect,
            part_0xe8706e6e,
            plasma_beam_info_0x6cc7412a,
            homing_missile_projectile,
            hover_then_home_projectile,
            echo_animation_information,
            echo_explosion,
            echo_scan,
            energy_wave_projectile,
            plasma_beam_info_0xec493f59,
            super_loop_projectile,
            part_0x8e96e5e4,
            txtr,
            unknown_0x4f6e81a8,
            unknown_0xe8f323f9,
            caud,
            unknown_0x8b8b33d9,
            unknown_0x09133ecd,
            is_dash_automatically,
            sound_invulnerable_loop,
            sound_shockwave,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00,")  # 44 properties

        data.write(b"\xb5\x04\x9b\xbb")  # 0xb5049bbb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5049bbb))

        data.write(b"3\x90\xe9\x15")  # 0x3390e915
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3390e915))

        data.write(b"\xf8\xcc:\xb0")  # 0xf8cc3ab0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf8cc3ab0))

        data.write(b"\xe5\xc9\n\x08")  # 0xe5c90a08
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe5c90a08))

        data.write(b".\x95\xd9\xad")  # 0x2e95d9ad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2e95d9ad))

        data.write(b"!\xe4\xd3#")  # 0x21e4d323
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan))

        data.write(b"\x00\xd1\xaag")  # 0xd1aa67
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x00d1aa67))

        data.write(b"\xa5{O\xac")  # 0xa57b4fac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa57b4fac))

        data.write(b"\x886\xc4&")  # 0x8836c426
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x8836c426))

        data.write(b"\xb8|Q9")  # 0xb87c5139
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb87c5139))

        data.write(b"\x9fVm\xb4")  # 0x9f566db4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9f566db4))

        data.write(b"\xa2\xaa\xc8\xe7")  # 0xa2aac8e7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa2aac8e7))

        data.write(b"\xf8\xac\xa3\x97")  # 0xf8aca397
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xf8aca397))

        data.write(b"\x80\xa0\xb2\xcb")  # 0x80a0b2cb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x80a0b2cb))

        data.write(b"i\xedI.")  # 0x69ed492e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x69ed492e))

        data.write(b"\x90A\x9aU")  # 0x90419a55
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x90419a55))

        data.write(b"v\x1d\xb7'")  # 0x761db727
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x761db727))

        data.write(b"\xdc\xb8\xaf\x1c")  # 0xdcb8af1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xdcb8af1c))

        data.write(b"\x9c\xfd\xdb\xa8")  # 0x9cfddba8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9cfddba8))

        data.write(b"\xf5\x05m\x9d")  # 0xf5056d9d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc_0xf5056d9d))

        data.write(b"X\xdb\xccR")  # 0x58dbcc52
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc_0x58dbcc52))

        data.write(b":m:d")  # 0x3a6d3a64
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x3a6d3a64))

        data.write(b"\xf3\xd8D\x88")  # 0xf3d84488
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.pillar_base))

        data.write(b"I\xbe\x8a\x11")  # 0x49be8a11
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.pillar_explosion_effect))

        data.write(b"\xe8pnn")  # 0xe8706e6e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xe8706e6e))

        data.write(b"l\xc7A*")  # 0x6cc7412a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.plasma_beam_info_0x6cc7412a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xac\xfd\x8e\xa8")  # 0xacfd8ea8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.homing_missile_projectile))

        data.write(b"\xe8\xfcw\x98")  # 0xe8fc7798
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hover_then_home_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Sw\xd4\xb5")  # 0x5377d4b5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.echo_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"L\x8a\xeem")  # 0x4c8aee6d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.echo_explosion))

        data.write(b"\x0b\x17Sl")  # 0xb17536c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.echo_scan))

        data.write(b"v\xc6DY")  # 0x76c64459
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.energy_wave_projectile))

        data.write(b"\xecI?Y")  # 0xec493f59
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.plasma_beam_info_0xec493f59.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd1\xd5\x1e5")  # 0xd1d51e35
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.super_loop_projectile))

        data.write(b"\x8e\x96\xe5\xe4")  # 0x8e96e5e4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x8e96e5e4))

        data.write(b"[g\xa4\xe7")  # 0x5b67a4e7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.txtr))

        data.write(b"On\x81\xa8")  # 0x4f6e81a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f6e81a8))

        data.write(b"\xe8\xf3#\xf9")  # 0xe8f323f9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xe8f323f9))

        data.write(b"\x90I\xa2\xfb")  # 0x9049a2fb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b"\x8b\x8b3\xd9")  # 0x8b8b33d9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x8b8b33d9))

        data.write(b"\t\x13>\xcd")  # 0x9133ecd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x09133ecd))

        data.write(b"<g\xb1N")  # 0x3c67b14e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.is_dash_automatically))

        data.write(b"\xafh\x89\xb0")  # 0xaf6889b0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_invulnerable_loop))

        data.write(b"\xa4~Q\xd3")  # 0xa47e51d3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_shockwave))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct27Json", data)
        return cls(
            unknown_0xb5049bbb=json_data["unknown_0xb5049bbb"],
            unknown_0x3390e915=json_data["unknown_0x3390e915"],
            unknown_0xf8cc3ab0=json_data["unknown_0xf8cc3ab0"],
            unknown_0xe5c90a08=json_data["unknown_0xe5c90a08"],
            unknown_0x2e95d9ad=json_data["unknown_0x2e95d9ad"],
            scan=json_data["scan"],
            unknown_0x00d1aa67=json_data["unknown_0x00d1aa67"],
            unknown_0xa57b4fac=json_data["unknown_0xa57b4fac"],
            unknown_0x8836c426=json_data["unknown_0x8836c426"],
            unknown_0xb87c5139=json_data["unknown_0xb87c5139"],
            unknown_0x9f566db4=json_data["unknown_0x9f566db4"],
            unknown_0xa2aac8e7=json_data["unknown_0xa2aac8e7"],
            unknown_0xf8aca397=json_data["unknown_0xf8aca397"],
            unknown_0x80a0b2cb=json_data["unknown_0x80a0b2cb"],
            unknown_0x69ed492e=json_data["unknown_0x69ed492e"],
            unknown_0x90419a55=json_data["unknown_0x90419a55"],
            unknown_0x761db727=json_data["unknown_0x761db727"],
            unknown_0xdcb8af1c=json_data["unknown_0xdcb8af1c"],
            unknown_0x9cfddba8=json_data["unknown_0x9cfddba8"],
            wpsc_0xf5056d9d=json_data["wpsc_0xf5056d9d"],
            wpsc_0x58dbcc52=json_data["wpsc_0x58dbcc52"],
            part_0x3a6d3a64=json_data["part_0x3a6d3a64"],
            pillar_base=json_data["pillar_base"],
            pillar_explosion_effect=json_data["pillar_explosion_effect"],
            part_0xe8706e6e=json_data["part_0xe8706e6e"],
            plasma_beam_info_0x6cc7412a=PlasmaBeamInfo.from_json(json_data["plasma_beam_info_0x6cc7412a"]),
            homing_missile_projectile=json_data["homing_missile_projectile"],
            hover_then_home_projectile=HoverThenHomeProjectile.from_json(json_data["hover_then_home_projectile"]),
            echo_animation_information=AnimationParameters.from_json(json_data["echo_animation_information"]),
            echo_explosion=json_data["echo_explosion"],
            echo_scan=json_data["echo_scan"],
            energy_wave_projectile=json_data["energy_wave_projectile"],
            plasma_beam_info_0xec493f59=PlasmaBeamInfo.from_json(json_data["plasma_beam_info_0xec493f59"]),
            super_loop_projectile=json_data["super_loop_projectile"],
            part_0x8e96e5e4=json_data["part_0x8e96e5e4"],
            txtr=json_data["txtr"],
            unknown_0x4f6e81a8=json_data["unknown_0x4f6e81a8"],
            unknown_0xe8f323f9=json_data["unknown_0xe8f323f9"],
            caud=json_data["caud"],
            unknown_0x8b8b33d9=json_data["unknown_0x8b8b33d9"],
            unknown_0x09133ecd=json_data["unknown_0x09133ecd"],
            is_dash_automatically=json_data["is_dash_automatically"],
            sound_invulnerable_loop=json_data["sound_invulnerable_loop"],
            sound_shockwave=json_data["sound_shockwave"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xb5049bbb": self.unknown_0xb5049bbb,
            "unknown_0x3390e915": self.unknown_0x3390e915,
            "unknown_0xf8cc3ab0": self.unknown_0xf8cc3ab0,
            "unknown_0xe5c90a08": self.unknown_0xe5c90a08,
            "unknown_0x2e95d9ad": self.unknown_0x2e95d9ad,
            "scan": self.scan,
            "unknown_0x00d1aa67": self.unknown_0x00d1aa67,
            "unknown_0xa57b4fac": self.unknown_0xa57b4fac,
            "unknown_0x8836c426": self.unknown_0x8836c426,
            "unknown_0xb87c5139": self.unknown_0xb87c5139,
            "unknown_0x9f566db4": self.unknown_0x9f566db4,
            "unknown_0xa2aac8e7": self.unknown_0xa2aac8e7,
            "unknown_0xf8aca397": self.unknown_0xf8aca397,
            "unknown_0x80a0b2cb": self.unknown_0x80a0b2cb,
            "unknown_0x69ed492e": self.unknown_0x69ed492e,
            "unknown_0x90419a55": self.unknown_0x90419a55,
            "unknown_0x761db727": self.unknown_0x761db727,
            "unknown_0xdcb8af1c": self.unknown_0xdcb8af1c,
            "unknown_0x9cfddba8": self.unknown_0x9cfddba8,
            "wpsc_0xf5056d9d": self.wpsc_0xf5056d9d,
            "wpsc_0x58dbcc52": self.wpsc_0x58dbcc52,
            "part_0x3a6d3a64": self.part_0x3a6d3a64,
            "pillar_base": self.pillar_base,
            "pillar_explosion_effect": self.pillar_explosion_effect,
            "part_0xe8706e6e": self.part_0xe8706e6e,
            "plasma_beam_info_0x6cc7412a": self.plasma_beam_info_0x6cc7412a.to_json(),
            "homing_missile_projectile": self.homing_missile_projectile,
            "hover_then_home_projectile": self.hover_then_home_projectile.to_json(),
            "echo_animation_information": self.echo_animation_information.to_json(),
            "echo_explosion": self.echo_explosion,
            "echo_scan": self.echo_scan,
            "energy_wave_projectile": self.energy_wave_projectile,
            "plasma_beam_info_0xec493f59": self.plasma_beam_info_0xec493f59.to_json(),
            "super_loop_projectile": self.super_loop_projectile,
            "part_0x8e96e5e4": self.part_0x8e96e5e4,
            "txtr": self.txtr,
            "unknown_0x4f6e81a8": self.unknown_0x4f6e81a8,
            "unknown_0xe8f323f9": self.unknown_0xe8f323f9,
            "caud": self.caud,
            "unknown_0x8b8b33d9": self.unknown_0x8b8b33d9,
            "unknown_0x09133ecd": self.unknown_0x09133ecd,
            "is_dash_automatically": self.is_dash_automatically,
            "sound_invulnerable_loop": self.sound_invulnerable_loop,
            "sound_shockwave": self.sound_shockwave,
        }


def _decode_plasma_beam_info_0x6cc7412a(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_hover_then_home_projectile(
    data: typing.BinaryIO, game: Game, property_size: int
) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_echo_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_plasma_beam_info_0xec493f59(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB5049BBB: ("unknown_0xb5049bbb", structs.decode_BIG_f),
    0x3390E915: ("unknown_0x3390e915", structs.decode_BIG_f),
    0xF8CC3AB0: ("unknown_0xf8cc3ab0", structs.decode_BIG_f),
    0xE5C90A08: ("unknown_0xe5c90a08", structs.decode_BIG_f),
    0x2E95D9AD: ("unknown_0x2e95d9ad", structs.decode_BIG_f),
    0x21E4D323: ("scan", structs.decode_BIG_Q),
    0x00D1AA67: ("unknown_0x00d1aa67", structs.decode_BIG_l),
    0xA57B4FAC: ("unknown_0xa57b4fac", structs.decode_BIG_l),
    0x8836C426: ("unknown_0x8836c426", structs.decode_BIG_l),
    0xB87C5139: ("unknown_0xb87c5139", structs.decode_BIG_l),
    0x9F566DB4: ("unknown_0x9f566db4", structs.decode_BIG_l),
    0xA2AAC8E7: ("unknown_0xa2aac8e7", structs.decode_BIG_l),
    0xF8ACA397: ("unknown_0xf8aca397", structs.decode_BIG_l),
    0x80A0B2CB: ("unknown_0x80a0b2cb", structs.decode_BIG_l),
    0x69ED492E: ("unknown_0x69ed492e", structs.decode_BIG_l),
    0x90419A55: ("unknown_0x90419a55", structs.decode_BIG_l),
    0x761DB727: ("unknown_0x761db727", structs.decode_BIG_l),
    0xDCB8AF1C: ("unknown_0xdcb8af1c", structs.decode_BIG_l),
    0x9CFDDBA8: ("unknown_0x9cfddba8", structs.decode_BIG_l),
    0xF5056D9D: ("wpsc_0xf5056d9d", structs.decode_BIG_Q),
    0x58DBCC52: ("wpsc_0x58dbcc52", structs.decode_BIG_Q),
    0x3A6D3A64: ("part_0x3a6d3a64", structs.decode_BIG_Q),
    0xF3D84488: ("pillar_base", structs.decode_BIG_Q),
    0x49BE8A11: ("pillar_explosion_effect", structs.decode_BIG_Q),
    0xE8706E6E: ("part_0xe8706e6e", structs.decode_BIG_Q),
    0x6CC7412A: ("plasma_beam_info_0x6cc7412a", _decode_plasma_beam_info_0x6cc7412a),
    0xACFD8EA8: ("homing_missile_projectile", structs.decode_BIG_Q),
    0xE8FC7798: ("hover_then_home_projectile", _decode_hover_then_home_projectile),
    0x5377D4B5: ("echo_animation_information", _decode_echo_animation_information),
    0x4C8AEE6D: ("echo_explosion", structs.decode_BIG_Q),
    0x0B17536C: ("echo_scan", structs.decode_BIG_Q),
    0x76C64459: ("energy_wave_projectile", structs.decode_BIG_Q),
    0xEC493F59: ("plasma_beam_info_0xec493f59", _decode_plasma_beam_info_0xec493f59),
    0xD1D51E35: ("super_loop_projectile", structs.decode_BIG_Q),
    0x8E96E5E4: ("part_0x8e96e5e4", structs.decode_BIG_Q),
    0x5B67A4E7: ("txtr", structs.decode_BIG_Q),
    0x4F6E81A8: ("unknown_0x4f6e81a8", structs.decode_BIG_f),
    0xE8F323F9: ("unknown_0xe8f323f9", structs.decode_BIG_Q),
    0x9049A2FB: ("caud", structs.decode_BIG_Q),
    0x8B8B33D9: ("unknown_0x8b8b33d9", structs.decode_BIG_Q),
    0x09133ECD: ("unknown_0x09133ecd", structs.decode_BIG_Q),
    0x3C67B14E: ("is_dash_automatically", structs.decode_BIG_Q),
    0xAF6889B0: ("sound_invulnerable_loop", structs.decode_BIG_Q),
    0xA47E51D3: ("sound_shockwave", structs.decode_BIG_Q),
}
