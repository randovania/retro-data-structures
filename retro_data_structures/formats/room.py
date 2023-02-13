import typing

import construct
from construct import Struct, Int32ul, Hex

from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.common_types import GUID
from retro_data_structures.construct_extensions.misc import ErrorWithMessage, Skip, UntilEof
from retro_data_structures.formats.chunk_descriptor import SingleTypeChunkDescriptor
from retro_data_structures.formats.form_description import FormDescription
from retro_data_structures.game_check import Game

GreedyBytes = typing.cast(construct.Construct, construct.GreedyBytes)

LoadUnit = FormDescription("LUNT", 0, Struct(
    header=SingleTypeChunkDescriptor("LUHD", Struct(
        name=construct.PascalString(Int32ul, "utf8"),
        guid=GUID,
        idB=GUID,
        unk1=construct.Int16ul,
        unk2=Int32ul,
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
    Struct(
        guid1=GUID,
        guid2=GUID,
        guid3=GUID,
        guid4=GUID,
        roomType1=construct.Int16ul,
        roomType2=construct.Int16ul,
    ),
)

DataEnumValue = Struct(
    unk1=Int32ul,
    idA=GUID,
    skip=Int32ul,
    _do_skip=Skip(construct.this.skip, construct.Int8ul),
    idB=GUID,
)

GameAreaHeader = Struct(
    id_a=GUID,
    unk1=construct.Int16ul,
    unk2=construct.Int16ul,
    unk3=construct.Flag,
    id_b=GUID,
    id_c=GUID,
    id_d=GUID,
    id_e=GUID,
    id_F=GUID,
    work_stages=Struct(
        items=construct.PrefixedArray(construct.Int16ul, Struct(
            type=Hex(construct.Int32ul),
            data=construct.Prefixed(construct.Int16ul, construct.Switch(
                construct.this.type,
                {
                    0x7B68B3A0: DataEnumValue,
                    0xb9187c94: DataEnumValue,
                    0xec5d9069: DataEnumValue,
                    0x8333a604: DataEnumValue,
                    0x5ca42b9d: DataEnumValue,

                    # LdrToEnum_ProductionWorkStageEnu
                    0x113F9CE1: Hex(Int32ul),
                },
                # TODO: should actually be GreedyBytes since the game skips over unknown ids
                ErrorWithMessage(lambda ctx: f"Unknown type: {ctx.type}"),
            ))
        )),
    ),
)

BakedLightning = construct.Struct(
    "unk1" / Int32ul,  # always either 3 or 0?
    construct.StopIf(lambda ctx: ctx.unk1 == 0),
    construct.Check(lambda ctx: ctx.unk1 == 3),
    "resource1" / GUID,
    "unk2" / construct.PrefixedArray(Int32ul, GUID),
    "unk3" / construct.PrefixedArray(Int32ul, Struct(
        "unk1" / Int32ul,
        "unk2" / Int32ul,
        "unk3" / Int32ul,
        "unk4" / construct.Const(0, Int32ul)
    )),
    "resource2" / GUID,
    construct.Terminated
)

RoomHeader = FormDescription(
    "HEAD", 0, Struct(
        game_area_header=SingleTypeChunkDescriptor("RMHD", GameAreaHeader),
        performance_groups=SingleTypeChunkDescriptor("PGRP", PerformanceGroups),
        generated_object_map=SingleTypeChunkDescriptor("LGEN", GeneratedObjectMap),
        docks=SingleTypeChunkDescriptor("DOCK", Docks),
        baked_lightinng=SingleTypeChunkDescriptor("BLIT", BakedLightning),
        load_units=construct.PrefixedArray(
            SingleTypeChunkDescriptor("LUNS", construct.Int16ul),
            LoadUnit,
        ),
    ),
)

STRP = Struct(
    unk=Int32ul,
    pools=construct.PrefixedArray(
        Int32ul,
        construct.Prefixed(
            Int32ul,
            construct.GreedyRange(construct.CString("utf-8")),
        ),
    ),
    z=GreedyBytes,
)

PooledString = Struct(
    a=construct.Int32sl,
    b=construct.IfThenElse(
        construct.this.a != -1,
        Int32ul,
        construct.Prefixed(Int32ul, GreedyBytes),
    ),
)

CalculateAllocatedMemoryForTypedefInterfaceSLdrFromCRC32 = Struct(
    a=construct.Prefixed(construct.Int16ul, GreedyBytes),
)


SizeofAllocationsForEventCriteriaSLdrFromStream = Struct(
    a=Int32ul,
    b=construct.If(construct.this.a != 0, Struct(
        a=CalculateAllocatedMemoryForTypedefInterfaceSLdrFromCRC32,
        b=construct.Prefixed(Int32ul, GreedyBytes),
    )),
)
SizeofAllocationsForActionPayloadSLdrFromStream = SizeofAllocationsForEventCriteriaSLdrFromStream
SizeofAllocationsForLinkDataSLdrFromStream = SizeofAllocationsForEventCriteriaSLdrFromStream


def PropertyType(known_properties: typing.Dict[int, construct.Construct]):
    return Struct(
        properties=construct.PrefixedArray(construct.Int16ul, Struct(
            type_id=Hex(construct.Int32sl),
            data=construct.Prefixed(construct.Int16ul, construct.Switch(
                construct.this.type_id, known_properties, GreedyBytes,
            ))
        )),
    )


SLdrVector_MP1Typedef = PropertyType({
    0x2649E551: construct.Float32l,  # x
    -0x2D44A43A: construct.Float32l,  # y
    0x7F9499B2: construct.Float32l,  # z
})

SLdrAnimSet_MP1Typedef = PropertyType({
    -0x5a76277b: GUID,
    -0x783fc5ff: PooledString,
    -0x290F3F10: PooledString,
})


SLdrWorldTeleporterTooMP1 = PropertyType(
    {
        -0x2B65AE81: GUID,  # idA
        -0x65A00494: GUID,  # idB
        0x6AEAEE72: SLdrAnimSet_MP1Typedef,
        -0x44c519d6: SLdrVector_MP1Typedef,
        -0x584CE072: GUID,  # idC
        0x4FB5E821: SLdrVector_MP1Typedef,
        -0x3dac9987: SLdrVector_MP1Typedef,
        0x5407BB23: GUID,  # idE
    },
)

Property = Struct(
    type_id=Hex(Int32ul),
    data=construct.Switch(
        construct.this.type_id,
        {
            # CWorldTeleporterToo
            0x2fa104ff: SLdrWorldTeleporterTooMP1,
        },
        GreedyBytes,
    ),
)

ScriptData = Struct(
    sdhr=SingleTypeChunkDescriptor("SDHR", Struct(
        properties_count=Int32ul,
        instance_data_count=Int32ul,
        skip_count=Int32ul,
        skip=construct.Bytes(construct.this.skip_count * 0x18),
    )),
    properties=construct.Array(construct.this.sdhr.properties_count, SingleTypeChunkDescriptor("SDEN", Property)),
    instance_data=construct.Array(construct.this.sdhr.instance_data_count, SingleTypeChunkDescriptor("IDTA", Struct(
        guid=GUID,
        str=PooledString,
        connections=construct.PrefixedArray(
            construct.Int16ul,
            Struct(
                skip1=construct.Bytes(0x1a),
                event_criteria_sldr=SizeofAllocationsForEventCriteriaSLdrFromStream,
                action_payload_sldr=SizeofAllocationsForActionPayloadSLdrFromStream,
                skip2=construct.Bytes(0x13),
            ),
        ),
        script_links=construct.PrefixedArray(
            construct.Int16ul,
            Struct(
                skip1=construct.Bytes(0x14),
                a=SizeofAllocationsForLinkDataSLdrFromStream,
                skip2=construct.Bytes(0x12),
            )
        ),
        skip_the_rest=GreedyBytes,
    ))),
)

GameObjectComponent = SingleTypeChunkDescriptor("COMP", Struct(
    component_type=Hex(Int32ul),
    instance_id=GUID,
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
    # components=FormDescription("SRIP", 0, UntilEof(GameObjectComponent)),
    components=GreedyBytes,
    _=construct.Terminated,
))

ROOM = FormDescription(
    "ROOM", 147, Struct(
        header=RoomHeader,
        strp=SingleTypeChunkDescriptor("STRP", STRP),
        script_data=FormDescription("SDTA", 0, ScriptData),
        layers=FormDescription("LYRS", 0, construct.Array(
            lambda ctx: len(ctx._._.header.performance_groups[0].layer_guids),
            Layer,
        )),
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
