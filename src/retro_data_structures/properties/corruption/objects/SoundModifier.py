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
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SoundModifierJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        time: float
        auto_reset: bool
        auto_start: bool
        global_: bool
        volume: json_util.JsonObject
        pan: json_util.JsonObject
        surround_pan: json_util.JsonObject
        pitch: json_util.JsonObject
        low_pass: json_util.JsonObject


@dataclasses.dataclass()
class SoundModifier(BaseObjectType):
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
    time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x44335AFF, original_name="Time"),
        },
    )
    auto_reset: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7BEF45CA, original_name="AutoReset"),
        },
    )
    auto_start: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3217DFF8, original_name="AutoStart"),
        },
    )
    global_: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2409B906, original_name="Global"),
        },
    )
    volume: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xF3FBE484, original_name="Volume", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    pan: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x2858C9F0, original_name="Pan", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    surround_pan: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x5113198F, original_name="SurroundPan", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    pitch: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x0E727FC4, original_name="Pitch", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    low_pass: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xD3049E04, original_name="LowPass", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SNDM"

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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44335AFF
        time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7BEF45CA
        auto_reset = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3217DFF8
        auto_start = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2409B906
        global_ = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3FBE484
        volume = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2858C9F0
        pan = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5113198F
        surround_pan = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0E727FC4
        pitch = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD3049E04
        low_pass = Spline.from_stream(data, game, property_size)

        return cls(editor_properties, time, auto_reset, auto_start, global_, volume, pan, surround_pan, pitch, low_pass)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\n")  # 10 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"D3Z\xff")  # 0x44335aff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.time))

        data.write(b"{\xefE\xca")  # 0x7bef45ca
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_reset))

        data.write(b"2\x17\xdf\xf8")  # 0x3217dff8
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.auto_start))

        data.write(b"$\t\xb9\x06")  # 0x2409b906
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.global_))

        data.write(b"\xf3\xfb\xe4\x84")  # 0xf3fbe484
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.volume.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"(X\xc9\xf0")  # 0x2858c9f0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.pan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Q\x13\x19\x8f")  # 0x5113198f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.surround_pan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0er\x7f\xc4")  # 0xe727fc4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.pitch.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd3\x04\x9e\x04")  # 0xd3049e04
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.low_pass.to_stream(data, game)
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
        json_data = typing.cast("SoundModifierJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            time=json_data["time"],
            auto_reset=json_data["auto_reset"],
            auto_start=json_data["auto_start"],
            global_=json_data["global_"],
            volume=Spline.from_json(json_data["volume"]),
            pan=Spline.from_json(json_data["pan"]),
            surround_pan=Spline.from_json(json_data["surround_pan"]),
            pitch=Spline.from_json(json_data["pitch"]),
            low_pass=Spline.from_json(json_data["low_pass"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "time": self.time,
            "auto_reset": self.auto_reset,
            "auto_start": self.auto_start,
            "global_": self.global_,
            "volume": self.volume.to_json(),
            "pan": self.pan.to_json(),
            "surround_pan": self.surround_pan.to_json(),
            "pitch": self.pitch.to_json(),
            "low_pass": self.low_pass.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_volume(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_pan(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_surround_pan(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_pitch(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_low_pass(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x44335AFF: ("time", structs.decode_BIG_f),
    0x7BEF45CA: ("auto_reset", structs.decode_BIG_bool_),
    0x3217DFF8: ("auto_start", structs.decode_BIG_bool_),
    0x2409B906: ("global_", structs.decode_BIG_bool_),
    0xF3FBE484: ("volume", _decode_volume),
    0x2858C9F0: ("pan", _decode_pan),
    0x5113198F: ("surround_pan", _decode_surround_pan),
    0x0E727FC4: ("pitch", _decode_pitch),
    0xD3049E04: ("low_pass", _decode_low_pass),
}
