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

    class PathDeterminationMethodTypeJson(typing_extensions.TypedDict):
        path_determination_method: int


class PathDeterminationMethod(enum.IntEnum):
    Unknown1 = 368071499
    Unknown2 = 866990353
    Unknown3 = 1330523455
    Unknown4 = 1762871141

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
_FAST_IDS = 0xB80D00A8


@dataclasses.dataclass()
class PathDeterminationMethodType(BaseProperty):
    path_determination_method: PathDeterminationMethod = dataclasses.field(
        default=PathDeterminationMethod.Unknown1,
        metadata={
            "reflection": FieldReflection[PathDeterminationMethod](
                PathDeterminationMethod,
                id=0xB80D00A8,
                original_name="PathDeterminationMethod",
                from_json=PathDeterminationMethod.from_json,
                to_json=PathDeterminationMethod.to_json,
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
            PathDeterminationMethod(dec[2]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"\xb8\r\x00\xa8")  # 0xb80d00a8
        data.write(b"\x00\x04")  # size
        self.path_determination_method.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PathDeterminationMethodTypeJson", data)
        return cls(
            path_determination_method=PathDeterminationMethod.from_json(json_data["path_determination_method"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "path_determination_method": self.path_determination_method.to_json(),
        }


def _decode_path_determination_method(data: typing.BinaryIO, game: Game, property_size: int) -> PathDeterminationMethod:
    return PathDeterminationMethod.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB80D00A8: ("path_determination_method", _decode_path_determination_method),
}
