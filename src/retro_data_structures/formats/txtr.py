"""
https://wiki.axiodl.com/w/TXTR_(File_Format)
"""

from __future__ import annotations

import enum
import io
import math
import typing

import construct
from construct import GreedyBytes, Int16ub, Int32ub, Struct
from PIL import Image

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

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


_BLOCK_SIZES = {
    ImageFormat.I4: (8, 8),
    ImageFormat.I8: (8, 4),
    ImageFormat.IA4: (8, 4),
    ImageFormat.IA8: (4, 4),
    ImageFormat.C4: (8, 8),
    ImageFormat.C8: (8, 8),
    ImageFormat.C14x2: (4, 4),
    ImageFormat.RGB565: (4, 4),
    ImageFormat.RGB5A3: (4, 4),
    ImageFormat.RGBA8: (4, 4),
    ImageFormat.CMPR: (8, 8),
}

TXTRHeader = Struct(
    format=EnumAdapter(ImageFormat),
    width=Int16ub,
    height=Int16ub,
    mipmap_count=Int32ub,
)
TXTR = Struct(
    header=TXTRHeader,
    image_data=GreedyBytes,
)

ColorTuple = tuple[int, int, int, int]


def _get_blocks_i4(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    for value in image_data.read(32):
        intensity = (value >> 4) * 0x11
        yield intensity, intensity, intensity, 0xFF
        intensity = (value & 0b00001111) * 0x11
        yield intensity, intensity, intensity, 0xFF


def _get_blocks_i8(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    for intensity in image_data.read(32):
        yield intensity, intensity, intensity, 0xFF


def _get_blocks_ia4(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    for value in image_data.read(32):
        intensity = 0x11 * (value & 0b00001111)
        alpha = 0x11 * ((value & 0b11110000) >> 4)
        yield intensity, intensity, intensity, alpha


def _get_blocks_ia8(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    for alpha, intensity in zip(*[iter(image_data.read(32))] * 2):
        yield intensity, intensity, intensity, alpha


def _get_blocks_rgb565(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    for _ in range(16):
        value = int.from_bytes(image_data.read(2), "big")
        red = value >> 11
        green = (value >> 5) & 0b111111
        blue = value & 0b11111
        yield red * 0x8, green * 0x4, blue * 0x8, 0xFF


def _get_blocks_rgb5a3(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    for _ in range(16):
        value = int.from_bytes(image_data.read(2), "big")
        if value >> 15:
            # no alpha
            red = (value >> 10) & 0b11111
            green = (value >> 5) & 0b11111
            blue = value & 0b11111
            yield red * 0x8, green * 0x8, blue * 0x8, 0xFF
        else:
            alpha = (value >> 12) & 0b111
            red = (value >> 8) & 0b1111
            green = (value >> 4) & 0b1111
            blue = value & 0b1111
            yield red * 0x11, green * 0x11, blue * 0x11, alpha * 0x20


_GET_BLOCKS_FUNCTIONS = {
    ImageFormat.I4: _get_blocks_i4,
    ImageFormat.I8: _get_blocks_i8,
    ImageFormat.IA4: _get_blocks_ia4,
    ImageFormat.IA8: _get_blocks_ia8,
    ImageFormat.RGB565: _get_blocks_rgb565,
    ImageFormat.RGB5A3: _get_blocks_rgb5a3,
}


def _get_block_data(image_data: io.BytesIO, image_format: ImageFormat) -> list[list[ColorTuple]]:
    block_generator = _GET_BLOCKS_FUNCTIONS[image_format](image_data)

    block_width, block_height = _BLOCK_SIZES[image_format]
    result: list[list[ColorTuple]] = []

    for pixel_y in range(block_height):
        result.append([])
        for pixel_x in range(block_width):
            result[-1].append(next(block_generator))

    return result


def _extract_image(
    image_data: io.BytesIO, image_width: int, image_height: int, image_format: ImageFormat
) -> Image.Image:
    block_width, block_height = _BLOCK_SIZES[image_format]
    blocks_per_row = math.ceil(image_width / block_width)
    num_rows = math.ceil(image_height / block_height)

    img = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    img_pixels = img.load()

    for row in range(num_rows):
        for column in range(blocks_per_row):
            block_data = _get_block_data(image_data, image_format)

            for pixel_y in range(block_height):
                for pixel_x in range(block_width):
                    x = pixel_x + column * block_width
                    y = pixel_y + row * block_height
                    if x < img.width and y < img.height:
                        img_pixels[x, img.height - y - 1] = block_data[pixel_y][pixel_x]

    return img


class Txtr(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "TXTR"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return TXTR

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []

    @property
    def format(self) -> ImageFormat:
        return self._raw.header.format

    @property
    def width(self) -> int:
        return self._raw.header.width

    @property
    def height(self) -> int:
        return self._raw.header.height

    @property
    def mipmap_count(self) -> int:
        return self._raw.header.mipmap_count

    @property
    def image_data(self) -> list[Image.Image]:
        result = []

        image_data = io.BytesIO(self._raw.image_data)
        image_width = self.width
        image_height = self.height

        for mipmap_index in range(self.mipmap_count):
            result.append(_extract_image(image_data, image_width, image_height, self.format))
            image_width = math.floor(image_width / 2)
            image_height = math.floor(image_height / 2)

        return result
