# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.HyperModeData import HyperModeData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.ModIncaData import ModIncaData
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SteamBotDataJson(typing_extensions.TypedDict):
        char: json_util.JsonObject
        unknown_0xf4f4a01d: float
        unknown_0x12940ffc: float
        unknown_0x303b4954: float
        rocket: json_util.JsonObject
        rocket_range_max: float
        rocket_range_min: float
        unknown_0x0588c742: float
        unknown_0x15793154: json_util.JsonValue
        unknown_0xe8fc0acd: float
        hover_then_home_projectile: json_util.JsonObject
        ray_gun: json_util.JsonObject
        unknown_0xdde5dccd: float
        unknown_0x3b85732c: float
        unknown_0x296b1195: float
        unknown_0xcf0bbe74: float
        unknown_0xa0d2af02: float
        unknown_0xd7b53cdb: int
        claw_damage: json_util.JsonObject
        claw_range_max: float
        claw_range_min: float
        claw_delay: float
        steam_blast: json_util.JsonObject
        steam_texture: int
        steam_alpha: float
        steam_fade_in: float
        steam_fade_out: float
        unknown_0xa296206a: float
        unknown_0x10c7fd02: float
        unknown_0xf6a752e3: float
        unknown_0x802b706e: float
        unknown_0xc80ac7db: float
        unknown_0x2e6a683a: float
        unknown_0x3e9f0188: float
        unknown_0xd8ffae69: float
        xy_scale: json_util.JsonObject
        z_scale: json_util.JsonObject
        model_alpha: json_util.JsonObject
        model_red: json_util.JsonObject
        model_green: json_util.JsonObject
        model_blue: json_util.JsonObject
        effects_alpha: json_util.JsonObject
        recheck_path_time: float
        recheck_path_distance: float
        avoidance_range: float
        scan_delay: float
        unknown_0x699da662: float
        unknown_0x8ffd0983: float
        unknown_0xdedd30a4: bool
        unknown_0xf8243d17: bool
        unknown_0xc6943950: int
        unknown_0x83967ad2: int
        unknown_0x6c8ae89f: float
        unknown_0x8aea477e: float
        unknown_0x5f1a7dd8: bool
        hyper_mode: json_util.JsonObject
        hyper_mode_hard: json_util.JsonObject
        hyper_mode_elite: json_util.JsonObject
        hurl_lerp: float
        hurl_knock_back_multiplier: float
        hurl_knock_back_resistance: float
        unknown_0x6cf3636f: float
        unknown_0x85d4691c: bool
        mod_inca_data: json_util.JsonObject


@dataclasses.dataclass()
class SteamBotData(BaseProperty):
    char: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xBE5E86B9,
                original_name="CHAR",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    unknown_0xf4f4a01d: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4F4A01D, original_name="Unknown"),
        },
    )
    unknown_0x12940ffc: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x12940FFC, original_name="Unknown"),
        },
    )
    unknown_0x303b4954: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x303B4954, original_name="Unknown"),
        },
    )
    rocket: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xAB247451,
                original_name="Rocket",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    rocket_range_max: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x55C19435, original_name="RocketRangeMax"),
        },
    )
    rocket_range_min: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB3A13BD4, original_name="RocketRangeMin"),
        },
    )
    unknown_0x0588c742: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0588C742, original_name="Unknown"),
        },
    )
    unknown_0x15793154: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x15793154, original_name="Unknown", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0xe8fc0acd: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8FC0ACD, original_name="Unknown"),
        },
    )
    hover_then_home_projectile: HoverThenHomeProjectile = dataclasses.field(
        default_factory=HoverThenHomeProjectile,
        metadata={
            "reflection": FieldReflection[HoverThenHomeProjectile](
                HoverThenHomeProjectile,
                id=0x7039FB9F,
                original_name="HoverThenHomeProjectile",
                from_json=HoverThenHomeProjectile.from_json,
                to_json=HoverThenHomeProjectile.to_json,
            ),
        },
    )
    ray_gun: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xB98CBA47,
                original_name="RayGun",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    unknown_0xdde5dccd: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDDE5DCCD, original_name="Unknown"),
        },
    )
    unknown_0x3b85732c: float = dataclasses.field(
        default=0.014999999664723873,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3B85732C, original_name="Unknown"),
        },
    )
    unknown_0x296b1195: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x296B1195, original_name="Unknown"),
        },
    )
    unknown_0xcf0bbe74: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF0BBE74, original_name="Unknown"),
        },
    )
    unknown_0xa0d2af02: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA0D2AF02, original_name="Unknown"),
        },
    )
    unknown_0xd7b53cdb: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD7B53CDB, original_name="Unknown"),
        },
    )
    claw_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8DBAEEF2,
                original_name="ClawDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    claw_range_max: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x582B9B3B, original_name="ClawRangeMax"),
        },
    )
    claw_range_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBE4B34DA, original_name="ClawRangeMin"),
        },
    )
    claw_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEBB134B5, original_name="ClawDelay"),
        },
    )
    steam_blast: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0xCA91ECB0,
                original_name="SteamBlast",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    steam_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x58A21824, original_name="SteamTexture"),
        },
    )
    steam_alpha: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C692453, original_name="SteamAlpha"),
        },
    )
    steam_fade_in: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x66A5CD17, original_name="SteamFadeIn"),
        },
    )
    steam_fade_out: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5C5B8B5D, original_name="SteamFadeOut"),
        },
    )
    unknown_0xa296206a: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA296206A, original_name="Unknown"),
        },
    )
    unknown_0x10c7fd02: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x10C7FD02, original_name="Unknown"),
        },
    )
    unknown_0xf6a752e3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF6A752E3, original_name="Unknown"),
        },
    )
    unknown_0x802b706e: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0x802B706E, original_name="Unknown"),
        },
    )
    unknown_0xc80ac7db: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC80AC7DB, original_name="Unknown"),
        },
    )
    unknown_0x2e6a683a: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2E6A683A, original_name="Unknown"),
        },
    )
    unknown_0x3e9f0188: float = dataclasses.field(
        default=1.100000023841858,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E9F0188, original_name="Unknown"),
        },
    )
    unknown_0xd8ffae69: float = dataclasses.field(
        default=0.8999999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD8FFAE69, original_name="Unknown"),
        },
    )
    xy_scale: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x48BA8EB1, original_name="XYScale", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    z_scale: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x180C38B0, original_name="ZScale", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    model_alpha: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x0F762790, original_name="ModelAlpha", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    model_red: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x0FEADC99, original_name="ModelRed", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    model_green: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x55BE3E8E, original_name="ModelGreen", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    model_blue: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x79F7CC48, original_name="ModelBlue", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    effects_alpha: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x564BD8CD, original_name="EffectsAlpha", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    recheck_path_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9AA90B6B, original_name="RecheckPathTime"),
        },
    )
    recheck_path_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7626EC89, original_name="RecheckPathDistance"),
        },
    )
    avoidance_range: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x50A9BD0D, original_name="AvoidanceRange"),
        },
    )
    scan_delay: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FC827A2, original_name="ScanDelay"),
        },
    )
    unknown_0x699da662: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x699DA662, original_name="Unknown"),
        },
    )
    unknown_0x8ffd0983: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8FFD0983, original_name="Unknown"),
        },
    )
    unknown_0xdedd30a4: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xDEDD30A4, original_name="Unknown"),
        },
    )
    unknown_0xf8243d17: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF8243D17, original_name="Unknown"),
        },
    )
    unknown_0xc6943950: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC6943950, original_name="Unknown"),
        },
    )
    unknown_0x83967ad2: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x83967AD2, original_name="Unknown"),
        },
    )
    unknown_0x6c8ae89f: float = dataclasses.field(
        default=2.0999999046325684,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C8AE89F, original_name="Unknown"),
        },
    )
    unknown_0x8aea477e: float = dataclasses.field(
        default=1.899999976158142,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8AEA477E, original_name="Unknown"),
        },
    )
    unknown_0x5f1a7dd8: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5F1A7DD8, original_name="Unknown"),
        },
    )
    hyper_mode: HyperModeData = dataclasses.field(
        default_factory=HyperModeData,
        metadata={
            "reflection": FieldReflection[HyperModeData](
                HyperModeData,
                id=0xB0A9B728,
                original_name="HyperMode",
                from_json=HyperModeData.from_json,
                to_json=HyperModeData.to_json,
            ),
        },
    )
    hyper_mode_hard: HyperModeData = dataclasses.field(
        default_factory=HyperModeData,
        metadata={
            "reflection": FieldReflection[HyperModeData](
                HyperModeData,
                id=0x14499FCB,
                original_name="HyperModeHard",
                from_json=HyperModeData.from_json,
                to_json=HyperModeData.to_json,
            ),
        },
    )
    hyper_mode_elite: HyperModeData = dataclasses.field(
        default_factory=HyperModeData,
        metadata={
            "reflection": FieldReflection[HyperModeData](
                HyperModeData,
                id=0xCD02221C,
                original_name="HyperModeElite",
                from_json=HyperModeData.from_json,
                to_json=HyperModeData.to_json,
            ),
        },
    )
    hurl_lerp: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x19863914, original_name="HurlLerp"),
        },
    )
    hurl_knock_back_multiplier: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x04AB182A, original_name="HurlKnockBackMultiplier"),
        },
    )
    hurl_knock_back_resistance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB008320B, original_name="HurlKnockBackResistance"),
        },
    )
    unknown_0x6cf3636f: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6CF3636F, original_name="Unknown"),
        },
    )
    unknown_0x85d4691c: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x85D4691C, original_name="Unknown"),
        },
    )
    mod_inca_data: ModIncaData = dataclasses.field(
        default_factory=ModIncaData,
        metadata={
            "reflection": FieldReflection[ModIncaData](
                ModIncaData,
                id=0xB4C02854,
                original_name="ModIncaData",
                from_json=ModIncaData.from_json,
                to_json=ModIncaData.to_json,
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
        if property_count != 64:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE5E86B9
        char = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4F4A01D
        unknown_0xf4f4a01d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12940FFC
        unknown_0x12940ffc = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x303B4954
        unknown_0x303b4954 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB247451
        rocket = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55C19435
        rocket_range_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3A13BD4
        rocket_range_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0588C742
        unknown_0x0588c742 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15793154
        unknown_0x15793154 = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8FC0ACD
        unknown_0xe8fc0acd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7039FB9F
        hover_then_home_projectile = HoverThenHomeProjectile.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB98CBA47
        ray_gun = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDDE5DCCD
        unknown_0xdde5dccd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3B85732C
        unknown_0x3b85732c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x296B1195
        unknown_0x296b1195 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF0BBE74
        unknown_0xcf0bbe74 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0D2AF02
        unknown_0xa0d2af02 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD7B53CDB
        unknown_0xd7b53cdb = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8DBAEEF2
        claw_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x582B9B3B
        claw_range_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE4B34DA
        claw_range_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBB134B5
        claw_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCA91ECB0
        steam_blast = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58A21824
        steam_texture = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C692453
        steam_alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66A5CD17
        steam_fade_in = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C5B8B5D
        steam_fade_out = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA296206A
        unknown_0xa296206a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10C7FD02
        unknown_0x10c7fd02 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF6A752E3
        unknown_0xf6a752e3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x802B706E
        unknown_0x802b706e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC80AC7DB
        unknown_0xc80ac7db = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E6A683A
        unknown_0x2e6a683a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E9F0188
        unknown_0x3e9f0188 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8FFAE69
        unknown_0xd8ffae69 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48BA8EB1
        xy_scale = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x180C38B0
        z_scale = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F762790
        model_alpha = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0FEADC99
        model_red = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55BE3E8E
        model_green = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79F7CC48
        model_blue = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x564BD8CD
        effects_alpha = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AA90B6B
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626EC89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50A9BD0D
        avoidance_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FC827A2
        scan_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x699DA662
        unknown_0x699da662 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8FFD0983
        unknown_0x8ffd0983 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDEDD30A4
        unknown_0xdedd30a4 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8243D17
        unknown_0xf8243d17 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6943950
        unknown_0xc6943950 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83967AD2
        unknown_0x83967ad2 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C8AE89F
        unknown_0x6c8ae89f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8AEA477E
        unknown_0x8aea477e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F1A7DD8
        unknown_0x5f1a7dd8 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB0A9B728
        hyper_mode = HyperModeData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14499FCB
        hyper_mode_hard = HyperModeData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD02221C
        hyper_mode_elite = HyperModeData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19863914
        hurl_lerp = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04AB182A
        hurl_knock_back_multiplier = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB008320B
        hurl_knock_back_resistance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6CF3636F
        unknown_0x6cf3636f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85D4691C
        unknown_0x85d4691c = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB4C02854
        mod_inca_data = ModIncaData.from_stream(data, game, property_size)

        return cls(
            char,
            unknown_0xf4f4a01d,
            unknown_0x12940ffc,
            unknown_0x303b4954,
            rocket,
            rocket_range_max,
            rocket_range_min,
            unknown_0x0588c742,
            unknown_0x15793154,
            unknown_0xe8fc0acd,
            hover_then_home_projectile,
            ray_gun,
            unknown_0xdde5dccd,
            unknown_0x3b85732c,
            unknown_0x296b1195,
            unknown_0xcf0bbe74,
            unknown_0xa0d2af02,
            unknown_0xd7b53cdb,
            claw_damage,
            claw_range_max,
            claw_range_min,
            claw_delay,
            steam_blast,
            steam_texture,
            steam_alpha,
            steam_fade_in,
            steam_fade_out,
            unknown_0xa296206a,
            unknown_0x10c7fd02,
            unknown_0xf6a752e3,
            unknown_0x802b706e,
            unknown_0xc80ac7db,
            unknown_0x2e6a683a,
            unknown_0x3e9f0188,
            unknown_0xd8ffae69,
            xy_scale,
            z_scale,
            model_alpha,
            model_red,
            model_green,
            model_blue,
            effects_alpha,
            recheck_path_time,
            recheck_path_distance,
            avoidance_range,
            scan_delay,
            unknown_0x699da662,
            unknown_0x8ffd0983,
            unknown_0xdedd30a4,
            unknown_0xf8243d17,
            unknown_0xc6943950,
            unknown_0x83967ad2,
            unknown_0x6c8ae89f,
            unknown_0x8aea477e,
            unknown_0x5f1a7dd8,
            hyper_mode,
            hyper_mode_hard,
            hyper_mode_elite,
            hurl_lerp,
            hurl_knock_back_multiplier,
            hurl_knock_back_resistance,
            unknown_0x6cf3636f,
            unknown_0x85d4691c,
            mod_inca_data,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00@")  # 64 properties

        data.write(b"\xbe^\x86\xb9")  # 0xbe5e86b9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.char.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xf4\xa0\x1d")  # 0xf4f4a01d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf4f4a01d))

        data.write(b"\x12\x94\x0f\xfc")  # 0x12940ffc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x12940ffc))

        data.write(b"0;IT")  # 0x303b4954
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x303b4954))

        data.write(b"\xab$tQ")  # 0xab247451
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.rocket.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"U\xc1\x945")  # 0x55c19435
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rocket_range_max))

        data.write(b"\xb3\xa1;\xd4")  # 0xb3a13bd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rocket_range_min))

        data.write(b"\x05\x88\xc7B")  # 0x588c742
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0588c742))

        data.write(b"\x15y1T")  # 0x15793154
        data.write(b"\x00\x0c")  # size
        self.unknown_0x15793154.to_stream(data, game)

        data.write(b"\xe8\xfc\n\xcd")  # 0xe8fc0acd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8fc0acd))

        data.write(b"p9\xfb\x9f")  # 0x7039fb9f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hover_then_home_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb9\x8c\xbaG")  # 0xb98cba47
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ray_gun.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdd\xe5\xdc\xcd")  # 0xdde5dccd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdde5dccd))

        data.write(b";\x85s,")  # 0x3b85732c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3b85732c))

        data.write(b")k\x11\x95")  # 0x296b1195
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x296b1195))

        data.write(b"\xcf\x0b\xbet")  # 0xcf0bbe74
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcf0bbe74))

        data.write(b"\xa0\xd2\xaf\x02")  # 0xa0d2af02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa0d2af02))

        data.write(b"\xd7\xb5<\xdb")  # 0xd7b53cdb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd7b53cdb))

        data.write(b"\x8d\xba\xee\xf2")  # 0x8dbaeef2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.claw_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X+\x9b;")  # 0x582b9b3b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.claw_range_max))

        data.write(b"\xbeK4\xda")  # 0xbe4b34da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.claw_range_min))

        data.write(b"\xeb\xb14\xb5")  # 0xebb134b5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.claw_delay))

        data.write(b"\xca\x91\xec\xb0")  # 0xca91ecb0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.steam_blast.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\xa2\x18$")  # 0x58a21824
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.steam_texture))

        data.write(b"li$S")  # 0x6c692453
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.steam_alpha))

        data.write(b"f\xa5\xcd\x17")  # 0x66a5cd17
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.steam_fade_in))

        data.write(b"\\[\x8b]")  # 0x5c5b8b5d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.steam_fade_out))

        data.write(b"\xa2\x96 j")  # 0xa296206a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa296206a))

        data.write(b"\x10\xc7\xfd\x02")  # 0x10c7fd02
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x10c7fd02))

        data.write(b"\xf6\xa7R\xe3")  # 0xf6a752e3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf6a752e3))

        data.write(b"\x80+pn")  # 0x802b706e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x802b706e))

        data.write(b"\xc8\n\xc7\xdb")  # 0xc80ac7db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc80ac7db))

        data.write(b".jh:")  # 0x2e6a683a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2e6a683a))

        data.write(b">\x9f\x01\x88")  # 0x3e9f0188
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3e9f0188))

        data.write(b"\xd8\xff\xaei")  # 0xd8ffae69
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd8ffae69))

        data.write(b"H\xba\x8e\xb1")  # 0x48ba8eb1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.xy_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x18\x0c8\xb0")  # 0x180c38b0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.z_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0fv'\x90")  # 0xf762790
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.model_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0f\xea\xdc\x99")  # 0xfeadc99
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.model_red.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"U\xbe>\x8e")  # 0x55be3e8e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.model_green.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"y\xf7\xccH")  # 0x79f7cc48
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.model_blue.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"VK\xd8\xcd")  # 0x564bd8cd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.effects_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9a\xa9\x0bk")  # 0x9aa90b6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b"v&\xec\x89")  # 0x7626ec89
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b"P\xa9\xbd\r")  # 0x50a9bd0d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b"\x7f\xc8'\xa2")  # 0x7fc827a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scan_delay))

        data.write(b"i\x9d\xa6b")  # 0x699da662
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x699da662))

        data.write(b"\x8f\xfd\t\x83")  # 0x8ffd0983
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8ffd0983))

        data.write(b"\xde\xdd0\xa4")  # 0xdedd30a4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xdedd30a4))

        data.write(b"\xf8$=\x17")  # 0xf8243d17
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf8243d17))

        data.write(b"\xc6\x949P")  # 0xc6943950
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc6943950))

        data.write(b"\x83\x96z\xd2")  # 0x83967ad2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x83967ad2))

        data.write(b"l\x8a\xe8\x9f")  # 0x6c8ae89f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6c8ae89f))

        data.write(b"\x8a\xeaG~")  # 0x8aea477e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8aea477e))

        data.write(b"_\x1a}\xd8")  # 0x5f1a7dd8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x5f1a7dd8))

        data.write(b"\xb0\xa9\xb7(")  # 0xb0a9b728
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x14I\x9f\xcb")  # 0x14499fcb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_hard.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcd\x02"\x1c')  # 0xcd02221c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hyper_mode_elite.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\x869\x14")  # 0x19863914
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hurl_lerp))

        data.write(b"\x04\xab\x18*")  # 0x4ab182a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hurl_knock_back_multiplier))

        data.write(b"\xb0\x082\x0b")  # 0xb008320b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hurl_knock_back_resistance))

        data.write(b"l\xf3co")  # 0x6cf3636f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6cf3636f))

        data.write(b"\x85\xd4i\x1c")  # 0x85d4691c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x85d4691c))

        data.write(b"\xb4\xc0(T")  # 0xb4c02854
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.mod_inca_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SteamBotDataJson", data)
        return cls(
            char=AnimationParameters.from_json(json_data["char"]),
            unknown_0xf4f4a01d=json_data["unknown_0xf4f4a01d"],
            unknown_0x12940ffc=json_data["unknown_0x12940ffc"],
            unknown_0x303b4954=json_data["unknown_0x303b4954"],
            rocket=LaunchProjectileData.from_json(json_data["rocket"]),
            rocket_range_max=json_data["rocket_range_max"],
            rocket_range_min=json_data["rocket_range_min"],
            unknown_0x0588c742=json_data["unknown_0x0588c742"],
            unknown_0x15793154=Vector.from_json(json_data["unknown_0x15793154"]),
            unknown_0xe8fc0acd=json_data["unknown_0xe8fc0acd"],
            hover_then_home_projectile=HoverThenHomeProjectile.from_json(json_data["hover_then_home_projectile"]),
            ray_gun=LaunchProjectileData.from_json(json_data["ray_gun"]),
            unknown_0xdde5dccd=json_data["unknown_0xdde5dccd"],
            unknown_0x3b85732c=json_data["unknown_0x3b85732c"],
            unknown_0x296b1195=json_data["unknown_0x296b1195"],
            unknown_0xcf0bbe74=json_data["unknown_0xcf0bbe74"],
            unknown_0xa0d2af02=json_data["unknown_0xa0d2af02"],
            unknown_0xd7b53cdb=json_data["unknown_0xd7b53cdb"],
            claw_damage=DamageInfo.from_json(json_data["claw_damage"]),
            claw_range_max=json_data["claw_range_max"],
            claw_range_min=json_data["claw_range_min"],
            claw_delay=json_data["claw_delay"],
            steam_blast=LaunchProjectileData.from_json(json_data["steam_blast"]),
            steam_texture=json_data["steam_texture"],
            steam_alpha=json_data["steam_alpha"],
            steam_fade_in=json_data["steam_fade_in"],
            steam_fade_out=json_data["steam_fade_out"],
            unknown_0xa296206a=json_data["unknown_0xa296206a"],
            unknown_0x10c7fd02=json_data["unknown_0x10c7fd02"],
            unknown_0xf6a752e3=json_data["unknown_0xf6a752e3"],
            unknown_0x802b706e=json_data["unknown_0x802b706e"],
            unknown_0xc80ac7db=json_data["unknown_0xc80ac7db"],
            unknown_0x2e6a683a=json_data["unknown_0x2e6a683a"],
            unknown_0x3e9f0188=json_data["unknown_0x3e9f0188"],
            unknown_0xd8ffae69=json_data["unknown_0xd8ffae69"],
            xy_scale=Spline.from_json(json_data["xy_scale"]),
            z_scale=Spline.from_json(json_data["z_scale"]),
            model_alpha=Spline.from_json(json_data["model_alpha"]),
            model_red=Spline.from_json(json_data["model_red"]),
            model_green=Spline.from_json(json_data["model_green"]),
            model_blue=Spline.from_json(json_data["model_blue"]),
            effects_alpha=Spline.from_json(json_data["effects_alpha"]),
            recheck_path_time=json_data["recheck_path_time"],
            recheck_path_distance=json_data["recheck_path_distance"],
            avoidance_range=json_data["avoidance_range"],
            scan_delay=json_data["scan_delay"],
            unknown_0x699da662=json_data["unknown_0x699da662"],
            unknown_0x8ffd0983=json_data["unknown_0x8ffd0983"],
            unknown_0xdedd30a4=json_data["unknown_0xdedd30a4"],
            unknown_0xf8243d17=json_data["unknown_0xf8243d17"],
            unknown_0xc6943950=json_data["unknown_0xc6943950"],
            unknown_0x83967ad2=json_data["unknown_0x83967ad2"],
            unknown_0x6c8ae89f=json_data["unknown_0x6c8ae89f"],
            unknown_0x8aea477e=json_data["unknown_0x8aea477e"],
            unknown_0x5f1a7dd8=json_data["unknown_0x5f1a7dd8"],
            hyper_mode=HyperModeData.from_json(json_data["hyper_mode"]),
            hyper_mode_hard=HyperModeData.from_json(json_data["hyper_mode_hard"]),
            hyper_mode_elite=HyperModeData.from_json(json_data["hyper_mode_elite"]),
            hurl_lerp=json_data["hurl_lerp"],
            hurl_knock_back_multiplier=json_data["hurl_knock_back_multiplier"],
            hurl_knock_back_resistance=json_data["hurl_knock_back_resistance"],
            unknown_0x6cf3636f=json_data["unknown_0x6cf3636f"],
            unknown_0x85d4691c=json_data["unknown_0x85d4691c"],
            mod_inca_data=ModIncaData.from_json(json_data["mod_inca_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "char": self.char.to_json(),
            "unknown_0xf4f4a01d": self.unknown_0xf4f4a01d,
            "unknown_0x12940ffc": self.unknown_0x12940ffc,
            "unknown_0x303b4954": self.unknown_0x303b4954,
            "rocket": self.rocket.to_json(),
            "rocket_range_max": self.rocket_range_max,
            "rocket_range_min": self.rocket_range_min,
            "unknown_0x0588c742": self.unknown_0x0588c742,
            "unknown_0x15793154": self.unknown_0x15793154.to_json(),
            "unknown_0xe8fc0acd": self.unknown_0xe8fc0acd,
            "hover_then_home_projectile": self.hover_then_home_projectile.to_json(),
            "ray_gun": self.ray_gun.to_json(),
            "unknown_0xdde5dccd": self.unknown_0xdde5dccd,
            "unknown_0x3b85732c": self.unknown_0x3b85732c,
            "unknown_0x296b1195": self.unknown_0x296b1195,
            "unknown_0xcf0bbe74": self.unknown_0xcf0bbe74,
            "unknown_0xa0d2af02": self.unknown_0xa0d2af02,
            "unknown_0xd7b53cdb": self.unknown_0xd7b53cdb,
            "claw_damage": self.claw_damage.to_json(),
            "claw_range_max": self.claw_range_max,
            "claw_range_min": self.claw_range_min,
            "claw_delay": self.claw_delay,
            "steam_blast": self.steam_blast.to_json(),
            "steam_texture": self.steam_texture,
            "steam_alpha": self.steam_alpha,
            "steam_fade_in": self.steam_fade_in,
            "steam_fade_out": self.steam_fade_out,
            "unknown_0xa296206a": self.unknown_0xa296206a,
            "unknown_0x10c7fd02": self.unknown_0x10c7fd02,
            "unknown_0xf6a752e3": self.unknown_0xf6a752e3,
            "unknown_0x802b706e": self.unknown_0x802b706e,
            "unknown_0xc80ac7db": self.unknown_0xc80ac7db,
            "unknown_0x2e6a683a": self.unknown_0x2e6a683a,
            "unknown_0x3e9f0188": self.unknown_0x3e9f0188,
            "unknown_0xd8ffae69": self.unknown_0xd8ffae69,
            "xy_scale": self.xy_scale.to_json(),
            "z_scale": self.z_scale.to_json(),
            "model_alpha": self.model_alpha.to_json(),
            "model_red": self.model_red.to_json(),
            "model_green": self.model_green.to_json(),
            "model_blue": self.model_blue.to_json(),
            "effects_alpha": self.effects_alpha.to_json(),
            "recheck_path_time": self.recheck_path_time,
            "recheck_path_distance": self.recheck_path_distance,
            "avoidance_range": self.avoidance_range,
            "scan_delay": self.scan_delay,
            "unknown_0x699da662": self.unknown_0x699da662,
            "unknown_0x8ffd0983": self.unknown_0x8ffd0983,
            "unknown_0xdedd30a4": self.unknown_0xdedd30a4,
            "unknown_0xf8243d17": self.unknown_0xf8243d17,
            "unknown_0xc6943950": self.unknown_0xc6943950,
            "unknown_0x83967ad2": self.unknown_0x83967ad2,
            "unknown_0x6c8ae89f": self.unknown_0x6c8ae89f,
            "unknown_0x8aea477e": self.unknown_0x8aea477e,
            "unknown_0x5f1a7dd8": self.unknown_0x5f1a7dd8,
            "hyper_mode": self.hyper_mode.to_json(),
            "hyper_mode_hard": self.hyper_mode_hard.to_json(),
            "hyper_mode_elite": self.hyper_mode_elite.to_json(),
            "hurl_lerp": self.hurl_lerp,
            "hurl_knock_back_multiplier": self.hurl_knock_back_multiplier,
            "hurl_knock_back_resistance": self.hurl_knock_back_resistance,
            "unknown_0x6cf3636f": self.unknown_0x6cf3636f,
            "unknown_0x85d4691c": self.unknown_0x85d4691c,
            "mod_inca_data": self.mod_inca_data.to_json(),
        }


def _decode_char(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_rocket(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_unknown_0x15793154(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_hover_then_home_projectile(
    data: typing.BinaryIO, game: Game, property_size: int
) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_ray_gun(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_claw_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_steam_blast(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_xy_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_z_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_red(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_green(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_blue(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_effects_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_hyper_mode_hard(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_hyper_mode_elite(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_mod_inca_data(data: typing.BinaryIO, game: Game, property_size: int) -> ModIncaData:
    return ModIncaData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xBE5E86B9: ("char", _decode_char),
    0xF4F4A01D: ("unknown_0xf4f4a01d", structs.decode_BIG_f),
    0x12940FFC: ("unknown_0x12940ffc", structs.decode_BIG_f),
    0x303B4954: ("unknown_0x303b4954", structs.decode_BIG_f),
    0xAB247451: ("rocket", _decode_rocket),
    0x55C19435: ("rocket_range_max", structs.decode_BIG_f),
    0xB3A13BD4: ("rocket_range_min", structs.decode_BIG_f),
    0x0588C742: ("unknown_0x0588c742", structs.decode_BIG_f),
    0x15793154: ("unknown_0x15793154", _decode_unknown_0x15793154),
    0xE8FC0ACD: ("unknown_0xe8fc0acd", structs.decode_BIG_f),
    0x7039FB9F: ("hover_then_home_projectile", _decode_hover_then_home_projectile),
    0xB98CBA47: ("ray_gun", _decode_ray_gun),
    0xDDE5DCCD: ("unknown_0xdde5dccd", structs.decode_BIG_f),
    0x3B85732C: ("unknown_0x3b85732c", structs.decode_BIG_f),
    0x296B1195: ("unknown_0x296b1195", structs.decode_BIG_f),
    0xCF0BBE74: ("unknown_0xcf0bbe74", structs.decode_BIG_f),
    0xA0D2AF02: ("unknown_0xa0d2af02", structs.decode_BIG_f),
    0xD7B53CDB: ("unknown_0xd7b53cdb", structs.decode_BIG_l),
    0x8DBAEEF2: ("claw_damage", _decode_claw_damage),
    0x582B9B3B: ("claw_range_max", structs.decode_BIG_f),
    0xBE4B34DA: ("claw_range_min", structs.decode_BIG_f),
    0xEBB134B5: ("claw_delay", structs.decode_BIG_f),
    0xCA91ECB0: ("steam_blast", _decode_steam_blast),
    0x58A21824: ("steam_texture", structs.decode_BIG_Q),
    0x6C692453: ("steam_alpha", structs.decode_BIG_f),
    0x66A5CD17: ("steam_fade_in", structs.decode_BIG_f),
    0x5C5B8B5D: ("steam_fade_out", structs.decode_BIG_f),
    0xA296206A: ("unknown_0xa296206a", structs.decode_BIG_f),
    0x10C7FD02: ("unknown_0x10c7fd02", structs.decode_BIG_f),
    0xF6A752E3: ("unknown_0xf6a752e3", structs.decode_BIG_f),
    0x802B706E: ("unknown_0x802b706e", structs.decode_BIG_f),
    0xC80AC7DB: ("unknown_0xc80ac7db", structs.decode_BIG_f),
    0x2E6A683A: ("unknown_0x2e6a683a", structs.decode_BIG_f),
    0x3E9F0188: ("unknown_0x3e9f0188", structs.decode_BIG_f),
    0xD8FFAE69: ("unknown_0xd8ffae69", structs.decode_BIG_f),
    0x48BA8EB1: ("xy_scale", _decode_xy_scale),
    0x180C38B0: ("z_scale", _decode_z_scale),
    0x0F762790: ("model_alpha", _decode_model_alpha),
    0x0FEADC99: ("model_red", _decode_model_red),
    0x55BE3E8E: ("model_green", _decode_model_green),
    0x79F7CC48: ("model_blue", _decode_model_blue),
    0x564BD8CD: ("effects_alpha", _decode_effects_alpha),
    0x9AA90B6B: ("recheck_path_time", structs.decode_BIG_f),
    0x7626EC89: ("recheck_path_distance", structs.decode_BIG_f),
    0x50A9BD0D: ("avoidance_range", structs.decode_BIG_f),
    0x7FC827A2: ("scan_delay", structs.decode_BIG_f),
    0x699DA662: ("unknown_0x699da662", structs.decode_BIG_f),
    0x8FFD0983: ("unknown_0x8ffd0983", structs.decode_BIG_f),
    0xDEDD30A4: ("unknown_0xdedd30a4", structs.decode_BIG_bool_),
    0xF8243D17: ("unknown_0xf8243d17", structs.decode_BIG_bool_),
    0xC6943950: ("unknown_0xc6943950", structs.decode_BIG_l),
    0x83967AD2: ("unknown_0x83967ad2", structs.decode_BIG_l),
    0x6C8AE89F: ("unknown_0x6c8ae89f", structs.decode_BIG_f),
    0x8AEA477E: ("unknown_0x8aea477e", structs.decode_BIG_f),
    0x5F1A7DD8: ("unknown_0x5f1a7dd8", structs.decode_BIG_bool_),
    0xB0A9B728: ("hyper_mode", _decode_hyper_mode),
    0x14499FCB: ("hyper_mode_hard", _decode_hyper_mode_hard),
    0xCD02221C: ("hyper_mode_elite", _decode_hyper_mode_elite),
    0x19863914: ("hurl_lerp", structs.decode_BIG_f),
    0x04AB182A: ("hurl_knock_back_multiplier", structs.decode_BIG_f),
    0xB008320B: ("hurl_knock_back_resistance", structs.decode_BIG_f),
    0x6CF3636F: ("unknown_0x6cf3636f", structs.decode_BIG_f),
    0x85D4691C: ("unknown_0x85d4691c", structs.decode_BIG_bool_),
    0xB4C02854: ("mod_inca_data", _decode_mod_inca_data),
}
