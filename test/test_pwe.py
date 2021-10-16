from pathlib import Path

from parse_pwe_templates import parse, read_property_names
from retro_data_structures.property_template import GameTemplate, PropertyNames


def test_compare_pwe_templates():
    base_path = Path(__file__).parent.parent

    property_names = read_property_names(base_path / "PrimeWorldEditor/templates/PropertyMap.xml")
    encoded = PropertyNames.build(property_names)
    assert encoded == PropertyNames.build(PropertyNames.parse(encoded))

    game_list = parse(["Prime", "Echoes", "Corruption"])
    for game, template in game_list.items():
        encoded = GameTemplate.build(template)
        assert encoded == GameTemplate.build(GameTemplate.parse(encoded))
