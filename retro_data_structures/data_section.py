from construct import Tell, Pointer, Int32ub, Struct, Array, Rebuild, If

from retro_data_structures.construct_extensions import AlignedPrefixed, Skip


def _get_current_section(context, increment=True):
    root = context["_root"]
    section = root["_current_section"]
    if increment:
        root["_current_section"] += 1
    return section

def _get_section_length_address(context):
    index = _get_current_section(context)
    return context._root._data_section_sizes.address + index * Int32ub.length

def DataSectionSizes(section_count, include_value=False):
    return Struct(
        address=Tell,
        value=If(include_value, Array(section_count, Rebuild(Int32ub, lambda ctx: 0))),
        offset=If(lambda this: not include_value, Skip(section_count, Int32ub))
    )

def GetDataSectionSize(context):
    return context._root._data_section_sizes.value[_get_current_section(context)]

def GetDataSectionId(context):
    return _get_current_section(context, False)

def DataSectionSizePointer():
    return Pointer(_get_section_length_address, Int32ub)


def DataSection(subcon, align=32):
    return AlignedPrefixed(DataSectionSizePointer(), subcon, align, 0, b"\x00")
