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
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class RoomAcousticsJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        room_volume: int
        priority: int
        reverb_hi_enabled: bool
        unknown_0x3263c26e: bool
        reverb_hi_time: float
        reverb_hi_pre_delay: float
        reverb_hi_damping: float
        reverb_hi_coloration: float
        reverb_hi_cross_talk: float
        reverb_hi_mix: float
        chorus_enabled: bool
        chorus_base_delay: float
        chorus_variation: float
        chorus_period: float
        reverb_std_enabled: bool
        unknown_0x4a5bbf90: bool
        reverb_std_time: float
        reverb_std_pre_delay: float
        reverb_std_damping: float
        reverb_std_coloration: float
        reverb_std_mix: float
        delay_enabled: bool
        delay0: int
        delay1: int
        delay2: int
        delay_feedback0: int
        delay_feedback1: int
        delay_feedback2: int
        delay_output0: int
        delay_output1: int
        delay_output2: int
        unknown_0xcf45711c: int
        unknown_0x626d1e9b: int
        unknown_0x7d8ee273: bool
        unknown_0x83378e6a: float
        unknown_0xf549d269: float
        unknown_0x11fdae16: float
        unknown_0xa3c439c1: float
        unknown_0x2dc70efe: float
        unknown_0xe2bd3706: float
        unknown_0x5e29cef8: float
        unknown_0x35ae9f10: float
        bitcrusher_enabled: bool
        unknown_0xf51a1d6a: int
        bitcrusher_gain: float
        bitcrusher_bit_depth: int
        unknown_0x58096e0b: float
        phaser_enabled: bool
        phaser_frequency: float
        phaser_feedback: float
        phaser_invert: float
        phaser_mix: float
        phaser_sweep: float


@dataclasses.dataclass()
class RoomAcoustics(BaseObjectType):
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
    room_volume: int = dataclasses.field(
        default=117,
        metadata={
            "reflection": FieldReflection[int](int, id=0xBD9EA266, original_name="RoomVolume"),
        },
    )
    priority: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x86CF23F4, original_name="Priority"),
        },
    )  # Choice
    reverb_hi_enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA00360CC, original_name="ReverbHiEnabled"),
        },
    )
    unknown_0x3263c26e: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3263C26E, original_name="Unknown"),
        },
    )
    reverb_hi_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC5868061, original_name="ReverbHiTime"),
        },
    )
    reverb_hi_pre_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6F50032, original_name="ReverbHiPreDelay"),
        },
    )
    reverb_hi_damping: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCBA5555D, original_name="ReverbHiDamping"),
        },
    )
    reverb_hi_coloration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7319CF50, original_name="ReverbHiColoration"),
        },
    )
    reverb_hi_cross_talk: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3DC3F16F, original_name="ReverbHiCrossTalk"),
        },
    )
    reverb_hi_mix: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5518B6C, original_name="ReverbHiMix"),
        },
    )
    chorus_enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x26997CCB, original_name="ChorusEnabled"),
        },
    )
    chorus_base_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x121BDFAD, original_name="ChorusBaseDelay"),
        },
    )
    chorus_variation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE8796BCE, original_name="ChorusVariation"),
        },
    )
    chorus_period: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24BBD5E4, original_name="ChorusPeriod"),
        },
    )
    reverb_std_enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFF31631B, original_name="ReverbStdEnabled"),
        },
    )
    unknown_0x4a5bbf90: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4A5BBF90, original_name="Unknown"),
        },
    )
    reverb_std_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9662498A, original_name="ReverbStdTime"),
        },
    )
    reverb_std_pre_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x91855D62, original_name="ReverbStdPreDelay"),
        },
    )
    reverb_std_damping: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD34D2029, original_name="ReverbStdDamping"),
        },
    )
    reverb_std_coloration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC78E83D, original_name="ReverbStdColoration"),
        },
    )
    reverb_std_mix: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x820B509E, original_name="ReverbStdMix"),
        },
    )
    delay_enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE9A36031, original_name="DelayEnabled"),
        },
    )
    delay0: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x62C49457, original_name="Delay0"),
        },
    )
    delay1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDA78F332, original_name="Delay1"),
        },
    )
    delay2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC8CD5CDC, original_name="Delay2"),
        },
    )
    delay_feedback0: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7C14FF17, original_name="DelayFeedback0"),
        },
    )
    delay_feedback1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC4A89872, original_name="DelayFeedback1"),
        },
    )
    delay_feedback2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD61D379C, original_name="DelayFeedback2"),
        },
    )
    delay_output0: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9F75987F, original_name="DelayOutput0"),
        },
    )
    delay_output1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x27C9FF1A, original_name="DelayOutput1"),
        },
    )
    delay_output2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x357C50F4, original_name="DelayOutput2"),
        },
    )
    unknown_0xcf45711c: int = dataclasses.field(
        default=32000,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCF45711C, original_name="Unknown"),
        },
    )
    unknown_0x626d1e9b: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x626D1E9B, original_name="Unknown"),
        },
    )
    unknown_0x7d8ee273: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7D8EE273, original_name="Unknown"),
        },
    )
    unknown_0x83378e6a: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x83378E6A, original_name="Unknown"),
        },
    )
    unknown_0xf549d269: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF549D269, original_name="Unknown"),
        },
    )
    unknown_0x11fdae16: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x11FDAE16, original_name="Unknown"),
        },
    )
    unknown_0xa3c439c1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA3C439C1, original_name="Unknown"),
        },
    )
    unknown_0x2dc70efe: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DC70EFE, original_name="Unknown"),
        },
    )
    unknown_0xe2bd3706: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE2BD3706, original_name="Unknown"),
        },
    )
    unknown_0x5e29cef8: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5E29CEF8, original_name="Unknown"),
        },
    )
    unknown_0x35ae9f10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x35AE9F10, original_name="Unknown"),
        },
    )
    bitcrusher_enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3E8D8694, original_name="BitcrusherEnabled"),
        },
    )
    unknown_0xf51a1d6a: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF51A1D6A, original_name="Unknown"),
        },
    )
    bitcrusher_gain: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBB1A0F34, original_name="BitcrusherGain"),
        },
    )
    bitcrusher_bit_depth: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEB009039, original_name="BitcrusherBitDepth"),
        },
    )
    unknown_0x58096e0b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x58096E0B, original_name="Unknown"),
        },
    )
    phaser_enabled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3D8CAD84, original_name="PhaserEnabled"),
        },
    )
    phaser_frequency: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23C340F6, original_name="PhaserFrequency"),
        },
    )
    phaser_feedback: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E5A52B8, original_name="PhaserFeedback"),
        },
    )
    phaser_invert: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1D69BEC4, original_name="PhaserInvert"),
        },
    )
    phaser_mix: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24538C4A, original_name="PhaserMix"),
        },
    )
    phaser_sweep: float = dataclasses.field(
        default=200.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD5388116, original_name="PhaserSweep"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "RMAC"

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
        if property_count != 54:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD9EA266
        room_volume = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86CF23F4
        priority = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA00360CC
        reverb_hi_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3263C26E
        unknown_0x3263c26e = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5868061
        reverb_hi_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6F50032
        reverb_hi_pre_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCBA5555D
        reverb_hi_damping = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7319CF50
        reverb_hi_coloration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DC3F16F
        reverb_hi_cross_talk = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5518B6C
        reverb_hi_mix = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26997CCB
        chorus_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x121BDFAD
        chorus_base_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8796BCE
        chorus_variation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24BBD5E4
        chorus_period = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF31631B
        reverb_std_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A5BBF90
        unknown_0x4a5bbf90 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9662498A
        reverb_std_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91855D62
        reverb_std_pre_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD34D2029
        reverb_std_damping = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC78E83D
        reverb_std_coloration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x820B509E
        reverb_std_mix = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9A36031
        delay_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62C49457
        delay0 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDA78F332
        delay1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC8CD5CDC
        delay2 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7C14FF17
        delay_feedback0 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4A89872
        delay_feedback1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD61D379C
        delay_feedback2 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F75987F
        delay_output0 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27C9FF1A
        delay_output1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x357C50F4
        delay_output2 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF45711C
        unknown_0xcf45711c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x626D1E9B
        unknown_0x626d1e9b = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D8EE273
        unknown_0x7d8ee273 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83378E6A
        unknown_0x83378e6a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF549D269
        unknown_0xf549d269 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11FDAE16
        unknown_0x11fdae16 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA3C439C1
        unknown_0xa3c439c1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DC70EFE
        unknown_0x2dc70efe = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2BD3706
        unknown_0xe2bd3706 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5E29CEF8
        unknown_0x5e29cef8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35AE9F10
        unknown_0x35ae9f10 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E8D8694
        bitcrusher_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF51A1D6A
        unknown_0xf51a1d6a = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB1A0F34
        bitcrusher_gain = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB009039
        bitcrusher_bit_depth = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58096E0B
        unknown_0x58096e0b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3D8CAD84
        phaser_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23C340F6
        phaser_frequency = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E5A52B8
        phaser_feedback = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D69BEC4
        phaser_invert = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24538C4A
        phaser_mix = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5388116
        phaser_sweep = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            room_volume,
            priority,
            reverb_hi_enabled,
            unknown_0x3263c26e,
            reverb_hi_time,
            reverb_hi_pre_delay,
            reverb_hi_damping,
            reverb_hi_coloration,
            reverb_hi_cross_talk,
            reverb_hi_mix,
            chorus_enabled,
            chorus_base_delay,
            chorus_variation,
            chorus_period,
            reverb_std_enabled,
            unknown_0x4a5bbf90,
            reverb_std_time,
            reverb_std_pre_delay,
            reverb_std_damping,
            reverb_std_coloration,
            reverb_std_mix,
            delay_enabled,
            delay0,
            delay1,
            delay2,
            delay_feedback0,
            delay_feedback1,
            delay_feedback2,
            delay_output0,
            delay_output1,
            delay_output2,
            unknown_0xcf45711c,
            unknown_0x626d1e9b,
            unknown_0x7d8ee273,
            unknown_0x83378e6a,
            unknown_0xf549d269,
            unknown_0x11fdae16,
            unknown_0xa3c439c1,
            unknown_0x2dc70efe,
            unknown_0xe2bd3706,
            unknown_0x5e29cef8,
            unknown_0x35ae9f10,
            bitcrusher_enabled,
            unknown_0xf51a1d6a,
            bitcrusher_gain,
            bitcrusher_bit_depth,
            unknown_0x58096e0b,
            phaser_enabled,
            phaser_frequency,
            phaser_feedback,
            phaser_invert,
            phaser_mix,
            phaser_sweep,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x006")  # 54 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbd\x9e\xa2f")  # 0xbd9ea266
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.room_volume))

        data.write(b"\x86\xcf#\xf4")  # 0x86cf23f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.priority))

        data.write(b"\xa0\x03`\xcc")  # 0xa00360cc
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.reverb_hi_enabled))

        data.write(b"2c\xc2n")  # 0x3263c26e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3263c26e))

        data.write(b"\xc5\x86\x80a")  # 0xc5868061
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_time))

        data.write(b"\xc6\xf5\x002")  # 0xc6f50032
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_pre_delay))

        data.write(b"\xcb\xa5U]")  # 0xcba5555d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_damping))

        data.write(b"s\x19\xcfP")  # 0x7319cf50
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_coloration))

        data.write(b"=\xc3\xf1o")  # 0x3dc3f16f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_cross_talk))

        data.write(b"\xd5Q\x8bl")  # 0xd5518b6c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_mix))

        data.write(b"&\x99|\xcb")  # 0x26997ccb
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.chorus_enabled))

        data.write(b"\x12\x1b\xdf\xad")  # 0x121bdfad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.chorus_base_delay))

        data.write(b"\xe8yk\xce")  # 0xe8796bce
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.chorus_variation))

        data.write(b"$\xbb\xd5\xe4")  # 0x24bbd5e4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.chorus_period))

        data.write(b"\xff1c\x1b")  # 0xff31631b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.reverb_std_enabled))

        data.write(b"J[\xbf\x90")  # 0x4a5bbf90
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4a5bbf90))

        data.write(b"\x96bI\x8a")  # 0x9662498a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_std_time))

        data.write(b"\x91\x85]b")  # 0x91855d62
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_std_pre_delay))

        data.write(b"\xd3M )")  # 0xd34d2029
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_std_damping))

        data.write(b"\xdcx\xe8=")  # 0xdc78e83d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_std_coloration))

        data.write(b"\x82\x0bP\x9e")  # 0x820b509e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.reverb_std_mix))

        data.write(b"\xe9\xa3`1")  # 0xe9a36031
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.delay_enabled))

        data.write(b"b\xc4\x94W")  # 0x62c49457
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay0))

        data.write(b"\xdax\xf32")  # 0xda78f332
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay1))

        data.write(b"\xc8\xcd\\\xdc")  # 0xc8cd5cdc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay2))

        data.write(b"|\x14\xff\x17")  # 0x7c14ff17
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay_feedback0))

        data.write(b"\xc4\xa8\x98r")  # 0xc4a89872
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay_feedback1))

        data.write(b"\xd6\x1d7\x9c")  # 0xd61d379c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay_feedback2))

        data.write(b"\x9fu\x98\x7f")  # 0x9f75987f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay_output0))

        data.write(b"'\xc9\xff\x1a")  # 0x27c9ff1a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay_output1))

        data.write(b"5|P\xf4")  # 0x357c50f4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.delay_output2))

        data.write(b"\xcfEq\x1c")  # 0xcf45711c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xcf45711c))

        data.write(b"bm\x1e\x9b")  # 0x626d1e9b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x626d1e9b))

        data.write(b"}\x8e\xe2s")  # 0x7d8ee273
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7d8ee273))

        data.write(b"\x837\x8ej")  # 0x83378e6a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x83378e6a))

        data.write(b"\xf5I\xd2i")  # 0xf549d269
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf549d269))

        data.write(b"\x11\xfd\xae\x16")  # 0x11fdae16
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x11fdae16))

        data.write(b"\xa3\xc49\xc1")  # 0xa3c439c1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa3c439c1))

        data.write(b"-\xc7\x0e\xfe")  # 0x2dc70efe
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2dc70efe))

        data.write(b"\xe2\xbd7\x06")  # 0xe2bd3706
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe2bd3706))

        data.write(b"^)\xce\xf8")  # 0x5e29cef8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5e29cef8))

        data.write(b"5\xae\x9f\x10")  # 0x35ae9f10
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x35ae9f10))

        data.write(b">\x8d\x86\x94")  # 0x3e8d8694
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.bitcrusher_enabled))

        data.write(b"\xf5\x1a\x1dj")  # 0xf51a1d6a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xf51a1d6a))

        data.write(b"\xbb\x1a\x0f4")  # 0xbb1a0f34
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bitcrusher_gain))

        data.write(b"\xeb\x00\x909")  # 0xeb009039
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.bitcrusher_bit_depth))

        data.write(b"X\tn\x0b")  # 0x58096e0b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x58096e0b))

        data.write(b"=\x8c\xad\x84")  # 0x3d8cad84
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.phaser_enabled))

        data.write(b"#\xc3@\xf6")  # 0x23c340f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phaser_frequency))

        data.write(b"\x1eZR\xb8")  # 0x1e5a52b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phaser_feedback))

        data.write(b"\x1di\xbe\xc4")  # 0x1d69bec4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phaser_invert))

        data.write(b"$S\x8cJ")  # 0x24538c4a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phaser_mix))

        data.write(b"\xd58\x81\x16")  # 0xd5388116
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phaser_sweep))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RoomAcousticsJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            room_volume=json_data["room_volume"],
            priority=json_data["priority"],
            reverb_hi_enabled=json_data["reverb_hi_enabled"],
            unknown_0x3263c26e=json_data["unknown_0x3263c26e"],
            reverb_hi_time=json_data["reverb_hi_time"],
            reverb_hi_pre_delay=json_data["reverb_hi_pre_delay"],
            reverb_hi_damping=json_data["reverb_hi_damping"],
            reverb_hi_coloration=json_data["reverb_hi_coloration"],
            reverb_hi_cross_talk=json_data["reverb_hi_cross_talk"],
            reverb_hi_mix=json_data["reverb_hi_mix"],
            chorus_enabled=json_data["chorus_enabled"],
            chorus_base_delay=json_data["chorus_base_delay"],
            chorus_variation=json_data["chorus_variation"],
            chorus_period=json_data["chorus_period"],
            reverb_std_enabled=json_data["reverb_std_enabled"],
            unknown_0x4a5bbf90=json_data["unknown_0x4a5bbf90"],
            reverb_std_time=json_data["reverb_std_time"],
            reverb_std_pre_delay=json_data["reverb_std_pre_delay"],
            reverb_std_damping=json_data["reverb_std_damping"],
            reverb_std_coloration=json_data["reverb_std_coloration"],
            reverb_std_mix=json_data["reverb_std_mix"],
            delay_enabled=json_data["delay_enabled"],
            delay0=json_data["delay0"],
            delay1=json_data["delay1"],
            delay2=json_data["delay2"],
            delay_feedback0=json_data["delay_feedback0"],
            delay_feedback1=json_data["delay_feedback1"],
            delay_feedback2=json_data["delay_feedback2"],
            delay_output0=json_data["delay_output0"],
            delay_output1=json_data["delay_output1"],
            delay_output2=json_data["delay_output2"],
            unknown_0xcf45711c=json_data["unknown_0xcf45711c"],
            unknown_0x626d1e9b=json_data["unknown_0x626d1e9b"],
            unknown_0x7d8ee273=json_data["unknown_0x7d8ee273"],
            unknown_0x83378e6a=json_data["unknown_0x83378e6a"],
            unknown_0xf549d269=json_data["unknown_0xf549d269"],
            unknown_0x11fdae16=json_data["unknown_0x11fdae16"],
            unknown_0xa3c439c1=json_data["unknown_0xa3c439c1"],
            unknown_0x2dc70efe=json_data["unknown_0x2dc70efe"],
            unknown_0xe2bd3706=json_data["unknown_0xe2bd3706"],
            unknown_0x5e29cef8=json_data["unknown_0x5e29cef8"],
            unknown_0x35ae9f10=json_data["unknown_0x35ae9f10"],
            bitcrusher_enabled=json_data["bitcrusher_enabled"],
            unknown_0xf51a1d6a=json_data["unknown_0xf51a1d6a"],
            bitcrusher_gain=json_data["bitcrusher_gain"],
            bitcrusher_bit_depth=json_data["bitcrusher_bit_depth"],
            unknown_0x58096e0b=json_data["unknown_0x58096e0b"],
            phaser_enabled=json_data["phaser_enabled"],
            phaser_frequency=json_data["phaser_frequency"],
            phaser_feedback=json_data["phaser_feedback"],
            phaser_invert=json_data["phaser_invert"],
            phaser_mix=json_data["phaser_mix"],
            phaser_sweep=json_data["phaser_sweep"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "room_volume": self.room_volume,
            "priority": self.priority,
            "reverb_hi_enabled": self.reverb_hi_enabled,
            "unknown_0x3263c26e": self.unknown_0x3263c26e,
            "reverb_hi_time": self.reverb_hi_time,
            "reverb_hi_pre_delay": self.reverb_hi_pre_delay,
            "reverb_hi_damping": self.reverb_hi_damping,
            "reverb_hi_coloration": self.reverb_hi_coloration,
            "reverb_hi_cross_talk": self.reverb_hi_cross_talk,
            "reverb_hi_mix": self.reverb_hi_mix,
            "chorus_enabled": self.chorus_enabled,
            "chorus_base_delay": self.chorus_base_delay,
            "chorus_variation": self.chorus_variation,
            "chorus_period": self.chorus_period,
            "reverb_std_enabled": self.reverb_std_enabled,
            "unknown_0x4a5bbf90": self.unknown_0x4a5bbf90,
            "reverb_std_time": self.reverb_std_time,
            "reverb_std_pre_delay": self.reverb_std_pre_delay,
            "reverb_std_damping": self.reverb_std_damping,
            "reverb_std_coloration": self.reverb_std_coloration,
            "reverb_std_mix": self.reverb_std_mix,
            "delay_enabled": self.delay_enabled,
            "delay0": self.delay0,
            "delay1": self.delay1,
            "delay2": self.delay2,
            "delay_feedback0": self.delay_feedback0,
            "delay_feedback1": self.delay_feedback1,
            "delay_feedback2": self.delay_feedback2,
            "delay_output0": self.delay_output0,
            "delay_output1": self.delay_output1,
            "delay_output2": self.delay_output2,
            "unknown_0xcf45711c": self.unknown_0xcf45711c,
            "unknown_0x626d1e9b": self.unknown_0x626d1e9b,
            "unknown_0x7d8ee273": self.unknown_0x7d8ee273,
            "unknown_0x83378e6a": self.unknown_0x83378e6a,
            "unknown_0xf549d269": self.unknown_0xf549d269,
            "unknown_0x11fdae16": self.unknown_0x11fdae16,
            "unknown_0xa3c439c1": self.unknown_0xa3c439c1,
            "unknown_0x2dc70efe": self.unknown_0x2dc70efe,
            "unknown_0xe2bd3706": self.unknown_0xe2bd3706,
            "unknown_0x5e29cef8": self.unknown_0x5e29cef8,
            "unknown_0x35ae9f10": self.unknown_0x35ae9f10,
            "bitcrusher_enabled": self.bitcrusher_enabled,
            "unknown_0xf51a1d6a": self.unknown_0xf51a1d6a,
            "bitcrusher_gain": self.bitcrusher_gain,
            "bitcrusher_bit_depth": self.bitcrusher_bit_depth,
            "unknown_0x58096e0b": self.unknown_0x58096e0b,
            "phaser_enabled": self.phaser_enabled,
            "phaser_frequency": self.phaser_frequency,
            "phaser_feedback": self.phaser_feedback,
            "phaser_invert": self.phaser_invert,
            "phaser_mix": self.phaser_mix,
            "phaser_sweep": self.phaser_sweep,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xBD9EA266: ("room_volume", structs.decode_BIG_l),
    0x86CF23F4: ("priority", structs.decode_BIG_L),
    0xA00360CC: ("reverb_hi_enabled", structs.decode_BIG_bool_),
    0x3263C26E: ("unknown_0x3263c26e", structs.decode_BIG_bool_),
    0xC5868061: ("reverb_hi_time", structs.decode_BIG_f),
    0xC6F50032: ("reverb_hi_pre_delay", structs.decode_BIG_f),
    0xCBA5555D: ("reverb_hi_damping", structs.decode_BIG_f),
    0x7319CF50: ("reverb_hi_coloration", structs.decode_BIG_f),
    0x3DC3F16F: ("reverb_hi_cross_talk", structs.decode_BIG_f),
    0xD5518B6C: ("reverb_hi_mix", structs.decode_BIG_f),
    0x26997CCB: ("chorus_enabled", structs.decode_BIG_bool_),
    0x121BDFAD: ("chorus_base_delay", structs.decode_BIG_f),
    0xE8796BCE: ("chorus_variation", structs.decode_BIG_f),
    0x24BBD5E4: ("chorus_period", structs.decode_BIG_f),
    0xFF31631B: ("reverb_std_enabled", structs.decode_BIG_bool_),
    0x4A5BBF90: ("unknown_0x4a5bbf90", structs.decode_BIG_bool_),
    0x9662498A: ("reverb_std_time", structs.decode_BIG_f),
    0x91855D62: ("reverb_std_pre_delay", structs.decode_BIG_f),
    0xD34D2029: ("reverb_std_damping", structs.decode_BIG_f),
    0xDC78E83D: ("reverb_std_coloration", structs.decode_BIG_f),
    0x820B509E: ("reverb_std_mix", structs.decode_BIG_f),
    0xE9A36031: ("delay_enabled", structs.decode_BIG_bool_),
    0x62C49457: ("delay0", structs.decode_BIG_l),
    0xDA78F332: ("delay1", structs.decode_BIG_l),
    0xC8CD5CDC: ("delay2", structs.decode_BIG_l),
    0x7C14FF17: ("delay_feedback0", structs.decode_BIG_l),
    0xC4A89872: ("delay_feedback1", structs.decode_BIG_l),
    0xD61D379C: ("delay_feedback2", structs.decode_BIG_l),
    0x9F75987F: ("delay_output0", structs.decode_BIG_l),
    0x27C9FF1A: ("delay_output1", structs.decode_BIG_l),
    0x357C50F4: ("delay_output2", structs.decode_BIG_l),
    0xCF45711C: ("unknown_0xcf45711c", structs.decode_BIG_l),
    0x626D1E9B: ("unknown_0x626d1e9b", structs.decode_BIG_l),
    0x7D8EE273: ("unknown_0x7d8ee273", structs.decode_BIG_bool_),
    0x83378E6A: ("unknown_0x83378e6a", structs.decode_BIG_f),
    0xF549D269: ("unknown_0xf549d269", structs.decode_BIG_f),
    0x11FDAE16: ("unknown_0x11fdae16", structs.decode_BIG_f),
    0xA3C439C1: ("unknown_0xa3c439c1", structs.decode_BIG_f),
    0x2DC70EFE: ("unknown_0x2dc70efe", structs.decode_BIG_f),
    0xE2BD3706: ("unknown_0xe2bd3706", structs.decode_BIG_f),
    0x5E29CEF8: ("unknown_0x5e29cef8", structs.decode_BIG_f),
    0x35AE9F10: ("unknown_0x35ae9f10", structs.decode_BIG_f),
    0x3E8D8694: ("bitcrusher_enabled", structs.decode_BIG_bool_),
    0xF51A1D6A: ("unknown_0xf51a1d6a", structs.decode_BIG_l),
    0xBB1A0F34: ("bitcrusher_gain", structs.decode_BIG_f),
    0xEB009039: ("bitcrusher_bit_depth", structs.decode_BIG_l),
    0x58096E0B: ("unknown_0x58096e0b", structs.decode_BIG_f),
    0x3D8CAD84: ("phaser_enabled", structs.decode_BIG_bool_),
    0x23C340F6: ("phaser_frequency", structs.decode_BIG_f),
    0x1E5A52B8: ("phaser_feedback", structs.decode_BIG_f),
    0x1D69BEC4: ("phaser_invert", structs.decode_BIG_f),
    0x24538C4A: ("phaser_mix", structs.decode_BIG_f),
    0xD5388116: ("phaser_sweep", structs.decode_BIG_f),
}
