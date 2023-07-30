from __future__ import annotations

import typing

from construct import (
    Const,
    Construct,
    Enum,
    FocusedSeq,
    GreedyBytes,
    If,
    Int8sb,
    Int8ub,
    Int16ub,
    Int32ub,
    Padded,
    Peek,
    Pointer,
    Prefixed,
    PrefixedArray,
    Rebuild,
    RepeatUntil,
    Seek,
    StopIf,
    Struct,
    Tell,
)

from retro_data_structures import game_check
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import String

if typing.TYPE_CHECKING:
    from retro_data_structures.game_check import Game

Pool = GreedyBytes


def project_table(offset: int, subcon, group_type: int | None = None):
    table = FocusedSeq(
        "table",
        "pos" / Tell,
        "offset" / Pointer(lambda ctx: ctx._._offsets + offset, Rebuild(Int32ub, lambda ctx: ctx.pos - ctx._._start)),
        Seek(lambda ctx: ctx._._start + ctx.offset),
        # Check(lambda ctx: (ctx.pos - ctx._._start) == ctx.offset),
        "table" / subcon,
    )
    if group_type is None:
        return table
    return If(lambda ctx: ctx.group_type == group_type, table)


StandardTable = RepeatUntil(lambda obj, lst, ctx: obj == 0xFFFF, Int16ub)

Project = Struct(
    "_start" / Tell,
    "group_end_offset" / Int32ub,
    StopIf(lambda ctx: ctx.group_end_offset == 0xFFFFFFFF),
    "group_id" / Int16ub,
    "group_type" / Enum(Int16ub, SongGroup=0, SFXGroup=1),
    "_offsets" / Tell,
    "_first_offset" / Peek(Int32ub),
    Seek(lambda ctx: ctx._start + ctx._first_offset),
    "soundmacro_id_table" / project_table(0x0, StandardTable),
    "sample_id_table" / project_table(0x4, StandardTable),
    "tables_table" / project_table(0x8, StandardTable),
    "keymaps_table" / project_table(0xC, StandardTable),
    "layers_table" / project_table(0x10, StandardTable),
    "song_group_stuff" / If(lambda ctx: ctx.group_type == 1, GreedyBytes),
    "sfx_table"
    / project_table(
        0x14,
        PrefixedArray(
            Padded(4, Int16ub),
            Padded(
                10,
                Struct(
                    "define_id" / Int16ub,
                    "object_id" / Int16ub,
                    "priority" / Int8ub,
                    "max_voices" / Int8ub,
                    "definite_velocity" / Int8ub,
                    "panning" / Int8sb,
                    "definite_key" / Int8ub,
                ),
            ),
        ),
    ),
)

Sample = GreedyBytes

SampleDirectory = GreedyBytes


def mp1_sized_chunk(subcon):
    return Prefixed(Int32ub, subcon)


def mp2_sized_chunk(offset: int, subcon):
    return Prefixed(Pointer(lambda ctx: ctx._size_offsets + offset, Int32ub), subcon)


DataMP1 = Struct(
    "audio_directory" / String,
    "audio_group_name" / String,
    "pool" / mp1_sized_chunk(Pool),
    "project" / mp1_sized_chunk(Project),
    "sample" / mp1_sized_chunk(Sample),
    "sample_directory" / mp1_sized_chunk(SampleDirectory),
)

DataMP2 = Struct(
    "version" / Const(1, Int32ub),
    "audio_group_name" / String,
    "group_id" / Int16ub,
    "_size_offsets" / Tell,
    Seek(0x10, 1),
    "pool" / mp2_sized_chunk(0, Pool),
    "project" / mp2_sized_chunk(4, Project),
    "sample_directory" / mp2_sized_chunk(8, SampleDirectory),
    "sample" / mp2_sized_chunk(12, Sample),
)

AGSC = game_check.current_game_at_least_else(game_check.Game.ECHOES, DataMP2, DataMP1)

ATBL = PrefixedArray(Int32ub, Int16ub)


class Atbl(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return ATBL

    @classmethod
    def resource_type(cls) -> AssetType:
        return "ATBL"

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []


class Agsc(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return AGSC

    @classmethod
    def resource_type(cls) -> AssetType:
        return "AGSC"

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []

    @property
    def define_ids(self) -> typing.Iterator[int]:
        project = self.raw.project

        if "sfx_table" not in project:
            return

        for sfx in project.sfx_table:
            yield sfx.define_id
