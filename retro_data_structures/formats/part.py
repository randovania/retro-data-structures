import construct
from construct import Struct, Const, RepeatUntil, Switch, Flag, Int32sb, Float32b, If, Terminated, Sequence, Probe, \
    Pass, IfThenElse, Int32ub, PrefixedArray, Byte, Array

from retro_data_structures import game_check
from retro_data_structures.common_types import FourCC, Color4f, Vector3
from retro_data_structures.construct_extensions import ErrorWithMessage, TerminatedWithPadding, AlignTo
from retro_data_structures.game_check import AssetIdCorrect

UnknownType = Sequence(Probe(into=lambda ctx: ctx["_"]), ErrorWithMessage("Unknown type"))


def FourCCSwitch(element_types):
    return Struct(
        type=FourCC,
        body=Switch(construct.this.type, element_types, UnknownType)
    )


def StartingAtVersion(version, subcon):
    return IfThenElse(
        game_check.get_current_game >= version,
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
    type=IfThenElse(game_check.get_current_game >= 2, FourCC, Int32ub),
    unk2=Int32ub,
    unk3=Int32ub,
)
SpawnSystemKeyframeData = Struct(
    magic=FourCC,
    value=If(
        construct.this.magic == 'CNST',
        Struct(
            unk1=Int32ub,
            unk2=Int32ub,
            endFrame=Int32ub,
            unk3=Int32ub,
            spawns=PrefixedArray(Int32ub, Struct(
                v1=Int32ub,
                v2=PrefixedArray(Int32ub, SpawnSystemKeyframeInfo),
            ))
        ),
    )
)

GetBool = Struct(magic=Const('CNST', FourCC), value=Flag)
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
GetChildGeneratorDesc = Struct(
    type=FourCC,
    body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect)
)
GetModel = Struct(
    type=FourCC,
    body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect)
)
GetSwooshGeneratorDesc = Struct(
    type=FourCC,
    body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect)
)
GetElectricGeneratorDesc = Struct(
    type=FourCC,
    body=IfThenElse(lambda this: this.type == "NONE", Pass, AssetIdCorrect)
)

GetBitFlag = Struct(
    magic1=FourCC,
    magic2=FourCC,
    a=Int32ub,
    body=IfThenElse(
        lambda this: this.magic2 == "BITF",
        Int32ub,
        Array(construct.this.a, Byte),
    )
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

REAL_ELEMENT_TYPES.update({
    'LFTW': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'CNST': GetReal,
    'CHAN': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetIntElement,
    ),
    'ADD_': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'CLMP': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
    ),
    'KEYE': REKeyframeEmitter,
    'KEYP': REKeyframeEmitter,
    'IRND': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'RAND': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'DOTP': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
    ),
    'MULT': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'PULS': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    'SCAL': GetRealElement,
    'RLPT': GetRealElement,
    'SINE': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
    ),
    'ISWT': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'CLTN': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    'CEQL': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    **{k: Pass for k in [f'PAP{i}' for i in range(1, 9)]},
    'PSLL': Pass,
    'PRLW': Pass,
    'SUB_': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'VMAG': GetVectorElement,
    'VXTR': GetVectorElement,
    'VYTR': GetVectorElement,
    'VZTR': GetVectorElement,
    'CEXT': GetIntElement,
    'ITRL': Struct(
        a=GetIntElement,
        b=GetRealElement,
    ),
    'CRNG': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetRealElement,
    ),
    'GTCR': GetColorElement,
    'GTCG': GetColorElement,
    'GTCB': GetColorElement,
    'GTCA': GetColorElement,
    # Prime 1 Complete

    # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
    'NONE': Pass,

    # Prime 2
    'OCSP': StartingAtVersion(2, GetIntElement),
    'GTCP': StartingAtVersion(2, Pass),
    'KEYF': StartingAtVersion(2, RFKeyframeEmitter),
    'KPIN': StartingAtVersion(2, GetRealElement),
    'PNO1': StartingAtVersion(2, Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetIntElement,
    )),
    'PNO2': StartingAtVersion(2, Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetIntElement,
    )),
    'PNO3': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetIntElement,
    )),
    'PNO4': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetIntElement,
    )),
    'PRN1': StartingAtVersion(2, GetRealElement),
    'PRN2': StartingAtVersion(2, Struct(
        a=GetRealElement,
        b=GetRealElement,
    )),
    'PRN3': StartingAtVersion(2, GetVectorElement),
    'PRN4': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetRealElement,
    )),
    'TOCS': StartingAtVersion(2, Struct(
        a=GetBool,
        b=GetIntElement,
        c=GetIntElement,
        d=GetIntElement,
    )),
    # Prime 2 Complete
})
INT_ELEMENT_TYPES.update({
    'KEYE': IEKeyframeEmitter,
    'KEYP': IEKeyframeEmitter,
    'DETH': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'CLMP': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetIntElement,
    ),
    'CHAN': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetIntElement,
    ),
    'ADD_': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'CNST': GetInt,
    'IMPL': GetIntElement,
    'ILPT': GetIntElement,
    'IRND': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'PULS': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetIntElement,
        d=GetIntElement,
    ),
    'MULT': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'DIVD': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'SPAH': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetIntElement,
    ),
    'RAND': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'RTOI': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'TSCL': GetRealElement,
    'GAPC': Pass,
    'GTCP': Pass,
    'GEMT': Pass,
    'MODU': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
    'SUB_': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),

    # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
    'NONE': Pass,

    # Prime 1 Complete
    'KEYF': StartingAtVersion(2, IFKeyframeEmitter),
    'ISWT': StartingAtVersion(2, Struct(
        a=GetIntElement,
        b=GetIntElement,
    )),
    'PDET': StartingAtVersion(2, Pass),
    'KPIN': StartingAtVersion(2, GetIntElement),
    'PCRT': StartingAtVersion(2, Pass),
    # Prime 2 Complete
})
VECTOR_ELEMENT_TYPES.update({
    'CONE': Struct(
        a=GetVectorElement,
        b=GetRealElement,
    ),
    'CHAN': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetIntElement,
    ),
    'ANGC': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetRealElement,
    ),
    'ADD_': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
    ),
    'CCLU': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetIntElement,
        d=GetRealElement,
    ),
    'CNST': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
    ),
    'CIRC': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetRealElement,
    ),
    'KEYE': VEKeyframeEmitter,
    'KEYP': VEKeyframeEmitter,
    'MULT': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
    ),
    'RTOV': GetRealElement,
    'PULS': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetVectorElement,
        d=GetVectorElement,
    ),
    'PVEL': Pass,
    'PLCO': Pass,
    'PLOC': Pass,
    'PSOF': Pass,
    'PSOU': Pass,
    'PSOR': Pass,
    'PSTR': Pass,
    'SUB_': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
    ),
    'CTVC': GetColorElement,
    # Prime 1 Complete

    # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
    'NONE': Pass,

    # Prime 2
    'PENV': StartingAtVersion(2, Pass),
    'ISWT': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetVectorElement,
    )),
    'KEYF': StartingAtVersion(2, VFKeyframeEmitter),
    'KPIN': StartingAtVersion(2, GetVectorElement),
    'PAP1': StartingAtVersion(2, Pass),
    'PAP2': StartingAtVersion(2, Pass),
    'PAP3': StartingAtVersion(2, Pass),
    'PAP4': StartingAtVersion(2, Pass),
    'NORM': StartingAtVersion(2, GetVectorElement),
    'PILV': StartingAtVersion(2, Pass),
    'PINV': StartingAtVersion(2, Pass),
    'PEVL': StartingAtVersion(2, Pass),
    'PNCV': StartingAtVersion(2, Pass),
    'PETR': StartingAtVersion(2, Pass),
    'PITR': StartingAtVersion(2, Pass),
    'RNDV': StartingAtVersion(2, GetRealElement),
})
TEXTURE_ELEMENT_TYPES.update({
    'CNST': Struct(
        sub_id=FourCC,
        id=If(lambda ctx: ctx.sub_id != 'NONE', AssetIdCorrect) * "TXTR",
    ),
    'ATEX': Struct(
        sub_id=FourCC,
        id=If(lambda ctx: ctx.sub_id != 'NONE', AssetIdCorrect) * "TXTR",
        extra=If(lambda ctx: ctx.sub_id != 'NONE', Struct(
            a=GetIntElement,
            b=GetIntElement,
            c=GetIntElement,
            d=GetIntElement,
            e=GetIntElement,
            f=GetBool,
        )),
    ),
    # Prime 1 Complete

    # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
    'NONE': Pass,
    # Prime 2 Complete
})
EMITTER_ELEMENT_TYPES.update({
    'SETR': Struct(
        prop1=FourCC,
        a=If(construct.this.prop1 == 'ILOC', GetVectorElement),
        prop2=If(construct.this.prop1 == 'ILOC', FourCC),
        b=If(construct.this.prop2 == 'IVEC', GetVectorElement),
    ),
    'SEMR': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
    ),
    'SPHE': Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
    ),
    'ASPH': Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetRealElement,
        f=GetRealElement,
        g=GetRealElement,
    ),
    # Prime 1 Complete

    'NONE': Pass,

    # Prime 2
    'PLNE': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetVectorElement,
        d=GetRealElement,
        e=GetRealElement,
        f=GetRealElement,
    )),
    'ELPS': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetVectorElement,
        d=GetRealElement,
        e=GetBool,
    )),

    # Complete
})
COLOR_ELEMENT_TYPES.update({
    'KEYE': CEKeyframeEmitter,
    'KEYP': CEKeyframeEmitter,
    'CNST': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    'CHAN': Struct(
        a=GetColorElement,
        b=GetColorElement,
        c=GetIntElement,
    ),
    'CFDE': Struct(
        a=GetColorElement,
        b=GetColorElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    'FADE': Struct(
        a=GetColorElement,
        b=GetColorElement,
        c=GetRealElement,
    ),
    'PULS': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetColorElement,
        d=GetColorElement,
    ),
    'PCOL': Pass,
    # Prime 1 Complete

    # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
    'NONE': Pass,

    # Prime 2
    'ISWT': StartingAtVersion(2, Struct(
        a=GetColorElement,
        b=GetColorElement,
    )),
    'KEYF': StartingAtVersion(2, CFKeyframeEmitter),
    'MDAO': StartingAtVersion(2, Struct(
        a=GetColorElement,
        b=GetRealElement,
    )),
    'KPIN': StartingAtVersion(2, Struct(
        a=GetColorElement,
    )),
    'MULT': StartingAtVersion(2, Struct(
        a=GetColorElement,
        b=GetColorElement,
    )),
    'VRTC': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetRealElement,
    )),

    # Prime 2 Complete
})
MOD_VECTOR_ELEMENT_TYPES.update({
    'IMPL': Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetBool,
    ),
    'EMPL': Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetBool,
    ),
    'CHAN': Struct(
        a=GetModVectorElement,
        b=GetModVectorElement,
        c=GetIntElement,
    ),
    'BNCE': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetBool,
    ),
    'CNST': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
    ),
    'GRAV': GetVectorElement,
    'EXPL': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'SPOS': GetVectorElement,
    'LMPL': Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetBool,
    ),
    'PULS': Struct(
        a=GetIntElement,
        b=GetIntElement,
        c=GetModVectorElement,
        d=GetModVectorElement,
    ),
    'WIND': Struct(
        a=GetVectorElement,
        b=GetRealElement,
    ),
    'SWRL': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    # Prime 1 Complete

    # Echoes explicitly tracks this value, but it's present in Prime 1 since the parser ignores unknown values
    'NONE': Pass,

    # Prime 2
    'BOXV': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetModVectorElement,
    )),
    'SPHV': StartingAtVersion(2, Struct(
        a=GetVectorElement,
        b=GetRealElement,
        c=GetModVectorElement,
    )),
    # Prime 2 Complete
})

# Particle

PARTICLE_TYPES = {
    'PMCL': GetColorElement,
    'LFOR': GetRealElement,
    'IDTS': GetChildGeneratorDesc,
    'EMTR': GetEmitterElement,
    'COLR': GetColorElement,
    'CIND': GetBool,
    'AAPH': GetBool,
    'CSSD': GetIntElement,
    'GRTE': GetRealElement,
    'FXLL': GetBool,
    'ICTS': GetChildGeneratorDesc,
    'KSSM': SpawnSystemKeyframeData,
    'ILOC': GetVectorElement,
    'IITS': GetChildGeneratorDesc,
    'IVEC': GetVectorElement,
    'LDIR': GetVectorElement,
    'LCLR': GetColorElement,
    'LENG': GetRealElement,
    'MAXP': GetIntElement,
    'LOFF': GetVectorElement,
    'LINT': GetRealElement,
    'LINE': GetBool,
    'LFOT': GetIntElement,
    'LIT_': GetBool,
    'LTME': GetIntElement,
    'LSLA': GetRealElement,
    'LTYP': GetIntElement,
    'NDSY': GetIntElement,
    'MBSP': GetIntElement,
    'MBLR': GetBool,
    'NCSY': GetIntElement,
    'PISY': GetIntElement,
    'OPTS': GetBool,
    'PMAB': GetBool,
    'SESD': GetIntElement,
    'SEPO': GetVectorElement,
    'PSLT': GetIntElement,
    'PMSC': GetVectorElement,
    'PMOP': GetVectorElement,
    'PMDL': GetModel,
    'PMRT': GetVectorElement,
    'POFS': GetVectorElement,
    'PMUS': GetBool,
    'PSIV': GetVectorElement,
    'ROTA': GetRealElement,
    'PSVM': GetModVectorElement,
    'PSTS': GetRealElement,
    'PSOV': GetVectorElement,
    'PSWT': GetIntElement,
    'SEED': GetIntElement,
    'PMOO': GetBool,
    'SSSD': GetIntElement,
    'SORT': GetBool,
    'SIZE': GetRealElement,
    'SISY': GetIntElement,
    'SSPO': GetVectorElement,
    'TEXR': GetTextureElement,
    'SSWH': GetSwooshGeneratorDesc,
    'TIND': GetTextureElement,
    'VMD4': GetBool,
    'VMD3': GetBool,
    'VMD2': GetBool,
    'VMD1': GetBool,
    'VEL4': GetModVectorElement,
    'VEL3': GetModVectorElement,
    'VEL2': GetModVectorElement,
    'VEL1': GetModVectorElement,
    'ZBUF': GetBool,
    'WIDT': GetRealElement,
    'ORNT': GetBool,
    'RSOP': GetBool,
    'ADV1': GetRealElement,
    'ADV2': GetRealElement,
    'ADV3': GetRealElement,
    'ADV4': GetRealElement,
    'ADV5': GetRealElement,
    'ADV6': GetRealElement,
    'ADV7': GetRealElement,
    'ADV8': GetRealElement,
    'SELC': GetElectricGeneratorDesc,

    # Prime 2
    'RDOP': StartingAtVersion(2, GetBool),
    'INDM': StartingAtVersion(2, GetBool),
    'VMPC': StartingAtVersion(2, GetBool),
    'FXBR': StartingAtVersion(2, GetRealElement),
    'FXBO': StartingAtVersion(2, GetVectorElement),
    'PMOV': StartingAtVersion(2, GetVectorElement),
    'VAV1': StartingAtVersion(2, GetVectorElement),
    'VAV2': StartingAtVersion(2, GetVectorElement),
    'VAV3': StartingAtVersion(2, GetVectorElement),
    'XTAD': StartingAtVersion(2, GetIntElement),
    'DFLG': StartingAtVersion(2, GetBitFlag),

    # End
    '_END': Pass,
}

PART = Struct(
    magic=Const('GPSM', FourCC),
    elements=RepeatUntil(
        lambda x, lst, ctx: x.type == '_END',
        FourCCSwitch(PARTICLE_TYPES),
    ),
)


def dependencies_for(obj, target_game):
    for element in obj.elements:
        if element.type in ('TEXR', 'TIND'):
            texture = element.body.body.id
            if texture is not None:
                yield "TXTR", texture

        if element.type == 'KSSM':
            for spawn in element.body.spawns:
                for t in spawn.v2:
                    if target_game >= 2:
                        yield t.type, t.id
                    else:
                        yield 'PART', t.id

        if element.type == 'SSWH':
            if element.body is not None:
                yield 'SWHC', element.body

        if element.type == 'PMDL':
            if element.body is not None:
                yield 'CMDL', element.body

        if element.type == 'SELC':
            if element.body is not None:
                yield 'ELSC', element.body

        if element.type in ('IDTS', 'ICTS', 'IITS'):
            if element.body is not None:
                yield "PART", element.body
