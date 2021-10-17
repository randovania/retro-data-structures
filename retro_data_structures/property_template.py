import enum
from pathlib import Path
from typing import Dict

from construct.core import (
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
    Int32ub,
    LazyBound,
    Peek,
    Prefixed,
    PrefixedArray,
    Struct,
    Subconstruct,
    Switch,
    VarInt,
    this,
)
from construct.lib.containers import Container

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


PropertyTypeEnum = Enum(VarInt, PropertyTypes)


def TypeSwitch(cases, default=None):
    return FocusedSeq(
        "result",
        "type" / Peek(PropertyTypeEnum),
        "result" / Switch(lambda this: this.type or this.result["type"], cases, default),
    )


def PropertyDef(*extra_fields, include_id=True):
    id_field = ["id" / LabeledOptional(b"ID", Hex(Int32ub))] if include_id else []
    return Struct("type" / PropertyTypeEnum, "name" / String, *id_field, *extra_fields)


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


def Property(include_id=True):
    default_value_field = [
        "default_value" / LabeledOptional(b"DV", Switch(this.type, PropertySubcons, Prefixed(VarInt, GreedyBytes)))
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


def CreatePropertyConstructs(game_id: Game):
    enums = _ENUMS_BY_GAME[game_id]
    game_template = GetGameTemplate(game_id)

    archetypes = Container()

    def get_subcon(prop, atomic=False):
        if prop.type == "Struct":
            add_archetype(prop.archetype, game_template.property_archetypes[prop.archetype])
            return archetypes[prop.archetype]

        if prop.type == "Array":
            data = PrefixedArray(Int32ub, get_subcon(prop.item_archetype, True))
        elif (
                hasattr(prop, "archetype")
                and prop.archetype is not None
                and (prop.type == "Choice" or prop.type == "Enum")
        ):
            data = Enum(Int32ub, getattr(enums, prop.archetype))
        else:
            data = PropertySubcons.get(prop.type, GreedyBytes)

        if atomic or game_id < Game.ECHOES:
            return data
        return Struct(
            "id" / Hex(Int32ub),
            "data" / Prefixed(Int16ub if game_id >= Game.ECHOES else Int32ub, data),
        )

    def get_property_name(prop, names):
        name = names.get(prop.id) or prop.name
        occurences = len([n for n in names.values() if n == name])
        if not name or occurences > 1:
            name += f"0x{prop.id:X}"
        return name

    def property_struct(properties, atomic):
        prefix = Int16ub if game_id >= Game.ECHOES else Int32ub

        id_field = []
        count_field = ["prop_count" / Const(len(properties), prefix)] if not atomic else []
        data = Struct(*count_field, **properties)

        if game_id >= Game.ECHOES:
            id_field = ["id" / If(lambda this: not (atomic and hasattr(this._, "count")), Hex(Int32ub))]
            data = IfThenElse(lambda this: not (atomic and hasattr(this._, "count")), Prefixed(prefix, data), data)

        return [
            *id_field,
            "data" / data,
        ]  # , Computed(lambda this: print(this.data) if game_check.is_prime1(this) else None)]

    def add_archetype(name, archetype):
        if name in archetypes.keys():
            return
        if archetype.type == "Choice" or archetype.type == "Enum":
            return
        names = {prop.id: GetPropertyName(game_id, prop.id) for prop in archetype.properties}
        properties = Container(
            {get_property_name(prop, names): get_subcon(prop, archetype.atomic) for prop in archetype.properties}
        )

        archetypes[name] = Struct(*property_struct(properties, archetype.atomic))

    for arch_name, archetype in game_template.property_archetypes.items():
        add_archetype(arch_name, archetype)

    script_objects = {}

    for script_name, obj in game_template.script_objects.items():
        property_names = {prop.id: GetPropertyName(game_id, prop.id) for prop in obj.properties}
        properties = Container({get_property_name(prop, property_names): get_subcon(prop) for prop in obj.properties})

        script_objects[script_name] = Struct("name" / Computed(obj.name), *property_struct(properties, False))

    PropertyConstructs[game_id] = script_objects


def GetPropertyConstruct(game: Game, obj_type: str) -> Subconstruct:
    if game not in PropertyConstructs:
        CreatePropertyConstructs(game)

    return PropertyConstructs[game].get(obj_type, GreedyBytes)
