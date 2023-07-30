from __future__ import annotations

import pytest
from tests import test_lib

from retro_data_structures.formats.scan import Scan


def test_compare_p1(prime1_asset_manager):
    # Resources/Uncategorized/Chozo Lore 002.SCAN
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0x60AA2A56,
        Scan,
    )


def test_compare_p2(prime2_asset_manager):
    # Resources/Uncategorized/Brizgee_0.SCAN
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0x62572238,
        Scan,
    )


@pytest.mark.xfail
def test_compare_p3(prime3_asset_manager):
    # Resources/uncategorized/Your PED Suit will allow you to absorb this Phazon.SCAN
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        0x5258014E053BFD2C,
        Scan,
    )
