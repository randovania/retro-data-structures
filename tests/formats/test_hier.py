from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.hier import Hier


def test_compare_p2(prime2_asset_manager):
    # Resources/NoARAM/DUMB_ScanHierarchy.DUMB

    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0xDD79DC2A,
        Hier,
    )
