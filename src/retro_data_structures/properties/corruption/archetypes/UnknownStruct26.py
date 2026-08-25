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

    class UnknownStruct26Json(typing_extensions.TypedDict):
        scan: int
        helmet_l_model: int
        helmet_r_model: int
        optic_array_model: int
        jammer_antenna_model: int
        part_0x537f8382: int
        jammer_antenna_explosion_effect: int
        part_0xad17a036: int
        leg_collision_effect: int
        visor_electric_effect: int
        missile_projectile: int
        huge_missile_projectile: int
        seeker_bomb_effect: int
        part_0xdbf176dd: int
        death_gibs: int
        part_0xdd6be17f: int
        max_grapple_distance: float
        grapple_data: json_util.JsonObject
        sound_jump_loop: int
        sound_bomb_loop: int
        caud_0xb4a84d85: int
        caud_0xfef01104: int
        caud_0xeb8805bd: int
        sound_fireball_loop: int
        unknown_0xa99ccb84: int
        unknown_0xb60df150: int


@dataclasses.dataclass()
class UnknownStruct26(BaseProperty):
    scan: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7FAB452A, original_name="SCAN"),
        },
    )
    helmet_l_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC47A5224, original_name="HelmetLModel"),
        },
    )
    helmet_r_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x38FABDE9, original_name="HelmetRModel"),
        },
    )
    optic_array_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4BA2833E, original_name="OpticArrayModel"),
        },
    )
    jammer_antenna_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC60FB911, original_name="JammerAntennaModel"),
        },
    )
    part_0x537f8382: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x537F8382, original_name="PART"),
        },
    )
    jammer_antenna_explosion_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0x98D5883D, original_name="JammerAntennaExplosionEffect"
            ),
        },
    )
    part_0xad17a036: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAD17A036, original_name="PART"),
        },
    )
    leg_collision_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x3FEF37BD, original_name="LegCollisionEffect"),
        },
    )
    visor_electric_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBD321538, original_name="VisorElectricEffect"),
        },
    )
    missile_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x70E97166, original_name="MissileProjectile"),
        },
    )
    huge_missile_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9EEF71C2, original_name="HugeMissileProjectile"),
        },
    )
    seeker_bomb_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF98FDCC9, original_name="SeekerBombEffect"),
        },
    )
    part_0xdbf176dd: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDBF176DD, original_name="PART"),
        },
    )
    death_gibs: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7AF488B1, original_name="DeathGibs"),
        },
    )
    part_0xdd6be17f: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDD6BE17F, original_name="PART"),
        },
    )
    max_grapple_distance: float = dataclasses.field(
        default=40.0,
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
    sound_jump_loop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2C558C5D, original_name="Sound_JumpLoop"),
        },
    )
    sound_bomb_loop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB3220B78, original_name="Sound_BombLoop"),
        },
    )
    caud_0xb4a84d85: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB4A84D85, original_name="CAUD"),
        },
    )
    caud_0xfef01104: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xFEF01104, original_name="CAUD"),
        },
    )
    caud_0xeb8805bd: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEB8805BD, original_name="CAUD"),
        },
    )
    sound_fireball_loop: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x657327CD, original_name="Sound_FireballLoop"),
        },
    )
    unknown_0xa99ccb84: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA99CCB84, original_name="Unknown"),
        },
    )
    unknown_0xb60df150: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB60DF150, original_name="Unknown"),
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
        if property_count != 26:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FAB452A
        scan = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC47A5224
        helmet_l_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38FABDE9
        helmet_r_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4BA2833E
        optic_array_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC60FB911
        jammer_antenna_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x537F8382
        part_0x537f8382 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98D5883D
        jammer_antenna_explosion_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD17A036
        part_0xad17a036 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FEF37BD
        leg_collision_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBD321538
        visor_electric_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70E97166
        missile_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9EEF71C2
        huge_missile_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF98FDCC9
        seeker_bomb_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDBF176DD
        part_0xdbf176dd = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7AF488B1
        death_gibs = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD6BE17F
        part_0xdd6be17f = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CC93984
        max_grapple_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF609C637
        grapple_data = GrappleData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C558C5D
        sound_jump_loop = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3220B78
        sound_bomb_loop = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB4A84D85
        caud_0xb4a84d85 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFEF01104
        caud_0xfef01104 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB8805BD
        caud_0xeb8805bd = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x657327CD
        sound_fireball_loop = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA99CCB84
        unknown_0xa99ccb84 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB60DF150
        unknown_0xb60df150 = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            scan,
            helmet_l_model,
            helmet_r_model,
            optic_array_model,
            jammer_antenna_model,
            part_0x537f8382,
            jammer_antenna_explosion_effect,
            part_0xad17a036,
            leg_collision_effect,
            visor_electric_effect,
            missile_projectile,
            huge_missile_projectile,
            seeker_bomb_effect,
            part_0xdbf176dd,
            death_gibs,
            part_0xdd6be17f,
            max_grapple_distance,
            grapple_data,
            sound_jump_loop,
            sound_bomb_loop,
            caud_0xb4a84d85,
            caud_0xfef01104,
            caud_0xeb8805bd,
            sound_fireball_loop,
            unknown_0xa99ccb84,
            unknown_0xb60df150,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1a")  # 26 properties

        data.write(b"\x7f\xabE*")  # 0x7fab452a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan))

        data.write(b"\xc4zR$")  # 0xc47a5224
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.helmet_l_model))

        data.write(b"8\xfa\xbd\xe9")  # 0x38fabde9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.helmet_r_model))

        data.write(b"K\xa2\x83>")  # 0x4ba2833e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.optic_array_model))

        data.write(b"\xc6\x0f\xb9\x11")  # 0xc60fb911
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.jammer_antenna_model))

        data.write(b"S\x7f\x83\x82")  # 0x537f8382
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0x537f8382))

        data.write(b"\x98\xd5\x88=")  # 0x98d5883d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.jammer_antenna_explosion_effect))

        data.write(b"\xad\x17\xa06")  # 0xad17a036
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xad17a036))

        data.write(b"?\xef7\xbd")  # 0x3fef37bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.leg_collision_effect))

        data.write(b"\xbd2\x158")  # 0xbd321538
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.visor_electric_effect))

        data.write(b"p\xe9qf")  # 0x70e97166
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.missile_projectile))

        data.write(b"\x9e\xefq\xc2")  # 0x9eef71c2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.huge_missile_projectile))

        data.write(b"\xf9\x8f\xdc\xc9")  # 0xf98fdcc9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.seeker_bomb_effect))

        data.write(b"\xdb\xf1v\xdd")  # 0xdbf176dd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xdbf176dd))

        data.write(b"z\xf4\x88\xb1")  # 0x7af488b1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death_gibs))

        data.write(b"\xddk\xe1\x7f")  # 0xdd6be17f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part_0xdd6be17f))

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

        data.write(b",U\x8c]")  # 0x2c558c5d
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_jump_loop))

        data.write(b'\xb3"\x0bx')  # 0xb3220b78
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_bomb_loop))

        data.write(b"\xb4\xa8M\x85")  # 0xb4a84d85
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xb4a84d85))

        data.write(b"\xfe\xf0\x11\x04")  # 0xfef01104
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xfef01104))

        data.write(b"\xeb\x88\x05\xbd")  # 0xeb8805bd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0xeb8805bd))

        data.write(b"es'\xcd")  # 0x657327cd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound_fireball_loop))

        data.write(b"\xa9\x9c\xcb\x84")  # 0xa99ccb84
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xa99ccb84))

        data.write(b"\xb6\r\xf1P")  # 0xb60df150
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xb60df150))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct26Json", data)
        return cls(
            scan=json_data["scan"],
            helmet_l_model=json_data["helmet_l_model"],
            helmet_r_model=json_data["helmet_r_model"],
            optic_array_model=json_data["optic_array_model"],
            jammer_antenna_model=json_data["jammer_antenna_model"],
            part_0x537f8382=json_data["part_0x537f8382"],
            jammer_antenna_explosion_effect=json_data["jammer_antenna_explosion_effect"],
            part_0xad17a036=json_data["part_0xad17a036"],
            leg_collision_effect=json_data["leg_collision_effect"],
            visor_electric_effect=json_data["visor_electric_effect"],
            missile_projectile=json_data["missile_projectile"],
            huge_missile_projectile=json_data["huge_missile_projectile"],
            seeker_bomb_effect=json_data["seeker_bomb_effect"],
            part_0xdbf176dd=json_data["part_0xdbf176dd"],
            death_gibs=json_data["death_gibs"],
            part_0xdd6be17f=json_data["part_0xdd6be17f"],
            max_grapple_distance=json_data["max_grapple_distance"],
            grapple_data=GrappleData.from_json(json_data["grapple_data"]),
            sound_jump_loop=json_data["sound_jump_loop"],
            sound_bomb_loop=json_data["sound_bomb_loop"],
            caud_0xb4a84d85=json_data["caud_0xb4a84d85"],
            caud_0xfef01104=json_data["caud_0xfef01104"],
            caud_0xeb8805bd=json_data["caud_0xeb8805bd"],
            sound_fireball_loop=json_data["sound_fireball_loop"],
            unknown_0xa99ccb84=json_data["unknown_0xa99ccb84"],
            unknown_0xb60df150=json_data["unknown_0xb60df150"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scan": self.scan,
            "helmet_l_model": self.helmet_l_model,
            "helmet_r_model": self.helmet_r_model,
            "optic_array_model": self.optic_array_model,
            "jammer_antenna_model": self.jammer_antenna_model,
            "part_0x537f8382": self.part_0x537f8382,
            "jammer_antenna_explosion_effect": self.jammer_antenna_explosion_effect,
            "part_0xad17a036": self.part_0xad17a036,
            "leg_collision_effect": self.leg_collision_effect,
            "visor_electric_effect": self.visor_electric_effect,
            "missile_projectile": self.missile_projectile,
            "huge_missile_projectile": self.huge_missile_projectile,
            "seeker_bomb_effect": self.seeker_bomb_effect,
            "part_0xdbf176dd": self.part_0xdbf176dd,
            "death_gibs": self.death_gibs,
            "part_0xdd6be17f": self.part_0xdd6be17f,
            "max_grapple_distance": self.max_grapple_distance,
            "grapple_data": self.grapple_data.to_json(),
            "sound_jump_loop": self.sound_jump_loop,
            "sound_bomb_loop": self.sound_bomb_loop,
            "caud_0xb4a84d85": self.caud_0xb4a84d85,
            "caud_0xfef01104": self.caud_0xfef01104,
            "caud_0xeb8805bd": self.caud_0xeb8805bd,
            "sound_fireball_loop": self.sound_fireball_loop,
            "unknown_0xa99ccb84": self.unknown_0xa99ccb84,
            "unknown_0xb60df150": self.unknown_0xb60df150,
        }


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FAB452A: ("scan", structs.decode_BIG_Q),
    0xC47A5224: ("helmet_l_model", structs.decode_BIG_Q),
    0x38FABDE9: ("helmet_r_model", structs.decode_BIG_Q),
    0x4BA2833E: ("optic_array_model", structs.decode_BIG_Q),
    0xC60FB911: ("jammer_antenna_model", structs.decode_BIG_Q),
    0x537F8382: ("part_0x537f8382", structs.decode_BIG_Q),
    0x98D5883D: ("jammer_antenna_explosion_effect", structs.decode_BIG_Q),
    0xAD17A036: ("part_0xad17a036", structs.decode_BIG_Q),
    0x3FEF37BD: ("leg_collision_effect", structs.decode_BIG_Q),
    0xBD321538: ("visor_electric_effect", structs.decode_BIG_Q),
    0x70E97166: ("missile_projectile", structs.decode_BIG_Q),
    0x9EEF71C2: ("huge_missile_projectile", structs.decode_BIG_Q),
    0xF98FDCC9: ("seeker_bomb_effect", structs.decode_BIG_Q),
    0xDBF176DD: ("part_0xdbf176dd", structs.decode_BIG_Q),
    0x7AF488B1: ("death_gibs", structs.decode_BIG_Q),
    0xDD6BE17F: ("part_0xdd6be17f", structs.decode_BIG_Q),
    0x1CC93984: ("max_grapple_distance", structs.decode_BIG_f),
    0xF609C637: ("grapple_data", _decode_grapple_data),
    0x2C558C5D: ("sound_jump_loop", structs.decode_BIG_Q),
    0xB3220B78: ("sound_bomb_loop", structs.decode_BIG_Q),
    0xB4A84D85: ("caud_0xb4a84d85", structs.decode_BIG_Q),
    0xFEF01104: ("caud_0xfef01104", structs.decode_BIG_Q),
    0xEB8805BD: ("caud_0xeb8805bd", structs.decode_BIG_Q),
    0x657327CD: ("sound_fireball_loop", structs.decode_BIG_Q),
    0xA99CCB84: ("unknown_0xa99ccb84", structs.decode_BIG_Q),
    0xB60DF150: ("unknown_0xb60df150", structs.decode_BIG_Q),
}
