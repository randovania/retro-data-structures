# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.LayerInfo import LayerInfo
from retro_data_structures.properties.echoes.archetypes.TriggerInfo import TriggerInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class WaterJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        trigger: json_util.JsonObject
        alpha_fadein_time: float
        alpha_fadeout_time: float
        unknown_0x4c60077e: float
        unknown_0x8518047a: float
        fluid_type: int
        light_map: int
        color_map: int
        color_warp_map: int
        gloss_map: int
        env_map: int
        env_map_size: float
        txtr: int
        foam_map: int
        alpha_map: int
        base_color: json_util.JsonValue
        alpha: float
        gloss_flat: float
        unknown_0xc63a0616: float
        unknown_0xdb7a3a6b: float
        unknown_0xb0259d23: float
        flow_color: json_util.JsonObject
        layer_info_0xe75248e4: json_util.JsonObject
        layer_info_0x385e0d43: json_util.JsonObject
        layer_info_0xd369b640: json_util.JsonObject
        layer_info_0x6ddea66d: json_util.JsonObject
        flow_speed: float
        flow_orientation: float
        underwater_fog_color: json_util.JsonValue
        splash_color: json_util.JsonValue
        splash_small: int
        splash_medium: int
        splash_big: int
        visor_runoff: int
        visor_runoff_ball: int
        sound_sound_runoff: int
        sound_sound_runoff_ball: int
        sound_splash_small: int
        sound_splash_medium: int
        sound_splash_big: int
        fog_color: json_util.JsonValue
        fog_height: float
        fog_bob_height: float
        fog_bob_freq: float
        unknown_0xd8521c1c: float
        unknown_0x7dce5dc2: float
        unknown_0x71819b3c: float
        unknown_0x9b96c630: float
        viscosity: float
        render_surface: bool
        unknown_0x3ddca674: bool
        unknown_0x0e791782: float
        unknown_0xc525c427: float
        unknown_0x3425e83f: float
        unknown_0x2293fdb0: float
        unknown_0xe9cf2e15: float
        unknown_0x268846d6: float
        unknown_0xedd49573: float
        unknown_0xc71c0d63: bool
        filter_sound_effects: bool
        unknown_0x414379ea: int


@dataclasses.dataclass()
class Water(BaseObjectType):
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
    trigger: TriggerInfo = dataclasses.field(
        default_factory=TriggerInfo,
        metadata={
            "reflection": FieldReflection[TriggerInfo](
                TriggerInfo,
                id=0x77A27411,
                original_name="Trigger",
                from_json=TriggerInfo.from_json,
                to_json=TriggerInfo.to_json,
            ),
        },
    )
    alpha_fadein_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE5EA267, original_name="AlphaFadeinTime"),
        },
    )
    alpha_fadeout_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x22B69324, original_name="AlphaFadeoutTime"),
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
    fluid_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7D606B78, original_name="FluidType"),
        },
    )
    light_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2421A2BF, original_name="LightMap"),
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
    env_map_size: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE054447, original_name="EnvMapSize"),
        },
    )
    txtr: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7A4B4685, original_name="TXTR"),
        },
    )
    foam_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5BA7702E, original_name="FoamMap"),
        },
    )
    alpha_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9A3463A7, original_name="AlphaMap"),
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
    alpha: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0F7C6FC2, original_name="Alpha"),
        },
    )
    gloss_flat: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x26382FCB, original_name="GlossFlat"),
        },
    )
    unknown_0xc63a0616: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC63A0616, original_name="Unknown"),
        },
    )
    unknown_0xdb7a3a6b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDB7A3A6B, original_name="Unknown"),
        },
    )
    unknown_0xb0259d23: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB0259D23, original_name="Unknown"),
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
    splash_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x13B56C22, original_name="SplashColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    splash_small: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3027043C, original_name="Splash_Small"),
        },
    )
    splash_medium: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x41C12BE2, original_name="Splash_Medium"),
        },
    )
    splash_big: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD6E82200, original_name="Splash_Big"),
        },
    )
    visor_runoff: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x94A23BF9, original_name="VisorRunoff"),
        },
    )
    visor_runoff_ball: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x43A704FB, original_name="VisorRunoffBall"),
        },
    )
    sound_sound_runoff: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xBA717F19, original_name="Sound_SoundRunoff"),
        },
    )
    sound_sound_runoff_ball: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xAE7C7EFC, original_name="Sound_SoundRunoffBall"),
        },
    )
    sound_splash_small: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xEEF81E4C, original_name="Sound_Splash_Small"),
        },
    )
    sound_splash_medium: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x63C96763, original_name="Sound_Splash_Medium"),
        },
    )
    sound_splash_big: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xD36209BC, original_name="Sound_Splash_Big"),
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
    unknown_0xd8521c1c: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD8521C1C, original_name="Unknown"),
        },
    )
    unknown_0x7dce5dc2: float = dataclasses.field(
        default=125.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7DCE5DC2, original_name="Unknown"),
        },
    )
    unknown_0x71819b3c: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x71819B3C, original_name="Unknown"),
        },
    )
    unknown_0x9b96c630: float = dataclasses.field(
        default=300.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9B96C630, original_name="Unknown"),
        },
    )
    viscosity: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFFE26F5C, original_name="Viscosity"),
        },
    )
    render_surface: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB5E9859F, original_name="RenderSurface"),
        },
    )
    unknown_0x3ddca674: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3DDCA674, original_name="Unknown"),
        },
    )
    unknown_0x0e791782: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0E791782, original_name="Unknown"),
        },
    )
    unknown_0xc525c427: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC525C427, original_name="Unknown"),
        },
    )
    unknown_0x3425e83f: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3425E83F, original_name="Unknown"),
        },
    )
    unknown_0x2293fdb0: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2293FDB0, original_name="Unknown"),
        },
    )
    unknown_0xe9cf2e15: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE9CF2E15, original_name="Unknown"),
        },
    )
    unknown_0x268846d6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x268846D6, original_name="Unknown"),
        },
    )
    unknown_0xedd49573: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEDD49573, original_name="Unknown"),
        },
    )
    unknown_0xc71c0d63: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC71C0D63, original_name="Unknown"),
        },
    )
    filter_sound_effects: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x822118B4, original_name="FilterSoundEffects"),
        },
    )
    unknown_0x414379ea: int = dataclasses.field(
        default=300,
        metadata={
            "reflection": FieldReflection[int](int, id=0x414379EA, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "WATR"

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
        if property_count != 62:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77A27411
        trigger = TriggerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE5EA267
        alpha_fadein_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22B69324
        alpha_fadeout_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C60077E
        unknown_0x4c60077e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8518047A
        unknown_0x8518047a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D606B78
        fluid_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2421A2BF
        light_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E8B37DD
        color_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x031D987E
        color_warp_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5AA79C9F
        gloss_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F0645CF
        env_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE054447
        env_map_size = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A4B4685
        txtr = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BA7702E
        foam_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A3463A7
        alpha_map = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041398D5
        base_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F7C6FC2
        alpha = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26382FCB
        gloss_flat = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC63A0616
        unknown_0xc63a0616 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDB7A3A6B
        unknown_0xdb7a3a6b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB0259D23
        unknown_0xb0259d23 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x244E9E6D
        flow_color = LayerInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE75248E4
        layer_info_0xe75248e4 = LayerInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385E0D43
        layer_info_0x385e0d43 = LayerInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD369B640
        layer_info_0xd369b640 = LayerInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DDEA66D
        layer_info_0x6ddea66d = LayerInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF14E3A14
        flow_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33EECDFD
        flow_orientation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5A96218C
        underwater_fog_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13B56C22
        splash_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3027043C
        splash_small = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41C12BE2
        splash_medium = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6E82200
        splash_big = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94A23BF9
        visor_runoff = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43A704FB
        visor_runoff_ball = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA717F19
        sound_sound_runoff = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE7C7EFC
        sound_sound_runoff_ball = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEEF81E4C
        sound_splash_small = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63C96763
        sound_splash_medium = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD36209BC
        sound_splash_big = structs.BIG_l.unpack(data.read(4))[0]

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
        assert property_id == 0xD8521C1C
        unknown_0xd8521c1c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7DCE5DC2
        unknown_0x7dce5dc2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71819B3C
        unknown_0x71819b3c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B96C630
        unknown_0x9b96c630 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFFE26F5C
        viscosity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5E9859F
        render_surface = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DDCA674
        unknown_0x3ddca674 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0E791782
        unknown_0x0e791782 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC525C427
        unknown_0xc525c427 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3425E83F
        unknown_0x3425e83f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2293FDB0
        unknown_0x2293fdb0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9CF2E15
        unknown_0xe9cf2e15 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x268846D6
        unknown_0x268846d6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDD49573
        unknown_0xedd49573 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC71C0D63
        unknown_0xc71c0d63 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x822118B4
        filter_sound_effects = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x414379EA
        unknown_0x414379ea = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            trigger,
            alpha_fadein_time,
            alpha_fadeout_time,
            unknown_0x4c60077e,
            unknown_0x8518047a,
            fluid_type,
            light_map,
            color_map,
            color_warp_map,
            gloss_map,
            env_map,
            env_map_size,
            txtr,
            foam_map,
            alpha_map,
            base_color,
            alpha,
            gloss_flat,
            unknown_0xc63a0616,
            unknown_0xdb7a3a6b,
            unknown_0xb0259d23,
            flow_color,
            layer_info_0xe75248e4,
            layer_info_0x385e0d43,
            layer_info_0xd369b640,
            layer_info_0x6ddea66d,
            flow_speed,
            flow_orientation,
            underwater_fog_color,
            splash_color,
            splash_small,
            splash_medium,
            splash_big,
            visor_runoff,
            visor_runoff_ball,
            sound_sound_runoff,
            sound_sound_runoff_ball,
            sound_splash_small,
            sound_splash_medium,
            sound_splash_big,
            fog_color,
            fog_height,
            fog_bob_height,
            fog_bob_freq,
            unknown_0xd8521c1c,
            unknown_0x7dce5dc2,
            unknown_0x71819b3c,
            unknown_0x9b96c630,
            viscosity,
            render_surface,
            unknown_0x3ddca674,
            unknown_0x0e791782,
            unknown_0xc525c427,
            unknown_0x3425e83f,
            unknown_0x2293fdb0,
            unknown_0xe9cf2e15,
            unknown_0x268846d6,
            unknown_0xedd49573,
            unknown_0xc71c0d63,
            filter_sound_effects,
            unknown_0x414379ea,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00>")  # 62 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\xa2t\x11")  # 0x77a27411
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.trigger.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xde^\xa2g")  # 0xde5ea267
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alpha_fadein_time))

        data.write(b'"\xb6\x93$')  # 0x22b69324
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alpha_fadeout_time))

        data.write(b"L`\x07~")  # 0x4c60077e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4c60077e))

        data.write(b"\x85\x18\x04z")  # 0x8518047a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8518047a))

        data.write(b"}`kx")  # 0x7d606b78
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.fluid_type))

        data.write(b"$!\xa2\xbf")  # 0x2421a2bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.light_map))

        data.write(b"^\x8b7\xdd")  # 0x5e8b37dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.color_map))

        data.write(b"\x03\x1d\x98~")  # 0x31d987e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.color_warp_map))

        data.write(b"Z\xa7\x9c\x9f")  # 0x5aa79c9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.gloss_map))

        data.write(b"/\x06E\xcf")  # 0x2f0645cf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.env_map))

        data.write(b"\xde\x05DG")  # 0xde054447
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.env_map_size))

        data.write(b"zKF\x85")  # 0x7a4b4685
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.txtr))

        data.write(b"[\xa7p.")  # 0x5ba7702e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.foam_map))

        data.write(b"\x9a4c\xa7")  # 0x9a3463a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.alpha_map))

        data.write(b"\x04\x13\x98\xd5")  # 0x41398d5
        data.write(b"\x00\x10")  # size
        self.base_color.to_stream(data, game)

        data.write(b"\x0f|o\xc2")  # 0xf7c6fc2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.alpha))

        data.write(b"&8/\xcb")  # 0x26382fcb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gloss_flat))

        data.write(b"\xc6:\x06\x16")  # 0xc63a0616
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc63a0616))

        data.write(b"\xdbz:k")  # 0xdb7a3a6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdb7a3a6b))

        data.write(b"\xb0%\x9d#")  # 0xb0259d23
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb0259d23))

        data.write(b"$N\x9em")  # 0x244e9e6d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flow_color.to_stream(
            data, game, default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7RH\xe4")  # 0xe75248e4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0xe75248e4.to_stream(
            data, game, default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"8^\rC")  # 0x385e0d43
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0x385e0d43.to_stream(
            data, game, default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd3i\xb6@")  # 0xd369b640
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0xd369b640.to_stream(
            data, game, default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"m\xde\xa6m")  # 0x6ddea66d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.layer_info_0x6ddea66d.to_stream(
            data, game, default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf1N:\x14")  # 0xf14e3a14
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flow_speed))

        data.write(b"3\xee\xcd\xfd")  # 0x33eecdfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flow_orientation))

        data.write(b"Z\x96!\x8c")  # 0x5a96218c
        data.write(b"\x00\x10")  # size
        self.underwater_fog_color.to_stream(data, game)

        data.write(b'\x13\xb5l"')  # 0x13b56c22
        data.write(b"\x00\x10")  # size
        self.splash_color.to_stream(data, game)

        data.write(b"0'\x04<")  # 0x3027043c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.splash_small))

        data.write(b"A\xc1+\xe2")  # 0x41c12be2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.splash_medium))

        data.write(b'\xd6\xe8"\x00')  # 0xd6e82200
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.splash_big))

        data.write(b"\x94\xa2;\xf9")  # 0x94a23bf9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.visor_runoff))

        data.write(b"C\xa7\x04\xfb")  # 0x43a704fb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.visor_runoff_ball))

        data.write(b"\xbaq\x7f\x19")  # 0xba717f19
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_sound_runoff))

        data.write(b"\xae|~\xfc")  # 0xae7c7efc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_sound_runoff_ball))

        data.write(b"\xee\xf8\x1eL")  # 0xeef81e4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_splash_small))

        data.write(b"c\xc9gc")  # 0x63c96763
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_splash_medium))

        data.write(b"\xd3b\t\xbc")  # 0xd36209bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_splash_big))

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

        data.write(b"\xd8R\x1c\x1c")  # 0xd8521c1c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd8521c1c))

        data.write(b"}\xce]\xc2")  # 0x7dce5dc2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7dce5dc2))

        data.write(b"q\x81\x9b<")  # 0x71819b3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x71819b3c))

        data.write(b"\x9b\x96\xc60")  # 0x9b96c630
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9b96c630))

        data.write(b"\xff\xe2o\\")  # 0xffe26f5c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.viscosity))

        data.write(b"\xb5\xe9\x85\x9f")  # 0xb5e9859f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.render_surface))

        data.write(b"=\xdc\xa6t")  # 0x3ddca674
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3ddca674))

        data.write(b"\x0ey\x17\x82")  # 0xe791782
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0e791782))

        data.write(b"\xc5%\xc4'")  # 0xc525c427
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc525c427))

        data.write(b"4%\xe8?")  # 0x3425e83f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3425e83f))

        data.write(b'"\x93\xfd\xb0')  # 0x2293fdb0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2293fdb0))

        data.write(b"\xe9\xcf.\x15")  # 0xe9cf2e15
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe9cf2e15))

        data.write(b"&\x88F\xd6")  # 0x268846d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x268846d6))

        data.write(b"\xed\xd4\x95s")  # 0xedd49573
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xedd49573))

        data.write(b"\xc7\x1c\rc")  # 0xc71c0d63
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xc71c0d63))

        data.write(b"\x82!\x18\xb4")  # 0x822118b4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.filter_sound_effects))

        data.write(b"ACy\xea")  # 0x414379ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x414379ea))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WaterJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            trigger=TriggerInfo.from_json(json_data["trigger"]),
            alpha_fadein_time=json_data["alpha_fadein_time"],
            alpha_fadeout_time=json_data["alpha_fadeout_time"],
            unknown_0x4c60077e=json_data["unknown_0x4c60077e"],
            unknown_0x8518047a=json_data["unknown_0x8518047a"],
            fluid_type=json_data["fluid_type"],
            light_map=json_data["light_map"],
            color_map=json_data["color_map"],
            color_warp_map=json_data["color_warp_map"],
            gloss_map=json_data["gloss_map"],
            env_map=json_data["env_map"],
            env_map_size=json_data["env_map_size"],
            txtr=json_data["txtr"],
            foam_map=json_data["foam_map"],
            alpha_map=json_data["alpha_map"],
            base_color=Color.from_json(json_data["base_color"]),
            alpha=json_data["alpha"],
            gloss_flat=json_data["gloss_flat"],
            unknown_0xc63a0616=json_data["unknown_0xc63a0616"],
            unknown_0xdb7a3a6b=json_data["unknown_0xdb7a3a6b"],
            unknown_0xb0259d23=json_data["unknown_0xb0259d23"],
            flow_color=LayerInfo.from_json(json_data["flow_color"]),
            layer_info_0xe75248e4=LayerInfo.from_json(json_data["layer_info_0xe75248e4"]),
            layer_info_0x385e0d43=LayerInfo.from_json(json_data["layer_info_0x385e0d43"]),
            layer_info_0xd369b640=LayerInfo.from_json(json_data["layer_info_0xd369b640"]),
            layer_info_0x6ddea66d=LayerInfo.from_json(json_data["layer_info_0x6ddea66d"]),
            flow_speed=json_data["flow_speed"],
            flow_orientation=json_data["flow_orientation"],
            underwater_fog_color=Color.from_json(json_data["underwater_fog_color"]),
            splash_color=Color.from_json(json_data["splash_color"]),
            splash_small=json_data["splash_small"],
            splash_medium=json_data["splash_medium"],
            splash_big=json_data["splash_big"],
            visor_runoff=json_data["visor_runoff"],
            visor_runoff_ball=json_data["visor_runoff_ball"],
            sound_sound_runoff=json_data["sound_sound_runoff"],
            sound_sound_runoff_ball=json_data["sound_sound_runoff_ball"],
            sound_splash_small=json_data["sound_splash_small"],
            sound_splash_medium=json_data["sound_splash_medium"],
            sound_splash_big=json_data["sound_splash_big"],
            fog_color=Color.from_json(json_data["fog_color"]),
            fog_height=json_data["fog_height"],
            fog_bob_height=json_data["fog_bob_height"],
            fog_bob_freq=json_data["fog_bob_freq"],
            unknown_0xd8521c1c=json_data["unknown_0xd8521c1c"],
            unknown_0x7dce5dc2=json_data["unknown_0x7dce5dc2"],
            unknown_0x71819b3c=json_data["unknown_0x71819b3c"],
            unknown_0x9b96c630=json_data["unknown_0x9b96c630"],
            viscosity=json_data["viscosity"],
            render_surface=json_data["render_surface"],
            unknown_0x3ddca674=json_data["unknown_0x3ddca674"],
            unknown_0x0e791782=json_data["unknown_0x0e791782"],
            unknown_0xc525c427=json_data["unknown_0xc525c427"],
            unknown_0x3425e83f=json_data["unknown_0x3425e83f"],
            unknown_0x2293fdb0=json_data["unknown_0x2293fdb0"],
            unknown_0xe9cf2e15=json_data["unknown_0xe9cf2e15"],
            unknown_0x268846d6=json_data["unknown_0x268846d6"],
            unknown_0xedd49573=json_data["unknown_0xedd49573"],
            unknown_0xc71c0d63=json_data["unknown_0xc71c0d63"],
            filter_sound_effects=json_data["filter_sound_effects"],
            unknown_0x414379ea=json_data["unknown_0x414379ea"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "trigger": self.trigger.to_json(),
            "alpha_fadein_time": self.alpha_fadein_time,
            "alpha_fadeout_time": self.alpha_fadeout_time,
            "unknown_0x4c60077e": self.unknown_0x4c60077e,
            "unknown_0x8518047a": self.unknown_0x8518047a,
            "fluid_type": self.fluid_type,
            "light_map": self.light_map,
            "color_map": self.color_map,
            "color_warp_map": self.color_warp_map,
            "gloss_map": self.gloss_map,
            "env_map": self.env_map,
            "env_map_size": self.env_map_size,
            "txtr": self.txtr,
            "foam_map": self.foam_map,
            "alpha_map": self.alpha_map,
            "base_color": self.base_color.to_json(),
            "alpha": self.alpha,
            "gloss_flat": self.gloss_flat,
            "unknown_0xc63a0616": self.unknown_0xc63a0616,
            "unknown_0xdb7a3a6b": self.unknown_0xdb7a3a6b,
            "unknown_0xb0259d23": self.unknown_0xb0259d23,
            "flow_color": self.flow_color.to_json(),
            "layer_info_0xe75248e4": self.layer_info_0xe75248e4.to_json(),
            "layer_info_0x385e0d43": self.layer_info_0x385e0d43.to_json(),
            "layer_info_0xd369b640": self.layer_info_0xd369b640.to_json(),
            "layer_info_0x6ddea66d": self.layer_info_0x6ddea66d.to_json(),
            "flow_speed": self.flow_speed,
            "flow_orientation": self.flow_orientation,
            "underwater_fog_color": self.underwater_fog_color.to_json(),
            "splash_color": self.splash_color.to_json(),
            "splash_small": self.splash_small,
            "splash_medium": self.splash_medium,
            "splash_big": self.splash_big,
            "visor_runoff": self.visor_runoff,
            "visor_runoff_ball": self.visor_runoff_ball,
            "sound_sound_runoff": self.sound_sound_runoff,
            "sound_sound_runoff_ball": self.sound_sound_runoff_ball,
            "sound_splash_small": self.sound_splash_small,
            "sound_splash_medium": self.sound_splash_medium,
            "sound_splash_big": self.sound_splash_big,
            "fog_color": self.fog_color.to_json(),
            "fog_height": self.fog_height,
            "fog_bob_height": self.fog_bob_height,
            "fog_bob_freq": self.fog_bob_freq,
            "unknown_0xd8521c1c": self.unknown_0xd8521c1c,
            "unknown_0x7dce5dc2": self.unknown_0x7dce5dc2,
            "unknown_0x71819b3c": self.unknown_0x71819b3c,
            "unknown_0x9b96c630": self.unknown_0x9b96c630,
            "viscosity": self.viscosity,
            "render_surface": self.render_surface,
            "unknown_0x3ddca674": self.unknown_0x3ddca674,
            "unknown_0x0e791782": self.unknown_0x0e791782,
            "unknown_0xc525c427": self.unknown_0xc525c427,
            "unknown_0x3425e83f": self.unknown_0x3425e83f,
            "unknown_0x2293fdb0": self.unknown_0x2293fdb0,
            "unknown_0xe9cf2e15": self.unknown_0xe9cf2e15,
            "unknown_0x268846d6": self.unknown_0x268846d6,
            "unknown_0xedd49573": self.unknown_0xedd49573,
            "unknown_0xc71c0d63": self.unknown_0xc71c0d63,
            "filter_sound_effects": self.filter_sound_effects,
            "unknown_0x414379ea": self.unknown_0x414379ea,
        }

    def _dependencies_for_light_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.light_map)

    def _dependencies_for_color_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_map)

    def _dependencies_for_color_warp_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_warp_map)

    def _dependencies_for_gloss_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.gloss_map)

    def _dependencies_for_env_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.env_map)

    def _dependencies_for_txtr(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.txtr)

    def _dependencies_for_foam_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.foam_map)

    def _dependencies_for_alpha_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.alpha_map)

    def _dependencies_for_splash_small(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_small)

    def _dependencies_for_splash_medium(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_medium)

    def _dependencies_for_splash_big(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_big)

    def _dependencies_for_visor_runoff(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_runoff)

    def _dependencies_for_visor_runoff_ball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_runoff_ball)

    def _dependencies_for_sound_sound_runoff(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_sound_runoff)

    def _dependencies_for_sound_sound_runoff_ball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_sound_runoff_ball)

    def _dependencies_for_sound_splash_small(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_splash_small)

    def _dependencies_for_sound_splash_medium(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_splash_medium)

    def _dependencies_for_sound_splash_big(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_splash_big)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_light_map, "light_map", "AssetId"),
            (self._dependencies_for_color_map, "color_map", "AssetId"),
            (self._dependencies_for_color_warp_map, "color_warp_map", "AssetId"),
            (self._dependencies_for_gloss_map, "gloss_map", "AssetId"),
            (self._dependencies_for_env_map, "env_map", "AssetId"),
            (self._dependencies_for_txtr, "txtr", "AssetId"),
            (self._dependencies_for_foam_map, "foam_map", "AssetId"),
            (self._dependencies_for_alpha_map, "alpha_map", "AssetId"),
            (self._dependencies_for_splash_small, "splash_small", "AssetId"),
            (self._dependencies_for_splash_medium, "splash_medium", "AssetId"),
            (self._dependencies_for_splash_big, "splash_big", "AssetId"),
            (self._dependencies_for_visor_runoff, "visor_runoff", "AssetId"),
            (self._dependencies_for_visor_runoff_ball, "visor_runoff_ball", "AssetId"),
            (self._dependencies_for_sound_sound_runoff, "sound_sound_runoff", "int"),
            (self._dependencies_for_sound_sound_runoff_ball, "sound_sound_runoff_ball", "int"),
            (self._dependencies_for_sound_splash_small, "sound_splash_small", "int"),
            (self._dependencies_for_sound_splash_medium, "sound_splash_medium", "int"),
            (self._dependencies_for_sound_splash_big, "sound_splash_big", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Water.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_trigger(data: typing.BinaryIO, game: Game, property_size: int) -> TriggerInfo:
    return TriggerInfo.from_stream(data, game, property_size)


def _decode_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flow_color(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
    )


def _decode_layer_info_0xe75248e4(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
    )


def _decode_layer_info_0x385e0d43(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
    )


def _decode_layer_info_0xd369b640(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
    )


def _decode_layer_info_0x6ddea66d(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"motion_type": 0, "amplitude": 0.15000000596046448, "texture_scale": 10.0},
    )


def _decode_underwater_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_splash_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x77A27411: ("trigger", _decode_trigger),
    0xDE5EA267: ("alpha_fadein_time", structs.decode_BIG_f),
    0x22B69324: ("alpha_fadeout_time", structs.decode_BIG_f),
    0x4C60077E: ("unknown_0x4c60077e", structs.decode_BIG_f),
    0x8518047A: ("unknown_0x8518047a", structs.decode_BIG_f),
    0x7D606B78: ("fluid_type", structs.decode_BIG_l),
    0x2421A2BF: ("light_map", structs.decode_BIG_L),
    0x5E8B37DD: ("color_map", structs.decode_BIG_L),
    0x031D987E: ("color_warp_map", structs.decode_BIG_L),
    0x5AA79C9F: ("gloss_map", structs.decode_BIG_L),
    0x2F0645CF: ("env_map", structs.decode_BIG_L),
    0xDE054447: ("env_map_size", structs.decode_BIG_f),
    0x7A4B4685: ("txtr", structs.decode_BIG_L),
    0x5BA7702E: ("foam_map", structs.decode_BIG_L),
    0x9A3463A7: ("alpha_map", structs.decode_BIG_L),
    0x041398D5: ("base_color", _decode_base_color),
    0x0F7C6FC2: ("alpha", structs.decode_BIG_f),
    0x26382FCB: ("gloss_flat", structs.decode_BIG_f),
    0xC63A0616: ("unknown_0xc63a0616", structs.decode_BIG_f),
    0xDB7A3A6B: ("unknown_0xdb7a3a6b", structs.decode_BIG_f),
    0xB0259D23: ("unknown_0xb0259d23", structs.decode_BIG_f),
    0x244E9E6D: ("flow_color", _decode_flow_color),
    0xE75248E4: ("layer_info_0xe75248e4", _decode_layer_info_0xe75248e4),
    0x385E0D43: ("layer_info_0x385e0d43", _decode_layer_info_0x385e0d43),
    0xD369B640: ("layer_info_0xd369b640", _decode_layer_info_0xd369b640),
    0x6DDEA66D: ("layer_info_0x6ddea66d", _decode_layer_info_0x6ddea66d),
    0xF14E3A14: ("flow_speed", structs.decode_BIG_f),
    0x33EECDFD: ("flow_orientation", structs.decode_BIG_f),
    0x5A96218C: ("underwater_fog_color", _decode_underwater_fog_color),
    0x13B56C22: ("splash_color", _decode_splash_color),
    0x3027043C: ("splash_small", structs.decode_BIG_L),
    0x41C12BE2: ("splash_medium", structs.decode_BIG_L),
    0xD6E82200: ("splash_big", structs.decode_BIG_L),
    0x94A23BF9: ("visor_runoff", structs.decode_BIG_L),
    0x43A704FB: ("visor_runoff_ball", structs.decode_BIG_L),
    0xBA717F19: ("sound_sound_runoff", structs.decode_BIG_l),
    0xAE7C7EFC: ("sound_sound_runoff_ball", structs.decode_BIG_l),
    0xEEF81E4C: ("sound_splash_small", structs.decode_BIG_l),
    0x63C96763: ("sound_splash_medium", structs.decode_BIG_l),
    0xD36209BC: ("sound_splash_big", structs.decode_BIG_l),
    0xE578C0DD: ("fog_color", _decode_fog_color),
    0xB4B0FD8D: ("fog_height", structs.decode_BIG_f),
    0xB90DFF44: ("fog_bob_height", structs.decode_BIG_f),
    0xF608D35C: ("fog_bob_freq", structs.decode_BIG_f),
    0xD8521C1C: ("unknown_0xd8521c1c", structs.decode_BIG_f),
    0x7DCE5DC2: ("unknown_0x7dce5dc2", structs.decode_BIG_f),
    0x71819B3C: ("unknown_0x71819b3c", structs.decode_BIG_f),
    0x9B96C630: ("unknown_0x9b96c630", structs.decode_BIG_f),
    0xFFE26F5C: ("viscosity", structs.decode_BIG_f),
    0xB5E9859F: ("render_surface", structs.decode_BIG_bool_),
    0x3DDCA674: ("unknown_0x3ddca674", structs.decode_BIG_bool_),
    0x0E791782: ("unknown_0x0e791782", structs.decode_BIG_f),
    0xC525C427: ("unknown_0xc525c427", structs.decode_BIG_f),
    0x3425E83F: ("unknown_0x3425e83f", structs.decode_BIG_f),
    0x2293FDB0: ("unknown_0x2293fdb0", structs.decode_BIG_f),
    0xE9CF2E15: ("unknown_0xe9cf2e15", structs.decode_BIG_f),
    0x268846D6: ("unknown_0x268846d6", structs.decode_BIG_f),
    0xEDD49573: ("unknown_0xedd49573", structs.decode_BIG_f),
    0xC71C0D63: ("unknown_0xc71c0d63", structs.decode_BIG_bool_),
    0x822118B4: ("filter_sound_effects", structs.decode_BIG_bool_),
    0x414379EA: ("unknown_0x414379ea", structs.decode_BIG_l),
}
