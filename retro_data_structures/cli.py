import argparse
import asyncio
import itertools
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Optional

from retro_data_structures import mlvl, construct_extensions
from retro_data_structures.ancs import ANCS
from retro_data_structures.anim import ANIM
from retro_data_structures.cmdl import CMDL
from retro_data_structures.mlvl import MLVL
from retro_data_structures.mrea import MREA
from retro_data_structures.pak import PAK

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
ALL_FORMATS = {
    "ancs": ANCS,
    "cmdl": CMDL,
    "mlvl": MLVL,
    "mrea": MREA,
    "pak": PAK,
    "anim": ANIM,
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

    construct_class = ALL_FORMATS[file_format.lower()]

    raw = input_path.read_bytes()
    decoded_from_raw = construct_class.parse(raw, target_game=game)
    print(decoded_from_raw)

    if re_encode:
        encoded = construct_class.build(decoded_from_raw, target_game=game)
        if raw != encoded:
            print(f"{input_path}: Results differ (len(raw): {len(raw)}; len(encoded): {len(encoded)})")


def decode_encode_compare_file(file_path: Path, game: int, file_format: str):
    construct_class = ALL_FORMATS[file_format.lower()]

    try:
        raw = file_path.read_bytes()
        decoded_from_raw = construct_class.parse(raw, target_game=game)
        encoded = construct_class.build(decoded_from_raw, target_game=game)

        if raw != encoded:
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
        results = [
            loop.run_in_executor(executor, decode_encode_compare_file, f, game, file_format)
            for f in apply_limit(input_path.rglob(f"*.{file_format.upper()}"))
        ]
        as_completed = asyncio.as_completed(results)
        if tqdm is not None:
            as_completed = tqdm.tqdm(as_completed, total=len(results))

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
    args = create_parser().parse_args()

    if args.command == "ksy-export":
        do_ksy_export(args)
    elif args.command == "decode":
        do_decode(args)
    elif args.command == "compare-files":
        asyncio.run(compare_all_files_in_path(args))
    else:
        raise ValueError(f"Unknown command: {args.command}")
