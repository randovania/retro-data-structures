from __future__ import annotations

import typing
from enum import IntEnum

import construct

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AABox, Transform4f, Vector3
from retro_data_structures.construct_extensions.misc import ErrorWithMessage
from retro_data_structures.game_check import Game, current_game_at_least_else, get_current_game


def _const(val: int):
    return construct.Const(val, construct.Int32ub)


class AreaVisibilty(IntEnum):
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


MappableObject = construct.Struct(
    type=construct.Switch(
        get_current_game,
        {
            Game.PRIME: construct.Enum(construct.Int32sb, ObjectTypeMP1),
            Game.ECHOES: construct.Enum(construct.Int32sb, ObjectTypeMP2),
        },
        default=construct.Int32sb,
    ),
    visibility_mode=construct.Enum(construct.Int32ub, ObjectVisibility),
    editor_id=construct.Int32ub,
    unk1=construct.Int32ub,
    transform=Transform4f,
    unk2=construct.Int32ub[4],
)

Primitive = construct.Aligned(
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

MAPA = construct.Aligned(
    32,
    construct.Struct(
        header=construct.Struct(
            _magic=_const(0xDEADD00D),
            version=construct.Switch(
                get_current_game,
                {
                    Game.PRIME: _const(2),
                    Game.ECHOES: _const(3),
                    Game.CORRUPTION: _const(5),
                },
                default=ErrorWithMessage("Unknown game"),
            ),
            type=construct.Int32ub,  # Light/Dark world for Echoes
            visibility_mode=construct.Enum(construct.Int32ub, AreaVisibilty),
            bounding_box=AABox,
            map_adjustment=current_game_at_least_else(Game.ECHOES, Vector3, construct.Pass),
            mappable_object_count=construct.Int32ub,
            vertex_count=construct.Int32ub,
            primitive_count=construct.Int32ub,
        ),
        mappable_objects=construct.Array(construct.this.header.mappable_object_count, MappableObject),
        vertices=construct.Array(construct.this.header.vertex_count, Vector3),
        primitive_headers=construct.Array(
            construct.this.header.primitive_count,
            construct.Struct(
                normal=Vector3,
                center_of_mass=Vector3,
                primitive_table_start=construct.Int32ub,
                border_table_start=construct.Int32ub,
            ),
        ),
        primitive_tables=construct.Array(
            construct.this.header.primitive_count,
            construct.Struct(
                primitives=construct.PrefixedArray(
                    construct.Int32ub,
                    Primitive,
                ),
                borders=construct.PrefixedArray(
                    construct.Int32ub,
                    Border,
                ),
            ),
        ),
    ),
    b"\xff",
)


class Mapa(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return MAPA

    @classmethod
    def resource_type(cls) -> AssetType:
        return "MAPA"

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
