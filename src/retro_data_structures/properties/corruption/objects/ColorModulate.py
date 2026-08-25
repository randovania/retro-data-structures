# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ColorModulateJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        color_a: json_util.JsonValue
        color_b: json_util.JsonValue
        blend_mode: int
        time_a2_b: float
        time_b2_a: float
        do_reverse: bool
        reset_target_when_done: bool
        depth_compare: bool
        depth_update: bool
        depth_backwards: bool
        auto_start: bool
        update_time: bool
        loop_forever: bool
        external_time: bool
        copy_model_color_to_color_a: bool
        write_depth_first: bool
        control_spline: json_util.JsonObject


class Blend_Mode(enum.IntEnum):
    Unknown1 = 3843753963
    Unknown2 = 4195520078
    Unknown3 = 2767891128
    Unknown4 = 3057539653
    Unknown5 = 3505979826
    Unknown6 = 188796281
    Unknown7 = 2832859382
    Unknown8 = 843861036
    Unknown9 = 144217437
    Unknown10 = 2495447389
    Unknown11 = 2676901319

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
class ColorModulate(BaseObjectType):
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
    color_a: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xD6A3D26F, original_name="Color_A", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    color_b: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x5037A0C1, original_name="Color_B", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    blend_mode: Blend_Mode = dataclasses.field(
        default=Blend_Mode.Unknown1,
        metadata={
            "reflection": FieldReflection[Blend_Mode](
                Blend_Mode,
                id=0xFF457546,
                original_name="Blend_Mode",
                from_json=Blend_Mode.from_json,
                to_json=Blend_Mode.to_json,
            ),
        },
    )
    time_a2_b: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AFA5C48, original_name="Time_A2B"),
        },
    )
    time_b2_a: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x12E12905, original_name="Time_B2A"),
        },
    )
    do_reverse: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCEC5244B, original_name="Do_Reverse"),
        },
    )
    reset_target_when_done: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x81FC979C, original_name="Reset_Target_When_Done"),
        },
    )
    depth_compare: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x94C01B0C, original_name="Depth_Compare"),
        },
    )
    depth_update: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAED25A51, original_name="Depth_Update"),
        },
    )
    depth_backwards: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x35DC43D0, original_name="Depth_Backwards"),
        },
    )
    auto_start: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3217DFF8, original_name="AutoStart"),
        },
    )
    update_time: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3A7F59F7, original_name="UpdateTime"),
        },
    )
    loop_forever: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x08BB73C5, original_name="LoopForever"),
        },
    )
    external_time: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7E379AE8, original_name="ExternalTime"),
        },
    )
    copy_model_color_to_color_a: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x74081E94, original_name="CopyModelColorToColorA"),
        },
    )
    write_depth_first: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9A306740, original_name="WriteDepthFirst"),
        },
    )
    control_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x15567FE7, original_name="ControlSpline", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "CLRM"

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
        if property_count != 18:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6A3D26F
        color_a = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5037A0C1
        color_b = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFF457546
        blend_mode = Blend_Mode.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AFA5C48
        time_a2_b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12E12905
        time_b2_a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEC5244B
        do_reverse = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81FC979C
        reset_target_when_done = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94C01B0C
        depth_compare = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAED25A51
        depth_update = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35DC43D0
        depth_backwards = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3217DFF8
        auto_start = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A7F59F7
        update_time = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08BB73C5
        loop_forever = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E379AE8
        external_time = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74081E94
        copy_model_color_to_color_a = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A306740
        write_depth_first = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15567FE7
        control_spline = Spline.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            color_a,
            color_b,
            blend_mode,
            time_a2_b,
            time_b2_a,
            do_reverse,
            reset_target_when_done,
            depth_compare,
            depth_update,
            depth_backwards,
            auto_start,
            update_time,
            loop_forever,
            external_time,
            copy_model_color_to_color_a,
            write_depth_first,
            control_spline,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x12")  # 18 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd6\xa3\xd2o")  # 0xd6a3d26f
        data.write(b"\x00\x10")  # size
        self.color_a.to_stream(data, game)

        data.write(b"P7\xa0\xc1")  # 0x5037a0c1
        data.write(b"\x00\x10")  # size
        self.color_b.to_stream(data, game)

        data.write(b"\xffEuF")  # 0xff457546
        data.write(b"\x00\x04")  # size
        self.blend_mode.to_stream(data, game)

        data.write(b"\x1a\xfa\\H")  # 0x1afa5c48
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_a2_b))

        data.write(b"\x12\xe1)\x05")  # 0x12e12905
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time_b2_a))

        data.write(b"\xce\xc5$K")  # 0xcec5244b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.do_reverse))

        data.write(b"\x81\xfc\x97\x9c")  # 0x81fc979c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.reset_target_when_done))

        data.write(b"\x94\xc0\x1b\x0c")  # 0x94c01b0c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.depth_compare))

        data.write(b"\xae\xd2ZQ")  # 0xaed25a51
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.depth_update))

        data.write(b"5\xdcC\xd0")  # 0x35dc43d0
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.depth_backwards))

        data.write(b"2\x17\xdf\xf8")  # 0x3217dff8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_start))

        data.write(b":\x7fY\xf7")  # 0x3a7f59f7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.update_time))

        data.write(b"\x08\xbbs\xc5")  # 0x8bb73c5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.loop_forever))

        data.write(b"~7\x9a\xe8")  # 0x7e379ae8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.external_time))

        data.write(b"t\x08\x1e\x94")  # 0x74081e94
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.copy_model_color_to_color_a))

        data.write(b"\x9a0g@")  # 0x9a306740
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.write_depth_first))

        data.write(b"\x15V\x7f\xe7")  # 0x15567fe7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.control_spline.to_stream(data, game)
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
        json_data = typing.cast("ColorModulateJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            color_a=Color.from_json(json_data["color_a"]),
            color_b=Color.from_json(json_data["color_b"]),
            blend_mode=Blend_Mode.from_json(json_data["blend_mode"]),
            time_a2_b=json_data["time_a2_b"],
            time_b2_a=json_data["time_b2_a"],
            do_reverse=json_data["do_reverse"],
            reset_target_when_done=json_data["reset_target_when_done"],
            depth_compare=json_data["depth_compare"],
            depth_update=json_data["depth_update"],
            depth_backwards=json_data["depth_backwards"],
            auto_start=json_data["auto_start"],
            update_time=json_data["update_time"],
            loop_forever=json_data["loop_forever"],
            external_time=json_data["external_time"],
            copy_model_color_to_color_a=json_data["copy_model_color_to_color_a"],
            write_depth_first=json_data["write_depth_first"],
            control_spline=Spline.from_json(json_data["control_spline"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "color_a": self.color_a.to_json(),
            "color_b": self.color_b.to_json(),
            "blend_mode": self.blend_mode.to_json(),
            "time_a2_b": self.time_a2_b,
            "time_b2_a": self.time_b2_a,
            "do_reverse": self.do_reverse,
            "reset_target_when_done": self.reset_target_when_done,
            "depth_compare": self.depth_compare,
            "depth_update": self.depth_update,
            "depth_backwards": self.depth_backwards,
            "auto_start": self.auto_start,
            "update_time": self.update_time,
            "loop_forever": self.loop_forever,
            "external_time": self.external_time,
            "copy_model_color_to_color_a": self.copy_model_color_to_color_a,
            "write_depth_first": self.write_depth_first,
            "control_spline": self.control_spline.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_color_a(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_b(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_blend_mode(data: typing.BinaryIO, game: Game, property_size: int) -> Blend_Mode:
    return Blend_Mode.from_stream(data, game)


def _decode_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xD6A3D26F: ("color_a", _decode_color_a),
    0x5037A0C1: ("color_b", _decode_color_b),
    0xFF457546: ("blend_mode", _decode_blend_mode),
    0x1AFA5C48: ("time_a2_b", structs.decode_BIG_f),
    0x12E12905: ("time_b2_a", structs.decode_BIG_f),
    0xCEC5244B: ("do_reverse", structs.decode_BIG_bool_),
    0x81FC979C: ("reset_target_when_done", structs.decode_BIG_bool_),
    0x94C01B0C: ("depth_compare", structs.decode_BIG_bool_),
    0xAED25A51: ("depth_update", structs.decode_BIG_bool_),
    0x35DC43D0: ("depth_backwards", structs.decode_BIG_bool_),
    0x3217DFF8: ("auto_start", structs.decode_BIG_bool_),
    0x3A7F59F7: ("update_time", structs.decode_BIG_bool_),
    0x08BB73C5: ("loop_forever", structs.decode_BIG_bool_),
    0x7E379AE8: ("external_time", structs.decode_BIG_bool_),
    0x74081E94: ("copy_model_color_to_color_a", structs.decode_BIG_bool_),
    0x9A306740: ("write_depth_first", structs.decode_BIG_bool_),
    0x15567FE7: ("control_spline", _decode_control_spline),
}
