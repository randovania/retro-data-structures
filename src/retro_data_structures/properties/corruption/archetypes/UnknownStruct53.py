# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct53Json(typing_extensions.TypedDict):
        part_0xccf0cc68: int
        part_0x9cf6186b: int
        part_0xafa0d295: int
        wpsc_0xb93e46e5: int
        below_beam: json_util.JsonObject
        txtr: int
        unknown_0xab46a8c3: float
        part_0xc89c34fd: int
        part_0xb10f94c5: int
        above_missile: int
        wpsc_0x67dd641e: int
        above_fireball: int
        part_0xca7f8a50: int
        tunnel_steam_effect: int
        tunnel_steam_texture: int
        sound_steam: int
        caud_0xe13ab25f: int
        caud_0x79169d11: int
        sound_mouth_beam: int
        caud_0xbd8e8710: int
        unknown_0x7802cbf0: float
        unknown_0x491096be: int
        unknown_0xdbf376a9: float
        unknown_0x6d56bc5b: int
        sound_beam_telegraph: int
        sound_initial_warning: int
        unknown_0xf1bf1c16: int
        unknown_0x0436327d: float
        unknown_0x772b6eb8: int
        unknown_0x154b5804: float
        unknown_0xbc77bd1d: int
        unknown_0xacb083ec: float
        unknown_0x0cd1f3cf: int
        unknown_0x5804032e: int
        unknown_0xa48bdf63: int
        unknown_0x1a058c4f: int


@dataclasses.dataclass()
class UnknownStruct53(BaseProperty):
    part_0xccf0cc68: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCCF0CC68, original_name="PART"),
        },
    )
    part_0x9cf6186b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9CF6186B, original_name="PART"),
        },
    )
    part_0xafa0d295: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAFA0D295, original_name="PART"),
        },
    )
    wpsc_0xb93e46e5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB93E46E5, original_name="WPSC"),
        },
    )
    below_beam: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x1AAE3DB5,
                original_name="BelowBeam",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    txtr: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBF4F8D8C, original_name="TXTR"),
        },
    )
    unknown_0xab46a8c3: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAB46A8C3, original_name="Unknown"),
        },
    )
    part_0xc89c34fd: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC89C34FD, original_name="PART"),
        },
    )
    part_0xb10f94c5: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB10F94C5, original_name="PART"),
        },
    )
    above_missile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0BD56E50, original_name="AboveMissile"),
        },
    )
    wpsc_0x67dd641e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x67DD641E, original_name="WPSC"),
        },
    )
    above_fireball: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x51FB4542, original_name="AboveFireball"),
        },
    )
    part_0xca7f8a50: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCA7F8A50, original_name="PART"),
        },
    )
    tunnel_steam_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC34287E4, original_name="TunnelSteamEffect"),
        },
    )
    tunnel_steam_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6F888688, original_name="TunnelSteamTexture"),
        },
    )
    sound_steam: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x84E9CCC8, original_name="Sound_Steam"),
        },
    )
    caud_0xe13ab25f: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE13AB25F, original_name="CAUD"),
        },
    )
    caud_0x79169d11: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x79169D11, original_name="CAUD"),
        },
    )
    sound_mouth_beam: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5037FAFB, original_name="Sound_MouthBeam"),
        },
    )
    caud_0xbd8e8710: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBD8E8710, original_name="CAUD"),
        },
    )
    unknown_0x7802cbf0: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7802CBF0, original_name="Unknown"),
        },
    )
    unknown_0x491096be: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x491096BE, original_name="Unknown"),
        },
    )
    unknown_0xdbf376a9: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDBF376A9, original_name="Unknown"),
        },
    )
    unknown_0x6d56bc5b: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6D56BC5B, original_name="Unknown"),
        },
    )
    sound_beam_telegraph: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4D0BFC69, original_name="Sound_BeamTelegraph"),
        },
    )
    sound_initial_warning: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8813C561, original_name="Sound_InitialWarning"),
        },
    )
    unknown_0xf1bf1c16: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF1BF1C16, original_name="Unknown"),
        },
    )
    unknown_0x0436327d: float = dataclasses.field(
        default=500.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0436327D, original_name="Unknown"),
        },
    )
    unknown_0x772b6eb8: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x772B6EB8, original_name="Unknown"),
        },
    )
    unknown_0x154b5804: float = dataclasses.field(
        default=250.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x154B5804, original_name="Unknown"),
        },
    )
    unknown_0xbc77bd1d: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBC77BD1D, original_name="Unknown"),
        },
    )
    unknown_0xacb083ec: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xACB083EC, original_name="Unknown"),
        },
    )
    unknown_0x0cd1f3cf: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0CD1F3CF, original_name="Unknown"),
        },
    )
    unknown_0x5804032e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5804032E, original_name="Unknown"),
        },
    )
    unknown_0xa48bdf63: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA48BDF63, original_name="Unknown"),
        },
    )
    unknown_0x1a058c4f: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1A058C4F, original_name="Unknown"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 36:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCF0CC68
        part_0xccf0cc68 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9CF6186B
        part_0x9cf6186b = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFA0D295
        part_0xafa0d295 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB93E46E5
        wpsc_0xb93e46e5 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AAE3DB5
        below_beam = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF4F8D8C
        txtr = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB46A8C3
        unknown_0xab46a8c3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC89C34FD
        part_0xc89c34fd = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB10F94C5
        part_0xb10f94c5 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BD56E50
        above_missile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67DD641E
        wpsc_0x67dd641e = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51FB4542
        above_fireball = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCA7F8A50
        part_0xca7f8a50 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC34287E4
        tunnel_steam_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6F888688
        tunnel_steam_texture = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84E9CCC8
        sound_steam = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE13AB25F
        caud_0xe13ab25f = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79169D11
        caud_0x79169d11 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5037FAFB
        sound_mouth_beam = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD8E8710
        caud_0xbd8e8710 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7802CBF0
        unknown_0x7802cbf0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x491096BE
        unknown_0x491096be = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDBF376A9
        unknown_0xdbf376a9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D56BC5B
        unknown_0x6d56bc5b = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D0BFC69
        sound_beam_telegraph = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8813C561
        sound_initial_warning = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1BF1C16
        unknown_0xf1bf1c16 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0436327D
        unknown_0x0436327d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x772B6EB8
        unknown_0x772b6eb8 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x154B5804
        unknown_0x154b5804 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC77BD1D
        unknown_0xbc77bd1d = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xACB083EC
        unknown_0xacb083ec = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CD1F3CF
        unknown_0x0cd1f3cf = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5804032E
        unknown_0x5804032e = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA48BDF63
        unknown_0xa48bdf63 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A058C4F
        unknown_0x1a058c4f = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            part_0xccf0cc68,
            part_0x9cf6186b,
            part_0xafa0d295,
            wpsc_0xb93e46e5,
            below_beam,
            txtr,
            unknown_0xab46a8c3,
            part_0xc89c34fd,
            part_0xb10f94c5,
            above_missile,
            wpsc_0x67dd641e,
            above_fireball,
            part_0xca7f8a50,
            tunnel_steam_effect,
            tunnel_steam_texture,
            sound_steam,
            caud_0xe13ab25f,
            caud_0x79169d11,
            sound_mouth_beam,
            caud_0xbd8e8710,
            unknown_0x7802cbf0,
            unknown_0x491096be,
            unknown_0xdbf376a9,
            unknown_0x6d56bc5b,
            sound_beam_telegraph,
            sound_initial_warning,
            unknown_0xf1bf1c16,
            unknown_0x0436327d,
            unknown_0x772b6eb8,
            unknown_0x154b5804,
            unknown_0xbc77bd1d,
            unknown_0xacb083ec,
            unknown_0x0cd1f3cf,
            unknown_0x5804032e,
            unknown_0xa48bdf63,
            unknown_0x1a058c4f,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00$")  # 36 properties

        data.write(b"\xcc\xf0\xcch")  # 0xccf0cc68
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xccf0cc68))

        data.write(b"\x9c\xf6\x18k")  # 0x9cf6186b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x9cf6186b))

        data.write(b"\xaf\xa0\xd2\x95")  # 0xafa0d295
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xafa0d295))

        data.write(b"\xb9>F\xe5")  # 0xb93e46e5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc_0xb93e46e5))

        data.write(b"\x1a\xae=\xb5")  # 0x1aae3db5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.below_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbfO\x8d\x8c")  # 0xbf4f8d8c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.txtr))

        data.write(b"\xabF\xa8\xc3")  # 0xab46a8c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xab46a8c3))

        data.write(b"\xc8\x9c4\xfd")  # 0xc89c34fd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xc89c34fd))

        data.write(b"\xb1\x0f\x94\xc5")  # 0xb10f94c5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xb10f94c5))

        data.write(b"\x0b\xd5nP")  # 0xbd56e50
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.above_missile))

        data.write(b"g\xddd\x1e")  # 0x67dd641e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc_0x67dd641e))

        data.write(b"Q\xfbEB")  # 0x51fb4542
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.above_fireball))

        data.write(b"\xca\x7f\x8aP")  # 0xca7f8a50
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xca7f8a50))

        data.write(b"\xc3B\x87\xe4")  # 0xc34287e4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.tunnel_steam_effect))

        data.write(b"o\x88\x86\x88")  # 0x6f888688
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.tunnel_steam_texture))

        data.write(b"\x84\xe9\xcc\xc8")  # 0x84e9ccc8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_steam))

        data.write(b"\xe1:\xb2_")  # 0xe13ab25f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xe13ab25f))

        data.write(b"y\x16\x9d\x11")  # 0x79169d11
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x79169d11))

        data.write(b"P7\xfa\xfb")  # 0x5037fafb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_mouth_beam))

        data.write(b"\xbd\x8e\x87\x10")  # 0xbd8e8710
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xbd8e8710))

        data.write(b"x\x02\xcb\xf0")  # 0x7802cbf0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7802cbf0))

        data.write(b"I\x10\x96\xbe")  # 0x491096be
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x491096be))

        data.write(b"\xdb\xf3v\xa9")  # 0xdbf376a9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdbf376a9))

        data.write(b"mV\xbc[")  # 0x6d56bc5b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x6d56bc5b))

        data.write(b"M\x0b\xfci")  # 0x4d0bfc69
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_beam_telegraph))

        data.write(b"\x88\x13\xc5a")  # 0x8813c561
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_initial_warning))

        data.write(b"\xf1\xbf\x1c\x16")  # 0xf1bf1c16
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xf1bf1c16))

        data.write(b"\x0462}")  # 0x436327d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0436327d))

        data.write(b"w+n\xb8")  # 0x772b6eb8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x772b6eb8))

        data.write(b"\x15KX\x04")  # 0x154b5804
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x154b5804))

        data.write(b"\xbcw\xbd\x1d")  # 0xbc77bd1d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xbc77bd1d))

        data.write(b"\xac\xb0\x83\xec")  # 0xacb083ec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xacb083ec))

        data.write(b"\x0c\xd1\xf3\xcf")  # 0xcd1f3cf
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x0cd1f3cf))

        data.write(b"X\x04\x03.")  # 0x5804032e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x5804032e))

        data.write(b"\xa4\x8b\xdfc")  # 0xa48bdf63
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xa48bdf63))

        data.write(b"\x1a\x05\x8cO")  # 0x1a058c4f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x1a058c4f))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct53Json", data)
        return cls(
            part_0xccf0cc68=json_data["part_0xccf0cc68"],
            part_0x9cf6186b=json_data["part_0x9cf6186b"],
            part_0xafa0d295=json_data["part_0xafa0d295"],
            wpsc_0xb93e46e5=json_data["wpsc_0xb93e46e5"],
            below_beam=PlasmaBeamInfo.from_json(json_data["below_beam"]),
            txtr=json_data["txtr"],
            unknown_0xab46a8c3=json_data["unknown_0xab46a8c3"],
            part_0xc89c34fd=json_data["part_0xc89c34fd"],
            part_0xb10f94c5=json_data["part_0xb10f94c5"],
            above_missile=json_data["above_missile"],
            wpsc_0x67dd641e=json_data["wpsc_0x67dd641e"],
            above_fireball=json_data["above_fireball"],
            part_0xca7f8a50=json_data["part_0xca7f8a50"],
            tunnel_steam_effect=json_data["tunnel_steam_effect"],
            tunnel_steam_texture=json_data["tunnel_steam_texture"],
            sound_steam=json_data["sound_steam"],
            caud_0xe13ab25f=json_data["caud_0xe13ab25f"],
            caud_0x79169d11=json_data["caud_0x79169d11"],
            sound_mouth_beam=json_data["sound_mouth_beam"],
            caud_0xbd8e8710=json_data["caud_0xbd8e8710"],
            unknown_0x7802cbf0=json_data["unknown_0x7802cbf0"],
            unknown_0x491096be=json_data["unknown_0x491096be"],
            unknown_0xdbf376a9=json_data["unknown_0xdbf376a9"],
            unknown_0x6d56bc5b=json_data["unknown_0x6d56bc5b"],
            sound_beam_telegraph=json_data["sound_beam_telegraph"],
            sound_initial_warning=json_data["sound_initial_warning"],
            unknown_0xf1bf1c16=json_data["unknown_0xf1bf1c16"],
            unknown_0x0436327d=json_data["unknown_0x0436327d"],
            unknown_0x772b6eb8=json_data["unknown_0x772b6eb8"],
            unknown_0x154b5804=json_data["unknown_0x154b5804"],
            unknown_0xbc77bd1d=json_data["unknown_0xbc77bd1d"],
            unknown_0xacb083ec=json_data["unknown_0xacb083ec"],
            unknown_0x0cd1f3cf=json_data["unknown_0x0cd1f3cf"],
            unknown_0x5804032e=json_data["unknown_0x5804032e"],
            unknown_0xa48bdf63=json_data["unknown_0xa48bdf63"],
            unknown_0x1a058c4f=json_data["unknown_0x1a058c4f"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "part_0xccf0cc68": self.part_0xccf0cc68,
            "part_0x9cf6186b": self.part_0x9cf6186b,
            "part_0xafa0d295": self.part_0xafa0d295,
            "wpsc_0xb93e46e5": self.wpsc_0xb93e46e5,
            "below_beam": self.below_beam.to_json(),
            "txtr": self.txtr,
            "unknown_0xab46a8c3": self.unknown_0xab46a8c3,
            "part_0xc89c34fd": self.part_0xc89c34fd,
            "part_0xb10f94c5": self.part_0xb10f94c5,
            "above_missile": self.above_missile,
            "wpsc_0x67dd641e": self.wpsc_0x67dd641e,
            "above_fireball": self.above_fireball,
            "part_0xca7f8a50": self.part_0xca7f8a50,
            "tunnel_steam_effect": self.tunnel_steam_effect,
            "tunnel_steam_texture": self.tunnel_steam_texture,
            "sound_steam": self.sound_steam,
            "caud_0xe13ab25f": self.caud_0xe13ab25f,
            "caud_0x79169d11": self.caud_0x79169d11,
            "sound_mouth_beam": self.sound_mouth_beam,
            "caud_0xbd8e8710": self.caud_0xbd8e8710,
            "unknown_0x7802cbf0": self.unknown_0x7802cbf0,
            "unknown_0x491096be": self.unknown_0x491096be,
            "unknown_0xdbf376a9": self.unknown_0xdbf376a9,
            "unknown_0x6d56bc5b": self.unknown_0x6d56bc5b,
            "sound_beam_telegraph": self.sound_beam_telegraph,
            "sound_initial_warning": self.sound_initial_warning,
            "unknown_0xf1bf1c16": self.unknown_0xf1bf1c16,
            "unknown_0x0436327d": self.unknown_0x0436327d,
            "unknown_0x772b6eb8": self.unknown_0x772b6eb8,
            "unknown_0x154b5804": self.unknown_0x154b5804,
            "unknown_0xbc77bd1d": self.unknown_0xbc77bd1d,
            "unknown_0xacb083ec": self.unknown_0xacb083ec,
            "unknown_0x0cd1f3cf": self.unknown_0x0cd1f3cf,
            "unknown_0x5804032e": self.unknown_0x5804032e,
            "unknown_0xa48bdf63": self.unknown_0xa48bdf63,
            "unknown_0x1a058c4f": self.unknown_0x1a058c4f,
        }


def _decode_below_beam(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCCF0CC68: ("part_0xccf0cc68", structs.decode_BIG_Q),
    0x9CF6186B: ("part_0x9cf6186b", structs.decode_BIG_Q),
    0xAFA0D295: ("part_0xafa0d295", structs.decode_BIG_Q),
    0xB93E46E5: ("wpsc_0xb93e46e5", structs.decode_BIG_Q),
    0x1AAE3DB5: ("below_beam", _decode_below_beam),
    0xBF4F8D8C: ("txtr", structs.decode_BIG_Q),
    0xAB46A8C3: ("unknown_0xab46a8c3", structs.decode_BIG_f),
    0xC89C34FD: ("part_0xc89c34fd", structs.decode_BIG_Q),
    0xB10F94C5: ("part_0xb10f94c5", structs.decode_BIG_Q),
    0x0BD56E50: ("above_missile", structs.decode_BIG_Q),
    0x67DD641E: ("wpsc_0x67dd641e", structs.decode_BIG_Q),
    0x51FB4542: ("above_fireball", structs.decode_BIG_Q),
    0xCA7F8A50: ("part_0xca7f8a50", structs.decode_BIG_Q),
    0xC34287E4: ("tunnel_steam_effect", structs.decode_BIG_Q),
    0x6F888688: ("tunnel_steam_texture", structs.decode_BIG_Q),
    0x84E9CCC8: ("sound_steam", structs.decode_BIG_Q),
    0xE13AB25F: ("caud_0xe13ab25f", structs.decode_BIG_Q),
    0x79169D11: ("caud_0x79169d11", structs.decode_BIG_Q),
    0x5037FAFB: ("sound_mouth_beam", structs.decode_BIG_Q),
    0xBD8E8710: ("caud_0xbd8e8710", structs.decode_BIG_Q),
    0x7802CBF0: ("unknown_0x7802cbf0", structs.decode_BIG_f),
    0x491096BE: ("unknown_0x491096be", structs.decode_BIG_Q),
    0xDBF376A9: ("unknown_0xdbf376a9", structs.decode_BIG_f),
    0x6D56BC5B: ("unknown_0x6d56bc5b", structs.decode_BIG_Q),
    0x4D0BFC69: ("sound_beam_telegraph", structs.decode_BIG_Q),
    0x8813C561: ("sound_initial_warning", structs.decode_BIG_Q),
    0xF1BF1C16: ("unknown_0xf1bf1c16", structs.decode_BIG_Q),
    0x0436327D: ("unknown_0x0436327d", structs.decode_BIG_f),
    0x772B6EB8: ("unknown_0x772b6eb8", structs.decode_BIG_Q),
    0x154B5804: ("unknown_0x154b5804", structs.decode_BIG_f),
    0xBC77BD1D: ("unknown_0xbc77bd1d", structs.decode_BIG_Q),
    0xACB083EC: ("unknown_0xacb083ec", structs.decode_BIG_f),
    0x0CD1F3CF: ("unknown_0x0cd1f3cf", structs.decode_BIG_Q),
    0x5804032E: ("unknown_0x5804032e", structs.decode_BIG_Q),
    0xA48BDF63: ("unknown_0xa48bdf63", structs.decode_BIG_Q),
    0x1A058C4F: ("unknown_0x1a058c4f", structs.decode_BIG_Q),
}
