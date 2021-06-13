import construct
from construct import Struct, Array, PrefixedArray, Const, Int8ub, Int16ub, Int32ub, Float32b, If, \
    IfThenElse, BitStruct, GreedyBytes, BitsInteger

from retro_data_structures import game_check
from retro_data_structures.common_types import CharAnimTime

UncompressedAnimation = Struct(
    duration=CharAnimTime,
    key_interval=CharAnimTime,
    key_count=Int32ub,
    root_bone_id=Int32ub,
    bone_channel_index_array=PrefixedArray(Const(0x64, Int32ub), Int8ub),
    rotation_channel_index_array=If(game_check.is_prime2, PrefixedArray(Int32ub, Int8ub)),
    translation_channel_index_array=PrefixedArray(Int32ub, Int8ub),
    scale_channel_index_array=If(game_check.is_prime2, PrefixedArray(Int32ub, Int8ub)),
    scale_key_array=If(game_check.is_prime2, PrefixedArray(Int32ub, Array(3, Float32b))),
    rotation_key_array=PrefixedArray(Int32ub, Array(4, Float32b)),
    translation_key_array=PrefixedArray(Int32ub, Array(3, Float32b)),
    event_id=If(game_check.is_prime1, Int32ub),
)

def ReadCompressedAnimData(keyCount):
    BoneChannelBits = Struct(
        "initial_x" / Int16ub,
        "delta_x" / Int8ub,
        "initial_y" / Int16ub,
        "delta_y" / Int8ub,
        "initial_z" / Int16ub,
        "delta_z" / Int8ub,
    )

    BoneChannelDescriptor = Struct(
        "bone_id" / IfThenElse(game_check.is_prime2, Int8ub, Int32ub),
        "rotation_keys_count" / Int16ub,
        "rotation_keys" / If(construct.this.rotation_keys_count != 0, BoneChannelBits),
        "translation_keys_count" / Int16ub,
        "translation_keys" / If(construct.this.translation_keys_count != 0, BoneChannelBits),
        "scale_keys_count" / If(game_check.is_prime2, Int16ub),
        "scale_keys" / If(game_check.is_prime2, If(construct.this.scale_keys_count != 0, BoneChannelBits)),
    )

    bone_channel_descriptor_table = PrefixedArray(Int32ub, BoneChannelDescriptor)
    for i in keyCount:
        if construct.this.bone_channel_descriptor_table[i].rotation_keys_count > 0:
            rotation_bit_struct=BitStruct(
                                "w" / BitsInteger(1),
                                "x" / BitsInteger(construct.this.bone_channel_descriptor_table[i].rotation_keys.delta_x),
                                "y" / BitsInteger(construct.this.bone_channel_descriptor_table[i].rotation_keys.delta_y),
                                "z" / BitsInteger(construct.this.bone_channel_descriptor_table[i].rotation_keys.delta_z),
            )
        if construct.this.bone_channel_descriptor_table[i].translation_keys_count > 0:
            translation_bit_struct=BitStruct(
                                "x" / BitsInteger(construct.this.bone_channel_descriptor_table[i].translation_keys.delta_x),
                                "y" / BitsInteger(construct.this.bone_channel_descriptor_table[i].translation_keys.delta_y),
                                "z" / BitsInteger(construct.this.bone_channel_descriptor_table[i].translation_keys.delta_z),
            )
        if construct.this.bone_channel_descriptor_table[i].scale_keys_count > 0:
            scale_bit_struct=BitStruct(
                                "x" / BitsInteger(construct.this.bone_channel_descriptor_table[i].scale_keys.delta_x),
                                "y" / BitsInteger(construct.this.bone_channel_descriptor_table[i].scale_keys.delta_y),
                                "z" / BitsInteger(construct.this.bone_channel_descriptor_table[i].scale_keys.delta_z),
            )

CompressedAnimation = Struct(
    scratch_size=Int32ub,
    event_id=If(game_check.is_prime1, Int32ub),
    unk_1=If(game_check.is_prime1, Const(0x00000001, Int32ub)),
    unk_2=If(game_check.is_prime2, Const(0x0101, Int16ub)),
    duration=Float32b,
    interval=Float32b,
    root_bone_id=Int32ub,
    looping_flag=Int32ub,
    rotation_divisor=Int32ub,
    translation_multiplier=Float32b,
    scale_multiplier=If(game_check.is_prime2, Float32b),
    bone_channel_count=Int32ub,
    unk_3=Int32ub,
    key_bitmap_count=Int32ub,
    key_bitmap_array=Array(-(construct.this.key_bitmap_count // -32), Int32ub),
    bone_channel_count_2=If(game_check.is_prime1, Int32ub),
    key_bitstream=ReadCompressedAnimData(construct.this.key_bitmap_count),
)

ANIM = Struct(
    anim_version=Int32ub,
    anim=IfThenElse(construct.this.anim_version == 0x00000000, UncompressedAnimation, CompressedAnimation),
)
