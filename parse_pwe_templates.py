import dataclasses
import keyword
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
        code += '    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):\n'
        code += f'        return cls({_CODE_PARSE_UINT32})\n'

        code += '\n    def to_stream(self, data: typing.BinaryIO):\n'
        code += '        data.write(struct.pack(">L", self.value))\n'

        code += '\n    @classmethod\n'
        code += '    def from_json(cls, data):\n'
        code += '        return cls(data)\n'

        code += '\n    def to_json(self):\n'
        code += '        return self.value\n'

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

        if name == "Unknown" and element.attrib.get("ID"):
            name += f'_{element.attrib.get("ID")}'

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
_invalid_chars_table = str.maketrans("", "", "()?'")
_to_underscore_table = str.maketrans("/ ", "__")


def _filter_property_name(n: str) -> str:
    result = inflection.underscore(n.translate(_to_underscore_table).replace("#", "Number")
                                   ).translate(_invalid_chars_table).lower()
    if keyword.iskeyword(result):
        result += "_"
    return result


def _ensure_is_generated_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    path.joinpath(".gitignore").write_text("*")
    init = path.joinpath("__init__.py")
    if not init.is_file():
        init.write_text("")


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
    _ensure_is_generated_dir(code_path)
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
        "Short": LiteralPropType("int", 2, ">h", 0),
    }

    core_path = code_path.joinpath("core")
    _ensure_is_generated_dir(core_path)

    core_path.joinpath("Color.py").write_text("""# Generated file
import dataclasses
import struct
import typing

from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class Color(BaseProperty):
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 0.0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        return cls(*struct.unpack('>ffff', data.read(16)))

    def to_stream(self, data: typing.BinaryIO):
        data.write(struct.pack('>ffff', self.r, self.g, self.b, self.a))

    @classmethod
    def from_json(cls, data: dict):
        return cls(data["r"], data["g"], data["b"], data["a"])

    def to_json(self) -> dict:
        return {
            "r": self.r,
            "g": self.g,
            "b": self.b,
            "a": self.a,
        }
""")
    core_path.joinpath("Vector.py").write_text("""# Generated file
import dataclasses
import struct
import typing

from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class Vector(BaseProperty):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        return cls(*struct.unpack('>fff', data.read(12)))

    def to_stream(self, data: typing.BinaryIO):
        data.write(struct.pack('>fff', self.x, self.y, self.z))

    @classmethod
    def from_json(cls, data: dict):
        return cls(data["x"], data["y"], data["z"])

    def to_json(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }
""")
    core_path.joinpath("AssetId.py").write_text("AssetId = int\n")
    core_path.joinpath("AnimationParameters.py").write_text("""# Generated file
import dataclasses
import struct
import typing

from retro_data_structures.properties.base_property import BaseProperty
from .AssetId import AssetId


@dataclasses.dataclass()
class AnimationParameters(BaseProperty):
    ancs: AssetId = 0xFFFFFFFF
    character_index: int = 0
    initial_anim: int = 0

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        return cls(*struct.unpack('>LLL', data.read(12)))

    def to_stream(self, data: typing.BinaryIO):
        data.write(struct.pack('>LLL', self.ancs, self.character_index, self.initial_anim))

    @classmethod
    def from_json(cls, data: dict):
        return cls(data["ancs"], data["character_index"], data["initial_anim"])

    def to_json(self) -> dict:
        return {
            "ancs": self.ancs,
            "character_index": self.character_index,
            "initial_anim": self.initial_anim,
        }
""")
    core_path.joinpath("Spline.py").write_text("""# Generated file
import dataclasses
import typing
import base64

from retro_data_structures.properties.base_property import BaseProperty


@dataclasses.dataclass()
class Spline(BaseProperty):
    data: bytes = b""

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        assert size is not None
        result = cls()
        result.data = data.read(size)
        return result

    def to_stream(self, data: typing.BinaryIO):
        data.write(self.data)

    @classmethod
    def from_json(cls, data):
        return cls(base64.b64decode(data))

    def to_json(self) -> str:
        return base64.b64encode(self.data).decode("ascii")
""")

    known_enums: dict[str, EnumDefinition] = {_scrub_enum(e.name): e for e in _enums_by_game[game_id]}

    @dataclasses.dataclass
    class PropDetails:
        prop_type: str
        need_enums: bool
        comment: typing.Optional[str]
        parse_code: str
        build_code: list[str]
        from_json_code: str
        to_json_code: str
        custom_cook_pref: bool

    def get_prop_details(prop, meta: dict, needed_imports: dict[str, str],
                         ) -> PropDetails:
        raw_type = prop["type"]
        prop_type = None
        need_enums = False
        comment = None
        parse_code = "None"
        build_code = []
        from_json_code = "None"
        to_json_code = "None"

        if raw_type == "Struct":
            archetype_path: str = prop["archetype"].replace("_", ".")
            prop_type = archetype_path.split(".")[-1]
            needed_imports[f"{import_base}.archetypes.{archetype_path}"] = prop_type
            meta["default_factory"] = prop_type
            parse_code = f"{prop_type}.from_stream(data, property_size)"
            build_code.append("{obj}.to_stream(data)")
            from_json_code = f"{prop_type}.from_json({{obj}})"
            to_json_code = "{obj}.to_json()"

        elif prop['type'] in ['Choice', 'Enum']:
            default_value = prop["default_value"] if prop['has_default'] else 0
            enum_name = _scrub_enum(prop["archetype"] or property_names.get(prop["id"]) or "")

            uses_known_enum = enum_name in known_enums and (
                    default_value in list(known_enums[enum_name].values.values())
            )
            if uses_known_enum:
                prop_type = f"enums.{enum_name}"
                need_enums = True
                parse_code = f"enums.{enum_name}.from_stream(data)"
                build_code.append("{obj}.to_stream(data)")
                from_json_code = f"{prop_type}.from_json({{obj}})"
                to_json_code = "{obj}.to_json()"

                for key, value in known_enums[enum_name].values.items():
                    if value == default_value:
                        meta["default"] = f"enums.{enum_name}.{_scrub_enum(key)}"
                assert "default" in meta
            else:
                comment = "Choice"
                prop_type = "int"
                meta["default"] = repr(default_value)
                parse_code = _CODE_PARSE_UINT32
                build_code.append('data.write(struct.pack(">L", {obj}))')
                from_json_code = "{obj}"
                to_json_code = "{obj}"

        elif raw_type == "Flags":
            default_value = repr(prop["default_value"] if prop['has_default'] else 0)
            if "flagset_name" in prop:
                prop_type = "enums." + _scrub_enum(prop["flagset_name"])
                need_enums = True
                meta["default"] = f"{prop_type}({default_value})"
                parse_code = f"{prop_type}.from_stream(data)"
                build_code.append("{obj}.to_stream(data)")
                from_json_code = f"{prop_type}.from_json({{obj}})"
                to_json_code = "{obj}.to_json()"
            else:
                prop_type = "int"
                comment = "Flagset"
                meta["default"] = default_value
                parse_code = _CODE_PARSE_UINT32
                build_code.append('data.write(struct.pack(">L", {obj}))')
                from_json_code = "{obj}"
                to_json_code = "{obj}"

        elif raw_type in ["Asset", "Sound"]:
            prop_type = "AssetId"
            needed_imports[f"{import_base}.core.AssetId"] = "AssetId"
            if raw_type == "Asset":
                meta["metadata"] = repr({"asset_types": prop["type_filter"]})
                if game_id in ["Prime", "Echoes"]:
                    default_value = 0xFFFFFFFF
                else:
                    default_value = 0xFFFFFFFFFFFFFFFF
            else:
                default_value = prop["default_value"] if prop['has_default'] else 0

            if game_id in ["Prime", "Echoes"]:
                format_specifier = '">L"'
                byte_count = 4
            else:
                format_specifier = '">Q"'
                byte_count = 8

            meta["default"] = hex(default_value)
            parse_code = f'struct.unpack({format_specifier}, data.read({byte_count}))[0]'
            build_code.append(f'data.write(struct.pack({format_specifier}, {{obj}}))')
            from_json_code = "{obj}"
            to_json_code = "{obj}"

        elif raw_type in ["AnimationSet", "Spline"]:
            if raw_type == "AnimationSet":
                prop_type = "AnimationParameters"
            else:
                prop_type = raw_type
            needed_imports[f"{import_base}.core.{prop_type}"] = prop_type
            parse_code = f"{prop_type}.from_stream(data, property_size)"
            build_code.append("{obj}.to_stream(data)")
            from_json_code = f"{prop_type}.from_json({{obj}})"
            to_json_code = "{obj}.to_json()"
            meta["default_factory"] = prop_type

        elif raw_type == "Array":
            inner_prop = get_prop_details(
                prop["item_archetype"], {}, needed_imports,
            )

            prop_type = f"list[{inner_prop.prop_type}]"
            need_enums = inner_prop.need_enums
            comment = inner_prop.comment
            meta["default_factory"] = "list"
            parse_code = f"[{inner_prop.parse_code} for _ in range({_CODE_PARSE_UINT32})]"
            build_code.extend([
                'array = {obj}',
                'data.write(struct.pack(">L", len(array)))',
                'for item in array:',
                *['    ' + inner.format(obj="item") for inner in inner_prop.build_code]
            ])
            from_json_code = "[{inner} for item in {{obj}}]".format(
                inner=inner_prop.from_json_code.format(obj="item")
            )
            to_json_code = "[{inner} for item in {{obj}}]".format(
                inner=inner_prop.to_json_code.format(obj="item")
            )

        elif raw_type == "String":
            prop_type = "str"
            meta["default"] = repr(prop["default_value"] if prop['has_default'] else "")
            null_byte = repr(b"\x00")
            parse_code = f'b"".join(iter(lambda: data.read(1), {null_byte})).decode("utf-8")'
            build_code.extend([
                'data.write({obj}.encode("utf-8"))',
                f'data.write({null_byte})',
            ])
            from_json_code = "{obj}"
            to_json_code = "{obj}"

        elif raw_type in ["Color", "Vector"]:
            prop_type = raw_type
            needed_imports[f"{import_base}.core.{raw_type}"] = prop_type
            parse_code = f"{prop_type}.from_stream(data)"
            build_code.append("{obj}.to_stream(data)")
            from_json_code = f"{prop_type}.from_json({{obj}})"
            to_json_code = "{obj}.to_json()"

            s = struct.Struct(">f")

            if prop['has_default']:
                default_value = {
                    k: s.unpack(s.pack(v))[0]
                    for k, v in prop["default_value"].items()
                }
                if raw_type == "Color":
                    value = {"A": 0.0, **default_value}
                    meta["default_factory"] = "lambda: Color(r={R}, g={G}, b={B}, a={A})".format(**value)
                else:
                    meta["default_factory"] = "lambda: Vector(x={X}, y={Y}, z={Z})".format(**default_value)
            else:
                meta["default_factory"] = prop_type

        elif raw_type in _literal_prop_types:
            literal_prop = _literal_prop_types[raw_type]
            prop_type = literal_prop.python_type
            parse_code = f"struct.unpack({repr(literal_prop.struct_format)}, data.read({literal_prop.byte_count}))[0]"
            build_code.append(f"data.write(struct.pack({repr(literal_prop.struct_format)}, {{obj}}))")
            from_json_code = "{obj}"
            to_json_code = "{obj}"

            default_value = prop["default_value"] if prop['has_default'] else literal_prop.default
            try:
                s = struct.Struct(literal_prop.struct_format)
                default_value = s.unpack(s.pack(default_value))[0]
            except struct.error as e:
                print(f"{hex(prop['id'])} has invalid default value  {default_value}: {e}")
                default_value = literal_prop.default
            meta["default"] = repr(default_value)

        if "default" not in meta and "default_factory" not in meta:
            raise ValueError(f"Unable to find default value for prop {prop}.")

        if prop_type is None:
            print("what?")
            print(prop)

        return PropDetails(prop_type, need_enums, comment, parse_code, build_code, from_json_code, to_json_code,
                           custom_cook_pref=prop['cook_preference'] != "Always")

    def parse_struct(name: str, this, output_path: Path, is_struct: bool):
        if this["type"] != "Struct":
            print("Ignoring {}. Is a {}".format(name, this["type"]))
            return

        all_names = [
            _filter_property_name(prop["name"] or property_names.get(prop["id"]) or "unnamed")
            for prop in this["properties"]
        ]

        needed_imports = {}
        need_enums = False
        has_custom_cook_pref = False

        class_name = name.split("_")[-1]
        class_path = name.replace("_", "/")

        # We created a nested module, but there was already a class with that name.
        rename_root = output_path
        for part in class_path.split("/")[:-1]:
            nested_dir = rename_root.joinpath(part)
            maybe_file = rename_root.joinpath(part + ".py")

            _ensure_is_generated_dir(nested_dir)
            if maybe_file.is_file():
                maybe_file.replace(rename_root.joinpath(part, "__init__.py"))
            rename_root = nested_dir

        class_code = f"@dataclasses.dataclass()\nclass {class_name}(BaseProperty):\n"
        properties_decoder = ""
        properties_builder = ""
        json_builder = ""
        json_parser = ""

        for prop, prop_name in zip(this["properties"], all_names):
            if all_names.count(prop_name) > 1:
                prop_name += "_0x{:08x}".format(prop["id"])

            meta = {}
            # prop_type, set_need_enums, comment, parse_code, build_code, from_json_code, to_json_code =
            pdetails = get_prop_details(
                prop, meta, needed_imports
            )
            need_enums = need_enums or pdetails.need_enums
            has_custom_cook_pref = has_custom_cook_pref or pdetails.custom_cook_pref

            if pdetails.prop_type is None:
                raise ValueError(f"Unable to parse property {prop_name} of {name}")

            class_code += f"    {prop_name}: {pdetails.prop_type}"
            if meta:
                class_code += " = dataclasses.field({})".format(
                    ", ".join(
                        f"{key}={value}"
                        for key, value in meta.items()
                    )
                )

            if pdetails.comment is not None:
                class_code += f"  # {pdetails.comment}"
            class_code += "\n"

            json_builder += f"            {repr(prop_name)}: {pdetails.to_json_code.format(obj=f'self.{prop_name}')},\n"
            json_parser += f"            {prop_name}={pdetails.from_json_code.format(obj=f'data[{repr(prop_name)}]')},\n"
            if this["atomic"] or game_id == "Prime":
                properties_decoder += f"        result.{prop_name} = {pdetails.parse_code}\n"
                for build in pdetails.build_code:
                    properties_builder += f"        {build.format(obj=f'self.{prop_name}')}\n"
            else:
                need_else = bool(properties_decoder)
                properties_decoder += "            "
                if need_else:
                    properties_decoder += "el"

                properties_decoder += f"if property_id == {hex(prop['id'])}:\n"
                properties_decoder += f"                result.{prop_name} = {pdetails.parse_code}\n"
                prop_id_bytes = struct.pack(">L", prop["id"])
                placeholder = repr(b'\x00\x00')
                properties_builder += "\n"
                if pdetails.custom_cook_pref:
                    properties_builder += f"        # Cook Preference: {prop['cook_preference']} (Not Implemented)\n"
                properties_builder += f'        data.write({repr(prop_id_bytes)})  # {hex(prop["id"])}\n'
                properties_builder += f"        before = data.tell()\n"
                properties_builder += f"        data.write({placeholder})  # size placeholder\n"
                for build in pdetails.build_code:
                    properties_builder += f"        {build.format(obj=f'self.{prop_name}')}\n"
                properties_builder += f"        after = data.tell()\n"
                properties_builder += f"        data.seek(before)\n"
                properties_builder += f'        data.write(struct.pack(">H", after - before - 2))\n'
                properties_builder += f'        data.seek(after)\n'

        # from stream

        class_code += f"""
    @classmethod
    def from_stream(cls, data: typing.BinaryIO, size: typing.Optional[int] = None):
        result = cls()
"""
        if this["atomic"] or game_id == "Prime":
            class_code += "        property_size = None\n"
            if game_id == "Prime" and is_struct:
                class_code += f"        property_count = {_CODE_PARSE_UINT32}\n"

            class_code += properties_decoder
        else:
            if is_struct:
                class_code += f"        struct_id = {_CODE_PARSE_UINT32}\n"
                class_code += "        assert struct_id == 0xFFFFFFFF\n"
                class_code += f"        size = {_CODE_PARSE_UINT16}\n"
                class_code += "        root_size_start = data.tell()\n"

            class_code += f"""
        property_count = {_CODE_PARSE_UINT16}
        for _ in range(property_count):
            property_id = {_CODE_PARSE_UINT32}
            property_size = {_CODE_PARSE_UINT16}
            start = data.tell()
"""
            class_code += properties_decoder
            class_code += "            else:\n"
            class_code += "                data.read(property_size)  # skip unknown property\n"
            class_code += "            assert data.tell() - start == property_size\n"

        if is_struct and not this["atomic"] and game_id != "Prime":
            class_code += "        assert data.tell() - root_size_start == size\n"

        class_code += f"""
        return result
"""

        # to stream

        class_code += f"""
    def to_stream(self, data: typing.BinaryIO):
"""
        if has_custom_cook_pref:
            assert game_id != "Prime"

        has_root_size_offset = False
        property_count = len(this["properties"])

        if not this["atomic"]:
            if is_struct and game_id != "Prime":
                null_bytes = repr(b"\xFF\xFF\xFF\xFF")
                class_code += f"        data.write({null_bytes})  # struct object id\n"
                placeholder = repr(b'\x00\x00')
                class_code += "        root_size_offset = data.tell()\n"
                class_code += f"        data.write({placeholder})  # placeholder for root struct size\n"
                has_root_size_offset = True

            elif has_custom_cook_pref:
                class_code += "        num_properties_offset = data.tell()\n"

            if game_id != "Prime" or is_struct:
                prop_count_repr = repr(struct.pack(">H" if game_id != "Prime" else ">L", property_count))
                class_code += f"        data.write({prop_count_repr})  # {property_count} properties\n"
                if has_custom_cook_pref:
                    class_code += f"        num_properties_written = {property_count}\n"
        else:
            assert not has_custom_cook_pref

        class_code += properties_builder

        if has_root_size_offset:
            class_code += "\n        struct_end_offset = data.tell()\n"
            class_code += "        data.seek(root_size_offset)\n"
            class_code += '        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))\n'
            if has_custom_cook_pref:
                class_code += '        data.write(struct.pack(">H", num_properties_written))\n'
            class_code += "        data.seek(struct_end_offset)\n"

        elif has_custom_cook_pref:
            class_code += "\n"
            class_code += f"        if num_properties_written != {property_count}:\n"
            class_code += "            struct_end_offset = data.tell()\n"
            class_code += "            data.seek(num_properties_offset)\n"
            class_code += '            data.write(struct.pack(">H", num_properties_written))\n'
            class_code += "            data.seek(struct_end_offset)\n"

        # from json
        class_code += """
    @classmethod
    def from_json(cls, data: dict):
        return cls(
"""
        class_code += json_parser + "        )\n"

        # to json
        class_code += """
    def to_json(self) -> dict:
        return {
"""
        class_code += json_builder + "        }\n"

        code_code = "# Generated File\n"
        code_code += "import dataclasses\nimport struct\nimport typing\n"
        code_code += "\nfrom retro_data_structures.properties.base_property import BaseProperty\n"

        if need_enums:
            code_code += f"import retro_data_structures.enums.{game_id.lower()} as enums\n"

        for import_path, code_import in sorted(needed_imports.items()):
            code_code += f"from {import_path} import {code_import}\n"

        code_code += "\n\n"
        code_code += class_code
        final_path = output_path.joinpath(class_path).with_suffix(".py")
        final_path.parent.mkdir(parents=True, exist_ok=True)

        # There's already a module with same name as this class. Place it as the __init__.py inside
        if final_path.with_suffix("").is_dir():
            final_path = final_path.with_suffix("").joinpath("__init__.py")

        _ensure_is_generated_dir(final_path.parent)
        final_path.write_text(code_code)

    getter_func = "# Generated File\n"
    getter_func += "import typing\n\n"
    getter_func += "from retro_data_structures.properties.base_property import BaseProperty\n"
    getter_func += "\n\ndef get_object(four_cc: str) -> typing.Type[BaseProperty]:\n"
    path = code_path.joinpath("objects")
    _ensure_is_generated_dir(path)
    for object_fourcc, script_object in script_objects.items():
        stem = Path(script_objects_paths[object_fourcc]).stem
        parse_struct(stem, script_object, path, is_struct=True)
        getter_func += f"    if four_cc == {repr(object_fourcc)}:\n"
        getter_func += f"        from .{stem} import {stem}\n"
        getter_func += f"        return {stem}\n"
    getter_func += '    raise ValueError(f"Unknown four_cc: {four_cc}")\n'
    path.joinpath("__init__.py").write_text(getter_func)

    print("> Creating archetypes")
    path = code_path.joinpath("archetypes")
    _ensure_is_generated_dir(path)
    for archetype_name, archetype in property_archetypes.items():
        parse_struct(archetype_name, archetype, path, is_struct=False)
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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # persist_data(parse(["Prime"]))
    persist_data(parse(_game_id_to_file.keys()))
