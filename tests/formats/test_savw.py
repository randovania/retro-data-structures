from __future__ import annotations

from typing import TYPE_CHECKING

from tests import test_lib

from retro_data_structures.formats import Savw

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


def test_compare_p1(prime1_asset_manager, savw_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        savw_asset_id,
        Savw,
    )


def test_compare_p2(prime2_asset_manager, savw_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        savw_asset_id,
        Savw,
    )


def test_compare_p3(prime3_asset_manager, savw_asset_id: AssetId) -> None:
    test_lib.parse_and_build_compare(
        prime3_asset_manager,
        savw_asset_id,
        Savw,
    )
