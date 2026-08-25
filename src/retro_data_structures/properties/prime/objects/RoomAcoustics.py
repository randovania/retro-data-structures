# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class RoomAcousticsJson(typing_extensions.TypedDict):
        name: str
        active: bool
        vol_scale: int
        rev_hi: bool
        rev_hi_dis: bool
        rev_hi_coloration: float
        rev_hi_mix: float
        rev_hi_time: float
        rev_hi_damping: float
        rev_hi_pre_delay: float
        rev_hi_crosstalk: float
        chorus: bool
        base_delay: float
        variation: float
        period: float
        rev_std: bool
        rev_std_dis: bool
        rev_std_coloration: float
        rev_std_mix: float
        rev_std_time: float
        rev_std_damping: float
        rev_std_pre_delay: float
        delay: bool
        delay_l: int
        delay_r: int
        delay_s: int
        feedback_l: int
        feedback_r: int
        feedback_s: int
        output_l: int
        output_r: int
        output_s: int


@dataclasses.dataclass()
class RoomAcoustics(BaseObjectType):
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="Active"),
        },
    )
    vol_scale: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="VolScale"),
        },
    )
    rev_hi: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000003, original_name="RevHi"),
        },
    )
    rev_hi_dis: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000004, original_name="RevHiDis"),
        },
    )
    rev_hi_coloration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="RevHiColoration"),
        },
    )
    rev_hi_mix: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="RevHiMix"),
        },
    )
    rev_hi_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="RevHiTime"),
        },
    )
    rev_hi_damping: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000008, original_name="RevHiDamping"),
        },
    )
    rev_hi_pre_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000009, original_name="RevHiPreDelay"),
        },
    )
    rev_hi_crosstalk: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000A, original_name="RevHiCrosstalk"),
        },
    )
    chorus: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000B, original_name="Chorus"),
        },
    )
    base_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000C, original_name="BaseDelay"),
        },
    )
    variation: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000D, original_name="Variation"),
        },
    )
    period: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000E, original_name="Period"),
        },
    )
    rev_std: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000F, original_name="RevStd"),
        },
    )
    rev_std_dis: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000010, original_name="RevStdDis"),
        },
    )
    rev_std_coloration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000011, original_name="RevStdColoration"),
        },
    )
    rev_std_mix: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000012, original_name="RevStdMix"),
        },
    )
    rev_std_time: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000013, original_name="RevStdTime"),
        },
    )
    rev_std_damping: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000014, original_name="RevStdDamping"),
        },
    )
    rev_std_pre_delay: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000015, original_name="RevStdPreDelay"),
        },
    )
    delay: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000016, original_name="Delay"),
        },
    )
    delay_l: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000017, original_name="DelayL"),
        },
    )
    delay_r: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000018, original_name="DelayR"),
        },
    )
    delay_s: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000019, original_name="DelayS"),
        },
    )
    feedback_l: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001A, original_name="FeedbackL"),
        },
    )
    feedback_r: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001B, original_name="FeedbackR"),
        },
    )
    feedback_s: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001C, original_name="FeedbackS"),
        },
    )
    output_l: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001D, original_name="OutputL"),
        },
    )
    output_r: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001E, original_name="OutputR"),
        },
    )
    output_s: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000001F, original_name="OutputS"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x5D

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        vol_scale = structs.BIG_l.unpack(data.read(4))[0]
        rev_hi = structs.BIG_bool_.unpack(data.read(1))[0]
        rev_hi_dis = structs.BIG_bool_.unpack(data.read(1))[0]
        rev_hi_coloration = structs.BIG_f.unpack(data.read(4))[0]
        rev_hi_mix = structs.BIG_f.unpack(data.read(4))[0]
        rev_hi_time = structs.BIG_f.unpack(data.read(4))[0]
        rev_hi_damping = structs.BIG_f.unpack(data.read(4))[0]
        rev_hi_pre_delay = structs.BIG_f.unpack(data.read(4))[0]
        rev_hi_crosstalk = structs.BIG_f.unpack(data.read(4))[0]
        chorus = structs.BIG_bool_.unpack(data.read(1))[0]
        base_delay = structs.BIG_f.unpack(data.read(4))[0]
        variation = structs.BIG_f.unpack(data.read(4))[0]
        period = structs.BIG_f.unpack(data.read(4))[0]
        rev_std = structs.BIG_bool_.unpack(data.read(1))[0]
        rev_std_dis = structs.BIG_bool_.unpack(data.read(1))[0]
        rev_std_coloration = structs.BIG_f.unpack(data.read(4))[0]
        rev_std_mix = structs.BIG_f.unpack(data.read(4))[0]
        rev_std_time = structs.BIG_f.unpack(data.read(4))[0]
        rev_std_damping = structs.BIG_f.unpack(data.read(4))[0]
        rev_std_pre_delay = structs.BIG_f.unpack(data.read(4))[0]
        delay = structs.BIG_bool_.unpack(data.read(1))[0]
        delay_l = structs.BIG_l.unpack(data.read(4))[0]
        delay_r = structs.BIG_l.unpack(data.read(4))[0]
        delay_s = structs.BIG_l.unpack(data.read(4))[0]
        feedback_l = structs.BIG_l.unpack(data.read(4))[0]
        feedback_r = structs.BIG_l.unpack(data.read(4))[0]
        feedback_s = structs.BIG_l.unpack(data.read(4))[0]
        output_l = structs.BIG_l.unpack(data.read(4))[0]
        output_r = structs.BIG_l.unpack(data.read(4))[0]
        output_s = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            active,
            vol_scale,
            rev_hi,
            rev_hi_dis,
            rev_hi_coloration,
            rev_hi_mix,
            rev_hi_time,
            rev_hi_damping,
            rev_hi_pre_delay,
            rev_hi_crosstalk,
            chorus,
            base_delay,
            variation,
            period,
            rev_std,
            rev_std_dis,
            rev_std_coloration,
            rev_std_mix,
            rev_std_time,
            rev_std_damping,
            rev_std_pre_delay,
            delay,
            delay_l,
            delay_r,
            delay_s,
            feedback_l,
            feedback_r,
            feedback_s,
            output_l,
            output_r,
            output_s,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00 ")  # 32 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_l.pack(self.vol_scale))
        data.write(structs.BIG_bool_.pack(self.rev_hi))
        data.write(structs.BIG_bool_.pack(self.rev_hi_dis))
        data.write(structs.BIG_f.pack(self.rev_hi_coloration))
        data.write(structs.BIG_f.pack(self.rev_hi_mix))
        data.write(structs.BIG_f.pack(self.rev_hi_time))
        data.write(structs.BIG_f.pack(self.rev_hi_damping))
        data.write(structs.BIG_f.pack(self.rev_hi_pre_delay))
        data.write(structs.BIG_f.pack(self.rev_hi_crosstalk))
        data.write(structs.BIG_bool_.pack(self.chorus))
        data.write(structs.BIG_f.pack(self.base_delay))
        data.write(structs.BIG_f.pack(self.variation))
        data.write(structs.BIG_f.pack(self.period))
        data.write(structs.BIG_bool_.pack(self.rev_std))
        data.write(structs.BIG_bool_.pack(self.rev_std_dis))
        data.write(structs.BIG_f.pack(self.rev_std_coloration))
        data.write(structs.BIG_f.pack(self.rev_std_mix))
        data.write(structs.BIG_f.pack(self.rev_std_time))
        data.write(structs.BIG_f.pack(self.rev_std_damping))
        data.write(structs.BIG_f.pack(self.rev_std_pre_delay))
        data.write(structs.BIG_bool_.pack(self.delay))
        data.write(structs.BIG_l.pack(self.delay_l))
        data.write(structs.BIG_l.pack(self.delay_r))
        data.write(structs.BIG_l.pack(self.delay_s))
        data.write(structs.BIG_l.pack(self.feedback_l))
        data.write(structs.BIG_l.pack(self.feedback_r))
        data.write(structs.BIG_l.pack(self.feedback_s))
        data.write(structs.BIG_l.pack(self.output_l))
        data.write(structs.BIG_l.pack(self.output_r))
        data.write(structs.BIG_l.pack(self.output_s))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RoomAcousticsJson", data)
        return cls(
            name=json_data["name"],
            active=json_data["active"],
            vol_scale=json_data["vol_scale"],
            rev_hi=json_data["rev_hi"],
            rev_hi_dis=json_data["rev_hi_dis"],
            rev_hi_coloration=json_data["rev_hi_coloration"],
            rev_hi_mix=json_data["rev_hi_mix"],
            rev_hi_time=json_data["rev_hi_time"],
            rev_hi_damping=json_data["rev_hi_damping"],
            rev_hi_pre_delay=json_data["rev_hi_pre_delay"],
            rev_hi_crosstalk=json_data["rev_hi_crosstalk"],
            chorus=json_data["chorus"],
            base_delay=json_data["base_delay"],
            variation=json_data["variation"],
            period=json_data["period"],
            rev_std=json_data["rev_std"],
            rev_std_dis=json_data["rev_std_dis"],
            rev_std_coloration=json_data["rev_std_coloration"],
            rev_std_mix=json_data["rev_std_mix"],
            rev_std_time=json_data["rev_std_time"],
            rev_std_damping=json_data["rev_std_damping"],
            rev_std_pre_delay=json_data["rev_std_pre_delay"],
            delay=json_data["delay"],
            delay_l=json_data["delay_l"],
            delay_r=json_data["delay_r"],
            delay_s=json_data["delay_s"],
            feedback_l=json_data["feedback_l"],
            feedback_r=json_data["feedback_r"],
            feedback_s=json_data["feedback_s"],
            output_l=json_data["output_l"],
            output_r=json_data["output_r"],
            output_s=json_data["output_s"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "active": self.active,
            "vol_scale": self.vol_scale,
            "rev_hi": self.rev_hi,
            "rev_hi_dis": self.rev_hi_dis,
            "rev_hi_coloration": self.rev_hi_coloration,
            "rev_hi_mix": self.rev_hi_mix,
            "rev_hi_time": self.rev_hi_time,
            "rev_hi_damping": self.rev_hi_damping,
            "rev_hi_pre_delay": self.rev_hi_pre_delay,
            "rev_hi_crosstalk": self.rev_hi_crosstalk,
            "chorus": self.chorus,
            "base_delay": self.base_delay,
            "variation": self.variation,
            "period": self.period,
            "rev_std": self.rev_std,
            "rev_std_dis": self.rev_std_dis,
            "rev_std_coloration": self.rev_std_coloration,
            "rev_std_mix": self.rev_std_mix,
            "rev_std_time": self.rev_std_time,
            "rev_std_damping": self.rev_std_damping,
            "rev_std_pre_delay": self.rev_std_pre_delay,
            "delay": self.delay,
            "delay_l": self.delay_l,
            "delay_r": self.delay_r,
            "delay_s": self.delay_s,
            "feedback_l": self.feedback_l,
            "feedback_r": self.feedback_r,
            "feedback_s": self.feedback_s,
            "output_l": self.output_l,
            "output_r": self.output_r,
            "output_s": self.output_s,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []
