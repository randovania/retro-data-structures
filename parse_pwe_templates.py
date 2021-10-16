import dataclasses
import pprint
import re
import typing
from pathlib import Path
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


@dataclasses.dataclass(frozen=True)
class EnumDefinition:
    name: str
    values: typing.Dict[str, typing.Any]


def create_enums(game: str, enums: typing.List[EnumDefinition], mode: str = "w"):
    code = '"""\nGenerated file.\n"""\nfrom enum import Enum\n' if mode == "w" else ""

    def _scrub(string: str):
        s = re.sub(r'\W', '', string)  # remove non-word characters
        s = re.sub(r'^(?=\d)', '_', s)  # add leading underscore to strings starting with a number
        s = re.sub(r'^None$', '_None', s)  # add leading underscore to None
        s = s or "_EMPTY"  # add name for empty string keys
        return s

    for e in enums:
        code += f"\n\nclass {_scrub(e.name)}(Enum):\n"
        for name, value in e.values.items():
            code += f"    {_scrub(name)} = {value}\n"

    with Path(__file__).parent.joinpath(f"retro_data_structures/enums/{game}.py").open(mode) as f:
        f.write(code)


def _prop_default_value(element: Element, game_id: str, path: Path) -> dict:
    default_value_types = {
        "Int": lambda el: int(el.text, 10),
        "Float": lambda el: float(el.text),
        "Bool": lambda el: el.text == "true",
        "Short": lambda el: int(el.text, 10),
        "Color": lambda el: {e.tag: float(e.text) for e in el},
        "Vector": lambda el: {e.tag: float(e.text) for e in el},
        "Flags": lambda el: int(el.text, 10),
        "Choice": lambda el: int(el.text, 10),
        "Enum": lambda el: int(el.text, 16)
    }

    default_value = None
    if (default_value_element := element.find("DefaultValue")) is not None:
        default_value = default_value_types.get(element.attrib["Type"], lambda el: el.text)(default_value_element)
    return {"default_value": default_value}


def _prop_struct(element: Element, game_id: str, path: Path) -> dict:
    return {
        "archetype": element.attrib.get("Archetype"),
        "properties": _parse_properties(element, game_id, path)["properties"]
    }


def _prop_asset(element: Element, game_id: str, path: Path) -> dict:
    type_filter = []
    if element.find("TypeFilter"):
        type_filter = [t.text for t in element.find("TypeFilter")]
    return {"type_filter": type_filter}


def _prop_array(element: Element, game_id: str, path: Path) -> dict:
    # print(ElementTree.tostring(element, encoding='utf8', method='xml'))
    item_archetype = None
    if (item_archetype_element := element.find("ItemArchetype")) is not None:
        item_archetype = _parse_single_property(item_archetype_element, game_id, path, include_id=False)
    # print(item_archetype)
    return {"item_archetype": item_archetype}


def _prop_choice(element: Element, game_id: str, path: Path) -> dict:
    _parse_choice(element, game_id, path)
    extras = {"archetype": element.attrib.get("Archetype")}
    extras.update(_prop_default_value(element, game_id, path))
    return extras


def _parse_single_property(element: Element, game_id: str, path: Path, include_id: bool=True) -> dict:
    parsed = {}
    if include_id:
        parsed.update({"id": int(element.attrib["ID"], 16)})
    name = element.find("Name")
    parsed.update({
        "type": element.attrib["Type"],
        "name": name.text if name is not None and name.text is not None else ""
    })
    
    property_type_extras = {
        "Struct": _prop_struct,
        "Asset": _prop_asset,
        "Array": _prop_array,
        "Enum": _prop_choice,
        "Choice": _prop_choice
    }

    parsed.update(property_type_extras.get(element.attrib["Type"], _prop_default_value)(element, game_id, path))

    return parsed


def _parse_properties(properties: Element, game_id: str, path: Path) -> dict:
    elements = []
    if (sub_properties := properties.find("SubProperties")) is not None:
        for element in sub_properties:
            element = typing.cast(Element, element)

            elements.append(_parse_single_property(element, game_id, path))

    return {
        "type": "Struct",
        "name": properties.find("Name").text if properties.find("Name") is not None else "",
        "atomic": properties.find("Atomic") is not None,
        "properties": elements,
    }


def _parse_choice(properties: Element, game_id: str, path: Path) -> dict:
    _type = properties.attrib.get("Type", "Choice")
    choices = {}

    if (values := properties.find("Values")) is not None:
        for element in values:
            element = typing.cast(Element, element)
            choices[element.attrib["Name"]] = int(element.attrib["ID"], 16)

        name = ""
        if properties.find("Name") is not None:
            name = properties.find("Name").text
        elif properties.attrib.get("ID"):
            name = property_names.get(int(properties.attrib.get("ID"), 16), path.stem + properties.attrib.get("ID"))
        else:
            return {
                "type": _type,
                "choices": choices
            }

        create_enums(game_id, [EnumDefinition(name, choices)], "a")

    return {
        "type": _type
    }


_parse_choice.unknowns = {}


def parse_script_object_file(path: Path, game_id: str) -> dict:
    t = ElementTree.parse(path)
    root = t.getroot()
    return _parse_properties(root.find("Properties"), game_id, path)


def parse_property_archetypes(path: Path, game_id: str) -> dict:
    t = ElementTree.parse(path)
    root = t.getroot()
    archetype = root.find("PropertyArchetype")
    _type = archetype.attrib["Type"]
    if _type == "Struct":
        return _parse_properties(archetype, game_id, path)
    elif _type == "Choice" or _type == "Enum":
        return _parse_choice(archetype, game_id, path)
    else:
        raise ValueError(f"Unknown Archetype format: {_type}")


property_names: typing.Dict[int, str] = {}


def read_property_names(map_path: Path):
    global property_names

    t = ElementTree.parse(map_path)
    root = t.getroot()
    m = root.find("PropertyMap")

    property_names = {
        int(item.find("Key").attrib["ID"], 16): item.find("Value").attrib["Name"]
        for item in typing.cast(typing.Iterable[Element], m)
    }

    return property_names


def get_paths(elements: typing.Iterable[Element]) -> typing.Dict[str, str]:
    return {
        item.find("Key").text: item.find("Value").attrib["Path"]
        for item in elements
    }


def get_key_map(elements: typing.Iterable[Element]) -> typing.Dict[str, str]:
    return {
        item.find("Key").text: item.find("Value").text
        for item in elements
    }


def parse_game(templates_path: Path, game_xml: Path, game_id: str) -> dict:
    base_path = templates_path / game_xml.parent

    t = ElementTree.parse(templates_path / game_xml)
    root = t.getroot()

    states = get_key_map(root.find("States"))
    messages = get_key_map(root.find("Messages"))
    create_enums(game_id, [
        EnumDefinition(
            "States",
            {
                value: repr(key)
                for key, value in states.items()
            }
        ),
        EnumDefinition(
            "Messages",
            {
                value: repr(key)
                for key, value in messages.items()
            }
        ),
    ])

    script_objects = {
        four_cc: parse_script_object_file(base_path / path, game_id)
        for four_cc, path in get_paths(root.find("ScriptObjects")).items()
    }
    property_archetypes = {
        name: parse_property_archetypes(base_path / path, game_id)
        for name, path in get_paths(root.find("PropertyArchetypes")).items()
    }

    return {
        "script_objects": script_objects,
        "property_archetypes": property_archetypes
    }


def parse_game_list(templates_path: Path) -> dict:
    t = ElementTree.parse(templates_path / "GameList.xml")
    root = t.getroot()
    return {
        game.attrib["ID"]: Path(game.find("GameTemplate").text)
        for game in root
    }


def parse(game_ids: typing.Iterable[str] = []) -> dict:
    templates_path = Path("PrimeWorldEditor/templates")
    read_property_names(templates_path / "PropertyMap.xml")

    game_list = parse_game_list(templates_path)
    _parse_choice.unknowns = {game: 0 for game in game_list.keys()}

    return {
        _id: parse_game(templates_path, game_path, _id)
        for _id, game_path in game_list.items()
        if not game_ids or _id in game_ids
    }


if __name__ == '__main__':
    pprint.pprint(parse(), sort_dicts=False)
