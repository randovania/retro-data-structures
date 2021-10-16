import pytest

from retro_data_structures.conversion import conversions
from retro_data_structures.conversion.asset_converter import AssetDetails
from retro_data_structures.game_check import Game


@pytest.mark.parametrize("asset_type", ["ANCS", "ANIM", "CINF", "CMDL", "CSKR", "EVNT", "PART", "TXTR"])
@pytest.mark.parametrize("game", Game)
def test_converter_for(asset_type, game: Game):
    details = AssetDetails(
        asset_id=None,
        asset_type=asset_type,
        original_game=game,
    )
    conversions.converter_for(details)
