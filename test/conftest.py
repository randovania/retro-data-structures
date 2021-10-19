import os
from pathlib import Path

import pytest


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
