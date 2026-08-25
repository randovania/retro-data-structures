# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct44Json(typing_extensions.TypedDict):
        wpsc: int
        carapace1: int
        carapace2: int
        stomach_plate: int
        tongue_piece: int
        tongue_tip: int
        part: int
        max_grapple_distance: float
        grapple_data: json_util.JsonObject
        sound_stomach_hit: int
        sound_phazon_lance: int
        sound_tongue_attack_loop: int
        sound_tongue_latch: int
        sound_tongue_release: int


@dataclasses.dataclass()
class UnknownStruct44(BaseProperty):
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x861CD2A0, original_name="WPSC"),
        },
    )
    carapace1: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA8C2AC76, original_name="Carapace1"),
        },
    )
    carapace2: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2E56DED8, original_name="Carapace2"),
        },
    )
    stomach_plate: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF47476CE, original_name="StomachPlate"),
        },
    )
    tongue_piece: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x470306BE, original_name="TonguePiece"),
        },
    )
    tongue_tip: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x87952FC5, original_name="TongueTip"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x01D82EEB, original_name="PART"),
        },
    )
    max_grapple_distance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1CC93984, original_name="MaxGrappleDistance"),
        },
    )
    grapple_data: GrappleData = dataclasses.field(
        default_factory=GrappleData,
        metadata={
            "reflection": FieldReflection[GrappleData](
                GrappleData,
                id=0xF609C637,
                original_name="GrappleData",
                from_json=GrappleData.from_json,
                to_json=GrappleData.to_json,
            ),
        },
    )
    sound_stomach_hit: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD887792B, original_name="Sound_StomachHit"),
        },
    )
    sound_phazon_lance: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF9826473, original_name="Sound_PhazonLance"),
        },
    )
    sound_tongue_attack_loop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9D6E1A47, original_name="Sound_TongueAttackLoop"),
        },
    )
    sound_tongue_latch: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x87E6E958, original_name="Sound_TongueLatch"),
        },
    )
    sound_tongue_release: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA6597839, original_name="Sound_TongueRelease"),
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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x861CD2A0
        wpsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8C2AC76
        carapace1 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E56DED8
        carapace2 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF47476CE
        stomach_plate = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x470306BE
        tongue_piece = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87952FC5
        tongue_tip = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01D82EEB
        part = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CC93984
        max_grapple_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF609C637
        grapple_data = GrappleData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD887792B
        sound_stomach_hit = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9826473
        sound_phazon_lance = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D6E1A47
        sound_tongue_attack_loop = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87E6E958
        sound_tongue_latch = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA6597839
        sound_tongue_release = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            wpsc,
            carapace1,
            carapace2,
            stomach_plate,
            tongue_piece,
            tongue_tip,
            part,
            max_grapple_distance,
            grapple_data,
            sound_stomach_hit,
            sound_phazon_lance,
            sound_tongue_attack_loop,
            sound_tongue_latch,
            sound_tongue_release,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"\x86\x1c\xd2\xa0")  # 0x861cd2a0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc))

        data.write(b"\xa8\xc2\xacv")  # 0xa8c2ac76
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.carapace1))

        data.write(b".V\xde\xd8")  # 0x2e56ded8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.carapace2))

        data.write(b"\xf4tv\xce")  # 0xf47476ce
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.stomach_plate))

        data.write(b"G\x03\x06\xbe")  # 0x470306be
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.tongue_piece))

        data.write(b"\x87\x95/\xc5")  # 0x87952fc5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.tongue_tip))

        data.write(b"\x01\xd8.\xeb")  # 0x1d82eeb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part))

        data.write(b"\x1c\xc99\x84")  # 0x1cc93984
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_grapple_distance))

        data.write(b"\xf6\t\xc67")  # 0xf609c637
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd8\x87y+")  # 0xd887792b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_stomach_hit))

        data.write(b"\xf9\x82ds")  # 0xf9826473
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_phazon_lance))

        data.write(b"\x9dn\x1aG")  # 0x9d6e1a47
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_tongue_attack_loop))

        data.write(b"\x87\xe6\xe9X")  # 0x87e6e958
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_tongue_latch))

        data.write(b"\xa6Yx9")  # 0xa6597839
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_tongue_release))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct44Json", data)
        return cls(
            wpsc=json_data["wpsc"],
            carapace1=json_data["carapace1"],
            carapace2=json_data["carapace2"],
            stomach_plate=json_data["stomach_plate"],
            tongue_piece=json_data["tongue_piece"],
            tongue_tip=json_data["tongue_tip"],
            part=json_data["part"],
            max_grapple_distance=json_data["max_grapple_distance"],
            grapple_data=GrappleData.from_json(json_data["grapple_data"]),
            sound_stomach_hit=json_data["sound_stomach_hit"],
            sound_phazon_lance=json_data["sound_phazon_lance"],
            sound_tongue_attack_loop=json_data["sound_tongue_attack_loop"],
            sound_tongue_latch=json_data["sound_tongue_latch"],
            sound_tongue_release=json_data["sound_tongue_release"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "wpsc": self.wpsc,
            "carapace1": self.carapace1,
            "carapace2": self.carapace2,
            "stomach_plate": self.stomach_plate,
            "tongue_piece": self.tongue_piece,
            "tongue_tip": self.tongue_tip,
            "part": self.part,
            "max_grapple_distance": self.max_grapple_distance,
            "grapple_data": self.grapple_data.to_json(),
            "sound_stomach_hit": self.sound_stomach_hit,
            "sound_phazon_lance": self.sound_phazon_lance,
            "sound_tongue_attack_loop": self.sound_tongue_attack_loop,
            "sound_tongue_latch": self.sound_tongue_latch,
            "sound_tongue_release": self.sound_tongue_release,
        }


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x861CD2A0: ("wpsc", structs.decode_BIG_Q),
    0xA8C2AC76: ("carapace1", structs.decode_BIG_Q),
    0x2E56DED8: ("carapace2", structs.decode_BIG_Q),
    0xF47476CE: ("stomach_plate", structs.decode_BIG_Q),
    0x470306BE: ("tongue_piece", structs.decode_BIG_Q),
    0x87952FC5: ("tongue_tip", structs.decode_BIG_Q),
    0x01D82EEB: ("part", structs.decode_BIG_Q),
    0x1CC93984: ("max_grapple_distance", structs.decode_BIG_f),
    0xF609C637: ("grapple_data", _decode_grapple_data),
    0xD887792B: ("sound_stomach_hit", structs.decode_BIG_Q),
    0xF9826473: ("sound_phazon_lance", structs.decode_BIG_Q),
    0x9D6E1A47: ("sound_tongue_attack_loop", structs.decode_BIG_Q),
    0x87E6E958: ("sound_tongue_latch", structs.decode_BIG_Q),
    0xA6597839: ("sound_tongue_release", structs.decode_BIG_Q),
}
