import construct
from construct import Struct, Const, RepeatUntil, Switch, Flag, Int32sb, Float32b, If, Terminated, Sequence, Probe

from retro_data_structures.common_types import FourCC
from retro_data_structures.game_check import AssetIdCorrect

UnknownType = Sequence(Probe(), construct.Error)

GetBool = Struct(
    magic=Const('CNST', FourCC),
    value=Flag,
)
GetInt = Int32sb
GetReal = Float32b

# Real Element

REAL_ELEMENT_TYPES = {
    'CNST': GetReal,
}

GetRealElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, REAL_ELEMENT_TYPES, UnknownType)
)

# Int Element

INT_ELEMENT_TYPES = {
    'CNST': GetInt,
}

GetIntElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, INT_ELEMENT_TYPES, UnknownType)
)

# Vector Element

VECTOR_ELEMENT_TYPES = {
    'CNST': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
    ),
    'ANGC': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetRealElement,
    ),
}

GetVectorElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, VECTOR_ELEMENT_TYPES, UnknownType)
)

# Element Types Post

REAL_ELEMENT_TYPES.update({
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
    'RAND': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'IRND': Struct(
        a=GetRealElement,
        b=GetRealElement,
    ),
    'RLPT': Struct(
        a=GetRealElement,
    )
})
INT_ELEMENT_TYPES.update({
    'RAND': Struct(
        a=GetIntElement,
        b=GetIntElement,
    ),
})
VECTOR_ELEMENT_TYPES.update({
    'CIRC': Struct(
        a=GetVectorElement,
        b=GetVectorElement,
        c=GetRealElement,
        d=GetRealElement,
        e=GetRealElement,
    )
})

# Texture Element

GetTextureElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, {
        'CNST': Struct(
            sub_id=FourCC,
            id=If(lambda ctx: ctx.sub_id != 'NONE', AssetIdCorrect),
        ),
        'ATEX': Struct(
            sub_id=FourCC,
            id=If(lambda ctx: ctx.sub_id != 'NONE', AssetIdCorrect),
            extra=If(lambda ctx: ctx.sub_id != 'NONE', Struct(
                a=GetIntElement,
                b=GetIntElement,
                c=GetIntElement,
                d=GetIntElement,
                e=GetIntElement,
                f=GetBool,
            )),
        ),
    }, UnknownType)
)

# Emitter Element

GetEmitterElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, {
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
    }, UnknownType)
)

# Color Element

CEKeyframeEmitter = construct.Error
CEParticleColor = construct.Error

COLOR_ELEMENT_TYPES = {
    'KEYE': CEKeyframeEmitter,
    'KEYP': CEKeyframeEmitter,
    'CNST': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
        d=GetRealElement,
    ),
    'PCOL': CEParticleColor,
}

GetColorElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, COLOR_ELEMENT_TYPES, UnknownType)
)

COLOR_ELEMENT_TYPES.update({
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
})

# Mod Vector Element

MOD_VECTOR_ELEMENT_TYPES = {}
GetModVectorElement = Struct(
    type=FourCC,
    body=Switch(construct.this.type, MOD_VECTOR_ELEMENT_TYPES, UnknownType)
)

MOD_VECTOR_ELEMENT_TYPES.update({
    'WIND': Struct(
        a=GetVectorElement,
        b=GetRealElement,
    ),
    'GRAV': Struct(
        a=GetVectorElement,
    ),
    'CNST': Struct(
        a=GetRealElement,
        b=GetRealElement,
        c=GetRealElement,
    )
})

# Particle

PARTICLE_TYPES = {
    'OPTS': GetBool,
    'GRTE': GetRealElement,
    'MAXP': GetIntElement,
    'POFS': GetVectorElement,
    'RDOP': GetBool,
    'INDM': GetBool,
    'RSOP': GetBool,
    'ORNT': GetBool,
    'CIND': GetBool,
    'FXLL': GetBool,
    'TEXR': GetTextureElement,
    'TIND': GetTextureElement,
    'MBSP': GetIntElement,
    'MBLR': GetBool,
    'LIT_': GetBool,
    'SORT': GetBool,
    'ZBUF': GetBool,
    'AAPH': GetBool,
    'WIDT': GetRealElement,
    'LENG': GetRealElement,
    'LINE': GetBool,
    'EMTR': GetEmitterElement,
    'SIZE': GetRealElement,
    'LTME': GetIntElement,
    'COLR': GetColorElement,
    'PMOO': GetBool,
    'PMUS': GetBool,
    'PMAB': GetBool,
    'VMPC': GetBool,
    'VMD4': GetBool,
    'VMD3': GetBool,
    'VMD2': GetBool,
    'VMD1': GetBool,
    'VEL4': GetModVectorElement,
    'VEL3': GetModVectorElement,
    'VEL2': GetModVectorElement,
    'VEL1': GetModVectorElement,
    'SISY': GetIntElement,
    'PISY': GetIntElement,
    'NDSY': GetIntElement,
    'NCSY': GetIntElement,
    'LSLA': GetRealElement,
    'LFOR': GetRealElement,
    'LFOT': GetIntElement,
    'LDIR': GetVectorElement,
    'LOFF': GetVectorElement,
    'LINT': GetRealElement,
    'LCLR': GetColorElement,
    'LTYP': GetIntElement,
}

PART = Struct(
    magic=Const('GPSM', FourCC),
    elements=RepeatUntil(
        lambda x, lst, ctx: x.type == '_END',
        Struct(
            type=FourCC,
            body=Switch(construct.this.type, PARTICLE_TYPES)
        )
    ),
    terminated=Terminated,
)


def dependencies_for(obj, target_game):
    for element in obj.elements:
        if element.type in ('TEXR', 'TIND'):
            texture = element.body.body.id
            if texture is not None:
                yield "TXTR", texture
