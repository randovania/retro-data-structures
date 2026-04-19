from __future__ import annotations

import io
import typing

import construct
from construct import Array, Bytes, OneOf, Padding, Rebuild, Struct

from retro_data_structures.formats.txtr import ImageFormat, _build_image, _extract_image

if typing.TYPE_CHECKING:
    from PIL import Image
    from typing_extensions import Self

_METADATA_COUNT = {b"BNR1": 1, b"BNR2": 6}
_MAGIC_FROM_COUNT = {1: b"BNR1", 6: b"BNR2"}


class _BannerString(construct.Adapter):
    def __init__(self, length: int):
        self._field_length = length
        super().__init__(Bytes(length))

    @staticmethod
    def _encoding(context: construct.Container) -> str:
        try:
            use_shift_jis = context._root._params.use_shift_jis
        except AttributeError:
            use_shift_jis = False
        return "shift_jis" if use_shift_jis else "latin-1"

    def _decode(self, obj: bytes, context: construct.Container, path: str) -> str:
        return obj.rstrip(b"\x00").decode(self._encoding(context))

    def _encode(self, obj: str, context: construct.Container, path: str) -> bytes:
        return obj.encode(self._encoding(context)).ljust(self._field_length, b"\x00")


# Each metadata block is 0x140 (320) bytes and describes one language entry.
# BNR1 has one block (US or JP); BNR2 has six (English, German, French, Spanish, Italian, Dutch).
MetadataBlock = Struct(
    "short_title" / _BannerString(32),
    "short_developer" / _BannerString(32),
    "long_title" / _BannerString(64),
    "long_developer" / _BannerString(64),
    "description" / _BannerString(128),
)

# Image data is a 96x32 pixel GX-tiled RGB5A3 texture (6144 bytes).
# RGB5A3 encodes each pixel as 16 bits: if the high bit is 1, the pixel is
# opaque RGB555; if 0, the pixel has 3-bit alpha and 4-bit RGB444.
# Pixels are stored in 4x4 tiles in row-major tile order (standard GX tiling).
# Conversion to/from a standard RGBA bitmap is not implemented here.
BANNER = Struct(
    "_magic"
    / Rebuild(
        OneOf(Bytes(4), [b"BNR1", b"BNR2"]),
        lambda ctx: _MAGIC_FROM_COUNT[len(ctx.metadata)],
    ),
    "_padding" / Padding(28),
    # Raw GX-tiled RGB5A3 texture data — see comment above for format details
    "image_data" / Bytes(6144),
    "metadata" / Array(lambda ctx: _METADATA_COUNT[ctx._magic], MetadataBlock),
)


class Banner:
    _raw: construct.Container
    _use_shift_jis: bool

    def __init__(self, raw: construct.Container, use_shift_jis: bool = False):
        self._raw = raw
        self._use_shift_jis = use_shift_jis

    @classmethod
    def construct_class(cls) -> construct.Construct:
        return BANNER

    @classmethod
    def parse(cls, data: bytes, use_shift_jis: bool = False) -> Self:
        return cls(cls.construct_class().parse(data, use_shift_jis=use_shift_jis), use_shift_jis)

    def build(self) -> bytes:
        return self.construct_class().build(self._raw, use_shift_jis=self._use_shift_jis)

    @property
    def raw(self) -> construct.Container:
        return self._raw

    @property
    def metadata(self) -> construct.Container:
        return self._raw.metadata

    @property
    def image(self) -> Image.Image:
        return _extract_image(io.BytesIO(self._raw.image_data), 96, 32, ImageFormat.RGB5A3, force_flip=False)

    @image.setter
    def image(self, img: Image.Image) -> None:
        self._raw.image_data = _build_image(img, ImageFormat.RGB5A3, force_flip=False)
