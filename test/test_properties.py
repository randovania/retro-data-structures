import importlib
from pathlib import Path

import pytest

_root = Path(__file__).parents[1]


@pytest.mark.parametrize("path", [
    pytest.param(p.relative_to(_root), id=p.relative_to(_root).as_posix())
    for p in _root.joinpath("retro_data_structures", "properties", "echoes").rglob("*.py")
    if p.name != "__init__.py"
])
def test_import_and_create(path):
    module_name = path.with_suffix("").as_posix().replace("/", ".")
    module = importlib.import_module(module_name)

    module_class = getattr(module, path.stem)
    module_class()
