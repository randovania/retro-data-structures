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

    class SpindleOrientationJson(typing_extensions.TypedDict):
        flags_spindle_orientation: int
        look_at_angular_offset: json_util.JsonObject
        look_at_z_offset: json_util.JsonObject


@dataclasses.dataclass()
class SpindleOrientation(BaseProperty):
    flags_spindle_orientation: int = dataclasses.field(
        default=786432,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1B4962BF, original_name="FlagsSpindleOrientation"),
        },
    )  # Flagset
    look_at_angular_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0x609C0608,
                original_name="LookAtAngularOffset",
                from_json=SpindlePositionInterpolant.from_json,
                to_json=SpindlePositionInterpolant.to_json,
            ),
        },
    )
    look_at_z_offset: SpindlePositionInterpolant = dataclasses.field(
        default_factory=SpindlePositionInterpolant,
        metadata={
            "reflection": FieldReflection[SpindlePositionInterpolant](
                SpindlePositionInterpolant,
                id=0xF6C828C0,
                original_name="LookAtZOffset",
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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1B4962BF
        flags_spindle_orientation = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x609C0608
        look_at_angular_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF6C828C0
        look_at_z_offset = SpindlePositionInterpolant.from_stream(data, game, property_size)

        return cls(flags_spindle_orientation, look_at_angular_offset, look_at_z_offset)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\x1bIb\xbf")  # 0x1b4962bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_spindle_orientation))

        data.write(b"`\x9c\x06\x08")  # 0x609c0608
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_at_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf6\xc8(\xc0")  # 0xf6c828c0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.look_at_z_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpindleOrientationJson", data)
        return cls(
            flags_spindle_orientation=json_data["flags_spindle_orientation"],
            look_at_angular_offset=SpindlePositionInterpolant.from_json(json_data["look_at_angular_offset"]),
            look_at_z_offset=SpindlePositionInterpolant.from_json(json_data["look_at_z_offset"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "flags_spindle_orientation": self.flags_spindle_orientation,
            "look_at_angular_offset": self.look_at_angular_offset.to_json(),
            "look_at_z_offset": self.look_at_z_offset.to_json(),
        }


def _decode_look_at_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


def _decode_look_at_z_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindlePositionInterpolant:
    return SpindlePositionInterpolant.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1B4962BF: ("flags_spindle_orientation", structs.decode_BIG_L),
    0x609C0608: ("look_at_angular_offset", _decode_look_at_angular_offset),
    0xF6C828C0: ("look_at_z_offset", _decode_look_at_z_offset),
}
