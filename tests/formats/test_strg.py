from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.formats.strg import Strg

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


def test_compare_p1(prime1_asset_manager, strg_asset_id: AssetId):
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        strg_asset_id,
        Strg,
    )


def test_compare_p2(prime2_asset_manager, strg_asset_id: AssetId):
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        strg_asset_id,
        Strg,
    )


@pytest.mark.xfail
def test_compare_p3(prime3_asset_manager):
    # with name table
    # Resources/strings/metroid3/gui/fesliderpopup.STRG
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x0D53311DE8B26040,
        Strg,
    )

    # without name table
    # Resources/strings/uncategorized/Action.STRG
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x8A3242A997AAEDE7,
        Strg,
    )

    # echoes format
    # Resources/strings/metroid2/ingame/languageselection.STRG
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x08417493AF6B57E2,
        Strg,
    )
