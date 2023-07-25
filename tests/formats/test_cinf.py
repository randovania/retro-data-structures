from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.cinf import Cinf

# Skeleton


def test_compare_p1(prime1_asset_manager):
    # Resources/Uncategorized/tickspin.CINF
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0x9A0FAE84,
        Cinf,
    )


def test_compare_p2(prime2_asset_manager):
    # Resources/Uncategorized/Swamplands_Luminoth_Hologram.CINF
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0xD6BA53FA,
        Cinf,
    )
