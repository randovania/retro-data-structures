from retro_data_structures.asset_manager import AssetManager
from test import test_lib


def test_particles_elsc(prime2_asset_manager: AssetManager, elsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, elsc_asset_id)


def test_particles_swhc(prime2_asset_manager: AssetManager, swhc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, swhc_asset_id)


def test_particles_crsc(prime2_asset_manager: AssetManager, crsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, crsc_asset_id)


def test_particles_wpsc(prime2_asset_manager: AssetManager, wpsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, wpsc_asset_id)


def test_particles_dpsc(prime2_asset_manager: AssetManager, dpsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, dpsc_asset_id)


def test_particles_srsc(prime2_asset_manager: AssetManager, srsc_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, srsc_asset_id)


def test_particles_part(prime2_asset_manager: AssetManager, part_asset_id):
    test_lib.parse_and_build_compare_auto_manager(prime2_asset_manager, part_asset_id)
