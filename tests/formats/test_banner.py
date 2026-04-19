from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

from retro_data_structures.formats.banner import Banner

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import IsoFileProvider


def test_decode_prime2_banner_ntsc(prime2_iso_provider: IsoFileProvider) -> None:
    data = prime2_iso_provider.read_binary("opening.bnr")

    banner = Banner.parse(data)
    metadata = banner.metadata
    assert len(metadata) == 1
    assert metadata[0].short_title == "Metroid Prime 2 Echoes"
    assert (
        metadata[0].description
        == "Upon landing on planet Aether, Samus finds\nherself in a battle between Light and Dark."
    )

    image_hash = hashlib.sha256(banner.image.tobytes("raw")).hexdigest()
    assert image_hash == "2330276caef433e6e5defed9af11c8831493527a57dc4dacbb99aad70fccab2d"

    original_image_bytes = banner._raw.image_data
    banner.image = banner.image  # Decodes, then re-encodes and saves to the orignal field
    assert banner._raw.image_data is not original_image_bytes  # Should be a new bytes object, not the original
    assert banner._raw.image_data == original_image_bytes  # But the content should be the same

    encoded = banner.build()
    assert data == encoded


def test_decode_prime2_banner_pal(prime2_pal_iso_provider: IsoFileProvider) -> None:
    data = prime2_pal_iso_provider.read_binary("opening.bnr")

    banner = Banner.parse(data)
    metadata = banner.metadata
    assert len(metadata) == 6
    assert metadata[0].short_title == "Metroid Prime 2 Echoes"
    assert (
        metadata[0].description
        == "Upon landing on planet Aether, Samus finds\nherself in a battle between Light and Dark."
    )
    assert (
        metadata[1].description
        == "Auf dem entlegenen Aether gerät Samus in den\nerbitterten Kampf zwischen Licht und Finsternis!"
    )
    assert (
        metadata[3].description == "Al llegar a Éter, Samus se ve atrapada en\nuna batalla entre la Luz y la Oscuridad."
    )

    encoded = banner.build()
    assert data == encoded
