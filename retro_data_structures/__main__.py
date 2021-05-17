import argparse
from pathlib import Path

from retro_data_structures import mlvl

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
    parser.add_argument("output_path", type=Path)
    return parser


def main():
    args = create_parser().parse_args()
    output_path: Path = args.output_path
    output_path.mkdir(parents=True, exist_ok=True)

    for game, formats in types_per_game.items():
        for format_name, cls in formats.items():
            print(f"Exporting {game} / {format_name}")
            cls.export_ksy(f"{game}_{format_name}", output_path.joinpath(f"{game}_{format_name}.ksy"))


if __name__ == '__main__':
    main()
