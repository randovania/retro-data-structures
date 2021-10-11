import enum
from pathlib import Path
from construct.core import Check, Compressed, Default, Flag, Float32b, GreedyBytes, Hex, IfThenElse, Int16ub, Int32ub, LazyBound, Prefixed, this, Adapter, Const, Enum, Error, FocusedSeq, Peek, PrefixedArray, Struct, Switch, VarInt
from retro_data_structures.common_types import FourCC, String
from retro_data_structures.construct_extensions import DictStruct, DictAdapter, ErrorWithMessage, LabeledOptional

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
    return Struct(
        "type" / PropertyTypeEnum,
        "id" / IfThenElse(include_id, Hex(Int32ub), Const(b'')),
        *extra_fields
    )

def Property(include_id=True):
    default_value_types = {
        "Int": Int32ub,
        "Float": Float32b,
        "Bool": Flag,
        "Short": Int16ub,
        "Color": Struct("R" / Proportion, "G" / Proportion, "B" / Proportion, "A" / Default(Proportion, 1.0)),
        "Vector": Struct("X" / Float32b, "Y" / Float32b, "Z" / Float32b),
        "Flags": Int32ub,
        "Choice": VarInt,
        "Enum": Int32ub
    }
    default_value_field = [
        "default_value" / LabeledOptional(b'DV', Switch(this.type, default_value_types, Prefixed(VarInt, GreedyBytes)))
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
                "properties" / PrefixedArray(VarInt, LazyBound(lambda: Property())),
                include_id=include_id
            ),
            "Asset": PropertyDef(
                "type_filter" / PrefixedArray(VarInt, FourCC),
                include_id=include_id
            ),
            "Array": PropertyDef(
                "item_archetype" / LabeledOptional(b'IA', LazyBound(lambda: Property(False))),
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
    "properties" / PrefixedArray(VarInt, Property())
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
