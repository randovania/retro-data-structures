# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SafeZoneCrystalJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_parameters: json_util.JsonObject
        scannable_info_collapsed: int
        scannable_info_entangled: int
        scannable_info_light: int
        scannable_info_annihilator: int
        safezone_type: int
        initially_entangled: bool
        collapsed_effect: int
        expanded_effect: int
        entangled_effect: int
        part: int
        echo_effect: int
        normal_crystal: int
        entangled_crystal: int
        energized_model: int
        echo_crystal: int
        max_time_expanded: float
        max_time_entangled: float
        unknown_0xf0a45c32: float
        unknown_0xd8116003: float
        unknown_0x415046ed: float
        unknown_0xec9c01b2: float
        unknown_0x545540e5: float
        power_beam_refresh_effect: int
        hit_radius: json_util.JsonValue
        hit_offset: json_util.JsonValue
        effect_offset: json_util.JsonValue
        unknown_0xbbbee60b: json_util.JsonObject


@dataclasses.dataclass()
class SafeZoneCrystal(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    actor_parameters: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0xD29C031D,
                original_name="ActorParameters",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    scannable_info_collapsed: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9B8B3323, original_name="ScannableInfoCollapsed"),
        },
    )
    scannable_info_entangled: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE36E20A7, original_name="ScannableInfoEntangled"),
        },
    )
    scannable_info_light: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAC794DA8, original_name="ScannableInfoLight"),
        },
    )
    scannable_info_annihilator: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC21F264F, original_name="ScannableInfoAnnihilator"),
        },
    )
    safezone_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1115FB68, original_name="SafezoneType"),
        },
    )
    initially_entangled: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA0D9E87F, original_name="InitiallyEntangled"),
        },
    )
    collapsed_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x42A046C2, original_name="CollapsedEffect"),
        },
    )
    expanded_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5B91FF38, original_name="ExpandedEffect"),
        },
    )
    entangled_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5B8275BC, original_name="EntangledEffect"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xADACEC90, original_name="PART"),
        },
    )
    echo_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0D2E4AD3, original_name="EchoEffect"),
        },
    )
    normal_crystal: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x71EFFFC4, original_name="NormalCrystal"),
        },
    )
    entangled_crystal: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC3DD9B75, original_name="EntangledCrystal"),
        },
    )
    energized_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF1F3D90F, original_name="Energized Model"),
        },
    )
    echo_crystal: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1E864B83, original_name="EchoCrystal"),
        },
    )
    max_time_expanded: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBD30F7A3, original_name="MaxTimeExpanded"),
        },
    )
    max_time_entangled: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA7BDC4F8, original_name="MaxTimeEntangled"),
        },
    )
    unknown_0xf0a45c32: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0A45C32, original_name="Unknown"),
        },
    )
    unknown_0xd8116003: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD8116003, original_name="Unknown"),
        },
    )
    unknown_0x415046ed: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x415046ED, original_name="Unknown"),
        },
    )
    unknown_0xec9c01b2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC9C01B2, original_name="Unknown"),
        },
    )
    unknown_0x545540e5: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x545540E5, original_name="Unknown"),
        },
    )
    power_beam_refresh_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5490E214, original_name="PowerBeamRefreshEffect"),
        },
    )
    hit_radius: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x887E8A8B, original_name="HitRadius", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    hit_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0xB7F5646D, original_name="HitOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    effect_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x41B72B2C, original_name="EffectOffset", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown_0xbbbee60b: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xBBBEE60B, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SFZC"

    @classmethod
    def modules(cls) -> list[str]:
        return ["ScriptSafeZone.rel"]

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 29:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD29C031D
        actor_parameters = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B8B3323
        scannable_info_collapsed = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE36E20A7
        scannable_info_entangled = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC794DA8
        scannable_info_light = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC21F264F
        scannable_info_annihilator = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1115FB68
        safezone_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0D9E87F
        initially_entangled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42A046C2
        collapsed_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B91FF38
        expanded_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B8275BC
        entangled_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xADACEC90
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D2E4AD3
        echo_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71EFFFC4
        normal_crystal = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3DD9B75
        entangled_crystal = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1F3D90F
        energized_model = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1E864B83
        echo_crystal = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD30F7A3
        max_time_expanded = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA7BDC4F8
        max_time_entangled = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0A45C32
        unknown_0xf0a45c32 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8116003
        unknown_0xd8116003 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x415046ED
        unknown_0x415046ed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEC9C01B2
        unknown_0xec9c01b2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x545540E5
        unknown_0x545540e5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5490E214
        power_beam_refresh_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x887E8A8B
        hit_radius = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7F5646D
        hit_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41B72B2C
        effect_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBBBEE60B
        unknown_0xbbbee60b = Spline.from_stream(data, game, property_size)

        return cls(
            editor_properties,
            actor_parameters,
            scannable_info_collapsed,
            scannable_info_entangled,
            scannable_info_light,
            scannable_info_annihilator,
            safezone_type,
            initially_entangled,
            collapsed_effect,
            expanded_effect,
            entangled_effect,
            part,
            echo_effect,
            normal_crystal,
            entangled_crystal,
            energized_model,
            echo_crystal,
            max_time_expanded,
            max_time_entangled,
            unknown_0xf0a45c32,
            unknown_0xd8116003,
            unknown_0x415046ed,
            unknown_0xec9c01b2,
            unknown_0x545540e5,
            power_beam_refresh_effect,
            hit_radius,
            hit_offset,
            effect_offset,
            unknown_0xbbbee60b,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x1d")  # 29 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd2\x9c\x03\x1d")  # 0xd29c031d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_parameters.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9b\x8b3#")  # 0x9b8b3323
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scannable_info_collapsed))

        data.write(b"\xe3n \xa7")  # 0xe36e20a7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scannable_info_entangled))

        data.write(b"\xacyM\xa8")  # 0xac794da8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scannable_info_light))

        data.write(b"\xc2\x1f&O")  # 0xc21f264f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scannable_info_annihilator))

        data.write(b"\x11\x15\xfbh")  # 0x1115fb68
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.safezone_type))

        data.write(b"\xa0\xd9\xe8\x7f")  # 0xa0d9e87f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.initially_entangled))

        data.write(b"B\xa0F\xc2")  # 0x42a046c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.collapsed_effect))

        data.write(b"[\x91\xff8")  # 0x5b91ff38
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.expanded_effect))

        data.write(b"[\x82u\xbc")  # 0x5b8275bc
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.entangled_effect))

        data.write(b"\xad\xac\xec\x90")  # 0xadacec90
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b"\r.J\xd3")  # 0xd2e4ad3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.echo_effect))

        data.write(b"q\xef\xff\xc4")  # 0x71efffc4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.normal_crystal))

        data.write(b"\xc3\xdd\x9bu")  # 0xc3dd9b75
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.entangled_crystal))

        data.write(b"\xf1\xf3\xd9\x0f")  # 0xf1f3d90f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.energized_model))

        data.write(b"\x1e\x86K\x83")  # 0x1e864b83
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.echo_crystal))

        data.write(b"\xbd0\xf7\xa3")  # 0xbd30f7a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_time_expanded))

        data.write(b"\xa7\xbd\xc4\xf8")  # 0xa7bdc4f8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_time_entangled))

        data.write(b"\xf0\xa4\\2")  # 0xf0a45c32
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf0a45c32))

        data.write(b"\xd8\x11`\x03")  # 0xd8116003
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd8116003))

        data.write(b"APF\xed")  # 0x415046ed
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x415046ed))

        data.write(b"\xec\x9c\x01\xb2")  # 0xec9c01b2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xec9c01b2))

        data.write(b"TU@\xe5")  # 0x545540e5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x545540e5))

        data.write(b"T\x90\xe2\x14")  # 0x5490e214
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.power_beam_refresh_effect))

        data.write(b"\x88~\x8a\x8b")  # 0x887e8a8b
        data.write(b"\x00\x0c")  # size
        self.hit_radius.to_stream(data, game)

        data.write(b"\xb7\xf5dm")  # 0xb7f5646d
        data.write(b"\x00\x0c")  # size
        self.hit_offset.to_stream(data, game)

        data.write(b"A\xb7+,")  # 0x41b72b2c
        data.write(b"\x00\x0c")  # size
        self.effect_offset.to_stream(data, game)

        data.write(b"\xbb\xbe\xe6\x0b")  # 0xbbbee60b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xbbbee60b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SafeZoneCrystalJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            actor_parameters=ActorParameters.from_json(json_data["actor_parameters"]),
            scannable_info_collapsed=json_data["scannable_info_collapsed"],
            scannable_info_entangled=json_data["scannable_info_entangled"],
            scannable_info_light=json_data["scannable_info_light"],
            scannable_info_annihilator=json_data["scannable_info_annihilator"],
            safezone_type=json_data["safezone_type"],
            initially_entangled=json_data["initially_entangled"],
            collapsed_effect=json_data["collapsed_effect"],
            expanded_effect=json_data["expanded_effect"],
            entangled_effect=json_data["entangled_effect"],
            part=json_data["part"],
            echo_effect=json_data["echo_effect"],
            normal_crystal=json_data["normal_crystal"],
            entangled_crystal=json_data["entangled_crystal"],
            energized_model=json_data["energized_model"],
            echo_crystal=json_data["echo_crystal"],
            max_time_expanded=json_data["max_time_expanded"],
            max_time_entangled=json_data["max_time_entangled"],
            unknown_0xf0a45c32=json_data["unknown_0xf0a45c32"],
            unknown_0xd8116003=json_data["unknown_0xd8116003"],
            unknown_0x415046ed=json_data["unknown_0x415046ed"],
            unknown_0xec9c01b2=json_data["unknown_0xec9c01b2"],
            unknown_0x545540e5=json_data["unknown_0x545540e5"],
            power_beam_refresh_effect=json_data["power_beam_refresh_effect"],
            hit_radius=Vector.from_json(json_data["hit_radius"]),
            hit_offset=Vector.from_json(json_data["hit_offset"]),
            effect_offset=Vector.from_json(json_data["effect_offset"]),
            unknown_0xbbbee60b=Spline.from_json(json_data["unknown_0xbbbee60b"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "actor_parameters": self.actor_parameters.to_json(),
            "scannable_info_collapsed": self.scannable_info_collapsed,
            "scannable_info_entangled": self.scannable_info_entangled,
            "scannable_info_light": self.scannable_info_light,
            "scannable_info_annihilator": self.scannable_info_annihilator,
            "safezone_type": self.safezone_type,
            "initially_entangled": self.initially_entangled,
            "collapsed_effect": self.collapsed_effect,
            "expanded_effect": self.expanded_effect,
            "entangled_effect": self.entangled_effect,
            "part": self.part,
            "echo_effect": self.echo_effect,
            "normal_crystal": self.normal_crystal,
            "entangled_crystal": self.entangled_crystal,
            "energized_model": self.energized_model,
            "echo_crystal": self.echo_crystal,
            "max_time_expanded": self.max_time_expanded,
            "max_time_entangled": self.max_time_entangled,
            "unknown_0xf0a45c32": self.unknown_0xf0a45c32,
            "unknown_0xd8116003": self.unknown_0xd8116003,
            "unknown_0x415046ed": self.unknown_0x415046ed,
            "unknown_0xec9c01b2": self.unknown_0xec9c01b2,
            "unknown_0x545540e5": self.unknown_0x545540e5,
            "power_beam_refresh_effect": self.power_beam_refresh_effect,
            "hit_radius": self.hit_radius.to_json(),
            "hit_offset": self.hit_offset.to_json(),
            "effect_offset": self.effect_offset.to_json(),
            "unknown_0xbbbee60b": self.unknown_0xbbbee60b.to_json(),
        }

    def _dependencies_for_scannable_info_collapsed(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_collapsed)

    def _dependencies_for_scannable_info_entangled(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_entangled)

    def _dependencies_for_scannable_info_light(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_light)

    def _dependencies_for_scannable_info_annihilator(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_annihilator)

    def _dependencies_for_collapsed_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collapsed_effect)

    def _dependencies_for_expanded_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.expanded_effect)

    def _dependencies_for_entangled_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.entangled_effect)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_echo_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_effect)

    def _dependencies_for_normal_crystal(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.normal_crystal)

    def _dependencies_for_entangled_crystal(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.entangled_crystal)

    def _dependencies_for_energized_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energized_model)

    def _dependencies_for_echo_crystal(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_crystal)

    def _dependencies_for_power_beam_refresh_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.power_beam_refresh_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.actor_parameters.dependencies_for, "actor_parameters", "ActorParameters"),
            (self._dependencies_for_scannable_info_collapsed, "scannable_info_collapsed", "AssetId"),
            (self._dependencies_for_scannable_info_entangled, "scannable_info_entangled", "AssetId"),
            (self._dependencies_for_scannable_info_light, "scannable_info_light", "AssetId"),
            (self._dependencies_for_scannable_info_annihilator, "scannable_info_annihilator", "AssetId"),
            (self._dependencies_for_collapsed_effect, "collapsed_effect", "AssetId"),
            (self._dependencies_for_expanded_effect, "expanded_effect", "AssetId"),
            (self._dependencies_for_entangled_effect, "entangled_effect", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self._dependencies_for_echo_effect, "echo_effect", "AssetId"),
            (self._dependencies_for_normal_crystal, "normal_crystal", "AssetId"),
            (self._dependencies_for_entangled_crystal, "entangled_crystal", "AssetId"),
            (self._dependencies_for_energized_model, "energized_model", "AssetId"),
            (self._dependencies_for_echo_crystal, "echo_crystal", "AssetId"),
            (self._dependencies_for_power_beam_refresh_effect, "power_beam_refresh_effect", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SafeZoneCrystal.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_hit_radius(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_hit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_effect_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0xbbbee60b(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xD29C031D: ("actor_parameters", _decode_actor_parameters),
    0x9B8B3323: ("scannable_info_collapsed", structs.decode_BIG_L),
    0xE36E20A7: ("scannable_info_entangled", structs.decode_BIG_L),
    0xAC794DA8: ("scannable_info_light", structs.decode_BIG_L),
    0xC21F264F: ("scannable_info_annihilator", structs.decode_BIG_L),
    0x1115FB68: ("safezone_type", structs.decode_BIG_l),
    0xA0D9E87F: ("initially_entangled", structs.decode_BIG_bool_),
    0x42A046C2: ("collapsed_effect", structs.decode_BIG_L),
    0x5B91FF38: ("expanded_effect", structs.decode_BIG_L),
    0x5B8275BC: ("entangled_effect", structs.decode_BIG_L),
    0xADACEC90: ("part", structs.decode_BIG_L),
    0x0D2E4AD3: ("echo_effect", structs.decode_BIG_L),
    0x71EFFFC4: ("normal_crystal", structs.decode_BIG_L),
    0xC3DD9B75: ("entangled_crystal", structs.decode_BIG_L),
    0xF1F3D90F: ("energized_model", structs.decode_BIG_L),
    0x1E864B83: ("echo_crystal", structs.decode_BIG_L),
    0xBD30F7A3: ("max_time_expanded", structs.decode_BIG_f),
    0xA7BDC4F8: ("max_time_entangled", structs.decode_BIG_f),
    0xF0A45C32: ("unknown_0xf0a45c32", structs.decode_BIG_f),
    0xD8116003: ("unknown_0xd8116003", structs.decode_BIG_f),
    0x415046ED: ("unknown_0x415046ed", structs.decode_BIG_f),
    0xEC9C01B2: ("unknown_0xec9c01b2", structs.decode_BIG_f),
    0x545540E5: ("unknown_0x545540e5", structs.decode_BIG_f),
    0x5490E214: ("power_beam_refresh_effect", structs.decode_BIG_L),
    0x887E8A8B: ("hit_radius", _decode_hit_radius),
    0xB7F5646D: ("hit_offset", _decode_hit_offset),
    0x41B72B2C: ("effect_offset", _decode_effect_offset),
    0xBBBEE60B: ("unknown_0xbbbee60b", _decode_unknown_0xbbbee60b),
}
