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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SpinnerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        forward_speed: float
        backward_speed: float
        unknown_0x449dd059: float
        unknown_0xfc849759: float
        shot_spinner: bool
        allow_wrap: bool
        no_backward: bool
        spline_control: bool
        unknown_0x865322ca: bool
        loop_sound: int
        start_sound: int
        stop_sound: int


@dataclasses.dataclass()
class Spinner(BaseObjectType):
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
    forward_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDE4F6A76, original_name="ForwardSpeed"),
        },
    )
    backward_speed: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x54E15A3C, original_name="BackwardSpeed"),
        },
    )
    unknown_0x449dd059: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x449DD059, original_name="Unknown"),
        },
    )
    unknown_0xfc849759: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFC849759, original_name="Unknown"),
        },
    )
    shot_spinner: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x50501E17, original_name="ShotSpinner"),
        },
    )
    allow_wrap: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3983CBA7, original_name="AllowWrap"),
        },
    )
    no_backward: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF1C8A0AE, original_name="NoBackward"),
        },
    )
    spline_control: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE8F0A1CE, original_name="SplineControl"),
        },
    )
    unknown_0x865322ca: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x865322CA, original_name="Unknown"),
        },
    )
    loop_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7147757A, original_name="LoopSound"),
        },
    )
    start_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA8CC48B3, original_name="StartSound"),
        },
    )
    stop_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x12AFE499, original_name="StopSound"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SPIN"

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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDE4F6A76
        forward_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54E15A3C
        backward_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x449DD059
        unknown_0x449dd059 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC849759
        unknown_0xfc849759 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50501E17
        shot_spinner = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3983CBA7
        allow_wrap = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1C8A0AE
        no_backward = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8F0A1CE
        spline_control = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x865322CA
        unknown_0x865322ca = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7147757A
        loop_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8CC48B3
        start_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12AFE499
        stop_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            editor_properties,
            forward_speed,
            backward_speed,
            unknown_0x449dd059,
            unknown_0xfc849759,
            shot_spinner,
            allow_wrap,
            no_backward,
            spline_control,
            unknown_0x865322ca,
            loop_sound,
            start_sound,
            stop_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\r")  # 13 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdeOjv")  # 0xde4f6a76
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.forward_speed))

        data.write(b"T\xe1Z<")  # 0x54e15a3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.backward_speed))

        data.write(b"D\x9d\xd0Y")  # 0x449dd059
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x449dd059))

        data.write(b"\xfc\x84\x97Y")  # 0xfc849759
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfc849759))

        data.write(b"PP\x1e\x17")  # 0x50501e17
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.shot_spinner))

        data.write(b"9\x83\xcb\xa7")  # 0x3983cba7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.allow_wrap))

        data.write(b"\xf1\xc8\xa0\xae")  # 0xf1c8a0ae
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.no_backward))

        data.write(b"\xe8\xf0\xa1\xce")  # 0xe8f0a1ce
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.spline_control))

        data.write(b'\x86S"\xca')  # 0x865322ca
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x865322ca))

        data.write(b"qGuz")  # 0x7147757a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.loop_sound))

        data.write(b"\xa8\xccH\xb3")  # 0xa8cc48b3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.start_sound))

        data.write(b"\x12\xaf\xe4\x99")  # 0x12afe499
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stop_sound))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpinnerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            forward_speed=json_data["forward_speed"],
            backward_speed=json_data["backward_speed"],
            unknown_0x449dd059=json_data["unknown_0x449dd059"],
            unknown_0xfc849759=json_data["unknown_0xfc849759"],
            shot_spinner=json_data["shot_spinner"],
            allow_wrap=json_data["allow_wrap"],
            no_backward=json_data["no_backward"],
            spline_control=json_data["spline_control"],
            unknown_0x865322ca=json_data["unknown_0x865322ca"],
            loop_sound=json_data["loop_sound"],
            start_sound=json_data["start_sound"],
            stop_sound=json_data["stop_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "forward_speed": self.forward_speed,
            "backward_speed": self.backward_speed,
            "unknown_0x449dd059": self.unknown_0x449dd059,
            "unknown_0xfc849759": self.unknown_0xfc849759,
            "shot_spinner": self.shot_spinner,
            "allow_wrap": self.allow_wrap,
            "no_backward": self.no_backward,
            "spline_control": self.spline_control,
            "unknown_0x865322ca": self.unknown_0x865322ca,
            "loop_sound": self.loop_sound,
            "start_sound": self.start_sound,
            "stop_sound": self.stop_sound,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xDE4F6A76: ("forward_speed", structs.decode_BIG_f),
    0x54E15A3C: ("backward_speed", structs.decode_BIG_f),
    0x449DD059: ("unknown_0x449dd059", structs.decode_BIG_f),
    0xFC849759: ("unknown_0xfc849759", structs.decode_BIG_f),
    0x50501E17: ("shot_spinner", structs.decode_BIG_bool_),
    0x3983CBA7: ("allow_wrap", structs.decode_BIG_bool_),
    0xF1C8A0AE: ("no_backward", structs.decode_BIG_bool_),
    0xE8F0A1CE: ("spline_control", structs.decode_BIG_bool_),
    0x865322CA: ("unknown_0x865322ca", structs.decode_BIG_bool_),
    0x7147757A: ("loop_sound", structs.decode_BIG_Q),
    0xA8CC48B3: ("start_sound", structs.decode_BIG_Q),
    0x12AFE499: ("stop_sound", structs.decode_BIG_Q),
}
