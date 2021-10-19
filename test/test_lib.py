from pathlib import Path

from construct.lib.containers import Container

from retro_data_structures.game_check import Game


def _parse_and_build_compare(module, game: Game, file_path: Path, print_data=False, save_file=None):
    raw = file_path.read_bytes()

    data = module.parse(raw, target_game=game)
    if print_data:
        print(data)
    encoded = module.build(data, target_game=game)

    if save_file:
        file_path.parent.joinpath(save_file).write_bytes(encoded)

    return (raw, encoded, data)


def parse_and_build_compare(module, game: Game, file_path: Path, print_data=False, save_file=None):
    raw, encoded, _ = _parse_and_build_compare(module, game, file_path, print_data, save_file)
    assert encoded == raw


def parse_and_build_compare_parsed(module, game: Game, file_path: Path, print_data=False, save_file=None):
    _, encoded, data = _parse_and_build_compare(module, game, file_path, print_data, save_file)

    data2 = module.parse(encoded, target_game=game)
    if print_data:
        print(data2)

    assert purge_hidden(data) == purge_hidden(data2)

def purge_hidden(data: Container) -> Container:
    data = {k: v for k, v in data.items() if not k.startswith("_")}
    return {k: purge_hidden(v) if isinstance(v, Container) else v for k, v in data.items()}