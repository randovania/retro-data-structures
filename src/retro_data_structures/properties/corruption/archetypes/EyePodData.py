# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.EyePodStruct import EyePodStruct
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class EyePodDataJson(typing_extensions.TypedDict):
        hearing_range: float
        lose_interest_distance: float
        lose_interest_time: float
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0x64d482d5: int
        unknown_0xc3e002ac: int
        unknown_0x4da7906b: float
        unknown_0xa2258e11: float
        min_charge_time: float
        max_charge_time: float
        unknown_0x88f13a51: float
        unknown_0x6773242b: float
        rapid_fire_projectile: int
        charge_shot_projectile: int
        rapid_fire_damage_info: json_util.JsonObject
        charge_shot_damage_info: json_util.JsonObject
        shot_angle_variance: float
        charge_shot_enabled: bool
        unknown_0x3db05763: float
        turn_anim_speed: float
        eye_pod_struct_0x5b0a8c8a: json_util.JsonObject
        eye_pod_struct_0x0ce679bb: json_util.JsonObject
        eye_pod_struct_0xf9bbcc33: json_util.JsonObject
        starts_invulnerable: bool
        unknown_0xa1ed5408: bool
        shot_collision_test: json_util.JsonObject


@dataclasses.dataclass()
class EyePodData(BaseProperty):
    hearing_range: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25474550, original_name="HearingRange"),
        },
    )
    lose_interest_distance: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF6B051B3, original_name="LoseInterestDistance"),
        },
    )
    lose_interest_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF8B0C2BB, original_name="LoseInterestTime"),
        },
    )
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0x64d482d5: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x64D482D5, original_name="Unknown"),
        },
    )
    unknown_0xc3e002ac: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC3E002AC, original_name="Unknown"),
        },
    )
    unknown_0x4da7906b: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4DA7906B, original_name="Unknown"),
        },
    )
    unknown_0xa2258e11: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA2258E11, original_name="Unknown"),
        },
    )
    min_charge_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB6A0464C, original_name="MinChargeTime"),
        },
    )
    max_charge_time: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE5065EA8, original_name="MaxChargeTime"),
        },
    )
    unknown_0x88f13a51: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88F13A51, original_name="Unknown"),
        },
    )
    unknown_0x6773242b: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6773242B, original_name="Unknown"),
        },
    )
    rapid_fire_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xE8C819E6, original_name="RapidFireProjectile"),
        },
    )
    charge_shot_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB14FEA52, original_name="ChargeShotProjectile"),
        },
    )
    rapid_fire_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xC93109E7,
                original_name="RapidFireDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    charge_shot_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x37A6F562,
                original_name="ChargeShotDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    shot_angle_variance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD75F9CF2, original_name="ShotAngleVariance"),
        },
    )
    charge_shot_enabled: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x7076D432, original_name="ChargeShotEnabled"),
        },
    )
    unknown_0x3db05763: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3DB05763, original_name="Unknown"),
        },
    )
    turn_anim_speed: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x190CB8D7, original_name="TurnAnimSpeed"),
        },
    )
    eye_pod_struct_0x5b0a8c8a: EyePodStruct = dataclasses.field(
        default_factory=EyePodStruct,
        metadata={
            "reflection": FieldReflection[EyePodStruct](
                EyePodStruct,
                id=0x5B0A8C8A,
                original_name="EyePodStruct",
                from_json=EyePodStruct.from_json,
                to_json=EyePodStruct.to_json,
            ),
        },
    )
    eye_pod_struct_0x0ce679bb: EyePodStruct = dataclasses.field(
        default_factory=EyePodStruct,
        metadata={
            "reflection": FieldReflection[EyePodStruct](
                EyePodStruct,
                id=0x0CE679BB,
                original_name="EyePodStruct",
                from_json=EyePodStruct.from_json,
                to_json=EyePodStruct.to_json,
            ),
        },
    )
    eye_pod_struct_0xf9bbcc33: EyePodStruct = dataclasses.field(
        default_factory=EyePodStruct,
        metadata={
            "reflection": FieldReflection[EyePodStruct](
                EyePodStruct,
                id=0xF9BBCC33,
                original_name="EyePodStruct",
                from_json=EyePodStruct.from_json,
                to_json=EyePodStruct.to_json,
            ),
        },
    )
    starts_invulnerable: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF1C247FF, original_name="StartsInvulnerable"),
        },
    )
    unknown_0xa1ed5408: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA1ED5408, original_name="Unknown"),
        },
    )
    shot_collision_test: StaticGeometryTest = dataclasses.field(
        default_factory=StaticGeometryTest,
        metadata={
            "reflection": FieldReflection[StaticGeometryTest](
                StaticGeometryTest,
                id=0x511961D4,
                original_name="ShotCollisionTest",
                from_json=StaticGeometryTest.from_json,
                to_json=StaticGeometryTest.to_json,
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
        if property_count != 27:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25474550
        hearing_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF6B051B3
        lose_interest_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8B0C2BB
        lose_interest_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95E7A2C2
        unknown_0x95e7a2c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76BA1C18
        unknown_0x76ba1c18 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64D482D5
        unknown_0x64d482d5 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3E002AC
        unknown_0xc3e002ac = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4DA7906B
        unknown_0x4da7906b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA2258E11
        unknown_0xa2258e11 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6A0464C
        min_charge_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE5065EA8
        max_charge_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88F13A51
        unknown_0x88f13a51 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6773242B
        unknown_0x6773242b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE8C819E6
        rapid_fire_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB14FEA52
        charge_shot_projectile = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC93109E7
        rapid_fire_damage_info = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37A6F562
        charge_shot_damage_info = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD75F9CF2
        shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7076D432
        charge_shot_enabled = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DB05763
        unknown_0x3db05763 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x190CB8D7
        turn_anim_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B0A8C8A
        eye_pod_struct_0x5b0a8c8a = EyePodStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CE679BB
        eye_pod_struct_0x0ce679bb = EyePodStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF9BBCC33
        eye_pod_struct_0xf9bbcc33 = EyePodStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1C247FF
        starts_invulnerable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1ED5408
        unknown_0xa1ed5408 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x511961D4
        shot_collision_test = StaticGeometryTest.from_stream(data, game, property_size)

        return cls(
            hearing_range,
            lose_interest_distance,
            lose_interest_time,
            unknown_0x95e7a2c2,
            unknown_0x76ba1c18,
            unknown_0x64d482d5,
            unknown_0xc3e002ac,
            unknown_0x4da7906b,
            unknown_0xa2258e11,
            min_charge_time,
            max_charge_time,
            unknown_0x88f13a51,
            unknown_0x6773242b,
            rapid_fire_projectile,
            charge_shot_projectile,
            rapid_fire_damage_info,
            charge_shot_damage_info,
            shot_angle_variance,
            charge_shot_enabled,
            unknown_0x3db05763,
            turn_anim_speed,
            eye_pod_struct_0x5b0a8c8a,
            eye_pod_struct_0x0ce679bb,
            eye_pod_struct_0xf9bbcc33,
            starts_invulnerable,
            unknown_0xa1ed5408,
            shot_collision_test,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1b")  # 27 properties

        data.write(b"%GEP")  # 0x25474550
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hearing_range))

        data.write(b"\xf6\xb0Q\xb3")  # 0xf6b051b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lose_interest_distance))

        data.write(b"\xf8\xb0\xc2\xbb")  # 0xf8b0c2bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lose_interest_time))

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b"d\xd4\x82\xd5")  # 0x64d482d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x64d482d5))

        data.write(b"\xc3\xe0\x02\xac")  # 0xc3e002ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc3e002ac))

        data.write(b"M\xa7\x90k")  # 0x4da7906b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4da7906b))

        data.write(b"\xa2%\x8e\x11")  # 0xa2258e11
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa2258e11))

        data.write(b"\xb6\xa0FL")  # 0xb6a0464c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_charge_time))

        data.write(b"\xe5\x06^\xa8")  # 0xe5065ea8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_charge_time))

        data.write(b"\x88\xf1:Q")  # 0x88f13a51
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x88f13a51))

        data.write(b"gs$+")  # 0x6773242b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6773242b))

        data.write(b"\xe8\xc8\x19\xe6")  # 0xe8c819e6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.rapid_fire_projectile))

        data.write(b"\xb1O\xeaR")  # 0xb14fea52
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.charge_shot_projectile))

        data.write(b"\xc91\t\xe7")  # 0xc93109e7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.rapid_fire_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"7\xa6\xf5b")  # 0x37a6f562
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.charge_shot_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd7_\x9c\xf2")  # 0xd75f9cf2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shot_angle_variance))

        data.write(b"pv\xd42")  # 0x7076d432
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.charge_shot_enabled))

        data.write(b"=\xb0Wc")  # 0x3db05763
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3db05763))

        data.write(b"\x19\x0c\xb8\xd7")  # 0x190cb8d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_anim_speed))

        data.write(b"[\n\x8c\x8a")  # 0x5b0a8c8a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.eye_pod_struct_0x5b0a8c8a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0c\xe6y\xbb")  # 0xce679bb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.eye_pod_struct_0x0ce679bb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf9\xbb\xcc3")  # 0xf9bbcc33
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.eye_pod_struct_0xf9bbcc33.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf1\xc2G\xff")  # 0xf1c247ff
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.starts_invulnerable))

        data.write(b"\xa1\xedT\x08")  # 0xa1ed5408
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa1ed5408))

        data.write(b"Q\x19a\xd4")  # 0x511961d4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shot_collision_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EyePodDataJson", data)
        return cls(
            hearing_range=json_data["hearing_range"],
            lose_interest_distance=json_data["lose_interest_distance"],
            lose_interest_time=json_data["lose_interest_time"],
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0x64d482d5=json_data["unknown_0x64d482d5"],
            unknown_0xc3e002ac=json_data["unknown_0xc3e002ac"],
            unknown_0x4da7906b=json_data["unknown_0x4da7906b"],
            unknown_0xa2258e11=json_data["unknown_0xa2258e11"],
            min_charge_time=json_data["min_charge_time"],
            max_charge_time=json_data["max_charge_time"],
            unknown_0x88f13a51=json_data["unknown_0x88f13a51"],
            unknown_0x6773242b=json_data["unknown_0x6773242b"],
            rapid_fire_projectile=json_data["rapid_fire_projectile"],
            charge_shot_projectile=json_data["charge_shot_projectile"],
            rapid_fire_damage_info=DamageInfo.from_json(json_data["rapid_fire_damage_info"]),
            charge_shot_damage_info=DamageInfo.from_json(json_data["charge_shot_damage_info"]),
            shot_angle_variance=json_data["shot_angle_variance"],
            charge_shot_enabled=json_data["charge_shot_enabled"],
            unknown_0x3db05763=json_data["unknown_0x3db05763"],
            turn_anim_speed=json_data["turn_anim_speed"],
            eye_pod_struct_0x5b0a8c8a=EyePodStruct.from_json(json_data["eye_pod_struct_0x5b0a8c8a"]),
            eye_pod_struct_0x0ce679bb=EyePodStruct.from_json(json_data["eye_pod_struct_0x0ce679bb"]),
            eye_pod_struct_0xf9bbcc33=EyePodStruct.from_json(json_data["eye_pod_struct_0xf9bbcc33"]),
            starts_invulnerable=json_data["starts_invulnerable"],
            unknown_0xa1ed5408=json_data["unknown_0xa1ed5408"],
            shot_collision_test=StaticGeometryTest.from_json(json_data["shot_collision_test"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hearing_range": self.hearing_range,
            "lose_interest_distance": self.lose_interest_distance,
            "lose_interest_time": self.lose_interest_time,
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0x64d482d5": self.unknown_0x64d482d5,
            "unknown_0xc3e002ac": self.unknown_0xc3e002ac,
            "unknown_0x4da7906b": self.unknown_0x4da7906b,
            "unknown_0xa2258e11": self.unknown_0xa2258e11,
            "min_charge_time": self.min_charge_time,
            "max_charge_time": self.max_charge_time,
            "unknown_0x88f13a51": self.unknown_0x88f13a51,
            "unknown_0x6773242b": self.unknown_0x6773242b,
            "rapid_fire_projectile": self.rapid_fire_projectile,
            "charge_shot_projectile": self.charge_shot_projectile,
            "rapid_fire_damage_info": self.rapid_fire_damage_info.to_json(),
            "charge_shot_damage_info": self.charge_shot_damage_info.to_json(),
            "shot_angle_variance": self.shot_angle_variance,
            "charge_shot_enabled": self.charge_shot_enabled,
            "unknown_0x3db05763": self.unknown_0x3db05763,
            "turn_anim_speed": self.turn_anim_speed,
            "eye_pod_struct_0x5b0a8c8a": self.eye_pod_struct_0x5b0a8c8a.to_json(),
            "eye_pod_struct_0x0ce679bb": self.eye_pod_struct_0x0ce679bb.to_json(),
            "eye_pod_struct_0xf9bbcc33": self.eye_pod_struct_0xf9bbcc33.to_json(),
            "starts_invulnerable": self.starts_invulnerable,
            "unknown_0xa1ed5408": self.unknown_0xa1ed5408,
            "shot_collision_test": self.shot_collision_test.to_json(),
        }


def _decode_rapid_fire_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_charge_shot_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_eye_pod_struct_0x5b0a8c8a(data: typing.BinaryIO, game: Game, property_size: int) -> EyePodStruct:
    return EyePodStruct.from_stream(data, game, property_size)


def _decode_eye_pod_struct_0x0ce679bb(data: typing.BinaryIO, game: Game, property_size: int) -> EyePodStruct:
    return EyePodStruct.from_stream(data, game, property_size)


def _decode_eye_pod_struct_0xf9bbcc33(data: typing.BinaryIO, game: Game, property_size: int) -> EyePodStruct:
    return EyePodStruct.from_stream(data, game, property_size)


def _decode_shot_collision_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x25474550: ("hearing_range", structs.decode_BIG_f),
    0xF6B051B3: ("lose_interest_distance", structs.decode_BIG_f),
    0xF8B0C2BB: ("lose_interest_time", structs.decode_BIG_f),
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0x64D482D5: ("unknown_0x64d482d5", structs.decode_BIG_l),
    0xC3E002AC: ("unknown_0xc3e002ac", structs.decode_BIG_l),
    0x4DA7906B: ("unknown_0x4da7906b", structs.decode_BIG_f),
    0xA2258E11: ("unknown_0xa2258e11", structs.decode_BIG_f),
    0xB6A0464C: ("min_charge_time", structs.decode_BIG_f),
    0xE5065EA8: ("max_charge_time", structs.decode_BIG_f),
    0x88F13A51: ("unknown_0x88f13a51", structs.decode_BIG_f),
    0x6773242B: ("unknown_0x6773242b", structs.decode_BIG_f),
    0xE8C819E6: ("rapid_fire_projectile", structs.decode_BIG_Q),
    0xB14FEA52: ("charge_shot_projectile", structs.decode_BIG_Q),
    0xC93109E7: ("rapid_fire_damage_info", _decode_rapid_fire_damage_info),
    0x37A6F562: ("charge_shot_damage_info", _decode_charge_shot_damage_info),
    0xD75F9CF2: ("shot_angle_variance", structs.decode_BIG_f),
    0x7076D432: ("charge_shot_enabled", structs.decode_BIG_bool_),
    0x3DB05763: ("unknown_0x3db05763", structs.decode_BIG_f),
    0x190CB8D7: ("turn_anim_speed", structs.decode_BIG_f),
    0x5B0A8C8A: ("eye_pod_struct_0x5b0a8c8a", _decode_eye_pod_struct_0x5b0a8c8a),
    0x0CE679BB: ("eye_pod_struct_0x0ce679bb", _decode_eye_pod_struct_0x0ce679bb),
    0xF9BBCC33: ("eye_pod_struct_0xf9bbcc33", _decode_eye_pod_struct_0xf9bbcc33),
    0xF1C247FF: ("starts_invulnerable", structs.decode_BIG_bool_),
    0xA1ED5408: ("unknown_0xa1ed5408", structs.decode_BIG_bool_),
    0x511961D4: ("shot_collision_test", _decode_shot_collision_test),
}
