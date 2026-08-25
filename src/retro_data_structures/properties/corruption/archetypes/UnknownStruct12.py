# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct7 import UnknownStruct7
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct12Json(typing_extensions.TypedDict):
        projectile: int
        damage: json_util.JsonObject
        weapon_info: json_util.JsonObject
        unknown_0xc2f2b95c: int
        unknown_0xeb8c4444: int
        unknown_0x6e7f4d8c: float
        unknown_0x7d3aab27: float
        unknown_0xb84c1410: float
        unknown_0x08730e2c: float
        turn_speed: float
        unknown_0xb638cfa7: float
        unknown_0x18505e36: float
        dongle_vulnerability: json_util.JsonObject
        dongle_model: int
        dongle_hinge1_model: int
        dongle_hinge2_model: int
        dongle_hinge3_model: int
        dongle_hinge4_model: int
        dongle_health: float
        unknown_struct7: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct12(BaseProperty):
    projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEF485DB9, original_name="Projectile"),
        },
    )
    damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x337F9524,
                original_name="Damage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    weapon_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x85DCA565,
                original_name="WeaponInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    unknown_0xc2f2b95c: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC2F2B95C, original_name="Unknown"),
        },
    )
    unknown_0xeb8c4444: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xEB8C4444, original_name="Unknown"),
        },
    )
    unknown_0x6e7f4d8c: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6E7F4D8C, original_name="Unknown"),
        },
    )
    unknown_0x7d3aab27: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D3AAB27, original_name="Unknown"),
        },
    )
    unknown_0xb84c1410: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB84C1410, original_name="Unknown"),
        },
    )
    unknown_0x08730e2c: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08730E2C, original_name="Unknown"),
        },
    )
    turn_speed: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x020C78BB, original_name="TurnSpeed"),
        },
    )
    unknown_0xb638cfa7: float = dataclasses.field(
        default=1.2999999523162842,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB638CFA7, original_name="Unknown"),
        },
    )
    unknown_0x18505e36: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x18505E36, original_name="Unknown"),
        },
    )
    dongle_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0x6A98EEF6,
                original_name="DongleVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    dongle_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x19AAF8F3, original_name="DongleModel"),
        },
    )
    dongle_hinge1_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5FCA665E, original_name="DongleHinge1Model"),
        },
    )
    dongle_hinge2_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC628005F, original_name="DongleHinge2Model"),
        },
    )
    dongle_hinge3_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x07A6DF9F, original_name="DongleHinge3Model"),
        },
    )
    dongle_hinge4_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2E9DCA1C, original_name="DongleHinge4Model"),
        },
    )
    dongle_health: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA90E610C, original_name="DongleHealth"),
        },
    )
    unknown_struct7: UnknownStruct7 = dataclasses.field(
        default_factory=UnknownStruct7,
        metadata={
            "reflection": FieldReflection[UnknownStruct7](
                UnknownStruct7,
                id=0x659DF76D,
                original_name="UnknownStruct7",
                from_json=UnknownStruct7.from_json,
                to_json=UnknownStruct7.to_json,
            ),
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
        if property_count != 20:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85DCA565
        weapon_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2F2B95C
        unknown_0xc2f2b95c = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEB8C4444
        unknown_0xeb8c4444 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E7F4D8C
        unknown_0x6e7f4d8c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D3AAB27
        unknown_0x7d3aab27 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB84C1410
        unknown_0xb84c1410 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08730E2C
        unknown_0x08730e2c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020C78BB
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB638CFA7
        unknown_0xb638cfa7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18505E36
        unknown_0x18505e36 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6A98EEF6
        dongle_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19AAF8F3
        dongle_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FCA665E
        dongle_hinge1_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC628005F
        dongle_hinge2_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07A6DF9F
        dongle_hinge3_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E9DCA1C
        dongle_hinge4_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA90E610C
        dongle_health = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x659DF76D
        unknown_struct7 = UnknownStruct7.from_stream(data, game, property_size)

        return cls(
            projectile,
            damage,
            weapon_info,
            unknown_0xc2f2b95c,
            unknown_0xeb8c4444,
            unknown_0x6e7f4d8c,
            unknown_0x7d3aab27,
            unknown_0xb84c1410,
            unknown_0x08730e2c,
            turn_speed,
            unknown_0xb638cfa7,
            unknown_0x18505e36,
            dongle_vulnerability,
            dongle_model,
            dongle_hinge1_model,
            dongle_hinge2_model,
            dongle_hinge3_model,
            dongle_hinge4_model,
            dongle_health,
            unknown_struct7,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x14")  # 20 properties

        data.write(b"\xefH]\xb9")  # 0xef485db9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.projectile))

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x85\xdc\xa5e")  # 0x85dca565
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc2\xf2\xb9\\")  # 0xc2f2b95c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc2f2b95c))

        data.write(b"\xeb\x8cDD")  # 0xeb8c4444
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xeb8c4444))

        data.write(b"n\x7fM\x8c")  # 0x6e7f4d8c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6e7f4d8c))

        data.write(b"}:\xab'")  # 0x7d3aab27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7d3aab27))

        data.write(b"\xb8L\x14\x10")  # 0xb84c1410
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb84c1410))

        data.write(b"\x08s\x0e,")  # 0x8730e2c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x08730e2c))

        data.write(b"\x02\x0cx\xbb")  # 0x20c78bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b"\xb68\xcf\xa7")  # 0xb638cfa7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb638cfa7))

        data.write(b"\x18P^6")  # 0x18505e36
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x18505e36))

        data.write(b"j\x98\xee\xf6")  # 0x6a98eef6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.dongle_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\xaa\xf8\xf3")  # 0x19aaf8f3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.dongle_model))

        data.write(b"_\xcaf^")  # 0x5fca665e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge1_model))

        data.write(b"\xc6(\x00_")  # 0xc628005f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge2_model))

        data.write(b"\x07\xa6\xdf\x9f")  # 0x7a6df9f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge3_model))

        data.write(b".\x9d\xca\x1c")  # 0x2e9dca1c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge4_model))

        data.write(b"\xa9\x0ea\x0c")  # 0xa90e610c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dongle_health))

        data.write(b"e\x9d\xf7m")  # 0x659df76d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct12Json", data)
        return cls(
            projectile=json_data["projectile"],
            damage=DamageInfo.from_json(json_data["damage"]),
            weapon_info=ShockWaveInfo.from_json(json_data["weapon_info"]),
            unknown_0xc2f2b95c=json_data["unknown_0xc2f2b95c"],
            unknown_0xeb8c4444=json_data["unknown_0xeb8c4444"],
            unknown_0x6e7f4d8c=json_data["unknown_0x6e7f4d8c"],
            unknown_0x7d3aab27=json_data["unknown_0x7d3aab27"],
            unknown_0xb84c1410=json_data["unknown_0xb84c1410"],
            unknown_0x08730e2c=json_data["unknown_0x08730e2c"],
            turn_speed=json_data["turn_speed"],
            unknown_0xb638cfa7=json_data["unknown_0xb638cfa7"],
            unknown_0x18505e36=json_data["unknown_0x18505e36"],
            dongle_vulnerability=DamageVulnerability.from_json(json_data["dongle_vulnerability"]),
            dongle_model=json_data["dongle_model"],
            dongle_hinge1_model=json_data["dongle_hinge1_model"],
            dongle_hinge2_model=json_data["dongle_hinge2_model"],
            dongle_hinge3_model=json_data["dongle_hinge3_model"],
            dongle_hinge4_model=json_data["dongle_hinge4_model"],
            dongle_health=json_data["dongle_health"],
            unknown_struct7=UnknownStruct7.from_json(json_data["unknown_struct7"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "projectile": self.projectile,
            "damage": self.damage.to_json(),
            "weapon_info": self.weapon_info.to_json(),
            "unknown_0xc2f2b95c": self.unknown_0xc2f2b95c,
            "unknown_0xeb8c4444": self.unknown_0xeb8c4444,
            "unknown_0x6e7f4d8c": self.unknown_0x6e7f4d8c,
            "unknown_0x7d3aab27": self.unknown_0x7d3aab27,
            "unknown_0xb84c1410": self.unknown_0xb84c1410,
            "unknown_0x08730e2c": self.unknown_0x08730e2c,
            "turn_speed": self.turn_speed,
            "unknown_0xb638cfa7": self.unknown_0xb638cfa7,
            "unknown_0x18505e36": self.unknown_0x18505e36,
            "dongle_vulnerability": self.dongle_vulnerability.to_json(),
            "dongle_model": self.dongle_model,
            "dongle_hinge1_model": self.dongle_hinge1_model,
            "dongle_hinge2_model": self.dongle_hinge2_model,
            "dongle_hinge3_model": self.dongle_hinge3_model,
            "dongle_hinge4_model": self.dongle_hinge4_model,
            "dongle_health": self.dongle_health,
            "unknown_struct7": self.unknown_struct7.to_json(),
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_weapon_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_dongle_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_unknown_struct7(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct7:
    return UnknownStruct7.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xEF485DB9: ("projectile", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0x85DCA565: ("weapon_info", _decode_weapon_info),
    0xC2F2B95C: ("unknown_0xc2f2b95c", structs.decode_BIG_l),
    0xEB8C4444: ("unknown_0xeb8c4444", structs.decode_BIG_l),
    0x6E7F4D8C: ("unknown_0x6e7f4d8c", structs.decode_BIG_f),
    0x7D3AAB27: ("unknown_0x7d3aab27", structs.decode_BIG_f),
    0xB84C1410: ("unknown_0xb84c1410", structs.decode_BIG_f),
    0x08730E2C: ("unknown_0x08730e2c", structs.decode_BIG_f),
    0x020C78BB: ("turn_speed", structs.decode_BIG_f),
    0xB638CFA7: ("unknown_0xb638cfa7", structs.decode_BIG_f),
    0x18505E36: ("unknown_0x18505e36", structs.decode_BIG_f),
    0x6A98EEF6: ("dongle_vulnerability", _decode_dongle_vulnerability),
    0x19AAF8F3: ("dongle_model", structs.decode_BIG_Q),
    0x5FCA665E: ("dongle_hinge1_model", structs.decode_BIG_Q),
    0xC628005F: ("dongle_hinge2_model", structs.decode_BIG_Q),
    0x07A6DF9F: ("dongle_hinge3_model", structs.decode_BIG_Q),
    0x2E9DCA1C: ("dongle_hinge4_model", structs.decode_BIG_Q),
    0xA90E610C: ("dongle_health", structs.decode_BIG_f),
    0x659DF76D: ("unknown_struct7", _decode_unknown_struct7),
}
