# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "retro-data-structures",
#   "tqdm",
# ]
#
# [tool.uv.sources]
# retro-data-structures = { path = ".." }
# ///
from __future__ import annotations

import argparse
import difflib
import hashlib
import io
import pprint
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import tqdm

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.game_check import Game


def _hash_mrea_sections(raw_data: bytes, game_value: int) -> list[tuple[str, int, str]]:
    """Parse an MREA and return (section_name, section_index, md5) for each section."""

    from retro_data_structures.formats.mrea import Mrea
    from retro_data_structures.game_check import Game

    game = Game(game_value)
    mrea = Mrea.parse(raw_data, target_game=game)

    results = []
    for section_name, sections in mrea._raw.raw_sections.items():
        if section_name == "geometry_section":
            h = hashlib.md5(b"".join(sections)).hexdigest()
            results.append((section_name, 0, h))
        else:
            for i, section_bytes in enumerate(sections):
                h = hashlib.md5(section_bytes).hexdigest()
                results.append((section_name, i, h))

    return results


def _hash_strg_languages(raw_data: bytes, game_value: int, engl_only: bool = False) -> list[tuple[str, str]]:
    """Parse a STRG and return (language_code, md5) for each language."""

    from retro_data_structures.formats.strg import Strg
    from retro_data_structures.game_check import Game

    game = Game(game_value)
    strg = Strg.parse(raw_data, target_game=game)

    results = []
    for lang_code, strings in strg._raw.languages.items():
        if engl_only and lang_code != "ENGL":
            continue
        h = hashlib.md5(b"".join(s.encode("utf-8") for s in strings)).hexdigest()
        results.append((lang_code, h))

    return results


def _decode_scan(raw_data: bytes, game_value: int) -> str:
    """Parse a SCAN and return a human-readable string representation."""
    from retro_data_structures.formats.scan import Scan
    from retro_data_structures.game_check import Game

    game = Game(game_value)
    scan = Scan.parse(raw_data, target_game=game)
    return pprint.pformat(scan.scannable_object_info.get_properties().to_json())


def _hash_bytes(data: bytes) -> str:
    """Hash raw asset bytes."""
    return hashlib.md5(data).hexdigest()


def _decode_file(raw_data: bytes, asset_type: str, game_value: int):
    """Decode the file based on its type and return a human-readable representation."""

    from retro_data_structures import formats

    parsed = formats.resource_type_for(asset_type).parse(raw_data, target_game=Game(game_value))

    return pprint.pformat(convert_to_raw_python(parsed.raw), width=200)


def _submit_asset(executor, raw_data: bytes, game_value: int, asset_type: str, detailed: bool, args):
    if detailed:
        return executor.submit(_decode_file, raw_data, asset_type, game_value)

    if asset_type == "MREA":
        return executor.submit(_hash_mrea_sections, raw_data, game_value)
    elif asset_type == "STRG":
        return executor.submit(_hash_strg_languages, raw_data, game_value, args.engl_only)
    else:
        return executor.submit(_hash_bytes, raw_data)


def _write_result(
    f,
    asset_id: int,
    custom_name: str | None,
    pak_name: str,
    asset_type: str,
    result,
    detailed: bool,
    iso_label: str | None = None,
):
    name_display = f"0x{asset_id:08X} ({custom_name})" if custom_name is not None else f"0x{asset_id:08X}"
    iso_prefix = f"[{iso_label}] " if iso_label is not None else ""
    prefix = f"{name_display} {iso_prefix}[{pak_name}]"

    if detailed:
        f.write(f"{prefix} {asset_type}\n{result}\n")
    elif asset_type == "MREA":
        for section_name, section_index, h in result:
            f.write(f"{prefix} MREA {section_name}[{section_index}] {h}\n")
    elif asset_type == "STRG":
        for lang_code, h in result:
            f.write(f"{prefix} STRG {lang_code} {h}\n")
    elif asset_type == "SCAN" and detailed:
        f.write(f"{prefix} SCAN\n{result}\n")
    else:
        f.write(f"{prefix} {asset_type} {result}\n")


def _process_iso(manager: AssetManager, game: Game, args, desc: str = "Submitting") -> dict:
    """Returns {(asset_id, pak_name): (asset_type, result)} for all assets in the manager."""
    futures: dict = {}

    with ThreadPoolExecutor() as executor:
        for asset_id in tqdm.tqdm(list(manager.all_asset_ids()), desc=desc, unit="asset"):
            asset_type = manager.get_asset_type(asset_id)

            for pak_name in sorted(manager.find_paks(asset_id)):
                raw_data = manager.get_pak(pak_name).get_asset(asset_id).data
                futures[asset_id, pak_name] = (
                    asset_type,
                    _submit_asset(executor, raw_data, game.value, asset_type, args.detailed, args),
                )

    return {key: (asset_type, future.result()) for key, (asset_type, future) in futures.items()}


def _hash_raw_iso(manager: AssetManager, desc: str) -> dict:
    """Returns {(asset_id, pak_name): (asset_type, raw_md5)} for all assets, without decoding."""
    futures: dict = {}

    with ThreadPoolExecutor() as executor:
        for asset_id in tqdm.tqdm(list(manager.all_asset_ids()), desc=desc, unit="asset"):
            asset_type = manager.get_asset_type(asset_id)

            for pak_name in sorted(manager.find_paks(asset_id)):
                raw_data = manager.get_pak(pak_name).get_asset(asset_id).data
                futures[asset_id, pak_name] = (asset_type, executor.submit(_hash_bytes, raw_data))

    return {key: (asset_type, future.result()) for key, (asset_type, future) in futures.items()}


def _decode_iso_entries(manager: AssetManager, game: Game, args, keys: set, desc: str, detailed: bool) -> dict:
    """Returns {(asset_id, pak_name): (asset_type, result)} for the given subset of keys."""
    futures: dict = {}

    with ThreadPoolExecutor() as executor:
        for asset_id, pak_name in tqdm.tqdm(keys, desc=desc, unit="asset"):
            asset_type = manager.get_asset_type(asset_id)
            raw_data = manager.get_pak(pak_name).get_asset(asset_id).data
            futures[asset_id, pak_name] = (
                asset_type,
                _submit_asset(executor, raw_data, game.value, asset_type, detailed, args),
            )

    return {key: (asset_type, future.result()) for key, (asset_type, future) in futures.items()}


def _compare_isos(manager: AssetManager, manager2: AssetManager, game: Game, args) -> list:
    """Returns entries list for two-ISO comparison mode."""
    raw1 = _hash_raw_iso(manager, "Hashing ISO1")
    raw2 = _hash_raw_iso(manager2, "Hashing ISO2")

    only_in_1 = {k for k in raw1 if k not in raw2}
    only_in_2 = {k for k in raw2 if k not in raw1}
    different = {k for k in raw1 if k in raw2 and raw1[k][1] != raw2[k][1]}

    if args.engl_only:
        strg_keys = {k for k in different if raw1[k][0] == "STRG"}
        if strg_keys:
            engl1 = _decode_iso_entries(manager, game, args, strg_keys, "Filtering STRG ENGL ISO1", False)
            engl2 = _decode_iso_entries(manager2, game, args, strg_keys, "Filtering STRG ENGL ISO2", False)
            different -= {k for k in strg_keys if engl1[k][1] == engl2[k][1]}

    decoded1 = _decode_iso_entries(manager, game, args, different, "Decoding ISO1", args.detailed)
    decoded2 = _decode_iso_entries(manager2, game, args, different, "Decoding ISO2", args.detailed)

    entries = []
    for key in raw1:
        asset_id, pak_name = key
        if key in only_in_1:
            entries.append((asset_id, pak_name, raw1[key][0], raw1[key][1], "iso1-only"))
        elif key in different:
            entries.append((asset_id, pak_name, decoded1[key][0], (decoded1[key][1], decoded2[key][1]), "diff"))
    for key in raw2:
        asset_id, pak_name = key
        if key in only_in_2:
            entries.append((asset_id, pak_name, raw2[key][0], raw2[key][1], "iso2-only"))
    return entries


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", required=True, choices=[g.name for g in Game])
    parser.add_argument("iso", type=Path)
    parser.add_argument(
        "iso2", type=Path, nargs="?", help="Optional second ISO; when given only differences are written"
    )
    parser.add_argument("output", type=Path)
    parser.add_argument("--engl-only", action="store_true", help="Only hash the ENGL language for STRG assets")
    parser.add_argument(
        "--detailed", action="store_true", help="Include raw string contents for STRG instead of hashing"
    )
    args = parser.parse_args()

    game: Game = getattr(Game, args.game)
    manager = AssetManager(IsoFileProvider(args.iso), target_game=game)

    if args.iso2 is not None:
        manager2 = AssetManager(IsoFileProvider(args.iso2), target_game=game)
        entries = _compare_isos(manager, manager2, game, args)
    else:
        results = _process_iso(manager, game, args, desc="Submitting", detailed=args.detailed)
        entries = [
            (asset_id, pak_name, asset_type, result, None)
            for (asset_id, pak_name), (asset_type, result) in results.items()
        ]

    with args.output.open("w") as f, tqdm.tqdm(total=len(entries), desc="Writing", unit="asset") as progress:
        for asset_id, pak_name, asset_type, result, iso_label in entries:
            custom_name = manager.get_custom_name_for(asset_id)
            if iso_label == "diff":
                result1, result2 = result
                buf1, buf2 = io.StringIO(), io.StringIO()
                _write_result(buf1, asset_id, custom_name, pak_name, asset_type, result1, args.detailed, "iso1")
                _write_result(buf2, asset_id, custom_name, pak_name, asset_type, result2, args.detailed, "iso2")
                lines1 = buf1.getvalue().splitlines(keepends=True)
                lines2 = buf2.getvalue().splitlines(keepends=True)
                f.writelines(difflib.unified_diff(lines1, lines2))
            else:
                _write_result(f, asset_id, custom_name, pak_name, asset_type, result, args.detailed, iso_label)
            progress.update(1)

    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
