# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.FOVInterpolationMethod import FOVInterpolationMethod
from retro_data_structures.properties.corruption.archetypes.MotionInterpolationMethod import MotionInterpolationMethod
from retro_data_structures.properties.corruption.archetypes.OrientationInterpolationMethod import (
    OrientationInterpolationMethod,
)
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraInterpolationJson(typing_extensions.TypedDict):
        on_flags: int
        on_distance: float
        on_angle: float
        motion_interpolation_on: json_util.JsonObject
        orientation_interpolation_on: json_util.JsonObject
        fov_interpolation_on: json_util.JsonObject
        off_flags: int
        off_distance: float
        off_angle: float
        motion_interpolation_off: json_util.JsonObject
        orientation_interpolation_off: json_util.JsonObject
        fov_interpolation_off: json_util.JsonObject
        custom_flags: int
        custom_distance: float
        custom_angle: float
        motion_interpolation_custom: json_util.JsonObject
        orientation_interpolation_custom: json_util.JsonObject
        fov_interpolation_method: json_util.JsonObject


@dataclasses.dataclass()
class CameraInterpolation(BaseProperty):
    on_flags: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1D49D35C, original_name="OnFlags"),
        },
    )  # Flagset
    on_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC22D6492, original_name="OnDistance"),
        },
    )
    on_angle: float = dataclasses.field(
        default=135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE02022D5, original_name="OnAngle"),
        },
    )
    motion_interpolation_on: MotionInterpolationMethod = dataclasses.field(
        default_factory=MotionInterpolationMethod,
        metadata={
            "reflection": FieldReflection[MotionInterpolationMethod](
                MotionInterpolationMethod,
                id=0xA738790A,
                original_name="MotionInterpolationOn",
                from_json=MotionInterpolationMethod.from_json,
                to_json=MotionInterpolationMethod.to_json,
            ),
        },
    )
    orientation_interpolation_on: OrientationInterpolationMethod = dataclasses.field(
        default_factory=OrientationInterpolationMethod,
        metadata={
            "reflection": FieldReflection[OrientationInterpolationMethod](
                OrientationInterpolationMethod,
                id=0xA768A18E,
                original_name="OrientationInterpolationOn",
                from_json=OrientationInterpolationMethod.from_json,
                to_json=OrientationInterpolationMethod.to_json,
            ),
        },
    )
    fov_interpolation_on: FOVInterpolationMethod = dataclasses.field(
        default_factory=FOVInterpolationMethod,
        metadata={
            "reflection": FieldReflection[FOVInterpolationMethod](
                FOVInterpolationMethod,
                id=0x3B8C7CB4,
                original_name="FOVInterpolationOn",
                from_json=FOVInterpolationMethod.from_json,
                to_json=FOVInterpolationMethod.to_json,
            ),
        },
    )
    off_flags: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x058C1B1D, original_name="OffFlags"),
        },
    )  # Flagset
    off_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x943F8A27, original_name="OffDistance"),
        },
    )
    off_angle: float = dataclasses.field(
        default=135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3127E68A, original_name="OffAngle"),
        },
    )
    motion_interpolation_off: MotionInterpolationMethod = dataclasses.field(
        default_factory=MotionInterpolationMethod,
        metadata={
            "reflection": FieldReflection[MotionInterpolationMethod](
                MotionInterpolationMethod,
                id=0x7FAC732A,
                original_name="MotionInterpolationOff",
                from_json=MotionInterpolationMethod.from_json,
                to_json=MotionInterpolationMethod.to_json,
            ),
        },
    )
    orientation_interpolation_off: OrientationInterpolationMethod = dataclasses.field(
        default_factory=OrientationInterpolationMethod,
        metadata={
            "reflection": FieldReflection[OrientationInterpolationMethod](
                OrientationInterpolationMethod,
                id=0xDFAB73B6,
                original_name="OrientationInterpolationOff",
                from_json=OrientationInterpolationMethod.from_json,
                to_json=OrientationInterpolationMethod.to_json,
            ),
        },
    )
    fov_interpolation_off: FOVInterpolationMethod = dataclasses.field(
        default_factory=FOVInterpolationMethod,
        metadata={
            "reflection": FieldReflection[FOVInterpolationMethod](
                FOVInterpolationMethod,
                id=0xF391EDBC,
                original_name="FOVInterpolationOff",
                from_json=FOVInterpolationMethod.from_json,
                to_json=FOVInterpolationMethod.to_json,
            ),
        },
    )
    custom_flags: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0x07A6C22C, original_name="CustomFlags"),
        },
    )  # Flagset
    custom_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC4E74018, original_name="CustomDistance"),
        },
    )
    custom_angle: float = dataclasses.field(
        default=135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x28B3B4B5, original_name="CustomAngle"),
        },
    )
    motion_interpolation_custom: MotionInterpolationMethod = dataclasses.field(
        default_factory=MotionInterpolationMethod,
        metadata={
            "reflection": FieldReflection[MotionInterpolationMethod](
                MotionInterpolationMethod,
                id=0xBC723CAC,
                original_name="MotionInterpolationCustom",
                from_json=MotionInterpolationMethod.from_json,
                to_json=MotionInterpolationMethod.to_json,
            ),
        },
    )
    orientation_interpolation_custom: OrientationInterpolationMethod = dataclasses.field(
        default_factory=OrientationInterpolationMethod,
        metadata={
            "reflection": FieldReflection[OrientationInterpolationMethod](
                OrientationInterpolationMethod,
                id=0xBE093676,
                original_name="OrientationInterpolationCustom",
                from_json=OrientationInterpolationMethod.from_json,
                to_json=OrientationInterpolationMethod.to_json,
            ),
        },
    )
    fov_interpolation_method: FOVInterpolationMethod = dataclasses.field(
        default_factory=FOVInterpolationMethod,
        metadata={
            "reflection": FieldReflection[FOVInterpolationMethod](
                FOVInterpolationMethod,
                id=0x70754E15,
                original_name="FOVInterpolationMethod",
                from_json=FOVInterpolationMethod.from_json,
                to_json=FOVInterpolationMethod.to_json,
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
        if property_count != 18:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1D49D35C
        on_flags = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC22D6492
        on_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE02022D5
        on_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA738790A
        motion_interpolation_on = MotionInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA768A18E
        orientation_interpolation_on = OrientationInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3B8C7CB4
        fov_interpolation_on = FOVInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x058C1B1D
        off_flags = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x943F8A27
        off_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3127E68A
        off_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FAC732A
        motion_interpolation_off = MotionInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFAB73B6
        orientation_interpolation_off = OrientationInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF391EDBC
        fov_interpolation_off = FOVInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07A6C22C
        custom_flags = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4E74018
        custom_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28B3B4B5
        custom_angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC723CAC
        motion_interpolation_custom = MotionInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE093676
        orientation_interpolation_custom = OrientationInterpolationMethod.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70754E15
        fov_interpolation_method = FOVInterpolationMethod.from_stream(data, game, property_size)

        return cls(
            on_flags,
            on_distance,
            on_angle,
            motion_interpolation_on,
            orientation_interpolation_on,
            fov_interpolation_on,
            off_flags,
            off_distance,
            off_angle,
            motion_interpolation_off,
            orientation_interpolation_off,
            fov_interpolation_off,
            custom_flags,
            custom_distance,
            custom_angle,
            motion_interpolation_custom,
            orientation_interpolation_custom,
            fov_interpolation_method,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x12")  # 18 properties

        data.write(b"\x1dI\xd3\\")  # 0x1d49d35c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.on_flags))

        data.write(b"\xc2-d\x92")  # 0xc22d6492
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.on_distance))

        data.write(b'\xe0 "\xd5')  # 0xe02022d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.on_angle))

        data.write(b"\xa78y\n")  # 0xa738790a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_interpolation_on.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa7h\xa1\x8e")  # 0xa768a18e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orientation_interpolation_on.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b";\x8c|\xb4")  # 0x3b8c7cb4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.fov_interpolation_on.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x05\x8c\x1b\x1d")  # 0x58c1b1d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.off_flags))

        data.write(b"\x94?\x8a'")  # 0x943f8a27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.off_distance))

        data.write(b"1'\xe6\x8a")  # 0x3127e68a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.off_angle))

        data.write(b"\x7f\xacs*")  # 0x7fac732a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_interpolation_off.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdf\xabs\xb6")  # 0xdfab73b6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orientation_interpolation_off.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3\x91\xed\xbc")  # 0xf391edbc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.fov_interpolation_off.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x07\xa6\xc2,")  # 0x7a6c22c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.custom_flags))

        data.write(b"\xc4\xe7@\x18")  # 0xc4e74018
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.custom_distance))

        data.write(b"(\xb3\xb4\xb5")  # 0x28b3b4b5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.custom_angle))

        data.write(b"\xbcr<\xac")  # 0xbc723cac
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_interpolation_custom.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbe\t6v")  # 0xbe093676
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.orientation_interpolation_custom.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"puN\x15")  # 0x70754e15
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.fov_interpolation_method.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraInterpolationJson", data)
        return cls(
            on_flags=json_data["on_flags"],
            on_distance=json_data["on_distance"],
            on_angle=json_data["on_angle"],
            motion_interpolation_on=MotionInterpolationMethod.from_json(json_data["motion_interpolation_on"]),
            orientation_interpolation_on=OrientationInterpolationMethod.from_json(
                json_data["orientation_interpolation_on"]
            ),
            fov_interpolation_on=FOVInterpolationMethod.from_json(json_data["fov_interpolation_on"]),
            off_flags=json_data["off_flags"],
            off_distance=json_data["off_distance"],
            off_angle=json_data["off_angle"],
            motion_interpolation_off=MotionInterpolationMethod.from_json(json_data["motion_interpolation_off"]),
            orientation_interpolation_off=OrientationInterpolationMethod.from_json(
                json_data["orientation_interpolation_off"]
            ),
            fov_interpolation_off=FOVInterpolationMethod.from_json(json_data["fov_interpolation_off"]),
            custom_flags=json_data["custom_flags"],
            custom_distance=json_data["custom_distance"],
            custom_angle=json_data["custom_angle"],
            motion_interpolation_custom=MotionInterpolationMethod.from_json(json_data["motion_interpolation_custom"]),
            orientation_interpolation_custom=OrientationInterpolationMethod.from_json(
                json_data["orientation_interpolation_custom"]
            ),
            fov_interpolation_method=FOVInterpolationMethod.from_json(json_data["fov_interpolation_method"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "on_flags": self.on_flags,
            "on_distance": self.on_distance,
            "on_angle": self.on_angle,
            "motion_interpolation_on": self.motion_interpolation_on.to_json(),
            "orientation_interpolation_on": self.orientation_interpolation_on.to_json(),
            "fov_interpolation_on": self.fov_interpolation_on.to_json(),
            "off_flags": self.off_flags,
            "off_distance": self.off_distance,
            "off_angle": self.off_angle,
            "motion_interpolation_off": self.motion_interpolation_off.to_json(),
            "orientation_interpolation_off": self.orientation_interpolation_off.to_json(),
            "fov_interpolation_off": self.fov_interpolation_off.to_json(),
            "custom_flags": self.custom_flags,
            "custom_distance": self.custom_distance,
            "custom_angle": self.custom_angle,
            "motion_interpolation_custom": self.motion_interpolation_custom.to_json(),
            "orientation_interpolation_custom": self.orientation_interpolation_custom.to_json(),
            "fov_interpolation_method": self.fov_interpolation_method.to_json(),
        }


def _decode_motion_interpolation_on(data: typing.BinaryIO, game: Game, property_size: int) -> MotionInterpolationMethod:
    return MotionInterpolationMethod.from_stream(data, game, property_size)


def _decode_orientation_interpolation_on(
    data: typing.BinaryIO, game: Game, property_size: int
) -> OrientationInterpolationMethod:
    return OrientationInterpolationMethod.from_stream(data, game, property_size)


def _decode_fov_interpolation_on(data: typing.BinaryIO, game: Game, property_size: int) -> FOVInterpolationMethod:
    return FOVInterpolationMethod.from_stream(data, game, property_size)


def _decode_motion_interpolation_off(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MotionInterpolationMethod:
    return MotionInterpolationMethod.from_stream(data, game, property_size)


def _decode_orientation_interpolation_off(
    data: typing.BinaryIO, game: Game, property_size: int
) -> OrientationInterpolationMethod:
    return OrientationInterpolationMethod.from_stream(data, game, property_size)


def _decode_fov_interpolation_off(data: typing.BinaryIO, game: Game, property_size: int) -> FOVInterpolationMethod:
    return FOVInterpolationMethod.from_stream(data, game, property_size)


def _decode_motion_interpolation_custom(
    data: typing.BinaryIO, game: Game, property_size: int
) -> MotionInterpolationMethod:
    return MotionInterpolationMethod.from_stream(data, game, property_size)


def _decode_orientation_interpolation_custom(
    data: typing.BinaryIO, game: Game, property_size: int
) -> OrientationInterpolationMethod:
    return OrientationInterpolationMethod.from_stream(data, game, property_size)


def _decode_fov_interpolation_method(data: typing.BinaryIO, game: Game, property_size: int) -> FOVInterpolationMethod:
    return FOVInterpolationMethod.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1D49D35C: ("on_flags", structs.decode_BIG_L),
    0xC22D6492: ("on_distance", structs.decode_BIG_f),
    0xE02022D5: ("on_angle", structs.decode_BIG_f),
    0xA738790A: ("motion_interpolation_on", _decode_motion_interpolation_on),
    0xA768A18E: ("orientation_interpolation_on", _decode_orientation_interpolation_on),
    0x3B8C7CB4: ("fov_interpolation_on", _decode_fov_interpolation_on),
    0x058C1B1D: ("off_flags", structs.decode_BIG_L),
    0x943F8A27: ("off_distance", structs.decode_BIG_f),
    0x3127E68A: ("off_angle", structs.decode_BIG_f),
    0x7FAC732A: ("motion_interpolation_off", _decode_motion_interpolation_off),
    0xDFAB73B6: ("orientation_interpolation_off", _decode_orientation_interpolation_off),
    0xF391EDBC: ("fov_interpolation_off", _decode_fov_interpolation_off),
    0x07A6C22C: ("custom_flags", structs.decode_BIG_L),
    0xC4E74018: ("custom_distance", structs.decode_BIG_f),
    0x28B3B4B5: ("custom_angle", structs.decode_BIG_f),
    0xBC723CAC: ("motion_interpolation_custom", _decode_motion_interpolation_custom),
    0xBE093676: ("orientation_interpolation_custom", _decode_orientation_interpolation_custom),
    0x70754E15: ("fov_interpolation_method", _decode_fov_interpolation_method),
}
