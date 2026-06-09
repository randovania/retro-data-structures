from __future__ import annotations

import typing
from enum import IntEnum

import construct

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AABox, Transform4f, Vector3
from retro_data_structures.construct_extensions.misc import ErrorWithMessage
from retro_data_structures.game_check import Game, current_game_at_least_else, get_current_game

if typing.TYPE_CHECKING:
    from retro_data_structures.formats.script_object import InstanceId
    from retro_data_structures.transform import Transform

Vec3 = tuple[float, float, float]


def _const(val: int):
    return construct.Const(val, construct.Int32ub)


class AreaVisibility(IntEnum):
    Always = 0
    VisitOrMapStation = 1
    VisitOnly = 2
    Never = 3


class ObjectVisibility(IntEnum):
    Always = 0
    AreaVisitOrMapStation = 1
    DoorVisit = 2
    Never = 3
    AreaVisitOrMapStation2 = 4


class ObjectTypeMP1(IntEnum):
    NormalDoor = 0
    ShieldDoor = 1
    IceDoor = 2
    WaveDoor = 3
    PlasmaDoor = 4
    BigDoor = 5
    BigDoor2 = 6
    IceDoorCeil = 7
    IceDoorFloor = 8
    WaveDoorCeil = 9
    WaveDoorFloor = 10
    PlasmaDoorCeil = 11
    PlasmaDoorFloor = 12
    IceDoorFloor2 = 13
    WaveDoorFloor2 = 14
    PlasmaDoorFloor2 = 15

    DownArrowYellow = 27
    UpArrowYellow = 28
    DownArrowGreen = 29
    UpArrowGreen = 30
    DownArrowRed = 31
    UpArrowRed = 32

    Elevator = 33
    SaveStation = 34
    MissileStation = 37

    @property
    def is_door_type(self):
        return self < ObjectTypeMP1.DownArrowYellow


class ObjectTypeMP2(IntEnum):
    NormalDoor = 0
    MissileDoor = 1
    DarkDoor = 2
    AnnihilatorDoor = 3
    LightDoor = 4
    SuperMissileDoor = 5
    SeekerMissileDoor = 6
    PowerBombDoor = 7

    Elevator = 16
    SaveStation = 17

    AmmoStation = 20
    Portal = 21
    LightTeleporter = 22
    TranslatorGate = 23
    UpArrow = 24
    DownArrow = 25

    @property
    def is_door_type(self):
        return self < ObjectTypeMP2.Elevator


class GXPrimitive(IntEnum):
    GX_QUADS = 0x80
    GX_TRIANGLES = 0x90
    GX_TRIANGLESTRIP = 0x98
    GX_TRIANGLEFAN = 0xA0
    GX_LINES = 0xA8
    GX_LINESTRIP = 0xB0
    GX_POINTS = 0xB8

    def __str__(self):
        return self.name


_MappableObjectConstruct = construct.Struct(
    type=construct.Switch(
        get_current_game,
        {
            Game.PRIME: EnumAdapter(ObjectTypeMP1, construct.Int32sb),
            Game.ECHOES: EnumAdapter(ObjectTypeMP2, construct.Int32sb),
        },
        default=construct.Int32sb,
    ),
    visibility_mode=EnumAdapter(ObjectVisibility),
    editor_id=construct.Int32ub,
    unk1=construct.Int32ub,
    transform=Transform4f,
    unk2=construct.Int32ub[4],
)


class MappableObject[T: (ObjectTypeMP1, ObjectTypeMP2)]:
    def __init__(self, raw: construct.Container):
        self._raw = raw

    def __repr__(self) -> str:
        object_type = self.object_type
        visibility_mode = self.visibility_mode
        editor_id = self.editor_id
        transform = self.transform

        return f"{self.__class__.__qualname__}({object_type=}, {visibility_mode=}, {editor_id=}, {transform=})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MappableObject):
            return False

        return (
            self.object_type == other.object_type
            and self.visibility_mode == other.visibility_mode
            and self.editor_id == other.editor_id
            and self.transform == other.transform
        )

    __hash__ = None

    @classmethod
    def create(
        cls,
        object_type: T,
        visibility_mode: ObjectVisibility,
        editor_id: InstanceId,
        transform: Transform,
    ) -> typing.Self:
        obj = cls(
            construct.Container(
                {
                    "unk1": 0xFFFFFFFF,
                    "unk2": [0xFFFFFFFF] * 4,
                }
            )
        )
        obj.object_type = object_type
        obj.visibility_mode = visibility_mode
        obj.editor_id = editor_id
        obj.transform = transform
        return obj

    @property
    def object_type(self) -> T:
        return self._raw.type

    @object_type.setter
    def object_type(self, value: T) -> None:
        self._raw.type = value

    @property
    def visibility_mode(self) -> ObjectVisibility:
        return self._raw.visibility_mode

    @visibility_mode.setter
    def visibility_mode(self, value: ObjectVisibility) -> None:
        self._raw.visibility_mode = value

    @property
    def editor_id(self) -> InstanceId:
        from retro_data_structures.formats.script_object import InstanceId

        return InstanceId(self._raw.editor_id)

    @editor_id.setter
    def editor_id(self, value: InstanceId) -> None:
        self._raw.editor_id = value

    @property
    def transform(self) -> Transform:
        return self._raw.transform

    @transform.setter
    def transform(self, value: Transform):
        self._raw.transform = value


class MappableObjectAdapter(construct.Adapter):
    def __init__(self):
        super().__init__(_MappableObjectConstruct)

    def _decode(self, obj: construct.Container, context: construct.Container, path: str) -> MappableObject:
        return MappableObject(obj)

    def _encode(self, obj: MappableObject, context: construct.Container, path: str) -> construct.Container:
        return obj._raw


MappableObjectConstruct = MappableObjectAdapter()


class Vec3TupleAdapter(construct.Adapter):
    def __init__(self):
        super().__init__(Vector3)

    def _decode(self, obj: list[float], context: construct.Container, path: str) -> Vec3:
        return tuple(obj)

    def _encode(self, obj: Vec3, context: construct.Container, path: str) -> list[float]:
        return list(obj)


Vec3Tuple = Vec3TupleAdapter()

PrimitiveConstruct = construct.Aligned(
    4,
    construct.Struct(
        type=EnumAdapter(GXPrimitive),
        indices=construct.PrefixedArray(construct.Int32ub, construct.Int8ub),
    ),
)

Border = construct.Aligned(
    4,
    construct.Struct(
        indices=construct.PrefixedArray(construct.Int32ub, construct.Int8ub),
    ),
)

PrimitiveTableConstruct = construct.Struct(
    index=construct.Computed(lambda this: this._index),
    primitives=construct.PrefixedArray(
        construct.Int32ub,
        PrimitiveConstruct,
    ),
    borders=construct.PrefixedArray(
        construct.Int32ub,
        Border,
    ),
)


class PrimitiveOffsetAdapter(construct.Adapter):
    def __init__(self):
        super().__init__(construct.Int32ub)

    def _decode(self, obj: int, context: construct.Container, path: str) -> int:
        end_of_header = context._.header._end_of_header
        end_of_mappables = context._._end_of_mappable_objects

        return (obj + end_of_header) - end_of_mappables

    def _encode(self, obj: int, context: construct.Container, path: str) -> int:
        end_of_header = context._.header._end_of_header
        end_of_mappables = context._._end_of_mappable_objects

        return (obj + end_of_mappables) - end_of_header


PrimitiveOffset = PrimitiveOffsetAdapter()

PrimitiveHeaderConstruct = construct.Struct(
    normal=Vec3Tuple,
    center_of_mass=Vec3Tuple,
    _raw_primitive_start=construct.Peek(construct.Int32ub),
    primitive_table_start=PrimitiveOffset,
    _raw_border_start=construct.Peek(construct.Int32ub),
    border_table_start=PrimitiveOffset,
)

MAPA = construct.Aligned(
    32,
    construct.Struct(
        "header"
        / construct.Struct(
            "_magic" / _const(0xDEADD00D),
            "version"
            / construct.Switch(
                get_current_game,
                {
                    Game.PRIME: _const(2),
                    Game.ECHOES: _const(3),
                    Game.CORRUPTION: _const(5),
                },
                default=ErrorWithMessage("Unknown game"),
            ),
            "type" / construct.Int32ub,  # Light/Dark world for Echoes
            "visibility_mode" / EnumAdapter(AreaVisibility),
            "bounding_box" / AABox,
            "map_adjustment" / current_game_at_least_else(Game.ECHOES, Vec3Tuple, construct.Pass),
            "_mappable_object_offset" / construct.Tell,
            construct.Seek(4, whence=1),
            "vertex_count" / construct.Int32ub,
            "primitive_count" / construct.Int32ub,
            "_end_of_header" / construct.Tell,
        ),
        "mappable_objects"
        / construct.PrefixedArray(
            construct.Pointer(
                lambda this: this._.header._mappable_object_offset,
                construct.Int32ub,
            ),
            MappableObjectConstruct,
        ),
        "_end_of_mappable_objects" / construct.Tell,
        "vertices" / construct.Array(construct.this.header.vertex_count, Vec3Tuple),
        "primitive_headers"
        / construct.Array(
            construct.this.header.primitive_count,
            PrimitiveHeaderConstruct,
        ),
        "primitive_tables"
        / construct.Array(
            construct.this.header.primitive_count,
            PrimitiveTableConstruct,
        ),
    ),
    b"\xff",
)


class Mapa[MappableObjT: (ObjectTypeMP1, ObjectTypeMP2)](BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MAPA

    @classmethod
    def resource_type(cls) -> AssetType:
        return "MAPA"

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []

    @property
    def version(self) -> int:
        return self.raw.header.version

    @property
    def is_dark_world(self) -> bool:
        return self.raw.header.type == 1

    @is_dark_world.setter
    def is_dark_world(self, value: bool) -> None:
        self.raw.header.type = 1 if value else 0

    @property
    def visibility_mode(self) -> AreaVisibility:
        return self.raw.header.visibility_mode

    @visibility_mode.setter
    def visibility_mode(self, value: AreaVisibility) -> None:
        self.raw.header.visibility_mode = value

    @property
    def bounding_box_min(self) -> Vec3:
        return tuple(self.raw.header.bounding_box.min)

    @bounding_box_min.setter
    def bounding_box_min(self, value: Vec3):
        self.raw.header.bounding_box.min = value

    @property
    def bounding_box_max(self) -> Vec3:
        return tuple(self.raw.header.bounding_box.max)

    @bounding_box_max.setter
    def bounding_box_max(self, value: Vec3):
        self.raw.header.bounding_box.max = value

    @property
    def map_adjustment(self) -> Vec3:
        return tuple(self.raw.header.map_adjustment)

    @map_adjustment.setter
    def map_adjustment(self, value: Vec3):
        self.raw.header.map_adjustment = value

    @property
    def mappable_objects(self) -> list[MappableObject[MappableObjT]]:
        return self.raw.mappable_objects

    @mappable_objects.setter
    def mappable_objects(self, value: list[MappableObject[MappableObjT]]) -> None:
        self.raw.mappable_objects = value
