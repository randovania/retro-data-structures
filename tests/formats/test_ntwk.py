from __future__ import annotations

from typing import TYPE_CHECKING

from retro_data_structures.formats.ntwk import Ntwk
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import IsoFileProvider


def test_prime2(prime2_iso_provider: IsoFileProvider) -> None:
    with prime2_iso_provider.open_binary("Standard.ntwk") as f:
        raw = f.read()

    decoded = Ntwk.parse(raw, Game.ECHOES)
    encoded = decoded.build()

    assert raw == encoded
