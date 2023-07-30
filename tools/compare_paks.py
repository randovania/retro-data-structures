from __future__ import annotations

import argparse
import collections
import dataclasses
import pprint
from pathlib import Path
from typing import TYPE_CHECKING

from retro_data_structures.formats import Pak
from retro_data_structures.game_check import Game

if TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


@dataclasses.dataclass()
class PakMetrics:
    id_occurrences: dict[AssetId, int]

    @classmethod
    def get_metrics(cls, pak: Pak):
        id_occurrences = collections.defaultdict(int)
        for file in pak._raw.files:
            id_occurrences[file.asset_id] += 1

        return cls(
            id_occurrences=id_occurrences,
        )


def compare(pak_a_path: Path, pak_b_path: Path, game: Game):
    pak_a = Pak.parse(pak_a_path.read_bytes(), target_game=game)
    pak_b = Pak.parse(pak_b_path.read_bytes(), target_game=game)

    names = {}

    for name, asset in pak_a.named_assets.items():
        names[asset] = name
    for name, asset in pak_b.named_assets.items():
        names[asset] = name

    def format_id(i):
        s = f"0x{i:08X}"
        if i in names:
            s += f" ({names[i]})"
        return s

    a_metrics = PakMetrics.get_metrics(pak_a)
    b_metrics = PakMetrics.get_metrics(pak_b)

    a_ids_set = set(a_metrics.id_occurrences.keys())
    b_ids_set = set(b_metrics.id_occurrences.keys())
    both_ids = a_ids_set.intersection(b_ids_set)

    a_only = a_ids_set - b_ids_set
    b_only = b_ids_set - a_ids_set

    if a_only:
        print("===== ids only in a =====")
        pprint.pp(list(map(format_id, a_only)), width=200)

    if b_only:
        print("===== ids only in b =====")
        pprint.pp(list(map(format_id, b_only)), width=200)

    different_occurrences = set()
    different_body = set()

    for asset in both_ids:
        if a_metrics.id_occurrences[asset] != b_metrics.id_occurrences[asset]:
            different_occurrences.add(asset)
        else:
            a_asset = pak_a.get_asset(asset, can_be_compressed=True)
            b_asset = pak_b.get_asset(asset, can_be_compressed=True)
            if a_asset != b_asset:
                if a_asset.compressed != b_asset.compressed:
                    if pak_a.get_asset(asset) == pak_b.get_asset(asset):
                        continue
                different_body.add(asset)

    if different_occurrences:
        print("===== different occurrences =====")
        pprint.pp(list(map(format_id, different_occurrences)), width=120)

    if different_body:
        print("===== different bodies =====")
        pprint.pp(list(map(format_id, different_body)), width=120)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", required=True, choices=[g.name for g in Game])
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("pak_a", type=Path)
    parser.add_argument("pak_b", type=Path)
    args = parser.parse_args()
    game = getattr(Game, args.game)

    root_a: Path = args.pak_a
    root_b: Path = args.pak_b

    if args.recursive:
        exists_in_a = {pak.relative_to(root_a).as_posix() for pak in root_a.rglob("*.pak")}
        exists_in_b = {pak.relative_to(root_b).as_posix() for pak in root_b.rglob("*.pak")}

        if exists_in_a - exists_in_b:
            print(f"Paks only in A: {exists_in_a - exists_in_b}")

        if exists_in_b - exists_in_a:
            print(f"Paks only in B: {exists_in_b - exists_in_a}")

        for pak in sorted(exists_in_a & exists_in_b):
            assert isinstance(pak, str)
            if pak.startswith("Metroid"):
                continue
            print(f">> Checking {pak}")
            compare(root_a.joinpath(pak), root_b.joinpath(pak), game)
    else:
        compare(root_a, root_b, game)
    print("I'm DONE")


if __name__ == "__main__":
    main()
