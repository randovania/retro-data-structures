# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayerControls_UnknownStruct1Json(typing_extensions.TypedDict):
        forward: int
        backward: int
        turn_left: int
        turn_right: int
        strafe_left: int
        strafe_right: int
        look_left: int
        look_right: int
        look_up: int
        look_down: int
        jump: int
        jump2: int
        fire_beam: int
        fire_beam2: int
        auto_fire_beam: int
        charge_beam: int
        charge_beam2: int
        use_item: int
        aim_up: int
        aim_down: int
        cycle_beam_up: int
        cycle_beam_down: int
        cycle_item: int
        select_power_beam: int
        select_ice_beam: int
        select_wave_beam: int
        select_plasma_beam: int
        gun_toggle_holster: int
        orbit_close: int
        orbit_far: int
        orbit_object: int
        orbit_select: int
        orbit_confirm: int
        orbit_left: int
        orbit_right: int
        orbit_up: int
        orbit_down: int
        hold_look1: int
        hold_look2: int
        look_zoom_in: int
        look_zoom_out: int
        hold_aim: int
        map_circle_up: int
        map_circle_down: int
        map_circle_left: int
        map_circle_right: int
        map_move_forward: int
        map_move_back: int
        map_move_left: int
        map_move_right: int
        map_zoom_in: int
        map_zoom_out: int
        spider_ball: int
        chase_camera: int
        x_ray_visor: int
        thermo_visor: int
        enviro_visor: int
        no_visor: int
        visor_menu: int
        cycle_visor_up: int
        cycle_visor_down: int
        dark_visor_toggle: int
        crosshairs: int
        unknown_0x29293fb1: int
        use_shield: int
        scan_item: int
        inventory_screen: int
        map_screen: int
        options_screen: int
        log_screen: int
        unknown_0xbf218f4f: int
        unknown_0x05ef2422: int
        boost_ball: int
        morph_into_ball: int
        morph_from_ball: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xAF03E16C,
    0xCFA71717,
    0x91532A8C,
    0x7ACC58D,
    0xACC575A2,
    0xDB475E1D,
    0xA900887A,
    0x534AC106,
    0xD723723,
    0x5C46B025,
    0xF836180A,
    0xFE16F98D,
    0xFD59AA9F,
    0x7E76F1F4,
    0x93DD818B,
    0x258402EC,
    0xB7A20CDA,
    0x5B9A9219,
    0x82A717CD,
    0xA7D5C15A,
    0x33731936,
    0xB72565FF,
    0xC592CA02,
    0x5228272C,
    0x901AC820,
    0x4ECEA0C0,
    0xA4F35804,
    0x919D7DE0,
    0x5200B48B,
    0x49C493A3,
    0xEB38A36B,
    0xC60F66D2,
    0x1D97CC2B,
    0xC449AE1D,
    0x80F17CDB,
    0xABC5A6AA,
    0x310F9642,
    0xC4923775,
    0xF57A2DE8,
    0xBA4FB516,
    0x9F45C8DB,
    0x5344D2F7,
    0x18C157D,
    0xAD1E8DE5,
    0x5858B5BA,
    0xC8DF5B8B,
    0x8D86D7B5,
    0xAB429EBD,
    0x31111D41,
    0xE2D939B7,
    0xB06D1B60,
    0x26293E7C,
    0x649B0835,
    0x5B1E0E7C,
    0xB35D2CCA,
    0x5A7E4DFC,
    0x76FAF77E,
    0x9BA498F6,
    0x2B9A4A7F,
    0xD6FB0BF9,
    0x8FE3ABE,
    0xC3F4F3EF,
    0x53E56DA8,
    0x29293FB1,
    0x2C06B91,
    0xBAA185CF,
    0x6CDD19A4,
    0xE08F6C6F,
    0x1230759B,
    0x5B9B4285,
    0xBF218F4F,
    0x5EF2422,
    0xCED85A1B,
    0x39CF6E72,
    0x64003596,
)


@dataclasses.dataclass()
class TweakPlayerControls_UnknownStruct1(BaseProperty):
    forward: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickUp,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xAF03E16C,
                original_name="Forward",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    backward: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xCFA71717,
                original_name="Backward",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    turn_left: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x91532A8C,
                original_name="TurnLeft",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    turn_right: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x07ACC58D,
                original_name="TurnRight",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    strafe_left: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xACC575A2,
                original_name="StrafeLeft",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    strafe_right: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xDB475E1D,
                original_name="StrafeRight",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    look_left: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xA900887A,
                original_name="LookLeft",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    look_right: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x534AC106,
                original_name="LookRight",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    look_up: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x0D723723,
                original_name="LookUp",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    look_down: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickUp,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5C46B025,
                original_name="LookDown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    jump: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.BButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xF836180A,
                original_name="Jump",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    jump2: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.BButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xFE16F98D,
                original_name="Jump2",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    fire_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.AButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xFD59AA9F,
                original_name="FireBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    fire_beam2: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.AButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x7E76F1F4,
                original_name="FireBeam2",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    auto_fire_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x93DD818B,
                original_name="AutoFireBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    charge_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.AButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x258402EC,
                original_name="ChargeBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    charge_beam2: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.AButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xB7A20CDA,
                original_name="ChargeBeam2",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    use_item: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.YButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5B9A9219,
                original_name="UseItem",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    aim_up: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x82A717CD,
                original_name="AimUp",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    aim_down: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xA7D5C15A,
                original_name="AimDown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    cycle_beam_up: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x33731936,
                original_name="CycleBeamUp",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    cycle_beam_down: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xB72565FF,
                original_name="CycleBeamDown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    cycle_item: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xC592CA02,
                original_name="CycleItem",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    select_power_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadUp,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5228272C,
                original_name="SelectPowerBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    select_ice_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x901AC820,
                original_name="SelectIceBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    select_wave_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x4ECEA0C0,
                original_name="SelectWaveBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    select_plasma_beam: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xA4F35804,
                original_name="SelectPlasmaBeam",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    gun_toggle_holster: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x919D7DE0,
                original_name="GunToggleHolster",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_close: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5200B48B,
                original_name="OrbitClose",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_far: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x49C493A3,
                original_name="OrbitFar",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_object: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftTriggerPress,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xEB38A36B,
                original_name="OrbitObject",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_select: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xC60F66D2,
                original_name="OrbitSelect",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_confirm: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x1D97CC2B,
                original_name="OrbitConfirm",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_left: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xC449AE1D,
                original_name="OrbitLeft",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_right: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x80F17CDB,
                original_name="OrbitRight",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_up: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickUp,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xABC5A6AA,
                original_name="OrbitUp",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    orbit_down: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x310F9642,
                original_name="OrbitDown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    hold_look1: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xC4923775,
                original_name="HoldLook1",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    hold_look2: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xF57A2DE8,
                original_name="HoldLook2",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    look_zoom_in: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.XButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xBA4FB516,
                original_name="LookZoomIn",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    look_zoom_out: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.YButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x9F45C8DB,
                original_name="LookZoomOut",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    hold_aim: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5344D2F7,
                original_name="HoldAim",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_circle_up: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x018C157D,
                original_name="MapCircleUp",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_circle_down: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickUp,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xAD1E8DE5,
                original_name="MapCircleDown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_circle_left: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5858B5BA,
                original_name="MapCircleLeft",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_circle_right: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftStickRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xC8DF5B8B,
                original_name="MapCircleRight",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_move_forward: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightStickUp,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x8D86D7B5,
                original_name="MapMoveForward",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_move_back: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightStickDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xAB429EBD,
                original_name="MapMoveBack",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_move_left: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightStickLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x31111D41,
                original_name="MapMoveLeft",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_move_right: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightStickRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xE2D939B7,
                original_name="MapMoveRight",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_zoom_in: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xB06D1B60,
                original_name="MapZoomIn",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_zoom_out: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x26293E7C,
                original_name="MapZoomOut",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    spider_ball: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x649B0835,
                original_name="SpiderBall",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    chase_camera: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5B1E0E7C,
                original_name="ChaseCamera",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    x_ray_visor: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xB35D2CCA,
                original_name="XRayVisor",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    thermo_visor: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5A7E4DFC,
                original_name="ThermoVisor",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    enviro_visor: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x76FAF77E,
                original_name="EnviroVisor",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    no_visor: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x9BA498F6,
                original_name="NoVisor",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    visor_menu: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x2B9A4A7F,
                original_name="VisorMenu",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    cycle_visor_up: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.ZButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xD6FB0BF9,
                original_name="CycleVisorUp",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    cycle_visor_down: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x08FE3ABE,
                original_name="CycleVisorDown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    dark_visor_toggle: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xC3F4F3EF,
                original_name="DarkVisorToggle",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    crosshairs: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightTriggerPress,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x53E56DA8,
                original_name="Crosshairs",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    unknown_0x29293fb1: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x29293FB1,
                original_name="Unknown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    use_shield: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum._None,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x02C06B91,
                original_name="UseShield",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    scan_item: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xBAA185CF,
                original_name="ScanItem",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    inventory_screen: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadLeft,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x6CDD19A4,
                original_name="InventoryScreen",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    map_screen: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.Start,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xE08F6C6F,
                original_name="MapScreen",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    options_screen: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadDown,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x1230759B,
                original_name="OptionsScreen",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    log_screen: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.DPadRight,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x5B9B4285,
                original_name="LogScreen",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    unknown_0xbf218f4f: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.LeftTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xBF218F4F,
                original_name="Unknown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    unknown_0x05ef2422: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.RightTrigger,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x05EF2422,
                original_name="Unknown",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    boost_ball: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.BButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0xCED85A1B,
                original_name="BoostBall",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    morph_into_ball: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.XButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x39CF6E72,
                original_name="MorphIntoBall",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
            ),
        },
    )
    morph_from_ball: enums.ControllerMappingEnum = dataclasses.field(
        default=enums.ControllerMappingEnum.XButton,
        metadata={
            "reflection": FieldReflection[enums.ControllerMappingEnum](
                enums.ControllerMappingEnum,
                id=0x64003596,
                original_name="MorphFromBall",
                from_json=enums.ControllerMappingEnum.from_json,
                to_json=enums.ControllerMappingEnum.to_json,
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
        if property_count != 75:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHLLHL"
            )

        dec = _FAST_FORMAT.unpack(data.read(750))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[60],
            dec[63],
            dec[66],
            dec[69],
            dec[72],
            dec[75],
            dec[78],
            dec[81],
            dec[84],
            dec[87],
            dec[90],
            dec[93],
            dec[96],
            dec[99],
            dec[102],
            dec[105],
            dec[108],
            dec[111],
            dec[114],
            dec[117],
            dec[120],
            dec[123],
            dec[126],
            dec[129],
            dec[132],
            dec[135],
            dec[138],
            dec[141],
            dec[144],
            dec[147],
            dec[150],
            dec[153],
            dec[156],
            dec[159],
            dec[162],
            dec[165],
            dec[168],
            dec[171],
            dec[174],
            dec[177],
            dec[180],
            dec[183],
            dec[186],
            dec[189],
            dec[192],
            dec[195],
            dec[198],
            dec[201],
            dec[204],
            dec[207],
            dec[210],
            dec[213],
            dec[216],
            dec[219],
            dec[222],
        ) == _FAST_IDS
        return cls(
            enums.ControllerMappingEnum(dec[2]),
            enums.ControllerMappingEnum(dec[5]),
            enums.ControllerMappingEnum(dec[8]),
            enums.ControllerMappingEnum(dec[11]),
            enums.ControllerMappingEnum(dec[14]),
            enums.ControllerMappingEnum(dec[17]),
            enums.ControllerMappingEnum(dec[20]),
            enums.ControllerMappingEnum(dec[23]),
            enums.ControllerMappingEnum(dec[26]),
            enums.ControllerMappingEnum(dec[29]),
            enums.ControllerMappingEnum(dec[32]),
            enums.ControllerMappingEnum(dec[35]),
            enums.ControllerMappingEnum(dec[38]),
            enums.ControllerMappingEnum(dec[41]),
            enums.ControllerMappingEnum(dec[44]),
            enums.ControllerMappingEnum(dec[47]),
            enums.ControllerMappingEnum(dec[50]),
            enums.ControllerMappingEnum(dec[53]),
            enums.ControllerMappingEnum(dec[56]),
            enums.ControllerMappingEnum(dec[59]),
            enums.ControllerMappingEnum(dec[62]),
            enums.ControllerMappingEnum(dec[65]),
            enums.ControllerMappingEnum(dec[68]),
            enums.ControllerMappingEnum(dec[71]),
            enums.ControllerMappingEnum(dec[74]),
            enums.ControllerMappingEnum(dec[77]),
            enums.ControllerMappingEnum(dec[80]),
            enums.ControllerMappingEnum(dec[83]),
            enums.ControllerMappingEnum(dec[86]),
            enums.ControllerMappingEnum(dec[89]),
            enums.ControllerMappingEnum(dec[92]),
            enums.ControllerMappingEnum(dec[95]),
            enums.ControllerMappingEnum(dec[98]),
            enums.ControllerMappingEnum(dec[101]),
            enums.ControllerMappingEnum(dec[104]),
            enums.ControllerMappingEnum(dec[107]),
            enums.ControllerMappingEnum(dec[110]),
            enums.ControllerMappingEnum(dec[113]),
            enums.ControllerMappingEnum(dec[116]),
            enums.ControllerMappingEnum(dec[119]),
            enums.ControllerMappingEnum(dec[122]),
            enums.ControllerMappingEnum(dec[125]),
            enums.ControllerMappingEnum(dec[128]),
            enums.ControllerMappingEnum(dec[131]),
            enums.ControllerMappingEnum(dec[134]),
            enums.ControllerMappingEnum(dec[137]),
            enums.ControllerMappingEnum(dec[140]),
            enums.ControllerMappingEnum(dec[143]),
            enums.ControllerMappingEnum(dec[146]),
            enums.ControllerMappingEnum(dec[149]),
            enums.ControllerMappingEnum(dec[152]),
            enums.ControllerMappingEnum(dec[155]),
            enums.ControllerMappingEnum(dec[158]),
            enums.ControllerMappingEnum(dec[161]),
            enums.ControllerMappingEnum(dec[164]),
            enums.ControllerMappingEnum(dec[167]),
            enums.ControllerMappingEnum(dec[170]),
            enums.ControllerMappingEnum(dec[173]),
            enums.ControllerMappingEnum(dec[176]),
            enums.ControllerMappingEnum(dec[179]),
            enums.ControllerMappingEnum(dec[182]),
            enums.ControllerMappingEnum(dec[185]),
            enums.ControllerMappingEnum(dec[188]),
            enums.ControllerMappingEnum(dec[191]),
            enums.ControllerMappingEnum(dec[194]),
            enums.ControllerMappingEnum(dec[197]),
            enums.ControllerMappingEnum(dec[200]),
            enums.ControllerMappingEnum(dec[203]),
            enums.ControllerMappingEnum(dec[206]),
            enums.ControllerMappingEnum(dec[209]),
            enums.ControllerMappingEnum(dec[212]),
            enums.ControllerMappingEnum(dec[215]),
            enums.ControllerMappingEnum(dec[218]),
            enums.ControllerMappingEnum(dec[221]),
            enums.ControllerMappingEnum(dec[224]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00K")  # 75 properties

        data.write(b"\xaf\x03\xe1l")  # 0xaf03e16c
        data.write(b"\x00\x04")  # size
        self.forward.to_stream(data, game)

        data.write(b"\xcf\xa7\x17\x17")  # 0xcfa71717
        data.write(b"\x00\x04")  # size
        self.backward.to_stream(data, game)

        data.write(b"\x91S*\x8c")  # 0x91532a8c
        data.write(b"\x00\x04")  # size
        self.turn_left.to_stream(data, game)

        data.write(b"\x07\xac\xc5\x8d")  # 0x7acc58d
        data.write(b"\x00\x04")  # size
        self.turn_right.to_stream(data, game)

        data.write(b"\xac\xc5u\xa2")  # 0xacc575a2
        data.write(b"\x00\x04")  # size
        self.strafe_left.to_stream(data, game)

        data.write(b"\xdbG^\x1d")  # 0xdb475e1d
        data.write(b"\x00\x04")  # size
        self.strafe_right.to_stream(data, game)

        data.write(b"\xa9\x00\x88z")  # 0xa900887a
        data.write(b"\x00\x04")  # size
        self.look_left.to_stream(data, game)

        data.write(b"SJ\xc1\x06")  # 0x534ac106
        data.write(b"\x00\x04")  # size
        self.look_right.to_stream(data, game)

        data.write(b"\rr7#")  # 0xd723723
        data.write(b"\x00\x04")  # size
        self.look_up.to_stream(data, game)

        data.write(b"\\F\xb0%")  # 0x5c46b025
        data.write(b"\x00\x04")  # size
        self.look_down.to_stream(data, game)

        data.write(b"\xf86\x18\n")  # 0xf836180a
        data.write(b"\x00\x04")  # size
        self.jump.to_stream(data, game)

        data.write(b"\xfe\x16\xf9\x8d")  # 0xfe16f98d
        data.write(b"\x00\x04")  # size
        self.jump2.to_stream(data, game)

        data.write(b"\xfdY\xaa\x9f")  # 0xfd59aa9f
        data.write(b"\x00\x04")  # size
        self.fire_beam.to_stream(data, game)

        data.write(b"~v\xf1\xf4")  # 0x7e76f1f4
        data.write(b"\x00\x04")  # size
        self.fire_beam2.to_stream(data, game)

        data.write(b"\x93\xdd\x81\x8b")  # 0x93dd818b
        data.write(b"\x00\x04")  # size
        self.auto_fire_beam.to_stream(data, game)

        data.write(b"%\x84\x02\xec")  # 0x258402ec
        data.write(b"\x00\x04")  # size
        self.charge_beam.to_stream(data, game)

        data.write(b"\xb7\xa2\x0c\xda")  # 0xb7a20cda
        data.write(b"\x00\x04")  # size
        self.charge_beam2.to_stream(data, game)

        data.write(b"[\x9a\x92\x19")  # 0x5b9a9219
        data.write(b"\x00\x04")  # size
        self.use_item.to_stream(data, game)

        data.write(b"\x82\xa7\x17\xcd")  # 0x82a717cd
        data.write(b"\x00\x04")  # size
        self.aim_up.to_stream(data, game)

        data.write(b"\xa7\xd5\xc1Z")  # 0xa7d5c15a
        data.write(b"\x00\x04")  # size
        self.aim_down.to_stream(data, game)

        data.write(b"3s\x196")  # 0x33731936
        data.write(b"\x00\x04")  # size
        self.cycle_beam_up.to_stream(data, game)

        data.write(b"\xb7%e\xff")  # 0xb72565ff
        data.write(b"\x00\x04")  # size
        self.cycle_beam_down.to_stream(data, game)

        data.write(b"\xc5\x92\xca\x02")  # 0xc592ca02
        data.write(b"\x00\x04")  # size
        self.cycle_item.to_stream(data, game)

        data.write(b"R(',")  # 0x5228272c
        data.write(b"\x00\x04")  # size
        self.select_power_beam.to_stream(data, game)

        data.write(b"\x90\x1a\xc8 ")  # 0x901ac820
        data.write(b"\x00\x04")  # size
        self.select_ice_beam.to_stream(data, game)

        data.write(b"N\xce\xa0\xc0")  # 0x4ecea0c0
        data.write(b"\x00\x04")  # size
        self.select_wave_beam.to_stream(data, game)

        data.write(b"\xa4\xf3X\x04")  # 0xa4f35804
        data.write(b"\x00\x04")  # size
        self.select_plasma_beam.to_stream(data, game)

        data.write(b"\x91\x9d}\xe0")  # 0x919d7de0
        data.write(b"\x00\x04")  # size
        self.gun_toggle_holster.to_stream(data, game)

        data.write(b"R\x00\xb4\x8b")  # 0x5200b48b
        data.write(b"\x00\x04")  # size
        self.orbit_close.to_stream(data, game)

        data.write(b"I\xc4\x93\xa3")  # 0x49c493a3
        data.write(b"\x00\x04")  # size
        self.orbit_far.to_stream(data, game)

        data.write(b"\xeb8\xa3k")  # 0xeb38a36b
        data.write(b"\x00\x04")  # size
        self.orbit_object.to_stream(data, game)

        data.write(b"\xc6\x0ff\xd2")  # 0xc60f66d2
        data.write(b"\x00\x04")  # size
        self.orbit_select.to_stream(data, game)

        data.write(b"\x1d\x97\xcc+")  # 0x1d97cc2b
        data.write(b"\x00\x04")  # size
        self.orbit_confirm.to_stream(data, game)

        data.write(b"\xc4I\xae\x1d")  # 0xc449ae1d
        data.write(b"\x00\x04")  # size
        self.orbit_left.to_stream(data, game)

        data.write(b"\x80\xf1|\xdb")  # 0x80f17cdb
        data.write(b"\x00\x04")  # size
        self.orbit_right.to_stream(data, game)

        data.write(b"\xab\xc5\xa6\xaa")  # 0xabc5a6aa
        data.write(b"\x00\x04")  # size
        self.orbit_up.to_stream(data, game)

        data.write(b"1\x0f\x96B")  # 0x310f9642
        data.write(b"\x00\x04")  # size
        self.orbit_down.to_stream(data, game)

        data.write(b"\xc4\x927u")  # 0xc4923775
        data.write(b"\x00\x04")  # size
        self.hold_look1.to_stream(data, game)

        data.write(b"\xf5z-\xe8")  # 0xf57a2de8
        data.write(b"\x00\x04")  # size
        self.hold_look2.to_stream(data, game)

        data.write(b"\xbaO\xb5\x16")  # 0xba4fb516
        data.write(b"\x00\x04")  # size
        self.look_zoom_in.to_stream(data, game)

        data.write(b"\x9fE\xc8\xdb")  # 0x9f45c8db
        data.write(b"\x00\x04")  # size
        self.look_zoom_out.to_stream(data, game)

        data.write(b"SD\xd2\xf7")  # 0x5344d2f7
        data.write(b"\x00\x04")  # size
        self.hold_aim.to_stream(data, game)

        data.write(b"\x01\x8c\x15}")  # 0x18c157d
        data.write(b"\x00\x04")  # size
        self.map_circle_up.to_stream(data, game)

        data.write(b"\xad\x1e\x8d\xe5")  # 0xad1e8de5
        data.write(b"\x00\x04")  # size
        self.map_circle_down.to_stream(data, game)

        data.write(b"XX\xb5\xba")  # 0x5858b5ba
        data.write(b"\x00\x04")  # size
        self.map_circle_left.to_stream(data, game)

        data.write(b"\xc8\xdf[\x8b")  # 0xc8df5b8b
        data.write(b"\x00\x04")  # size
        self.map_circle_right.to_stream(data, game)

        data.write(b"\x8d\x86\xd7\xb5")  # 0x8d86d7b5
        data.write(b"\x00\x04")  # size
        self.map_move_forward.to_stream(data, game)

        data.write(b"\xabB\x9e\xbd")  # 0xab429ebd
        data.write(b"\x00\x04")  # size
        self.map_move_back.to_stream(data, game)

        data.write(b"1\x11\x1dA")  # 0x31111d41
        data.write(b"\x00\x04")  # size
        self.map_move_left.to_stream(data, game)

        data.write(b"\xe2\xd99\xb7")  # 0xe2d939b7
        data.write(b"\x00\x04")  # size
        self.map_move_right.to_stream(data, game)

        data.write(b"\xb0m\x1b`")  # 0xb06d1b60
        data.write(b"\x00\x04")  # size
        self.map_zoom_in.to_stream(data, game)

        data.write(b"&)>|")  # 0x26293e7c
        data.write(b"\x00\x04")  # size
        self.map_zoom_out.to_stream(data, game)

        data.write(b"d\x9b\x085")  # 0x649b0835
        data.write(b"\x00\x04")  # size
        self.spider_ball.to_stream(data, game)

        data.write(b"[\x1e\x0e|")  # 0x5b1e0e7c
        data.write(b"\x00\x04")  # size
        self.chase_camera.to_stream(data, game)

        data.write(b"\xb3],\xca")  # 0xb35d2cca
        data.write(b"\x00\x04")  # size
        self.x_ray_visor.to_stream(data, game)

        data.write(b"Z~M\xfc")  # 0x5a7e4dfc
        data.write(b"\x00\x04")  # size
        self.thermo_visor.to_stream(data, game)

        data.write(b"v\xfa\xf7~")  # 0x76faf77e
        data.write(b"\x00\x04")  # size
        self.enviro_visor.to_stream(data, game)

        data.write(b"\x9b\xa4\x98\xf6")  # 0x9ba498f6
        data.write(b"\x00\x04")  # size
        self.no_visor.to_stream(data, game)

        data.write(b"+\x9aJ\x7f")  # 0x2b9a4a7f
        data.write(b"\x00\x04")  # size
        self.visor_menu.to_stream(data, game)

        data.write(b"\xd6\xfb\x0b\xf9")  # 0xd6fb0bf9
        data.write(b"\x00\x04")  # size
        self.cycle_visor_up.to_stream(data, game)

        data.write(b"\x08\xfe:\xbe")  # 0x8fe3abe
        data.write(b"\x00\x04")  # size
        self.cycle_visor_down.to_stream(data, game)

        data.write(b"\xc3\xf4\xf3\xef")  # 0xc3f4f3ef
        data.write(b"\x00\x04")  # size
        self.dark_visor_toggle.to_stream(data, game)

        data.write(b"S\xe5m\xa8")  # 0x53e56da8
        data.write(b"\x00\x04")  # size
        self.crosshairs.to_stream(data, game)

        data.write(b"))?\xb1")  # 0x29293fb1
        data.write(b"\x00\x04")  # size
        self.unknown_0x29293fb1.to_stream(data, game)

        data.write(b"\x02\xc0k\x91")  # 0x2c06b91
        data.write(b"\x00\x04")  # size
        self.use_shield.to_stream(data, game)

        data.write(b"\xba\xa1\x85\xcf")  # 0xbaa185cf
        data.write(b"\x00\x04")  # size
        self.scan_item.to_stream(data, game)

        data.write(b"l\xdd\x19\xa4")  # 0x6cdd19a4
        data.write(b"\x00\x04")  # size
        self.inventory_screen.to_stream(data, game)

        data.write(b"\xe0\x8flo")  # 0xe08f6c6f
        data.write(b"\x00\x04")  # size
        self.map_screen.to_stream(data, game)

        data.write(b"\x120u\x9b")  # 0x1230759b
        data.write(b"\x00\x04")  # size
        self.options_screen.to_stream(data, game)

        data.write(b"[\x9bB\x85")  # 0x5b9b4285
        data.write(b"\x00\x04")  # size
        self.log_screen.to_stream(data, game)

        data.write(b"\xbf!\x8fO")  # 0xbf218f4f
        data.write(b"\x00\x04")  # size
        self.unknown_0xbf218f4f.to_stream(data, game)

        data.write(b'\x05\xef$"')  # 0x5ef2422
        data.write(b"\x00\x04")  # size
        self.unknown_0x05ef2422.to_stream(data, game)

        data.write(b"\xce\xd8Z\x1b")  # 0xced85a1b
        data.write(b"\x00\x04")  # size
        self.boost_ball.to_stream(data, game)

        data.write(b"9\xcfnr")  # 0x39cf6e72
        data.write(b"\x00\x04")  # size
        self.morph_into_ball.to_stream(data, game)

        data.write(b"d\x005\x96")  # 0x64003596
        data.write(b"\x00\x04")  # size
        self.morph_from_ball.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerControls_UnknownStruct1Json", data)
        return cls(
            forward=enums.ControllerMappingEnum.from_json(json_data["forward"]),
            backward=enums.ControllerMappingEnum.from_json(json_data["backward"]),
            turn_left=enums.ControllerMappingEnum.from_json(json_data["turn_left"]),
            turn_right=enums.ControllerMappingEnum.from_json(json_data["turn_right"]),
            strafe_left=enums.ControllerMappingEnum.from_json(json_data["strafe_left"]),
            strafe_right=enums.ControllerMappingEnum.from_json(json_data["strafe_right"]),
            look_left=enums.ControllerMappingEnum.from_json(json_data["look_left"]),
            look_right=enums.ControllerMappingEnum.from_json(json_data["look_right"]),
            look_up=enums.ControllerMappingEnum.from_json(json_data["look_up"]),
            look_down=enums.ControllerMappingEnum.from_json(json_data["look_down"]),
            jump=enums.ControllerMappingEnum.from_json(json_data["jump"]),
            jump2=enums.ControllerMappingEnum.from_json(json_data["jump2"]),
            fire_beam=enums.ControllerMappingEnum.from_json(json_data["fire_beam"]),
            fire_beam2=enums.ControllerMappingEnum.from_json(json_data["fire_beam2"]),
            auto_fire_beam=enums.ControllerMappingEnum.from_json(json_data["auto_fire_beam"]),
            charge_beam=enums.ControllerMappingEnum.from_json(json_data["charge_beam"]),
            charge_beam2=enums.ControllerMappingEnum.from_json(json_data["charge_beam2"]),
            use_item=enums.ControllerMappingEnum.from_json(json_data["use_item"]),
            aim_up=enums.ControllerMappingEnum.from_json(json_data["aim_up"]),
            aim_down=enums.ControllerMappingEnum.from_json(json_data["aim_down"]),
            cycle_beam_up=enums.ControllerMappingEnum.from_json(json_data["cycle_beam_up"]),
            cycle_beam_down=enums.ControllerMappingEnum.from_json(json_data["cycle_beam_down"]),
            cycle_item=enums.ControllerMappingEnum.from_json(json_data["cycle_item"]),
            select_power_beam=enums.ControllerMappingEnum.from_json(json_data["select_power_beam"]),
            select_ice_beam=enums.ControllerMappingEnum.from_json(json_data["select_ice_beam"]),
            select_wave_beam=enums.ControllerMappingEnum.from_json(json_data["select_wave_beam"]),
            select_plasma_beam=enums.ControllerMappingEnum.from_json(json_data["select_plasma_beam"]),
            gun_toggle_holster=enums.ControllerMappingEnum.from_json(json_data["gun_toggle_holster"]),
            orbit_close=enums.ControllerMappingEnum.from_json(json_data["orbit_close"]),
            orbit_far=enums.ControllerMappingEnum.from_json(json_data["orbit_far"]),
            orbit_object=enums.ControllerMappingEnum.from_json(json_data["orbit_object"]),
            orbit_select=enums.ControllerMappingEnum.from_json(json_data["orbit_select"]),
            orbit_confirm=enums.ControllerMappingEnum.from_json(json_data["orbit_confirm"]),
            orbit_left=enums.ControllerMappingEnum.from_json(json_data["orbit_left"]),
            orbit_right=enums.ControllerMappingEnum.from_json(json_data["orbit_right"]),
            orbit_up=enums.ControllerMappingEnum.from_json(json_data["orbit_up"]),
            orbit_down=enums.ControllerMappingEnum.from_json(json_data["orbit_down"]),
            hold_look1=enums.ControllerMappingEnum.from_json(json_data["hold_look1"]),
            hold_look2=enums.ControllerMappingEnum.from_json(json_data["hold_look2"]),
            look_zoom_in=enums.ControllerMappingEnum.from_json(json_data["look_zoom_in"]),
            look_zoom_out=enums.ControllerMappingEnum.from_json(json_data["look_zoom_out"]),
            hold_aim=enums.ControllerMappingEnum.from_json(json_data["hold_aim"]),
            map_circle_up=enums.ControllerMappingEnum.from_json(json_data["map_circle_up"]),
            map_circle_down=enums.ControllerMappingEnum.from_json(json_data["map_circle_down"]),
            map_circle_left=enums.ControllerMappingEnum.from_json(json_data["map_circle_left"]),
            map_circle_right=enums.ControllerMappingEnum.from_json(json_data["map_circle_right"]),
            map_move_forward=enums.ControllerMappingEnum.from_json(json_data["map_move_forward"]),
            map_move_back=enums.ControllerMappingEnum.from_json(json_data["map_move_back"]),
            map_move_left=enums.ControllerMappingEnum.from_json(json_data["map_move_left"]),
            map_move_right=enums.ControllerMappingEnum.from_json(json_data["map_move_right"]),
            map_zoom_in=enums.ControllerMappingEnum.from_json(json_data["map_zoom_in"]),
            map_zoom_out=enums.ControllerMappingEnum.from_json(json_data["map_zoom_out"]),
            spider_ball=enums.ControllerMappingEnum.from_json(json_data["spider_ball"]),
            chase_camera=enums.ControllerMappingEnum.from_json(json_data["chase_camera"]),
            x_ray_visor=enums.ControllerMappingEnum.from_json(json_data["x_ray_visor"]),
            thermo_visor=enums.ControllerMappingEnum.from_json(json_data["thermo_visor"]),
            enviro_visor=enums.ControllerMappingEnum.from_json(json_data["enviro_visor"]),
            no_visor=enums.ControllerMappingEnum.from_json(json_data["no_visor"]),
            visor_menu=enums.ControllerMappingEnum.from_json(json_data["visor_menu"]),
            cycle_visor_up=enums.ControllerMappingEnum.from_json(json_data["cycle_visor_up"]),
            cycle_visor_down=enums.ControllerMappingEnum.from_json(json_data["cycle_visor_down"]),
            dark_visor_toggle=enums.ControllerMappingEnum.from_json(json_data["dark_visor_toggle"]),
            crosshairs=enums.ControllerMappingEnum.from_json(json_data["crosshairs"]),
            unknown_0x29293fb1=enums.ControllerMappingEnum.from_json(json_data["unknown_0x29293fb1"]),
            use_shield=enums.ControllerMappingEnum.from_json(json_data["use_shield"]),
            scan_item=enums.ControllerMappingEnum.from_json(json_data["scan_item"]),
            inventory_screen=enums.ControllerMappingEnum.from_json(json_data["inventory_screen"]),
            map_screen=enums.ControllerMappingEnum.from_json(json_data["map_screen"]),
            options_screen=enums.ControllerMappingEnum.from_json(json_data["options_screen"]),
            log_screen=enums.ControllerMappingEnum.from_json(json_data["log_screen"]),
            unknown_0xbf218f4f=enums.ControllerMappingEnum.from_json(json_data["unknown_0xbf218f4f"]),
            unknown_0x05ef2422=enums.ControllerMappingEnum.from_json(json_data["unknown_0x05ef2422"]),
            boost_ball=enums.ControllerMappingEnum.from_json(json_data["boost_ball"]),
            morph_into_ball=enums.ControllerMappingEnum.from_json(json_data["morph_into_ball"]),
            morph_from_ball=enums.ControllerMappingEnum.from_json(json_data["morph_from_ball"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "forward": self.forward.to_json(),
            "backward": self.backward.to_json(),
            "turn_left": self.turn_left.to_json(),
            "turn_right": self.turn_right.to_json(),
            "strafe_left": self.strafe_left.to_json(),
            "strafe_right": self.strafe_right.to_json(),
            "look_left": self.look_left.to_json(),
            "look_right": self.look_right.to_json(),
            "look_up": self.look_up.to_json(),
            "look_down": self.look_down.to_json(),
            "jump": self.jump.to_json(),
            "jump2": self.jump2.to_json(),
            "fire_beam": self.fire_beam.to_json(),
            "fire_beam2": self.fire_beam2.to_json(),
            "auto_fire_beam": self.auto_fire_beam.to_json(),
            "charge_beam": self.charge_beam.to_json(),
            "charge_beam2": self.charge_beam2.to_json(),
            "use_item": self.use_item.to_json(),
            "aim_up": self.aim_up.to_json(),
            "aim_down": self.aim_down.to_json(),
            "cycle_beam_up": self.cycle_beam_up.to_json(),
            "cycle_beam_down": self.cycle_beam_down.to_json(),
            "cycle_item": self.cycle_item.to_json(),
            "select_power_beam": self.select_power_beam.to_json(),
            "select_ice_beam": self.select_ice_beam.to_json(),
            "select_wave_beam": self.select_wave_beam.to_json(),
            "select_plasma_beam": self.select_plasma_beam.to_json(),
            "gun_toggle_holster": self.gun_toggle_holster.to_json(),
            "orbit_close": self.orbit_close.to_json(),
            "orbit_far": self.orbit_far.to_json(),
            "orbit_object": self.orbit_object.to_json(),
            "orbit_select": self.orbit_select.to_json(),
            "orbit_confirm": self.orbit_confirm.to_json(),
            "orbit_left": self.orbit_left.to_json(),
            "orbit_right": self.orbit_right.to_json(),
            "orbit_up": self.orbit_up.to_json(),
            "orbit_down": self.orbit_down.to_json(),
            "hold_look1": self.hold_look1.to_json(),
            "hold_look2": self.hold_look2.to_json(),
            "look_zoom_in": self.look_zoom_in.to_json(),
            "look_zoom_out": self.look_zoom_out.to_json(),
            "hold_aim": self.hold_aim.to_json(),
            "map_circle_up": self.map_circle_up.to_json(),
            "map_circle_down": self.map_circle_down.to_json(),
            "map_circle_left": self.map_circle_left.to_json(),
            "map_circle_right": self.map_circle_right.to_json(),
            "map_move_forward": self.map_move_forward.to_json(),
            "map_move_back": self.map_move_back.to_json(),
            "map_move_left": self.map_move_left.to_json(),
            "map_move_right": self.map_move_right.to_json(),
            "map_zoom_in": self.map_zoom_in.to_json(),
            "map_zoom_out": self.map_zoom_out.to_json(),
            "spider_ball": self.spider_ball.to_json(),
            "chase_camera": self.chase_camera.to_json(),
            "x_ray_visor": self.x_ray_visor.to_json(),
            "thermo_visor": self.thermo_visor.to_json(),
            "enviro_visor": self.enviro_visor.to_json(),
            "no_visor": self.no_visor.to_json(),
            "visor_menu": self.visor_menu.to_json(),
            "cycle_visor_up": self.cycle_visor_up.to_json(),
            "cycle_visor_down": self.cycle_visor_down.to_json(),
            "dark_visor_toggle": self.dark_visor_toggle.to_json(),
            "crosshairs": self.crosshairs.to_json(),
            "unknown_0x29293fb1": self.unknown_0x29293fb1.to_json(),
            "use_shield": self.use_shield.to_json(),
            "scan_item": self.scan_item.to_json(),
            "inventory_screen": self.inventory_screen.to_json(),
            "map_screen": self.map_screen.to_json(),
            "options_screen": self.options_screen.to_json(),
            "log_screen": self.log_screen.to_json(),
            "unknown_0xbf218f4f": self.unknown_0xbf218f4f.to_json(),
            "unknown_0x05ef2422": self.unknown_0x05ef2422.to_json(),
            "boost_ball": self.boost_ball.to_json(),
            "morph_into_ball": self.morph_into_ball.to_json(),
            "morph_from_ball": self.morph_from_ball.to_json(),
        }


def _decode_forward(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_backward(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_turn_left(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_turn_right(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_strafe_left(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_strafe_right(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_look_left(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_look_right(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_look_up(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_look_down(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_jump(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_jump2(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_fire_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_fire_beam2(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_auto_fire_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_charge_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_charge_beam2(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_use_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_aim_up(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_aim_down(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_cycle_beam_up(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_cycle_beam_down(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_cycle_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_select_power_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_select_ice_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_select_wave_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_select_plasma_beam(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_gun_toggle_holster(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_close(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_far(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_object(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_select(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_confirm(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_left(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_right(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_up(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_orbit_down(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_hold_look1(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_hold_look2(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_look_zoom_in(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_look_zoom_out(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_hold_aim(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_circle_up(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_circle_down(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_circle_left(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_circle_right(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_move_forward(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_move_back(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_move_left(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_move_right(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_zoom_in(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_zoom_out(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_spider_ball(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_chase_camera(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_x_ray_visor(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_thermo_visor(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_enviro_visor(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_no_visor(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_visor_menu(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_cycle_visor_up(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_cycle_visor_down(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_dark_visor_toggle(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_crosshairs(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_unknown_0x29293fb1(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_use_shield(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_scan_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_inventory_screen(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_map_screen(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_options_screen(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_log_screen(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_unknown_0xbf218f4f(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_unknown_0x05ef2422(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_boost_ball(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_morph_into_ball(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


def _decode_morph_from_ball(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ControllerMappingEnum:
    return enums.ControllerMappingEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xAF03E16C: ("forward", _decode_forward),
    0xCFA71717: ("backward", _decode_backward),
    0x91532A8C: ("turn_left", _decode_turn_left),
    0x07ACC58D: ("turn_right", _decode_turn_right),
    0xACC575A2: ("strafe_left", _decode_strafe_left),
    0xDB475E1D: ("strafe_right", _decode_strafe_right),
    0xA900887A: ("look_left", _decode_look_left),
    0x534AC106: ("look_right", _decode_look_right),
    0x0D723723: ("look_up", _decode_look_up),
    0x5C46B025: ("look_down", _decode_look_down),
    0xF836180A: ("jump", _decode_jump),
    0xFE16F98D: ("jump2", _decode_jump2),
    0xFD59AA9F: ("fire_beam", _decode_fire_beam),
    0x7E76F1F4: ("fire_beam2", _decode_fire_beam2),
    0x93DD818B: ("auto_fire_beam", _decode_auto_fire_beam),
    0x258402EC: ("charge_beam", _decode_charge_beam),
    0xB7A20CDA: ("charge_beam2", _decode_charge_beam2),
    0x5B9A9219: ("use_item", _decode_use_item),
    0x82A717CD: ("aim_up", _decode_aim_up),
    0xA7D5C15A: ("aim_down", _decode_aim_down),
    0x33731936: ("cycle_beam_up", _decode_cycle_beam_up),
    0xB72565FF: ("cycle_beam_down", _decode_cycle_beam_down),
    0xC592CA02: ("cycle_item", _decode_cycle_item),
    0x5228272C: ("select_power_beam", _decode_select_power_beam),
    0x901AC820: ("select_ice_beam", _decode_select_ice_beam),
    0x4ECEA0C0: ("select_wave_beam", _decode_select_wave_beam),
    0xA4F35804: ("select_plasma_beam", _decode_select_plasma_beam),
    0x919D7DE0: ("gun_toggle_holster", _decode_gun_toggle_holster),
    0x5200B48B: ("orbit_close", _decode_orbit_close),
    0x49C493A3: ("orbit_far", _decode_orbit_far),
    0xEB38A36B: ("orbit_object", _decode_orbit_object),
    0xC60F66D2: ("orbit_select", _decode_orbit_select),
    0x1D97CC2B: ("orbit_confirm", _decode_orbit_confirm),
    0xC449AE1D: ("orbit_left", _decode_orbit_left),
    0x80F17CDB: ("orbit_right", _decode_orbit_right),
    0xABC5A6AA: ("orbit_up", _decode_orbit_up),
    0x310F9642: ("orbit_down", _decode_orbit_down),
    0xC4923775: ("hold_look1", _decode_hold_look1),
    0xF57A2DE8: ("hold_look2", _decode_hold_look2),
    0xBA4FB516: ("look_zoom_in", _decode_look_zoom_in),
    0x9F45C8DB: ("look_zoom_out", _decode_look_zoom_out),
    0x5344D2F7: ("hold_aim", _decode_hold_aim),
    0x018C157D: ("map_circle_up", _decode_map_circle_up),
    0xAD1E8DE5: ("map_circle_down", _decode_map_circle_down),
    0x5858B5BA: ("map_circle_left", _decode_map_circle_left),
    0xC8DF5B8B: ("map_circle_right", _decode_map_circle_right),
    0x8D86D7B5: ("map_move_forward", _decode_map_move_forward),
    0xAB429EBD: ("map_move_back", _decode_map_move_back),
    0x31111D41: ("map_move_left", _decode_map_move_left),
    0xE2D939B7: ("map_move_right", _decode_map_move_right),
    0xB06D1B60: ("map_zoom_in", _decode_map_zoom_in),
    0x26293E7C: ("map_zoom_out", _decode_map_zoom_out),
    0x649B0835: ("spider_ball", _decode_spider_ball),
    0x5B1E0E7C: ("chase_camera", _decode_chase_camera),
    0xB35D2CCA: ("x_ray_visor", _decode_x_ray_visor),
    0x5A7E4DFC: ("thermo_visor", _decode_thermo_visor),
    0x76FAF77E: ("enviro_visor", _decode_enviro_visor),
    0x9BA498F6: ("no_visor", _decode_no_visor),
    0x2B9A4A7F: ("visor_menu", _decode_visor_menu),
    0xD6FB0BF9: ("cycle_visor_up", _decode_cycle_visor_up),
    0x08FE3ABE: ("cycle_visor_down", _decode_cycle_visor_down),
    0xC3F4F3EF: ("dark_visor_toggle", _decode_dark_visor_toggle),
    0x53E56DA8: ("crosshairs", _decode_crosshairs),
    0x29293FB1: ("unknown_0x29293fb1", _decode_unknown_0x29293fb1),
    0x02C06B91: ("use_shield", _decode_use_shield),
    0xBAA185CF: ("scan_item", _decode_scan_item),
    0x6CDD19A4: ("inventory_screen", _decode_inventory_screen),
    0xE08F6C6F: ("map_screen", _decode_map_screen),
    0x1230759B: ("options_screen", _decode_options_screen),
    0x5B9B4285: ("log_screen", _decode_log_screen),
    0xBF218F4F: ("unknown_0xbf218f4f", _decode_unknown_0xbf218f4f),
    0x05EF2422: ("unknown_0x05ef2422", _decode_unknown_0x05ef2422),
    0xCED85A1B: ("boost_ball", _decode_boost_ball),
    0x39CF6E72: ("morph_into_ball", _decode_morph_into_ball),
    0x64003596: ("morph_from_ball", _decode_morph_from_ball),
}
