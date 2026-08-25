# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraControlsJson(typing_extensions.TypedDict):
        look_up: json_util.JsonObject
        look_down: json_util.JsonObject
        look_left: json_util.JsonObject
        look_right: json_util.JsonObject
        unknown: json_util.JsonObject
        view_lock: json_util.JsonObject
        skip_cinematic: json_util.JsonObject
        look_up_control: json_util.JsonObject
        look_down_control: json_util.JsonObject


@dataclasses.dataclass()
class CameraControls(BaseProperty):
    look_up: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x1C1D6F49,
                original_name="LookUp",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    look_down: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x1A20D5F4,
                original_name="LookDown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    look_left: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x90415E79,
                original_name="LookLeft",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    look_right: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x23C1333C,
                original_name="LookRight",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x2B4BA1A3,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    view_lock: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xD47F24D7,
                original_name="ViewLock",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    skip_cinematic: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x19A3E07D,
                original_name="SkipCinematic",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    look_up_control: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xA03390A5, original_name="LookUpControl", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    look_down_control: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xE746F77E,
                original_name="LookDownControl",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C1D6F49
        look_up = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A20D5F4
        look_down = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90415E79
        look_left = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23C1333C
        look_right = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B4BA1A3
        unknown = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD47F24D7
        view_lock = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19A3E07D
        skip_cinematic = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA03390A5
        look_up_control = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE746F77E
        look_down_control = Spline.from_stream(data, game, property_size)

        return cls(
            look_up,
            look_down,
            look_left,
            look_right,
            unknown,
            view_lock,
            skip_cinematic,
            look_up_control,
            look_down_control,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\x1c\x1doI")  # 0x1c1d6f49
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1a \xd5\xf4")  # 0x1a20d5f4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x90A^y")  # 0x90415e79
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"#\xc13<")  # 0x23c1333c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"+K\xa1\xa3")  # 0x2b4ba1a3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd4\x7f$\xd7")  # 0xd47f24d7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.view_lock.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\xa3\xe0}")  # 0x19a3e07d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.skip_cinematic.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa03\x90\xa5")  # 0xa03390a5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_up_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe7F\xf7~")  # 0xe746f77e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_down_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraControlsJson", data)
        return cls(
            look_up=RevolutionControl.from_json(json_data["look_up"]),
            look_down=RevolutionControl.from_json(json_data["look_down"]),
            look_left=RevolutionControl.from_json(json_data["look_left"]),
            look_right=RevolutionControl.from_json(json_data["look_right"]),
            unknown=RevolutionControl.from_json(json_data["unknown"]),
            view_lock=RevolutionControl.from_json(json_data["view_lock"]),
            skip_cinematic=RevolutionControl.from_json(json_data["skip_cinematic"]),
            look_up_control=Spline.from_json(json_data["look_up_control"]),
            look_down_control=Spline.from_json(json_data["look_down_control"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "look_up": self.look_up.to_json(),
            "look_down": self.look_down.to_json(),
            "look_left": self.look_left.to_json(),
            "look_right": self.look_right.to_json(),
            "unknown": self.unknown.to_json(),
            "view_lock": self.view_lock.to_json(),
            "skip_cinematic": self.skip_cinematic.to_json(),
            "look_up_control": self.look_up_control.to_json(),
            "look_down_control": self.look_down_control.to_json(),
        }


def _decode_look_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_look_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_look_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_look_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_view_lock(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_skip_cinematic(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_look_up_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_look_down_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1C1D6F49: ("look_up", _decode_look_up),
    0x1A20D5F4: ("look_down", _decode_look_down),
    0x90415E79: ("look_left", _decode_look_left),
    0x23C1333C: ("look_right", _decode_look_right),
    0x2B4BA1A3: ("unknown", _decode_unknown),
    0xD47F24D7: ("view_lock", _decode_view_lock),
    0x19A3E07D: ("skip_cinematic", _decode_skip_cinematic),
    0xA03390A5: ("look_up_control", _decode_look_up_control),
    0xE746F77E: ("look_down_control", _decode_look_down_control),
}
