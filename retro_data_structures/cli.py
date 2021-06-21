import argparse
import asyncio
import itertools
import json
import logging
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Optional, List

from retro_data_structures import construct_extensions, dependencies, formats
from retro_data_structures.asset_provider import AssetProvider
from retro_data_structures.formats import mlvl

types_per_game = {
    "metroid_prime_1": {
        "mlvl": mlvl.Prime1MLVL,
    },
    "metroid_prime_2": {
        "mlvl": mlvl.Prime2MLVL,
    },
    "metroid_prime_3": {
        "mlvl": mlvl.Prime3MLVL,
    },
}


def create_parser():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command", required=True)

    ksy_export = subparser.add_parser("ksy-export")
    ksy_export.add_argument("output_path", type=Path)

    decode = subparser.add_parser("decode")
    decode.add_argument("--game", help="Hint the game of the file", type=int)
    decode.add_argument("--format", help="Hint the format of the file. Defaults to extension.")
    decode.add_argument("--re-encode", help="Re-encode afterwards and compares to the original.", action="store_true")
    decode.add_argument("input_path", type=Path, help="Path to the file")

    compare = subparser.add_parser("compare-files")
    compare.add_argument("--game", help="Hint the game of the file", type=int)
    compare.add_argument("--format", help="Hint the format of the file")
    compare.add_argument("--limit", help="Limit the number of files to test", type=int)
    compare.add_argument("input_path", type=Path, help="Path to the directory to glob")

    decode_from_paks = subparser.add_parser("decode-from-pak")
    decode_from_paks.add_argument("--game", help="Hint the game of the file", type=int)
    decode_from_paks.add_argument("paks_path", type=Path, help="Path to where to find pak files")
    decode_from_paks.add_argument("asset_id", type=lambda x: int(x, 0), help="Asset id to print")

    deps = subparser.add_parser("list-dependencies")
    deps.add_argument("--game", help="Hint the game of the file", type=int)
    deps.add_argument("paks_path", type=Path, help="Path to where to find pak files")
    deps.add_argument("asset_ids", type=int, nargs='+', help="Asset id to list dependencies for")

    return parser


def do_ksy_export(args):
    output_path: Path = args.output_path
    output_path.mkdir(parents=True, exist_ok=True)

    for game, formats in types_per_game.items():
        for format_name, cls in formats.items():
            print(f"Exporting {game} / {format_name}")
            cls.export_ksy(f"{game}_{format_name}", output_path.joinpath(f"{game}_{format_name}.ksy"))


def dump_to(path: Path, decoded):
    def default(o):
        if callable(o):
            o = o()
        if isinstance(o, bytes):
            return len(o)

        raise TypeError(f'Object of type {o.__class__.__name__} '
                        f'is not JSON serializable')

    with path.open("w") as f:
        x = construct_extensions.convert_to_raw_python(decoded)
        f.write(json.JSONEncoder(indent=4, default=default).encode(x))


def do_decode(args):
    input_path: Path = args.input_path
    file_format = args.format
    game = args.game
    re_encode = args.re_encode

    if file_format is None:
        file_format = input_path.suffix[1:]

    construct_class = formats.format_for(file_format)

    raw = input_path.read_bytes()
    decoded_from_raw = construct_class.parse(raw, target_game=game)
    print(decoded_from_raw)

    if re_encode:
        encoded = construct_class.build(decoded_from_raw, target_game=game)
        if raw != encoded:
            print(f"{input_path}: Results differ (len(raw): {len(raw)}; len(encoded): {len(encoded)})")


def do_decode_from_pak(args):
    game = args.game
    paks_path: Path = args.paks_path
    asset_id: int = args.asset_id

    with AssetProvider(list(paks_path.glob("*.pak")), game) as asset_provider:
        print(asset_provider.get_asset(asset_id))


def list_dependencies(args):
    game = args.game
    paks_path: Path = args.paks_path
    asset_ids: List[int] = args.asset_ids

    with AssetProvider(list(paks_path.glob("*.pak")), game) as asset_provider:
        for asset_type, asset_id in dependencies.recursive_dependencies_for(asset_provider, asset_ids):
            print("{}: {}".format(asset_type, hex(asset_id)))


def decode_encode_compare_file(file_path: Path, game: int, file_format: str):
    construct_class = formats.format_for(file_format)

    try:
        raw = file_path.read_bytes()
        decoded_from_raw = construct_class.parse(raw, target_game=game)
        encoded = construct_class.build(decoded_from_raw, target_game=game)

        if raw != encoded and raw.rstrip(b"\xFF") != encoded:
            return f"{file_path}: Results differ (len(raw): {len(raw)}; len(encoded): {len(encoded)})"
        return None

    except Exception as e:
        return f"{file_path}: Received error - {e}"


async def compare_all_files_in_path(args):
    input_path: Path = args.input_path
    file_format: str = args.format
    game: int = args.game
    limit: Optional[int] = args.limit

    def apply_limit(it):
        if limit is None:
            return it
        else:
            return itertools.islice(it, limit)

    loop = asyncio.get_running_loop()

    try:
        import tqdm
    except ImportError:
        tqdm = None

    errors = []

    with ProcessPoolExecutor() as executor:
        files = apply_limit(input_path.rglob(f"*.{file_format.upper()}"))
        if tqdm is not None:
            files = tqdm.tqdm(files, unit=" file")

        results = [loop.run_in_executor(executor, decode_encode_compare_file, f, game, file_format)
                   for f in files]
        as_completed = asyncio.as_completed(results)
        if tqdm is not None:
            as_completed = tqdm.tqdm(as_completed, total=len(results), unit=" file")

        for c in as_completed:
            message = await c
            if message:
                if tqdm is not None:
                    errors.append(message)
                    as_completed.set_postfix_str(f"{len(errors)} errors")
                else:
                    print(message)

    if errors:
        print("Errors:")
        for m in errors:
            print(m)


def main():
    logging.basicConfig(level=logging.INFO)
    args = create_parser().parse_args()

    if args.command == "ksy-export":
        do_ksy_export(args)
    elif args.command == "decode":
        do_decode(args)
    elif args.command == "decode-from-pak":
        do_decode_from_pak(args)
    elif args.command == "list-dependencies":
        list_dependencies(args)
    elif args.command == "compare-files":
        asyncio.run(compare_all_files_in_path(args))
    else:
        raise ValueError(f"Unknown command: {args.command}")
