import typing
from typing import Optional

import construct
from construct import (
    Const,
    RepeatUntil,
    Switch,
    Flag,
    Int32sb,
    Float32b,
    Sequence,
    Probe,
    Pass,
    IfThenElse,
    Byte,
    Array,
)
from construct import Struct, PrefixedArray, Int32ub, If

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC, Color4f
from retro_data_structures.common_types import Vector3
from retro_data_structures.construct_extensions.misc import ErrorWithMessage
from retro_data_structures.base_resource import BaseResource, AssetType, Dependency
from retro_data_structures.game_check import AssetIdCorrect
from retro_data_structures.game_check import Game

UnknownType = Sequence(Probe(into=lambda ctx: ctx["_"]), ErrorWithMessage("Unknown type"))


def FourCCSwitch(element_types):
    return Struct(type=FourCC, body=Switch(construct.this.type, element_types, UnknownType))


def StartingAtVersion(version: Game, subcon):
    return IfThenElse(
        game_check.current_game_at_least(version),
        subcon,
        ErrorWithMessage(f"Type only supported starting at version {version}"),
    )


def create_keyframe_emitter(keys_type):
    return Struct(
        percent=Int32ub,
        unk1=Int32ub,
        loop=Flag,
        unk2=Flag,
        loopEnd=Int32ub,
        loopStart=Int32ub,
        keys=PrefixedArray(Int32ub, keys_type),
    )


# Subtypes
CEKeyframeEmitter = create_keyframe_emitter(Color4f)
REKeyframeEmitter = create_keyframe_emitter(Float32b)
VEKeyframeEmitter = create_keyframe_emitter(Vector3)
IEKeyframeEmitter = create_keyframe_emitter(Int32sb)

SpawnSystemKeyframeInfo = Struct(
    id=AssetIdCorrect,
    type=IfThenElse(game_check.current_game_at_least(Game.ECHOES), FourCC, Int32ub),
    unk2=Int32ub,
    unk3=Int32ub,
)
SpawnSystemKeyframeData = Struct(
    magic=FourCC,
    value=If(
        construct.this.magic == "CNST",
        Struct(
            unk1=Int32ub,
            unk2=Int32ub,
            endFrame=Int32ub,
            unk3=Int32ub,
            spawns=PrefixedArray(
                Int32ub,
                Struct(
                    v1=Int32ub,
                    v2=PrefixedArray(Int32ub, SpawnSystemKeyframeInfo),
                ),
            ),
        ),
    ),
)

GetBool = Struct(magic=Const("CNST", FourCC), value=Flag)
GetInt = Int32sb
GetReal = Float32b

# Element Types Declarations

REAL_ELEMENT_TYPES = {}
INT_ELEMENT_TYPES = {}
VECTOR_ELEMENT_TYPES = {}
TEXTURE_ELEMENT_TYPES = {}
EMITTER_ELEMENT_TYPES = {}
COLOR_ELEMENT_TYPES = {}
MOD_VECTOR_ELEMENT_TYPES = {}

GetRealElement = FourCCSwitch(REAL_ELEMENT_TYPES)
GetIntElement = FourCCSwitch(INT_ELEMENT_TYPES)
GetVectorElement = FourCCSwitch(VECTOR_ELEMENT_TYPES)
GetTextureElement = FourCCSwitch(TEXTURE_ELEMENT_TYPES)
GetEmitterElement = FourCCSwitch(EMITTER_ELEMENT_TYPES)
GetColorElement = FourCCSwitch(COLOR_ELEMENT_TYPES)
GetModVectorElement = FourCCSwitch(MOD_VECTOR_ELEMENT_TYPES)
GetChildGeneratorDesc = Struct(type=FourCC, body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect))
GetModel = Struct(type=FourCC, body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect))
GetSwooshGeneratorDesc = Struct(type=FourCC, body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect))
GetElectricGeneratorDesc = Struct(type=FourCC, body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect))

GetBitFlag = Struct(
    magic1=FourCC,
    magic2=FourCC,
    a=Int32ub,
    body=IfThenElse(
        lambda this: this.magic2 == "BITF",
        Int32ub,
        Array(construct.this.a, Byte),
    ),
)


#


def create_keyf_emitter(keys_type):
    return Struct(
        a=Int32ub,
        b=Int32ub,
        c=Flag,
        d=Flag,
        e=Int32ub,
        f=Int32ub,
        g=Float32b,
        h=Float32b,
        keys=PrefixedArray(Int32ub, keys_type),
        i=GetRealElement,
    )


CFKeyframeEmitter = create_keyf_emitter(Color4f)
IFKeyframeEmitter = create_keyf_emitter(Int32ub)
RFKeyframeEmitter = create_keyf_emitter(Float32b)
VFKeyframeEmitter = create_keyf_emitter(Vector3)

# Element Types Post

REAL_ELEMENT_TYPES.update(
    {
        "LFTW": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "CNST": GetReal,
        "CHAN": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetIntElement,
        ),
        "ADD_": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "CLMP": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
        ),
        "KEYE": REKeyframeEmitter,
        "KEYP": REKeyframeEmitter,
        "IRND": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "RAND": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "DOTP": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
        ),
        "MULT": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "PULS": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetRealElement,
            d=GetRealElement,
        ),
        "SCAL": GetRealElement,
        "RLPT": GetRealElement,
        "SINE": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
        ),
        "ISWT": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "CLTN": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
        ),
        "CEQL": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
        ),
        **{k: Pass for k in [f"PAP{i}" for i in range(1, 9)]},
        "PSLL": Pass,
        "PRLW": Pass,
        "SUB_": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "VMAG": GetVectorElement,
        "VXTR": GetVectorElement,
        "VYTR": GetVectorElement,
        "VZTR": GetVectorElement,
        "CEXT": GetIntElement,
        "ITRL": Struct(
            a=GetIntElement,
            b=GetRealElement,
        ),
        "CRNG": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetRealElement,
        ),
        "GTCR": GetColorElement,
        "GTCG": GetColorElement,
        "GTCB": GetColorElement,
        "GTCA": GetColorElement,
        # Prime 1 Complete
        # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
        "NONE": Pass,
        # Prime 2
        "OCSP": StartingAtVersion(Game.ECHOES, GetIntElement),
        "GTCP": StartingAtVersion(Game.ECHOES, Pass),
        "KEYF": StartingAtVersion(Game.ECHOES, RFKeyframeEmitter),
        "KPIN": StartingAtVersion(Game.ECHOES, GetRealElement),
        "PNO1": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetRealElement,
                b=GetRealElement,
                c=GetRealElement,
                d=GetIntElement,
            ),
        ),
        "PNO2": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetRealElement,
                b=GetRealElement,
                c=GetRealElement,
                d=GetRealElement,
                e=GetIntElement,
            ),
        ),
        "PNO3": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetRealElement,
                c=GetRealElement,
                d=GetIntElement,
            ),
        ),
        "PNO4": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetRealElement,
                c=GetRealElement,
                d=GetRealElement,
                e=GetIntElement,
            ),
        ),
        "PRN1": StartingAtVersion(Game.ECHOES, GetRealElement),
        "PRN2": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetRealElement,
                b=GetRealElement,
            ),
        ),
        "PRN3": StartingAtVersion(Game.ECHOES, GetVectorElement),
        "PRN4": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetRealElement,
            ),
        ),
        "TOCS": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetBool,
                b=GetIntElement,
                c=GetIntElement,
                d=GetIntElement,
            ),
        ),
        # Prime 2 Complete
        # Prime 3
        "PAP9": StartingAtVersion(Game.CORRUPTION, Pass),
    }
)
INT_ELEMENT_TYPES.update(
    {
        "KEYE": IEKeyframeEmitter,
        "KEYP": IEKeyframeEmitter,
        "DETH": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "CLMP": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetIntElement,
        ),
        "CHAN": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetIntElement,
        ),
        "ADD_": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "CNST": GetInt,
        "IMPL": GetIntElement,
        "ILPT": GetIntElement,
        "IRND": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "PULS": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetIntElement,
            d=GetIntElement,
        ),
        "MULT": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "DIVD": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "SPAH": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetIntElement,
        ),
        "RAND": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "RTOI": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "TSCL": GetRealElement,
        "GAPC": Pass,
        "GTCP": Pass,
        "GEMT": Pass,
        "MODU": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        "SUB_": Struct(
            a=GetIntElement,
            b=GetIntElement,
        ),
        # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
        "NONE": Pass,
        # Prime 1 Complete
        "KEYF": StartingAtVersion(Game.ECHOES, IFKeyframeEmitter),
        "ISWT": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetIntElement,
                b=GetIntElement,
            ),
        ),
        "PDET": StartingAtVersion(Game.ECHOES, Pass),
        "KPIN": StartingAtVersion(Game.ECHOES, GetIntElement),
        "PCRT": StartingAtVersion(Game.ECHOES, Pass),
        # Prime 2 Complete
    }
)
VECTOR_ELEMENT_TYPES.update(
    {
        "CONE": Struct(
            a=GetVectorElement,
            b=GetRealElement,
        ),
        "CHAN": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
            c=GetIntElement,
        ),
        "ANGC": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetRealElement,
        ),
        "ADD_": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
        ),
        "CCLU": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
            c=GetIntElement,
            d=GetRealElement,
        ),
        "CNST": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
        ),
        "CIRC": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetRealElement,
        ),
        "KEYE": VEKeyframeEmitter,
        "KEYP": VEKeyframeEmitter,
        "MULT": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
        ),
        "RTOV": GetRealElement,
        "PULS": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetVectorElement,
            d=GetVectorElement,
        ),
        "PVEL": Pass,
        "PLCO": Pass,
        "PLOC": Pass,
        "PSOF": Pass,
        "PSOU": Pass,
        "PSOR": Pass,
        "PSTR": Pass,
        "SUB_": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
        ),
        "CTVC": GetColorElement,
        # Prime 1 Complete
        # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
        "NONE": Pass,
        # Prime 2
        "PENV": StartingAtVersion(Game.ECHOES, Pass),
        "ISWT": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetVectorElement,
            ),
        ),
        "KEYF": StartingAtVersion(Game.ECHOES, VFKeyframeEmitter),
        "KPIN": StartingAtVersion(Game.ECHOES, GetVectorElement),
        "PAP1": StartingAtVersion(Game.ECHOES, Pass),
        "PAP2": StartingAtVersion(Game.ECHOES, Pass),
        "PAP3": StartingAtVersion(Game.ECHOES, Pass),
        "PAP4": StartingAtVersion(Game.ECHOES, Pass),
        "NORM": StartingAtVersion(Game.ECHOES, GetVectorElement),
        "PILV": StartingAtVersion(Game.ECHOES, Pass),
        "PINV": StartingAtVersion(Game.ECHOES, Pass),
        "PEVL": StartingAtVersion(Game.ECHOES, Pass),
        "PNCV": StartingAtVersion(Game.ECHOES, Pass),
        "PETR": StartingAtVersion(Game.ECHOES, Pass),
        "PITR": StartingAtVersion(Game.ECHOES, Pass),
        "RNDV": StartingAtVersion(Game.ECHOES, GetRealElement),
    }
)
TEXTURE_ELEMENT_TYPES.update(
    {
        "CNST": Struct(
            sub_id=FourCC,
            id=If(lambda ctx: ctx.sub_id != "NONE", AssetIdCorrect) * "TXTR",
        ),
        "ATEX": Struct(
            sub_id=FourCC,
            id=If(lambda ctx: ctx.sub_id != "NONE", AssetIdCorrect) * "TXTR",
            extra=If(
                lambda ctx: ctx.sub_id != "NONE",
                Struct(
                    a=GetIntElement,
                    b=GetIntElement,
                    c=GetIntElement,
                    d=GetIntElement,
                    e=GetIntElement,
                    f=GetBool,
                ),
            ),
        ),
        # Prime 1 Complete
        # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
        "NONE": Pass,
        # Prime 2 Complete
        # Prime 3
        "TEXP": StartingAtVersion(
            Game.CORRUPTION,
            Struct(
                sub_id=FourCC,
                id=If(lambda ctx: ctx.sub_id != "NONE", AssetIdCorrect) * "TXTR",
                a=GetIntElement,
                b=GetIntElement,
                c=GetRealElement,
            ),
        ),
    }
)
EMITTER_ELEMENT_TYPES.update(
    {
        "SETR": Struct(
            prop1=FourCC,
            a=If(construct.this.prop1 == "ILOC", GetVectorElement),
            prop2=If(construct.this.prop1 == "ILOC", FourCC),
            b=If(construct.this.prop2 == "IVEC", GetVectorElement),
        ),
        "SEMR": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
        ),
        "SPHE": Struct(
            a=GetVectorElement,
            b=GetRealElement,
            c=GetRealElement,
        ),
        "ASPH": Struct(
            a=GetVectorElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetRealElement,
            f=GetRealElement,
            g=GetRealElement,
        ),
        # Prime 1 Complete
        "NONE": Pass,
        # Prime 2
        "PLNE": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetVectorElement,
                c=GetVectorElement,
                d=GetRealElement,
                e=GetRealElement,
                f=GetRealElement,
            ),
        ),
        "ELPS": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetVectorElement,
                c=GetVectorElement,
                d=GetRealElement,
                e=GetBool,
            ),
        ),
        # Complete
    }
)
COLOR_ELEMENT_TYPES.update(
    {
        "KEYE": CEKeyframeEmitter,
        "KEYP": CEKeyframeEmitter,
        "CNST": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
        ),
        "CHAN": Struct(
            a=GetColorElement,
            b=GetColorElement,
            c=GetIntElement,
        ),
        "CFDE": Struct(
            a=GetColorElement,
            b=GetColorElement,
            c=GetRealElement,
            d=GetRealElement,
        ),
        "FADE": Struct(
            a=GetColorElement,
            b=GetColorElement,
            c=GetRealElement,
        ),
        "PULS": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetColorElement,
            d=GetColorElement,
        ),
        "PCOL": Pass,
        # Prime 1 Complete
        # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
        "NONE": Pass,
        # Prime 2
        "ISWT": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetColorElement,
                b=GetColorElement,
            ),
        ),
        "KEYF": StartingAtVersion(Game.ECHOES, CFKeyframeEmitter),
        "MDAO": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetColorElement,
                b=GetRealElement,
            ),
        ),
        "KPIN": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetColorElement,
            ),
        ),
        "MULT": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetColorElement,
                b=GetColorElement,
            ),
        ),
        "VRTC": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetRealElement,
            ),
        ),
        # Prime 2 Complete
        # Prime 3
        "CFDL": StartingAtVersion(
            Game.CORRUPTION,
            Struct(
                a=GetColorElement,
                b=GetColorElement,
            ),
        ),
    }
)
MOD_VECTOR_ELEMENT_TYPES.update(
    {
        "IMPL": Struct(
            a=GetVectorElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetBool,
        ),
        "EMPL": Struct(
            a=GetVectorElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetBool,
        ),
        "CHAN": Struct(
            a=GetModVectorElement,
            b=GetModVectorElement,
            c=GetIntElement,
        ),
        "BNCE": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetBool,
        ),
        "CNST": Struct(
            a=GetRealElement,
            b=GetRealElement,
            c=GetRealElement,
        ),
        "GRAV": GetVectorElement,
        "EXPL": Struct(
            a=GetRealElement,
            b=GetRealElement,
        ),
        "SPOS": GetVectorElement,
        "LMPL": Struct(
            a=GetVectorElement,
            b=GetRealElement,
            c=GetRealElement,
            d=GetRealElement,
            e=GetBool,
        ),
        "PULS": Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetModVectorElement,
            d=GetModVectorElement,
        ),
        "WIND": Struct(
            a=GetVectorElement,
            b=GetRealElement,
        ),
        "SWRL": Struct(
            a=GetVectorElement,
            b=GetVectorElement,
            c=GetRealElement,
            d=GetRealElement,
        ),
        # Prime 1 Complete
        # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
        "NONE": Pass,
        # Prime 2
        "BOXV": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetVectorElement,
                c=GetModVectorElement,
            ),
        ),
        "SPHV": StartingAtVersion(
            Game.ECHOES,
            Struct(
                a=GetVectorElement,
                b=GetRealElement,
                c=GetModVectorElement,
            ),
        ),
        # Prime 2 Complete
        # Prime 3
        "SWLC": StartingAtVersion(
            Game.CORRUPTION,
            Struct(
                a=GetRealElement,
                b=GetRealElement,
            ),
        ),
    }
)

# Particle

PARTICLE_TYPES = {
    "PMCL": GetColorElement,
    "LFOR": GetRealElement,
    "IDTS": GetChildGeneratorDesc,
    "EMTR": GetEmitterElement,
    "COLR": GetColorElement,
    "CIND": GetBool,
    "AAPH": GetBool,
    "CSSD": GetIntElement,
    "GRTE": GetRealElement,
    "FXLL": GetBool,
    "ICTS": GetChildGeneratorDesc,
    "KSSM": SpawnSystemKeyframeData,
    "ILOC": GetVectorElement,
    "IITS": GetChildGeneratorDesc,
    "IVEC": GetVectorElement,
    "LDIR": GetVectorElement,
    "LCLR": GetColorElement,
    "LENG": GetRealElement,
    "MAXP": GetIntElement,
    "LOFF": GetVectorElement,
    "LINT": GetRealElement,
    "LINE": GetBool,
    "LFOT": GetIntElement,
    "LIT_": GetBool,
    "LTME": GetIntElement,
    "LSLA": GetRealElement,
    "LTYP": GetIntElement,
    "NDSY": GetIntElement,
    "MBSP": GetIntElement,
    "MBLR": GetBool,
    "NCSY": GetIntElement,
    "PISY": GetIntElement,
    "OPTS": GetBool,
    "PMAB": GetBool,
    "SESD": GetIntElement,
    "SEPO": GetVectorElement,
    "PSLT": GetIntElement,
    "PMSC": GetVectorElement,
    "PMOP": GetVectorElement,
    "PMDL": GetModel,
    "PMRT": GetVectorElement,
    "POFS": GetVectorElement,
    "PMUS": GetBool,
    "PSIV": GetVectorElement,
    "ROTA": GetRealElement,
    "PSVM": GetModVectorElement,
    "PSTS": GetRealElement,
    "PSOV": GetVectorElement,
    "PSWT": GetIntElement,
    "SEED": GetIntElement,
    "PMOO": GetBool,
    "SSSD": GetIntElement,
    "SORT": GetBool,
    "SIZE": GetRealElement,
    "SISY": GetIntElement,
    "SSPO": GetVectorElement,
    "TEXR": GetTextureElement,
    "SSWH": GetSwooshGeneratorDesc,
    "TIND": GetTextureElement,
    "VMD4": GetBool,
    "VMD3": GetBool,
    "VMD2": GetBool,
    "VMD1": GetBool,
    "VEL4": GetModVectorElement,
    "VEL3": GetModVectorElement,
    "VEL2": GetModVectorElement,
    "VEL1": GetModVectorElement,
    "ZBUF": GetBool,
    "WIDT": GetRealElement,
    "ORNT": GetBool,
    "RSOP": GetBool,
    "ADV1": GetRealElement,
    "ADV2": GetRealElement,
    "ADV3": GetRealElement,
    "ADV4": GetRealElement,
    "ADV5": GetRealElement,
    "ADV6": GetRealElement,
    "ADV7": GetRealElement,
    "ADV8": GetRealElement,
    "SELC": GetElectricGeneratorDesc,
    # Prime 2
    "RDOP": StartingAtVersion(Game.ECHOES, GetBool),
    "INDM": StartingAtVersion(Game.ECHOES, GetBool),
    "VMPC": StartingAtVersion(Game.ECHOES, GetBool),
    "FXBR": StartingAtVersion(Game.ECHOES, GetRealElement),
    "FXBO": StartingAtVersion(Game.ECHOES, GetVectorElement),
    "PMOV": StartingAtVersion(Game.ECHOES, GetVectorElement),
    "VAV1": StartingAtVersion(Game.ECHOES, GetVectorElement),
    "VAV2": StartingAtVersion(Game.ECHOES, GetVectorElement),
    "VAV3": StartingAtVersion(Game.ECHOES, GetVectorElement),
    "XTAD": StartingAtVersion(Game.ECHOES, GetIntElement),
    "DFLG": StartingAtVersion(Game.ECHOES, GetBitFlag),
    # Prime 3
    "STOP": StartingAtVersion(Game.CORRUPTION, GetBool),
    "PBDM": StartingAtVersion(Game.CORRUPTION, GetIntElement),
    "PMLT": StartingAtVersion(Game.CORRUPTION, GetBool),
    "MBDM": StartingAtVersion(Game.CORRUPTION, GetIntElement),
    "VGD1": StartingAtVersion(Game.CORRUPTION, GetBool),
    "VGD2": StartingAtVersion(Game.CORRUPTION, GetBool),
    "VGD3": StartingAtVersion(Game.CORRUPTION, GetBool),
    "VGD4": StartingAtVersion(Game.CORRUPTION, GetBool),
    "ALSC": StartingAtVersion(Game.CORRUPTION, GetIntElement),
    "DBPS": StartingAtVersion(Game.CORRUPTION, GetBool),
    "SVEO": StartingAtVersion(Game.CORRUPTION, GetRealElement),
    "ORTC": StartingAtVersion(Game.CORRUPTION, GetBool),
    "ISVF": StartingAtVersion(Game.CORRUPTION, GetRealElement),
    "ADV9": StartingAtVersion(Game.CORRUPTION, GetRealElement),
    "AMSC": StartingAtVersion(Game.CORRUPTION, GetIntElement),
    "XJAK": StartingAtVersion(Game.CORRUPTION, GetIntElement),
    "EADV": StartingAtVersion(Game.CORRUPTION, GetRealElement),
    "PMTF": StartingAtVersion(Game.CORRUPTION, GetBool),
    "HJAK": StartingAtVersion(Game.CORRUPTION, GetIntElement),
    # End
    "_END": Pass,
}

PART = Struct(
    magic=Const("GPSM", FourCC),
    elements=RepeatUntil(
        lambda x, lst, ctx: x.type == "_END",
        FourCCSwitch(PARTICLE_TYPES),
    ),
)


def _yield_dependency_if_valid(asset_id: Optional[int], asset_type: str, game: Game):
    if asset_id is not None and game.is_valid_asset_id(asset_id):
        yield asset_type, asset_id


def dependencies_for(obj, target_game: Game):
    for element in obj.elements:
        if element.type in ("TEXR", "TIND"):
            if element.body.body is not None:
                yield from _yield_dependency_if_valid(element.body.body.id, "TXTR", target_game)

        if element.type == "KSSM":
            if element.body.magic != "NONE":
                for spawn in element.body.value.spawns:
                    for t in spawn.v2:
                        yield from _yield_dependency_if_valid(
                            t.id,
                            t.type if target_game >= Game.ECHOES else "PART",
                            target_game,
                        )

        if element.type == "SSWH":
            if element.body is not None:
                yield from _yield_dependency_if_valid(element.body.body, "SWHC", target_game)

        if element.type == "PMDL":
            if element.body is not None:
                yield from _yield_dependency_if_valid(element.body.body, "CMDL", target_game)

        if element.type == "SELC":
            if element.body is not None:
                yield from _yield_dependency_if_valid(element.body.body, "ELSC", target_game)

        if element.type in ("IDTS", "ICTS", "IITS"):
            if element.body is not None:
                yield from _yield_dependency_if_valid(element.body.body, "PART", target_game)


class Part(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "PART"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return PART

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from dependencies_for(self.raw, self.target_game)
