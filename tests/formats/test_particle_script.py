from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from tests import test_lib

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager


def test_particles_elsc(prime2_asset_manager: AssetManager, elsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, elsc_asset_id)


def test_particles_swhc(prime2_asset_manager: AssetManager, swhc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, swhc_asset_id)


def test_particles_crsc(prime2_asset_manager: AssetManager, crsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(
        prime2_asset_manager,
        crsc_asset_id,
        byte_match=crsc_asset_id
        in {
            0x6091C2BD,
            0x39EB7161,
            0x20174221,
            0x29592460,
            0x31E60852,
            0x6731F933,
            0x4D90E3DA,
            0x4E6CF690,
            0xFBD1B105,
            0x15FDC70A,
            0xAEC26927,
            0x2C9E9ADD,
            0xB0823ECE,
            0xA0C10690,
            0xFB5E6DA1,
            0x5550D412,
            0x13763D25,
            0xB7D3455B,
            0x7FE927EF,
        },
    )


def test_particles_wpsc(prime2_asset_manager: AssetManager, wpsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, wpsc_asset_id)


def test_particles_dpsc(prime2_asset_manager: AssetManager, dpsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, dpsc_asset_id)


def test_particles_srsc(prime2_asset_manager: AssetManager, srsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, srsc_asset_id, byte_match=False)


def test_particles_part(prime2_asset_manager: AssetManager, part_asset_id):
    if part_asset_id in {
        0x851BEE5C,
        0xA40F7D8B,
        0xE03127E6,
        0x4FB5D427,
        0x324CBEBF,
        0xAC4863F1,
        0x5FE8F8CA,
        0x5E41C887,
        0xC7A3AE86,
    }:
        pytest.xfail()
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, part_asset_id)
