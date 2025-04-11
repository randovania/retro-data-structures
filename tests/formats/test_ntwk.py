from __future__ import annotations

from typing import TYPE_CHECKING

from retro_data_structures.formats.ntwk import Ntwk
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import IsoFileProvider


def perform_test(iso_provider: IsoFileProvider) -> None:
    with iso_provider.open_binary("Standard.ntwk") as f:
        raw = f.read()

    decoded = Ntwk.parse(raw, Game.ECHOES)

    for instance in decoded.instances:
        instance.set_properties(instance.get_properties())

    encoded = decoded.build()

    assert raw == encoded


def test_prime2_ntsc(prime2_iso_provider: IsoFileProvider) -> None:
    perform_test(prime2_iso_provider)


def test_prime2_pal(prime2_pal_iso_provider: IsoFileProvider) -> None:
    perform_test(prime2_pal_iso_provider)
