import construct
from construct import Array, FocusedSeq, Tell, Prefixed, Pointer, Int32ub


def DataSectionSizes(section_count):
    return Array(section_count, FocusedSeq(
        "address",
        address=Tell,
        value=construct.Seek(4, 1),
    ))


def DataSection(subcon):
    def get_section_length_address(context):
        root = context["_root"]
        index = root["_current_section"]
        root["_current_section"] += 1
        return root._data_section_sizes[index]

    return Prefixed(Pointer(get_section_length_address, Int32ub), subcon)
