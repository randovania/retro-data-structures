"""
Decides which resources are compressed in a pak.

- Prime (zlib):
   - TXTR, CMDL, CSKR, ANCS, ANIM and FONT are always compressed.
   - The effects (PART, ELSC, SWHC, WPSC, DPSC and CRSC) are compressed when they're at least 0x400 bytes.
- Echoes (segmented LZO):
   - the same types are compressed when it makes them smaller.
- Later games: nothing is compressed.
"""

from __future__ import annotations

import typing

from retro_data_structures.formats.pak_common import PakFile, _compress
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId, AssetType

ALWAYS_COMPRESSED_TYPES = frozenset({"TXTR", "CMDL", "CSKR", "ANCS", "ANIM", "FONT"})
"""In Prime, these types are always compressed."""

EFFECT_TYPES = frozenset({"PART", "ELSC", "SWHC", "WPSC", "DPSC", "CRSC"})
"""In Prime, these types are compressed when they're at least `PRIME_EFFECT_MIN_SIZE` bytes."""

COMPRESSIBLE_TYPES = ALWAYS_COMPRESSED_TYPES | EFFECT_TYPES
"""The only types that can be compressed in Prime and Echoes."""

PRIME_EFFECT_MIN_SIZE = 0x400


def create_pak_file(
    game: Game,
    asset_id: AssetId,
    asset_type: AssetType,
    data: bytes,
    *,
    force_uncompressed: bool = False,
) -> PakFile:
    """
    Creates the pak entry for a resource, compressed if Retro's packer would compress it.
    :param force_uncompressed: Never compress the resource, for the exceptions where vanilla didn't.
    """
    should_compress = False
    compressed_data = None

    if force_uncompressed or asset_type not in COMPRESSIBLE_TYPES:
        pass

    elif game == Game.PRIME:
        should_compress = asset_type in ALWAYS_COMPRESSED_TYPES or len(data) >= PRIME_EFFECT_MIN_SIZE

    elif game == Game.ECHOES:
        compressed_data = _compress(data, game)
        should_compress = len(compressed_data) < len(data)

    return PakFile(
        asset_id=asset_id,
        asset_type=asset_type,
        should_compress=should_compress,
        uncompressed_data=data,
        compressed_data=compressed_data if should_compress else None,
    )


def should_compress(game: Game, asset_type: AssetType, data: bytes) -> bool:
    """Whether a resource should be compressed."""
    return create_pak_file(game, 0, asset_type, data).should_compress
