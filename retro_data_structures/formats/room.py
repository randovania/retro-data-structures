import typing

import construct
from construct import Struct, Int32ul, Hex

from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.common_types import AssetId128, GUID
from retro_data_structures.construct_extensions.misc import UntilEof
from retro_data_structures.formats.chunk_descriptor import SingleTypeChunkDescriptor
from retro_data_structures.formats.form_description import FormDescription
from retro_data_structures.game_check import Game

GreedyBytes = typing.cast(construct.Construct, construct.GreedyBytes)

LoadUnit = FormDescription("LUNT", 0, Struct(
    header=SingleTypeChunkDescriptor("LUHD", Struct(
        name=construct.PascalString(Int32ul, "utf8"),
        guid=GUID,
        unk1=construct.Int16ul,
        rest=GreedyBytes,
    )),
    load_resources=SingleTypeChunkDescriptor("LRES", construct.PrefixedArray(Int32ul, GUID)),
    load_layers=SingleTypeChunkDescriptor("LLYR", construct.PrefixedArray(Int32ul, GUID)),
))

PerformanceGroups = construct.PrefixedArray(
    construct.Int16ul,
    Struct(
        name=construct.PascalString(Int32ul, "utf8"),
        controller_id=GUID,
        unk1=construct.Flag,
        layer_guids=construct.PrefixedArray(construct.Int16ul, GUID),
    ),
)

GeneratedObjectMap = construct.PrefixedArray(
    construct.Int16ul,
    Struct(
        object_id=GUID,
        layer_id=GUID,
    )
)

Docks = construct.PrefixedArray(
    construct.Int16ul,
    GreedyBytes,
)

RoomHeader = FormDescription(
    "HEAD", 0, Struct(
        room_header=SingleTypeChunkDescriptor("RMHD", GreedyBytes),
        performance_groups=SingleTypeChunkDescriptor("PGRP", PerformanceGroups),
        generated_object_map=SingleTypeChunkDescriptor("LGEN", GeneratedObjectMap),
        docks=SingleTypeChunkDescriptor("DOCK", Docks),
        blit=SingleTypeChunkDescriptor("BLIT", GreedyBytes),
        load_units=construct.PrefixedArray(
            SingleTypeChunkDescriptor("LUNS", construct.Int16ul),
            LoadUnit,
        ),
    ),
)

GameObjectComponent = SingleTypeChunkDescriptor("COMP", Struct(
    component_type=Hex(Int32ul),
    instance_id=GUID,
    a=Hex(Int32ul),
    b=Hex(Int32ul),
    c=Hex(Int32ul),
    d=Hex(Int32ul),
    # name=construct.PascalString(Int32ul, "utf8"),
    z=GreedyBytes,
))

Layer = FormDescription("LAYR", 0, Struct(
    header=SingleTypeChunkDescriptor("LHED", Struct(
        name=construct.PascalString(Int32ul, "utf8"),
        id=GUID,
        unk1=Int32ul,
        rest=GreedyBytes,
    )),
    generated_script_object=FormDescription("GSRP", 0, GreedyBytes),
    # generated_script_object=FormDescription("GSRP", 0, SingleTypeChunkDescriptor(
    #     "GGOB", Struct(
    #         generated_game_object_id=AssetId128,
    #         z=GreedyBytes,
    #     ),
    # )),
    components=FormDescription("SRIP", 0, UntilEof(GameObjectComponent)),
    _=construct.Terminated,
))

ROOM = construct.FocusedSeq(
    "form",
    form=FormDescription(
        "ROOM", 147, Struct(
            header=RoomHeader,
            strp=SingleTypeChunkDescriptor("STRP", GreedyBytes),
            sdta=FormDescription("SDTA", 0, GreedyBytes),
            layers=FormDescription("LYRS", 0, construct.Array(
                lambda ctx: len(ctx._._.header.performance_groups[0].layer_guids),
                Layer,
            )),
            _=construct.Terminated,
        ),
    ),
    _=construct.Terminated,
)


class Room(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "ROOM"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return ROOM

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []
