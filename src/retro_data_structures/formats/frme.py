from __future__ import annotations

import enum
from typing import TYPE_CHECKING

import construct
from construct import FixedSized, Flag, Float32b, Int8ub, Int16ub, Int32ub, PrefixedArray, Struct, Switch

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, Color4f, FourCC, ObjectTag_32, String, Vector2f, Vector3
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.construct_extensions.misc import ErrorWithMessage
from retro_data_structures.construct_extensions.version import WithVersion
from retro_data_structures.formats.room import GreedyBytes

if TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures.game_check import Game


class FrmeVersion(enum.IntEnum):
    MP1 = 0
    MP1_PAL = 1
    MP2 = 4
    MP2_JPN = 5


class LightType(enum.IntEnum):
    SPOT = 0
    POINT = 1
    DIRECTIONAL = 2
    LOCAL_AMBIENT = 3
    CUSTOM = 4


class CameraProjection(enum.IntEnum):
    PERSPECTIVE = 0
    ORTHOGRAPHIC = 1


HWIG = construct.Pass
BWIG = construct.Pass
LITE = Struct(
    "light_type" / EnumAdapter(LightType),
    "dist_c" / Float32b,
    "dist_l" / Float32b,
    "dist_q" / Float32b,
    "ang_c" / Float32b,
    "ang_l" / Float32b,
    "ang_q" / Float32b,
    "light_id" / Int32ub,
    "cut_off" / construct.If(construct.this.light_type == LightType.SPOT, Float32b),
)
CAMR = Struct(
    "projection" / EnumAdapter(CameraProjection),
    "inner"
    / construct.Switch(
        construct.this.projection,
        {
            CameraProjection.PERSPECTIVE: Struct(
                "fov" / Float32b,
                "aspect" / Float32b,
                "znear" / Float32b,
                "zfar" / Float32b,
            ),
            CameraProjection.ORTHOGRAPHIC: Struct(
                "left" / Float32b,
                "right" / Float32b,
                "top" / Float32b,
                "bottom" / Float32b,
                "znear" / Float32b,
                "zfar" / Float32b,
            ),
        },
        ErrorWithMessage(lambda ctx: f"unknown projection: {ctx.projection}"),
    ),
)
GRUP = ErrorWithMessage("GRUP Not implemented yet")
PANE = ErrorWithMessage("PANE Not implemented yet")
IMGP = ErrorWithMessage("IMGP Not implemented yet")
METR = Struct(
    "unk1" / Flag,
    "no_round_up" / Flag,
    "max_capacity" / Int32ub,
    "worker_count" / Int32ub,
)
MODL = Struct(
    "cmdl_id" / AssetId32,
    "model_index" / Int32ub,
    "light_mode" / Int32ub,
)
TBGP = Struct(
    "unk1" / Int8ub,
)
SLGP = ErrorWithMessage("SLGP Not implemented yet")
TXPN = Struct(
    "dim" / Vector2f,
    "vec" / Vector3,
    "font_id" / AssetId32,
    "word_wrap" / Int8ub,  # can be 0 to 2, instead of bool. TODO: figure out what each value means
    "unk3" / Int32ub,
    "font_info"
    / Struct(
        "unk1" / Int32ub,
        "unk2" / Int32ub,
        "unk3" / Float32b[4],
        "unk4" / Float32b[4],
        "font_id" / AssetId32,
    )[2],
    "unk4" / Int8ub,
    # TODO: additional fields starting with Echoes JPN
    "unk5" / WithVersion(FrmeVersion.MP2_JPN, Int32ub),
    "unk6" / WithVersion(FrmeVersion.MP2_JPN, Float32b),
    "unk7" / WithVersion(FrmeVersion.MP2_JPN, Int8ub),
)
ENRG = Struct(
    "txtr_id" / AssetId32,
)
BMTR = Struct(
    "coords" / PrefixedArray(Int32ub, Vector3),
    "uvs" / PrefixedArray(Int32ub, Vector2f),
    "txtr_id" / AssetId32,
)

widget_types = {
    "HWIG": HWIG,
    "BWIG": BWIG,
    "LITE": LITE,
    "CAMR": CAMR,
    "GRUP": GRUP,
    "PANE": PANE,
    "IMGP": IMGP,
    "METR": METR,
    "MODL": MODL,
    "TBGP": TBGP,
    "SLGP": SLGP,
    "TXPN": TXPN,
    "ENRG": ENRG,
    "BMTR": BMTR,
}

Widget = Struct(
    "type" / FourCC,
    "name" / String,
    "parent_name" / String,
    "use_anim_controller" / Flag,
    "default_vis" / Flag,
    "default_active" / Flag,
    "cull_faces" / Flag,
    "color" / Color4f,
    "draw_flags" / Int32ub,  # TODO
    "specific"
    / Switch(
        construct.this.type,
        widget_types,
        ErrorWithMessage(lambda ctx: f"Unknown type: {ctx.type}"),
    ),
    "is_worker" / Flag,
    "worker_id" / construct.If(construct.this.is_worker, Int16ub),
    "trans" / Vector3,
    "orient" / Vector3[3],
)

FRME = Struct(
    "version" / EnumAdapter(FrmeVersion),
    "header"
    / Struct(
        "dependencies" / PrefixedArray(Int32ub, ObjectTag_32),
        "alloc_size" / Int32ub,
        "unique_cmdl_count" / Int32ub,
        "section_sizes" / PrefixedArray(Int32ub, Int32ub),
        "blob" / FixedSized(construct.this.alloc_size, GreedyBytes),
    ),
    "widgets" / PrefixedArray(Int32ub, Widget),
    AlignTo(32, b"\xff"),
    construct.Terminated,
)


class Frme(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "FRME"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return FRME

    def dependencies_for(self) -> Iterator[Dependency]:
        for dep in self._raw.header.dependencies:
            yield from self.asset_manager.get_dependencies_for_asset(dep.id)
