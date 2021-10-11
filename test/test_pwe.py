from parse_pwe_templates import parse
from retro_data_structures.property_template import GameTemplate
from pathlib import Path

def test_compare_pwe_templates():
    game_list = parse(["Prime", "Echoes", "Corruption"])
    
    for game, template in game_list.items():
        encoded = GameTemplate.build(template)
        assert encoded == GameTemplate.build(GameTemplate.parse(encoded))

        Path(__file__).parent.parent.joinpath(f"retro_data_structures/properties/{game}.prop").write_bytes(encoded)
