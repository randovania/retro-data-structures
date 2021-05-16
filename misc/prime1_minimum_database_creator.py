import argparse
import functools
import json
import pprint
import struct
from pathlib import Path
from typing import Any, List, Dict

import construct
from construct import Struct, Int32ub, Int64ub, PrefixedArray, Array, Float32b, Int16ub, Int8ub, CString, PaddedString, \
    PascalString


def find_worlds(base):
    return base.rglob("*.MLVL.rsmeta")


def get_strg_id(meta):
    with meta.open("rb") as f:
        return struct.unpack_from(">I", f.read(), 32)[0]


def get_mlvl_id(meta):
    with meta.open("rb") as f:
        return struct.unpack_from(">I", f.read(), 32) [0]


AssetId = Int32ub
Vector3 = Array(3, Float32b)

MLVLMemoryRelay = Struct(
    memory_relay_index=Int32ub,
    target_index=Int32ub,
    message=Int16ub,
    active=Int8ub,
)

MLVLConnectingDock = Struct(
    area_index=Int32ub,
    dock_index=Int32ub,
)

MLVLDock = Struct(
    connecting_dock=PrefixedArray(Int32ub, MLVLConnectingDock),
    dock_coordinates=PrefixedArray(Int32ub, Vector3),
)

MLVLAreaDependency = Struct(
    asset_id=AssetId,
    asset_type=PaddedString(4, "utf-8")
)

MLVLAreaDependencies = Struct(
    unknown=Int32ub,
    dependencies=PrefixedArray(Int32ub, MLVLAreaDependency),
    dependencies_offset=PrefixedArray(Int32ub, Int32ub),
)

MLVLArea = Struct(
    area_name_id=AssetId,
    area_transform=Array(12, Float32b),
    area_bounding_box=Array(6, Float32b),
    area_mrea_id=AssetId,
    internal_area_id=AssetId,
    attached_area_index=PrefixedArray(Int32ub, Int16ub),
    dependencies=MLVLAreaDependencies,
    docks=PrefixedArray(Int32ub, MLVLDock),
)

Prime1MLVL = Struct(
    magic=Int32ub,
    version=Int32ub,
    world_name_id=AssetId,
    world_save_info_id=AssetId,
    default_skybox_id=AssetId,
    memory_relays=PrefixedArray(Int32ub, MLVLMemoryRelay),
    areas_count=Int32ub,
    unknown=Int32ub, # always 1
    areas=Array(lambda this: this.areas_count, MLVLArea),
    world_map_id=AssetId,
)

STRGString = PascalString(Int32ub, "utf-8")

Prime1STRG = Struct(
    magic=Int32ub,
    version=Int32ub,
    language_count=Int32ub,
    string_count=Int32ub,
    language_table=Array(lambda this: this.language_count, Struct(
        language_id=PaddedString(4, "utf-8"),
        string_offsets=Int32ub,
    )),
    string_table=Array(lambda this: this.language_count, Struct(
        string_table_size=Int32ub,
        string_offsets=Array(lambda this: this._root.string_count, Int32ub),
        string_array=Array(lambda this: this._root.string_count, CString("utf_16_be")),
    )),
)


@functools.lru_cache()
def strg_to_dict(path):
    with path.open('rb') as f:
        data = Prime1STRG.parse_stream(f)
        languages = {}
        lang_id = 0
        for lang in data["language_table"]:
            all_strings = []
            for index in range(0, data["string_count"]):
                all_strings.append(data["string_table"][lang_id].string_array[index])
        languages[lang.language_id] = all_strings
    return languages


def read_mlvl(path):
    return Prime1MLVL.parse_file(path)


def _convert_to_raw_python(value):
    if isinstance(value, construct.ListContainer):
        return [
            _convert_to_raw_python(item)
            for item in value
        ]

    if isinstance(value, construct.Container):
        return {
            key: _convert_to_raw_python(item)
            for key, item in value.items()
            if not key.startswith("_")
        }

    if isinstance(value, construct.EnumIntegerString):
        return str(value)

    return value


def _calc_doc_position(coordinates: List[List[float]]) -> Dict[str, float]:
    x, y, z = 0, 0, 0
    for item in coordinates:
        x += item[0]
        y += item[1]
        z += item[2]

    c = len(coordinates)
    return {"x": x / c, "y": y / c, "z": z / c}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    args = parser.parse_args()

    all_strg = {}
    for i, strg_path in enumerate(args.base.rglob("*.STRG.rsmeta")):
        all_strg[get_strg_id(strg_path)] = strg_path.with_suffix("")

    def get_name(strg_id):
        if strg_id == 0xffffffff:
            return "Unknown"
        return strg_to_dict(all_strg[strg_id])["ENGL"][0]
        
    worlds = []

    for world_meta in find_worlds(args.base):
        world_asset_id = get_mlvl_id(world_meta)

        world_mlvl = world_meta.with_suffix("")
        world_data = read_mlvl(world_mlvl)
            
        world = {
            "name": get_name(world_data["world_name_id"]),
            "dark_name": "",
            "asset_id": world_asset_id,
            "areas": [
                {
                    "name": get_name(area_data["area_name_id"]),
                    "in_dark_aether": False,
                    "asset_id": area_data["area_mrea_id"],
                    "default_node_index": None,
                    "docks": [
                        _convert_to_raw_python(dock)
                        for dock in area_data["docks"]
                    ]
                }
                for area_data in world_data["areas"]
            ],
        }
        for area in world["areas"]:
            docks = area.pop("docks")
            if not docks:
                area["nodes"] = []
                continue

            area["nodes"] = []
            for meta_dock in docks:
                dock_position = _calc_doc_position(meta_dock["dock_coordinates"])
                for dock in meta_dock["connecting_dock"]:
                    other_area = world["areas"][dock["area_index"]]
                    other_name = other_area["name"]
                    if other_name is None:
                        other_name = other_area["_name"]
                    area["nodes"].append({
                        "name": 'Dock to %s' % other_name,
                        "heal": False,
                        "coordinates": dock_position,
                        "node_type": "dock",
                        "dock_index": len(area["nodes"]),
                        "connected_area_asset_id": other_area["asset_id"],
                        "connected_dock_index": dock["dock_index"],
                        "dock_type": 0,
                        "dock_weakness_index": 0,
                        "connections": {}
                    })

        worlds.append(world)

    json_file = "randovania/data/json_data/prime1.json"
    with open(json_file, "w") as output_file:
        json.dump(worlds, output_file, indent=4)

if __name__ == '__main__':
    main()
