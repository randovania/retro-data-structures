from __future__ import annotations

import io
import typing

import construct
from construct import Array, Bytes, OneOf, Rebuild, Struct

from retro_data_structures.formats.txtr import ImageFormat, _build_image, _extract_image

if typing.TYPE_CHECKING:
    from PIL import Image
    from typing_extensions import Self


class _BannerString(construct.Adapter):
    """
    Strings in the Banner are fixed-length, padded with \x00.
    They're either latin-1 or shift-jis, depending on the game's region.
    """

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

_METADATA_COUNT = {b"BNR1": 1, b"BNR2": 6}
BANNER = Struct(
    "_magic"
    / construct.Aligned(
        32,
        Rebuild(
            OneOf(Bytes(4), [b"BNR1", b"BNR2"]),
            lambda ctx: next(key for key, value in _METADATA_COUNT.items() if value == len(ctx.metadata)),
        ),
    ),
    # Raw bytes for a GX-tiled RGB5A3 96x32 texture — see txtr.py for format details
    "image_data" / Bytes(96 * 32 * 2),
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
        """Decodes the raw image into a Pillow Image object."""
        return _extract_image(io.BytesIO(self._raw.image_data), 96, 32, ImageFormat.RGB5A3, force_flip=False)

    @image.setter
    def image(self, img: Image.Image) -> None:
        self._raw.image_data = _build_image(img, ImageFormat.RGB5A3, force_flip=False)
