import os
from pathlib import Path

import pytest


@pytest.fixture()
def prime1_pwe_project():
    return Path(os.environ["PRIME1_PWE_PROJECT"])


@pytest.fixture()
def prime2_pwe_project():
    return Path(os.environ["PRIME2_PWE_PROJECT"])


@pytest.fixture()
def prime1_paks_path():
    return Path(os.environ["PRIME1_PAKS"])


@pytest.fixture()
def prime2_paks_path():
    return Path(os.environ["PRIME2_PAKS"])

