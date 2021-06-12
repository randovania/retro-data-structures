from construct import Array, Tell, Prefixed, Pointer, Int32ub, Struct


def DataSectionSizes(section_count):
    return Array(section_count, Struct(
        address=Tell,
        value=Int32ub,
    ))


def DataSection(subcon):
    def get_section_length_address(context):
        root = context["_root"]
        index = root["_current_section"]
        root["_current_section"] += 1
        return root._data_section_sizes[index].address

    return Prefixed(Pointer(get_section_length_address, Int32ub), subcon)
