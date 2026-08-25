# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct11Json(typing_extensions.TypedDict):
        shield_charge_damage: json_util.JsonObject
        shield_vulnerability: json_util.JsonObject
        unknown_0xc1d9dbc6: float
        unknown_0x927fc322: float
        shield_charge_speed: float
        shield_explode_effect: int
        sound_shield_explode: int
        unknown_0x6cb0da5a: float
        unknown_0xc3938663: float
        arm_shield_chance: float
        arm_shield_time: float
        unknown_0xe1b0efa0: float
        arm_shield_explode_effect: int
        shield_charge_effect: int
        arm_shield_effect: int
        sound_0xbf3c59b6: int
        sound_0x78be3b8d: int


@dataclasses.dataclass()
class UnknownStruct11(BaseProperty):
    shield_charge_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4DA4A894,
                original_name="ShieldChargeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    shield_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xD34F1323,
                original_name="ShieldVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_0xc1d9dbc6: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC1D9DBC6, original_name="Unknown"),
        },
    )
    unknown_0x927fc322: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x927FC322, original_name="Unknown"),
        },
    )
    shield_charge_speed: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x717824B4, original_name="ShieldChargeSpeed"),
        },
    )
    shield_explode_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA41F75EF, original_name="ShieldExplodeEffect"),
        },
    )
    sound_shield_explode: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE6E92E73, original_name="Sound_ShieldExplode"),
        },
    )
    unknown_0x6cb0da5a: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6CB0DA5A, original_name="Unknown"),
        },
    )
    unknown_0xc3938663: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3938663, original_name="Unknown"),
        },
    )
    arm_shield_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x865C109C, original_name="ArmShieldChance"),
        },
    )
    arm_shield_time: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B48A2F8, original_name="ArmShieldTime"),
        },
    )
    unknown_0xe1b0efa0: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE1B0EFA0, original_name="Unknown"),
        },
    )
    arm_shield_explode_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x5CA206CA, original_name="ArmShieldExplodeEffect"),
        },
    )
    shield_charge_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEBF69CF0, original_name="ShieldChargeEffect"),
        },
    )
    arm_shield_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4AAB4E04, original_name="ArmShieldEffect"),
        },
    )
    sound_0xbf3c59b6: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xBF3C59B6, original_name="Sound"),
        },
    )
    sound_0x78be3b8d: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x78BE3B8D, original_name="Sound"),
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
        if property_count != 17:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4DA4A894
        shield_charge_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_knock_back_power": 5.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD34F1323
        shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC1D9DBC6
        unknown_0xc1d9dbc6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x927FC322
        unknown_0x927fc322 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x717824B4
        shield_charge_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA41F75EF
        shield_explode_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE6E92E73
        sound_shield_explode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6CB0DA5A
        unknown_0x6cb0da5a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3938663
        unknown_0xc3938663 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x865C109C
        arm_shield_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B48A2F8
        arm_shield_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1B0EFA0
        unknown_0xe1b0efa0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5CA206CA
        arm_shield_explode_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBF69CF0
        shield_charge_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AAB4E04
        arm_shield_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF3C59B6
        sound_0xbf3c59b6 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78BE3B8D
        sound_0x78be3b8d = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            shield_charge_damage,
            shield_vulnerability,
            unknown_0xc1d9dbc6,
            unknown_0x927fc322,
            shield_charge_speed,
            shield_explode_effect,
            sound_shield_explode,
            unknown_0x6cb0da5a,
            unknown_0xc3938663,
            arm_shield_chance,
            arm_shield_time,
            unknown_0xe1b0efa0,
            arm_shield_explode_effect,
            shield_charge_effect,
            arm_shield_effect,
            sound_0xbf3c59b6,
            sound_0x78be3b8d,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x11")  # 17 properties

        data.write(b"M\xa4\xa8\x94")  # 0x4da4a894
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shield_charge_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_knock_back_power": 5.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd3O\x13#")  # 0xd34f1323
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc1\xd9\xdb\xc6")  # 0xc1d9dbc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc1d9dbc6))

        data.write(b'\x92\x7f\xc3"')  # 0x927fc322
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x927fc322))

        data.write(b"qx$\xb4")  # 0x717824b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shield_charge_speed))

        data.write(b"\xa4\x1fu\xef")  # 0xa41f75ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shield_explode_effect))

        data.write(b"\xe6\xe9.s")  # 0xe6e92e73
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_shield_explode))

        data.write(b"l\xb0\xdaZ")  # 0x6cb0da5a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6cb0da5a))

        data.write(b"\xc3\x93\x86c")  # 0xc3938663
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc3938663))

        data.write(b"\x86\\\x10\x9c")  # 0x865c109c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arm_shield_chance))

        data.write(b"\x8bH\xa2\xf8")  # 0x8b48a2f8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.arm_shield_time))

        data.write(b"\xe1\xb0\xef\xa0")  # 0xe1b0efa0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe1b0efa0))

        data.write(b"\\\xa2\x06\xca")  # 0x5ca206ca
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.arm_shield_explode_effect))

        data.write(b"\xeb\xf6\x9c\xf0")  # 0xebf69cf0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shield_charge_effect))

        data.write(b"J\xabN\x04")  # 0x4aab4e04
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.arm_shield_effect))

        data.write(b"\xbf<Y\xb6")  # 0xbf3c59b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0xbf3c59b6))

        data.write(b"x\xbe;\x8d")  # 0x78be3b8d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_0x78be3b8d))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct11Json", data)
        return cls(
            shield_charge_damage=DamageInfo.from_json(json_data["shield_charge_damage"]),
            shield_vulnerability=DamageVulnerability.from_json(json_data["shield_vulnerability"]),
            unknown_0xc1d9dbc6=json_data["unknown_0xc1d9dbc6"],
            unknown_0x927fc322=json_data["unknown_0x927fc322"],
            shield_charge_speed=json_data["shield_charge_speed"],
            shield_explode_effect=json_data["shield_explode_effect"],
            sound_shield_explode=json_data["sound_shield_explode"],
            unknown_0x6cb0da5a=json_data["unknown_0x6cb0da5a"],
            unknown_0xc3938663=json_data["unknown_0xc3938663"],
            arm_shield_chance=json_data["arm_shield_chance"],
            arm_shield_time=json_data["arm_shield_time"],
            unknown_0xe1b0efa0=json_data["unknown_0xe1b0efa0"],
            arm_shield_explode_effect=json_data["arm_shield_explode_effect"],
            shield_charge_effect=json_data["shield_charge_effect"],
            arm_shield_effect=json_data["arm_shield_effect"],
            sound_0xbf3c59b6=json_data["sound_0xbf3c59b6"],
            sound_0x78be3b8d=json_data["sound_0x78be3b8d"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "shield_charge_damage": self.shield_charge_damage.to_json(),
            "shield_vulnerability": self.shield_vulnerability.to_json(),
            "unknown_0xc1d9dbc6": self.unknown_0xc1d9dbc6,
            "unknown_0x927fc322": self.unknown_0x927fc322,
            "shield_charge_speed": self.shield_charge_speed,
            "shield_explode_effect": self.shield_explode_effect,
            "sound_shield_explode": self.sound_shield_explode,
            "unknown_0x6cb0da5a": self.unknown_0x6cb0da5a,
            "unknown_0xc3938663": self.unknown_0xc3938663,
            "arm_shield_chance": self.arm_shield_chance,
            "arm_shield_time": self.arm_shield_time,
            "unknown_0xe1b0efa0": self.unknown_0xe1b0efa0,
            "arm_shield_explode_effect": self.arm_shield_explode_effect,
            "shield_charge_effect": self.shield_charge_effect,
            "arm_shield_effect": self.arm_shield_effect,
            "sound_0xbf3c59b6": self.sound_0xbf3c59b6,
            "sound_0x78be3b8d": self.sound_0x78be3b8d,
        }

    def _dependencies_for_shield_explode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_explode_effect)

    def _dependencies_for_sound_shield_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_shield_explode)

    def _dependencies_for_arm_shield_explode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.arm_shield_explode_effect)

    def _dependencies_for_shield_charge_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_charge_effect)

    def _dependencies_for_arm_shield_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.arm_shield_effect)

    def _dependencies_for_sound_0xbf3c59b6(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0xbf3c59b6)

    def _dependencies_for_sound_0x78be3b8d(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_0x78be3b8d)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_shield_explode_effect, "shield_explode_effect", "AssetId"),
            (self._dependencies_for_sound_shield_explode, "sound_shield_explode", "int"),
            (self._dependencies_for_arm_shield_explode_effect, "arm_shield_explode_effect", "AssetId"),
            (self._dependencies_for_shield_charge_effect, "shield_charge_effect", "AssetId"),
            (self._dependencies_for_arm_shield_effect, "arm_shield_effect", "AssetId"),
            (self._dependencies_for_sound_0xbf3c59b6, "sound_0xbf3c59b6", "int"),
            (self._dependencies_for_sound_0x78be3b8d, "sound_0x78be3b8d", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct11.{field_name} ({field_type}): {e}")


def _decode_shield_charge_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 10.0, "di_knock_back_power": 5.0},
    )


def _decode_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4DA4A894: ("shield_charge_damage", _decode_shield_charge_damage),
    0xD34F1323: ("shield_vulnerability", _decode_shield_vulnerability),
    0xC1D9DBC6: ("unknown_0xc1d9dbc6", structs.decode_BIG_f),
    0x927FC322: ("unknown_0x927fc322", structs.decode_BIG_f),
    0x717824B4: ("shield_charge_speed", structs.decode_BIG_f),
    0xA41F75EF: ("shield_explode_effect", structs.decode_BIG_L),
    0xE6E92E73: ("sound_shield_explode", structs.decode_BIG_l),
    0x6CB0DA5A: ("unknown_0x6cb0da5a", structs.decode_BIG_f),
    0xC3938663: ("unknown_0xc3938663", structs.decode_BIG_f),
    0x865C109C: ("arm_shield_chance", structs.decode_BIG_f),
    0x8B48A2F8: ("arm_shield_time", structs.decode_BIG_f),
    0xE1B0EFA0: ("unknown_0xe1b0efa0", structs.decode_BIG_f),
    0x5CA206CA: ("arm_shield_explode_effect", structs.decode_BIG_L),
    0xEBF69CF0: ("shield_charge_effect", structs.decode_BIG_L),
    0x4AAB4E04: ("arm_shield_effect", structs.decode_BIG_L),
    0xBF3C59B6: ("sound_0xbf3c59b6", structs.decode_BIG_l),
    0x78BE3B8D: ("sound_0x78be3b8d", structs.decode_BIG_l),
}
