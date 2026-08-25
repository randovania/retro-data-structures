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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.EchoParameters import EchoParameters
from retro_data_structures.properties.echoes.archetypes.SafeZoneStructA import SafeZoneStructA
from retro_data_structures.properties.echoes.archetypes.SafeZoneStructB import SafeZoneStructB
from retro_data_structures.properties.echoes.archetypes.TriggerInfo import TriggerInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SafeZoneJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        trigger: json_util.JsonObject
        deactivate_on_enter: bool
        deactivate_on_exit: bool
        activation_time: float
        deactivation_time: float
        lifetime: float
        random_lifetime_offset: float
        impact_effect: int
        filter_sound_effects: bool
        unknown_0x414379ea: int
        ignore_cinematic_camera: bool
        normal_safe_zone_struct: json_util.JsonObject
        energized_safe_zone_struct: json_util.JsonObject
        supercharged_safe_zone_struct: json_util.JsonObject
        normal_damage: json_util.JsonObject
        damage_info: json_util.JsonObject
        inside_fade_start: float
        inside_fade_time: float
        unknown_0x6c14904c: float
        flash_time: float
        flash_brightness: float
        flash_sound: int
        safezone_shape: int
        mobile: bool
        generate_mobile_light: bool
        mobile_light_offset: json_util.JsonValue
        unknown_0xe71b43e1: json_util.JsonValue
        unknown_0x9f638987: float
        safe_zone_struct_a_0x8a09f99a: json_util.JsonObject
        safe_zone_struct_a_0xafb855b8: json_util.JsonObject
        echo_parameters: json_util.JsonObject


@dataclasses.dataclass()
class SafeZone(BaseObjectType):
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
    deactivate_on_enter: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8D33465F, original_name="DeactivateOnEnter"),
        },
    )
    deactivate_on_exit: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1C453986, original_name="DeactivateOnExit"),
        },
    )
    activation_time: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEAD3E22E, original_name="ActivationTime"),
        },
    )
    deactivation_time: float = dataclasses.field(
        default=0.15000000596046448,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5CDF196, original_name="DeactivationTime"),
        },
    )
    lifetime: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32DC67F6, original_name="Lifetime"),
        },
    )
    random_lifetime_offset: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE169DB0, original_name="RandomLifetimeOffset"),
        },
    )
    impact_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9BE4BBD8, original_name="ImpactEffect"),
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
    ignore_cinematic_camera: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x62BAC460, original_name="IgnoreCinematicCamera"),
        },
    )
    normal_safe_zone_struct: SafeZoneStructB = dataclasses.field(
        default_factory=SafeZoneStructB,
        metadata={
            "reflection": FieldReflection[SafeZoneStructB](
                SafeZoneStructB,
                id=0xB4A293C7,
                original_name="Normal Safe Zone Struct",
                from_json=SafeZoneStructB.from_json,
                to_json=SafeZoneStructB.to_json,
            ),
        },
    )
    energized_safe_zone_struct: SafeZoneStructB = dataclasses.field(
        default_factory=SafeZoneStructB,
        metadata={
            "reflection": FieldReflection[SafeZoneStructB](
                SafeZoneStructB,
                id=0xDAE8C14E,
                original_name="Energized Safe Zone Struct",
                from_json=SafeZoneStructB.from_json,
                to_json=SafeZoneStructB.to_json,
            ),
        },
    )
    supercharged_safe_zone_struct: SafeZoneStructB = dataclasses.field(
        default_factory=SafeZoneStructB,
        metadata={
            "reflection": FieldReflection[SafeZoneStructB](
                SafeZoneStructB,
                id=0x6471D643,
                original_name="Supercharged Safe Zone Struct",
                from_json=SafeZoneStructB.from_json,
                to_json=SafeZoneStructB.to_json,
            ),
        },
    )
    normal_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xEEE2B188,
                original_name="NormalDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x78A13CA0,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    inside_fade_start: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08CCFFD0, original_name="InsideFadeStart"),
        },
    )
    inside_fade_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FEBBFE7, original_name="InsideFadeTime"),
        },
    )
    unknown_0x6c14904c: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C14904C, original_name="Unknown"),
        },
    )
    flash_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x48B4B865, original_name="FlashTime"),
        },
    )
    flash_brightness: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x452F7876, original_name="FlashBrightness"),
        },
    )
    flash_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x4FAAC896, original_name="FlashSound"),
        },
    )
    safezone_shape: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD5869B0B, original_name="SafezoneShape"),
        },
    )
    mobile: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x222A258E, original_name="Mobile"),
        },
    )
    generate_mobile_light: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x6C90E396, original_name="GenerateMobileLight"),
        },
    )
    mobile_light_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xA7963E03,
                original_name="MobileLightOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    unknown_0xe71b43e1: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.7372549772262573, g=1.0, b=1.0, a=0.24705900251865387),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE71B43E1, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x9f638987: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F638987, original_name="Unknown"),
        },
    )
    safe_zone_struct_a_0x8a09f99a: SafeZoneStructA = dataclasses.field(
        default_factory=SafeZoneStructA,
        metadata={
            "reflection": FieldReflection[SafeZoneStructA](
                SafeZoneStructA,
                id=0x8A09F99A,
                original_name="SafeZoneStructA",
                from_json=SafeZoneStructA.from_json,
                to_json=SafeZoneStructA.to_json,
            ),
        },
    )
    safe_zone_struct_a_0xafb855b8: SafeZoneStructA = dataclasses.field(
        default_factory=SafeZoneStructA,
        metadata={
            "reflection": FieldReflection[SafeZoneStructA](
                SafeZoneStructA,
                id=0xAFB855B8,
                original_name="SafeZoneStructA",
                from_json=SafeZoneStructA.from_json,
                to_json=SafeZoneStructA.to_json,
            ),
        },
    )
    echo_parameters: EchoParameters = dataclasses.field(
        default_factory=EchoParameters,
        metadata={
            "reflection": FieldReflection[EchoParameters](
                EchoParameters,
                id=0x4476BED8,
                original_name="EchoParameters",
                from_json=EchoParameters.from_json,
                to_json=EchoParameters.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SAFE"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptSafeZone.rel"]

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
        if property_count != 32:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77A27411
        trigger = TriggerInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D33465F
        deactivate_on_enter = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C453986
        deactivate_on_exit = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEAD3E22E
        activation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5CDF196
        deactivation_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32DC67F6
        lifetime = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE169DB0
        random_lifetime_offset = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9BE4BBD8
        impact_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x822118B4
        filter_sound_effects = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x414379EA
        unknown_0x414379ea = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62BAC460
        ignore_cinematic_camera = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB4A293C7
        normal_safe_zone_struct = SafeZoneStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDAE8C14E
        energized_safe_zone_struct = SafeZoneStructB.from_stream(
            data,
            game,
            property_size,
            default_override={
                "shell1_animated_horiz_rate": 0.03999999910593033,
                "shell1_animated_vert_rate": 0.0,
                "shell1_scale_horiz": 4.0,
                "shell1_scale_vert": 2.0,
                "shell2_scale_horiz": 10.0,
                "shell2_scale_vert": 12.0,
                "shell_color": Color(r=1.0, g=0.7372549772262573, b=0.3921569883823395, a=0.0),
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6471D643
        supercharged_safe_zone_struct = SafeZoneStructB.from_stream(
            data,
            game,
            property_size,
            default_override={
                "shell1_animated_horiz_rate": 0.03999999910593033,
                "shell1_animated_vert_rate": 0.0,
                "shell1_scale_horiz": 4.0,
                "shell1_scale_vert": 2.0,
                "shell2_scale_horiz": 10.0,
                "shell2_scale_vert": 12.0,
                "shell_color": Color(r=1.0, g=0.0, b=0.0, a=0.0),
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEEE2B188
        normal_damage = DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 20})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78A13CA0
        damage_info = DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 18})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08CCFFD0
        inside_fade_start = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FEBBFE7
        inside_fade_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C14904C
        unknown_0x6c14904c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48B4B865
        flash_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x452F7876
        flash_brightness = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4FAAC896
        flash_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5869B0B
        safezone_shape = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x222A258E
        mobile = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C90E396
        generate_mobile_light = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA7963E03
        mobile_light_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE71B43E1
        unknown_0xe71b43e1 = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F638987
        unknown_0x9f638987 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A09F99A
        safe_zone_struct_a_0x8a09f99a = SafeZoneStructA.from_stream(
            data,
            game,
            property_size,
            default_override={
                "enabled": False,
                "mode": 1,
                "color": Color(r=0.7372549772262573, g=1.0, b=1.0, a=0.0),
                "color_rate": 5.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFB855B8
        safe_zone_struct_a_0xafb855b8 = SafeZoneStructA.from_stream(
            data,
            game,
            property_size,
            default_override={
                "enabled": False,
                "mode": 1,
                "color": Color(r=0.0, g=0.09803900122642517, b=0.0, a=0.0),
                "color_rate": 5.0,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4476BED8
        echo_parameters = EchoParameters.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            trigger,
            deactivate_on_enter,
            deactivate_on_exit,
            activation_time,
            deactivation_time,
            lifetime,
            random_lifetime_offset,
            impact_effect,
            filter_sound_effects,
            unknown_0x414379ea,
            ignore_cinematic_camera,
            normal_safe_zone_struct,
            energized_safe_zone_struct,
            supercharged_safe_zone_struct,
            normal_damage,
            damage_info,
            inside_fade_start,
            inside_fade_time,
            unknown_0x6c14904c,
            flash_time,
            flash_brightness,
            flash_sound,
            safezone_shape,
            mobile,
            generate_mobile_light,
            mobile_light_offset,
            unknown_0xe71b43e1,
            unknown_0x9f638987,
            safe_zone_struct_a_0x8a09f99a,
            safe_zone_struct_a_0xafb855b8,
            echo_parameters,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00 ")  # 32 properties

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

        data.write(b"\x8d3F_")  # 0x8d33465f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.deactivate_on_enter))

        data.write(b"\x1cE9\x86")  # 0x1c453986
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.deactivate_on_exit))

        data.write(b"\xea\xd3\xe2.")  # 0xead3e22e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.activation_time))

        data.write(b"\xb5\xcd\xf1\x96")  # 0xb5cdf196
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.deactivation_time))

        data.write(b"2\xdcg\xf6")  # 0x32dc67f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lifetime))

        data.write(b"\xde\x16\x9d\xb0")  # 0xde169db0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.random_lifetime_offset))

        data.write(b"\x9b\xe4\xbb\xd8")  # 0x9be4bbd8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.impact_effect))

        data.write(b"\x82!\x18\xb4")  # 0x822118b4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.filter_sound_effects))

        data.write(b"ACy\xea")  # 0x414379ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x414379ea))

        data.write(b"b\xba\xc4`")  # 0x62bac460
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ignore_cinematic_camera))

        data.write(b"\xb4\xa2\x93\xc7")  # 0xb4a293c7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.normal_safe_zone_struct.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xda\xe8\xc1N")  # 0xdae8c14e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.energized_safe_zone_struct.to_stream(
            data,
            game,
            default_override={
                "shell1_animated_horiz_rate": 0.03999999910593033,
                "shell1_animated_vert_rate": 0.0,
                "shell1_scale_horiz": 4.0,
                "shell1_scale_vert": 2.0,
                "shell2_scale_horiz": 10.0,
                "shell2_scale_vert": 12.0,
                "shell_color": Color(r=1.0, g=0.7372549772262573, b=0.3921569883823395, a=0.0),
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"dq\xd6C")  # 0x6471d643
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.supercharged_safe_zone_struct.to_stream(
            data,
            game,
            default_override={
                "shell1_animated_horiz_rate": 0.03999999910593033,
                "shell1_animated_vert_rate": 0.0,
                "shell1_scale_horiz": 4.0,
                "shell1_scale_vert": 2.0,
                "shell2_scale_horiz": 10.0,
                "shell2_scale_vert": 12.0,
                "shell_color": Color(r=1.0, g=0.0, b=0.0, a=0.0),
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xee\xe2\xb1\x88")  # 0xeee2b188
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.normal_damage.to_stream(data, game, default_override={"di_weapon_type": 20})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"x\xa1<\xa0")  # 0x78a13ca0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info.to_stream(data, game, default_override={"di_weapon_type": 18})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x08\xcc\xff\xd0")  # 0x8ccffd0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.inside_fade_start))

        data.write(b"\x7f\xeb\xbf\xe7")  # 0x7febbfe7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.inside_fade_time))

        data.write(b"l\x14\x90L")  # 0x6c14904c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6c14904c))

        data.write(b"H\xb4\xb8e")  # 0x48b4b865
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_time))

        data.write(b"E/xv")  # 0x452f7876
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flash_brightness))

        data.write(b"O\xaa\xc8\x96")  # 0x4faac896
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.flash_sound))

        data.write(b"\xd5\x86\x9b\x0b")  # 0xd5869b0b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.safezone_shape))

        data.write(b'"*%\x8e')  # 0x222a258e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.mobile))

        data.write(b"l\x90\xe3\x96")  # 0x6c90e396
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.generate_mobile_light))

        data.write(b"\xa7\x96>\x03")  # 0xa7963e03
        data.write(b"\x00\x0c")  # size
        self.mobile_light_offset.to_stream(data, game)

        data.write(b"\xe7\x1bC\xe1")  # 0xe71b43e1
        data.write(b"\x00\x10")  # size
        self.unknown_0xe71b43e1.to_stream(data, game)

        data.write(b"\x9fc\x89\x87")  # 0x9f638987
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9f638987))

        data.write(b"\x8a\t\xf9\x9a")  # 0x8a09f99a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.safe_zone_struct_a_0x8a09f99a.to_stream(
            data,
            game,
            default_override={
                "enabled": False,
                "mode": 1,
                "color": Color(r=0.7372549772262573, g=1.0, b=1.0, a=0.0),
                "color_rate": 5.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaf\xb8U\xb8")  # 0xafb855b8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.safe_zone_struct_a_0xafb855b8.to_stream(
            data,
            game,
            default_override={
                "enabled": False,
                "mode": 1,
                "color": Color(r=0.0, g=0.09803900122642517, b=0.0, a=0.0),
                "color_rate": 5.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Dv\xbe\xd8")  # 0x4476bed8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.echo_parameters.to_stream(data, game)
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
        json_data = typing.cast("SafeZoneJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            trigger=TriggerInfo.from_json(json_data["trigger"]),
            deactivate_on_enter=json_data["deactivate_on_enter"],
            deactivate_on_exit=json_data["deactivate_on_exit"],
            activation_time=json_data["activation_time"],
            deactivation_time=json_data["deactivation_time"],
            lifetime=json_data["lifetime"],
            random_lifetime_offset=json_data["random_lifetime_offset"],
            impact_effect=json_data["impact_effect"],
            filter_sound_effects=json_data["filter_sound_effects"],
            unknown_0x414379ea=json_data["unknown_0x414379ea"],
            ignore_cinematic_camera=json_data["ignore_cinematic_camera"],
            normal_safe_zone_struct=SafeZoneStructB.from_json(json_data["normal_safe_zone_struct"]),
            energized_safe_zone_struct=SafeZoneStructB.from_json(json_data["energized_safe_zone_struct"]),
            supercharged_safe_zone_struct=SafeZoneStructB.from_json(json_data["supercharged_safe_zone_struct"]),
            normal_damage=DamageInfo.from_json(json_data["normal_damage"]),
            damage_info=DamageInfo.from_json(json_data["damage_info"]),
            inside_fade_start=json_data["inside_fade_start"],
            inside_fade_time=json_data["inside_fade_time"],
            unknown_0x6c14904c=json_data["unknown_0x6c14904c"],
            flash_time=json_data["flash_time"],
            flash_brightness=json_data["flash_brightness"],
            flash_sound=json_data["flash_sound"],
            safezone_shape=json_data["safezone_shape"],
            mobile=json_data["mobile"],
            generate_mobile_light=json_data["generate_mobile_light"],
            mobile_light_offset=Vector.from_json(json_data["mobile_light_offset"]),
            unknown_0xe71b43e1=Color.from_json(json_data["unknown_0xe71b43e1"]),
            unknown_0x9f638987=json_data["unknown_0x9f638987"],
            safe_zone_struct_a_0x8a09f99a=SafeZoneStructA.from_json(json_data["safe_zone_struct_a_0x8a09f99a"]),
            safe_zone_struct_a_0xafb855b8=SafeZoneStructA.from_json(json_data["safe_zone_struct_a_0xafb855b8"]),
            echo_parameters=EchoParameters.from_json(json_data["echo_parameters"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "trigger": self.trigger.to_json(),
            "deactivate_on_enter": self.deactivate_on_enter,
            "deactivate_on_exit": self.deactivate_on_exit,
            "activation_time": self.activation_time,
            "deactivation_time": self.deactivation_time,
            "lifetime": self.lifetime,
            "random_lifetime_offset": self.random_lifetime_offset,
            "impact_effect": self.impact_effect,
            "filter_sound_effects": self.filter_sound_effects,
            "unknown_0x414379ea": self.unknown_0x414379ea,
            "ignore_cinematic_camera": self.ignore_cinematic_camera,
            "normal_safe_zone_struct": self.normal_safe_zone_struct.to_json(),
            "energized_safe_zone_struct": self.energized_safe_zone_struct.to_json(),
            "supercharged_safe_zone_struct": self.supercharged_safe_zone_struct.to_json(),
            "normal_damage": self.normal_damage.to_json(),
            "damage_info": self.damage_info.to_json(),
            "inside_fade_start": self.inside_fade_start,
            "inside_fade_time": self.inside_fade_time,
            "unknown_0x6c14904c": self.unknown_0x6c14904c,
            "flash_time": self.flash_time,
            "flash_brightness": self.flash_brightness,
            "flash_sound": self.flash_sound,
            "safezone_shape": self.safezone_shape,
            "mobile": self.mobile,
            "generate_mobile_light": self.generate_mobile_light,
            "mobile_light_offset": self.mobile_light_offset.to_json(),
            "unknown_0xe71b43e1": self.unknown_0xe71b43e1.to_json(),
            "unknown_0x9f638987": self.unknown_0x9f638987,
            "safe_zone_struct_a_0x8a09f99a": self.safe_zone_struct_a_0x8a09f99a.to_json(),
            "safe_zone_struct_a_0xafb855b8": self.safe_zone_struct_a_0xafb855b8.to_json(),
            "echo_parameters": self.echo_parameters.to_json(),
        }

    def _dependencies_for_impact_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.impact_effect)

    def _dependencies_for_flash_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.flash_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_impact_effect, "impact_effect", "AssetId"),
            (self.normal_safe_zone_struct.dependencies_for, "normal_safe_zone_struct", "SafeZoneStructB"),
            (self.energized_safe_zone_struct.dependencies_for, "energized_safe_zone_struct", "SafeZoneStructB"),
            (self.supercharged_safe_zone_struct.dependencies_for, "supercharged_safe_zone_struct", "SafeZoneStructB"),
            (self._dependencies_for_flash_sound, "flash_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SafeZone.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_trigger(data: typing.BinaryIO, game: Game, property_size: int) -> TriggerInfo:
    return TriggerInfo.from_stream(data, game, property_size)


def _decode_normal_safe_zone_struct(data: typing.BinaryIO, game: Game, property_size: int) -> SafeZoneStructB:
    return SafeZoneStructB.from_stream(data, game, property_size)


def _decode_energized_safe_zone_struct(data: typing.BinaryIO, game: Game, property_size: int) -> SafeZoneStructB:
    return SafeZoneStructB.from_stream(
        data,
        game,
        property_size,
        default_override={
            "shell1_animated_horiz_rate": 0.03999999910593033,
            "shell1_animated_vert_rate": 0.0,
            "shell1_scale_horiz": 4.0,
            "shell1_scale_vert": 2.0,
            "shell2_scale_horiz": 10.0,
            "shell2_scale_vert": 12.0,
            "shell_color": Color(r=1.0, g=0.7372549772262573, b=0.3921569883823395, a=0.0),
        },
    )


def _decode_supercharged_safe_zone_struct(data: typing.BinaryIO, game: Game, property_size: int) -> SafeZoneStructB:
    return SafeZoneStructB.from_stream(
        data,
        game,
        property_size,
        default_override={
            "shell1_animated_horiz_rate": 0.03999999910593033,
            "shell1_animated_vert_rate": 0.0,
            "shell1_scale_horiz": 4.0,
            "shell1_scale_vert": 2.0,
            "shell2_scale_horiz": 10.0,
            "shell2_scale_vert": 12.0,
            "shell_color": Color(r=1.0, g=0.0, b=0.0, a=0.0),
        },
    )


def _decode_normal_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 20})


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 18})


def _decode_mobile_light_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0xe71b43e1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_safe_zone_struct_a_0x8a09f99a(data: typing.BinaryIO, game: Game, property_size: int) -> SafeZoneStructA:
    return SafeZoneStructA.from_stream(
        data,
        game,
        property_size,
        default_override={
            "enabled": False,
            "mode": 1,
            "color": Color(r=0.7372549772262573, g=1.0, b=1.0, a=0.0),
            "color_rate": 5.0,
        },
    )


def _decode_safe_zone_struct_a_0xafb855b8(data: typing.BinaryIO, game: Game, property_size: int) -> SafeZoneStructA:
    return SafeZoneStructA.from_stream(
        data,
        game,
        property_size,
        default_override={
            "enabled": False,
            "mode": 1,
            "color": Color(r=0.0, g=0.09803900122642517, b=0.0, a=0.0),
            "color_rate": 5.0,
        },
    )


def _decode_echo_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> EchoParameters:
    return EchoParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x77A27411: ("trigger", _decode_trigger),
    0x8D33465F: ("deactivate_on_enter", structs.decode_BIG_bool_),
    0x1C453986: ("deactivate_on_exit", structs.decode_BIG_bool_),
    0xEAD3E22E: ("activation_time", structs.decode_BIG_f),
    0xB5CDF196: ("deactivation_time", structs.decode_BIG_f),
    0x32DC67F6: ("lifetime", structs.decode_BIG_f),
    0xDE169DB0: ("random_lifetime_offset", structs.decode_BIG_f),
    0x9BE4BBD8: ("impact_effect", structs.decode_BIG_L),
    0x822118B4: ("filter_sound_effects", structs.decode_BIG_bool_),
    0x414379EA: ("unknown_0x414379ea", structs.decode_BIG_l),
    0x62BAC460: ("ignore_cinematic_camera", structs.decode_BIG_bool_),
    0xB4A293C7: ("normal_safe_zone_struct", _decode_normal_safe_zone_struct),
    0xDAE8C14E: ("energized_safe_zone_struct", _decode_energized_safe_zone_struct),
    0x6471D643: ("supercharged_safe_zone_struct", _decode_supercharged_safe_zone_struct),
    0xEEE2B188: ("normal_damage", _decode_normal_damage),
    0x78A13CA0: ("damage_info", _decode_damage_info),
    0x08CCFFD0: ("inside_fade_start", structs.decode_BIG_f),
    0x7FEBBFE7: ("inside_fade_time", structs.decode_BIG_f),
    0x6C14904C: ("unknown_0x6c14904c", structs.decode_BIG_f),
    0x48B4B865: ("flash_time", structs.decode_BIG_f),
    0x452F7876: ("flash_brightness", structs.decode_BIG_f),
    0x4FAAC896: ("flash_sound", structs.decode_BIG_l),
    0xD5869B0B: ("safezone_shape", structs.decode_BIG_l),
    0x222A258E: ("mobile", structs.decode_BIG_bool_),
    0x6C90E396: ("generate_mobile_light", structs.decode_BIG_bool_),
    0xA7963E03: ("mobile_light_offset", _decode_mobile_light_offset),
    0xE71B43E1: ("unknown_0xe71b43e1", _decode_unknown_0xe71b43e1),
    0x9F638987: ("unknown_0x9f638987", structs.decode_BIG_f),
    0x8A09F99A: ("safe_zone_struct_a_0x8a09f99a", _decode_safe_zone_struct_a_0x8a09f99a),
    0xAFB855B8: ("safe_zone_struct_a_0xafb855b8", _decode_safe_zone_struct_a_0xafb855b8),
    0x4476BED8: ("echo_parameters", _decode_echo_parameters),
}
