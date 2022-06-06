import argparse
import json
from pathlib import Path

from retro_data_structures.asset_manager import AssetManager, IsoFileProvider
from retro_data_structures.game_check import Game


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("game", choices=[g.name for g in Game])
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    game: Game = getattr(Game, args.game)

    manager = AssetManager(IsoFileProvider(args.path), target_game=game)

    result = [
        {"id": asset_id, "type": manager.get_asset_type(asset_id)}
        for asset_id in manager.all_asset_ids()
    ]
    Path(__file__).parents[1].joinpath("test", "test_files", f"assets_{game.name.lower()}.json").write_text(
        json.dumps(result, indent=4)
    )


if __name__ == '__main__':
    main()
