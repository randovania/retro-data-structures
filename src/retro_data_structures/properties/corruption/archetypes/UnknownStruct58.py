# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct58Json(typing_extensions.TypedDict):
        unknown_0x90aefee1: bool
        char: json_util.JsonObject
        swarm_bot_vulnerability: json_util.JsonObject
        part_0xb64ed093: int
        unknown_0xc7dc6d3e: int
        unknown_0x41481f90: int
        giant_form_electric_effect: int
        part_0x3b5b99a8: int
        giant_electric_ball_effect: int
        part_0x2975be8d: int
        part_0x3dcf98a5: int
        part_0xdc17fb84: int
        part_0xc35db9ce: int
        part_0xa70e1bbb: int
        part_0x7cc1b298: int
        part_0x7be868ce: int
        ring_idle_effect: int
        part_0x4d9ed8e1: int
        ring_projectile: int
        ring_explosion_effect: int
        wheel_portal_effect: int
        wheel_tumble_effect: int
        part_0xe3c3de5e: int
        shock_not_solid: int
        elsc: int
        part_0x3b6cdadb: int
        part_0xa6e942ed: int
        plasma_beam_info: json_util.JsonObject
        part_0x82ee63c8: int
        part_0xab0a66da: int
        txtr: int
        unknown_0x4f6e81a8: float
        interface_delayed_effect: int
        scan_sphere_form: int
        scan_tornado_form: int
        scan_wheel_form: int
        scan_ring_form: int
        scan_giant_form: int
        scan: int
        caud_0x9a469187: int
        caud_0xa959b017: int


@dataclasses.dataclass()
class UnknownStruct58(BaseProperty):
    unknown_0x90aefee1: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x90AEFEE1, original_name="Unknown"),
        },
    )
    char: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x4C64D3A6,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    swarm_bot_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x00DD06CC,
                original_name="SwarmBotVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    part_0xb64ed093: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB64ED093, original_name="PART"),
        },
    )
    unknown_0xc7dc6d3e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC7DC6D3E, original_name="Unknown"),
        },
    )
    unknown_0x41481f90: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x41481F90, original_name="Unknown"),
        },
    )
    giant_form_electric_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC5012A38, original_name="GiantFormElectricEffect"),
        },
    )
    part_0x3b5b99a8: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3B5B99A8, original_name="PART"),
        },
    )
    giant_electric_ball_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6AE0CAE6, original_name="GiantElectricBallEffect"),
        },
    )
    part_0x2975be8d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2975BE8D, original_name="PART"),
        },
    )
    part_0x3dcf98a5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3DCF98A5, original_name="PART"),
        },
    )
    part_0xdc17fb84: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDC17FB84, original_name="PART"),
        },
    )
    part_0xc35db9ce: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC35DB9CE, original_name="PART"),
        },
    )
    part_0xa70e1bbb: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA70E1BBB, original_name="PART"),
        },
    )
    part_0x7cc1b298: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7CC1B298, original_name="PART"),
        },
    )
    part_0x7be868ce: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7BE868CE, original_name="PART"),
        },
    )
    ring_idle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC90CDA8C, original_name="RingIdleEffect"),
        },
    )
    part_0x4d9ed8e1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4D9ED8E1, original_name="PART"),
        },
    )
    ring_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x21DC4C35, original_name="RingProjectile"),
        },
    )
    ring_explosion_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCB673DA3, original_name="RingExplosionEffect"),
        },
    )
    wheel_portal_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC1BBBED8, original_name="WheelPortalEffect"),
        },
    )
    wheel_tumble_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF4386C42, original_name="WheelTumbleEffect"),
        },
    )
    part_0xe3c3de5e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE3C3DE5E, original_name="PART"),
        },
    )
    shock_not_solid: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1899C839, original_name="ShockNotSolid"),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6B6606B8, original_name="ELSC"),
        },
    )
    part_0x3b6cdadb: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3B6CDADB, original_name="PART"),
        },
    )
    part_0xa6e942ed: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA6E942ED, original_name="PART"),
        },
    )
    plasma_beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x21EC3D21,
                original_name="PlasmaBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    part_0x82ee63c8: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x82EE63C8, original_name="PART"),
        },
    )
    part_0xab0a66da: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAB0A66DA, original_name="PART"),
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
    interface_delayed_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAD6ECC7F, original_name="InterfaceDelayedEffect"),
        },
    )
    scan_sphere_form: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x91D5F317, original_name="Scan_SphereForm"),
        },
    )
    scan_tornado_form: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1DDFD45A, original_name="Scan_TornadoForm"),
        },
    )
    scan_wheel_form: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x01FBA748, original_name="Scan_WheelForm"),
        },
    )
    scan_ring_form: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCD2F3D00, original_name="Scan_RingForm"),
        },
    )
    scan_giant_form: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAE813F86, original_name="Scan_GiantForm"),
        },
    )
    scan: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD27E8786, original_name="SCAN"),
        },
    )
    caud_0x9a469187: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9A469187, original_name="CAUD"),
        },
    )
    caud_0xa959b017: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA959B017, original_name="CAUD"),
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
        if property_count != 41:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90AEFEE1
        unknown_0x90aefee1 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C64D3A6
        char = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00DD06CC
        swarm_bot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB64ED093
        part_0xb64ed093 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7DC6D3E
        unknown_0xc7dc6d3e = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41481F90
        unknown_0x41481f90 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5012A38
        giant_form_electric_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3B5B99A8
        part_0x3b5b99a8 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6AE0CAE6
        giant_electric_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2975BE8D
        part_0x2975be8d = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DCF98A5
        part_0x3dcf98a5 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC17FB84
        part_0xdc17fb84 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC35DB9CE
        part_0xc35db9ce = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA70E1BBB
        part_0xa70e1bbb = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CC1B298
        part_0x7cc1b298 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7BE868CE
        part_0x7be868ce = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC90CDA8C
        ring_idle_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D9ED8E1
        part_0x4d9ed8e1 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21DC4C35
        ring_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB673DA3
        ring_explosion_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC1BBBED8
        wheel_portal_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4386C42
        wheel_tumble_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE3C3DE5E
        part_0xe3c3de5e = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1899C839
        shock_not_solid = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6B6606B8
        elsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3B6CDADB
        part_0x3b6cdadb = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6E942ED
        part_0xa6e942ed = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21EC3D21
        plasma_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82EE63C8
        part_0x82ee63c8 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB0A66DA
        part_0xab0a66da = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B67A4E7
        txtr = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F6E81A8
        unknown_0x4f6e81a8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD6ECC7F
        interface_delayed_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91D5F317
        scan_sphere_form = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1DDFD45A
        scan_tornado_form = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01FBA748
        scan_wheel_form = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD2F3D00
        scan_ring_form = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE813F86
        scan_giant_form = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD27E8786
        scan = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A469187
        caud_0x9a469187 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA959B017
        caud_0xa959b017 = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            unknown_0x90aefee1,
            char,
            swarm_bot_vulnerability,
            part_0xb64ed093,
            unknown_0xc7dc6d3e,
            unknown_0x41481f90,
            giant_form_electric_effect,
            part_0x3b5b99a8,
            giant_electric_ball_effect,
            part_0x2975be8d,
            part_0x3dcf98a5,
            part_0xdc17fb84,
            part_0xc35db9ce,
            part_0xa70e1bbb,
            part_0x7cc1b298,
            part_0x7be868ce,
            ring_idle_effect,
            part_0x4d9ed8e1,
            ring_projectile,
            ring_explosion_effect,
            wheel_portal_effect,
            wheel_tumble_effect,
            part_0xe3c3de5e,
            shock_not_solid,
            elsc,
            part_0x3b6cdadb,
            part_0xa6e942ed,
            plasma_beam_info,
            part_0x82ee63c8,
            part_0xab0a66da,
            txtr,
            unknown_0x4f6e81a8,
            interface_delayed_effect,
            scan_sphere_form,
            scan_tornado_form,
            scan_wheel_form,
            scan_ring_form,
            scan_giant_form,
            scan,
            caud_0x9a469187,
            caud_0xa959b017,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00)")  # 41 properties

        data.write(b"\x90\xae\xfe\xe1")  # 0x90aefee1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x90aefee1))

        data.write(b"Ld\xd3\xa6")  # 0x4c64d3a6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\xdd\x06\xcc")  # 0xdd06cc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.swarm_bot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb6N\xd0\x93")  # 0xb64ed093
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xb64ed093))

        data.write(b"\xc7\xdcm>")  # 0xc7dc6d3e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xc7dc6d3e))

        data.write(b"AH\x1f\x90")  # 0x41481f90
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x41481f90))

        data.write(b"\xc5\x01*8")  # 0xc5012a38
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.giant_form_electric_effect))

        data.write(b";[\x99\xa8")  # 0x3b5b99a8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x3b5b99a8))

        data.write(b"j\xe0\xca\xe6")  # 0x6ae0cae6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.giant_electric_ball_effect))

        data.write(b")u\xbe\x8d")  # 0x2975be8d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x2975be8d))

        data.write(b"=\xcf\x98\xa5")  # 0x3dcf98a5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x3dcf98a5))

        data.write(b"\xdc\x17\xfb\x84")  # 0xdc17fb84
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xdc17fb84))

        data.write(b"\xc3]\xb9\xce")  # 0xc35db9ce
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xc35db9ce))

        data.write(b"\xa7\x0e\x1b\xbb")  # 0xa70e1bbb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xa70e1bbb))

        data.write(b"|\xc1\xb2\x98")  # 0x7cc1b298
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x7cc1b298))

        data.write(b"{\xe8h\xce")  # 0x7be868ce
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x7be868ce))

        data.write(b"\xc9\x0c\xda\x8c")  # 0xc90cda8c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ring_idle_effect))

        data.write(b"M\x9e\xd8\xe1")  # 0x4d9ed8e1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x4d9ed8e1))

        data.write(b"!\xdcL5")  # 0x21dc4c35
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ring_projectile))

        data.write(b"\xcbg=\xa3")  # 0xcb673da3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.ring_explosion_effect))

        data.write(b"\xc1\xbb\xbe\xd8")  # 0xc1bbbed8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wheel_portal_effect))

        data.write(b"\xf48lB")  # 0xf4386c42
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wheel_tumble_effect))

        data.write(b"\xe3\xc3\xde^")  # 0xe3c3de5e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xe3c3de5e))

        data.write(b"\x18\x99\xc89")  # 0x1899c839
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.shock_not_solid))

        data.write(b"kf\x06\xb8")  # 0x6b6606b8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc))

        data.write(b";l\xda\xdb")  # 0x3b6cdadb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x3b6cdadb))

        data.write(b"\xa6\xe9B\xed")  # 0xa6e942ed
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xa6e942ed))

        data.write(b"!\xec=!")  # 0x21ec3d21
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.plasma_beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x82\xeec\xc8")  # 0x82ee63c8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x82ee63c8))

        data.write(b"\xab\nf\xda")  # 0xab0a66da
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xab0a66da))

        data.write(b"[g\xa4\xe7")  # 0x5b67a4e7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.txtr))

        data.write(b"On\x81\xa8")  # 0x4f6e81a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f6e81a8))

        data.write(b"\xadn\xcc\x7f")  # 0xad6ecc7f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.interface_delayed_effect))

        data.write(b"\x91\xd5\xf3\x17")  # 0x91d5f317
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_sphere_form))

        data.write(b"\x1d\xdf\xd4Z")  # 0x1ddfd45a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_tornado_form))

        data.write(b"\x01\xfb\xa7H")  # 0x1fba748
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_wheel_form))

        data.write(b"\xcd/=\x00")  # 0xcd2f3d00
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_ring_form))

        data.write(b"\xae\x81?\x86")  # 0xae813f86
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_giant_form))

        data.write(b"\xd2~\x87\x86")  # 0xd27e8786
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan))

        data.write(b"\x9aF\x91\x87")  # 0x9a469187
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x9a469187))

        data.write(b"\xa9Y\xb0\x17")  # 0xa959b017
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xa959b017))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct58Json", data)
        return cls(
            unknown_0x90aefee1=json_data["unknown_0x90aefee1"],
            char=AnimationParameters.from_json(json_data["char"]),
            swarm_bot_vulnerability=DamageVulnerability.from_json(json_data["swarm_bot_vulnerability"]),
            part_0xb64ed093=json_data["part_0xb64ed093"],
            unknown_0xc7dc6d3e=json_data["unknown_0xc7dc6d3e"],
            unknown_0x41481f90=json_data["unknown_0x41481f90"],
            giant_form_electric_effect=json_data["giant_form_electric_effect"],
            part_0x3b5b99a8=json_data["part_0x3b5b99a8"],
            giant_electric_ball_effect=json_data["giant_electric_ball_effect"],
            part_0x2975be8d=json_data["part_0x2975be8d"],
            part_0x3dcf98a5=json_data["part_0x3dcf98a5"],
            part_0xdc17fb84=json_data["part_0xdc17fb84"],
            part_0xc35db9ce=json_data["part_0xc35db9ce"],
            part_0xa70e1bbb=json_data["part_0xa70e1bbb"],
            part_0x7cc1b298=json_data["part_0x7cc1b298"],
            part_0x7be868ce=json_data["part_0x7be868ce"],
            ring_idle_effect=json_data["ring_idle_effect"],
            part_0x4d9ed8e1=json_data["part_0x4d9ed8e1"],
            ring_projectile=json_data["ring_projectile"],
            ring_explosion_effect=json_data["ring_explosion_effect"],
            wheel_portal_effect=json_data["wheel_portal_effect"],
            wheel_tumble_effect=json_data["wheel_tumble_effect"],
            part_0xe3c3de5e=json_data["part_0xe3c3de5e"],
            shock_not_solid=json_data["shock_not_solid"],
            elsc=json_data["elsc"],
            part_0x3b6cdadb=json_data["part_0x3b6cdadb"],
            part_0xa6e942ed=json_data["part_0xa6e942ed"],
            plasma_beam_info=PlasmaBeamInfo.from_json(json_data["plasma_beam_info"]),
            part_0x82ee63c8=json_data["part_0x82ee63c8"],
            part_0xab0a66da=json_data["part_0xab0a66da"],
            txtr=json_data["txtr"],
            unknown_0x4f6e81a8=json_data["unknown_0x4f6e81a8"],
            interface_delayed_effect=json_data["interface_delayed_effect"],
            scan_sphere_form=json_data["scan_sphere_form"],
            scan_tornado_form=json_data["scan_tornado_form"],
            scan_wheel_form=json_data["scan_wheel_form"],
            scan_ring_form=json_data["scan_ring_form"],
            scan_giant_form=json_data["scan_giant_form"],
            scan=json_data["scan"],
            caud_0x9a469187=json_data["caud_0x9a469187"],
            caud_0xa959b017=json_data["caud_0xa959b017"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x90aefee1": self.unknown_0x90aefee1,
            "char": self.char.to_json(),
            "swarm_bot_vulnerability": self.swarm_bot_vulnerability.to_json(),
            "part_0xb64ed093": self.part_0xb64ed093,
            "unknown_0xc7dc6d3e": self.unknown_0xc7dc6d3e,
            "unknown_0x41481f90": self.unknown_0x41481f90,
            "giant_form_electric_effect": self.giant_form_electric_effect,
            "part_0x3b5b99a8": self.part_0x3b5b99a8,
            "giant_electric_ball_effect": self.giant_electric_ball_effect,
            "part_0x2975be8d": self.part_0x2975be8d,
            "part_0x3dcf98a5": self.part_0x3dcf98a5,
            "part_0xdc17fb84": self.part_0xdc17fb84,
            "part_0xc35db9ce": self.part_0xc35db9ce,
            "part_0xa70e1bbb": self.part_0xa70e1bbb,
            "part_0x7cc1b298": self.part_0x7cc1b298,
            "part_0x7be868ce": self.part_0x7be868ce,
            "ring_idle_effect": self.ring_idle_effect,
            "part_0x4d9ed8e1": self.part_0x4d9ed8e1,
            "ring_projectile": self.ring_projectile,
            "ring_explosion_effect": self.ring_explosion_effect,
            "wheel_portal_effect": self.wheel_portal_effect,
            "wheel_tumble_effect": self.wheel_tumble_effect,
            "part_0xe3c3de5e": self.part_0xe3c3de5e,
            "shock_not_solid": self.shock_not_solid,
            "elsc": self.elsc,
            "part_0x3b6cdadb": self.part_0x3b6cdadb,
            "part_0xa6e942ed": self.part_0xa6e942ed,
            "plasma_beam_info": self.plasma_beam_info.to_json(),
            "part_0x82ee63c8": self.part_0x82ee63c8,
            "part_0xab0a66da": self.part_0xab0a66da,
            "txtr": self.txtr,
            "unknown_0x4f6e81a8": self.unknown_0x4f6e81a8,
            "interface_delayed_effect": self.interface_delayed_effect,
            "scan_sphere_form": self.scan_sphere_form,
            "scan_tornado_form": self.scan_tornado_form,
            "scan_wheel_form": self.scan_wheel_form,
            "scan_ring_form": self.scan_ring_form,
            "scan_giant_form": self.scan_giant_form,
            "scan": self.scan,
            "caud_0x9a469187": self.caud_0x9a469187,
            "caud_0xa959b017": self.caud_0xa959b017,
        }


def _decode_char(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_swarm_bot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_plasma_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x90AEFEE1: ("unknown_0x90aefee1", structs.decode_BIG_bool_),
    0x4C64D3A6: ("char", _decode_char),
    0x00DD06CC: ("swarm_bot_vulnerability", _decode_swarm_bot_vulnerability),
    0xB64ED093: ("part_0xb64ed093", structs.decode_BIG_Q),
    0xC7DC6D3E: ("unknown_0xc7dc6d3e", structs.decode_BIG_Q),
    0x41481F90: ("unknown_0x41481f90", structs.decode_BIG_Q),
    0xC5012A38: ("giant_form_electric_effect", structs.decode_BIG_Q),
    0x3B5B99A8: ("part_0x3b5b99a8", structs.decode_BIG_Q),
    0x6AE0CAE6: ("giant_electric_ball_effect", structs.decode_BIG_Q),
    0x2975BE8D: ("part_0x2975be8d", structs.decode_BIG_Q),
    0x3DCF98A5: ("part_0x3dcf98a5", structs.decode_BIG_Q),
    0xDC17FB84: ("part_0xdc17fb84", structs.decode_BIG_Q),
    0xC35DB9CE: ("part_0xc35db9ce", structs.decode_BIG_Q),
    0xA70E1BBB: ("part_0xa70e1bbb", structs.decode_BIG_Q),
    0x7CC1B298: ("part_0x7cc1b298", structs.decode_BIG_Q),
    0x7BE868CE: ("part_0x7be868ce", structs.decode_BIG_Q),
    0xC90CDA8C: ("ring_idle_effect", structs.decode_BIG_Q),
    0x4D9ED8E1: ("part_0x4d9ed8e1", structs.decode_BIG_Q),
    0x21DC4C35: ("ring_projectile", structs.decode_BIG_Q),
    0xCB673DA3: ("ring_explosion_effect", structs.decode_BIG_Q),
    0xC1BBBED8: ("wheel_portal_effect", structs.decode_BIG_Q),
    0xF4386C42: ("wheel_tumble_effect", structs.decode_BIG_Q),
    0xE3C3DE5E: ("part_0xe3c3de5e", structs.decode_BIG_Q),
    0x1899C839: ("shock_not_solid", structs.decode_BIG_Q),
    0x6B6606B8: ("elsc", structs.decode_BIG_Q),
    0x3B6CDADB: ("part_0x3b6cdadb", structs.decode_BIG_Q),
    0xA6E942ED: ("part_0xa6e942ed", structs.decode_BIG_Q),
    0x21EC3D21: ("plasma_beam_info", _decode_plasma_beam_info),
    0x82EE63C8: ("part_0x82ee63c8", structs.decode_BIG_Q),
    0xAB0A66DA: ("part_0xab0a66da", structs.decode_BIG_Q),
    0x5B67A4E7: ("txtr", structs.decode_BIG_Q),
    0x4F6E81A8: ("unknown_0x4f6e81a8", structs.decode_BIG_f),
    0xAD6ECC7F: ("interface_delayed_effect", structs.decode_BIG_Q),
    0x91D5F317: ("scan_sphere_form", structs.decode_BIG_Q),
    0x1DDFD45A: ("scan_tornado_form", structs.decode_BIG_Q),
    0x01FBA748: ("scan_wheel_form", structs.decode_BIG_Q),
    0xCD2F3D00: ("scan_ring_form", structs.decode_BIG_Q),
    0xAE813F86: ("scan_giant_form", structs.decode_BIG_Q),
    0xD27E8786: ("scan", structs.decode_BIG_Q),
    0x9A469187: ("caud_0x9a469187", structs.decode_BIG_Q),
    0xA959B017: ("caud_0xa959b017", structs.decode_BIG_Q),
}
