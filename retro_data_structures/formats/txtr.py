"""
https://wiki.axiodl.com/w/TXTR_(File_Format)
"""
import enum
import typing

import construct
from construct import Int16ub, GreedyBytes
from construct import Struct, Int32ub

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.game_check import Game


class ImageFormat(enum.IntEnum):
    I4 = 0x0
    I8 = 0x1
    IA4 = 0x2
    IA8 = 0x3
    C4 = 0x4
    C8 = 0x5
    C14x2 = 0x6
    RGB565 = 0x7
    RGB5A3 = 0x8
    RGBA8 = 0x9
    CMPR = 0xA


TXTR = Struct(
    header=Struct(
        format=EnumAdapter(ImageFormat),
        width=Int16ub,
        height=Int16ub,
        mipmap_count=Int32ub,
    ),
    image_data=GreedyBytes,
)


class Txtr(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "TXTR"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return TXTR

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
