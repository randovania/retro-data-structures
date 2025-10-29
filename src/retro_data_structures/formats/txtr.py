"""
https://wiki.axiodl.com/w/TXTR_(File_Format)
"""

from __future__ import annotations

import enum
import io
import math
import struct
import typing

import construct
from construct import GreedyBytes, Int16ub, Int32ub, Struct
from PIL import Image

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency

if typing.TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

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
    ImageFormat.C8: (8, 4),
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
PaletteHeader = Struct(
    format=Int32ub,
    width=Int16ub,
    height=Int16ub,
)
TXTR = Struct(
    header=TXTRHeader,
    image_data=GreedyBytes,
)

ColorTuple = tuple[int, int, int, int]


def _read_palette(image_data: io.BytesIO) -> Sequence[ColorTuple]:
    header = PaletteHeader.parse_stream(image_data)

    match header.format:
        case 0:  # IA8

            def decode(d: bytes) -> ColorTuple:
                intensity, alpha = d
                return intensity, intensity, intensity, alpha
        case 1:  # RGB565

            def decode(d: bytes) -> ColorTuple:
                return _decode_rgb565(int.from_bytes(d, "big"))
        case 2:  # RGB5A3

            def decode(d: bytes) -> ColorTuple:
                return _decode_rgb5a3(int.from_bytes(d, "big"))
        case _:
            raise ValueError("Unexpected format")

    return [decode(image_data.read(2)) for _ in range(header.width * header.height)]


def _get_blocks_i4(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    for value in image_data.read(32):
        intensity = (value >> 4) * 0x11
        yield intensity, intensity, intensity, 0xFF
        intensity = (value & 0b00001111) * 0x11
        yield intensity, intensity, intensity, 0xFF


def _get_blocks_i8(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    for intensity in image_data.read(32):
        yield intensity, intensity, intensity, 0xFF


def _get_blocks_ia4(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    for value in image_data.read(32):
        intensity = 0x11 * (value & 0b00001111)
        alpha = 0x11 * ((value & 0b11110000) >> 4)
        yield intensity, intensity, intensity, alpha


def _get_blocks_ia8(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    for alpha, intensity in zip(*[iter(image_data.read(32))] * 2):
        yield intensity, intensity, intensity, alpha


def _decode_rgb565(value: int) -> ColorTuple:
    red = value >> 11
    green = (value >> 5) & 0b111111
    blue = value & 0b11111
    return red * 0x8, green * 0x4, blue * 0x8, 0xFF


def _get_blocks_rgb565(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    for _ in range(16):
        value = int.from_bytes(image_data.read(2), "big")
        yield _decode_rgb565(value)


def _decode_rgb5a3(value: int) -> ColorTuple:
    if value >> 15:
        # no alpha
        red = (value >> 10) & 0b11111
        green = (value >> 5) & 0b11111
        blue = value & 0b11111
        return red * 0x8, green * 0x8, blue * 0x8, 0xFF
    else:
        alpha = (value >> 12) & 0b111
        red = (value >> 8) & 0b1111
        green = (value >> 4) & 0b1111
        blue = value & 0b1111
        return red * 0x11, green * 0x11, blue * 0x11, alpha * 0x20


def _get_blocks_rgb5a3(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    for _ in range(16):
        yield _decode_rgb5a3(int.from_bytes(image_data.read(2), "big"))


def _get_blocks_rgba8(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    alpha_red = zip(*([iter(image_data.read(32))] * 2))
    green_blue = zip(*([iter(image_data.read(32))] * 2))
    for (alpha, red), (green, blue) in zip(alpha_red, green_blue):
        yield red, green, blue, alpha


def _interpolate(a: ColorTuple, b: ColorTuple, r: float) -> ColorTuple:
    rev = 1 - r
    return (
        int(a[0] * r + b[0] * rev),
        int(a[1] * r + b[1] * rev),
        int(a[2] * r + b[2] * rev),
        int(a[3] * r + b[3] * rev),
    )


def _get_sub_block_cmpr(image_data: io.BytesIO) -> Iterator[ColorTuple]:
    """"""
    palette_a, palette_b = struct.unpack(">HH", image_data.read(4))
    palettes = [_decode_rgb565(palette_a), _decode_rgb565(palette_b)]

    if palette_a > palette_b:
        palettes.append(_interpolate(palettes[0], palettes[1], 2 / 3))
        palettes.append(_interpolate(palettes[0], palettes[1], 1 / 3))
    else:
        palettes.append(_interpolate(palettes[0], palettes[1], 1 / 2))
        palettes.append((0, 0, 0, 0))

    for y in range(4):
        b = int.from_bytes(image_data.read(1))
        for x in range(4):
            shift = 6 - x * 2
            yield palettes[(b >> shift) & 0x3]


def _get_blocks_cmpr(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    """
    A CMPR block (of size 8x8) consists for 4 subblocks of size 4x4.
    Read all these blocks, then reorder the results as expected from _get_block_data.
    """
    rows = [[] for _ in range(8)]

    for y in range(2):
        for x in range(2):
            sub_block = list(_get_sub_block_cmpr(image_data))
            rows[4 * y + 0].extend(sub_block[0:4])
            rows[4 * y + 1].extend(sub_block[4:8])
            rows[4 * y + 2].extend(sub_block[8:12])
            rows[4 * y + 3].extend(sub_block[12:16])
            assert len(sub_block) == 16

    for row in rows:
        yield from row


def _get_blocks_c4(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    assert palette is not None
    for i in image_data.read(32):
        yield palette[i >> 4]
        yield palette[i & 0b1111]


def _get_blocks_c8(image_data: io.BytesIO, palette: Sequence[ColorTuple] | None) -> Iterator[ColorTuple]:
    assert palette is not None
    for i in image_data.read(32):
        yield palette[i]


_GET_BLOCKS_FUNCTIONS = {
    ImageFormat.I4: _get_blocks_i4,
    ImageFormat.I8: _get_blocks_i8,
    ImageFormat.IA4: _get_blocks_ia4,
    ImageFormat.IA8: _get_blocks_ia8,
    ImageFormat.C4: _get_blocks_c4,
    ImageFormat.C8: _get_blocks_c8,
    ImageFormat.RGB565: _get_blocks_rgb565,
    ImageFormat.RGB5A3: _get_blocks_rgb5a3,
    ImageFormat.RGBA8: _get_blocks_rgba8,
    ImageFormat.CMPR: _get_blocks_cmpr,
}


def _get_block_data(
    image_data: io.BytesIO, image_format: ImageFormat, palette: Sequence[ColorTuple] | None
) -> Iterator[tuple[int, int, ColorTuple]]:
    """
    Gets a two-dimensional structure of pixel colors.
    Delegates to _GET_BLOCKS_FUNCTIONS to get a sequence of parsed blocks, then handles the width/height.
    """
    block_width, block_height = _BLOCK_SIZES[image_format]

    block_generator = _GET_BLOCKS_FUNCTIONS[image_format](image_data, palette)
    for pixel_y in range(block_height):
        for pixel_x in range(block_width):
            yield pixel_x, pixel_y, next(block_generator)


def _extract_image(
    image_data: io.BytesIO, image_width: int, image_height: int, image_format: ImageFormat
) -> Image.Image:
    block_width, block_height = _BLOCK_SIZES[image_format]
    blocks_per_row = math.ceil(image_width / block_width)
    num_rows = math.ceil(image_height / block_height)

    palette = None
    if image_format in {ImageFormat.C4, ImageFormat.C8, ImageFormat.C14x2}:
        palette = _read_palette(image_data)

    img = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    img_pixels = img.load()

    flip_y = palette is None

    for row in range(num_rows):
        for column in range(blocks_per_row):
            for pixel_x, pixel_y, pixel_data in _get_block_data(image_data, image_format, palette):
                x = pixel_x + column * block_width
                y = pixel_y + row * block_height
                if x < img.width and y < img.height:
                    img_pixels[x, (img.height - y - 1) if flip_y else y] = pixel_data

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
    def main_image_data(self) -> Image.Image:
        """
        Decodes the main image, ignoring all mipmaps.
        """
        return _extract_image(io.BytesIO(self._raw.image_data), self.width, self.height, self.format)

    @property
    def all_image_data(self) -> list[Image.Image]:
        """
        Decodes the texture data, including all mipmaps.
        """
        result = []

        image_data = io.BytesIO(self._raw.image_data)
        image_width = self.width
        image_height = self.height

        for mipmap_index in range(self.mipmap_count):
            result.append(_extract_image(image_data, image_width, image_height, self.format))
            image_width = math.floor(image_width / 2)
            image_height = math.floor(image_height / 2)

        return result
