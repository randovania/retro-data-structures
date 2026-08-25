# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PhazonHarvesterDataJson(typing_extensions.TypedDict):
        starts_flying: bool
        weapon_projectile: json_util.JsonObject
        weapon_vulnerability: json_util.JsonObject
        weapon_stun_damage: float
        unknown_0x6b554a8d: float
        unknown_0x08772297: float
        unknown_0xee178d76: float
        weapon_max_pitch: float
        weapon_min_pitch: float
        max_weapon_rotation: float
        weapon_rotation_speed: float
        hatch_open_time: float
        hatch_close_time: float
        flight_normal: json_util.JsonObject
        flight_attack: json_util.JsonObject
        weapon_model: int
        left_front_hatch_model: int
        left_back_hatch_model: int
        right_fron_hatch_model: int
        right_back_hatch_model: int


@dataclasses.dataclass()
class PhazonHarvesterData(BaseProperty):
    starts_flying: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1CE8F439, original_name="StartsFlying"),
        },
    )
    weapon_projectile: LaunchProjectileData = dataclasses.field(
        default_factory=LaunchProjectileData,
        metadata={
            "reflection": FieldReflection[LaunchProjectileData](
                LaunchProjectileData,
                id=0x2036077F,
                original_name="WeaponProjectile",
                from_json=LaunchProjectileData.from_json,
                to_json=LaunchProjectileData.to_json,
            ),
        },
    )
    weapon_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xAE22E0DC,
                original_name="WeaponVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    weapon_stun_damage: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4FDC1683, original_name="WeaponStunDamage"),
        },
    )
    unknown_0x6b554a8d: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6B554A8D, original_name="Unknown"),
        },
    )
    unknown_0x08772297: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08772297, original_name="Unknown"),
        },
    )
    unknown_0xee178d76: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEE178D76, original_name="Unknown"),
        },
    )
    weapon_max_pitch: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x75608ED3, original_name="WeaponMaxPitch"),
        },
    )
    weapon_min_pitch: float = dataclasses.field(
        default=-90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x352FF6A5, original_name="WeaponMinPitch"),
        },
    )
    max_weapon_rotation: float = dataclasses.field(
        default=70.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCD8AB1E3, original_name="MaxWeaponRotation"),
        },
    )
    weapon_rotation_speed: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0E64D85, original_name="WeaponRotationSpeed"),
        },
    )
    hatch_open_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2B3449F5, original_name="HatchOpenTime"),
        },
    )
    hatch_close_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1DD9E8BF, original_name="HatchCloseTime"),
        },
    )
    flight_normal: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0x130CF1A1,
                original_name="FlightNormal",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    flight_attack: FlyerMovementMode = dataclasses.field(
        default_factory=FlyerMovementMode,
        metadata={
            "reflection": FieldReflection[FlyerMovementMode](
                FlyerMovementMode,
                id=0xFC51DF90,
                original_name="FlightAttack",
                from_json=FlyerMovementMode.from_json,
                to_json=FlyerMovementMode.to_json,
            ),
        },
    )
    weapon_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x7A154E49, original_name="WeaponModel"),
        },
    )
    left_front_hatch_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC7426B90, original_name="LeftFrontHatchModel"),
        },
    )
    left_back_hatch_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE2EFEE98, original_name="LeftBackHatchModel"),
        },
    )
    right_fron_hatch_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x155BF24B, original_name="RightFronHatchModel"),
        },
    )
    right_back_hatch_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD757CB94, original_name="RightBackHatchModel"),
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
        assert property_id == 0x1CE8F439
        starts_flying = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2036077F
        weapon_projectile = LaunchProjectileData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE22E0DC
        weapon_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4FDC1683
        weapon_stun_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6B554A8D
        unknown_0x6b554a8d = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08772297
        unknown_0x08772297 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEE178D76
        unknown_0xee178d76 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75608ED3
        weapon_max_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x352FF6A5
        weapon_min_pitch = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD8AB1E3
        max_weapon_rotation = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0E64D85
        weapon_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B3449F5
        hatch_open_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1DD9E8BF
        hatch_close_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x130CF1A1
        flight_normal = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC51DF90
        flight_attack = FlyerMovementMode.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A154E49
        weapon_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC7426B90
        left_front_hatch_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2EFEE98
        left_back_hatch_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x155BF24B
        right_fron_hatch_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD757CB94
        right_back_hatch_model = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            starts_flying,
            weapon_projectile,
            weapon_vulnerability,
            weapon_stun_damage,
            unknown_0x6b554a8d,
            unknown_0x08772297,
            unknown_0xee178d76,
            weapon_max_pitch,
            weapon_min_pitch,
            max_weapon_rotation,
            weapon_rotation_speed,
            hatch_open_time,
            hatch_close_time,
            flight_normal,
            flight_attack,
            weapon_model,
            left_front_hatch_model,
            left_back_hatch_model,
            right_fron_hatch_model,
            right_back_hatch_model,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x14")  # 20 properties

        data.write(b"\x1c\xe8\xf49")  # 0x1ce8f439
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.starts_flying))

        data.write(b" 6\x07\x7f")  # 0x2036077f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xae"\xe0\xdc')  # 0xae22e0dc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"O\xdc\x16\x83")  # 0x4fdc1683
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.weapon_stun_damage))

        data.write(b"kUJ\x8d")  # 0x6b554a8d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6b554a8d))

        data.write(b'\x08w"\x97')  # 0x8772297
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x08772297))

        data.write(b"\xee\x17\x8dv")  # 0xee178d76
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xee178d76))

        data.write(b"u`\x8e\xd3")  # 0x75608ed3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.weapon_max_pitch))

        data.write(b"5/\xf6\xa5")  # 0x352ff6a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.weapon_min_pitch))

        data.write(b"\xcd\x8a\xb1\xe3")  # 0xcd8ab1e3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_weapon_rotation))

        data.write(b"\xf0\xe6M\x85")  # 0xf0e64d85
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.weapon_rotation_speed))

        data.write(b"+4I\xf5")  # 0x2b3449f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hatch_open_time))

        data.write(b"\x1d\xd9\xe8\xbf")  # 0x1dd9e8bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hatch_close_time))

        data.write(b"\x13\x0c\xf1\xa1")  # 0x130cf1a1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flight_normal.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfcQ\xdf\x90")  # 0xfc51df90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flight_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"z\x15NI")  # 0x7a154e49
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.weapon_model))

        data.write(b"\xc7Bk\x90")  # 0xc7426b90
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_front_hatch_model))

        data.write(b"\xe2\xef\xee\x98")  # 0xe2efee98
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left_back_hatch_model))

        data.write(b"\x15[\xf2K")  # 0x155bf24b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_fron_hatch_model))

        data.write(b"\xd7W\xcb\x94")  # 0xd757cb94
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right_back_hatch_model))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PhazonHarvesterDataJson", data)
        return cls(
            starts_flying=json_data["starts_flying"],
            weapon_projectile=LaunchProjectileData.from_json(json_data["weapon_projectile"]),
            weapon_vulnerability=DamageVulnerability.from_json(json_data["weapon_vulnerability"]),
            weapon_stun_damage=json_data["weapon_stun_damage"],
            unknown_0x6b554a8d=json_data["unknown_0x6b554a8d"],
            unknown_0x08772297=json_data["unknown_0x08772297"],
            unknown_0xee178d76=json_data["unknown_0xee178d76"],
            weapon_max_pitch=json_data["weapon_max_pitch"],
            weapon_min_pitch=json_data["weapon_min_pitch"],
            max_weapon_rotation=json_data["max_weapon_rotation"],
            weapon_rotation_speed=json_data["weapon_rotation_speed"],
            hatch_open_time=json_data["hatch_open_time"],
            hatch_close_time=json_data["hatch_close_time"],
            flight_normal=FlyerMovementMode.from_json(json_data["flight_normal"]),
            flight_attack=FlyerMovementMode.from_json(json_data["flight_attack"]),
            weapon_model=json_data["weapon_model"],
            left_front_hatch_model=json_data["left_front_hatch_model"],
            left_back_hatch_model=json_data["left_back_hatch_model"],
            right_fron_hatch_model=json_data["right_fron_hatch_model"],
            right_back_hatch_model=json_data["right_back_hatch_model"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "starts_flying": self.starts_flying,
            "weapon_projectile": self.weapon_projectile.to_json(),
            "weapon_vulnerability": self.weapon_vulnerability.to_json(),
            "weapon_stun_damage": self.weapon_stun_damage,
            "unknown_0x6b554a8d": self.unknown_0x6b554a8d,
            "unknown_0x08772297": self.unknown_0x08772297,
            "unknown_0xee178d76": self.unknown_0xee178d76,
            "weapon_max_pitch": self.weapon_max_pitch,
            "weapon_min_pitch": self.weapon_min_pitch,
            "max_weapon_rotation": self.max_weapon_rotation,
            "weapon_rotation_speed": self.weapon_rotation_speed,
            "hatch_open_time": self.hatch_open_time,
            "hatch_close_time": self.hatch_close_time,
            "flight_normal": self.flight_normal.to_json(),
            "flight_attack": self.flight_attack.to_json(),
            "weapon_model": self.weapon_model,
            "left_front_hatch_model": self.left_front_hatch_model,
            "left_back_hatch_model": self.left_back_hatch_model,
            "right_fron_hatch_model": self.right_fron_hatch_model,
            "right_back_hatch_model": self.right_back_hatch_model,
        }


def _decode_weapon_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_weapon_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_flight_normal(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_flight_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1CE8F439: ("starts_flying", structs.decode_BIG_bool_),
    0x2036077F: ("weapon_projectile", _decode_weapon_projectile),
    0xAE22E0DC: ("weapon_vulnerability", _decode_weapon_vulnerability),
    0x4FDC1683: ("weapon_stun_damage", structs.decode_BIG_f),
    0x6B554A8D: ("unknown_0x6b554a8d", structs.decode_BIG_f),
    0x08772297: ("unknown_0x08772297", structs.decode_BIG_f),
    0xEE178D76: ("unknown_0xee178d76", structs.decode_BIG_f),
    0x75608ED3: ("weapon_max_pitch", structs.decode_BIG_f),
    0x352FF6A5: ("weapon_min_pitch", structs.decode_BIG_f),
    0xCD8AB1E3: ("max_weapon_rotation", structs.decode_BIG_f),
    0xF0E64D85: ("weapon_rotation_speed", structs.decode_BIG_f),
    0x2B3449F5: ("hatch_open_time", structs.decode_BIG_f),
    0x1DD9E8BF: ("hatch_close_time", structs.decode_BIG_f),
    0x130CF1A1: ("flight_normal", _decode_flight_normal),
    0xFC51DF90: ("flight_attack", _decode_flight_attack),
    0x7A154E49: ("weapon_model", structs.decode_BIG_Q),
    0xC7426B90: ("left_front_hatch_model", structs.decode_BIG_Q),
    0xE2EFEE98: ("left_back_hatch_model", structs.decode_BIG_Q),
    0x155BF24B: ("right_fron_hatch_model", structs.decode_BIG_Q),
    0xD757CB94: ("right_back_hatch_model", structs.decode_BIG_Q),
}
