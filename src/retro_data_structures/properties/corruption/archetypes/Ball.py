# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BallJson(typing_extensions.TypedDict):
        morph_ball: bool
        boost_ball: bool
        spider_ball: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xF618C8E5, 0x15C99E7A, 0x62FFBD9C)


@dataclasses.dataclass()
class Ball(BaseProperty):
    morph_ball: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF618C8E5, original_name="MorphBall"),
        },
    )
    boost_ball: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x15C99E7A, original_name="BoostBall"),
        },
    )
    spider_ball: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x62FFBD9C, original_name="SpiderBall"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LH?LH?")

        dec = _FAST_FORMAT.unpack(data.read(21))
        assert (dec[0], dec[3], dec[6]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\xf6\x18\xc8\xe5")  # 0xf618c8e5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.morph_ball))

        data.write(b"\x15\xc9\x9ez")  # 0x15c99e7a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.boost_ball))

        data.write(b"b\xff\xbd\x9c")  # 0x62ffbd9c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.spider_ball))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BallJson", data)
        return cls(
            morph_ball=json_data["morph_ball"],
            boost_ball=json_data["boost_ball"],
            spider_ball=json_data["spider_ball"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "morph_ball": self.morph_ball,
            "boost_ball": self.boost_ball,
            "spider_ball": self.spider_ball,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF618C8E5: ("morph_ball", structs.decode_BIG_bool_),
    0x15C99E7A: ("boost_ball", structs.decode_BIG_bool_),
    0x62FFBD9C: ("spider_ball", structs.decode_BIG_bool_),
}
