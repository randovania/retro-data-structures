import construct
from construct import (Struct, Const, Int16ub, PrefixedArray, Int32ub, PascalString, IfThenElse,
                       FocusedSeq, Pointer, Aligned, Tell, Rebuild,
                       GreedyBytes, Array, Seek, Computed, RawCopy)

from retro_data_structures import game_check
from retro_data_structures.common_types import ObjectTag_32
from retro_data_structures.compression import LZOCompressedBlock, ZlibCompressedBlock
from retro_data_structures.construct_extensions import AlignTo, AlignedPrefixed, LazyPatchedForBug

PAKHeader = Struct(
    version_major=Const(3, Int16ub),
    version_minor=Const(5, Int16ub),
    unused=Const(0, Int32ub),
)

ResourceHeader = Struct(
    compressed=Int32ub,
    asset=ObjectTag_32,
    size=Int32ub,
    offset=Int32ub,
)

PAKNoData = Struct(
    _header=PAKHeader,
    named_resources=PrefixedArray(Int32ub, Struct(
        asset=ObjectTag_32,
        name=PascalString(Int32ub, "utf-8"),
    )),
    resources=PrefixedArray(Int32ub, ResourceHeader)
)


def header_field(offset):
    def result(ctx):
        parents = [ctx]
        while "_" in parents[-1]:
            parents.append(parents[-1]["_"])

        start_headers = None
        index = None

        for c in reversed(parents):
            if "_start_headers" in c:
                start_headers = c["_start_headers"]
                break

        for c in parents:
            if "_resource_index" in c:
                index = c["_resource_index"]
                break

        if index is None or start_headers is None:
            raise ValueError("Missing required context key")

        return start_headers + (index * ResourceHeader.sizeof()) + offset

    return result


def skip_headers(ctx):
    result = ResourceHeader.sizeof() * ctx["_num_resources"]
    return result


CompressedPakResource = FocusedSeq(
    "data",
    decompressed_size=Rebuild(Int32ub, construct.len_(construct.this.data)),
    data=IfThenElse(
        game_check.uses_lzo,
        LZOCompressedBlock(construct.this.decompressed_size),
        ZlibCompressedBlock,
    ),
)


def create():
    return "PAK" / Struct(
        _header=PAKHeader,
        named_resources=PrefixedArray(Int32ub, Struct(
            asset=ObjectTag_32,
            name=PascalString(Int32ub, "utf-8"),
        )),
        _num_resources=Rebuild(Int32ub, construct.len_(construct.this.resources)),
        _start_headers=Tell,
        _skip_headers=Seek(skip_headers, 1),
        _align=AlignTo(32),
        resources=Array(
            construct.this["_num_resources"],
            Aligned(32, Struct(
                _start=Tell,
                _resource_index=Computed(lambda ctx: ctx["_index"]),
                compressed=Pointer(header_field(0x0), Int32ub),
                asset=Pointer(header_field(0x4), ObjectTag_32),
                contents=RawCopy(LazyPatchedForBug(AlignedPrefixed(
                    Pointer(header_field(0xC), Int32ub),
                    IfThenElse(
                        construct.this.compressed > 0,
                        CompressedPakResource,
                        GreedyBytes,
                    ),
                    32,
                    Int32ub.length,
                ))),
                _end=Tell,
                size=Pointer(header_field(0xC), Rebuild(Int32ub, construct.this.contents.length)),
                _offset=Pointer(header_field(0x10), Rebuild(Int32ub, lambda ctx: ctx["_start"])),
            )),
        ),
    )


PAK = create()
