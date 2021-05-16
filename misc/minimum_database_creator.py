import argparse
import functools
import json
import pprint
import struct
from pathlib import Path
from typing import Any

import construct
from construct import Struct, Int32ub, Int64ub, PrefixedArray, Array, Float32b, Int16ub, CString, PaddedString, \
    PascalString


def find_worlds(base: Path):
    return base.rglob("*.MLVL.rsmeta")


def get_strg_id(meta: Path):
    with meta.open("rb") as f:
        return struct.unpack_from(">Q", f.read(), 32)[0]


def get_mlvl_id(meta: Path):
    with meta.open("rb") as f:
        return struct.unpack_from(">Q", f.read(), 46)[0]


AssetId = Int64ub
Vector3 = Array(3, Float32b)

MLVLConnectingDock = Struct(
    area_index=Int32ub,
    dock_index=Int32ub,
)

MLVLDock = Struct(
    connecting_dock=PrefixedArray(Int32ub, MLVLConnectingDock),
    dock_coordinates=PrefixedArray(Int32ub, Vector3),
)

MLVLArea = Struct(
    area_name_id=AssetId,
    area_transform=Array(12, Float32b),
    area_bounding_box=Array(6, Float32b),
    area_mrea_id=AssetId,
    internal_area_id=AssetId,
    attached_area_index=PrefixedArray(Int32ub, Int16ub),
    docks=PrefixedArray(Int32ub, MLVLDock),
    internal_area_name=CString("utf-8"),
)

Prime3MLVL = Struct(
    magic=Int32ub,
    version=Int32ub,
    world_name_id=AssetId,
    temple_key_world_index=Int32ub,
    world_save_info_id=AssetId,
    default_skybox_id=AssetId,
    areas=PrefixedArray(Int32ub, MLVLArea),
    world_map_id=AssetId,
)

NameEntry = Struct(
    name_offset=Int32ub,
    string_index=Int32ub,
)

NameTable = Struct(
    name_count=Int32ub,
    name_table_size=Int32ub,
    string_name_entries=Array(lambda this: this.name_count, NameEntry),
    string_name_array=Array(lambda this: this.name_count, CString("utf-8")),
)

STRGString = PascalString(Int32ub, "utf-8")

Prime3STRG = Struct(
    magic=Int32ub,
    version=Int32ub,
    language_count=Int32ub,
    string_count=Int32ub,
    name_table=NameTable,
    language_id_array=Array(lambda this: this.language_count, PaddedString(4, "utf-8")),
    language_table=Array(lambda this: this.language_count, Struct(
        strings_size=Int32ub,
        string_offsets=Array(lambda this: this._root.string_count, Int32ub),
    )),
)


@functools.lru_cache()
def strg_to_dict(path: Path):
    with path.open('rb') as f:
        data = Prime3STRG.parse_stream(f)

        languages = {
            _convert_to_raw_python(language_id): _convert_to_raw_python(language_table["string_offsets"])
            for language_id, language_table in zip(data["language_id_array"], data["language_table"])
        }
        all_strings_indices = set()
        for strings in languages.values():
            all_strings_indices |= set(strings)

        initial_offset = f.tell()
        all_strings = {}
        for index in sorted(all_strings_indices):
            f.seek(initial_offset + index)
            all_strings[index] = STRGString.parse_stream(f)[:-1]

    return {
        language_id: [all_strings[offset] for offset in string_offsets]
        for language_id, string_offsets in languages.items()
    }


def read_mlvl(path: Path):
    return Prime3MLVL.parse_file(path)


def _convert_to_raw_python(value) -> Any:
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    args = parser.parse_args()

    all_strg = {}
    for i, strg_path in enumerate(args.base.rglob("*.STRG.rsmeta")):
        all_strg[get_strg_id(strg_path)] = strg_path.with_suffix("")

    def get_name(strg_id):
        if strg_id == 0xffffffffffffffff:
            return None
        return strg_to_dict(all_strg[strg_id])["ENGL"][0]

    worlds = []

    for world_meta in find_worlds(args.base):
        world_asset_id = get_mlvl_id(world_meta)

        world_mlvl = world_meta.with_suffix("")
        world_data = read_mlvl(world_mlvl)

        world: dict = {
            "name": get_name(world_data["world_name_id"]),
            "dark_name": world_meta.name,
            "asset_id": world_asset_id,
            "areas": [
                {
                    "name": get_name(area_data["area_name_id"]),
                    "asset_id": area_data["area_mrea_id"],
                    "_name": area_data["internal_area_name"],
                    "default_node_index": None,
                    "docks": [
                        _convert_to_raw_python(dock["connecting_dock"])
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
            for docks in docks:
                for dock in docks:
                    other_area = world["areas"][dock["area_index"]]
                    other_name = other_area["name"]
                    if other_name is None:
                        other_name = other_area["_name"]
                    area["nodes"].append({
                        "name": f'Dock to {other_name}',
                        "heal": False,
                        "node_type": "dock",
                        "dock_index": len(area["nodes"]),
                        "connected_area_asset_id": other_area["asset_id"],
                        "connected_dock_index": dock["dock_index"],
                        "dock_type": 0,
                        "dock_weakness_index": 0,
                        "connections": {}
                    })

        worlds.append(world)

    with open("result.json", "w") as output_file:
        json.dump(worlds, output_file, indent=4)

if __name__ == '__main__':
    main()
