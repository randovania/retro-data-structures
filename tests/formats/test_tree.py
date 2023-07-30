from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.tree import TREE


def test_compare_p2(prime2_asset_manager):
    # Resources/Logbook/DUMB_ScanTree.DUMB
    test_lib.parse_and_build_compare_construct(
        prime2_asset_manager,
        0x95B61279,
        TREE,
    )
