import enum
from pathlib import Path
import construct
from construct.core import Check, Compressed, Computed, Default, FixedSized, Flag, Float32b, GreedyBytes, Hex, If, IfThenElse, Int16ub, Int32ub, LazyBound, Prefixed, Subconstruct, this, Adapter, Const, Enum, Error, FocusedSeq, Peek, PrefixedArray, Struct, Switch, VarInt
from construct.lib.containers import Container
from retro_data_structures import game_check
from retro_data_structures.common_types import AssetId32, AssetId64, FourCC, String
from retro_data_structures.construct_extensions import DictStruct, DictAdapter, ErrorWithMessage, LabeledOptional
from retro_data_structures.game_check import AssetIdCorrect, Game, get_current_game

Proportion = FocusedSeq(
    "value",
    "value" / Float32b,
    Check(lambda this: this.value >= 0.0 and this.value <= 1.0)
)

class PropertyTypes(enum.IntEnum):
    Int=enum.auto()
    Bool=enum.auto()
    Float=enum.auto()
    String=enum.auto()
    Short=enum.auto()

    Asset=enum.auto()
    Choice=enum.auto()
    Struct=enum.auto()
    Flags=enum.auto()
    Array=enum.auto()
    
    Color=enum.auto()
    Vector=enum.auto()

    AnimationSet=enum.auto()
    Spline=enum.auto()
    AnimParams=enum.auto()
    Collision=enum.auto()
    Billboard=enum.auto()
    Sound=enum.auto()
    Model=enum.auto()

    Enum=enum.auto()

PropertyTypeEnum = Enum(VarInt, PropertyTypes)

def TypeSwitch(cases, default=None):
    return FocusedSeq(
        "result",
        "type" / Peek(PropertyTypeEnum),
        "result" / Switch(lambda this: this.type or this.result["type"], cases, default)
    )

def PropertyDef(*extra_fields, include_id=True):
    id_field = ["id" / LabeledOptional(b'ID', Hex(Int32ub))] if include_id else []
    return Struct(
        "type" / PropertyTypeEnum,
        "name" / String,
        *id_field,
        *extra_fields
    )

PropertySubcons = {
    "Int": Int32ub,
    "Float": Float32b,
    "Bool": Flag,
    "Short": Int16ub,
    "Color": Struct("R" / Proportion, "G" / Proportion, "B" / Proportion, "A" / Default(Proportion, 1.0)),
    "Vector": Struct("X" / Float32b, "Y" / Float32b, "Z" / Float32b),
    "Flags": Int32ub,
    "Choice": Int32ub,
    "Enum": Int32ub,
    "String": String,
}

def Property(include_id=True):
    default_value_field = [
        "default_value" / LabeledOptional(b'DV', Switch(this.type, PropertySubcons, Prefixed(VarInt, GreedyBytes)))
    ]
    enum_property = PropertyDef(
        "archetype" / LabeledOptional(b'AR', String),
        *default_value_field,
        include_id=include_id
    )
    return TypeSwitch(
        {
            "Struct": PropertyDef(
                "archetype" / LabeledOptional(b'AR', String),
                "properties" / PrefixedArray(VarInt, LazyBound(lambda: Property(include_id))),
                include_id=include_id
            ),
            "Asset": PropertyDef(
                "type_filter" / PrefixedArray(VarInt, FourCC),
                include_id=include_id
            ),
            "Array": PropertyDef(
                "item_archetype" / LazyBound(lambda: Property(False)),
                include_id=include_id
            ),
            "Choice": enum_property,
            "Enum": enum_property
        },
        PropertyDef(
            *default_value_field
        )
    )

ScriptObjectTemplate = DictStruct(
    "type" / Const("Struct", PropertyTypeEnum),
    "atomic" / Default(Flag, False),
    "properties" / PrefixedArray(VarInt, Property()),
    "name" / String
)

PropertyArchetype = TypeSwitch(
    {
        "Struct": ScriptObjectTemplate,
        "Choice": DictStruct("type" / Const("Choice", PropertyTypeEnum)),
        "Enum": DictStruct("type" / Const("Enum", PropertyTypeEnum))
    },
    ErrorWithMessage(f"Unknown Archetype format: {this.type or this.archetype['type']}")
)

GameTemplate = Prefixed(VarInt, Compressed(Struct(
    "script_objects" /  DictAdapter(ScriptObjectTemplate),
    "property_archetypes" / DictAdapter(PropertyArchetype)
), "zlib"))

ListGameTemplate = DictStruct(
    "script_objects" /  DictAdapter(ScriptObjectTemplate),
    "property_archetypes" / DictAdapter(PropertyArchetype)
)

GameList = DictAdapter(ListGameTemplate)

PropertyNames = Prefixed(VarInt, Compressed(
    DictAdapter(String, objisdict=False),
    "zlib"
))

_game_template_cache = {}
def GetGameTemplate(game: Game):
    prop_path = Path(__file__).parent.joinpath("properties")

    game_id = {Game.PRIME: "Prime", Game.ECHOES: "Echoes", Game.CORRUPTION: "Corruption"}[game]

    if not game_id in _game_template_cache.keys():
        _game_template_cache[game_id] = GameTemplate.parse_file(prop_path / (game_id + ".prop"))

    return _game_template_cache[game_id]

_property_names_cache = {}
def GetPropertyName(prop_id):
    global _property_names_cache
    prop_path = prop_path = Path(__file__).parent.joinpath("properties")
    if not _property_names_cache:
        _property_names_cache = PropertyNames.parse_file(prop_path / "property_names.pname")
    return _property_names_cache.get(prop_id, "")

PropertyConstructs = Container()
def CreatePropertyConstructs(games=[Game.PRIME, Game.ECHOES, Game.CORRUPTION]):
    for game_id in games:
        game_template = GetGameTemplate(game_id)

        archetypes = Container()
        
        def get_subcon(prop, atomic=False):
            if prop.type == "Struct":
                archetype = game_template.property_archetypes[prop.archetype]
                add_archetype(prop.archetype, archetype)
                return archetypes[prop.archetype]
            
            if prop.type == "Array":
                data = PrefixedArray(Int32ub, get_subcon(prop.item_archetype, True))
            elif prop.type == "Asset":
                data = AssetId32 if game_id.uses_asset_id_32 else AssetId64
            else:
                data = PropertySubcons.get(prop.type, GreedyBytes)
            
            if atomic:
                return data
            return Struct(
                "id" / Hex(Int32ub),
                "data" / Prefixed(Int16ub if game_id >= Game.ECHOES else Int32ub, data),
            )
        
        def get_property_name(prop, names):
            name = names[prop.id] or prop.name
            occurences = len([n for n in names.values() if n == name])
            if not name or occurences > 1:
                name += f'0x{prop.id:X}'
            return name

        def add_archetype(name, archetype):
            if name in archetypes.keys():
                return
            if archetype.type == "Choice" or archetype.type == "Enum":
                return
            names = {prop.id: GetPropertyName(prop.id) for prop in archetype.properties}
            properties = Container({get_property_name(prop, names): get_subcon(prop) for prop in archetype.properties})
            atomic_properties = Container({get_property_name(prop, names): get_subcon(prop, True) for prop in archetype.properties})
            prefix = Int16ub if game_id >= Game.ECHOES else Int32ub
            if archetype.atomic:
                archetypes[name] = Struct(
                    "id" / If(lambda this: not hasattr(this._, "count"), Hex(Int32ub)),
                    "data" / IfThenElse(
                        lambda this: not hasattr(this._, "count"),
                        Prefixed(prefix, Struct(**atomic_properties)),
                        Struct(**atomic_properties)
                    ),
                )
            else:
                archetypes[name] = Struct(
                    "id" / Hex(Int32ub),
                    "data" / Prefixed(prefix, Struct(
                        "prop_count" / Const(len(properties), prefix),
                        **properties
                    )),
                )

        for name, archetype in game_template.property_archetypes.items():
            add_archetype(name, archetype)

        script_objects = Container()

        for name, obj in game_template.script_objects.items():
            names = {prop.id: GetPropertyName(prop.id) for prop in obj.properties}
            properties = Container({get_property_name(prop, names): get_subcon(prop) for prop in obj.properties})
            prefix = Int16ub if game_id >= Game.ECHOES else Int32ub
            script_objects[name] = Struct(
                "name" / Computed(obj.name),
                "id" / Const(0xFFFFFFFF, Hex(Int32ub)),
                "data" / Prefixed(prefix, Struct(
                    "prop_count" / Const(len(properties), prefix),
                    **properties
                ))
            )

        PropertyConstructs[game_id] = script_objects

def GetPropertyConstruct(game, obj_id) -> Subconstruct:
    if not game in PropertyConstructs:
        CreatePropertyConstructs([game])
    return PropertyConstructs[game].get(obj_id, GreedyBytes)
