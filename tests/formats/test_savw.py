from __future__ import annotations

import copy
from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.formats import Savw
from retro_data_structures.formats.mlvl import Mlvl

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId

_ECHOES_SAVW = 0x32E95269


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


@pytest.mark.xfail
def test_rebuild_p1(prime1_asset_manager, mlvl_asset_id: AssetId) -> None:
    mlvl = prime1_asset_manager.get_parsed_asset(mlvl_asset_id, type_hint=Mlvl)

    original_savw = copy.deepcopy(mlvl.savw.raw)
    mlvl.rebuild_savw()

    assert test_lib.purge_hidden(original_savw, ordered=False) == test_lib.purge_hidden(mlvl.savw.raw, ordered=False)


def test_rebuild_p2(prime2_asset_manager, mlvl_asset_id: AssetId) -> None:
    mlvl = prime2_asset_manager.get_parsed_asset(mlvl_asset_id, type_hint=Mlvl)

    original_savw = copy.deepcopy(mlvl.savw.raw)
    mlvl.rebuild_savw()

    assert test_lib.purge_hidden(original_savw, ordered=False) == test_lib.purge_hidden(mlvl.savw.raw, ordered=False)


@pytest.mark.xfail
def test_rebuild_p3(prime3_asset_manager, mlvl_asset_id: AssetId) -> None:
    mlvl = prime3_asset_manager.get_parsed_asset(mlvl_asset_id, type_hint=Mlvl)

    original_savw = copy.deepcopy(mlvl.savw.raw)
    mlvl.rebuild_savw()

    assert test_lib.purge_hidden(original_savw, ordered=False) == test_lib.purge_hidden(mlvl.savw.raw, ordered=False)
