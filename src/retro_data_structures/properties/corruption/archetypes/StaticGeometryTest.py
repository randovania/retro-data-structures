# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class StaticGeometryTestJson(typing_extensions.TypedDict):
        static_geometry_test: int


class StaticGeometryTestEnum(enum.IntEnum):
    Unknown1 = 996120112
    Unknown2 = 3961747340
    Unknown3 = 1419069414

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


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = 0x14B3F716


@dataclasses.dataclass()
class StaticGeometryTest(BaseProperty):
    static_geometry_test: StaticGeometryTestEnum = dataclasses.field(
        default=StaticGeometryTestEnum.Unknown2,
        metadata={
            "reflection": FieldReflection[StaticGeometryTestEnum](
                StaticGeometryTestEnum,
                id=0x14B3F716,
                original_name="StaticGeometryTest",
                from_json=StaticGeometryTestEnum.from_json,
                to_json=StaticGeometryTestEnum.to_json,
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
        if property_count != 1:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHL")

        dec = _FAST_FORMAT.unpack(data.read(10))
        assert (dec[0]) == _FAST_IDS
        return cls(
            StaticGeometryTestEnum(dec[2]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"\x14\xb3\xf7\x16")  # 0x14b3f716
        data.write(b"\x00\x04")  # size
        self.static_geometry_test.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("StaticGeometryTestJson", data)
        return cls(
            static_geometry_test=StaticGeometryTestEnum.from_json(json_data["static_geometry_test"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "static_geometry_test": self.static_geometry_test.to_json(),
        }


def _decode_static_geometry_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTestEnum:
    return StaticGeometryTestEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x14B3F716: ("static_geometry_test", _decode_static_geometry_test),
}
