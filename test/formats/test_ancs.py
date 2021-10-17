from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.formats.ancs import ANCS
from retro_data_structures.game_check import Game


def test_compare_p1(prime1_pwe_project):
    input_path = prime1_pwe_project.joinpath("Resources/Uncategorized/alpha_metaree.ANCS")
    game = Game.PRIME
    raw = input_path.read_bytes()

    data = ANCS.parse(raw, target_game=game)
    encoded = ANCS.build(data, target_game=game)

    assert encoded == raw


def test_compare_p2(prime2_pwe_project):
    input_path = prime2_pwe_project.joinpath("Resources/Uncategorized/annihilatorBeam.ANCS")
    game = Game.ECHOES
    raw = input_path.read_bytes()

    data = ANCS.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    encoded = ANCS.build(data_as_dict, target_game=game)

    assert encoded == raw


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
