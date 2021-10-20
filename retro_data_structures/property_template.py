import enum
from pathlib import Path
from typing import Dict

from construct.core import (
    Adapter,
    Check,
    Compressed,
    Computed,
    Const,
    Default,
    Enum,
    Flag,
    Float32b,
    FocusedSeq,
    GreedyBytes,
    Hex,
    If,
    IfThenElse,
    Int16ub,
    Int32sb,
    Int32ub,
    LazyBound,
    Optional,
    Pass,
    Peek,
    Prefixed,
    PrefixedArray,
    Rebuild,
    Struct,
    Subconstruct,
    Switch,
    VarInt,
    this,
)
from construct.lib.containers import Container, ListContainer

import retro_data_structures.enums.corruption
import retro_data_structures.enums.echoes
import retro_data_structures.enums.prime
from retro_data_structures.common_types import FourCC, String
from retro_data_structures.construct_extensions.dict import DictAdapter, DictStruct
from retro_data_structures.construct_extensions.misc import ErrorWithMessage, LabeledOptional
from retro_data_structures.game_check import AssetIdCorrect, Game

Proportion = FocusedSeq("value", "value" / Float32b, Check(lambda t: 0.0 <= t.value <= 1.0))


class PropertyTypes(enum.IntEnum):
    Int = enum.auto()
    Bool = enum.auto()
    Float = enum.auto()
    String = enum.auto()
    Short = enum.auto()

    Asset = enum.auto()
    Choice = enum.auto()
    Struct = enum.auto()
    Flags = enum.auto()
    Array = enum.auto()

    Color = enum.auto()
    Vector = enum.auto()

    AnimationSet = enum.auto()
    Spline = enum.auto()
    Sound = enum.auto()

    Enum = enum.auto()

class CookPreference(enum.IntEnum):
    Always = enum.auto()
    OnlyIfModified = enum.auto()
    Default = enum.auto()
    Never = enum.auto()

PropertyTypeEnum = Enum(VarInt, PropertyTypes)


def TypeSwitch(cases, default=None):
    return FocusedSeq(
        "result",
        "type" / Peek(PropertyTypeEnum),
        "result" / Switch(lambda this: this.type or this.result["type"], cases, default),
    )


def PropertyDef(*extra_fields, include_id=True):
    id_field = ["id" / LabeledOptional(b"ID", Hex(Int32ub))] if include_id else []
    return Struct(
        "type" / PropertyTypeEnum,
        "name" / String,
        "cook_preference" / Enum(VarInt, CookPreference),
        *id_field,
        *extra_fields
    )


PropertySubcons = {
    "Int": Int32ub,
    "Bool": Flag,
    "Float": Float32b,
    "String": String,
    "Short": Int16ub,
    "Asset": AssetIdCorrect,
    "Choice": Int32ub,
    # Struct
    "Flags": Int32ub,
    # Array
    "Color": Struct("R" / Proportion, "G" / Proportion, "B" / Proportion, "A" / Default(Proportion, 1.0)),
    "Vector": Struct("X" / Float32b, "Y" / Float32b, "Z" / Float32b),
    "AnimationSet": Struct("AnimationCharacterSet" / AssetIdCorrect, "Character" / Int32ub, "DefaultAnim" / Int32ub),
    # TODO: Spline
    "Sound": Hex(Int32ub),
    "Enum": Int32ub,
}

PropertyDefaults = {
    "Int": 0,
    "Bool": False,
    "Float": 0.0,
    "String": "",
    "Short": 0,
    "Asset": 0,
    "Choice": 0,
    "Struct": Container(),
    "Flags": 0,
    "Array": ListContainer(),
    "Color": Container({"R": 1.0, "G": 1.0, "B": 1.0}),
    "Vector": Container({"X": 0.0, "Y": 0.0, "Z": 0.0}),
    "AnimationSet": Container({"AnimationCharacterSet": 0, "Character": 0, "DefaultAnim": 0}),
    "Spline": b'', # FIXME
    "Sound": 0,
    "Enum": 0,
}


def Property(include_id=True):
    default_value_field = [
        "has_default" / Flag,
        "default_value" / If(this.has_default, Switch(this.type, PropertySubcons, Prefixed(VarInt, GreedyBytes)))
    ]
    enum_property = PropertyDef(
        "archetype" / LabeledOptional(b"AR", String), *default_value_field, include_id=include_id
    )
    return TypeSwitch(
        {
            "Struct": PropertyDef(
                "archetype" / LabeledOptional(b"AR", String),
                "properties" / PrefixedArray(VarInt, LazyBound(lambda: Property(include_id))),
                include_id=include_id,
            ),
            "Asset": PropertyDef("type_filter" / PrefixedArray(VarInt, FourCC), include_id=include_id),
            "Array": PropertyDef("item_archetype" / LazyBound(lambda: Property(False)), include_id=include_id),
            "Choice": enum_property,
            "Enum": enum_property,
        },
        PropertyDef(*default_value_field),
    )


ScriptObjectTemplate = DictStruct(
    "type" / Const("Struct", PropertyTypeEnum),
    "atomic" / Default(Flag, False),
    "properties" / PrefixedArray(VarInt, Property()),
    "name" / String,
)

PropertyArchetype = TypeSwitch(
    {
        "Struct": ScriptObjectTemplate,
        "Choice": DictStruct("type" / Const("Choice", PropertyTypeEnum)),
        "Enum": DictStruct("type" / Const("Enum", PropertyTypeEnum)),
    },
    ErrorWithMessage(f"Unknown Archetype format: {this.type or this.archetype['type']}"),
)

GameTemplate = Prefixed(
    VarInt,
    Compressed(
        Struct(
            "script_objects" / DictAdapter(ScriptObjectTemplate), "property_archetypes" / DictAdapter(PropertyArchetype)
        ),
        "zlib",
    ),
)

ListGameTemplate = DictStruct(
    "script_objects" / DictAdapter(ScriptObjectTemplate), "property_archetypes" / DictAdapter(PropertyArchetype)
)

GameList = DictAdapter(ListGameTemplate)

PropertyNames = Prefixed(VarInt, Compressed(DictAdapter(String, objisdict=False), "zlib"))

_game_template_cache = {}


def GetGameTemplate(game: Game):
    prop_path = Path(__file__).parent.joinpath("properties")

    game_id = {Game.PRIME: "Prime", Game.ECHOES: "Echoes", Game.CORRUPTION: "Corruption"}[game]

    if not game_id in _game_template_cache.keys():
        _game_template_cache[game_id] = GameTemplate.parse_file(prop_path / (game_id + ".prop"))

    return _game_template_cache[game_id]


_property_names_cache = {}


def GetPropertyName(game_id: Game, prop_id):
    if game_id < Game.ECHOES:
        return ""

    global _property_names_cache

    prop_path = Path(__file__).parent.joinpath("properties")
    if not _property_names_cache:
        _property_names_cache = PropertyNames.parse_file(prop_path / "property_names.pname")
    return _property_names_cache.get(prop_id, "")


PropertyConstructs: Dict[Game, Dict[str, Subconstruct]] = {}

_ENUMS_BY_GAME = {
    Game.PRIME: retro_data_structures.enums.prime,
    Game.ECHOES: retro_data_structures.enums.echoes,
    Game.CORRUPTION: retro_data_structures.enums.corruption,
}


class OnlyIfModified(Adapter):
    def __init__(self, subcon, default):
        super().__init__(Optional(subcon))
        self.default = default
    
    def _decode(self, obj, context, path):
        return obj if obj else self.default
    
    def _encode(self, obj, context, path):
        return None if obj == self.default else obj


def CreatePropertyConstructs(game_id: Game):
    enums = _ENUMS_BY_GAME[game_id]
    game_template = GetGameTemplate(game_id)

    archetypes = Container()
    default_archetypes = Container()

    def get_subcon(prop, atomic=False, default=False):
        if prop.type == "Struct":
            archetype = game_template.property_archetypes.get(prop.archetype, Container({"properties": ListContainer()}))
            prop_id = prop.id if not atomic else None
            if not prop.properties:
                # no changes to defaults or cook preferences
                add_archetype(prop.archetype, archetype)
                arch = default_archetypes[prop.archetype] if default else archetypes[prop.archetype]
                return arch(prop_id)
            else:
                properties = {p.id: p for p in archetype.properties.copy()}
                properties.update({p.id: p for p in prop.properties})
                return property_struct(properties.values(), atomic, default)(prop_id)

        if prop.type == "Array":
            data = PrefixedArray(Int32ub, get_subcon(prop.item_archetype, True, default))
        elif (
                hasattr(prop, "archetype")
                and prop.archetype is not None
                and (prop.type == "Choice" or prop.type == "Enum")
        ):
            data = Enum(Int32ub, getattr(enums, prop.archetype))
        else:
            data = PropertySubcons.get(prop.type, GreedyBytes)

        if not atomic and game_id >= Game.ECHOES:
            data = FocusedSeq(
                "data",
                "id" / Const(prop.id, Hex(Int32ub)),
                "data" / Prefixed(Int16ub if game_id >= Game.ECHOES else Int32ub, data),
            )
        
        if default:
            default_value = prop.get("default_value") or PropertyDefaults[prop.type]
            data = Default(data, default_value)

        if prop.cook_preference == "Always":
            pass # default behavior
        elif prop.cook_preference == "OnlyIfModified":
            data = OnlyIfModified(data, prop.default_value)
        elif prop.cook_preference == "Never":
            data = Pass
        elif prop.cook_preference == "Default":
            data = Const(prop.default_value, data)

        return data

    def get_property_name(prop, names):
        name = names.get(prop.id) or prop.name
        occurences = len([n for n in names.values() if n == name])
        if not name or occurences > 1:
            name += f"0x{prop.id:X}"
        return name

    def rebuild_count(props, names):
        fixed_count = len([prop for prop in props if prop.cook_preference == "Always" or prop.cook_preference == "Default"])
        optionals = [get_property_name(prop, names) for prop in props if prop.cook_preference == "OnlyIfModified"]
        def _(context):
            optional_count = len([name for name in optionals if context.get(name) is not None])
            return fixed_count + optional_count
        return _
    
    def property_struct(_properties, atomic, default, *extra_fields):
        def result(property_id=None):
            prefix = Int16ub if game_id >= Game.ECHOES else Int32ub
            
            property_names = {prop.id: GetPropertyName(game_id, prop.id) for prop in _properties}
            properties = Container({get_property_name(prop, property_names): get_subcon(prop, atomic, default) for prop in _properties})
            
            id_field = []
            count_field = ["_prop_count" / Rebuild(prefix, rebuild_count(_properties, property_names))] if not atomic else []
            data = Struct(*extra_fields, *count_field, **properties)

            if game_id >= Game.ECHOES:
                id_field = ["id" / If(lambda this: not (atomic and hasattr(this._, "count")), Const(property_id, Hex(Int32ub)))]
                data = IfThenElse(lambda this: not (atomic and hasattr(this._, "count")), Prefixed(prefix, data), data)
            
            if default:
                data = Default(data, {})

            return Default(FocusedSeq(
                "data",
                *id_field,
                "data" / data,
            ), {})
        return result

    def add_archetype(name, archetype):
        if name in archetypes.keys():
            return
        if archetype.type == "Choice" or archetype.type == "Enum":
            return
        default_archetypes[name] = property_struct(archetype.properties, archetype.atomic, True)
        archetypes[name] = property_struct(archetype.properties, archetype.atomic, False)

    for arch_name, archetype in game_template.property_archetypes.items():
        add_archetype(arch_name, archetype)

    script_objects = {}
    script_objects_default = {}

    for script_name, obj in game_template.script_objects.items():
        script_objects[script_name] = property_struct(obj.properties, False, False, "_name" / Computed(obj.name))(0xFFFFFFFF)
        script_objects_default[script_name] = property_struct(obj.properties, False, True, "_name" / Computed(obj.name))(0xFFFFFFFF)

    PropertyConstructs[game_id] = {"standard": script_objects, "default": script_objects_default}


def GetPropertyConstruct(game: Game, obj_type: str, default: bool = False) -> Subconstruct:
    if game not in PropertyConstructs:
        CreatePropertyConstructs(game)

    return PropertyConstructs[game]["default" if default else "standard"].get(obj_type, GreedyBytes)
