import argparse
from pathlib import Path

from retro_data_structures import mlvl
from retro_data_structures.ancs import ANCS
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


def create_parser():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command", required=True)

    ksy_export = subparser.add_parser("ksy-export")
    ksy_export.add_argument("output_path", type=Path)

    decode = subparser.add_parser("decode")
    decode.add_argument("--game", help="Hint the game of the file")
    decode.add_argument("--format", help="Hint the format of the file. Defaults to extension.")
    decode.add_argument("input_path", type=Path, help="Path to the file")

    return parser


def do_ksy_export(args):
    output_path: Path = args.output_path
    output_path.mkdir(parents=True, exist_ok=True)

    for game, formats in types_per_game.items():
        for format_name, cls in formats.items():
            print(f"Exporting {game} / {format_name}")
            cls.export_ksy(f"{game}_{format_name}", output_path.joinpath(f"{game}_{format_name}.ksy"))


def do_decode(args):
    input_path: Path = args.input_path
    file_format = args.format

    if file_format is None:
        file_format = input_path.suffix[1:]

    formats = {
        "ancs": ANCS,
        "cmdl": CMDL,
        "mlvl": MLVL,
        "mrea": MREA,
        "pak": PAK,
    }
    construct_class = formats[file_format.lower()]
    data = construct_class.parse_file(input_path, game_hack=1)

    # print(len(data.named_resources))
    # print(len(data.resources))
    #
    print(data)


def main():
    args = create_parser().parse_args()

    if args.command == "ksy-export":
        do_ksy_export(args)
    elif args.command == "decode":
        do_decode(args)


if __name__ == '__main__':
    main()
