import typing

import construct
from construct import Struct

from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.formats.chunk_descriptor import ChunkDescriptor
from retro_data_structures.formats.form_description import FormDescription
from retro_data_structures.game_check import Game

Header = Struct(

)

GreedyBytes = typing.cast(construct.Construct, construct.GreedyBytes)

LoadUnit = FormDescription("LUNT", 0, GreedyBytes)

RoomHeader = FormDescription(
    "HEAD", 0, Struct(
        room_header=ChunkDescriptor({"RMHD": GreedyBytes}),
        performance_groups=ChunkDescriptor({"PGRP": GreedyBytes}),
        generated_object_map=ChunkDescriptor({"LGEN": GreedyBytes}),
        docks=ChunkDescriptor({"DOCK": GreedyBytes}),
        blit=ChunkDescriptor({"BLIT": GreedyBytes}),
        luns=ChunkDescriptor({"LUNS": GreedyBytes}),
        load_units=construct.GreedyRange(LoadUnit),
        _=construct.Terminated,
    ),
)

Layer = FormDescription("LAYR", 0, Struct(
    header=ChunkDescriptor({"LHED": GreedyBytes}),
    generated_script_object=FormDescription("GSRP", 0, GreedyBytes),
    components=FormDescription("SRIP", 0, ChunkDescriptor({
        "COMP": GreedyBytes,
    })),
    _=construct.Terminated,
))

ROOM = FormDescription(
    "ROOM", 147, Struct(
        header=RoomHeader,
        strp=ChunkDescriptor({"STRP": GreedyBytes}),
        sdta=FormDescription("SDTA", 0, GreedyBytes),
        layers=FormDescription("LYRS", 0, construct.GreedyRange(Layer)),
        _=construct.Terminated,
    ),
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
