# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.SpindlePositionInterpolant import SpindlePositionInterpolant
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SpindlePositionJson(typing_extensions.TypedDict):
        flags_spindle_position: int
        angular_speed: json_util.JsonObject
        linear_speed: json_util.JsonObject
        motion_radius: json_util.JsonObject
        radial_offset: json_util.JsonObject
        desired_angular_offset: json_util.JsonObject
        min_angular_offset: json_util.JsonObject
        max_angular_offset: json_util.JsonObject
        z_offset: json_util.JsonObject
        angular_constraint: json_util.JsonObject
        angular_dampening: json_util.JsonObject
        desired_angular_speed: json_util.JsonObject
        constraint_flip_angle: json_util.JsonObject


@dataclasses.dataclass()
class SpindlePosition(BaseProperty):
    flags_spindle_position: int = dataclasses.field(
        default=320,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB8A6413A, original_name="FlagsSpindlePosition"),
        },
    )  # Flagset
    angular_speed: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0xA0FB9986,
                original_name="AngularSpeed",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    linear_speed: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x58079583,
                original_name="LinearSpeed",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    motion_radius: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0xE44C1003,
                original_name="MotionRadius",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    radial_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x39936936,
                original_name="RadialOffset",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    desired_angular_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x2D8C38B0,
                original_name="DesiredAngularOffset",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    min_angular_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x1D2A6188,
                original_name="MinAngularOffset",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    max_angular_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x91CC9F6A,
                original_name="MaxAngularOffset",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    z_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x905289AC,
                original_name="ZOffset",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    angular_constraint: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0xF5F6849D,
                original_name="AngularConstraint",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    angular_dampening: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x7B66A7B4,
                original_name="AngularDampening",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    desired_angular_speed: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x68926CCD,
                original_name="DesiredAngularSpeed",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    constraint_flip_angle: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x3158FD3B,
                original_name="ConstraintFlipAngle",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8A6413A
        flags_spindle_position = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0FB9986
        angular_speed = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58079583
        linear_speed = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE44C1003
        motion_radius = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39936936
        radial_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D8C38B0
        desired_angular_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D2A6188
        min_angular_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91CC9F6A
        max_angular_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x905289AC
        z_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5F6849D
        angular_constraint = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7B66A7B4
        angular_dampening = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68926CCD
        desired_angular_speed = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3158FD3B
        constraint_flip_angle = SpindlePositionInterpolant.from_stream(data, game, property_size)

        return cls(
            flags_spindle_position,
            angular_speed,
            linear_speed,
            motion_radius,
            radial_offset,
            desired_angular_offset,
            min_angular_offset,
            max_angular_offset,
            z_offset,
            angular_constraint,
            angular_dampening,
            desired_angular_speed,
            constraint_flip_angle,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\r")  # 13 properties

        data.write(b"\xb8\xa6A:")  # 0xb8a6413a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_spindle_position))

        data.write(b"\xa0\xfb\x99\x86")  # 0xa0fb9986
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.angular_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"X\x07\x95\x83")  # 0x58079583
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.linear_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe4L\x10\x03")  # 0xe44c1003
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_radius.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"9\x93i6")  # 0x39936936
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.radial_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"-\x8c8\xb0")  # 0x2d8c38b0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.desired_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1d*a\x88")  # 0x1d2a6188
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.min_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x91\xcc\x9fj")  # 0x91cc9f6a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.max_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x90R\x89\xac")  # 0x905289ac
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.z_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf5\xf6\x84\x9d")  # 0xf5f6849d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.angular_constraint.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"{f\xa7\xb4")  # 0x7b66a7b4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.angular_dampening.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"h\x92l\xcd")  # 0x68926ccd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.desired_angular_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"1X\xfd;")  # 0x3158fd3b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.constraint_flip_angle.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpindlePositionJson", data)
        return cls(
            flags_spindle_position=json_data["flags_spindle_position"],
            angular_speed=SpindlePositionInterpolant.from_json(json_data["angular_speed"]),
            linear_speed=SpindlePositionInterpolant.from_json(json_data["linear_speed"]),
            motion_radius=SpindlePositionInterpolant.from_json(json_data["motion_radius"]),
            radial_offset=SpindlePositionInterpolant.from_json(json_data["radial_offset"]),
            desired_angular_offset=SpindlePositionInterpolant.from_json(json_data["desired_angular_offset"]),
            min_angular_offset=SpindlePositionInterpolant.from_json(json_data["min_angular_offset"]),
            max_angular_offset=SpindlePositionInterpolant.from_json(json_data["max_angular_offset"]),
            z_offset=SpindlePositionInterpolant.from_json(json_data["z_offset"]),
            angular_constraint=SpindlePositionInterpolant.from_json(json_data["angular_constraint"]),
            angular_dampening=SpindlePositionInterpolant.from_json(json_data["angular_dampening"]),
            desired_angular_speed=SpindlePositionInterpolant.from_json(json_data["desired_angular_speed"]),
            constraint_flip_angle=SpindlePositionInterpolant.from_json(json_data["constraint_flip_angle"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "flags_spindle_position": self.flags_spindle_position,
            "angular_speed": self.angular_speed.to_json(),
            "linear_speed": self.linear_speed.to_json(),
            "motion_radius": self.motion_radius.to_json(),
            "radial_offset": self.radial_offset.to_json(),
            "desired_angular_offset": self.desired_angular_offset.to_json(),
            "min_angular_offset": self.min_angular_offset.to_json(),
            "max_angular_offset": self.max_angular_offset.to_json(),
            "z_offset": self.z_offset.to_json(),
            "angular_constraint": self.angular_constraint.to_json(),
            "angular_dampening": self.angular_dampening.to_json(),
            "desired_angular_speed": self.desired_angular_speed.to_json(),
            "constraint_flip_angle": self.constraint_flip_angle.to_json(),
        }


def _decode_angular_speed(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_linear_speed(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_motion_radius(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_radial_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_desired_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_min_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_max_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_z_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_angular_constraint(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_angular_dampening(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_desired_angular_speed(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_constraint_flip_angle(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB8A6413A: ("flags_spindle_position", structs.decode_BIG_L),
    0xA0FB9986: ("angular_speed", _decode_angular_speed),
    0x58079583: ("linear_speed", _decode_linear_speed),
    0xE44C1003: ("motion_radius", _decode_motion_radius),
    0x39936936: ("radial_offset", _decode_radial_offset),
    0x2D8C38B0: ("desired_angular_offset", _decode_desired_angular_offset),
    0x1D2A6188: ("min_angular_offset", _decode_min_angular_offset),
    0x91CC9F6A: ("max_angular_offset", _decode_max_angular_offset),
    0x905289AC: ("z_offset", _decode_z_offset),
    0xF5F6849D: ("angular_constraint", _decode_angular_constraint),
    0x7B66A7B4: ("angular_dampening", _decode_angular_dampening),
    0x68926CCD: ("desired_angular_speed", _decode_desired_angular_speed),
    0x3158FD3B: ("constraint_flip_angle", _decode_constraint_flip_angle),
}
