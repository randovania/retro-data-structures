import json
import logging
import pathlib
import time

import pytest

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.formats.mlvl import Mlvl

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
        "Torvus Lagoon": {
            "missing": {},
            "extra": {
                "1st Pass": {("PART", "0x28747f78")}
            }
        },
        "Ruined Alcove": {
            "missing": {},
            "extra": {
                "1st Pass": {("PART", "0x28747f78")}
            }
        },
        "Undertemple": {
            "missing": {},
            "extra": {
                "Ingsporb battle": {("AGSC", "0xfa61924c")}
            }
        }
    },
    "Sanctuary Fortress": {
        "Entrance Defense Hall": {
            "missing": {},
            "extra": {
                "1st pass": {("AGSC", "0xc8739bec")}
            }
        }
    },
    "Temple Grounds": {
        "Hive Chamber A": {
            "missing": {},
            "extra": {
                "Default": {("TXTR", "0xbf916e5a")}
            }
        },
        "Trooper Security Station": {
            "missing": {},
            "extra": {
                "2nd Pass": {
                    ("CMDL", "0xa33ef428"),
                    ("TXTR", "0x286d4e4a"),
                    ("TXTR", "0x5a7f9d53"),
                }
            }
        }
    },
    "Agon Wastes": {
        "Agon Temple": {
            "missing": {},
            "extra": {
                "1st pass enemy_Bomb Boss": {
                    ("CMDL", "0x792f1949"),
                    ("CMDL", "0x952eae59"),
                }
            }
        }
    }
}


@pytest.mark.skip_dependency_tests
def test_mlvl_dependencies(prime2_asset_manager: AssetManager):
    print()
    total_elapsed = 0.0

    world_reports = {}

    for mlvl_id in _MLVLS:
        mlvl = prime2_asset_manager.get_file(mlvl_id, Mlvl)
        logging.info(mlvl.world_name)
        world_reports[mlvl.world_name] = {}

        for area in mlvl.areas:
            old = area.dependencies
            old = {layer_name: set((typ, hex(idx)) for typ, idx, _ in layer) for layer_name, layer in old.items()}

            start = time.time()
            area.build_mlvl_dependencies()
            elapsed = time.time() - start
            total_elapsed += elapsed

            new = area.dependencies
            new = {layer_name: set((typ, hex(idx)) for typ, idx, _ in layer) for layer_name, layer in new.items()}

            missing = {
                layer_name: old_layer.difference(new_layer)
                for (layer_name, old_layer), new_layer
                in zip(old.items(), new.values())
            }
            extra = {
                layer_name: new_layer.difference(old_layer)
                for (layer_name, old_layer), new_layer
                in zip(old.items(), new.values())
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
                f.parent.mkdir(exist_ok=True, parents=True)
                f.touch()

                world_reports[mlvl.world_name][area.name] = {"missing": missing, "extra": extra}
                with f.open("w") as of:
                    json.dump(
                        {"missing": {n: list(miss) for n, miss in missing.items() if miss},
                         "extra": {n: list(ext) for n, ext in extra.items() if ext}},
                        of, indent=4)
            else:
                logging.info(msg)
                f.unlink(missing_ok=True)

    logging.info(f"Total elapsed time: {total_elapsed}")
    assert world_reports == _EXPECTED_DEPENDENCY
