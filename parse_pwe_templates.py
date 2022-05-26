import dataclasses
import logging
import re
import struct
import typing
from pathlib import Path
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import inflection

_game_id_to_file = {
    "Prime": "prime",
    "Echoes": "echoes",
    "Corruption": "corruption",
    "DKCReturns": "dkc_returns",
}

_CODE_PARSE_UINT16 = 'struct.unpack(">H", data.read(2))[0]'
_CODE_PARSE_UINT32 = 'struct.unpack(">L", data.read(4))[0]'


@dataclasses.dataclass(frozen=True)
class EnumDefinition:
    name: str
    values: typing.Dict[str, typing.Any]
    enum_base: str = "Enum"


_enums_by_game: typing.Dict[str, typing.List[EnumDefinition]] = {}


def _scrub_enum(string: str):
    s = re.sub(r'\W', '', string)  # remove non-word characters
    s = re.sub(r'^(?=\d)', '_', s)  # add leading underscore to strings starting with a number
    s = re.sub(r'^None$', '_None', s)  # add leading underscore to None
    s = s or "_EMPTY"  # add name for empty string keys
    return s


def create_enums_file(enums: typing.List[EnumDefinition]):
    code = '"""\nGenerated file.\n"""\nimport enum\nimport typing\nimport struct\n'

    for e in enums:
        code += f"\n\nclass {_scrub_enum(e.name)}(enum.{e.enum_base}):\n"
        for name, value in e.values.items():
            code += f"    {_scrub_enum(name)} = {value}\n"

        code += '\n    @classmethod\n'
        code += '    def from_stream(cls, data: typing.BinaryIO):\n'
        code += f'        return cls({_CODE_PARSE_UINT32})\n'

        code += '\n    def to_stream(self, data: typing.BinaryIO):\n'
        code += '        data.write(struct.pack(">L", self.value))\n'

    return code


def _prop_default_value(element: Element, game_id: str, path: Path) -> dict:
    default_value_types = {
        "Int": lambda el: int(el.text, 10) & 0xFFFFFFFF,
        "Float": lambda el: float(el.text),
        "Bool": lambda el: el.text == "true",
        "Short": lambda el: int(el.text, 10) & 0xFFFF,
        "Color": lambda el: {e.tag: float(e.text) for e in el},
        "Vector": lambda el: {e.tag: float(e.text) for e in el},
        "Flags": lambda el: int(el.text, 10) & 0xFFFFFFFF,
        "Choice": lambda el: int(el.text, 10) & 0xFFFFFFFF,
        "Enum": lambda el: int(el.text, 16) & 0xFFFFFFFF,
        "Sound": lambda el: int(el.text, 10) & 0xFFFFFFFF,
    }

    default_value = None
    has_default = False
    if (default_value_element := element.find("DefaultValue")) is not None:
        default_value = default_value_types.get(element.attrib["Type"], lambda el: el.text)(default_value_element)
        has_default = True
    return {"has_default": has_default, "default_value": default_value}


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


def _prop_flags(element: Element, game_id: str, path: Path) -> dict:
    extras = _prop_default_value(element, game_id, path)
    if (flags_element := element.find("Flags")) is not None:
        extras["flags"] = {
            element.attrib["Name"]: int(element.attrib["Mask"], 16)
            for element in flags_element.findall("Element")
        }

        name = None
        if element.find("Name") is not None:
            name = element.find("Name").text
        elif element.attrib.get("ID"):
            name = property_names.get(int(element.attrib.get("ID"), 16))

        _enums_by_game[game_id].append(EnumDefinition(name, extras["flags"], enum_base="IntFlag"))
        extras["flagset_name"] = name

    return extras


def _parse_single_property(element: Element, game_id: str, path: Path, include_id: bool = True) -> dict:
    parsed = {}
    if include_id:
        parsed.update({"id": int(element.attrib["ID"], 16)})
    name = element.find("Name")
    cook = element.find("CookPreference")
    parsed.update({
        "type": element.attrib["Type"],
        "name": name.text if name is not None and name.text is not None else "",
        "cook_preference": cook.text if cook is not None and cook.text is not None else "Always"
    })

    property_type_extras = {
        "Struct": _prop_struct,
        "Asset": _prop_asset,
        "Array": _prop_array,
        "Enum": _prop_choice,
        "Choice": _prop_choice,
        "Flags": _prop_flags,
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
                "choices": choices,
            }

        _enums_by_game[game_id].append(EnumDefinition(name, choices))

    return {
        "type": _type,
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


_to_snake_case_re = re.compile(r'(?<!^)(?=[A-Z])')
_invalid_chars_table = str.maketrans("", "", "()?")


def _filter_property_name(n: str) -> str:
    return inflection.underscore(n.replace(" ", "_").replace("#", "Number")).translate(_invalid_chars_table).lower()


def parse_game(templates_path: Path, game_xml: Path, game_id: str) -> dict:
    logging.info("Parsing templates for game %s: %s", game_id, game_xml)

    base_path = templates_path / game_xml.parent

    t = ElementTree.parse(templates_path / game_xml)
    root = t.getroot()

    states = get_key_map(root.find("States"))
    messages = get_key_map(root.find("Messages"))

    _enums_by_game[game_id] = [
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
    ]

    script_objects_paths = {
        four_cc: path
        for four_cc, path in get_paths(root.find("ScriptObjects")).items()
    }
    script_objects = {
        four_cc: parse_script_object_file(base_path / path, game_id)
        for four_cc, path in script_objects_paths.items()
    }
    property_archetypes = {
        name: parse_property_archetypes(base_path / path, game_id)
        for name, path in get_paths(root.find("PropertyArchetypes")).items()
    }

    code_path = Path(__file__).parent.joinpath("retro_data_structures", "properties", game_id.lower())
    import_base = f"retro_data_structures.properties.{game_id.lower()}"

    class LiteralPropType(typing.NamedTuple):
        python_type: str
        byte_count: int
        struct_format: str
        default: typing.Any

    _literal_prop_types = {
        "Int": LiteralPropType("int", 4, ">l", 0),
        "Float": LiteralPropType("float", 4, ">f", 0.0),
        "Bool": LiteralPropType("bool", 1, ">?", False),
        "Short": LiteralPropType("int", 4, ">h", 0),
    }

    core_path = code_path.joinpath("core")
    core_path.mkdir(parents=True, exist_ok=True)

    core_path.joinpath("Color.py").write_text("""# Generated file
import dataclasses
import struct
import typing


@dataclasses.dataclass()
class Color:
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 0.0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO):
        return cls(*struct.unpack('>ffff', data.read(16)))

    def to_stream(self, data: typing.BinaryIO):
        data.write(struct.pack('>ffff', self.r, self.g, self.b, self.a))
""")
    core_path.joinpath("Vector.py").write_text("""# Generated file
import dataclasses
import struct
import typing


@dataclasses.dataclass()
class Vector:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: int):
        return cls(*struct.unpack('>fff', data.read(12)))

    def to_stream(self, data: typing.BinaryIO):
        data.write(struct.pack('>fff', self.x, self.y, self.z))
""")
    core_path.joinpath("AssetId.py").write_text("AssetId = int\n")
    core_path.joinpath("AnimationParameters.py").write_text("""# Generated file
import dataclasses
import struct
import typing

from .AssetId import AssetId


@dataclasses.dataclass()
class AnimationParameters:
    ancs: AssetId = 0xFFFFFFFF
    character_index: int = 0
    initial_anim: int = 0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: int):
        return cls(*struct.unpack('>LLL', data.read(12)))

    def to_stream(self, data: typing.BinaryIO):
        data.write(struct.pack('>LLL', self.ancs, self.character_index, self.initial_anim))
""")
    core_path.joinpath("Spline.py").write_text("""# Generated file
import dataclasses
import typing


@dataclasses.dataclass()
class Spline:
    data: bytes = b""

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: int):
        result = cls()
        result.data = data.read(size)
        return result

    def to_stream(self, data: typing.BinaryIO):
        data.write(self.data)
""")

    known_enums: dict[str, EnumDefinition] = {_scrub_enum(e.name): e for e in _enums_by_game[game_id]}

    def get_prop_details(prop, meta: dict, needed_imports: dict[str, str],
                         ) -> tuple[str, bool, typing.Optional[str], str, str]:
        raw_type = prop["type"]
        prop_type = None
        need_enums = False
        comment = None
        parse_code = "None"
        build_code = "pass"

        if raw_type == "Struct":
            archetype_path: str = prop["archetype"].replace("_", ".")
            prop_type = archetype_path.split(".")[-1]
            needed_imports[f"{import_base}.archetypes.{archetype_path}"] = prop_type
            meta["default_factory"] = prop_type
            parse_code = f"{prop_type}.from_stream(data, property_size)"
            build_code = f"obj.to_stream(data)"

        elif prop['type'] == 'Choice':
            default_value = prop["default_value"] if prop['has_default'] else 0
            enum_name = _scrub_enum(prop["archetype"] or property_names.get(prop["id"]) or "")
            if enum_name in known_enums:
                prop_type = f"enums.{enum_name}"
                need_enums = True
                parse_code = f"enums.{enum_name}.from_stream(data, property_size)"
                build_code = f"obj.to_stream(data)"

                for key, value in known_enums[enum_name].values.items():
                    if value == default_value:
                        meta["default"] = f"enums.{enum_name}.{_scrub_enum(key)}"
            else:
                comment = "Choice"
                prop_type = "int"
                meta["default"] = repr(default_value)
                parse_code = _CODE_PARSE_UINT32
                build_code = f'data.write(struct.pack(">L", obj))'

        elif raw_type == "Flags":
            default_value = repr(prop["default_value"] if prop['has_default'] else 0)
            if "flagset_name" in prop:
                prop_type = "enums." + prop["flagset_name"]
                need_enums = True
                meta["default"] = f"{prop_type}({default_value})"
                parse_code = f"{prop_type}.from_stream(data, property_size)"
                build_code = f"obj.to_stream(data)"
            else:
                prop_type = "int"
                comment = "Flagset"
                meta["default"] = default_value
                parse_code = _CODE_PARSE_UINT32
                build_code = f'data.write(struct.pack(">L", obj))'

        elif raw_type in ["Asset", "Sound"]:
            prop_type = "AssetId"
            needed_imports[f"{import_base}.core.AssetId"] = "AssetId"
            if raw_type == "Asset":
                meta["metadata"] = repr({"asset_types": prop["type_filter"]})
                meta["default"] = "0xFFFFFFFF"
            else:
                meta["default"] = repr(prop["default_value"] if prop['has_default'] else 0)

            parse_code = _CODE_PARSE_UINT32
            build_code = f'data.write(struct.pack(">L", obj))'

        elif raw_type in ["AnimationSet", "Spline"]:
            if raw_type == "AnimationSet":
                prop_type = "AnimationParameters"
            else:
                prop_type = raw_type
            needed_imports[f"{import_base}.core.{prop_type}"] = prop_type
            parse_code = f"{prop_type}.from_stream(data, property_size)"
            build_code = f"obj.to_stream(data)"
            meta["default_factory"] = prop_type

        elif raw_type == "Array":
            inner_prop_type, need_enums, comment, inner_parse, inner_build = get_prop_details(
                prop["item_archetype"], {}, needed_imports,
            )
            prop_type = f"list[{inner_prop_type}]"
            meta["default_factory"] = "list"
            # TODO: code for parse and build

        elif raw_type == "String":
            prop_type = "str"
            meta["default"] = repr(prop["default_value"] if prop['has_default'] else "")
            parse_code = f'data.read({_CODE_PARSE_UINT32}).decode("utf-8")'
            build_code = f'obj = obj.encode("utf-8"); data.write(struct.pack(">L", len(obj))); data.write(obj)'

        elif raw_type in ["Color", "Vector"]:
            prop_type = raw_type
            needed_imports[f"{import_base}.core.{raw_type}"] = prop_type
            parse_code = f"{prop_type}.from_stream(data, property_size)"
            build_code = f"obj.to_stream(data)"

            if prop['has_default']:
                if raw_type == "Color":
                    value = {"A": 0.0, **prop["default_value"]}
                    meta["default_factory"] = "lambda: Color(r={R}, g={G}, b={B}, a={A})".format(**value)
                else:
                    meta["default_factory"] = "lambda: Vector(x={X}, y={Y}, z={Z})".format(**prop["default_value"])
            else:
                meta["default_factory"] = prop_type

        elif raw_type in _literal_prop_types:
            literal_prop = _literal_prop_types[raw_type]
            prop_type = literal_prop.python_type
            parse_code = f"struct.unpack({repr(literal_prop.struct_format)}, data.read({literal_prop.byte_count}))[0]"
            build_code = f"data.write(struct.pack({repr(literal_prop.struct_format)}, obj))"

            default_value = prop["default_value"] if prop['has_default'] else literal_prop.default
            try:
                struct.pack(literal_prop.struct_format, default_value)
            except struct.error as e:
                print(f"{hex(prop['id'])} has invalid default value  {default_value}: {e}")
                default_value = literal_prop.default
            meta["default"] = repr(default_value)

        return prop_type, need_enums, comment, parse_code, build_code

    def parse_struct(name: str, this, output_path: Path):
        if this["type"] != "Struct":
            print("Ignoring {}. Is a {}".format(name, this["type"]))
            return

        all_names = [
            _filter_property_name(prop["name"] or property_names.get(prop["id"]) or "unnamed")
            for prop in this["properties"]
        ]

        needed_imports = {}
        need_enums = False

        class_name = name.split("_")[-1]
        class_path = name.replace("_", "/")

        class_code = f"@dataclasses.dataclass()\nclass {class_name}:\n"
        properties_decoder = ""
        properties_builder = ""

        for prop, prop_name in zip(this["properties"], all_names):
            if all_names.count(prop_name) > 1:
                prop_name += "_0x{:08x}".format(prop["id"])

            meta = {}
            prop_type, set_need_enums, comment, parse_code, build_code = get_prop_details(prop, meta, needed_imports)
            need_enums = need_enums or set_need_enums

            if prop_type is None:
                raise ValueError(f"Unable to parse property {prop_name} of {name}")

            class_code += f"    {prop_name}: {prop_type}"
            if meta:
                class_code += " = dataclasses.field({})".format(
                    ", ".join(
                        f"{key}={value}"
                        for key, value in meta.items()
                    )
                )

            if comment is not None:
                class_code += f"  # {comment}"
            class_code += "\n"

            if this["atomic"]:
                properties_decoder += f"        result.{prop_name} = {parse_code}\n"
                properties_builder += f"        obj = self.{prop_name}\n"
                properties_builder += f"        {build_code}\n"
            else:
                need_else = bool(properties_decoder)
                properties_decoder += "            "
                if need_else:
                    properties_decoder += "el"

                properties_decoder += f"if property_id == {hex(prop['id'])}:\n"
                properties_decoder += f"                result.{prop_name} = {parse_code}\n"
                prop_id_bytes = struct.pack(">L", prop["id"])
                placeholder = repr(b'\x00\x00')
                properties_builder += f"\n        obj = self.{prop_name}\n"
                properties_builder += f'        data.write({repr(prop_id_bytes)})  # {hex(prop["id"])}\n'
                properties_builder += f"        before = data.tell()\n"
                properties_builder += f"        data.write({placeholder})  # size placeholder\n"
                properties_builder += f"        {build_code}\n"
                properties_builder += f"        after = data.tell()\n"
                properties_builder += f"        data.seek(before)\n"
                properties_builder += f'        data.write(struct.pack(">H", after - before - 2))\n'
                properties_builder += f'        data.seek(after)\n'

        class_code += f"""
    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: int):
        result = cls()
"""
        if this["atomic"]:
            class_code += properties_decoder
        else:
            class_code += f"""
        property_count = {_CODE_PARSE_UINT16}
        for _ in range(property_count):
            property_id = {_CODE_PARSE_UINT32}
            property_size = {_CODE_PARSE_UINT16}
            start = data.tell()
"""
            class_code += properties_decoder
            class_code += """            else:
                data.read(property_size)  # skip unknown property
            assert data.tell() - start == property_size
"""

        class_code += f"""
        return result
"""

        class_code += f"""
    def to_stream(self, data: typing.BinaryIO):
"""
        if not this["atomic"]:
            # TODO: respect cook preference
            property_count = len(this["properties"])
            prop_count_repr = repr(struct.pack(">H", property_count))
            class_code += f"        data.write({prop_count_repr})  # {property_count} properties\n"
        class_code += properties_builder

        code_code = "# Generated File\n"
        code_code += "import dataclasses\nimport struct\nimport typing\n"
        if need_enums or needed_imports:
            code_code += "\n"

        if need_enums:
            code_code += f"import retro_data_structures.enums.{game_id.lower()} as enums\n"

        for import_path, code_import in sorted(needed_imports.items()):
            code_code += f"from {import_path} import {code_import}\n"

        code_code += "\n\n"
        code_code += class_code
        final_path = output_path.joinpath(class_path).with_suffix(".py")
        final_path.parent.mkdir(parents=True, exist_ok=True)
        final_path.write_text(code_code)

    getter_func = "def get_object(four_cc: str):\n"
    path = code_path.joinpath("objects")
    path.mkdir(parents=True, exist_ok=True)
    for object_fourcc, script_object in script_objects.items():
        stem = Path(script_objects_paths[object_fourcc]).stem
        parse_struct(stem, script_object, path)
        getter_func += f"    if four_cc == {repr(object_fourcc)}:\n"
        getter_func += f"        from .{stem} import {stem}\n"
        getter_func += f"        return {stem}\n"
    getter_func += '    raise ValueError(f"Unknown four_cc: {four_cc}")\n'
    path.joinpath("__init__.py").write_text(getter_func)

    print("> Creating archetypes")
    path = code_path.joinpath("archetypes")
    path.mkdir(parents=True, exist_ok=True)
    for archetype_name, archetype in property_archetypes.items():
        parse_struct(archetype_name, archetype, path)
    print("> Done.")

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


def parse(game_ids: typing.Optional[typing.Iterable[str]] = None) -> dict:
    base_dir = Path(__file__).parent
    templates_path = base_dir.joinpath("PrimeWorldEditor/templates")
    read_property_names(templates_path / "PropertyMap.xml")

    game_list = parse_game_list(templates_path)
    _parse_choice.unknowns = {game: 0 for game in game_list.keys()}

    return {
        _id: parse_game(templates_path, game_path, _id)
        for _id, game_path in game_list.items()
        if game_ids is None or _id in game_ids
    }


def persist_data(parse_result):
    logging.info("Persisting the parsed properties")
    base_dir = Path(__file__).parent

    # First write the enums
    for game_id in parse_result.keys():
        if game_id in _game_id_to_file:
            base_dir.joinpath(f"retro_data_structures/enums/{_game_id_to_file[game_id]}.py").write_text(
                create_enums_file(_enums_by_game[game_id])
            )

    # Now import these files, since they depend on the generated enum files
    from retro_data_structures.property_template import PropertyNames, GameTemplate

    encoded = PropertyNames.build(property_names)
    base_dir.joinpath(f"retro_data_structures/properties/property_names.pname").write_bytes(encoded)

    for game_id, template in parse_result.items():
        if game_id in _game_id_to_file:
            encoded = GameTemplate.build(template)
            base_dir.joinpath(f"retro_data_structures/properties/{game_id}.prop").write_bytes(encoded)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    persist_data(parse(["Echoes"]))
