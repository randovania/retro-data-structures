from __future__ import annotations

import os
from pathlib import Path

import pytest

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
from retro_data_structures.game_check import Game
from tests import test_lib

_FAIL_INSTEAD_OF_SKIP = False


def get_env_or_skip(env_name):
    if env_name not in os.environ:
        if _FAIL_INSTEAD_OF_SKIP:
            pytest.fail(f"Missing environment variable {env_name}")
        else:
            pytest.skip(f"Skipped due to missing environment variable {env_name}")
    return os.environ[env_name]


@pytest.fixture(scope="module")
def prime1_iso() -> Path:
    return Path(get_env_or_skip("PRIME1_ISO"))


@pytest.fixture(scope="module")
def prime2_iso() -> Path:
    return Path(get_env_or_skip("PRIME2_ISO"))


@pytest.fixture(scope="module")
def prime2_pal_iso() -> Path:
    return Path(get_env_or_skip("PRIME2_PAL_ISO"))


@pytest.fixture(scope="module")
def prime3_iso() -> Path:
    return Path(get_env_or_skip("PRIME3_ISO"))


@pytest.fixture(scope="module")
def prime1_iso_provider(prime1_iso: Path) -> IsoFileProvider:
    return IsoFileProvider(prime1_iso)


@pytest.fixture(scope="module")
def prime2_iso_provider(prime2_iso: Path) -> IsoFileProvider:
    return IsoFileProvider(prime2_iso)


@pytest.fixture(scope="module")
def prime2_pal_iso_provider(prime2_pal_iso: Path) -> IsoFileProvider:
    return IsoFileProvider(prime2_pal_iso)


@pytest.fixture(scope="module")
def prime3_iso_provider(prime3_iso: Path) -> IsoFileProvider:
    return IsoFileProvider(prime3_iso)


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
    fixture_names: list[str] = list(metafunc.fixturenames)
    asset_manager_fixtures = [fixture for fixture in metafunc.fixturenames if fixture.endswith("_asset_manager")]
    if asset_manager_fixtures:
        asset_id_fixtures = [fixture_name for fixture_name in fixture_names if fixture_name.endswith("_asset_id")]
        if asset_id_fixtures:
            if len(asset_manager_fixtures) > 1:
                raise ValueError("Test has more than one asset_manager")

            game_name = asset_manager_fixtures[0].split("_asset_manager")[0]
            if game_name == "prime1":
                asset_ids = test_lib.PRIME_ASSET_IDS
            elif game_name == "prime2":
                asset_ids = test_lib.ECHOES_ASSET_IDS
            else:
                raise RuntimeError(f"Unsupported {game_name} for id list")

            for fixture_name in asset_id_fixtures:
                asset_type = fixture_name[: -len("_asset_id")]
                asset_ids = [
                    pytest.param(asset.id, id=f"0x{asset.id:08x}")
                    for asset in asset_ids
                    if asset.type.lower() == asset_type
                ]
                if asset_ids:
                    metafunc.parametrize(fixture_name, asset_ids)


def pytest_addoption(parser):
    parser.addoption(
        "--fail-if-missing",
        action="store_true",
        dest="fail_if_missing",
        default=False,
        help="Fails tests instead of skipping, in case any asset is missing",
    )
    parser.addoption(
        "--skip-dependency-tests",
        action="store_true",
        dest="skip_dependency_tests",
        default=False,
        help="Skips tests that involves calculating dependencies",
    )


def pytest_configure(config: pytest.Config):
    global _FAIL_INSTEAD_OF_SKIP  # noqa: PLW0603
    _FAIL_INSTEAD_OF_SKIP = config.option.fail_if_missing

    markers = []

    if config.option.skip_dependency_tests:
        markers.append("not skip_dependency_tests")

    config.option.markexpr = " and ".join(markers)
