# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.FluidUVMotion import FluidUVMotion
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class WaterJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000003: json_util.JsonObject
        force: json_util.JsonValue
        flags: int
        thermal_cold: bool
        display_surface: bool
        pattern_map1: int
        pattern_map2: int
        color_map: int
        bump_map: int
        env_map: int
        env_bump_map: int
        bump_light_dir: json_util.JsonValue
        bump_scale: float
        morph_in_time: float
        morph_out_time: float
        active: bool
        fluid_type: int
        unknown: bool
        alpha: float
        unnamed_0x00000016: json_util.JsonObject
        turb_speed: float
        turb_distance: float
        turb_frequence_max: float
        turb_frequence_min: float
        turb_phase_max: float
        turb_phase_min: float
        turb_amplitude_max: float
        turb_amplitude_min: float
        splash_color: json_util.JsonValue
        inside_fog_color: json_util.JsonValue
        splash_particle1: int
        splash_particle2: int
        splash_particle3: int
        visor_runoff_particle: int
        unmorph_visor_runoff_particle: int
        visor_runoff_sound: int
        unmorph_visor_runoff_sound: int
        splash_sfx1: int
        splash_sfx2: int
        splash_sfx3: int
        tile_size: float
        tile_subdivisions: int
        specular_min: float
        specular_max: float
        reflection_size: float
        ripple_intensity: float
        reflection_blend: float
        fog_bias: float
        fog_magnitude: float
        fog_speed: float
        fog_color: json_util.JsonValue
        lightmap: int
        units_per_lightmap_texel: float
        alpha_in_time: float
        alpha_out_time: float
        alpha_in_recip: int
        alpha_out_recip: int
        unknown_will_crash_if_on: bool
        ignore_0x0000003d: int
        ignore_0x0000003e: int


class Flags(enum.IntFlag):
    PendingAmbush = 1
    CeilingAmbush = 2
    NonAggressive = 4
    Melee = 8
    NoShuffleCloseCheck = 16
    OnlyAttackInRange = 32
    Unknown = 64
    NoKnockbackImpulseReset = 128
    NoMeleeAttack = 512
    BreakAttack = 1024
    Seated = 4096
    ShadowPirate = 8192
    AlertBeforeCloak = 16384
    NoBreakDamage = 32768
    FloatingCorpse = 65536
    RagdollNoAiCollision = 131072
    Trooper = 262144

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


class FluidType(enum.IntEnum):
    NormalWater = 0
    PoisonWater = 1
    Lava = 2
    PhazonFluid = 3
    Four = 4
    ThickLava = 5

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
class Water(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000001, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    scale: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Scale", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unnamed_0x00000003: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo, id=0x00000003, original_name="3", from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
            ),
        },
    )
    force: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000004, original_name="Force", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    flags: Flags = dataclasses.field(
        default=Flags(0),
        metadata={
            "reflection": FieldReflection[Flags](
                Flags, id=0x00000005, original_name="Flags", from_json=Flags.from_json, to_json=Flags.to_json
            ),
        },
    )
    thermal_cold: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="ThermalCold"),
        },
    )
    display_surface: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000007, original_name="DisplaySurface"),
        },
    )
    pattern_map1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000008, original_name="PatternMap1"),
        },
    )
    pattern_map2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000009, original_name="PatternMap2"),
        },
    )
    color_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000A, original_name="ColorMap"),
        },
    )
    bump_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000B, original_name="BumpMap"),
        },
    )
    env_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000C, original_name="EnvMap"),
        },
    )
    env_bump_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0000000D, original_name="EnvBumpMap"),
        },
    )
    bump_light_dir: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x0000000E, original_name="BumpLightDir", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    bump_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000F, original_name="BumpScale"),
        },
    )
    morph_in_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000010, original_name="MorphInTime"),
        },
    )
    morph_out_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="MorphOutTime"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000012, original_name="Active"),
        },
    )
    fluid_type: FluidType = dataclasses.field(
        default=FluidType.NormalWater,
        metadata={
            "reflection": FieldReflection[FluidType](
                FluidType,
                id=0x00000013,
                original_name="FluidType",
                from_json=FluidType.from_json,
                to_json=FluidType.to_json,
            ),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000014, original_name="Unknown"),
        },
    )
    alpha: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="Alpha"),
        },
    )
    unnamed_0x00000016: FluidUVMotion = dataclasses.field(
        default_factory=FluidUVMotion,
        metadata={
            "reflection": FieldReflection[FluidUVMotion](
                FluidUVMotion,
                id=0x00000016,
                original_name="22",
                from_json=FluidUVMotion.from_json,
                to_json=FluidUVMotion.to_json,
            ),
        },
    )
    turb_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000017, original_name="TurbSpeed"),
        },
    )
    turb_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000018, original_name="TurbDistance"),
        },
    )
    turb_frequence_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000019, original_name="TurbFrequenceMax"),
        },
    )
    turb_frequence_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001A, original_name="TurbFrequenceMin"),
        },
    )
    turb_phase_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001B, original_name="TurbPhaseMax"),
        },
    )
    turb_phase_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001C, original_name="TurbPhaseMin"),
        },
    )
    turb_amplitude_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001D, original_name="TurbAmplitudeMax"),
        },
    )
    turb_amplitude_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000001E, original_name="TurbAmplitudeMin"),
        },
    )
    splash_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x0000001F, original_name="SplashColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    inside_fog_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000020, original_name="InsideFogColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    splash_particle1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000021, original_name="SplashParticle1"),
        },
    )
    splash_particle2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000022, original_name="SplashParticle2"),
        },
    )
    splash_particle3: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000023, original_name="SplashParticle3"),
        },
    )
    visor_runoff_particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000024, original_name="VisorRunoffParticle"),
        },
    )
    unmorph_visor_runoff_particle: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000025, original_name="UnmorphVisorRunoffParticle"),
        },
    )
    visor_runoff_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000026, original_name="Visor Runoff Sound"),
        },
    )
    unmorph_visor_runoff_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000027, original_name="Unmorph Visor Runoff Sound"),
        },
    )
    splash_sfx1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000028, original_name="SplashSFX1"),
        },
    )
    splash_sfx2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x00000029, original_name="SplashSFX2"),
        },
    )
    splash_sfx3: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000002A, original_name="SplashSFX3"),
        },
    )
    tile_size: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002B, original_name="TileSize"),
        },
    )
    tile_subdivisions: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000002C, original_name="TileSubdivisions"),
        },
    )
    specular_min: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002D, original_name="SpecularMin"),
        },
    )
    specular_max: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002E, original_name="SpecularMax"),
        },
    )
    reflection_size: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000002F, original_name="ReflectionSize"),
        },
    )
    ripple_intensity: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000030, original_name="RippleIntensity"),
        },
    )
    reflection_blend: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000031, original_name="ReflectionBlend"),
        },
    )
    fog_bias: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000032, original_name="FogBias"),
        },
    )
    fog_magnitude: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000033, original_name="FogMagnitude"),
        },
    )
    fog_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000034, original_name="FogSpeed"),
        },
    )
    fog_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000035, original_name="FogColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    lightmap: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00000036, original_name="Lightmap"),
        },
    )
    units_per_lightmap_texel: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000037, original_name="UnitsPerLightmapTexel"),
        },
    )
    alpha_in_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000038, original_name="AlphaInTime"),
        },
    )
    alpha_out_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000039, original_name="AlphaOutTime"),
        },
    )
    alpha_in_recip: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000003A, original_name="AlphaInRecip"),
        },
    )
    alpha_out_recip: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000003B, original_name="AlphaOutRecip"),
        },
    )
    unknown_will_crash_if_on: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000003C, original_name="Unknown (Will Crash if On)"),
        },
    )
    ignore_0x0000003d: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000003D, original_name="Ignore"),
        },
    )
    ignore_0x0000003e: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000003E, original_name="Ignore"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x20

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000003 = DamageInfo.from_stream(data, game, property_size)
        force = Vector.from_stream(data, game, property_size)
        flags = Flags.from_stream(data, game)
        thermal_cold = structs.BIG_bool_.unpack(data.read(1))[0]
        display_surface = structs.BIG_bool_.unpack(data.read(1))[0]
        pattern_map1 = structs.BIG_L.unpack(data.read(4))[0]
        pattern_map2 = structs.BIG_L.unpack(data.read(4))[0]
        color_map = structs.BIG_L.unpack(data.read(4))[0]
        bump_map = structs.BIG_L.unpack(data.read(4))[0]
        env_map = structs.BIG_L.unpack(data.read(4))[0]
        env_bump_map = structs.BIG_L.unpack(data.read(4))[0]
        bump_light_dir = Vector.from_stream(data, game, property_size)
        bump_scale = structs.BIG_f.unpack(data.read(4))[0]
        morph_in_time = structs.BIG_f.unpack(data.read(4))[0]
        morph_out_time = structs.BIG_f.unpack(data.read(4))[0]
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        fluid_type = FluidType.from_stream(data, game)
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
        alpha = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000016 = FluidUVMotion.from_stream(data, game, property_size)
        turb_speed = structs.BIG_f.unpack(data.read(4))[0]
        turb_distance = structs.BIG_f.unpack(data.read(4))[0]
        turb_frequence_max = structs.BIG_f.unpack(data.read(4))[0]
        turb_frequence_min = structs.BIG_f.unpack(data.read(4))[0]
        turb_phase_max = structs.BIG_f.unpack(data.read(4))[0]
        turb_phase_min = structs.BIG_f.unpack(data.read(4))[0]
        turb_amplitude_max = structs.BIG_f.unpack(data.read(4))[0]
        turb_amplitude_min = structs.BIG_f.unpack(data.read(4))[0]
        splash_color = Color.from_stream(data, game, property_size)
        inside_fog_color = Color.from_stream(data, game, property_size)
        splash_particle1 = structs.BIG_L.unpack(data.read(4))[0]
        splash_particle2 = structs.BIG_L.unpack(data.read(4))[0]
        splash_particle3 = structs.BIG_L.unpack(data.read(4))[0]
        visor_runoff_particle = structs.BIG_L.unpack(data.read(4))[0]
        unmorph_visor_runoff_particle = structs.BIG_L.unpack(data.read(4))[0]
        visor_runoff_sound = structs.BIG_l.unpack(data.read(4))[0]
        unmorph_visor_runoff_sound = structs.BIG_l.unpack(data.read(4))[0]
        splash_sfx1 = structs.BIG_l.unpack(data.read(4))[0]
        splash_sfx2 = structs.BIG_l.unpack(data.read(4))[0]
        splash_sfx3 = structs.BIG_l.unpack(data.read(4))[0]
        tile_size = structs.BIG_f.unpack(data.read(4))[0]
        tile_subdivisions = structs.BIG_l.unpack(data.read(4))[0]
        specular_min = structs.BIG_f.unpack(data.read(4))[0]
        specular_max = structs.BIG_f.unpack(data.read(4))[0]
        reflection_size = structs.BIG_f.unpack(data.read(4))[0]
        ripple_intensity = structs.BIG_f.unpack(data.read(4))[0]
        reflection_blend = structs.BIG_f.unpack(data.read(4))[0]
        fog_bias = structs.BIG_f.unpack(data.read(4))[0]
        fog_magnitude = structs.BIG_f.unpack(data.read(4))[0]
        fog_speed = structs.BIG_f.unpack(data.read(4))[0]
        fog_color = Color.from_stream(data, game, property_size)
        lightmap = structs.BIG_L.unpack(data.read(4))[0]
        units_per_lightmap_texel = structs.BIG_f.unpack(data.read(4))[0]
        alpha_in_time = structs.BIG_f.unpack(data.read(4))[0]
        alpha_out_time = structs.BIG_f.unpack(data.read(4))[0]
        alpha_in_recip = structs.BIG_l.unpack(data.read(4))[0]
        alpha_out_recip = structs.BIG_l.unpack(data.read(4))[0]
        unknown_will_crash_if_on = structs.BIG_bool_.unpack(data.read(1))[0]
        ignore_0x0000003d = structs.BIG_h.unpack(data.read(2))[0]
        ignore_0x0000003e = structs.BIG_h.unpack(data.read(2))[0]
        return cls(
            name,
            position,
            scale,
            unnamed_0x00000003,
            force,
            flags,
            thermal_cold,
            display_surface,
            pattern_map1,
            pattern_map2,
            color_map,
            bump_map,
            env_map,
            env_bump_map,
            bump_light_dir,
            bump_scale,
            morph_in_time,
            morph_out_time,
            active,
            fluid_type,
            unknown,
            alpha,
            unnamed_0x00000016,
            turb_speed,
            turb_distance,
            turb_frequence_max,
            turb_frequence_min,
            turb_phase_max,
            turb_phase_min,
            turb_amplitude_max,
            turb_amplitude_min,
            splash_color,
            inside_fog_color,
            splash_particle1,
            splash_particle2,
            splash_particle3,
            visor_runoff_particle,
            unmorph_visor_runoff_particle,
            visor_runoff_sound,
            unmorph_visor_runoff_sound,
            splash_sfx1,
            splash_sfx2,
            splash_sfx3,
            tile_size,
            tile_subdivisions,
            specular_min,
            specular_max,
            reflection_size,
            ripple_intensity,
            reflection_blend,
            fog_bias,
            fog_magnitude,
            fog_speed,
            fog_color,
            lightmap,
            units_per_lightmap_texel,
            alpha_in_time,
            alpha_out_time,
            alpha_in_recip,
            alpha_out_recip,
            unknown_will_crash_if_on,
            ignore_0x0000003d,
            ignore_0x0000003e,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00?")  # 63 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000003.to_stream(data, game)
        self.force.to_stream(data, game)
        self.flags.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.thermal_cold))
        data.write(structs.BIG_bool_.pack(self.display_surface))
        data.write(structs.BIG_L.pack(self.pattern_map1))
        data.write(structs.BIG_L.pack(self.pattern_map2))
        data.write(structs.BIG_L.pack(self.color_map))
        data.write(structs.BIG_L.pack(self.bump_map))
        data.write(structs.BIG_L.pack(self.env_map))
        data.write(structs.BIG_L.pack(self.env_bump_map))
        self.bump_light_dir.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.bump_scale))
        data.write(structs.BIG_f.pack(self.morph_in_time))
        data.write(structs.BIG_f.pack(self.morph_out_time))
        data.write(structs.BIG_bool_.pack(self.active))
        self.fluid_type.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.unknown))
        data.write(structs.BIG_f.pack(self.alpha))
        self.unnamed_0x00000016.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.turb_speed))
        data.write(structs.BIG_f.pack(self.turb_distance))
        data.write(structs.BIG_f.pack(self.turb_frequence_max))
        data.write(structs.BIG_f.pack(self.turb_frequence_min))
        data.write(structs.BIG_f.pack(self.turb_phase_max))
        data.write(structs.BIG_f.pack(self.turb_phase_min))
        data.write(structs.BIG_f.pack(self.turb_amplitude_max))
        data.write(structs.BIG_f.pack(self.turb_amplitude_min))
        self.splash_color.to_stream(data, game)
        self.inside_fog_color.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.splash_particle1))
        data.write(structs.BIG_L.pack(self.splash_particle2))
        data.write(structs.BIG_L.pack(self.splash_particle3))
        data.write(structs.BIG_L.pack(self.visor_runoff_particle))
        data.write(structs.BIG_L.pack(self.unmorph_visor_runoff_particle))
        data.write(structs.BIG_l.pack(self.visor_runoff_sound))
        data.write(structs.BIG_l.pack(self.unmorph_visor_runoff_sound))
        data.write(structs.BIG_l.pack(self.splash_sfx1))
        data.write(structs.BIG_l.pack(self.splash_sfx2))
        data.write(structs.BIG_l.pack(self.splash_sfx3))
        data.write(structs.BIG_f.pack(self.tile_size))
        data.write(structs.BIG_l.pack(self.tile_subdivisions))
        data.write(structs.BIG_f.pack(self.specular_min))
        data.write(structs.BIG_f.pack(self.specular_max))
        data.write(structs.BIG_f.pack(self.reflection_size))
        data.write(structs.BIG_f.pack(self.ripple_intensity))
        data.write(structs.BIG_f.pack(self.reflection_blend))
        data.write(structs.BIG_f.pack(self.fog_bias))
        data.write(structs.BIG_f.pack(self.fog_magnitude))
        data.write(structs.BIG_f.pack(self.fog_speed))
        self.fog_color.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.lightmap))
        data.write(structs.BIG_f.pack(self.units_per_lightmap_texel))
        data.write(structs.BIG_f.pack(self.alpha_in_time))
        data.write(structs.BIG_f.pack(self.alpha_out_time))
        data.write(structs.BIG_l.pack(self.alpha_in_recip))
        data.write(structs.BIG_l.pack(self.alpha_out_recip))
        data.write(structs.BIG_bool_.pack(self.unknown_will_crash_if_on))
        data.write(structs.BIG_h.pack(self.ignore_0x0000003d))
        data.write(structs.BIG_h.pack(self.ignore_0x0000003e))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WaterJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            scale=Vector.from_json(json_data["scale"]),
            unnamed_0x00000003=DamageInfo.from_json(json_data["unnamed_0x00000003"]),
            force=Vector.from_json(json_data["force"]),
            flags=Flags.from_json(json_data["flags"]),
            thermal_cold=json_data["thermal_cold"],
            display_surface=json_data["display_surface"],
            pattern_map1=json_data["pattern_map1"],
            pattern_map2=json_data["pattern_map2"],
            color_map=json_data["color_map"],
            bump_map=json_data["bump_map"],
            env_map=json_data["env_map"],
            env_bump_map=json_data["env_bump_map"],
            bump_light_dir=Vector.from_json(json_data["bump_light_dir"]),
            bump_scale=json_data["bump_scale"],
            morph_in_time=json_data["morph_in_time"],
            morph_out_time=json_data["morph_out_time"],
            active=json_data["active"],
            fluid_type=FluidType.from_json(json_data["fluid_type"]),
            unknown=json_data["unknown"],
            alpha=json_data["alpha"],
            unnamed_0x00000016=FluidUVMotion.from_json(json_data["unnamed_0x00000016"]),
            turb_speed=json_data["turb_speed"],
            turb_distance=json_data["turb_distance"],
            turb_frequence_max=json_data["turb_frequence_max"],
            turb_frequence_min=json_data["turb_frequence_min"],
            turb_phase_max=json_data["turb_phase_max"],
            turb_phase_min=json_data["turb_phase_min"],
            turb_amplitude_max=json_data["turb_amplitude_max"],
            turb_amplitude_min=json_data["turb_amplitude_min"],
            splash_color=Color.from_json(json_data["splash_color"]),
            inside_fog_color=Color.from_json(json_data["inside_fog_color"]),
            splash_particle1=json_data["splash_particle1"],
            splash_particle2=json_data["splash_particle2"],
            splash_particle3=json_data["splash_particle3"],
            visor_runoff_particle=json_data["visor_runoff_particle"],
            unmorph_visor_runoff_particle=json_data["unmorph_visor_runoff_particle"],
            visor_runoff_sound=json_data["visor_runoff_sound"],
            unmorph_visor_runoff_sound=json_data["unmorph_visor_runoff_sound"],
            splash_sfx1=json_data["splash_sfx1"],
            splash_sfx2=json_data["splash_sfx2"],
            splash_sfx3=json_data["splash_sfx3"],
            tile_size=json_data["tile_size"],
            tile_subdivisions=json_data["tile_subdivisions"],
            specular_min=json_data["specular_min"],
            specular_max=json_data["specular_max"],
            reflection_size=json_data["reflection_size"],
            ripple_intensity=json_data["ripple_intensity"],
            reflection_blend=json_data["reflection_blend"],
            fog_bias=json_data["fog_bias"],
            fog_magnitude=json_data["fog_magnitude"],
            fog_speed=json_data["fog_speed"],
            fog_color=Color.from_json(json_data["fog_color"]),
            lightmap=json_data["lightmap"],
            units_per_lightmap_texel=json_data["units_per_lightmap_texel"],
            alpha_in_time=json_data["alpha_in_time"],
            alpha_out_time=json_data["alpha_out_time"],
            alpha_in_recip=json_data["alpha_in_recip"],
            alpha_out_recip=json_data["alpha_out_recip"],
            unknown_will_crash_if_on=json_data["unknown_will_crash_if_on"],
            ignore_0x0000003d=json_data["ignore_0x0000003d"],
            ignore_0x0000003e=json_data["ignore_0x0000003e"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "scale": self.scale.to_json(),
            "unnamed_0x00000003": self.unnamed_0x00000003.to_json(),
            "force": self.force.to_json(),
            "flags": self.flags.to_json(),
            "thermal_cold": self.thermal_cold,
            "display_surface": self.display_surface,
            "pattern_map1": self.pattern_map1,
            "pattern_map2": self.pattern_map2,
            "color_map": self.color_map,
            "bump_map": self.bump_map,
            "env_map": self.env_map,
            "env_bump_map": self.env_bump_map,
            "bump_light_dir": self.bump_light_dir.to_json(),
            "bump_scale": self.bump_scale,
            "morph_in_time": self.morph_in_time,
            "morph_out_time": self.morph_out_time,
            "active": self.active,
            "fluid_type": self.fluid_type.to_json(),
            "unknown": self.unknown,
            "alpha": self.alpha,
            "unnamed_0x00000016": self.unnamed_0x00000016.to_json(),
            "turb_speed": self.turb_speed,
            "turb_distance": self.turb_distance,
            "turb_frequence_max": self.turb_frequence_max,
            "turb_frequence_min": self.turb_frequence_min,
            "turb_phase_max": self.turb_phase_max,
            "turb_phase_min": self.turb_phase_min,
            "turb_amplitude_max": self.turb_amplitude_max,
            "turb_amplitude_min": self.turb_amplitude_min,
            "splash_color": self.splash_color.to_json(),
            "inside_fog_color": self.inside_fog_color.to_json(),
            "splash_particle1": self.splash_particle1,
            "splash_particle2": self.splash_particle2,
            "splash_particle3": self.splash_particle3,
            "visor_runoff_particle": self.visor_runoff_particle,
            "unmorph_visor_runoff_particle": self.unmorph_visor_runoff_particle,
            "visor_runoff_sound": self.visor_runoff_sound,
            "unmorph_visor_runoff_sound": self.unmorph_visor_runoff_sound,
            "splash_sfx1": self.splash_sfx1,
            "splash_sfx2": self.splash_sfx2,
            "splash_sfx3": self.splash_sfx3,
            "tile_size": self.tile_size,
            "tile_subdivisions": self.tile_subdivisions,
            "specular_min": self.specular_min,
            "specular_max": self.specular_max,
            "reflection_size": self.reflection_size,
            "ripple_intensity": self.ripple_intensity,
            "reflection_blend": self.reflection_blend,
            "fog_bias": self.fog_bias,
            "fog_magnitude": self.fog_magnitude,
            "fog_speed": self.fog_speed,
            "fog_color": self.fog_color.to_json(),
            "lightmap": self.lightmap,
            "units_per_lightmap_texel": self.units_per_lightmap_texel,
            "alpha_in_time": self.alpha_in_time,
            "alpha_out_time": self.alpha_out_time,
            "alpha_in_recip": self.alpha_in_recip,
            "alpha_out_recip": self.alpha_out_recip,
            "unknown_will_crash_if_on": self.unknown_will_crash_if_on,
            "ignore_0x0000003d": self.ignore_0x0000003d,
            "ignore_0x0000003e": self.ignore_0x0000003e,
        }

    def _dependencies_for_pattern_map1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pattern_map1)

    def _dependencies_for_pattern_map2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pattern_map2)

    def _dependencies_for_color_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_map)

    def _dependencies_for_bump_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bump_map)

    def _dependencies_for_env_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.env_map)

    def _dependencies_for_env_bump_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.env_bump_map)

    def _dependencies_for_splash_particle1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_particle1)

    def _dependencies_for_splash_particle2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_particle2)

    def _dependencies_for_splash_particle3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_particle3)

    def _dependencies_for_visor_runoff_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_runoff_particle)

    def _dependencies_for_unmorph_visor_runoff_particle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unmorph_visor_runoff_particle)

    def _dependencies_for_visor_runoff_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.visor_runoff_sound)

    def _dependencies_for_unmorph_visor_runoff_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.unmorph_visor_runoff_sound)

    def _dependencies_for_splash_sfx1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.splash_sfx1)

    def _dependencies_for_splash_sfx2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.splash_sfx2)

    def _dependencies_for_splash_sfx3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.splash_sfx3)

    def _dependencies_for_lightmap(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.lightmap)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_pattern_map1, "pattern_map1", "AssetId"),
            (self._dependencies_for_pattern_map2, "pattern_map2", "AssetId"),
            (self._dependencies_for_color_map, "color_map", "AssetId"),
            (self._dependencies_for_bump_map, "bump_map", "AssetId"),
            (self._dependencies_for_env_map, "env_map", "AssetId"),
            (self._dependencies_for_env_bump_map, "env_bump_map", "AssetId"),
            (self._dependencies_for_splash_particle1, "splash_particle1", "AssetId"),
            (self._dependencies_for_splash_particle2, "splash_particle2", "AssetId"),
            (self._dependencies_for_splash_particle3, "splash_particle3", "AssetId"),
            (self._dependencies_for_visor_runoff_particle, "visor_runoff_particle", "AssetId"),
            (self._dependencies_for_unmorph_visor_runoff_particle, "unmorph_visor_runoff_particle", "AssetId"),
            (self._dependencies_for_visor_runoff_sound, "visor_runoff_sound", "int"),
            (self._dependencies_for_unmorph_visor_runoff_sound, "unmorph_visor_runoff_sound", "int"),
            (self._dependencies_for_splash_sfx1, "splash_sfx1", "int"),
            (self._dependencies_for_splash_sfx2, "splash_sfx2", "int"),
            (self._dependencies_for_splash_sfx3, "splash_sfx3", "int"),
            (self._dependencies_for_lightmap, "lightmap", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Water.{field_name} ({field_type}): {e}")
