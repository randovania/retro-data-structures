from __future__ import annotations

import collections.abc
import enum
import typing

import construct

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, FourCC
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.construct_extensions.misc import ErrorWithMessage

if typing.TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

    from retro_data_structures.game_check import Game


class ComparisonOperator(enum.IntEnum):
    LessThan = 0
    LessThanOrEqualTo = 1
    EqualTo = 2
    GreaterThanOrEqualTo = 3
    GreaterThan = 4


class ValueType(enum.IntEnum):
    Bool = 0
    Float = 1
    Int32 = 2


class ActionId(enum.StrEnum):
    """
    The FourCC of a rule action. Which actions are understood depends on who evaluates the RULE:
    the knockback rules or the pickup generator rules. Any other id is ignored by that evaluator.
    """

    # Unused by the code. Retail rules use it as an action that matches nothing in the pickup generator.
    NONE = "NONE"

    # Knockback: reaction (kAR_*)
    FLINCH = "FLCH"
    KNOCK_BACK = "HHIT"
    HURLED = "HURL"
    FALL = "DIMP"

    # Knockback: follow-up (kFU_*)
    FREEZE = "FRZN"  # duration: float
    SHOCK = "ELEC"  # duration: float
    BURN = "BURN"  # duration: float
    SLOW = "SLOW"  # duration: float, secondary duration: float
    BURN_PHASE = "BRNP"  # duration: float, secondary duration: float
    DEATH = "DETH"
    EXPLODE_DEATH = "GIBB"
    ICE_DEATH = "ICGB"
    BURN_DEATH = "ASHH"
    LAGGED_BURN_DEATH = "DSGT"
    BLACK_DEATH = "BLKD"
    IMMEDIATE_EXPLOSION = "IMEX"  # duration: float
    IMMEDIATE_DISINTEGRATION = "IMDS"

    # Knockback: reaction flags (names are guesses from the AI code consuming them)
    BREAK_FREEZE = "UNFZ"  # 1
    DOUSE_FIRE = "STFR"  # 2
    STOP_ELECTROCUTION = "STEC"  # 4
    BREAK_ORBIT = "BRKL"  # 8
    DISABLE_PHYSICS = "NPKB"  # 16
    RESET_TIME_SCALE = "STSL"  # 32
    SKIP_FALL_ROTATION = "IRTN"  # 64

    # Pickup generator: chance (percent, float), minimum amount (int, default 1), maximum amount (int, default 0).
    # The slot a pickup template uses is picked by its item and amount (CScriptPickupGenerator::GetSpawnablePickups).
    SMALL_MISSILE = "SLMS"  # amount <= 5
    BIG_MISSILE = "BGMS"  # amount > 5
    HEALTH_10 = "SLHL"  # anything but 30, 50 and 100
    HEALTH_30 = "BGHL"
    HEALTH_50 = "MGHL"
    HEALTH_100 = "GGHL"
    POWER_BOMB = "PBMB"
    LIGHT_AMMO_10 = "LTAM"
    DARK_AMMO_10 = "DKAM"
    LIGHT_AMMO_SMALL = "LTAx"  # amount < 10
    DARK_AMMO_SMALL = "DKAx"
    LIGHT_AMMO_LARGE = "LTAX"  # amount > 10
    DARK_AMMO_LARGE = "DKAX"
    LIGHT_BEAM = "LTBM"
    DARK_BEAM = "DKBM"
    ANNIHILATOR_BEAM = "ANBM"


_FLOAT = ValueType.Float
_INT = ValueType.Int32

# The type of each property by position. Rule files only store 32 bits for each; the evaluator picks how to read
# them (CRuleValue::GetFloat/GetInt/GetBool). Properties past the end of the list are raw (unsigned) 32-bit integers.
ACTION_PROPERTY_TYPES: dict[str, tuple[ValueType, ...]] = {
    **dict.fromkeys(
        (
            ActionId.FREEZE,
            ActionId.SHOCK,
            ActionId.BURN,
            ActionId.IMMEDIATE_EXPLOSION,
        ),
        (_FLOAT,),
    ),
    **dict.fromkeys((ActionId.SLOW, ActionId.BURN_PHASE), (_FLOAT, _FLOAT)),
    **dict.fromkeys(
        (
            ActionId.SMALL_MISSILE,
            ActionId.BIG_MISSILE,
            ActionId.HEALTH_10,
            ActionId.HEALTH_30,
            ActionId.HEALTH_50,
            ActionId.HEALTH_100,
            ActionId.POWER_BOMB,
            ActionId.LIGHT_AMMO_10,
            ActionId.DARK_AMMO_10,
            ActionId.LIGHT_AMMO_SMALL,
            ActionId.DARK_AMMO_SMALL,
            ActionId.LIGHT_AMMO_LARGE,
            ActionId.DARK_AMMO_LARGE,
            ActionId.LIGHT_BEAM,
            ActionId.DARK_BEAM,
            ActionId.ANNIHILATOR_BEAM,
        ),
        (_FLOAT, _INT, _INT),
    ),
}


class _FourCCEnumAdapter(construct.Adapter):
    """Reads a FourCC as an enum member when there is one, or as the plain string when there isn't."""

    def __init__(self, enum_class: type[enum.StrEnum]):
        super().__init__(FourCC)
        self._enum_class = enum_class

    def _decode(self, obj: str, context: construct.Container, path: str) -> enum.StrEnum | str:
        try:
            return self._enum_class(obj)
        except ValueError:
            return obj

    def _encode(self, obj: enum.StrEnum | str, context: construct.Container, path: str) -> str:
        return str(obj.value if isinstance(obj, enum.Enum) else obj)


def _property_type(context: construct.Container) -> ValueType | None:
    """The type of the property being read/written: `_index` is the position, `id` is of the action."""
    index = context._index
    while "id" not in context:
        context = context._
    types = ACTION_PROPERTY_TYPES.get(context.id, ())
    return types[index] if index < len(types) else None


_ActionProperty = construct.Switch(
    _property_type,
    {
        ValueType.Float: construct.Float32b,
        ValueType.Int32: construct.Int32sb,
    },
    default=construct.Int32ub,
)

RuleCondition = construct.Struct(
    id=FourCC,
    operator=EnumAdapter(ComparisonOperator, construct.Int8ub),
    value_type=EnumAdapter(ValueType, construct.Int8ub),
    value=construct.Switch(
        construct.this.value_type,
        {
            # The evaluator ignores operator and value for conditions that are bools, as these are just true/false.
            ValueType.Bool: construct.Int32ub,
            ValueType.Float: construct.Float32b,
            ValueType.Int32: construct.Int32sb,
        },
        default=ErrorWithMessage(lambda ctx: f"Unknown type: {ctx.value_type}"),
    ),
)

Action = construct.Struct(
    id=_FourCCEnumAdapter(ActionId),
    properties=construct.PrefixedArray(construct.Int8ub, _ActionProperty),
)

RuleSetRule = construct.Struct(
    conditions=construct.PrefixedArray(construct.Int16ub, RuleCondition),
    actions=construct.PrefixedArray(construct.Int16ub, Action),
)

RULE = construct.Struct(
    magic=construct.Const(b"RULE"),
    version=construct.Const(1, construct.Int8ub),
    parent_rule=AssetId32,
    rules=construct.PrefixedArray(
        construct.Int16ub,
        RuleSetRule,
    ),
    _align=AlignTo(32, b"\xff"),
    end=construct.Terminated,
)

PropertyValue = float | int
ConditionValue = bool | float | int


class RuleConditionView:
    """A condition of a rule. Wraps the parsed data, so changes apply to the RuleSet."""

    def __init__(self, raw: construct.Container):
        self._raw = raw

    def __repr__(self) -> str:
        return f"<Condition {self.id} {self.operator.name} {self.value!r}>"

    @property
    def id(self) -> str:
        """FourCC of the value the evaluator checks, such as `PHLT` for the player's health percentage."""
        return self._raw.id

    @id.setter
    def id(self, value: str) -> None:
        self._raw.id = value

    @property
    def operator(self) -> ComparisonOperator:
        return self._raw.operator

    @operator.setter
    def operator(self, value: ComparisonOperator) -> None:
        self._raw.operator = value

    @property
    def value_type(self) -> ValueType:
        return self._raw.value_type

    @property
    def value(self) -> ConditionValue:
        if self._raw.value_type == ValueType.Bool:
            return bool(self._raw.value)
        return self._raw.value

    @value.setter
    def value(self, value: ConditionValue) -> None:
        """The type of `value` selects how it's stored. Use what the evaluator returns for this id."""
        if isinstance(value, bool):
            self._raw.value_type, self._raw.value = ValueType.Bool, int(value)
        elif isinstance(value, float):
            self._raw.value_type, self._raw.value = ValueType.Float, value
        else:
            self._raw.value_type, self._raw.value = ValueType.Int32, value


class RuleActionView:
    """An action of a rule. Wraps the parsed data, so changes apply to the RuleSet."""

    def __init__(self, raw: construct.Container):
        self._raw = raw

    def __repr__(self) -> str:
        return f"<Action {self.id} {list(self.properties)}>"

    @property
    def id(self) -> ActionId | str:
        return self._raw.id

    @id.setter
    def id(self, value: ActionId | str) -> None:
        """Properties are typed from the id, so change them as well when the types differ."""
        self._raw.id = value

    @property
    def properties(self) -> list[PropertyValue]:
        """Floats and ints, depending on the action. See `ACTION_PROPERTY_TYPES`. Edit in place or replace."""
        return self._raw.properties

    @properties.setter
    def properties(self, value: Iterable[PropertyValue]) -> None:
        self._raw.properties = construct.ListContainer(value)


class RuleView:
    """A rule: when all conditions are true, the actions are executed."""

    def __init__(self, raw: construct.Container):
        self._raw = raw

    def __repr__(self) -> str:
        return f"<Rule if {list(self.conditions)} then {list(self.actions)}>"

    @property
    def conditions(self) -> _ViewList[RuleConditionView]:
        return _ViewList(self._raw.conditions, RuleConditionView)

    @property
    def actions(self) -> _ViewList[RuleActionView]:
        return _ViewList(self._raw.actions, RuleActionView)

    def add_condition(self, id: str, operator: ComparisonOperator, value: ConditionValue = True) -> RuleConditionView:
        raw = construct.Container(id=id, operator=operator, value_type=ValueType.Bool, value=0)
        self._raw.conditions.append(raw)
        view = RuleConditionView(raw)
        view.value = value
        return view

    def add_action(self, id: ActionId | str, *properties: PropertyValue) -> RuleActionView:
        raw = construct.Container(id=id, properties=construct.ListContainer(properties))
        self._raw.actions.append(raw)
        return RuleActionView(raw)


class _ViewList[V](collections.abc.Sequence[V]):
    """The items of a raw list as views. Items can be removed, but are added with the owner's `add_*`."""

    def __init__(self, raw: list, view_class: type[V]):
        self._raw = raw
        self._view_class = view_class

    def __len__(self) -> int:
        return len(self._raw)

    def __getitem__(self, index):  # noqa: ANN001
        if isinstance(index, slice):
            return [self._view_class(r) for r in self._raw[index]]
        return self._view_class(self._raw[index])

    def __delitem__(self, index: int | slice) -> None:
        del self._raw[index]


class RuleSet(BaseResource):
    """
    A RULE asset. A list of rules that are checked in order; if all conditions of a rule are true, its actions run.
    Then, unless an action asks to keep going, the evaluation stops. If it reaches the end, it moves on to the
    `parent_rule`.

    Views of the rules and their parts edit the RuleSet in place:

        rule_set = RuleSet.create(game)
        rule = rule_set.add_rule()
        rule.add_condition("PHLT", ComparisonOperator.LessThan, 20.0)
        rule.add_action(ActionId.HEALTH_100, 75.0, 1, 1)
        rule_set.rules[0].actions[0].properties[0] = 50.0
    """

    @classmethod
    def resource_type(cls) -> AssetType:
        return "RULE"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return RULE

    @classmethod
    def create(cls, target_game: Game, parent_rule: AssetId | None = None) -> RuleSet:
        """An empty RuleSet."""
        parent = target_game.invalid_asset_id if parent_rule is None else parent_rule
        data = RULE.build({"parent_rule": parent, "rules": []}, target_game=target_game)
        return cls.parse(data, target_game)

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        if self.target_game.is_valid_asset_id(self._raw.parent_rule):
            yield Dependency("RULE", self._raw.parent_rule)

    @property
    def parent_rule(self) -> AssetId | None:
        """The RULE evaluated after this one when no rule stopped the evaluation."""
        if self.target_game.is_valid_asset_id(self._raw.parent_rule):
            return self._raw.parent_rule
        return None

    @parent_rule.setter
    def parent_rule(self, value: AssetId | None) -> None:
        self._raw.parent_rule = self.target_game.invalid_asset_id if value is None else value

    @property
    def rules(self) -> _ViewList[RuleView]:
        """In evaluation order. Use `add_rule` to add, `del rules[i]` to remove."""
        return _ViewList(self._raw.rules, RuleView)

    def add_rule(self, index: int | None = None) -> RuleView:
        """Adds an empty rule, at the end or before `index`."""
        raw = construct.Container(conditions=construct.ListContainer(), actions=construct.ListContainer())
        if index is None:
            self._raw.rules.append(raw)
        else:
            self._raw.rules.insert(index, raw)
        return RuleView(raw)

    def __iter__(self) -> Iterator[RuleView]:
        return iter(self.rules)
