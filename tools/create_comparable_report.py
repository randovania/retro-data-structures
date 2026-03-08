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
import hashlib
import pprint
from concurrent.futures import InterpreterPoolExecutor, ThreadPoolExecutor
from pathlib import Path

import tqdm

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
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
    """Hash raw asset bytes. Runs in a subinterpreter."""

    return hashlib.md5(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", required=True, choices=[g.name for g in Game])
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--engl-only", action="store_true", help="Only hash the ENGL language for STRG assets")
    parser.add_argument(
        "--detailed", action="store_true", help="Include raw string contents for STRG instead of hashing"
    )
    args = parser.parse_args()

    game: Game = getattr(Game, args.game)
    manager = AssetManager(IsoFileProvider(args.iso), target_game=game)

    output_path = args.output

    mrea_futures: dict = {}
    strg_futures: dict = {}
    scan_futures: dict = {}
    other_futures: dict = {}

    all_asset_ids = list(manager.all_asset_ids())

    with ThreadPoolExecutor() as thread_executor, InterpreterPoolExecutor() as interp_executor:
        for asset_id in tqdm.tqdm(all_asset_ids, desc="Submitting", unit="asset"):
            asset_type = manager.get_asset_type(asset_id)
            raw_data = manager.get_raw_asset(asset_id).data

            if asset_type == "MREA":
                mrea_futures[asset_id] = thread_executor.submit(_hash_mrea_sections, raw_data, game.value)
            elif asset_type == "STRG":
                strg_futures[asset_id] = thread_executor.submit(
                    _hash_strg_languages, raw_data, game.value, args.engl_only
                )
            elif asset_type == "SCAN" and args.detailed:
                scan_futures[asset_id] = thread_executor.submit(_decode_scan, raw_data, game.value)
            else:
                other_futures[asset_id] = (
                    asset_type,
                    interp_executor.submit(_hash_bytes, raw_data),
                )

    total = len(mrea_futures) + len(strg_futures) + len(scan_futures) + len(other_futures)
    with output_path.open("w") as f, tqdm.tqdm(total=total, desc="Writing", unit="asset") as progress:
        for asset_id in sorted(mrea_futures):
            results = mrea_futures[asset_id].result()
            for section_name, section_index, h in results:
                f.write(f"0x{asset_id:08X} MREA {section_name}[{section_index}] {h}\n")
            progress.update(1)

        for asset_id in sorted(strg_futures):
            results = strg_futures[asset_id].result()
            for lang_code, h in results:
                f.write(f"0x{asset_id:08X} STRG {lang_code} {h}\n")
            progress.update(1)

        for asset_id in sorted(scan_futures):
            text = scan_futures[asset_id].result()
            f.write(f"0x{asset_id:08X} SCAN\n{text}\n")
            progress.update(1)

        for asset_id in sorted(other_futures):
            asset_type, future = other_futures[asset_id]
            h = future.result()
            f.write(f"0x{asset_id:08X} {asset_type} {h}\n")
            progress.update(1)

    print(f"Report written to {output_path}")


if __name__ == "__main__":
    main()
