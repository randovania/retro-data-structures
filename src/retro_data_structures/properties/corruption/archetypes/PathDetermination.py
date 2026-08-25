# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PathDeterminationMethodType import (
    PathDeterminationMethodType,
)
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PathDeterminationJson(typing_extensions.TypedDict):
        path_link_type: int
        path_determination_method_type: json_util.JsonObject


class PathLinkType(enum.IntEnum):
    Unknown1 = 3955847150
    Unknown2 = 3844849857
    Unknown3 = 1461363479
    Unknown4 = 3983564465

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
class PathDetermination(BaseProperty):
    path_link_type: PathLinkType = dataclasses.field(
        default=PathLinkType.Unknown3,
        metadata={
            "reflection": FieldReflection[PathLinkType](
                PathLinkType,
                id=0x559542AB,
                original_name="PathLinkType",
                from_json=PathLinkType.from_json,
                to_json=PathLinkType.to_json,
            ),
        },
    )
    path_determination_method_type: PathDeterminationMethodType = dataclasses.field(
        default_factory=PathDeterminationMethodType,
        metadata={
            "reflection": FieldReflection[PathDeterminationMethodType](
                PathDeterminationMethodType,
                id=0x4150490C,
                original_name="PathDeterminationMethodType",
                from_json=PathDeterminationMethodType.from_json,
                to_json=PathDeterminationMethodType.to_json,
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
        if property_count != 2:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x559542AB
        path_link_type = PathLinkType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4150490C
        path_determination_method_type = PathDeterminationMethodType.from_stream(data, game, property_size)

        return cls(path_link_type, path_determination_method_type)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"U\x95B\xab")  # 0x559542ab
        data.write(b"\x00\x04")  # size
        self.path_link_type.to_stream(data, game)

        data.write(b"API\x0c")  # 0x4150490c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.path_determination_method_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PathDeterminationJson", data)
        return cls(
            path_link_type=PathLinkType.from_json(json_data["path_link_type"]),
            path_determination_method_type=PathDeterminationMethodType.from_json(
                json_data["path_determination_method_type"]
            ),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "path_link_type": self.path_link_type.to_json(),
            "path_determination_method_type": self.path_determination_method_type.to_json(),
        }


def _decode_path_link_type(data: typing.BinaryIO, game: Game, property_size: int) -> PathLinkType:
    return PathLinkType.from_stream(data, game)


def _decode_path_determination_method_type(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PathDeterminationMethodType:
    return PathDeterminationMethodType.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x559542AB: ("path_link_type", _decode_path_link_type),
    0x4150490C: ("path_determination_method_type", _decode_path_determination_method_type),
}
