import importlib
import io
import typing
from pathlib import Path

import pytest

from retro_data_structures.properties.base_property import BaseProperty

_root = Path(__file__).parents[1]


def perform_module_checks(path: Path):
    module_name = path.with_suffix("").as_posix().replace("/", ".")
    module = importlib.import_module(module_name)

    module_class: typing.Type[BaseProperty] = getattr(module, path.stem)
    obj = module_class()

    stream = io.BytesIO()
    obj.to_stream(stream)
    size = stream.tell()

    stream.seek(0)
    decode = module_class.from_stream(stream, size)

    assert decode == obj

    json_obj = obj.to_json()
    assert json_obj is not None
    decode = module_class.from_json(json_obj)
    assert decode == obj


def _parametrize_for_game(game: str):
    return [
        pytest.param(p.relative_to(_root), id=p.relative_to(_root).as_posix())
        for p in _root.joinpath("retro_data_structures", "properties", game).rglob("*.py")
        if p.name not in ("__init__.py", "AssetId.py")
    ]


@pytest.mark.parametrize("path", _parametrize_for_game("prime"))
def test_import_and_create_prime(path):
    perform_module_checks(path)


@pytest.mark.parametrize("path", _parametrize_for_game("echoes"))
def test_import_and_create_echoes(path):
    perform_module_checks(path)


@pytest.mark.parametrize("path", _parametrize_for_game("corruption"))
def test_import_and_create_corruption(path):
    perform_module_checks(path)


@pytest.mark.parametrize("path", _parametrize_for_game("prime_remastered"))
def test_import_and_create_prime_remastered(path):
    perform_module_checks(path)


def test_door():
    data = (b'\xFF\xFF\xFF\xFF\x06\x9a\x00\x16%ZE\x80\x00H\x00\x04INAM\x00\x05Door\x00XFRM\x00$\xc1\xb6'
            b'\xad\xc9\xc3BwZ\xc26\x9e\xcb\x00\x00\x00\x00\x00\x00\x00\x00C4\x00\x00?\x80\x00\x00?\x80\x00'
            b'\x00?\x80\x00\x00ACTV\x00\x01\x01])\x8aC\x00\x04\x00\x00\x00\x03\xf3D\xc0\xb0\x00\x0c>\xb333@'
            b'\xa0\x00\x00@\x80\x00\x00.hl*\x00\x0c\xbe333\x00\x00\x00\x00@\x00\x00\x00\xcf\x90\xd1^\x00'
            b'\x16\x00\x02\xf0f\x89\x19\x00\x04?\x80\x00\x00:-\x17\xe4\x00\x04?\x80\x00\x00{q\xae\x90\x03'
            b'\xf9\x00\x1d\xac\x8b\xb2\xa7\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04'
            b'\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\xb1\x9bml\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h'
            b'\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\x00$D\xc6\x00\x1d\x00\x03\x85-8q'
            b'\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\xe6\xba\xcd'
            b'\xe5\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}'
            b'\xa2\x00\x01\x01\xd9\x9c\x04\x00\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86'
            b'\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\xc7\r\x8b\x8b\x00\x1d\x00\x03\x85-8q\x00\x04'
            b'\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\x86o\x91\xbf\x00'
            b'\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2'
            b'\x00\x01\x01h\xae\x13\xa0\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04'
            b'\x00\x00\x00\x00\x93g}\xa2\x00\x01\x00\xf0\xb2\xf4\xcf\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8'
            b'\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x00\x00\xef\xe8\xcb\x00\x1d'
            b'\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01'
            b'\x01\xbbp\t?\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00'
            b'\x01\x93g}\xa2\x00\x01\x01\xbf\xac"\x9f\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac'
            b'\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01P\xdd\xe8\x91\x00\x1d\x00\x03\x85-8q'
            b'\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\x97\xb5'
            b'\xc6\x8b\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00'
            b'\x93g}\xa2\x00\x01\x01\xf4\xce\x8a\xcf\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac'
            b'\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\x1dRX\x8d\x00\x1d\x00\x03\x85-8q\x00'
            b'\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01d\xdd\xd5C'
            b'\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}'
            b'\xa2\x00\x01\x01=b_\x10\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04'
            b'\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01Y\x1b\x80\xe3\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00'
            b'\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\xa4B\xb4\xa3\x00\x1d\x00'
            b'\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01*'
            b'\x0f\x05$\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00'
            b'\x93g}\xa2\x00\x01\x01\x94\x9e<\x86\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86'
            b'\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01[\xa9\x91\xb1\x00\x1d\x00\x03\x85-8q\x00\x04B'
            b'\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01i$\xb8\xc1\x00\x1d'
            b'\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01'
            b'\x01\x1a\xb7\x8b\xef\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00'
            b'\x00\x00\x93g}\xa2\x00\x01\x01\xfc\xdc\xb7\xd4\x00\x1d\x00\x03\x85-8q\x00\x04B\xc8\x00\x00h\xac'
            b'\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x011\x1f\xb0a\x00\x1d\x00\x03\x85-8q\x00\x04B'
            b'\xc8\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x01\x89\xd2]\xf4\x00\x1d\x00'
            b'\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}\xa2\x00\x01\x013V'
            b'\xd3~\x00\x1d\x00\x03\x85-8q\x00\x04\x00\x00\x00\x00h\xac\xbd\x86\x00\x04\x00\x00\x00\x00\x93g}'
            b'\xa2\x00\x01\x01\xe2_\xb0\x8c\x00\x0c\xce\xb0\x91\xf7\x00\x00\x00\x00\x00\x00\x00\x03\xb2\x0c\xc2q'
            b'\x00\x04kx\xfd\x92\xae[!\x14\x00\x04kx\xfd\x92G\xb4\xe8c\x00\x10\x00\x00\x00\x00?\x80\x00\x00?\x80'
            b'\x00\x00?\x80\x00\x00%\x89\xc3\xf0\x00\x04\x98\xcb\xbf\xb8~9\x7f\xed\x01M\x00\x11\xb0(\xdb\x0e\x00'
            b'\xa0\x00\x0f\xcdc\x9bF\x00\x01\x01\x1d\x01\x1a9\x00\x04?\x80\x00\x00\xec\xdaAc\x00\x04\x00\x00\x00'
            b'\x00>,\xd3\x8d\x00\x04?\x80\x00\x00\x03(\xe3\x1b\x00\x04A\xa0\x00\x00\xa3>[\x0e\x00\x10?\x80\x00\x00?'
            b'\x80\x00\x00?\x80\x00\x00?\x80\x00\x00\xa7\x18\x10\xe9\x00\x01\x01k^u\t\x00\x04\x00\x00\x00\x01b'
            b'\x8ej\xc3\x00\x04\x00\x00\x00\x01\xd1\x9d\xe7u\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\xca\xc1\xe7x\x00\x04\x00\x00\x00\x04g\xf4\xd3\xde\x00\x04\x00\x00\x00\x04\xfbzz\xbb\x00'
            b'\x01\x01a\xa9@\xd6\x00\x01\x00\x1fq_\xd3\x00\x04\x00\x00\x00\x007[\xfd|\x00\x0c\x00\x01\xb9N\x9b'
            b'\xe7\x00\x04\x18f?9\xc0\xba\x9e\x18\x00\x04\xff\xff\xff\xff\x9f\x02}\x91\x00\x04\xff\xff\xff\xffk'
            b'\x1f\xbc:\x00\x04\xff\xff\xff\xff\xeb\x1d\x06\xbe\x00\x04\xff\xff\xff\xff\x14\x99\x80<\x00\x01\x01'
            b'\x90\xaa4\x1f\x00\x04?\x80\x00\x00|&\x9e\xbc\x00\x04?\x80\x00\x00\x05\xad%\x0e\x00\x13\x00\x02'
            b'\xfe\x9d\xc2f\x00\x01\x00\xca\x19\xe8\xc6\x00\x04\x00\x00\x00\x0f\xcdL\x81\xa1\x00\x01\x00y\x92c'
            b'\xf1\x00\x01\x00\xed:n\x87\x00\x01\x01\xf0y\x81\xe8\x00\x01\x00m\xf38E\x00\x01\x00\xc7\x12\x84|'
            b'\x00\x04\x00\x00\x00\x7f\xba&\x00\xd7\x00\x04\x00\x00\x00\x7f\x85\x01\x15\xe4\x00\x0c\x00\x00\x00'
            b'\x00\x00\x00\x00\x00@ \x00\x00\xa1\xdf\xfa\xd2\x00\x01\x00\xde\xe70\xf5\x00\x01\x00 \x07\xb7\x1d'
            b'\x00\x04?\x00\x00\x00\xf1\xa5\r)\x00\x04?\x00\x00\x00\x06\xdc\xf1\x18\x00\x04>\x80\x00\x00]\xcf\nd'
            b'\x00\x04?\x00\x00\x00\xcd\xcaY+\x00\x04?\x00\x00\x00\xcc\x00\x9f5\x00\x01\x00\xc2\x97e\xea\x00'
            b'\x01\x00\x9e\xc6\'\x12\x00\x0c\x00\x01\xb9N\x9b\xe7\x00\x04\xff\xff\xff\xff')

    from retro_data_structures.properties.echoes.objects import Door
    from retro_data_structures.properties.echoes.core.Color import Color
    from retro_data_structures.properties.echoes.archetypes.WeaponVulnerability import WeaponVulnerability
    from retro_data_structures.enums.echoes import Effect

    door = Door.from_stream(io.BytesIO(data))
    assert door.editor_properties.name == "Door"
    assert door.shell_color == Color(0.0, 1.0, 1.0, 1.0)
    assert door.vulnerability.boost_ball == WeaponVulnerability(0.0, Effect.Normal, True)
