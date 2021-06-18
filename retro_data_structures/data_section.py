from construct import Tell, Pointer, Int32ub, Struct, Seek

from retro_data_structures.construct_extensions import AlignedPrefixed, Skip


def DataSectionSizes(section_count):
    return Struct(
        address=Tell,
        offset=Skip(section_count, Int32ub),
        # value=Array(section_count, Rebuild(Int32ub, lambda ctx: 0)),
    )


def DataSection(subcon, align=32):
    def get_section_length_address(context):
        root = context["_root"]
        index = root["_current_section"]
        root["_current_section"] += 1
        return root._data_section_sizes.address + index * Int32ub.length

    return AlignedPrefixed(Pointer(get_section_length_address, Int32ub), subcon, align, 0, b"\x00")
