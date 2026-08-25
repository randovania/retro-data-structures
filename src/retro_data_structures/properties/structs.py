# Generated File
from __future__ import annotations

import struct
import typing

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game

LITTLE_bool_ = struct.Struct("<?")
LITTLE_H = struct.Struct("<H")
LITTLE_L = struct.Struct("<L")
LITTLE_LH = struct.Struct("<LH")
LITTLE_f = struct.Struct("<f")
LITTLE_l = struct.Struct("<l")
BIG_bool_ = struct.Struct(">?")
BIG_H = struct.Struct(">H")
BIG_L = struct.Struct(">L")
BIG_LH = struct.Struct(">LH")
BIG_LHH = struct.Struct(">LHH")
BIG_Q = struct.Struct(">Q")
BIG_f = struct.Struct(">f")
BIG_h = struct.Struct(">h")
BIG_l = struct.Struct(">l")


def decode_BIG_L(data: typing.BinaryIO, game: Game, property_size: int) -> int:
    return BIG_L.unpack(data.read(4))[0]


def decode_BIG_Q(data: typing.BinaryIO, game: Game, property_size: int) -> int:
    return BIG_Q.unpack(data.read(8))[0]


def decode_BIG_bool_(data: typing.BinaryIO, game: Game, property_size: int) -> bool:
    return BIG_bool_.unpack(data.read(1))[0]


def decode_BIG_f(data: typing.BinaryIO, game: Game, property_size: int) -> float:
    return BIG_f.unpack(data.read(4))[0]


def decode_BIG_l(data: typing.BinaryIO, game: Game, property_size: int) -> int:
    return BIG_l.unpack(data.read(4))[0]


def decode_LITTLE_bool_(data: typing.BinaryIO, game: Game, property_size: int) -> bool:
    return LITTLE_bool_.unpack(data.read(1))[0]


def decode_LITTLE_f(data: typing.BinaryIO, game: Game, property_size: int) -> float:
    return LITTLE_f.unpack(data.read(4))[0]


def decode_LITTLE_l(data: typing.BinaryIO, game: Game, property_size: int) -> int:
    return LITTLE_l.unpack(data.read(4))[0]
