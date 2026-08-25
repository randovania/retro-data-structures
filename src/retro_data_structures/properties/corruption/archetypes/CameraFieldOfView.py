# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraFieldOfViewJson(typing_extensions.TypedDict):
        fov_type: int
        fov_path_object: int
        desired_fov: float
        unknown_0x972c0e20: json_util.JsonObject
        unknown_0x812cf888: json_util.JsonObject


class FOVPathObject(enum.IntEnum):
    Unknown1 = 221052433
    Unknown2 = 3545934728
    Unknown3 = 2921949809

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
class CameraFieldOfView(BaseProperty):
    fov_type: int = dataclasses.field(
        default=2839405128,
        metadata={
            "reflection": FieldReflection[int](int, id=0x19EA151B, original_name="FOVType"),
        },
    )  # Choice
    fov_path_object: FOVPathObject = dataclasses.field(
        default=FOVPathObject.Unknown1,
        metadata={
            "reflection": FieldReflection[FOVPathObject](
                FOVPathObject,
                id=0xD1E91886,
                original_name="FOVPathObject",
                from_json=FOVPathObject.from_json,
                to_json=FOVPathObject.to_json,
            ),
        },
    )
    desired_fov: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCAFE3DA7, original_name="DesiredFOV"),
        },
    )
    unknown_0x972c0e20: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x972C0E20, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x812cf888: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x812CF888, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19EA151B
        fov_type = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1E91886
        fov_path_object = FOVPathObject.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCAFE3DA7
        desired_fov = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x972C0E20
        unknown_0x972c0e20 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x812CF888
        unknown_0x812cf888 = Spline.from_stream(data, game, property_size)

        return cls(fov_type, fov_path_object, desired_fov, unknown_0x972c0e20, unknown_0x812cf888)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"\x19\xea\x15\x1b")  # 0x19ea151b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.fov_type))

        data.write(b"\xd1\xe9\x18\x86")  # 0xd1e91886
        data.write(b"\x00\x04")  # size
        self.fov_path_object.to_stream(data, game)

        data.write(b"\xca\xfe=\xa7")  # 0xcafe3da7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.desired_fov))

        data.write(b"\x97,\x0e ")  # 0x972c0e20
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x972c0e20.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81,\xf8\x88")  # 0x812cf888
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x812cf888.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraFieldOfViewJson", data)
        return cls(
            fov_type=json_data["fov_type"],
            fov_path_object=FOVPathObject.from_json(json_data["fov_path_object"]),
            desired_fov=json_data["desired_fov"],
            unknown_0x972c0e20=Spline.from_json(json_data["unknown_0x972c0e20"]),
            unknown_0x812cf888=Spline.from_json(json_data["unknown_0x812cf888"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "fov_type": self.fov_type,
            "fov_path_object": self.fov_path_object.to_json(),
            "desired_fov": self.desired_fov,
            "unknown_0x972c0e20": self.unknown_0x972c0e20.to_json(),
            "unknown_0x812cf888": self.unknown_0x812cf888.to_json(),
        }


def _decode_fov_path_object(data: typing.BinaryIO, game: Game, property_size: int) -> FOVPathObject:
    return FOVPathObject.from_stream(data, game)


def _decode_unknown_0x972c0e20(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x812cf888(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x19EA151B: ("fov_type", structs.decode_BIG_L),
    0xD1E91886: ("fov_path_object", _decode_fov_path_object),
    0xCAFE3DA7: ("desired_fov", structs.decode_BIG_f),
    0x972C0E20: ("unknown_0x972c0e20", _decode_unknown_0x972c0e20),
    0x812CF888: ("unknown_0x812cf888", _decode_unknown_0x812cf888),
}
