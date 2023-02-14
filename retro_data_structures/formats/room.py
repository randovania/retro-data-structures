import io
import typing

import construct
from construct import Struct, Int32ul, Hex

import retro_data_structures.properties.prime_remastered.objects
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.common_types import GUID
from retro_data_structures.construct_extensions.misc import ErrorWithMessage
from retro_data_structures.formats.chunk_descriptor import SingleTypeChunkDescriptor
from retro_data_structures.formats.form_descriptor import FormDescriptor
from retro_data_structures.game_check import Game
from retro_data_structures.properties import BaseProperty

GreedyBytes = typing.cast(construct.Construct, construct.GreedyBytes)

LoadUnit = FormDescriptor("LUNT", 0, 0, Struct(
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
    skip=construct.Prefixed(Int32ul, GreedyBytes),
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
    id_f=GUID,
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

RoomHeader = FormDescriptor(
    "HEAD", 0, 0, Struct(
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


class RDSPropertyAdapter(construct.Adapter):
    def __init__(self, type_id):
        super().__init__(GreedyBytes)
        self.type_id = type_id

    def _decode(self, obj: bytes, context, path):
        type_id = self.type_id(context)
        try:
            property_class = retro_data_structures.properties.prime_remastered.objects.get_object(type_id)
        except KeyError:
            return obj
        return property_class.from_stream(io.BytesIO(obj))

    def _encode(self, obj: typing.Union[BaseProperty, bytes], context, path):
        if isinstance(obj, BaseProperty):
            data = io.BytesIO()
            obj.to_stream(data)
            return data.getvalue()
        return obj


Property = Struct(
    type_id=Hex(Int32ul),
    data=RDSPropertyAdapter(construct.this.type_id),
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

Layer = FormDescriptor("LAYR", 0, 0, Struct(
    header=SingleTypeChunkDescriptor("LHED", Struct(
        name=construct.PascalString(Int32ul, "utf8"),
        id=GUID,
        unk1=Int32ul,
        rest=GreedyBytes,
    )),
    generated_script_object=FormDescriptor("GSRP", 0, 0, GreedyBytes),
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

ROOM = FormDescriptor(
    "ROOM", 147, 160, Struct(
        header=RoomHeader,
        strp=SingleTypeChunkDescriptor("STRP", STRP),
        script_data=FormDescriptor("SDTA", 0, 0, ScriptData),
        layers=FormDescriptor("LYRS", 0, 0, construct.Array(
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
