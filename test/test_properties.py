import importlib
import io
from pathlib import Path

import pytest

_root = Path(__file__).parents[1]


@pytest.mark.parametrize("path", [
    pytest.param(p.relative_to(_root), id=p.relative_to(_root).as_posix())
    for p in _root.joinpath("retro_data_structures", "properties", "echoes").rglob("*.py")
    if p.name not in ("__init__.py", "AssetId.py")
])
def test_import_and_create(path):
    module_name = path.with_suffix("").as_posix().replace("/", ".")
    module = importlib.import_module(module_name)

    module_class = getattr(module, path.stem)
    obj = module_class()

    stream = io.BytesIO()
    obj.to_stream(stream)
    size = stream.tell()

    stream.seek(0)
    decode = module_class.from_stream(stream, size)

    assert decode == obj
