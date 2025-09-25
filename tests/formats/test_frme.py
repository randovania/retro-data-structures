from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.formats import Frme, dependency_cheating
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


@pytest.mark.parametrize(
    "asset_id",
    (
        0x13856B27,
        0x58008329,
        0x96BC9B7D,
        0x977252CF,
        0xB5CF0C19,
        0xBAF48D93,
        0xD9D58FA5,
        0xE0BCA226,
    ),
)
def test_p2_pal(prime2_pal_iso_provider, asset_id) -> None:
    asset_manager = AssetManager(prime2_pal_iso_provider, target_game=Game.ECHOES)
    test_lib.parse_and_build_compare(
        asset_manager,
        asset_id,
        Frme,
    )


def test_compare_p2(prime2_asset_manager, frme_asset_id: AssetId) -> None:
    resource, decoded, _ = test_lib.parse_and_build_compare(
        prime2_asset_manager,
        frme_asset_id,
        Frme,
    )

    decoded_deps = list(decoded.dependencies_for())
    cheated_deps = list(dependency_cheating.get_cheated_dependencies(resource, prime2_asset_manager))
    assert decoded_deps == cheated_deps
