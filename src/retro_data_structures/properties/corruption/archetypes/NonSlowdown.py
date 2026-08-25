# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PathType import PathType
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class NonSlowdownJson(typing_extensions.TypedDict):
        path_shape: json_util.JsonObject


@dataclasses.dataclass()
class NonSlowdown(BaseProperty):
    path_shape: PathType = dataclasses.field(
        default_factory=PathType,
        metadata={
            "reflection": FieldReflection[PathType](
                PathType,
                id=0x7FCD6908,
                original_name="PathShape",
                from_json=PathType.from_json,
                to_json=PathType.to_json,
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

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FCD6908
        path_shape = PathType.from_stream(data, game, property_size)

        return cls(path_shape)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b"\x7f\xcdi\x08")  # 0x7fcd6908
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.path_shape.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("NonSlowdownJson", data)
        return cls(
            path_shape=PathType.from_json(json_data["path_shape"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "path_shape": self.path_shape.to_json(),
        }


def _decode_path_shape(data: typing.BinaryIO, game: Game, property_size: int) -> PathType:
    return PathType.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FCD6908: ("path_shape", _decode_path_shape),
}
