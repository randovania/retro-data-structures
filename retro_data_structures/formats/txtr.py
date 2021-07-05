"""
https://wiki.axiodl.com/w/TXTR_(File_Format)
"""
import enum

from construct import Struct, Int16ub, Int32ub, GreedyBytes

from retro_data_structures.construct_extensions import EnumAdapter


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
