import json
import logging
from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.formats.mlvl import Mlvl
import pytest


mlvl_ids = [
    0x3BFA3EFF,
    0x863FCD72,
    0x42B935E4,
    0x3DFD2249,
    0x1BAA96C2,
    # 0x69802220,
    # 0xA50A80CC,
    # 0xAE171602,
    # 0xE3B0C703,
    # 0x233E42BE,
    # 0x406ADD7F,
    # 0x7E19ED26
]
@pytest.mark.parametrize("mlvl_id", mlvl_ids)
def test_mlvl(prime2_asset_manager: AssetManager, mlvl_id):
    # original_deps = {}
    # new_deps = {}

    mlvl = prime2_asset_manager.get_file(mlvl_id, Mlvl)
    print(mlvl)
    # original_deps[mlvl.world_name] = {}
    # new_deps[mlvl.world_name] = {}

    for area in mlvl.areas:
        try:
            print(area.name)
        except:
            pass
        area.build_mlvl_dependencies()
            # old = area.dependencies
            # old = {layer_name: [(typ, hex(idx)) for typ, idx in layer] for layer_name, layer in old.items()}
            # area.build_mlvl_dependencies()
            # new = area.dependencies
            # new = {layer_name: [(typ, hex(idx)) for typ, idx in layer] for layer_name, layer in new.items()}

            # for (layer_name, old_layer), new_layer in zip(old.items(), new.values()):
            #     old_types = set(typ for typ, _ in old_layer)
            #     new_types = set(typ for typ, _ in new_layer)
                
            #     orphaned_types = old_types.symmetric_difference(new_types)
            #     orphaned_types = orphaned_types.difference((
            #         "AGSC",
            #     ))

            #     if len(orphaned_types):
            #         logging.warn(f"Orphaned types in {area.name} layer {layer_name}: {orphaned_types}")
            #         # print(layer_name)
            #         # old_layer = set((typ, _) for typ, _ in old_layer if typ != "AGSC")
            #         # assert old_layer.symmetric_difference(new_layer) == set()

            # original_deps[mlvl.world_name][area.name] = old
            # new_deps[mlvl.world_name][area.name] = new

        # assert original_deps[mlvl.world_name] == new_deps[mlvl.world_name]
    
    # assert original_deps == new_deps
