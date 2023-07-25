from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.cskr import Cskr

# Skin


def test_compare_p1(prime1_asset_manager):
    # Resources/NoARAM/Fusion.CSKR
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0x627F684B,
        Cskr,
    )


def test_compare_p2(prime2_asset_manager):
    # Resources/SamusGunLow/Holo.CSKR

    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0xD9828657,
        Cskr,
    )
