from __future__ import annotations

import dataclasses
import struct
import typing

from retro_data_structures.properties.base_property import BaseProperty

if typing.TYPE_CHECKING:
    import typing_extensions

    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game


@dataclasses.dataclass()
class Color(BaseProperty):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 0.0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(*struct.unpack(game.struct_endianness + "ffff", data.read(16)))

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(struct.pack(game.struct_endianness + "ffff", self.r, self.g, self.b, self.a))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("dict[str, float]", data)
        return cls(json_data["r"], json_data["g"], json_data["b"], json_data["a"])

    def to_json(self) -> json_util.JsonObject:
        return {
            "r": self.r,
            "g": self.g,
            "b": self.b,
            "a": self.a,
        }
