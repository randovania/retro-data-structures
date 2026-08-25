# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.GrappleBlock import GrappleBlock
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GrappleDataJson(typing_extensions.TypedDict):
        grapple_type: int
        point_visible: bool
        unknown_0xb2bd2723: bool
        unknown_0x1a8dbea7: float
        unknown_0xa439ca6a: bool
        unknown_0x4b848c9b: bool
        grapple_block1: json_util.JsonObject
        grapple_block2: json_util.JsonObject
        grapple_block3: json_util.JsonObject
        grapple_block4: json_util.JsonObject
        grapple_block5: json_util.JsonObject
        unknown_0x5bbbe79e: float
        unknown_0x426f2f60: float
        sound_effect: int
        voltage_min_energy: float
        voltage_max_energy: float
        voltage_initial_energy: float
        voltage_energy_rate: float
        unknown_0x07648f63: int


@dataclasses.dataclass()
class GrappleData(BaseProperty):
    grapple_type: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x5DCF91E1, original_name="GrappleType"),
        },
    )
    point_visible: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC10219BF, original_name="PointVisible"),
        },
    )
    unknown_0xb2bd2723: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB2BD2723, original_name="Unknown"),
        },
    )
    unknown_0x1a8dbea7: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1A8DBEA7, original_name="Unknown"),
        },
    )
    unknown_0xa439ca6a: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA439CA6A, original_name="Unknown"),
        },
    )
    unknown_0x4b848c9b: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4B848C9B, original_name="Unknown"),
        },
    )
    grapple_block1: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0x5F669BA0,
                original_name="GrappleBlock1",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
            ),
        },
    )
    grapple_block2: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0xE2ACF76E,
                original_name="GrappleBlock2",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
            ),
        },
    )
    grapple_block3: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0x3F3A2EEB,
                original_name="GrappleBlock3",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
            ),
        },
    )
    grapple_block4: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0x424928B3,
                original_name="GrappleBlock4",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
            ),
        },
    )
    grapple_block5: GrappleBlock = dataclasses.field(
        default_factory=GrappleBlock,
        metadata={
            "reflection": FieldReflection[GrappleBlock](
                GrappleBlock,
                id=0x9FDFF136,
                original_name="GrappleBlock5",
                from_json=GrappleBlock.from_json,
                to_json=GrappleBlock.to_json,
            ),
        },
    )
    unknown_0x5bbbe79e: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BBBE79E, original_name="Unknown"),
        },
    )
    unknown_0x426f2f60: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x426F2F60, original_name="Unknown"),
        },
    )
    sound_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x771A3176, original_name="SoundEffect"),
        },
    )
    voltage_min_energy: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEFD287D9, original_name="VoltageMinEnergy"),
        },
    )
    voltage_max_energy: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x56F41CA8, original_name="VoltageMaxEnergy"),
        },
    )
    voltage_initial_energy: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4BDEE69A, original_name="VoltageInitialEnergy"),
        },
    )
    voltage_energy_rate: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0598B045, original_name="VoltageEnergyRate"),
        },
    )
    unknown_0x07648f63: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x07648F63, original_name="Unknown"),
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
        if property_count != 19:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5DCF91E1
        grapple_type = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC10219BF
        point_visible = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2BD2723
        unknown_0xb2bd2723 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1A8DBEA7
        unknown_0x1a8dbea7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA439CA6A
        unknown_0xa439ca6a = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B848C9B
        unknown_0x4b848c9b = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F669BA0
        grapple_block1 = GrappleBlock.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2ACF76E
        grapple_block2 = GrappleBlock.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3F3A2EEB
        grapple_block3 = GrappleBlock.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x424928B3
        grapple_block4 = GrappleBlock.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9FDFF136
        grapple_block5 = GrappleBlock.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BBBE79E
        unknown_0x5bbbe79e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x426F2F60
        unknown_0x426f2f60 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x771A3176
        sound_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEFD287D9
        voltage_min_energy = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56F41CA8
        voltage_max_energy = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4BDEE69A
        voltage_initial_energy = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0598B045
        voltage_energy_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07648F63
        unknown_0x07648f63 = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            grapple_type,
            point_visible,
            unknown_0xb2bd2723,
            unknown_0x1a8dbea7,
            unknown_0xa439ca6a,
            unknown_0x4b848c9b,
            grapple_block1,
            grapple_block2,
            grapple_block3,
            grapple_block4,
            grapple_block5,
            unknown_0x5bbbe79e,
            unknown_0x426f2f60,
            sound_effect,
            voltage_min_energy,
            voltage_max_energy,
            voltage_initial_energy,
            voltage_energy_rate,
            unknown_0x07648f63,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x00\x07")  # 7 properties
        num_properties_written = 7

        data.write(b"]\xcf\x91\xe1")  # 0x5dcf91e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grapple_type))

        data.write(b"\xc1\x02\x19\xbf")  # 0xc10219bf
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.point_visible))

        if self.unknown_0xb2bd2723 != default_override.get("unknown_0xb2bd2723", False):
            num_properties_written += 1
            data.write(b"\xb2\xbd'#")  # 0xb2bd2723
            data.write(b"\x00\x01")  # size
            data.write(structs.BIG_bool_.pack(self.unknown_0xb2bd2723))

        data.write(b"\x1a\x8d\xbe\xa7")  # 0x1a8dbea7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1a8dbea7))

        data.write(b"\xa49\xcaj")  # 0xa439ca6a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa439ca6a))

        data.write(b"K\x84\x8c\x9b")  # 0x4b848c9b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4b848c9b))

        data.write(b"_f\x9b\xa0")  # 0x5f669ba0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_block1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe2\xac\xf7n")  # 0xe2acf76e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.grapple_block2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.grapple_block3 != default_override.get("grapple_block3", GrappleBlock()):
            num_properties_written += 1
            data.write(b"?:.\xeb")  # 0x3f3a2eeb
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.grapple_block3.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.grapple_block4 != default_override.get("grapple_block4", GrappleBlock()):
            num_properties_written += 1
            data.write(b"BI(\xb3")  # 0x424928b3
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.grapple_block4.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.grapple_block5 != default_override.get("grapple_block5", GrappleBlock()):
            num_properties_written += 1
            data.write(b"\x9f\xdf\xf16")  # 0x9fdff136
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.grapple_block5.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.unknown_0x5bbbe79e != default_override.get("unknown_0x5bbbe79e", 8.0):
            num_properties_written += 1
            data.write(b"[\xbb\xe7\x9e")  # 0x5bbbe79e
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.unknown_0x5bbbe79e))

        if self.unknown_0x426f2f60 != default_override.get("unknown_0x426f2f60", 6.0):
            num_properties_written += 1
            data.write(b"Bo/`")  # 0x426f2f60
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.unknown_0x426f2f60))

        if self.sound_effect != default_override.get("sound_effect", default_asset_id):
            num_properties_written += 1
            data.write(b"w\x1a1v")  # 0x771a3176
            data.write(b"\x00\x08")  # size
            data.write(structs.BIG_Q.pack(self.sound_effect))

        if self.voltage_min_energy != default_override.get("voltage_min_energy", 0.0):
            num_properties_written += 1
            data.write(b"\xef\xd2\x87\xd9")  # 0xefd287d9
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.voltage_min_energy))

        if self.voltage_max_energy != default_override.get("voltage_max_energy", 100.0):
            num_properties_written += 1
            data.write(b"V\xf4\x1c\xa8")  # 0x56f41ca8
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.voltage_max_energy))

        if self.voltage_initial_energy != default_override.get("voltage_initial_energy", 50.0):
            num_properties_written += 1
            data.write(b"K\xde\xe6\x9a")  # 0x4bdee69a
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.voltage_initial_energy))

        if self.voltage_energy_rate != default_override.get("voltage_energy_rate", 10.0):
            num_properties_written += 1
            data.write(b"\x05\x98\xb0E")  # 0x598b045
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_f.pack(self.voltage_energy_rate))

        if self.unknown_0x07648f63 != default_override.get("unknown_0x07648f63", -1):
            num_properties_written += 1
            data.write(b"\x07d\x8fc")  # 0x7648f63
            data.write(b"\x00\x04")  # size
            data.write(structs.BIG_l.pack(self.unknown_0x07648f63))

        if num_properties_written != 7:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GrappleDataJson", data)
        return cls(
            grapple_type=json_data["grapple_type"],
            point_visible=json_data["point_visible"],
            unknown_0xb2bd2723=json_data["unknown_0xb2bd2723"],
            unknown_0x1a8dbea7=json_data["unknown_0x1a8dbea7"],
            unknown_0xa439ca6a=json_data["unknown_0xa439ca6a"],
            unknown_0x4b848c9b=json_data["unknown_0x4b848c9b"],
            grapple_block1=GrappleBlock.from_json(json_data["grapple_block1"]),
            grapple_block2=GrappleBlock.from_json(json_data["grapple_block2"]),
            grapple_block3=GrappleBlock.from_json(json_data["grapple_block3"]),
            grapple_block4=GrappleBlock.from_json(json_data["grapple_block4"]),
            grapple_block5=GrappleBlock.from_json(json_data["grapple_block5"]),
            unknown_0x5bbbe79e=json_data["unknown_0x5bbbe79e"],
            unknown_0x426f2f60=json_data["unknown_0x426f2f60"],
            sound_effect=json_data["sound_effect"],
            voltage_min_energy=json_data["voltage_min_energy"],
            voltage_max_energy=json_data["voltage_max_energy"],
            voltage_initial_energy=json_data["voltage_initial_energy"],
            voltage_energy_rate=json_data["voltage_energy_rate"],
            unknown_0x07648f63=json_data["unknown_0x07648f63"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "grapple_type": self.grapple_type,
            "point_visible": self.point_visible,
            "unknown_0xb2bd2723": self.unknown_0xb2bd2723,
            "unknown_0x1a8dbea7": self.unknown_0x1a8dbea7,
            "unknown_0xa439ca6a": self.unknown_0xa439ca6a,
            "unknown_0x4b848c9b": self.unknown_0x4b848c9b,
            "grapple_block1": self.grapple_block1.to_json(),
            "grapple_block2": self.grapple_block2.to_json(),
            "grapple_block3": self.grapple_block3.to_json(),
            "grapple_block4": self.grapple_block4.to_json(),
            "grapple_block5": self.grapple_block5.to_json(),
            "unknown_0x5bbbe79e": self.unknown_0x5bbbe79e,
            "unknown_0x426f2f60": self.unknown_0x426f2f60,
            "sound_effect": self.sound_effect,
            "voltage_min_energy": self.voltage_min_energy,
            "voltage_max_energy": self.voltage_max_energy,
            "voltage_initial_energy": self.voltage_initial_energy,
            "voltage_energy_rate": self.voltage_energy_rate,
            "unknown_0x07648f63": self.unknown_0x07648f63,
        }


def _decode_grapple_block1(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


def _decode_grapple_block2(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


def _decode_grapple_block3(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


def _decode_grapple_block4(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


def _decode_grapple_block5(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5DCF91E1: ("grapple_type", structs.decode_BIG_l),
    0xC10219BF: ("point_visible", structs.decode_BIG_bool_),
    0xB2BD2723: ("unknown_0xb2bd2723", structs.decode_BIG_bool_),
    0x1A8DBEA7: ("unknown_0x1a8dbea7", structs.decode_BIG_f),
    0xA439CA6A: ("unknown_0xa439ca6a", structs.decode_BIG_bool_),
    0x4B848C9B: ("unknown_0x4b848c9b", structs.decode_BIG_bool_),
    0x5F669BA0: ("grapple_block1", _decode_grapple_block1),
    0xE2ACF76E: ("grapple_block2", _decode_grapple_block2),
    0x3F3A2EEB: ("grapple_block3", _decode_grapple_block3),
    0x424928B3: ("grapple_block4", _decode_grapple_block4),
    0x9FDFF136: ("grapple_block5", _decode_grapple_block5),
    0x5BBBE79E: ("unknown_0x5bbbe79e", structs.decode_BIG_f),
    0x426F2F60: ("unknown_0x426f2f60", structs.decode_BIG_f),
    0x771A3176: ("sound_effect", structs.decode_BIG_Q),
    0xEFD287D9: ("voltage_min_energy", structs.decode_BIG_f),
    0x56F41CA8: ("voltage_max_energy", structs.decode_BIG_f),
    0x4BDEE69A: ("voltage_initial_energy", structs.decode_BIG_f),
    0x0598B045: ("voltage_energy_rate", structs.decode_BIG_f),
    0x07648F63: ("unknown_0x07648f63", structs.decode_BIG_l),
}
