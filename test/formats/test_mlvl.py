import json
import logging
import pathlib
import time

from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.formats.mlvl import Mlvl


_MLVLS = (
    0x3BFA3EFF, # Temple Grounds
    0x863FCD72, # Great Temple
    0x42B935E4, # Agon Wastes
    0x3DFD2249, # Torvus Bog
    0x1BAA96C2, # Sanctuary Fortress
)


def test_mlvl_dependencies(prime2_asset_manager: AssetManager):
    print()
    total_elapsed = 0.0
    
    for mlvl_id in _MLVLS:
        mlvl = prime2_asset_manager.get_file(mlvl_id, Mlvl)
        logging.info(mlvl.world_name)
        
        for area in mlvl.areas:
            old = area.dependencies
            old = {layer_name: set((typ, hex(idx)) for typ, idx in layer) for layer_name, layer in old.items()}
            
            start = time.time()
            area.build_mlvl_dependencies()
            elapsed = time.time()-start
            total_elapsed += elapsed
            
            new = area.dependencies
            new = {layer_name: set((typ, hex(idx)) for typ, idx in layer) for layer_name, layer in new.items()}

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
            missing = {n: list(miss) for n, miss in missing.items() if miss}
            extra = {n: list(ext) for n, ext in extra.items() if ext}
            
            f = pathlib.Path(f"area_deps/{mlvl.world_name}/{area.name}.json")
            msg = f"    {area.name} ({elapsed:.3f}s)"
            if missing or extra:
                if missing:
                    logging.error(msg)
                elif extra:
                    logging.warning(msg)
                f.parent.parent.mkdir(exist_ok=True)
                f.parent.mkdir(exist_ok=True)
                f.touch()
                json.dump({"missing": missing, "extra": extra}, f.open("w"), indent=4)
            else:
                logging.info(msg)
                f.unlink(missing_ok=True)
    
    logging.info(f"Total elapsed time: {total_elapsed}")
