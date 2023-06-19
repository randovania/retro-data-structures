import os
from pathlib import Path
from test import test_lib

import pytest

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
from retro_data_structures.game_check import Game

_FAIL_INSTEAD_OF_SKIP = False


def get_env_or_skip(env_name):
    if env_name not in os.environ:
        if _FAIL_INSTEAD_OF_SKIP:
            pytest.fail(f"Missing environment variable {env_name}")
        else:
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


@pytest.fixture(scope="module")
def prime1_iso_provider():
    return IsoFileProvider(Path(get_env_or_skip("PRIME1_ISO")))


@pytest.fixture(scope="module")
def prime2_iso_provider():
    return IsoFileProvider(Path(get_env_or_skip("PRIME2_ISO")))


@pytest.fixture(scope="module")
def prime3_iso_provider():
    return IsoFileProvider(Path(get_env_or_skip("PRIME3_ISO")))


@pytest.fixture(scope="module")
def prime1_asset_manager(prime1_iso_provider):
    return AssetManager(prime1_iso_provider, target_game=Game.PRIME)


@pytest.fixture(scope="module")
def prime2_asset_manager(prime2_iso_provider):
    return AssetManager(prime2_iso_provider, target_game=Game.ECHOES)


@pytest.fixture(scope="module")
def prime3_asset_manager(prime3_iso_provider):
    return AssetManager(prime3_iso_provider, target_game=Game.CORRUPTION)


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


def pytest_addoption(parser):
    parser.addoption('--fail-if-missing', action='store_true', dest="fail_if_missing",
                     default=False, help="Fails tests instead of skipping, in case any asset is missing")


def pytest_configure(config):
    global _FAIL_INSTEAD_OF_SKIP
    _FAIL_INSTEAD_OF_SKIP = config.option.fail_if_missing
