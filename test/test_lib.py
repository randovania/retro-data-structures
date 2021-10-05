from io import BytesIO
from pathlib import Path

import json

from retro_data_structures.construct_extensions import convert_to_raw_python
from retro_data_structures.game_check import Game

class ByteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.hex(' ').upper()
        if isinstance(obj, BytesIO):
            return None

        return json.JSONEncoder.default(self, obj)

def _parse_and_build_compare(module, game: Game, file_path: Path, print_data=False, save_file=False):
    raw = file_path.read_bytes()

    data = module.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    if print_data:
        print(json.dumps(data_as_dict, indent=4, cls=ByteEncoder))
    encoded = module.build(data_as_dict, target_game=game)

    if save_file:
        file_path.parent.joinpath("TESTED.DUMB").write_bytes(encoded)
    
    return (raw, encoded, data_as_dict)

def parse_and_build_compare(module, game: Game, file_path: Path, print_data=False, save_file=False):
    raw, encoded, _ = _parse_and_build_compare(module, game, file_path, print_data, save_file)
    assert encoded == raw

def parse_and_build_compare_parsed(module, game: Game, file_path: Path, print_data=False, save_file=False):
    raw, encoded, data_as_dict = _parse_and_build_compare(module, game, file_path, print_data, save_file)
   
    data2 = module.parse(encoded, target_game=game)
    data2_as_dict = convert_to_raw_python(data2)
    if print_data:
        print(json.dumps(data2_as_dict, indent=4, cls=ByteEncoder))

    assert data_as_dict == data2_as_dict