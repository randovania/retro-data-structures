from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.dcln import Dcln

# Dynamic collision


def test_compare_p1(prime1_asset_manager):
    # Phendrana Shorelines' floating platforms
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0x87ED2F68,
        Dcln,
    )


def test_compare_p2(prime2_asset_manager):
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0x2B755A38,
        Dcln,
    )
