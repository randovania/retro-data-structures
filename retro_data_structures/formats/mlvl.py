"""
Wiki: https://wiki.axiodl.com/w/MLVL_(File_Format)
"""
import construct
from construct import (
    Array, Struct, Int32ub, PrefixedArray, Int64ub, Float32b, Int16ub, CString, Const, Int8ub,
    Switch, Peek, Sequence, FocusedSeq
)

from retro_data_structures.common_types import Vector3, AssetId32, AssetId64, FourCC
from retro_data_structures.construct_extensions import PrefixedArrayWithExtra
from retro_data_structures.formats.guid import GUID

MLVLConnectingDock = Struct(
    area_index=Int32ub,
    dock_index=Int32ub,
)

MLVLDock = Struct(
    connecting_dock=PrefixedArray(Int32ub, MLVLConnectingDock),
    dock_coordinates=PrefixedArray(Int32ub, Vector3),
)

MLVLMemoryRelay = Struct(
    memory_relay_index=Int32ub,
    target_index=Int32ub,
    message=Int16ub,
    active=Int8ub,
)

MLVLAreaLayerFlags = Struct(
    layer_count=Int32ub,
    layer_flags=Int64ub,
)


def create_area(version: int, asset_id):
    MLVLAreaDependency = Struct(
        asset_id=asset_id,
        asset_type=FourCC,
    )

    MLVLAreaDependencies = Struct(
        # Always empty
        dependencies_a=PrefixedArray(Int32ub, MLVLAreaDependency),
        dependencies_b=PrefixedArray(Int32ub, MLVLAreaDependency),
        dependencies_offset=PrefixedArray(Int32ub, Int32ub),
    )

    area_fields = [
        "area_name_id" / asset_id,
        "area_transform" / Array(12, Float32b),
        "area_bounding_box" / Array(6, Float32b),
        "area_mrea_id" / asset_id,
        "internal_area_id" / asset_id,
    ]

    # DKCR
    if version < 0x1B:
        area_fields.append("attached_area_index" / PrefixedArray(Int32ub, Int16ub))

    # Corruption
    if version < 0x19:
        area_fields.append("dependencies" / MLVLAreaDependencies)

    area_fields.append("docks" / PrefixedArray(Int32ub, MLVLDock))

    # Echoes
    if version == 0x17:
        area_fields.append("module_dependencies" / Struct(
            rel_module=PrefixedArray(Int32ub, CString("utf-8")),
            rel_offset=PrefixedArray(Int32ub, Int32ub),
        ))

    # DKCR
    if version >= 0x1B:
        # Unknown, always 0?
        area_fields.append(Const(0, Int32ub))

    # Prime 2 Demo
    if version >= 0x14:
        area_fields.append("internal_area_name" / CString("utf-8"))

    return Struct(*area_fields)


def create(version: int, asset_id):
    area = create_area(version, asset_id)

    fields = [
        "magic" / Const(0xDEAFBABE, Int32ub),
        "version" / Const(version, Int32ub),
        "world_name_id" / asset_id,
    ]

    # Prime 2
    if version == 0x17:
        fields.append("dark_world_name_id" / asset_id)

    # Prime 2 and 3
    if 0x17 <= version <= 0x19:
        fields.append("temple_key_world_index" / Int32ub)

    # TODO: time attack for DKCR

    fields.extend([
        "world_save_info_id" / asset_id,
        "default_skybox_id" / asset_id,
    ])

    # Prime 1
    if version <= 0x11:
        # Array describing all outgoing Memory Relay connections in this world.
        # Memory Relays connected to multiple objects are listed multiple times.
        fields.append("memory_relays" / PrefixedArray(Int32ub, MLVLMemoryRelay))

    # Prime 1
    if version <= 0x11:
        # Extra field is unknown, always 1
        fields.append(
            "areas" / PrefixedArrayWithExtra(Int32ub, Const(1, Int32ub), area)
        )
    else:
        fields.append(
            "areas" / PrefixedArray(Int32ub, area)
        )

    # DKCR
    if version <= 0x1B:
        fields.append("world_map_id" / asset_id)

        # This is presumably the same unknown value as at the beginning of the SCLY format. Always 0.
        fields.append("unknown_scly_field" / Const(0, Int8ub))

        # The MLVL format embeds a script layer. This script layer is used in the MP1 demo for storing Dock instances,
        # but it's unused in all retail builds, so this is always 0.
        fields.append("script_instance_count" / Const(0x0, Int32ub))

    # Prime 1
    if version <= 0x11:
        fields.append(
            "audio_group" / PrefixedArray(Int32ub, Struct(
                group_id=Int32ub,
                agsc_id=asset_id,
            ))
        )

        # Unknown purpose, always empty
        fields.append(CString("utf-8"))

    fields.extend([
        "area_layer_flags" / PrefixedArray(Int32ub, MLVLAreaLayerFlags),
        "layer_names" / PrefixedArray(Int32ub, CString("utf-8")),
    ])

    # Corruption
    if version >= 0x19:
        fields.append("layer_guid" / PrefixedArray(Int32ub, GUID))

    fields.append("area_layer_name_offset" / PrefixedArray(Int32ub, Int32ub))

    return Struct(*fields)


Prime1MLVL = create(0x11, AssetId32)
Prime2MLVL = create(0x17, AssetId32)
Prime3MLVL = create(0x19, AssetId64)

MLVL = FocusedSeq(
    "mlvl",
    header=Peek(Sequence(Int32ub, Int32ub)),
    mlvl=Switch(
        construct.this.header[1],
        {
            0x11: Prime1MLVL,
            0x17: Prime2MLVL,
            0x19: Prime3MLVL,
        },
        construct.Error,
    )
)
