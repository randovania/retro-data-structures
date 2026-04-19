from __future__ import annotations

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
