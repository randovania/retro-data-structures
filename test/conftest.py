import os
from pathlib import Path

import pytest

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
from retro_data_structures.game_check import Game
from test import test_lib


def get_env_or_skip(env_name):
    if env_name not in os.environ:
        pytest.skip(f"Skipped due to missing environment variable {env_name}")
    return os.environ[env_name]


@pytest.fixture()
def prime1_pwe_project():
    return Path(get_env_or_skip("PRIME1_PWE_PROJECT"))


@pytest.fixture()
def prime2_pwe_project():
    return Path(get_env_or_skip("PRIME2_PWE_PROJECT"))


@pytest.fixture()
def prime3_pwe_project():
    return Path(get_env_or_skip("PRIME3_PWE_PROJECT"))


@pytest.fixture()
def prime1_paks_path():
    return Path(get_env_or_skip("PRIME1_PAKS"))


@pytest.fixture()
def prime2_paks_path():
    return Path(get_env_or_skip("PRIME2_PAKS"))


@pytest.fixture()
def prime3_paks_path():
    return Path(get_env_or_skip("PRIME3_PAKS"))


@pytest.fixture(scope="module")
def prime1_asset_manager():
    return AssetManager(IsoFileProvider(Path(get_env_or_skip("PRIME1_ISO"))),
                        target_game=Game.PRIME)


@pytest.fixture(scope="module")
def prime2_asset_manager():
    return AssetManager(IsoFileProvider(Path(get_env_or_skip("PRIME2_ISO"))),
                        target_game=Game.ECHOES)


@pytest.fixture(scope="module")
def prime3_asset_manager():
    return AssetManager(IsoFileProvider(Path(get_env_or_skip("PRIME3_ISO"))),
                        target_game=Game.CORRUPTION)


def pytest_generate_tests(metafunc):
    if any("_asset_manager" in fixture for fixture in metafunc.fixturenames):
        for fixture_name in metafunc.fixturenames:
            assert isinstance(fixture_name, str)
            if fixture_name.endswith("_asset_id"):
                asset_type = fixture_name[:-len("_asset_id")]
                asset_ids = [
                    pytest.param(asset.id, id=f"0x{asset.id:08x}")
                    for asset in test_lib.ECHOES_ASSET_IDS
                    if asset.type.lower() == asset_type
                ]
                if asset_ids:
                    metafunc.parametrize(fixture_name, asset_ids)
