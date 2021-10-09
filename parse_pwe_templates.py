import dataclasses
import pprint
import typing
from pathlib import Path
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


@dataclasses.dataclass(frozen=True)
class EnumDefinition:
    name: str
    values: typing.Dict[str, typing.Any]


def create_enums(game: str, enums: typing.List[EnumDefinition]):
    code = '"""\nGenerated file.\n"""\nfrom enum import Enum\n'

    for e in enums:
        code += f"\n\nclass {e.name}(Enum):\n"
        for name, value in e.values.items():
            code += f"    {name} = {value}\n"

    Path(__file__).parent.joinpath(f"retro_data_structures/enums/{game}.py").write_text(code)


def _parse_properties(properties: Element) -> dict:
    elements = []
    for element in properties.find("SubProperties"):
        element = typing.cast(Element, element)

        # TODO: parsing default_value depends on the type
        # if (default_value_element := element.find("DefaultValue")) is not None:
        #     default_value = default_value_element.text
        # else:
        #     default_value = None

        elements.append({
            "id": int(element.attrib["ID"], 16),
            "type": element.attrib["Type"],
            "archetype": element.attrib.get("Archetype"),
            # "default_value": default_value,
        })
        pass

    return {
        "type": "struct",
        "properties": elements,
    }


def _parse_choice(properties: Element) -> dict:
    choices = {}

    for element in properties.find("Values"):
        element = typing.cast(Element, element)
        choices[element.attrib["Name"]] = int(element.attrib["ID"], 16)

    return {
        "type": "choice",
        "choices": choices,
    }


def parse_script_object_file(path: Path):
    t = ElementTree.parse(path)
    root = t.getroot()
    return _parse_properties(root.find("Properties"))


def parse_property_archetypes(path: Path):
    t = ElementTree.parse(path)
    root = t.getroot()
    archetype = root.find("PropertyArchetype")
    if archetype.attrib["Type"] == "Struct":
        return _parse_properties(archetype)
    elif archetype.attrib["Type"] == "Choice":
        return _parse_choice(archetype)
    else:
        raise ValueError(f"Unknown Archetype format: {archetype.attrib['Type']}")


def read_property_names(map_path: Path) -> typing.Dict[int, str]:
    t = ElementTree.parse(map_path)
    root = t.getroot()
    m = root.find("PropertyMap")

    return {
        int(item.find("Key").attrib["ID"], 16): item.find("Value").attrib["Name"]
        for item in typing.cast(typing.Iterable[Element], m)
    }


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


def parse_echoes(templates_path: Path):
    base_path = templates_path / "MP2"

    t = ElementTree.parse(base_path / "Game.xml")
    root = t.getroot()

    states = get_key_map(root.find("States"))
    messages = get_key_map(root.find("Messages"))

    script_objects = {
        four_cc: parse_script_object_file(base_path / path)
        for four_cc, path in get_paths(root.find("ScriptObjects")).items()
    }
    property_archetypes = {
        name: parse_property_archetypes(base_path / path)
        for name, path in get_paths(root.find("PropertyArchetypes")).items()
    }

    create_enums("echoes", [
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


def parse():
    templates_path = Path("PrimeWorldEditor/templates")
    property_names = read_property_names(templates_path / "PropertyMap.xml")

    parse_echoes(templates_path)


if __name__ == '__main__':
    parse()
