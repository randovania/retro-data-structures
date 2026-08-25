# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.LayerInfo import LayerInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FluidPropertiesJson(typing_extensions.TypedDict):
        fluid_type: int
        is_morph_target: bool
        render_surface: bool
        render_under_surface: bool
        unknown_0x3ddca674: bool
        unknown_0x4817eaa7: bool
        unknown_0x13013139: float
        grid_spacing: float
        unknown_0x4c60077e: float
        unknown_0x8518047a: float
        bloom: int
        base_color: json_util.JsonValue
        underwater_fog_color: json_util.JsonValue
        color_map: int
        color_warp_map: int
        gloss_map: int
        env_map: int
        light_map: int
        txtr: int
        unknown_0xdd2f6dbd: float
        unknown_0xf90deda5: float
        unknown_0x3425e83f: float
        flow_speed: float
        flow_orientation: float
        flow_color: json_util.JsonObject
        layer_info_0xe75248e4: json_util.JsonObject
        layer_info_0x385e0d43: json_util.JsonObject
        layer_info_0xd369b640: json_util.JsonObject
        layer_info_0x6ddea66d: json_util.JsonObject
        splash_color: json_util.JsonValue
        splash_effect_tiny: int
        splash_effect_small: int
        splash_effect_medium: int
        splash_effect_big: int
        splash_sound_tiny: int
        calculate_seed: int
        splash_sound_medium: int
        splash_sound_big: int
        caud_0x0efcdea0: int
        caud_0x78df0e7f: int
        unknown_0x84e241ed: float
        unknown_0xe2072799: float
        rolling_splash_effect: int
        runoff_visor_effect: int
        runoff_ball_effect: int
        slow_exit_sound: int
        fast_exit_sound: int
        fast_exit_speed: float
        unknown_0x687df7a3: float
        unknown_0xe73aad13: float
        unknown_0xac67b7d7: float
        fog_color: json_util.JsonValue
        fog_height: float
        fog_bob_height: float
        fog_bob_freq: float
        unknown_0xfe3bc8f7: bool
        freeze_radius: float
        player_freeze_radius: float
        caud_0x84927794: int
        caud_0xa6e650a0: int
        vertical_sound: int
        damage_sound: int
        damage_effect: int
        footstep_sound: int
        filter_sound_effects: bool
        volume_attenuation: float
        unknown_0x414379ea: int
        fluid_lock_string: str


class FluidType(enum.IntEnum):
    Unknown1 = 1425213472
    Unknown2 = 230544723
    Unknown3 = 1204522302

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


class Bloom(enum.IntEnum):
    Unknown1 = 1222417634
    Unknown2 = 759120936
    Unknown3 = 413038581
    Unknown4 = 3476137679
    Unknown5 = 1255115501
    Unknown6 = 131148223
    Unknown7 = 176197152

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class FluidProperties(BaseProperty):
    fluid_type: FluidType = dataclasses.field(
        default=FluidType.Unknown1,
        metadata={
            "reflection": FieldReflection[FluidType](
                FluidType,
                id=0xBE253B54,
                original_name="FluidType",
                from_json=FluidType.from_json,
                to_json=FluidType.to_json,
            ),
        },
    )
    is_morph_target: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7F2A8353, original_name="IsMorphTarget"),
        },
    )
    render_surface: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB5E9859F, original_name="RenderSurface"),
        },
    )
    render_under_surface: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1F5E78C2, original_name="RenderUnderSurface"),
        },
    )
    unknown_0x3ddca674: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3DDCA674, original_name="Unknown"),
        },
    )
    unknown_0x4817eaa7: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4817EAA7, original_name="Unknown"),
        },
    )
    unknown_0x13013139: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x13013139, original_name="Unknown"),
        },
    )
    grid_spacing: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x628F03DB, original_name="GridSpacing"),
        },
    )
    unknown_0x4c60077e: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4C60077E, original_name="Unknown"),
        },
    )
    unknown_0x8518047a: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8518047A, original_name="Unknown"),
        },
    )
    bloom: Bloom = dataclasses.field(
        default=Bloom.Unknown1,
        metadata={
            "reflection": FieldReflection[Bloom](
                Bloom, id=0xA4D23616, original_name="Bloom", from_json=Bloom.from_json, to_json=Bloom.to_json
            ),
        },
    )
    base_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.49803900718688965, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x041398D5, original_name="BaseColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    underwater_fog_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.49803900718688965, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color,
                id=0x5A96218C,
                original_name="UnderwaterFogColor",
                from_json=Color.from_json,
                to_json=Color.to_json,
            ),
        },
    )
    color_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5E8B37DD, original_name="ColorMap"),
        },
    )
    color_warp_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x031D987E, original_name="ColorWarpMap"),
        },
    )
    gloss_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5AA79C9F, original_name="GlossMap"),
        },
    )
    env_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2F0645CF, original_name="EnvMap"),
        },
    )
    light_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2421A2BF, original_name="LightMap"),
        },
    )
    txtr: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7A4B4685, original_name="TXTR"),
        },
    )
    unknown_0xdd2f6dbd: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDD2F6DBD, original_name="Unknown"),
        },
    )
    unknown_0xf90deda5: float = dataclasses.field(
        default=0.05000000074505806,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF90DEDA5, original_name="Unknown"),
        },
    )
    unknown_0x3425e83f: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3425E83F, original_name="Unknown"),
        },
    )
    flow_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF14E3A14, original_name="FlowSpeed"),
        },
    )
    flow_orientation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x33EECDFD, original_name="FlowOrientation"),
        },
    )
    flow_color: LayerInfo = dataclasses.field(
        default_factory=LayerInfo,
        metadata={
            "reflection": FieldReflection[LayerInfo](
                LayerInfo,
                id=0x244E9E6D,
                original_name="FlowColor",
                from_json=LayerInfo.from_json,
                to_json=LayerInfo.to_json,
            ),
        },
    )
    layer_info_0xe75248e4: LayerInfo = dataclasses.field(
        default_factory=LayerInfo,
        metadata={
            "reflection": FieldReflection[LayerInfo](
                LayerInfo,
                id=0xE75248E4,
                original_name="LayerInfo",
                from_json=LayerInfo.from_json,
                to_json=LayerInfo.to_json,
            ),
        },
    )
    layer_info_0x385e0d43: LayerInfo = dataclasses.field(
        default_factory=LayerInfo,
        metadata={
            "reflection": FieldReflection[LayerInfo](
                LayerInfo,
                id=0x385E0D43,
                original_name="LayerInfo",
                from_json=LayerInfo.from_json,
                to_json=LayerInfo.to_json,
            ),
        },
    )
    layer_info_0xd369b640: LayerInfo = dataclasses.field(
        default_factory=LayerInfo,
        metadata={
            "reflection": FieldReflection[LayerInfo](
                LayerInfo,
                id=0xD369B640,
                original_name="LayerInfo",
                from_json=LayerInfo.from_json,
                to_json=LayerInfo.to_json,
            ),
        },
    )
    layer_info_0x6ddea66d: LayerInfo = dataclasses.field(
        default_factory=LayerInfo,
        metadata={
            "reflection": FieldReflection[LayerInfo](
                LayerInfo,
                id=0x6DDEA66D,
                original_name="LayerInfo",
                from_json=LayerInfo.from_json,
                to_json=LayerInfo.to_json,
            ),
        },
    )
    splash_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x13B56C22, original_name="SplashColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    splash_effect_tiny: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3DA16854, original_name="SplashEffectTiny"),
        },
    )
    splash_effect_small: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x856941FE, original_name="SplashEffectSmall"),
        },
    )
    splash_effect_medium: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x341EC63B, original_name="SplashEffectMedium"),
        },
    )
    splash_effect_big: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x388E3C07, original_name="SplashEffectBig"),
        },
    )
    splash_sound_tiny: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x418643C2, original_name="SplashSoundTiny"),
        },
    )
    calculate_seed: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9C7950A4, original_name="CalculateSeed"),
        },
    )
    splash_sound_medium: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBFB96EC0, original_name="SplashSoundMedium"),
        },
    )
    splash_sound_big: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC34A1DC9, original_name="SplashSoundBig"),
        },
    )
    caud_0x0efcdea0: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0EFCDEA0, original_name="CAUD"),
        },
    )
    caud_0x78df0e7f: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x78DF0E7F, original_name="CAUD"),
        },
    )
    unknown_0x84e241ed: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x84E241ED, original_name="Unknown"),
        },
    )
    unknown_0xe2072799: float = dataclasses.field(
        default=45000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE2072799, original_name="Unknown"),
        },
    )
    rolling_splash_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAB463F9A, original_name="RollingSplashEffect"),
        },
    )
    runoff_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x66D466B5, original_name="RunoffVisorEffect"),
        },
    )
    runoff_ball_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB97CCEDE, original_name="RunoffBallEffect"),
        },
    )
    slow_exit_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4D82BB1E, original_name="SlowExitSound"),
        },
    )
    fast_exit_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC51DA2DC, original_name="FastExitSound"),
        },
    )
    fast_exit_speed: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x03D24E64, original_name="FastExitSpeed"),
        },
    )
    unknown_0x687df7a3: float = dataclasses.field(
        default=-0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x687DF7A3, original_name="Unknown"),
        },
    )
    unknown_0xe73aad13: float = dataclasses.field(
        default=-1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE73AAD13, original_name="Unknown"),
        },
    )
    unknown_0xac67b7d7: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAC67B7D7, original_name="Unknown"),
        },
    )
    fog_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE578C0DD, original_name="FogColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    fog_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB4B0FD8D, original_name="FogHeight"),
        },
    )
    fog_bob_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB90DFF44, original_name="FogBobHeight"),
        },
    )
    fog_bob_freq: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF608D35C, original_name="FogBobFreq"),
        },
    )
    unknown_0xfe3bc8f7: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFE3BC8F7, original_name="Unknown"),
        },
    )
    freeze_radius: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x318418AA, original_name="FreezeRadius"),
        },
    )
    player_freeze_radius: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7B77E31D, original_name="PlayerFreezeRadius"),
        },
    )
    caud_0x84927794: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x84927794, original_name="CAUD"),
        },
    )
    caud_0xa6e650a0: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA6E650A0, original_name="CAUD"),
        },
    )
    vertical_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x90B8EB66, original_name="VerticalSound"),
        },
    )
    damage_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3EEDE8F7, original_name="DamageSound"),
        },
    )
    damage_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC110ED44, original_name="DamageEffect"),
        },
    )
    footstep_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB9413FE6, original_name="FootstepSound"),
        },
    )
    filter_sound_effects: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x822118B4, original_name="FilterSoundEffects"),
        },
    )
    volume_attenuation: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFE89B6E4, original_name="VolumeAttenuation"),
        },
    )
    unknown_0x414379ea: int = dataclasses.field(
        default=300,
        metadata={
            "reflection": FieldReflection[int](int, id=0x414379EA, original_name="Unknown"),
        },
    )
    fluid_lock_string: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x3C764739, original_name="FluidLockString"),
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
        if property_count != 68:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE253B54
        fluid_type = FluidType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F2A8353
        is_morph_target = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5E9859F
        render_surface = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1F5E78C2
        render_under_surface = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DDCA674
        unknown_0x3ddca674 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4817EAA7
        unknown_0x4817eaa7 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13013139
        unknown_0x13013139 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x628F03DB
        grid_spacing = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C60077E
        unknown_0x4c60077e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8518047A
        unknown_0x8518047a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4D23616
        bloom = Bloom.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041398D5
        base_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5A96218C
        underwater_fog_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E8B37DD
        color_map = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x031D987E
        color_warp_map = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5AA79C9F
        gloss_map = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F0645CF
        env_map = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2421A2BF
        light_map = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A4B4685
        txtr = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD2F6DBD
        unknown_0xdd2f6dbd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF90DEDA5
        unknown_0xf90deda5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3425E83F
        unknown_0x3425e83f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF14E3A14
        flow_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33EECDFD
        flow_orientation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x244E9E6D
        flow_color = LayerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE75248E4
        layer_info_0xe75248e4 = LayerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385E0D43
        layer_info_0x385e0d43 = LayerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD369B640
        layer_info_0xd369b640 = LayerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DDEA66D
        layer_info_0x6ddea66d = LayerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13B56C22
        splash_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DA16854
        splash_effect_tiny = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x856941FE
        splash_effect_small = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x341EC63B
        splash_effect_medium = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388E3C07
        splash_effect_big = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x418643C2
        splash_sound_tiny = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9C7950A4
        calculate_seed = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFB96EC0
        splash_sound_medium = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC34A1DC9
        splash_sound_big = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0EFCDEA0
        caud_0x0efcdea0 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78DF0E7F
        caud_0x78df0e7f = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84E241ED
        unknown_0x84e241ed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2072799
        unknown_0xe2072799 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB463F9A
        rolling_splash_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66D466B5
        runoff_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB97CCEDE
        runoff_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D82BB1E
        slow_exit_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC51DA2DC
        fast_exit_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03D24E64
        fast_exit_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x687DF7A3
        unknown_0x687df7a3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE73AAD13
        unknown_0xe73aad13 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC67B7D7
        unknown_0xac67b7d7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE578C0DD
        fog_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB4B0FD8D
        fog_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB90DFF44
        fog_bob_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF608D35C
        fog_bob_freq = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE3BC8F7
        unknown_0xfe3bc8f7 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x318418AA
        freeze_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B77E31D
        player_freeze_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84927794
        caud_0x84927794 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6E650A0
        caud_0xa6e650a0 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90B8EB66
        vertical_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3EEDE8F7
        damage_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC110ED44
        damage_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB9413FE6
        footstep_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x822118B4
        filter_sound_effects = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE89B6E4
        volume_attenuation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x414379EA
        unknown_0x414379ea = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C764739
        fluid_lock_string = data.read(property_size)[:-1].decode("utf-8")

        return cls(
            fluid_type,
            is_morph_target,
            render_surface,
            render_under_surface,
            unknown_0x3ddca674,
            unknown_0x4817eaa7,
            unknown_0x13013139,
            grid_spacing,
            unknown_0x4c60077e,
            unknown_0x8518047a,
            bloom,
            base_color,
            underwater_fog_color,
            color_map,
            color_warp_map,
            gloss_map,
            env_map,
            light_map,
            txtr,
            unknown_0xdd2f6dbd,
            unknown_0xf90deda5,
            unknown_0x3425e83f,
            flow_speed,
            flow_orientation,
            flow_color,
            layer_info_0xe75248e4,
            layer_info_0x385e0d43,
            layer_info_0xd369b640,
            layer_info_0x6ddea66d,
            splash_color,
            splash_effect_tiny,
            splash_effect_small,
            splash_effect_medium,
            splash_effect_big,
            splash_sound_tiny,
            calculate_seed,
            splash_sound_medium,
            splash_sound_big,
            caud_0x0efcdea0,
            caud_0x78df0e7f,
            unknown_0x84e241ed,
            unknown_0xe2072799,
            rolling_splash_effect,
            runoff_visor_effect,
            runoff_ball_effect,
            slow_exit_sound,
            fast_exit_sound,
            fast_exit_speed,
            unknown_0x687df7a3,
            unknown_0xe73aad13,
            unknown_0xac67b7d7,
            fog_color,
            fog_height,
            fog_bob_height,
            fog_bob_freq,
            unknown_0xfe3bc8f7,
            freeze_radius,
            player_freeze_radius,
            caud_0x84927794,
            caud_0xa6e650a0,
            vertical_sound,
            damage_sound,
            damage_effect,
            footstep_sound,
            filter_sound_effects,
            volume_attenuation,
            unknown_0x414379ea,
            fluid_lock_string,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00D")  # 68 properties

        data.write(b"\xbe%;T")  # 0xbe253b54
        data.write(b"\x00\x04")  # size
        self.fluid_type.to_stream(data, game)

        data.write(b"\x7f*\x83S")  # 0x7f2a8353
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_morph_target))

        data.write(b"\xb5\xe9\x85\x9f")  # 0xb5e9859f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.render_surface))

        data.write(b"\x1f^x\xc2")  # 0x1f5e78c2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.render_under_surface))

        data.write(b"=\xdc\xa6t")  # 0x3ddca674
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3ddca674))

        data.write(b"H\x17\xea\xa7")  # 0x4817eaa7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4817eaa7))

        data.write(b"\x13\x0119")  # 0x13013139
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x13013139))

        data.write(b"b\x8f\x03\xdb")  # 0x628f03db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grid_spacing))

        data.write(b"L`\x07~")  # 0x4c60077e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4c60077e))

        data.write(b"\x85\x18\x04z")  # 0x8518047a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8518047a))

        data.write(b"\xa4\xd26\x16")  # 0xa4d23616
        data.write(b"\x00\x04")  # size
        self.bloom.to_stream(data, game)

        data.write(b"\x04\x13\x98\xd5")  # 0x41398d5
        data.write(b"\x00\x10")  # size
        self.base_color.to_stream(data, game)

        data.write(b"Z\x96!\x8c")  # 0x5a96218c
        data.write(b"\x00\x10")  # size
        self.underwater_fog_color.to_stream(data, game)

        data.write(b"^\x8b7\xdd")  # 0x5e8b37dd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.color_map))

        data.write(b"\x03\x1d\x98~")  # 0x31d987e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.color_warp_map))

        data.write(b"Z\xa7\x9c\x9f")  # 0x5aa79c9f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.gloss_map))

        data.write(b"/\x06E\xcf")  # 0x2f0645cf
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.env_map))

        data.write(b"$!\xa2\xbf")  # 0x2421a2bf
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.light_map))

        data.write(b"zKF\x85")  # 0x7a4b4685
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.txtr))

        data.write(b"\xdd/m\xbd")  # 0xdd2f6dbd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdd2f6dbd))

        data.write(b"\xf9\r\xed\xa5")  # 0xf90deda5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf90deda5))

        data.write(b"4%\xe8?")  # 0x3425e83f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3425e83f))

        data.write(b"\xf1N:\x14")  # 0xf14e3a14
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flow_speed))

        data.write(b"3\xee\xcd\xfd")  # 0x33eecdfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flow_orientation))

        data.write(b"$N\x9em")  # 0x244e9e6d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flow_color.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7RH\xe4")  # 0xe75248e4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0xe75248e4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"8^\rC")  # 0x385e0d43
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0x385e0d43.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd3i\xb6@")  # 0xd369b640
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0xd369b640.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"m\xde\xa6m")  # 0x6ddea66d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0x6ddea66d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x13\xb5l"')  # 0x13b56c22
        data.write(b"\x00\x10")  # size
        self.splash_color.to_stream(data, game)

        data.write(b"=\xa1hT")  # 0x3da16854
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_tiny))

        data.write(b"\x85iA\xfe")  # 0x856941fe
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_small))

        data.write(b"4\x1e\xc6;")  # 0x341ec63b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_medium))

        data.write(b"8\x8e<\x07")  # 0x388e3c07
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_big))

        data.write(b"A\x86C\xc2")  # 0x418643c2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_tiny))

        data.write(b"\x9cyP\xa4")  # 0x9c7950a4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.calculate_seed))

        data.write(b"\xbf\xb9n\xc0")  # 0xbfb96ec0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_medium))

        data.write(b"\xc3J\x1d\xc9")  # 0xc34a1dc9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_big))

        data.write(b"\x0e\xfc\xde\xa0")  # 0xefcdea0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x0efcdea0))

        data.write(b"x\xdf\x0e\x7f")  # 0x78df0e7f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x78df0e7f))

        data.write(b"\x84\xe2A\xed")  # 0x84e241ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x84e241ed))

        data.write(b"\xe2\x07'\x99")  # 0xe2072799
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe2072799))

        data.write(b"\xabF?\x9a")  # 0xab463f9a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.rolling_splash_effect))

        data.write(b"f\xd4f\xb5")  # 0x66d466b5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.runoff_visor_effect))

        data.write(b"\xb9|\xce\xde")  # 0xb97ccede
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.runoff_ball_effect))

        data.write(b"M\x82\xbb\x1e")  # 0x4d82bb1e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.slow_exit_sound))

        data.write(b"\xc5\x1d\xa2\xdc")  # 0xc51da2dc
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.fast_exit_sound))

        data.write(b"\x03\xd2Nd")  # 0x3d24e64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fast_exit_speed))

        data.write(b"h}\xf7\xa3")  # 0x687df7a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x687df7a3))

        data.write(b"\xe7:\xad\x13")  # 0xe73aad13
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe73aad13))

        data.write(b"\xacg\xb7\xd7")  # 0xac67b7d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xac67b7d7))

        data.write(b"\xe5x\xc0\xdd")  # 0xe578c0dd
        data.write(b"\x00\x10")  # size
        self.fog_color.to_stream(data, game)

        data.write(b"\xb4\xb0\xfd\x8d")  # 0xb4b0fd8d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fog_height))

        data.write(b"\xb9\r\xffD")  # 0xb90dff44
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fog_bob_height))

        data.write(b"\xf6\x08\xd3\\")  # 0xf608d35c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fog_bob_freq))

        data.write(b"\xfe;\xc8\xf7")  # 0xfe3bc8f7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xfe3bc8f7))

        data.write(b"1\x84\x18\xaa")  # 0x318418aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.freeze_radius))

        data.write(b"{w\xe3\x1d")  # 0x7b77e31d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_freeze_radius))

        data.write(b"\x84\x92w\x94")  # 0x84927794
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x84927794))

        data.write(b"\xa6\xe6P\xa0")  # 0xa6e650a0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xa6e650a0))

        data.write(b"\x90\xb8\xebf")  # 0x90b8eb66
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.vertical_sound))

        data.write(b">\xed\xe8\xf7")  # 0x3eede8f7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.damage_sound))

        data.write(b"\xc1\x10\xedD")  # 0xc110ed44
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.damage_effect))

        data.write(b"\xb9A?\xe6")  # 0xb9413fe6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.footstep_sound))

        data.write(b"\x82!\x18\xb4")  # 0x822118b4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.filter_sound_effects))

        data.write(b"\xfe\x89\xb6\xe4")  # 0xfe89b6e4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.volume_attenuation))

        data.write(b"ACy\xea")  # 0x414379ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x414379ea))

        data.write(b"<vG9")  # 0x3c764739
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.fluid_lock_string.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FluidPropertiesJson", data)
        return cls(
            fluid_type=FluidType.from_json(json_data["fluid_type"]),
            is_morph_target=json_data["is_morph_target"],
            render_surface=json_data["render_surface"],
            render_under_surface=json_data["render_under_surface"],
            unknown_0x3ddca674=json_data["unknown_0x3ddca674"],
            unknown_0x4817eaa7=json_data["unknown_0x4817eaa7"],
            unknown_0x13013139=json_data["unknown_0x13013139"],
            grid_spacing=json_data["grid_spacing"],
            unknown_0x4c60077e=json_data["unknown_0x4c60077e"],
            unknown_0x8518047a=json_data["unknown_0x8518047a"],
            bloom=Bloom.from_json(json_data["bloom"]),
            base_color=Color.from_json(json_data["base_color"]),
            underwater_fog_color=Color.from_json(json_data["underwater_fog_color"]),
            color_map=json_data["color_map"],
            color_warp_map=json_data["color_warp_map"],
            gloss_map=json_data["gloss_map"],
            env_map=json_data["env_map"],
            light_map=json_data["light_map"],
            txtr=json_data["txtr"],
            unknown_0xdd2f6dbd=json_data["unknown_0xdd2f6dbd"],
            unknown_0xf90deda5=json_data["unknown_0xf90deda5"],
            unknown_0x3425e83f=json_data["unknown_0x3425e83f"],
            flow_speed=json_data["flow_speed"],
            flow_orientation=json_data["flow_orientation"],
            flow_color=LayerInfo.from_json(json_data["flow_color"]),
            layer_info_0xe75248e4=LayerInfo.from_json(json_data["layer_info_0xe75248e4"]),
            layer_info_0x385e0d43=LayerInfo.from_json(json_data["layer_info_0x385e0d43"]),
            layer_info_0xd369b640=LayerInfo.from_json(json_data["layer_info_0xd369b640"]),
            layer_info_0x6ddea66d=LayerInfo.from_json(json_data["layer_info_0x6ddea66d"]),
            splash_color=Color.from_json(json_data["splash_color"]),
            splash_effect_tiny=json_data["splash_effect_tiny"],
            splash_effect_small=json_data["splash_effect_small"],
            splash_effect_medium=json_data["splash_effect_medium"],
            splash_effect_big=json_data["splash_effect_big"],
            splash_sound_tiny=json_data["splash_sound_tiny"],
            calculate_seed=json_data["calculate_seed"],
            splash_sound_medium=json_data["splash_sound_medium"],
            splash_sound_big=json_data["splash_sound_big"],
            caud_0x0efcdea0=json_data["caud_0x0efcdea0"],
            caud_0x78df0e7f=json_data["caud_0x78df0e7f"],
            unknown_0x84e241ed=json_data["unknown_0x84e241ed"],
            unknown_0xe2072799=json_data["unknown_0xe2072799"],
            rolling_splash_effect=json_data["rolling_splash_effect"],
            runoff_visor_effect=json_data["runoff_visor_effect"],
            runoff_ball_effect=json_data["runoff_ball_effect"],
            slow_exit_sound=json_data["slow_exit_sound"],
            fast_exit_sound=json_data["fast_exit_sound"],
            fast_exit_speed=json_data["fast_exit_speed"],
            unknown_0x687df7a3=json_data["unknown_0x687df7a3"],
            unknown_0xe73aad13=json_data["unknown_0xe73aad13"],
            unknown_0xac67b7d7=json_data["unknown_0xac67b7d7"],
            fog_color=Color.from_json(json_data["fog_color"]),
            fog_height=json_data["fog_height"],
            fog_bob_height=json_data["fog_bob_height"],
            fog_bob_freq=json_data["fog_bob_freq"],
            unknown_0xfe3bc8f7=json_data["unknown_0xfe3bc8f7"],
            freeze_radius=json_data["freeze_radius"],
            player_freeze_radius=json_data["player_freeze_radius"],
            caud_0x84927794=json_data["caud_0x84927794"],
            caud_0xa6e650a0=json_data["caud_0xa6e650a0"],
            vertical_sound=json_data["vertical_sound"],
            damage_sound=json_data["damage_sound"],
            damage_effect=json_data["damage_effect"],
            footstep_sound=json_data["footstep_sound"],
            filter_sound_effects=json_data["filter_sound_effects"],
            volume_attenuation=json_data["volume_attenuation"],
            unknown_0x414379ea=json_data["unknown_0x414379ea"],
            fluid_lock_string=json_data["fluid_lock_string"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "fluid_type": self.fluid_type.to_json(),
            "is_morph_target": self.is_morph_target,
            "render_surface": self.render_surface,
            "render_under_surface": self.render_under_surface,
            "unknown_0x3ddca674": self.unknown_0x3ddca674,
            "unknown_0x4817eaa7": self.unknown_0x4817eaa7,
            "unknown_0x13013139": self.unknown_0x13013139,
            "grid_spacing": self.grid_spacing,
            "unknown_0x4c60077e": self.unknown_0x4c60077e,
            "unknown_0x8518047a": self.unknown_0x8518047a,
            "bloom": self.bloom.to_json(),
            "base_color": self.base_color.to_json(),
            "underwater_fog_color": self.underwater_fog_color.to_json(),
            "color_map": self.color_map,
            "color_warp_map": self.color_warp_map,
            "gloss_map": self.gloss_map,
            "env_map": self.env_map,
            "light_map": self.light_map,
            "txtr": self.txtr,
            "unknown_0xdd2f6dbd": self.unknown_0xdd2f6dbd,
            "unknown_0xf90deda5": self.unknown_0xf90deda5,
            "unknown_0x3425e83f": self.unknown_0x3425e83f,
            "flow_speed": self.flow_speed,
            "flow_orientation": self.flow_orientation,
            "flow_color": self.flow_color.to_json(),
            "layer_info_0xe75248e4": self.layer_info_0xe75248e4.to_json(),
            "layer_info_0x385e0d43": self.layer_info_0x385e0d43.to_json(),
            "layer_info_0xd369b640": self.layer_info_0xd369b640.to_json(),
            "layer_info_0x6ddea66d": self.layer_info_0x6ddea66d.to_json(),
            "splash_color": self.splash_color.to_json(),
            "splash_effect_tiny": self.splash_effect_tiny,
            "splash_effect_small": self.splash_effect_small,
            "splash_effect_medium": self.splash_effect_medium,
            "splash_effect_big": self.splash_effect_big,
            "splash_sound_tiny": self.splash_sound_tiny,
            "calculate_seed": self.calculate_seed,
            "splash_sound_medium": self.splash_sound_medium,
            "splash_sound_big": self.splash_sound_big,
            "caud_0x0efcdea0": self.caud_0x0efcdea0,
            "caud_0x78df0e7f": self.caud_0x78df0e7f,
            "unknown_0x84e241ed": self.unknown_0x84e241ed,
            "unknown_0xe2072799": self.unknown_0xe2072799,
            "rolling_splash_effect": self.rolling_splash_effect,
            "runoff_visor_effect": self.runoff_visor_effect,
            "runoff_ball_effect": self.runoff_ball_effect,
            "slow_exit_sound": self.slow_exit_sound,
            "fast_exit_sound": self.fast_exit_sound,
            "fast_exit_speed": self.fast_exit_speed,
            "unknown_0x687df7a3": self.unknown_0x687df7a3,
            "unknown_0xe73aad13": self.unknown_0xe73aad13,
            "unknown_0xac67b7d7": self.unknown_0xac67b7d7,
            "fog_color": self.fog_color.to_json(),
            "fog_height": self.fog_height,
            "fog_bob_height": self.fog_bob_height,
            "fog_bob_freq": self.fog_bob_freq,
            "unknown_0xfe3bc8f7": self.unknown_0xfe3bc8f7,
            "freeze_radius": self.freeze_radius,
            "player_freeze_radius": self.player_freeze_radius,
            "caud_0x84927794": self.caud_0x84927794,
            "caud_0xa6e650a0": self.caud_0xa6e650a0,
            "vertical_sound": self.vertical_sound,
            "damage_sound": self.damage_sound,
            "damage_effect": self.damage_effect,
            "footstep_sound": self.footstep_sound,
            "filter_sound_effects": self.filter_sound_effects,
            "volume_attenuation": self.volume_attenuation,
            "unknown_0x414379ea": self.unknown_0x414379ea,
            "fluid_lock_string": self.fluid_lock_string,
        }


def _decode_fluid_type(data: typing.BinaryIO, game: Game, property_size: int) -> FluidType:
    return FluidType.from_stream(data, game)


def _decode_bloom(data: typing.BinaryIO, game: Game, property_size: int) -> Bloom:
    return Bloom.from_stream(data, game)


def _decode_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_underwater_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flow_color(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_layer_info_0xe75248e4(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_layer_info_0x385e0d43(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_layer_info_0xd369b640(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_layer_info_0x6ddea66d(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_splash_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fluid_lock_string(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xBE253B54: ("fluid_type", _decode_fluid_type),
    0x7F2A8353: ("is_morph_target", structs.decode_BIG_bool_),
    0xB5E9859F: ("render_surface", structs.decode_BIG_bool_),
    0x1F5E78C2: ("render_under_surface", structs.decode_BIG_bool_),
    0x3DDCA674: ("unknown_0x3ddca674", structs.decode_BIG_bool_),
    0x4817EAA7: ("unknown_0x4817eaa7", structs.decode_BIG_bool_),
    0x13013139: ("unknown_0x13013139", structs.decode_BIG_f),
    0x628F03DB: ("grid_spacing", structs.decode_BIG_f),
    0x4C60077E: ("unknown_0x4c60077e", structs.decode_BIG_f),
    0x8518047A: ("unknown_0x8518047a", structs.decode_BIG_f),
    0xA4D23616: ("bloom", _decode_bloom),
    0x041398D5: ("base_color", _decode_base_color),
    0x5A96218C: ("underwater_fog_color", _decode_underwater_fog_color),
    0x5E8B37DD: ("color_map", structs.decode_BIG_Q),
    0x031D987E: ("color_warp_map", structs.decode_BIG_Q),
    0x5AA79C9F: ("gloss_map", structs.decode_BIG_Q),
    0x2F0645CF: ("env_map", structs.decode_BIG_Q),
    0x2421A2BF: ("light_map", structs.decode_BIG_Q),
    0x7A4B4685: ("txtr", structs.decode_BIG_Q),
    0xDD2F6DBD: ("unknown_0xdd2f6dbd", structs.decode_BIG_f),
    0xF90DEDA5: ("unknown_0xf90deda5", structs.decode_BIG_f),
    0x3425E83F: ("unknown_0x3425e83f", structs.decode_BIG_f),
    0xF14E3A14: ("flow_speed", structs.decode_BIG_f),
    0x33EECDFD: ("flow_orientation", structs.decode_BIG_f),
    0x244E9E6D: ("flow_color", _decode_flow_color),
    0xE75248E4: ("layer_info_0xe75248e4", _decode_layer_info_0xe75248e4),
    0x385E0D43: ("layer_info_0x385e0d43", _decode_layer_info_0x385e0d43),
    0xD369B640: ("layer_info_0xd369b640", _decode_layer_info_0xd369b640),
    0x6DDEA66D: ("layer_info_0x6ddea66d", _decode_layer_info_0x6ddea66d),
    0x13B56C22: ("splash_color", _decode_splash_color),
    0x3DA16854: ("splash_effect_tiny", structs.decode_BIG_Q),
    0x856941FE: ("splash_effect_small", structs.decode_BIG_Q),
    0x341EC63B: ("splash_effect_medium", structs.decode_BIG_Q),
    0x388E3C07: ("splash_effect_big", structs.decode_BIG_Q),
    0x418643C2: ("splash_sound_tiny", structs.decode_BIG_Q),
    0x9C7950A4: ("calculate_seed", structs.decode_BIG_Q),
    0xBFB96EC0: ("splash_sound_medium", structs.decode_BIG_Q),
    0xC34A1DC9: ("splash_sound_big", structs.decode_BIG_Q),
    0x0EFCDEA0: ("caud_0x0efcdea0", structs.decode_BIG_Q),
    0x78DF0E7F: ("caud_0x78df0e7f", structs.decode_BIG_Q),
    0x84E241ED: ("unknown_0x84e241ed", structs.decode_BIG_f),
    0xE2072799: ("unknown_0xe2072799", structs.decode_BIG_f),
    0xAB463F9A: ("rolling_splash_effect", structs.decode_BIG_Q),
    0x66D466B5: ("runoff_visor_effect", structs.decode_BIG_Q),
    0xB97CCEDE: ("runoff_ball_effect", structs.decode_BIG_Q),
    0x4D82BB1E: ("slow_exit_sound", structs.decode_BIG_Q),
    0xC51DA2DC: ("fast_exit_sound", structs.decode_BIG_Q),
    0x03D24E64: ("fast_exit_speed", structs.decode_BIG_f),
    0x687DF7A3: ("unknown_0x687df7a3", structs.decode_BIG_f),
    0xE73AAD13: ("unknown_0xe73aad13", structs.decode_BIG_f),
    0xAC67B7D7: ("unknown_0xac67b7d7", structs.decode_BIG_f),
    0xE578C0DD: ("fog_color", _decode_fog_color),
    0xB4B0FD8D: ("fog_height", structs.decode_BIG_f),
    0xB90DFF44: ("fog_bob_height", structs.decode_BIG_f),
    0xF608D35C: ("fog_bob_freq", structs.decode_BIG_f),
    0xFE3BC8F7: ("unknown_0xfe3bc8f7", structs.decode_BIG_bool_),
    0x318418AA: ("freeze_radius", structs.decode_BIG_f),
    0x7B77E31D: ("player_freeze_radius", structs.decode_BIG_f),
    0x84927794: ("caud_0x84927794", structs.decode_BIG_Q),
    0xA6E650A0: ("caud_0xa6e650a0", structs.decode_BIG_Q),
    0x90B8EB66: ("vertical_sound", structs.decode_BIG_Q),
    0x3EEDE8F7: ("damage_sound", structs.decode_BIG_Q),
    0xC110ED44: ("damage_effect", structs.decode_BIG_Q),
    0xB9413FE6: ("footstep_sound", structs.decode_BIG_Q),
    0x822118B4: ("filter_sound_effects", structs.decode_BIG_bool_),
    0xFE89B6E4: ("volume_attenuation", structs.decode_BIG_f),
    0x414379EA: ("unknown_0x414379ea", structs.decode_BIG_l),
    0x3C764739: ("fluid_lock_string", _decode_fluid_lock_string),
}
