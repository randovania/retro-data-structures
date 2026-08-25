# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryItem import PlayerInventoryItem
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class WeaponsJson(typing_extensions.TypedDict):
        power_beam: bool
        plasma_beam: bool
        nova_beam: bool
        charge_upgrade: bool
        missile: json_util.JsonObject
        ice_missile: bool
        seeker_missile: bool
        grapple_beam_pull: bool
        grapple_beam_swing: bool
        grapple_beam_voltage: bool
        bomb: bool


@dataclasses.dataclass()
class Weapons(BaseProperty):
    power_beam: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF9BC3E3D, original_name="PowerBeam"),
        },
    )
    plasma_beam: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x42C900ED, original_name="PlasmaBeam"),
        },
    )
    nova_beam: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4AE27FE7, original_name="NovaBeam"),
        },
    )
    charge_upgrade: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF34F99D7, original_name="ChargeUpgrade"),
        },
    )
    missile: PlayerInventoryItem = dataclasses.field(
        default_factory=PlayerInventoryItem,
        metadata={
            "reflection": FieldReflection[PlayerInventoryItem](
                PlayerInventoryItem,
                id=0xA387191D,
                original_name="Missile",
                from_json=PlayerInventoryItem.from_json,
                to_json=PlayerInventoryItem.to_json,
            ),
        },
    )
    ice_missile: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5DB3E694, original_name="IceMissile"),
        },
    )
    seeker_missile: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9AA405C1, original_name="SeekerMissile"),
        },
    )
    grapple_beam_pull: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA4658688, original_name="GrappleBeamPull"),
        },
    )
    grapple_beam_swing: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xD23CF29D, original_name="GrappleBeamSwing"),
        },
    )
    grapple_beam_voltage: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5A7E301E, original_name="GrappleBeamVoltage"),
        },
    )
    bomb: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAFC6082D, original_name="Bomb"),
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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9BC3E3D
        power_beam = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42C900ED
        plasma_beam = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AE27FE7
        nova_beam = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF34F99D7
        charge_upgrade = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA387191D
        missile = PlayerInventoryItem.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5DB3E694
        ice_missile = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9AA405C1
        seeker_missile = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4658688
        grapple_beam_pull = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD23CF29D
        grapple_beam_swing = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5A7E301E
        grapple_beam_voltage = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAFC6082D
        bomb = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            power_beam,
            plasma_beam,
            nova_beam,
            charge_upgrade,
            missile,
            ice_missile,
            seeker_missile,
            grapple_beam_pull,
            grapple_beam_swing,
            grapple_beam_voltage,
            bomb,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"\xf9\xbc>=")  # 0xf9bc3e3d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.power_beam))

        data.write(b"B\xc9\x00\xed")  # 0x42c900ed
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.plasma_beam))

        data.write(b"J\xe2\x7f\xe7")  # 0x4ae27fe7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.nova_beam))

        data.write(b"\xf3O\x99\xd7")  # 0xf34f99d7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.charge_upgrade))

        data.write(b"\xa3\x87\x19\x1d")  # 0xa387191d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.missile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"]\xb3\xe6\x94")  # 0x5db3e694
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ice_missile))

        data.write(b"\x9a\xa4\x05\xc1")  # 0x9aa405c1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.seeker_missile))

        data.write(b"\xa4e\x86\x88")  # 0xa4658688
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.grapple_beam_pull))

        data.write(b"\xd2<\xf2\x9d")  # 0xd23cf29d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.grapple_beam_swing))

        data.write(b"Z~0\x1e")  # 0x5a7e301e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.grapple_beam_voltage))

        data.write(b"\xaf\xc6\x08-")  # 0xafc6082d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.bomb))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WeaponsJson", data)
        return cls(
            power_beam=json_data["power_beam"],
            plasma_beam=json_data["plasma_beam"],
            nova_beam=json_data["nova_beam"],
            charge_upgrade=json_data["charge_upgrade"],
            missile=PlayerInventoryItem.from_json(json_data["missile"]),
            ice_missile=json_data["ice_missile"],
            seeker_missile=json_data["seeker_missile"],
            grapple_beam_pull=json_data["grapple_beam_pull"],
            grapple_beam_swing=json_data["grapple_beam_swing"],
            grapple_beam_voltage=json_data["grapple_beam_voltage"],
            bomb=json_data["bomb"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "power_beam": self.power_beam,
            "plasma_beam": self.plasma_beam,
            "nova_beam": self.nova_beam,
            "charge_upgrade": self.charge_upgrade,
            "missile": self.missile.to_json(),
            "ice_missile": self.ice_missile,
            "seeker_missile": self.seeker_missile,
            "grapple_beam_pull": self.grapple_beam_pull,
            "grapple_beam_swing": self.grapple_beam_swing,
            "grapple_beam_voltage": self.grapple_beam_voltage,
            "bomb": self.bomb,
        }


def _decode_missile(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryItem:
    return PlayerInventoryItem.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF9BC3E3D: ("power_beam", structs.decode_BIG_bool_),
    0x42C900ED: ("plasma_beam", structs.decode_BIG_bool_),
    0x4AE27FE7: ("nova_beam", structs.decode_BIG_bool_),
    0xF34F99D7: ("charge_upgrade", structs.decode_BIG_bool_),
    0xA387191D: ("missile", _decode_missile),
    0x5DB3E694: ("ice_missile", structs.decode_BIG_bool_),
    0x9AA405C1: ("seeker_missile", structs.decode_BIG_bool_),
    0xA4658688: ("grapple_beam_pull", structs.decode_BIG_bool_),
    0xD23CF29D: ("grapple_beam_swing", structs.decode_BIG_bool_),
    0x5A7E301E: ("grapple_beam_voltage", structs.decode_BIG_bool_),
    0xAFC6082D: ("bomb", structs.decode_BIG_bool_),
}
