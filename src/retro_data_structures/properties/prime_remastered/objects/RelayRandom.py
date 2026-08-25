# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import base64
import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game


@dataclasses.dataclass()
class RelayRandom(BaseProperty):
    unknown_properties: dict[int, bytes] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.LITTLE_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        present_fields["unknown_properties"] = {}

        for _ in range(property_count):
            property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                present_fields["unknown_properties"][property_id] = data.read(property_size)
            assert data.tell() - start == property_size

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 0:
            return None

        return cls()

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(struct.pack("<H", 0 + len(self.unknown_properties)))

        for property_id, property_data in self.unknown_properties.items():
            data.write(struct.pack("<LH", property_id, len(property_data)))
            data.write(property_data)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("json_util.JsonObject", data)
        unknown_properties = typing.cast("dict[str, str]", json_data["unknown_properties"])
        return cls(
            unknown_properties={
                int(property_id, 16): base64.b64decode(property_data)
                for property_id, property_data in unknown_properties.items()
            },
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_properties": {
                hex(property_id): base64.b64encode(property_data).decode("utf-8")
                for property_id, property_data in self.unknown_properties.items()
            }
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {}
