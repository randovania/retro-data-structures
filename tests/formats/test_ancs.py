from __future__ import annotations

from tests import test_lib

from retro_data_structures.formats.ancs import Ancs


def test_compare_p1(prime1_asset_manager):
    # Resources/Uncategorized/alpha_metaree.ANCS
    test_lib.parse_and_build_compare(
        prime1_asset_manager,
        0xBBEE2818,
        Ancs,
    )


def test_compare_p2(prime2_asset_manager):
    # Resources/Uncategorized/annihilatorBeam.ANCS
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        0x4C4B3D9D,
        Ancs,
    )


"""
def test_dependencies_all_p1(prime1_pwe_project):
    pak_path = prime1_pwe_project.joinpath("Disc", "files")
    with AssetProvider(Game.PRIME, list(pak_path.glob("*.pak"))) as asset_provider:
        asset_ids = [
            asset_id
            for asset_id, (resource, _) in asset_provider._resource_by_asset_id.items()
            if resource.asset.type == "ANCS"
        ]

        for asset_type, asset_id in dependencies.recursive_dependencies_for(asset_provider, asset_ids):
            print("{}: {}".format(asset_type, hex(asset_id)))
            """
