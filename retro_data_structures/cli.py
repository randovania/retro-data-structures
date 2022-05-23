import argparse
import asyncio
import itertools
import json
import logging
import typing
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Optional, List

from retro_data_structures import dependencies, formats
from retro_data_structures.base_resource import AssetId
from retro_data_structures.construct_extensions.json import convert_to_raw_python
from retro_data_structures.conversion import conversions
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.asset_manager import AssetManager, PathFileProvider, IsoFileProvider
from retro_data_structures.formats import mlvl
from retro_data_structures.game_check import Game

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


def game_argument_type(s: str) -> Game:
    try:
        return Game(int(s))
    except ValueError:
        # not a number, look by name
        for g in Game:
            g = typing.cast(Game, g)
            if g.name.lower() == s.lower():
                return g
        raise ValueError(f"No enum named {s} found")


def add_game_argument(parser: argparse.ArgumentParser, name="--game"):
    choices = []
    for g in Game:
        g = typing.cast(Game, g)
        choices.append(g.value)
        choices.append(g.name)

    parser.add_argument(name, help="The game of the file", type=game_argument_type, choices=list(Game), required=True)


def add_provider_argument(parser: argparse.ArgumentParser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--input-path", type=Path, help="Path to where to find pak files")
    group.add_argument("--input-iso", type=Path, help="Path to where to find ISO")


def get_provider_from_argument(args):
    if args.input_path is not None:
        return PathFileProvider(args.input_path)
    else:
        return IsoFileProvider(args.input_iso)


def create_parser():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command", required=True)

    ksy_export = subparser.add_parser("ksy-export")
    ksy_export.add_argument("output_path", type=Path)

    decode = subparser.add_parser("decode")
    add_game_argument(decode)
    decode.add_argument("--format", help="Hint the format of the file. Defaults to extension.")
    decode.add_argument("--re-encode", help="Re-encode afterwards and compares to the original.", action="store_true")
    decode.add_argument("input_path", type=Path, help="Path to the file")

    compare = subparser.add_parser("compare-files")
    add_game_argument(compare)
    compare.add_argument("--format", help="Hint the format of the file", required=True)
    compare.add_argument("--limit", help="Limit the number of files to test", type=int)
    compare.add_argument("input_path", type=Path, help="Path to the directory to glob")

    decode_from_paks = subparser.add_parser("decode-from-pak")
    add_game_argument(decode_from_paks)
    add_provider_argument(decode_from_paks)
    decode_from_paks.add_argument("asset_id", type=lambda x: int(x, 0), help="Asset id to print")

    deps = subparser.add_parser("list-dependencies")
    add_game_argument(deps)
    add_provider_argument(deps)
    g = deps.add_mutually_exclusive_group()
    g.add_argument("--asset-ids", type=lambda x: int(x, 0), nargs="+", help="Asset id to list dependencies for")
    g.add_argument("--asset-type", type=str, help="List dependencies for all assets of the given type.")

    convert = subparser.add_parser("convert")
    add_game_argument(convert, "--source-game")
    add_game_argument(convert, "--target-game")
    add_provider_argument(convert)
    convert.add_argument("asset_ids", type=lambda x: int(x, 0), nargs="+", help="Asset id to list dependencies for")

    return parser


def do_ksy_export(args):
    output_path: Path = args.output_path
    output_path.mkdir(parents=True, exist_ok=True)

    for game, game_formats in types_per_game.items():
        for format_name, cls in game_formats.items():
            print(f"Exporting {game} / {format_name}")
            cls.export_ksy(f"{game}_{format_name}", output_path.joinpath(f"{game}_{format_name}.ksy"))


def dump_to(path: Path, decoded):
    def default(o):
        if callable(o):
            o = o()
        if isinstance(o, bytes):
            return len(o)

        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

    with path.open("w") as f:
        x = convert_to_raw_python(decoded)
        f.write(json.JSONEncoder(indent=4, default=default).encode(x))


def do_decode(args):
    input_path: Path = args.input_path
    file_format = args.format
    game: Game = args.game
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
    game: Game = args.game
    asset_id: int = args.asset_id

    asset_provider = AssetManager(get_provider_from_argument(args), game)
    print(asset_provider.get_parsed_asset(asset_id).raw)


def list_dependencies(args):
    game: Game = args.game
    asset_ids: List[int]

    asset_provider = AssetManager(get_provider_from_argument(args), game)
    if args.asset_ids is not None:
        asset_ids = args.asset_ids
    else:
        asset_ids = [
            asset_id
            for asset_id in asset_provider.all_asset_ids()
            if asset_provider.get_asset_type(asset_id) == args.asset_type.upper()
        ]

    for asset_type, asset_id in dependencies.recursive_dependencies_for(asset_provider, asset_ids):
        print("{}: {}".format(asset_type, hex(asset_id)))


def do_convert(args):
    source_game: Game = args.source_game
    target_game: Game = args.target_game
    asset_ids: List[int] = args.asset_ids

    next_generated_id = 0xFFFF0000
    asset_manager = AssetManager(get_provider_from_argument(args), source_game)

    def id_generator(asset_type):
        # Proper implementation would need an AssetManager for the target game.
        nonlocal next_generated_id
        result = next_generated_id
        next_generated_id = result + 1
        return result

    converter = AssetConverter(
        target_game=target_game,
        asset_providers={source_game: asset_manager},
        id_generator=id_generator,
        converters=conversions.converter_for,
    )

    for asset_id in asset_ids:
        converted = converter.convert_asset_by_id(asset_id, source_game)

        print(
            "\n========================="
            "\n* Original Id: {:08x}"
            "\n* Target Id: {:08x}"
            "\n* Asset Type: {}"
            "\n\n{}".format(
                asset_id,
                converted.id,
                converted.type,
                converted.resource,
            )
        )

        for dependency in dependencies.direct_dependencies_for(converted.resource, converted.type, target_game):
            print(f"* Dependency: {dependency[1]:08x} ({dependency[0]})")

    print("==================\n>> All converted assets")
    reverse_converted_ids: typing.Dict[AssetId, typing.Tuple[Game, AssetId]] = {
        v: k for k, v in converter.converted_ids.items()
    }

    for converted_asset in converter.converted_assets.values():
        print(
            " {}: {:08x} from {:08x} ({})".format(
                converted_asset.type,
                converted_asset.id,
                reverse_converted_ids[converted_asset.id][1],
                reverse_converted_ids[converted_asset.id][0].name,
            )
        )


def decode_encode_compare_file(file_path: Path, game: Game, file_format: str):
    construct_class = formats.format_for(file_format)

    try:
        raw = file_path.read_bytes()
        decoded_from_raw = construct_class.parse(raw, target_game=game)

        sections = []
        for group in decoded_from_raw.section_groups:
            sections.extend(group.sections)

        encoded = construct_class.build(decoded_from_raw, target_game=game)

        if raw != encoded and raw.rstrip(b"\xFF") != encoded:
            return f"{file_path}: Results differ (len(raw): {len(raw)}; len(encoded): {len(encoded)})"
        return None

    except Exception as e:
        return f"{file_path}: Received error - {e}"


async def compare_all_files_in_path(args):
    input_path: Path = args.input_path
    file_format: str = args.format
    game: Game = args.game
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

    with ProcessPoolExecutor(max_workers=1) as executor:
        files = apply_limit(input_path.rglob(f"*.{file_format.upper()}"))
        if tqdm is not None:
            files = tqdm.tqdm(files, unit=" file")

        results = [loop.run_in_executor(executor, decode_encode_compare_file, f, game, file_format) for f in files]
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
            raise SystemExit

    if errors:
        print(f"{len(errors)} errors:")
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
    elif args.command == "convert":
        do_convert(args)
    elif args.command == "compare-files":
        asyncio.run(compare_all_files_in_path(args))
    else:
        raise ValueError(f"Unknown command: {args.command}")
