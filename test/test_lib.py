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
            return self.default(obj.getvalue())
        return json.JSONEncoder.default(self, obj)

def parse_and_build_compare(module, game: Game, file_path: Path, print_data=False):
    raw = file_path.read_bytes()

    data = module.parse(raw, target_game=game)
    data_as_dict = convert_to_raw_python(data)
    if print_data:
        print(json.dumps(data_as_dict, indent=4, cls=ByteEncoder))
    encoded = module.build(data_as_dict, target_game=game)

    assert encoded == raw
