from __future__ import annotations

import json
import logging
import os
import pathlib
import time
from typing import TYPE_CHECKING

import pytest
from tests import test_lib

from retro_data_structures.formats.mlvl import Mlvl
from retro_data_structures.formats.mrea import AreaDependencies

if TYPE_CHECKING:
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import AssetId

_MLVLS = (
    0x3BFA3EFF,  # Temple Grounds
    0x863FCD72,  # Great Temple
    0x42B935E4,  # Agon Wastes
    0x3DFD2249,  # Torvus Bog
    0x1BAA96C2,  # Sanctuary Fortress
)

_EXPECTED_DEPENDENCY = {
    "Great Temple": {},
    "Torvus Bog": {
        "Torvus Lagoon": {"missing": {}, "extra": {"1st Pass": {("PART", "0x28747f78")}}},
        "Ruined Alcove": {"missing": {}, "extra": {"1st Pass": {("PART", "0x28747f78")}}},
        "Undertemple": {"missing": {}, "extra": {"Ingsporb battle": {("AGSC", "0xfa61924c")}}},
    },
    "Sanctuary Fortress": {"Entrance Defense Hall": {"missing": {}, "extra": {"1st pass": {("AGSC", "0xc8739bec")}}}},
    "Temple Grounds": {
        "Hive Chamber A": {"missing": {}, "extra": {"Default": {("TXTR", "0xbf916e5a")}}},
        "Trooper Security Station": {
            "missing": {},
            "extra": {
                "2nd Pass": {
                    ("CMDL", "0xa33ef428"),
                    ("TXTR", "0x286d4e4a"),
                    ("TXTR", "0x5a7f9d53"),
                }
            },
        },
    },
    "Agon Wastes": {
        "Agon Temple": {
            "missing": {},
            "extra": {
                "1st pass enemy_Bomb Boss": {
                    ("CMDL", "0x792f1949"),
                    ("CMDL", "0x952eae59"),
                }
            },
        }
    },
}


def _write_to_file(data: dict, path: pathlib.Path):
    path.parent.mkdir(exist_ok=True, parents=True)
    path.touch()

    with path.open("w") as of:
        json.dump(data, of, indent=4)


@pytest.mark.skip_dependency_tests
def test_mlvl_dependencies(prime2_asset_manager: AssetManager):
    print()
    total_elapsed = 0.0

    write_reports = os.environ.get("WRITE_DEPENDENCIES_REPORTS", "") != ""

    world_reports = {}

    for mlvl_id in _MLVLS:
        mlvl = prime2_asset_manager.get_file(mlvl_id, Mlvl)
        logging.info(mlvl.world_name)
        world_reports[mlvl.world_name] = {}

        for area in mlvl.areas:
            old = area.dependencies_by_layer
            old = {layer_name: {(dep.type, hex(dep.id)) for dep in layer} for layer_name, layer in old.items()}

            start = time.time()
            area.build_mlvl_dependencies()
            elapsed = time.time() - start
            total_elapsed += elapsed

            new = area.dependencies_by_layer
            new = {layer_name: {(dep.type, hex(dep.id)) for dep in layer} for layer_name, layer in new.items()}

            missing = {
                layer_name: old_layer.difference(new_layer)
                for (layer_name, old_layer), new_layer in zip(old.items(), new.values())
            }
            extra = {
                layer_name: new_layer.difference(old_layer)
                for (layer_name, old_layer), new_layer in zip(old.items(), new.values())
            }
            missing = {n: miss for n, miss in missing.items() if miss}
            extra = {n: ext for n, ext in extra.items() if ext}

            f = pathlib.Path(f"area_deps/{mlvl.world_name}/{area.name}.json")
            msg = f"    {area.name} ({elapsed:.3f}s)"
            if missing or extra:
                if missing:
                    logging.error(msg)
                elif extra:
                    logging.warning(msg)

                world_reports[mlvl.world_name][area.name] = {"missing": missing, "extra": extra}
                if write_reports:
                    _write_to_file(
                        {
                            "missing": {n: list(miss) for n, miss in missing.items() if miss},
                            "extra": {n: list(ext) for n, ext in extra.items() if ext},
                        },
                        f,
                    )
            else:
                logging.info(msg)
                if write_reports:
                    f.unlink(missing_ok=True)

    logging.info(f"Total elapsed time: {total_elapsed}")
    assert world_reports == _EXPECTED_DEPENDENCY


_EXPECTED_MODULES = {
    "Temple Grounds": {},
    "Great Temple": {},
    "Agon Wastes": {},
    "Torvus Bog": {},
    "Sanctuary Fortress": {},
}


@pytest.mark.skip_dependency_tests
def test_module_dependencies(prime2_asset_manager: AssetManager):
    write_reports = os.environ.get("WRITE_DEPENDENCIES_REPORTS", "") != ""

    world_reports = {}

    for mlvl_id in _MLVLS:
        mlvl = prime2_asset_manager.get_file(mlvl_id, Mlvl)
        logging.info(mlvl.world_name)
        world_reports[mlvl.world_name] = {}

        for area in mlvl.areas:
            old = area.module_dependencies_by_layer
            area.build_module_dependencies()
            new = area.module_dependencies_by_layer

            f = pathlib.Path(f"area_deps/{mlvl.world_name}/{area.name}.json")
            msg = f"    {area.name}"
            if old != new:
                logging.error(msg)
                world_reports[mlvl.world_name][area.name] = {"old": old, "new": new}
                if write_reports:
                    _write_to_file(world_reports[mlvl.world_name][area.name], f)
            else:
                logging.info(msg)
                if write_reports:
                    f.unlink(missing_ok=True)

    assert world_reports == _EXPECTED_MODULES


def test_compare_mlvl(prime2_asset_manager: AssetManager):
    mlvl_id = 0x3BFA3EFF
    mlvl = prime2_asset_manager.get_parsed_asset(mlvl_id, type_hint=Mlvl)

    old_deps: AreaDependencies = mlvl.raw.areas[0].dependencies
    old_deps = AreaDependencies(old_deps.layers, old_deps.non_layer)

    area = next(mlvl.areas)
    area.update_all_dependencies()

    prime2_asset_manager.replace_asset(mlvl_id, mlvl)
    new = prime2_asset_manager.get_parsed_asset(mlvl_id, type_hint=Mlvl)

    new_deps: AreaDependencies = new.raw.areas[0]["dependencies"]

    assert old_deps == new_deps
    assert set(old_deps.all_dependencies) == set(new_deps.all_dependencies)


def test_compare_p1(prime1_asset_manager, mlvl_asset_id: AssetId):
    # FIXME: what's actually wrong here?
    with pytest.raises(KeyError):
        test_lib.parse_and_build_compare(
            prime1_asset_manager,
            mlvl_asset_id,
            Mlvl,
        )


def test_compare_p2(prime2_asset_manager, mlvl_asset_id: AssetId):
    test_lib.parse_and_build_compare(
        prime2_asset_manager,
        mlvl_asset_id,
        Mlvl,
    )


# Textures that vanilla lists among those of a model, but that nothing uses. Probably from older versions of the
# models.
_PRIME_STALE_MINES_TEXTURES = {
    ("TXTR", 0x342F5F5B),
    ("TXTR", 0x34CBBF23),
    ("TXTR", 0x3C2D48A9),
    ("TXTR", 0x0469B47D),
    ("TXTR", 0x58994B6A),
    ("TXTR", 0x5F56CB9E),
    ("TXTR", 0x7717E9B7),
    ("TXTR", 0x86FAB12C),
    ("TXTR", 0xC4A75BC8),
}

# For each MREA and layer, the dependencies vanilla lists that aren't found, and the ones found that vanilla doesn't
# list. The extras are all listed in another layer of the same area.
_PRIME_EXPECTED_DEPENDENCY = {
    0xD5CDB809: {"extra": {"Default": {("AFSM", 0xE23DFB53)}, "First Pass": {("AFSM", 0xE23DFB53)}}},
    0x3C785450: {"extra": {"Default": {("AFSM", 0xE23DFB53)}}},
    0x8A97BB54: {
        "missing": {
            "3rd Pass Elite Bustout": {("TXTR", 0x3901C7C4), ("TXTR", 0xBB9590D9)},
            "Dummy Elite": {
                ("TXTR", 0x2AC64BC1),
                ("TXTR", 0x2BFBDE65),
                ("TXTR", 0x3901C7C4),
                ("TXTR", 0x68919D46),
                ("TXTR", 0xBB9590D9),
            },
        }
    },
    0x3F375ECC: {"extra": {"Default": {("PART", 0x19723E43)}, "1st Pass enemies": {("PART", 0x19723E43)}}},
    0xF517A1EA: {
        "missing": {"!!non_layer!!": {("TXTR", 0x5A369D26)}},
        "extra": {"Default": {("STRG", 0x0C476789)}},
    },
    0x67156A0D: {"missing": {"Default": _PRIME_STALE_MINES_TEXTURES}},
    0xDADF06C3: {"missing": {"Default": _PRIME_STALE_MINES_TEXTURES}},
    0x0749DF46: {"missing": {"Default": _PRIME_STALE_MINES_TEXTURES}},
    0x7A3AD91E: {"missing": {"Default": _PRIME_STALE_MINES_TEXTURES}},
    0xA7AC009B: {"missing": {"Default": _PRIME_STALE_MINES_TEXTURES}},
}

# An ActorKeyframe has a FadeOut of 2, which these templates don't accept
_PRIME_AREAS_THAT_FAIL = {0x956F1552}


@pytest.mark.skip_dependency_tests
def test_prime_mlvl_dependencies(prime1_asset_manager: AssetManager):
    mlvl_ids = [
        asset_id
        for asset_id in prime1_asset_manager.all_asset_ids()
        if prime1_asset_manager.get_asset_type(asset_id) == "MLVL"
    ]
    assert len(mlvl_ids) == 8

    differences = {}
    for mlvl_id in mlvl_ids:
        mlvl = prime1_asset_manager.get_file(mlvl_id, Mlvl)
        for area in mlvl.areas:
            old = {name: {(dep.type, dep.id) for dep in layer} for name, layer in area.dependencies_by_layer.items()}
            if area.mrea_asset_id in _PRIME_AREAS_THAT_FAIL:
                with pytest.raises(ValueError, match="is not a valid FadeOut"):
                    area.build_mlvl_dependencies()
                continue

            area.build_mlvl_dependencies()
            new = {name: {(dep.type, dep.id) for dep in layer} for name, layer in area.dependencies_by_layer.items()}

            missing = {name: old[name] - new[name] for name in old if old[name] - new[name]}
            extra = {name: new[name] - old[name] for name in old if new[name] - old[name]}
            if missing or extra:
                differences[area.mrea_asset_id] = {
                    key: value for key, value in (("missing", missing), ("extra", extra)) if value
                }

    assert differences == _PRIME_EXPECTED_DEPENDENCY
