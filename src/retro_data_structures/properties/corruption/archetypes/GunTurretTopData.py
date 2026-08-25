# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class GunTurretTopDataJson(typing_extensions.TypedDict):
        is_pirate_turret: bool
        unknown_0xf54e1111: bool
        shoots_at_player: bool
        unknown_0x5219dccd: bool
        instant_hit_range: float
        static_geometry_test: json_util.JsonObject
        tracking_speed: float
        panning_speed: float
        unknown_0x4b106481: float
        unknown_0xa1dd15f6: float
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_0x3eb2de35: float
        unknown_0xe50d8dd2: float
        unknown_0x64d482d5: int
        unknown_0xc3e002ac: int
        crsc: int
        wpsc: int
        projectile_damage_info: json_util.JsonObject
        unknown_0x4173ec53: float
        shot_angle_variance: float


@dataclasses.dataclass()
class GunTurretTopData(BaseProperty):
    is_pirate_turret: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x701D65CD, original_name="IsPirateTurret"),
        },
    )
    unknown_0xf54e1111: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF54E1111, original_name="Unknown"),
        },
    )
    shoots_at_player: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0A7846EC, original_name="ShootsAtPlayer"),
        },
    )
    unknown_0x5219dccd: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5219DCCD, original_name="Unknown"),
        },
    )
    instant_hit_range: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0BD3794D, original_name="InstantHitRange"),
        },
    )
    static_geometry_test: StaticGeometryTest = dataclasses.field(
        default_factory=StaticGeometryTest,
        metadata={
            "reflection": FieldReflection[StaticGeometryTest](
                StaticGeometryTest,
                id=0xCFA1ACE2,
                original_name="StaticGeometryTest",
                from_json=StaticGeometryTest.from_json,
                to_json=StaticGeometryTest.to_json,
            ),
        },
    )
    tracking_speed: float = dataclasses.field(
        default=180.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFE6829EC, original_name="TrackingSpeed"),
        },
    )
    panning_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4D28523E, original_name="PanningSpeed"),
        },
    )
    unknown_0x4b106481: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B106481, original_name="Unknown"),
        },
    )
    unknown_0xa1dd15f6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1DD15F6, original_name="Unknown"),
        },
    )
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_0x3eb2de35: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3EB2DE35, original_name="Unknown"),
        },
    )
    unknown_0xe50d8dd2: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE50D8DD2, original_name="Unknown"),
        },
    )
    unknown_0x64d482d5: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x64D482D5, original_name="Unknown"),
        },
    )
    unknown_0xc3e002ac: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC3E002AC, original_name="Unknown"),
        },
    )
    crsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CRSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x16E7D74A, original_name="CRSC"),
        },
    )
    wpsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x00E9C72C, original_name="WPSC"),
        },
    )
    projectile_damage_info: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xBE7FB5CC,
                original_name="ProjectileDamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x4173ec53: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4173EC53, original_name="Unknown"),
        },
    )
    shot_angle_variance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD75F9CF2, original_name="ShotAngleVariance"),
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
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x701D65CD
        is_pirate_turret = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF54E1111
        unknown_0xf54e1111 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A7846EC
        shoots_at_player = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5219DCCD
        unknown_0x5219dccd = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BD3794D
        instant_hit_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFA1ACE2
        static_geometry_test = StaticGeometryTest.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE6829EC
        tracking_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D28523E
        panning_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B106481
        unknown_0x4b106481 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1DD15F6
        unknown_0xa1dd15f6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95E7A2C2
        unknown_0x95e7a2c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76BA1C18
        unknown_0x76ba1c18 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3EB2DE35
        unknown_0x3eb2de35 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE50D8DD2
        unknown_0xe50d8dd2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64D482D5
        unknown_0x64d482d5 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3E002AC
        unknown_0xc3e002ac = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16E7D74A
        crsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00E9C72C
        wpsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE7FB5CC
        projectile_damage_info = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4173EC53
        unknown_0x4173ec53 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD75F9CF2
        shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            is_pirate_turret,
            unknown_0xf54e1111,
            shoots_at_player,
            unknown_0x5219dccd,
            instant_hit_range,
            static_geometry_test,
            tracking_speed,
            panning_speed,
            unknown_0x4b106481,
            unknown_0xa1dd15f6,
            unknown_0x95e7a2c2,
            unknown_0x76ba1c18,
            unknown_0x3eb2de35,
            unknown_0xe50d8dd2,
            unknown_0x64d482d5,
            unknown_0xc3e002ac,
            crsc,
            wpsc,
            projectile_damage_info,
            unknown_0x4173ec53,
            shot_angle_variance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"p\x1de\xcd")  # 0x701d65cd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_pirate_turret))

        data.write(b"\xf5N\x11\x11")  # 0xf54e1111
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf54e1111))

        data.write(b"\nxF\xec")  # 0xa7846ec
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.shoots_at_player))

        data.write(b"R\x19\xdc\xcd")  # 0x5219dccd
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x5219dccd))

        data.write(b"\x0b\xd3yM")  # 0xbd3794d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.instant_hit_range))

        data.write(b"\xcf\xa1\xac\xe2")  # 0xcfa1ace2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.static_geometry_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfeh)\xec")  # 0xfe6829ec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.tracking_speed))

        data.write(b"M(R>")  # 0x4d28523e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.panning_speed))

        data.write(b"K\x10d\x81")  # 0x4b106481
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4b106481))

        data.write(b"\xa1\xdd\x15\xf6")  # 0xa1dd15f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa1dd15f6))

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b">\xb2\xde5")  # 0x3eb2de35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3eb2de35))

        data.write(b"\xe5\r\x8d\xd2")  # 0xe50d8dd2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe50d8dd2))

        data.write(b"d\xd4\x82\xd5")  # 0x64d482d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x64d482d5))

        data.write(b"\xc3\xe0\x02\xac")  # 0xc3e002ac
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc3e002ac))

        data.write(b"\x16\xe7\xd7J")  # 0x16e7d74a
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.crsc))

        data.write(b"\x00\xe9\xc7,")  # 0xe9c72c
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.wpsc))

        data.write(b"\xbe\x7f\xb5\xcc")  # 0xbe7fb5cc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.projectile_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"As\xecS")  # 0x4173ec53
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4173ec53))

        data.write(b"\xd7_\x9c\xf2")  # 0xd75f9cf2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shot_angle_variance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GunTurretTopDataJson", data)
        return cls(
            is_pirate_turret=json_data["is_pirate_turret"],
            unknown_0xf54e1111=json_data["unknown_0xf54e1111"],
            shoots_at_player=json_data["shoots_at_player"],
            unknown_0x5219dccd=json_data["unknown_0x5219dccd"],
            instant_hit_range=json_data["instant_hit_range"],
            static_geometry_test=StaticGeometryTest.from_json(json_data["static_geometry_test"]),
            tracking_speed=json_data["tracking_speed"],
            panning_speed=json_data["panning_speed"],
            unknown_0x4b106481=json_data["unknown_0x4b106481"],
            unknown_0xa1dd15f6=json_data["unknown_0xa1dd15f6"],
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_0x3eb2de35=json_data["unknown_0x3eb2de35"],
            unknown_0xe50d8dd2=json_data["unknown_0xe50d8dd2"],
            unknown_0x64d482d5=json_data["unknown_0x64d482d5"],
            unknown_0xc3e002ac=json_data["unknown_0xc3e002ac"],
            crsc=json_data["crsc"],
            wpsc=json_data["wpsc"],
            projectile_damage_info=DamageInfo.from_json(json_data["projectile_damage_info"]),
            unknown_0x4173ec53=json_data["unknown_0x4173ec53"],
            shot_angle_variance=json_data["shot_angle_variance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "is_pirate_turret": self.is_pirate_turret,
            "unknown_0xf54e1111": self.unknown_0xf54e1111,
            "shoots_at_player": self.shoots_at_player,
            "unknown_0x5219dccd": self.unknown_0x5219dccd,
            "instant_hit_range": self.instant_hit_range,
            "static_geometry_test": self.static_geometry_test.to_json(),
            "tracking_speed": self.tracking_speed,
            "panning_speed": self.panning_speed,
            "unknown_0x4b106481": self.unknown_0x4b106481,
            "unknown_0xa1dd15f6": self.unknown_0xa1dd15f6,
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_0x3eb2de35": self.unknown_0x3eb2de35,
            "unknown_0xe50d8dd2": self.unknown_0xe50d8dd2,
            "unknown_0x64d482d5": self.unknown_0x64d482d5,
            "unknown_0xc3e002ac": self.unknown_0xc3e002ac,
            "crsc": self.crsc,
            "wpsc": self.wpsc,
            "projectile_damage_info": self.projectile_damage_info.to_json(),
            "unknown_0x4173ec53": self.unknown_0x4173ec53,
            "shot_angle_variance": self.shot_angle_variance,
        }


def _decode_static_geometry_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


def _decode_projectile_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x701D65CD: ("is_pirate_turret", structs.decode_BIG_bool_),
    0xF54E1111: ("unknown_0xf54e1111", structs.decode_BIG_bool_),
    0x0A7846EC: ("shoots_at_player", structs.decode_BIG_bool_),
    0x5219DCCD: ("unknown_0x5219dccd", structs.decode_BIG_bool_),
    0x0BD3794D: ("instant_hit_range", structs.decode_BIG_f),
    0xCFA1ACE2: ("static_geometry_test", _decode_static_geometry_test),
    0xFE6829EC: ("tracking_speed", structs.decode_BIG_f),
    0x4D28523E: ("panning_speed", structs.decode_BIG_f),
    0x4B106481: ("unknown_0x4b106481", structs.decode_BIG_f),
    0xA1DD15F6: ("unknown_0xa1dd15f6", structs.decode_BIG_f),
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0x3EB2DE35: ("unknown_0x3eb2de35", structs.decode_BIG_f),
    0xE50D8DD2: ("unknown_0xe50d8dd2", structs.decode_BIG_f),
    0x64D482D5: ("unknown_0x64d482d5", structs.decode_BIG_l),
    0xC3E002AC: ("unknown_0xc3e002ac", structs.decode_BIG_l),
    0x16E7D74A: ("crsc", structs.decode_BIG_Q),
    0x00E9C72C: ("wpsc", structs.decode_BIG_Q),
    0xBE7FB5CC: ("projectile_damage_info", _decode_projectile_damage_info),
    0x4173EC53: ("unknown_0x4173ec53", structs.decode_BIG_f),
    0xD75F9CF2: ("shot_angle_variance", structs.decode_BIG_f),
}
