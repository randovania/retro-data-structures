# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.SpacePirateWeaponData import SpacePirateWeaponData
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class DarkSamusEchoDataJson(typing_extensions.TypedDict):
        death_explosion: int
        death_explosion_sound: int
        part: int
        caud: int
        initial_attack_time: float
        min_attack_time: float
        attack_time_variance: float
        morphball_attack_speed: float
        morphball_attack_damage: json_util.JsonObject
        unknown_0xc3a06ae1: float
        unknown_0x23e3c3bb: float
        min_morphball_attack_duration: float
        max_morphball_attack_duration: float
        unknown_0xd03984cd: float
        unknown_0xe831a7d0: float
        unknown_0xbeb2b793: float
        unknown_0x9d9d3760: float
        morphball_animation: json_util.JsonObject
        weapon_data: json_util.JsonObject


@dataclasses.dataclass()
class DarkSamusEchoData(BaseProperty):
    death_explosion: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0687C33E, original_name="DeathExplosion"),
        },
    )
    death_explosion_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xED08FC4B, original_name="DeathExplosionSound"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8F0400E2, original_name="PART"),
        },
    )
    caud: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCCC7A920, original_name="CAUD"),
        },
    )
    initial_attack_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x446EFCAD, original_name="InitialAttackTime"),
        },
    )
    min_attack_time: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2EDF3368, original_name="MinAttackTime"),
        },
    )
    attack_time_variance: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F269614, original_name="AttackTimeVariance"),
        },
    )
    morphball_attack_speed: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x992C7B48, original_name="MorphballAttackSpeed"),
        },
    )
    morphball_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x76293001,
                original_name="MorphballAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xc3a06ae1: float = dataclasses.field(
        default=0.699999988079071,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3A06AE1, original_name="Unknown"),
        },
    )
    unknown_0x23e3c3bb: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x23E3C3BB, original_name="Unknown"),
        },
    )
    min_morphball_attack_duration: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x597245A1, original_name="MinMorphballAttackDuration"),
        },
    )
    max_morphball_attack_duration: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76AD063C, original_name="MaxMorphballAttackDuration"),
        },
    )
    unknown_0xd03984cd: float = dataclasses.field(
        default=135.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD03984CD, original_name="Unknown"),
        },
    )
    unknown_0xe831a7d0: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE831A7D0, original_name="Unknown"),
        },
    )
    unknown_0xbeb2b793: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBEB2B793, original_name="Unknown"),
        },
    )
    unknown_0x9d9d3760: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9D9D3760, original_name="Unknown"),
        },
    )
    morphball_animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x26B752E1,
                original_name="MorphballAnimation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    weapon_data: SpacePirateWeaponData = dataclasses.field(
        default_factory=SpacePirateWeaponData,
        metadata={
            "reflection": FieldReflection[SpacePirateWeaponData](
                SpacePirateWeaponData,
                id=0xDC89CC3C,
                original_name="WeaponData",
                from_json=SpacePirateWeaponData.from_json,
                to_json=SpacePirateWeaponData.to_json,
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
        if property_count != 19:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0687C33E
        death_explosion = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED08FC4B
        death_explosion_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F0400E2
        part = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCCC7A920
        caud = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x446EFCAD
        initial_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2EDF3368
        min_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F269614
        attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x992C7B48
        morphball_attack_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76293001
        morphball_attack_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3A06AE1
        unknown_0xc3a06ae1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23E3C3BB
        unknown_0x23e3c3bb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x597245A1
        min_morphball_attack_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76AD063C
        max_morphball_attack_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD03984CD
        unknown_0xd03984cd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE831A7D0
        unknown_0xe831a7d0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBEB2B793
        unknown_0xbeb2b793 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D9D3760
        unknown_0x9d9d3760 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26B752E1
        morphball_animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDC89CC3C
        weapon_data = SpacePirateWeaponData.from_stream(data, game, property_size)

        return cls(
            death_explosion,
            death_explosion_sound,
            part,
            caud,
            initial_attack_time,
            min_attack_time,
            attack_time_variance,
            morphball_attack_speed,
            morphball_attack_damage,
            unknown_0xc3a06ae1,
            unknown_0x23e3c3bb,
            min_morphball_attack_duration,
            max_morphball_attack_duration,
            unknown_0xd03984cd,
            unknown_0xe831a7d0,
            unknown_0xbeb2b793,
            unknown_0x9d9d3760,
            morphball_animation,
            weapon_data,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x13")  # 19 properties

        data.write(b"\x06\x87\xc3>")  # 0x687c33e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death_explosion))

        data.write(b"\xed\x08\xfcK")  # 0xed08fc4b
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.death_explosion_sound))

        data.write(b"\x8f\x04\x00\xe2")  # 0x8f0400e2
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.part))

        data.write(b"\xcc\xc7\xa9 ")  # 0xccc7a920
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b"Dn\xfc\xad")  # 0x446efcad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_attack_time))

        data.write(b".\xdf3h")  # 0x2edf3368
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_time))

        data.write(b"\x9f&\x96\x14")  # 0x9f269614
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_time_variance))

        data.write(b"\x99,{H")  # 0x992c7b48
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.morphball_attack_speed))

        data.write(b"v)0\x01")  # 0x76293001
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.morphball_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc3\xa0j\xe1")  # 0xc3a06ae1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc3a06ae1))

        data.write(b"#\xe3\xc3\xbb")  # 0x23e3c3bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x23e3c3bb))

        data.write(b"YrE\xa1")  # 0x597245a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_morphball_attack_duration))

        data.write(b"v\xad\x06<")  # 0x76ad063c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_morphball_attack_duration))

        data.write(b"\xd09\x84\xcd")  # 0xd03984cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd03984cd))

        data.write(b"\xe81\xa7\xd0")  # 0xe831a7d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe831a7d0))

        data.write(b"\xbe\xb2\xb7\x93")  # 0xbeb2b793
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbeb2b793))

        data.write(b"\x9d\x9d7`")  # 0x9d9d3760
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9d9d3760))

        data.write(b"&\xb7R\xe1")  # 0x26b752e1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.morphball_animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdc\x89\xcc<")  # 0xdc89cc3c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.weapon_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkSamusEchoDataJson", data)
        return cls(
            death_explosion=json_data["death_explosion"],
            death_explosion_sound=json_data["death_explosion_sound"],
            part=json_data["part"],
            caud=json_data["caud"],
            initial_attack_time=json_data["initial_attack_time"],
            min_attack_time=json_data["min_attack_time"],
            attack_time_variance=json_data["attack_time_variance"],
            morphball_attack_speed=json_data["morphball_attack_speed"],
            morphball_attack_damage=DamageInfo.from_json(json_data["morphball_attack_damage"]),
            unknown_0xc3a06ae1=json_data["unknown_0xc3a06ae1"],
            unknown_0x23e3c3bb=json_data["unknown_0x23e3c3bb"],
            min_morphball_attack_duration=json_data["min_morphball_attack_duration"],
            max_morphball_attack_duration=json_data["max_morphball_attack_duration"],
            unknown_0xd03984cd=json_data["unknown_0xd03984cd"],
            unknown_0xe831a7d0=json_data["unknown_0xe831a7d0"],
            unknown_0xbeb2b793=json_data["unknown_0xbeb2b793"],
            unknown_0x9d9d3760=json_data["unknown_0x9d9d3760"],
            morphball_animation=AnimationParameters.from_json(json_data["morphball_animation"]),
            weapon_data=SpacePirateWeaponData.from_json(json_data["weapon_data"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "death_explosion": self.death_explosion,
            "death_explosion_sound": self.death_explosion_sound,
            "part": self.part,
            "caud": self.caud,
            "initial_attack_time": self.initial_attack_time,
            "min_attack_time": self.min_attack_time,
            "attack_time_variance": self.attack_time_variance,
            "morphball_attack_speed": self.morphball_attack_speed,
            "morphball_attack_damage": self.morphball_attack_damage.to_json(),
            "unknown_0xc3a06ae1": self.unknown_0xc3a06ae1,
            "unknown_0x23e3c3bb": self.unknown_0x23e3c3bb,
            "min_morphball_attack_duration": self.min_morphball_attack_duration,
            "max_morphball_attack_duration": self.max_morphball_attack_duration,
            "unknown_0xd03984cd": self.unknown_0xd03984cd,
            "unknown_0xe831a7d0": self.unknown_0xe831a7d0,
            "unknown_0xbeb2b793": self.unknown_0xbeb2b793,
            "unknown_0x9d9d3760": self.unknown_0x9d9d3760,
            "morphball_animation": self.morphball_animation.to_json(),
            "weapon_data": self.weapon_data.to_json(),
        }


def _decode_morphball_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_morphball_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_weapon_data(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateWeaponData:
    return SpacePirateWeaponData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0687C33E: ("death_explosion", structs.decode_BIG_Q),
    0xED08FC4B: ("death_explosion_sound", structs.decode_BIG_Q),
    0x8F0400E2: ("part", structs.decode_BIG_Q),
    0xCCC7A920: ("caud", structs.decode_BIG_Q),
    0x446EFCAD: ("initial_attack_time", structs.decode_BIG_f),
    0x2EDF3368: ("min_attack_time", structs.decode_BIG_f),
    0x9F269614: ("attack_time_variance", structs.decode_BIG_f),
    0x992C7B48: ("morphball_attack_speed", structs.decode_BIG_f),
    0x76293001: ("morphball_attack_damage", _decode_morphball_attack_damage),
    0xC3A06AE1: ("unknown_0xc3a06ae1", structs.decode_BIG_f),
    0x23E3C3BB: ("unknown_0x23e3c3bb", structs.decode_BIG_f),
    0x597245A1: ("min_morphball_attack_duration", structs.decode_BIG_f),
    0x76AD063C: ("max_morphball_attack_duration", structs.decode_BIG_f),
    0xD03984CD: ("unknown_0xd03984cd", structs.decode_BIG_f),
    0xE831A7D0: ("unknown_0xe831a7d0", structs.decode_BIG_f),
    0xBEB2B793: ("unknown_0xbeb2b793", structs.decode_BIG_f),
    0x9D9D3760: ("unknown_0x9d9d3760", structs.decode_BIG_f),
    0x26B752E1: ("morphball_animation", _decode_morphball_animation),
    0xDC89CC3C: ("weapon_data", _decode_weapon_data),
}
