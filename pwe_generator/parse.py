"""Reads the templates of one game into `GameData`."""

from __future__ import annotations

import keyword
import re
import struct
import typing
from pathlib import Path
from xml.etree import ElementTree

import inflection

from pwe_generator.model import Codec, GameData, GClass, GEnum, GField, PrimeEditorSpec, Value, lit
from retro_data_structures.game_check import Game

if typing.TYPE_CHECKING:
    from xml.etree.ElementTree import Element


def find_assured(element: Element, path: str) -> Element:
    e = element.find(path)
    assert e is not None, path
    return e


def scrub_enum(string: str) -> str:
    s = re.sub(r"\W", "", string)  # remove non-word characters
    s = re.sub(r"^(?=\d)", "_", s)  # add leading underscore to strings starting with a number
    s = re.sub(r"^None$", "_None", s)  # add leading underscore to None
    return s or "_EMPTY"  # add name for empty string keys


_invalid_chars_table = str.maketrans("", "", "()?'")
_to_underscore_table = str.maketrans("/ ", "__")


def filter_property_name(n: str) -> str:
    result = (
        inflection.underscore(n.translate(_to_underscore_table).replace("#", "Number"))
        .translate(_invalid_chars_table)
        .lower()
    )
    if result[:1].isdigit():
        result = "number_" + result
    if keyword.iskeyword(result):
        result += "_"
    return result


def parse_int_text(text: str, default_base: int = 10) -> int:
    text = text.strip()
    if text.lower().startswith(("0x", "-0x")):
        return int(text, 16)
    return int(text, default_base)


def read_property_names(map_path: Path) -> dict[int, str]:
    root = ElementTree.parse(map_path).getroot()
    m = find_assured(root, "PropertyMap")
    return {
        int(find_assured(item, "Key").attrib["ID"], 16): find_assured(item, "Value").attrib["Name"]
        for item in typing.cast("typing.Iterable[Element]", m)
    }


# Prime properties that are only present when another (bool) property is set
# Maps class name -> property -> the property that controls it.
PRIME_CONDITIONAL_PROPERTIES: dict[str, dict[str, str]] = {
    # The game also reads a bitset after these when it's set, which isn't supported.
    "Water": {
        "ignore_0x0000003d": "unknown_will_crash_if_on",
        "ignore_0x0000003e": "unknown_will_crash_if_on",
    },
}

# Prime classes whose count conditions are irregular: the properties are kept required.
PRIME_IRREGULAR_COUNTS: set[str] = set()
# Prime classes where the properties after the optional ones are always there (the template says so)
PRIME_REQUIRED_AFTER_OPTIONAL = {"ControllerAction"}

_COUNT_CONDITION = re.compile(r"^(?:only read if )?(?:struct )?(?:propCount|property count) (>=|>) (\d+)")
_PAL_CONDITION = re.compile(r"\(struct property count (>=|>) (\d+)\)")


def min_property_count(condition: str | None) -> int | None:
    """
    The smallest property count of a Prime struct for which a property is in the data, from the `LoadCondition` of its
    template. None if the property is always there, or if the condition is not a simple threshold.
    """
    if condition is None or "always true" in condition or "instead" in condition:
        return None
    match = _COUNT_CONDITION.match(condition) or _PAL_CONDITION.search(condition)
    if match is None:
        return None
    return int(match.group(2)) + (1 if match.group(1) == ">" else 0)


# Names that a field can't have: they are used by the base classes
RESERVED_FIELD_NAMES = {
    "game",
    "games",
    "modules",
    "object_type",
    "get_name",
    "set_name",
    "set_game",
    "to_game",
    "from_stream",
    "to_stream",
    "from_bytes",
    "to_bytes",
    "from_json",
    "to_json",
    "dependencies_for",
    "unknown_properties",
}

ENUMS_THAT_ALLOW_UNKNOWN_VALUES = {"InventorySlotEnum"}

_SCALARS = {
    "Int": ("s32", "l"),
    "UInt": ("u32", "L"),
    "Float": ("f32", "f"),
    "Bool": ("bool_", "?"),
    "Short": ("s16", "h"),
    "Animation": ("s32", "l"),  # Index of a character animation, -1 when unset
}


def _py(expr: str, factory: bool = False) -> Value:
    return Value("py", expr, factory)


class GameParser:
    def __init__(self, game: Game, templates_path: Path, game_xml: Path, property_names: dict[int, str]):
        self.game = game
        self.templates_path = templates_path
        self.game_xml = game_xml
        self.base_path = templates_path / game_xml.parent
        self.property_names = property_names
        self.data = GameData(game)
        self._enum_defs: dict[tuple, GEnum] = {}
        self._archetypes: dict[str, dict] = {}
        self._field_names: dict[str, dict[int, str]] = {}

    # Raw parsing of the xml files

    def _register_enum(self, name: str, kind: str, values: dict[str, int], owner: Path | None) -> tuple:
        key = (name, kind, tuple(values.items()))
        definition = self._enum_defs.get(key)
        if definition is None:
            definition = self._enum_defs[key] = GEnum(self.game, name, kind, dict(values), base="IntEnum")
        if owner is not None and owner.parent.stem != "Enums":
            definition.owners.append(owner.stem)
        return key

    def _prop_default_value(self, element: Element) -> dict:
        default_value_types = {
            "Int": lambda el: struct.unpack("<l", struct.pack("<L", (int(el.text, 10) & 0xFFFFFFFF)))[0],
            "Animation": lambda el: struct.unpack("<l", struct.pack("<L", (int(el.text, 10) & 0xFFFFFFFF)))[0],
            "Float": lambda el: float(el.text),
            "Bool": lambda el: el.text == "true",
            "Short": lambda el: int(el.text, 10) & 0xFFFF,
            "Color": lambda el: {e.tag: float(e.text) for e in el},
            "Vector": lambda el: {e.tag: float(e.text) for e in el},
            "Flags": lambda el: parse_int_text(el.text) & 0xFFFFFFFF,
            "Choice": lambda el: parse_int_text(el.text) & 0xFFFFFFFF,
            "Enum": lambda el: parse_int_text(el.text, 16) & 0xFFFFFFFF,
            "Sound": lambda el: struct.unpack("<l", struct.pack("<L", parse_int_text(el.text) & 0xFFFFFFFF))[0],
        }
        default_value = None
        has_default = False
        if (default_value_element := element.find("DefaultValue")) is not None:
            default_value = default_value_types.get(element.attrib["Type"], lambda el: el.text)(default_value_element)
            has_default = True
        return {"has_default": has_default, "default_value": default_value}

    def _prop_struct(self, element: Element, path: Path) -> dict:
        return {
            "archetype": element.attrib.get("Archetype"),
            "properties": self._parse_properties(element, path)["properties"],
        }

    def _prop_asset(self, element: Element, path: Path) -> dict:
        type_filter = []
        if (filt := element.find("TypeFilter")) is not None:
            type_filter = [t.text for t in filt]
        return {"type_filter": type_filter}

    def _prop_array(self, element: Element, path: Path) -> dict:
        item_archetype = None
        if (item_archetype_element := element.find("ItemArchetype")) is not None:
            item_archetype = self._parse_single_property(item_archetype_element, path, include_id=False)
        return {"item_archetype": item_archetype}

    def _prop_choice(self, element: Element, path: Path) -> dict:
        extras = {"archetype": element.attrib.get("Archetype")}
        extras["enum_def"] = self._parse_choice(element, path).get("enum_def")
        extras.update(self._prop_default_value(element))
        return extras

    def _prop_flags(self, element: Element, path: Path) -> dict:
        extras = self._prop_default_value(element)
        if element.find("Flags") is None and (archetype := element.attrib.get("Archetype")) is not None:
            # The flags are defined in a shared Flags archetype, which registers the enum.
            extras["flagset_name"] = archetype
            extras["archetype"] = archetype
            return extras

        if (flags_element := element.find("Flags")) is not None:
            extras["flags"] = {e.attrib["Name"]: int(e.attrib["Mask"], 16) for e in flags_element.findall("Element")}

            element_id = element.attrib.get("ID")
            name = None
            if (ele_name := element.find("Name")) is not None:
                name = ele_name.text
            elif element_id is not None:
                name = self.property_names.get(int(element_id, 16))

            if name is None:
                name = "Unknown"
            if name == "Unknown" and element_id is not None:
                name += f"_{element_id}"
            if name == path.stem:
                name += "Flags"

            extras["enum_def"] = self._register_enum(name, "flags", extras["flags"], path)
            extras["flagset_name"] = name
        return extras

    def _parse_single_property(self, element: Element, path: Path, include_id: bool = True) -> dict:
        parsed: dict[str, typing.Any] = {}
        if include_id:
            parsed["id"] = int(element.attrib["ID"], 16)

        if (name := element.attrib.get("Name", "")) == "":
            name_element = element.find("Name")
            name = name_element.text if name_element is not None and name_element.text is not None else ""

        cook = element.find("CookPreference")
        load_condition = element.find("LoadCondition")
        parsed.update(
            {
                "load_condition": load_condition.text if load_condition is not None else None,
                "type": element.attrib["Type"],
                "name": name,
                "cook_preference": cook.text if cook is not None and cook.text is not None else "Always",
                "cook_explicit": cook is not None and cook.text is not None,
            }
        )
        if element.attrib.get("IgnoreDependenciesMlvl", "False").lower() != "false":
            parsed["ignore_dependencies_mlvl"] = True

        extras = {
            "Struct": self._prop_struct,
            "Asset": self._prop_asset,
            "Array": self._prop_array,
            "Enum": self._prop_choice,
            "Choice": self._prop_choice,
            "Flags": self._prop_flags,
        }.get(element.attrib["Type"])
        parsed.update(extras(element, path) if extras is not None else self._prop_default_value(element))
        return parsed

    def _parse_properties(self, properties: Element, path: Path) -> dict:
        elements = []
        if (sub_properties := properties.find("SubProperties")) is not None:
            for element in sub_properties:
                elements.append(self._parse_single_property(typing.cast("Element", element), path))
        return {
            "type": "Struct",
            "name": name.text if (name := properties.find("Name")) is not None else "",
            "atomic": properties.find("Atomic") is not None,
            "incomplete": properties.attrib.get("Incomplete") == "true",
            "properties": elements,
        }

    def _parse_choice(self, properties: Element, path: Path) -> dict:
        choices = {}
        if (values := properties.find("Values")) is None:
            return {}
        for element in values:
            element = typing.cast("Element", element)
            choices[element.attrib["Name"]] = int(element.attrib["ID"], 16)

        if (ele_name := properties.find("Name")) is not None:
            assert ele_name.text is not None
            name = ele_name.text
        elif (ele_id := properties.attrib.get("ID")) is not None:
            name = self.property_names.get(int(ele_id, 16), path.stem + ele_id)
        else:
            return {}

        if name == path.stem:
            name += "Enum"
        return {"enum_def": self._register_enum(name, "enum", choices, path)}

    def _parse_flags_archetype(self, archetype: Element, path: Path) -> dict:
        name = find_assured(archetype, "Name").text
        assert name is not None
        flags_element = archetype.find("Flags")
        flags = (
            {e.attrib["Name"]: int(e.attrib["Mask"], 16) for e in flags_element.findall("Element")}
            if flags_element is not None
            else {}
        )
        if flags:
            # Not added to the enum uses: it has no owner, so it's always a shared enum.
            self._register_enum(name, "flags", flags, None)
        default_value = self._prop_default_value(archetype)["default_value"]
        return {
            "type": "Flags",
            "flags": flags,
            "has_default": default_value is not None,
            "default_value": default_value,
        }

    def _parse_archetype_file(self, path: Path) -> dict:
        archetype = find_assured(ElementTree.parse(path).getroot(), "PropertyArchetype")
        _type = archetype.attrib["Type"]
        if _type == "Struct":
            return self._parse_properties(archetype, path)
        if _type in {"Choice", "Enum"}:
            return {"type": _type, **self._parse_choice(archetype, path)}
        if _type == "Flags":
            return self._parse_flags_archetype(archetype, path)
        raise ValueError(f"Unknown Archetype format: {_type}")

    # Resolving

    def _enum_names(self) -> dict[str, tuple]:
        """Enums by name, preferring the ones with a file of their own. Finds the enum that an archetype names."""
        result: dict[str, tuple] = {}
        for key, definition in self._enum_defs.items():
            name = scrub_enum(definition.name)
            if name not in result or not definition.owners:
                result[name] = key
        return result

    def _field_names_of(self, archetype: str) -> dict[int, str]:
        result = self._field_names.get(archetype)
        if result is None:
            result = self._field_names[archetype] = dict(self._class_field_names(self._archetypes[archetype]))
        return result

    def _class_field_names(self, raw_def: dict) -> typing.Iterator[tuple[int, str]]:
        names = [self._base_name(prop) for prop in raw_def["properties"]]
        for prop, name in zip(raw_def["properties"], names, strict=True):
            yield prop["id"], (f"{name}_0x{prop['id']:08x}" if names.count(name) > 1 else name)

    def _base_name(self, prop: dict) -> str:
        result = filter_property_name(prop["name"] or self.property_names.get(prop["id"]) or "unnamed")
        return result + "_" if result in RESERVED_FIELD_NAMES else result

    def _lookup_enum(self, prop: dict, suffix: str) -> GEnum | None:
        name = scrub_enum(prop["archetype"] or prop["name"] or self.property_names.get(prop["id"]) or "")
        by_name = self._enum_names()
        key = by_name.get(name) or by_name.get(name + suffix)
        return self._enum_defs[key] if key else None

    def resolve(self, prop: dict) -> tuple[Codec, Value | None]:  # noqa: PLR0911, PLR0912
        """The codec and the default (None if it's the one of the codec) of a parsed property."""
        raw_type = prop["type"]
        has_default = prop.get("has_default")
        default = prop.get("default_value")

        if raw_type == "Sound":
            return Codec("sound"), _py(repr(default if has_default else 0))

        if raw_type == "Struct":
            archetype: str = prop["archetype"].rsplit(".", maxsplit=1)[-1]
            overrides: list[tuple[str, Value]] = []
            names = self._field_names_of(prop["archetype"])
            cooks: list[tuple[str, str]] = []
            for inner in prop["properties"]:
                inner_name = names.get(inner["id"])
                if inner_name is None or inner_name == "unknown":
                    continue
                if inner["cook_explicit"] and self.game != Game.PRIME:
                    # The data omits these when equal to the default of the use site: `Default` there acts like this
                    cook = inner["cook_preference"]
                    cooks.append((inner_name, "OnlyIfModified" if cook == "Default" else cook))
                if not inner.get("has_default"):
                    continue
                target = next(p for p in self._archetypes[prop["archetype"]]["properties"] if p["id"] == inner["id"])
                _, inner_value = self.resolve({**target, "has_default": True, "default_value": inner["default_value"]})
                if inner_value is not None:
                    overrides.append((inner_name, inner_value))
            return Codec("struct", ref=archetype, defaults=tuple(overrides), cooks=tuple(cooks)), None

        if raw_type in ("Choice", "Enum"):
            default_value = default if has_default else 0
            definition = self._enum_defs.get(prop["enum_def"]) if prop.get("enum_def") else None
            if definition is None:
                definition = self._lookup_enum(prop, "Enum")
            if definition is not None and definition.kind == "enum" and default_value in definition.values.values():
                return Codec("enum_", ref=definition.key), Value(
                    "enum", ref=definition.key, raw=typing.cast("int", default_value)
                )
            return Codec("u32"), _py(repr(default_value))

        if raw_type == "Flags":
            default_int = default if has_default else 0
            if not has_default and "archetype" in prop:
                archetype_default = self._archetypes[prop["archetype"]]["default_value"]
                default_int = archetype_default if archetype_default is not None else 0
            definition = None
            if "flagset_name" in prop:
                if "archetype" in prop:
                    if self._archetypes[prop["archetype"]]["flags"]:
                        definition = self._lookup_enum({**prop, "archetype": prop["flagset_name"]}, "Flags")
                else:
                    definition = self._enum_defs[prop["enum_def"]]
            if definition is not None:
                return Codec("flags_", ref=definition.key), Value(
                    "flags", ref=definition.key, raw=typing.cast("int", default_int)
                )
            return Codec("u32"), _py(repr(default_int))

        if raw_type == "Asset":
            return Codec("asset", tuple(prop["type_filter"]), prop.get("ignore_dependencies_mlvl", False)), None

        if raw_type == "AnimationSet":
            return Codec("animation_parameters"), None
        if raw_type == "Spline":
            return Codec("spline"), None

        if raw_type == "Array":
            inner_codec, _ = self.resolve(prop["item_archetype"])
            return Codec("array", inner=inner_codec), None

        if raw_type == "String":
            return Codec("string"), _py(lit(default if has_default else ""))

        if raw_type == "Guid":
            return Codec("guid"), None

        if raw_type in ("Color", "Vector"):
            f32 = struct.Struct(">f")
            if not has_default:
                return Codec(raw_type.lower()), None
            assert default is not None
            rounded = {k: f32.unpack(f32.pack(v))[0] for k, v in default.items()}
            if not any(rounded.values()):
                return Codec(raw_type.lower()), None
            if raw_type == "Color":
                rounded = {"A": 0.0, **rounded}
                return Codec("color"), _py("Color({R!r}, {G!r}, {B!r}, {A!r})".format(**rounded), factory=True)
            return Codec("vector"), _py("Vector({X!r}, {Y!r}, {Z!r})".format(**rounded), factory=True)

        # Hack for LayerSwitch
        if prop["name"] == "Area ID" and raw_type == "Int":
            raw_type = "UInt"
        codec_name, fmt = _SCALARS[raw_type]
        zero = {"f": 0.0, "?": False}.get(fmt, 0)
        value = default if has_default else zero
        try:
            s = struct.Struct(">" + fmt)
            value = s.unpack(s.pack(value))[0]
        except struct.error as e:
            print(f"{hex(prop['id'])} ({prop['type']}) has invalid default value {value}: {e}")
            value = zero
        return Codec(codec_name), _py(repr(value))

    # Classes

    def _build_class(self, name: str, raw_def: dict, kind: str, object_type: str | int | None, path: Path) -> GClass:
        names = dict(self._class_field_names(raw_def))
        fields = []
        for prop in raw_def["properties"]:
            codec, default = self.resolve(prop)
            fields.append(
                GField(
                    game=self.game,
                    name=names[prop["id"]],
                    original_name=prop["name"] or self.property_names.get(prop["id"]),
                    locator=prop["id"],
                    codec=codec,
                    default=default,
                    cook=prop["cook_preference"] if self.game != Game.PRIME else "Always",
                    min_count=min_property_count(prop.get("load_condition")) if self.game == Game.PRIME else None,
                )
            )
        if self.game == Game.PRIME:
            ids = [f.locator for f in fields]
            assert ids == sorted(set(ids)), f"Prime positions of {name} are not increasing"
            for field_name, controller in PRIME_CONDITIONAL_PROPERTIES.get(name, {}).items():
                assert controller in names.values()
                next(f for f in fields if f.name == field_name).only_if = controller

        count_issue = (
            self._check_optional_properties(name, fields, raw_def["atomic"]) if self.game == Game.PRIME else None
        )
        result = GClass(
            self.game,
            name,
            kind,
            fields,
            count_issue=count_issue,
            atomic=raw_def["atomic"],
            incomplete=raw_def["incomplete"],
            modules=raw_def.get("modules"),
            object_type=object_type,
        )
        if self.game == Game.PRIME and kind != "struct":
            self._fold_editor_properties(result, path)
        return result

    @staticmethod
    def _check_optional_properties(name: str, fields: list[GField], atomic: bool) -> str | None:
        """
        Checks that the Prime properties with a count condition can be optional: they are the last ones, and the data
        has a property count that makes each of them present exactly when it is there. Otherwise they are made required
        again, and the reason is returned.
        """
        optional = [f for f in fields if f.min_count is not None]
        if not optional:
            return None
        reason = None
        required = len(fields) - len(optional)
        thresholds = [f.min_count for f in optional if f.min_count is not None]
        if name in PRIME_IRREGULAR_COUNTS:
            reason = "irregular count condition"
        elif atomic:
            reason = "atomic struct has no property count"
        elif fields[required:] != optional and name not in PRIME_REQUIRED_AFTER_OPTIONAL:
            reason = "optional properties are not the last ones"
        elif thresholds != sorted(thresholds):
            reason = "counts do not increase with the position"
        elif any(
            required + sum(1 for u in thresholds if u <= t) < t  # the count written would be too low to read it
            or required + sum(1 for u in thresholds if u < t) >= t  # the count written without it would read it
            for t in thresholds
        ):
            reason = "counts do not match the number of properties"
        if reason is None:
            return None
        for f in optional:
            f.min_count = None
        return reason

    def _fold_editor_properties(self, cls: GClass, path: Path) -> None:
        """Replaces the properties listed in the `<EditorProperties>` of a Prime template with one field."""
        block = ElementTree.parse(path).getroot().find("EditorProperties")
        if block is None:
            return

        def position(tag: str) -> int | None:
            element = block.find(tag)
            if element is None or element.text is None or ":" in element.text:
                return None  # not there, or inside a struct
            return int(element.text, 16)

        slot_positions = {
            "name": position("NameProperty"),
            "position": position("PositionProperty"),
            "rotation": position("RotationProperty"),
            "scale": position("ScaleProperty"),
            "active": position("ActiveProperty"),
        }
        expected = {"name": "string", "position": "vector", "rotation": "vector", "scale": "vector", "active": "bool_"}
        by_position = {f.locator: f for f in cls.fields}
        for slot_name, slot in list(slot_positions.items()):
            if slot is None:
                continue
            kind = by_position[slot].codec.kind
            assert by_position[slot].min_count is None, (cls.name, slot_name)
            assert kind == expected[slot_name], (cls.name, slot_name, kind)
        assert slot_positions["name"] is not None, cls.name

        removed = {p for p in slot_positions.values() if p is not None}
        cls.fields = [f for f in cls.fields if f.locator not in removed]
        spec = PrimeEditorSpec(
            slot_positions["name"],
            slot_positions["position"],
            slot_positions["rotation"],
            slot_positions["scale"],
            slot_positions["active"],
        )
        cls.fields.insert(
            0,
            GField(
                self.game, "editor_properties", "EditorProperties", spec, Codec("struct", ref="EditorProperties"), None
            ),
        )

    def parse(self) -> GameData:
        root = ElementTree.parse(self.templates_path / self.game_xml).getroot()

        def get_paths(element: Element) -> dict[str, str]:
            return {
                key: find_assured(item, "Value").attrib["Path"]
                for item in element
                if (key := find_assured(item, "Key").text) is not None
            }

        script_objects_paths = get_paths(find_assured(root, "ScriptObjects"))
        script_objects = {
            four_cc: self._parse_script_object(self.base_path / path) for four_cc, path in script_objects_paths.items()
        }
        archetype_paths = get_paths(find_assured(root, "PropertyArchetypes"))
        self._archetypes = {
            name: self._parse_archetype_file(self.base_path / path) for name, path in archetype_paths.items()
        }
        misc_element = root.find("MiscTemplates")
        misc_paths = get_paths(misc_element) if misc_element is not None else {}
        misc = {name: self._parse_script_object(self.base_path / path) for name, path in misc_paths.items()}
        self._assign_enum_keys()

        for four_cc, raw in script_objects.items():
            stem = Path(script_objects_paths[four_cc]).stem
            object_type: str | int = parse_int_text(four_cc, 16) if self.game == Game.PRIME else four_cc
            kind = "tweak" if Path(script_objects_paths[four_cc]).parts[0] == "Misc" else "object"
            previous = self.data.classes.get(stem)
            self.data.classes[stem] = self._build_class(
                stem, raw, kind, object_type, self.base_path / script_objects_paths[four_cc]
            )
            if previous is not None and previous.object_type is not None:
                # Two object types that use the same template: the last one is the main one, as it always was
                self.data.classes[stem].alias_object_types = [*previous.alias_object_types, previous.object_type]

        for name, raw in self._archetypes.items():
            if raw["type"] != "Struct":
                continue
            if name in self.data.classes:
                continue  # Already read as a script object
            self.data.classes[name] = self._build_class(
                name, raw, "struct", None, self.base_path / archetype_paths[name]
            )

        for name, raw in misc.items():
            if name in self.data.classes:
                continue  # Already read as a script object, which has an object type (e.g. SNFO)
            self.data.classes[name] = self._build_class(name, raw, "tweak", None, self.base_path / misc_paths[name])

        self._add_states(root)
        return self.data

    def _parse_script_object(self, path: Path) -> dict:
        root = ElementTree.parse(path).getroot()
        result = self._parse_properties(find_assured(root, "Properties"), path)
        if (modules := root.find("Modules")) is not None:
            result["modules"] = [item.text for item in modules.findall("Element")]
        return result

    def _assign_enum_keys(self) -> None:
        # An enum defined by exactly one template is local to its class. The rest (the ones with a file of their own,
        # or defined more than once) are shared.
        for definition in self._enum_defs.values():
            if len(definition.owners) == 1:
                definition.key = ("local", definition.owners[0], scrub_enum(definition.name))
            else:
                definition.key = ("shared", scrub_enum(definition.name))
        for definition in self._enum_defs.values():
            self.data.enums.setdefault(definition.key, definition)

    def _add_states(self, root: Element) -> None:
        for tag, name in (("States", "State"), ("Messages", "Message")):
            mapping = {
                find_assured(item, "Value").text or "": find_assured(item, "Key").text or ""
                for item in find_assured(root, tag)
            }
            if self.game == Game.PRIME:
                values: dict[str, typing.Any] = {k: parse_int_text(v, 16) for k, v in mapping.items()}
            else:
                values = dict(mapping)
            definition = GEnum(self.game, name, "enum", values, key=("shared", name), base="Enum")
            self.data.enums[definition.key] = definition
