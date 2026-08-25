# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SteamLordDataJson(typing_extensions.TypedDict):
        unknown_0xe9553ffa: bool
        is_initially_cloaked: bool
        cloak_time: float
        decloak_time: float
        re_cloak_time: float
        dodge_damage_threshold: float
        dodge_chance: float
        flight_max_speed: float
        flight_acceleration: float
        target_hover_height: float
        repair_hover_height: float
        unknown_0xb35f3997: float
        abort_repair_damage: float
        repair_effect: int
        contact_visor_effect: int
        elsc_0xbe36e228: int
        elsc_0x24a4fc9e: int
        unknown_0xe1f030d5: float
        unknown_0xfb72f91e: float
        damage_info_0xfe138b07: json_util.JsonObject
        damage_info_0xaa19d1dc: json_util.JsonObject


@dataclasses.dataclass()
class SteamLordData(BaseProperty):
    unknown_0xe9553ffa: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE9553FFA, original_name="Unknown"),
        },
    )
    is_initially_cloaked: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1C893F54, original_name="IsInitiallyCloaked"),
        },
    )
    cloak_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x388BC31F, original_name="CloakTime"),
        },
    )
    decloak_time: float = dataclasses.field(
        default=0.25,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4319C840, original_name="DecloakTime"),
        },
    )
    re_cloak_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3BCBE7E2, original_name="ReCloakTime"),
        },
    )
    dodge_damage_threshold: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x91C8BA81, original_name="DodgeDamageThreshold"),
        },
    )
    dodge_chance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47BE3298, original_name="DodgeChance"),
        },
    )
    flight_max_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4DEC629, original_name="FlightMaxSpeed"),
        },
    )
    flight_acceleration: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A2BB377, original_name="FlightAcceleration"),
        },
    )
    target_hover_height: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x70130FE6, original_name="TargetHoverHeight"),
        },
    )
    repair_hover_height: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFCC4E240, original_name="RepairHoverHeight"),
        },
    )
    unknown_0xb35f3997: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB35F3997, original_name="Unknown"),
        },
    )
    abort_repair_damage: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEBA0C5F7, original_name="AbortRepairDamage"),
        },
    )
    repair_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x9F4E6A36, original_name="RepairEffect"),
        },
    )
    contact_visor_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0DE136F7, original_name="ContactVisorEffect"),
        },
    )
    elsc_0xbe36e228: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBE36E228, original_name="ELSC"),
        },
    )
    elsc_0x24a4fc9e: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x24A4FC9E, original_name="ELSC"),
        },
    )
    unknown_0xe1f030d5: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE1F030D5, original_name="Unknown"),
        },
    )
    unknown_0xfb72f91e: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB72F91E, original_name="Unknown"),
        },
    )
    damage_info_0xfe138b07: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xFE138B07,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0xaa19d1dc: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xAA19D1DC,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
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
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE9553FFA
        unknown_0xe9553ffa = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C893F54
        is_initially_cloaked = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388BC31F
        cloak_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4319C840
        decloak_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3BCBE7E2
        re_cloak_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91C8BA81
        dodge_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47BE3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4DEC629
        flight_max_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A2BB377
        flight_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70130FE6
        target_hover_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFCC4E240
        repair_hover_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB35F3997
        unknown_0xb35f3997 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBA0C5F7
        abort_repair_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F4E6A36
        repair_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0DE136F7
        contact_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE36E228
        elsc_0xbe36e228 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24A4FC9E
        elsc_0x24a4fc9e = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1F030D5
        unknown_0xe1f030d5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB72F91E
        unknown_0xfb72f91e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE138B07
        damage_info_0xfe138b07 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA19D1DC
        damage_info_0xaa19d1dc = DamageInfo.from_stream(data, game, property_size)

        return cls(
            unknown_0xe9553ffa,
            is_initially_cloaked,
            cloak_time,
            decloak_time,
            re_cloak_time,
            dodge_damage_threshold,
            dodge_chance,
            flight_max_speed,
            flight_acceleration,
            target_hover_height,
            repair_hover_height,
            unknown_0xb35f3997,
            abort_repair_damage,
            repair_effect,
            contact_visor_effect,
            elsc_0xbe36e228,
            elsc_0x24a4fc9e,
            unknown_0xe1f030d5,
            unknown_0xfb72f91e,
            damage_info_0xfe138b07,
            damage_info_0xaa19d1dc,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"\xe9U?\xfa")  # 0xe9553ffa
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xe9553ffa))

        data.write(b"\x1c\x89?T")  # 0x1c893f54
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_initially_cloaked))

        data.write(b"8\x8b\xc3\x1f")  # 0x388bc31f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.cloak_time))

        data.write(b"C\x19\xc8@")  # 0x4319c840
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.decloak_time))

        data.write(b";\xcb\xe7\xe2")  # 0x3bcbe7e2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.re_cloak_time))

        data.write(b"\x91\xc8\xba\x81")  # 0x91c8ba81
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_damage_threshold))

        data.write(b"G\xbe2\x98")  # 0x47be3298
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b"\xd4\xde\xc6)")  # 0xd4dec629
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flight_max_speed))

        data.write(b"z+\xb3w")  # 0x7a2bb377
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flight_acceleration))

        data.write(b"p\x13\x0f\xe6")  # 0x70130fe6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.target_hover_height))

        data.write(b"\xfc\xc4\xe2@")  # 0xfcc4e240
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.repair_hover_height))

        data.write(b"\xb3_9\x97")  # 0xb35f3997
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb35f3997))

        data.write(b"\xeb\xa0\xc5\xf7")  # 0xeba0c5f7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.abort_repair_damage))

        data.write(b"\x9fNj6")  # 0x9f4e6a36
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.repair_effect))

        data.write(b"\r\xe16\xf7")  # 0xde136f7
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.contact_visor_effect))

        data.write(b"\xbe6\xe2(")  # 0xbe36e228
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc_0xbe36e228))

        data.write(b"$\xa4\xfc\x9e")  # 0x24a4fc9e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc_0x24a4fc9e))

        data.write(b"\xe1\xf00\xd5")  # 0xe1f030d5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe1f030d5))

        data.write(b"\xfbr\xf9\x1e")  # 0xfb72f91e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfb72f91e))

        data.write(b"\xfe\x13\x8b\x07")  # 0xfe138b07
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0xfe138b07.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xaa\x19\xd1\xdc")  # 0xaa19d1dc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0xaa19d1dc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SteamLordDataJson", data)
        return cls(
            unknown_0xe9553ffa=json_data["unknown_0xe9553ffa"],
            is_initially_cloaked=json_data["is_initially_cloaked"],
            cloak_time=json_data["cloak_time"],
            decloak_time=json_data["decloak_time"],
            re_cloak_time=json_data["re_cloak_time"],
            dodge_damage_threshold=json_data["dodge_damage_threshold"],
            dodge_chance=json_data["dodge_chance"],
            flight_max_speed=json_data["flight_max_speed"],
            flight_acceleration=json_data["flight_acceleration"],
            target_hover_height=json_data["target_hover_height"],
            repair_hover_height=json_data["repair_hover_height"],
            unknown_0xb35f3997=json_data["unknown_0xb35f3997"],
            abort_repair_damage=json_data["abort_repair_damage"],
            repair_effect=json_data["repair_effect"],
            contact_visor_effect=json_data["contact_visor_effect"],
            elsc_0xbe36e228=json_data["elsc_0xbe36e228"],
            elsc_0x24a4fc9e=json_data["elsc_0x24a4fc9e"],
            unknown_0xe1f030d5=json_data["unknown_0xe1f030d5"],
            unknown_0xfb72f91e=json_data["unknown_0xfb72f91e"],
            damage_info_0xfe138b07=DamageInfo.from_json(json_data["damage_info_0xfe138b07"]),
            damage_info_0xaa19d1dc=DamageInfo.from_json(json_data["damage_info_0xaa19d1dc"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xe9553ffa": self.unknown_0xe9553ffa,
            "is_initially_cloaked": self.is_initially_cloaked,
            "cloak_time": self.cloak_time,
            "decloak_time": self.decloak_time,
            "re_cloak_time": self.re_cloak_time,
            "dodge_damage_threshold": self.dodge_damage_threshold,
            "dodge_chance": self.dodge_chance,
            "flight_max_speed": self.flight_max_speed,
            "flight_acceleration": self.flight_acceleration,
            "target_hover_height": self.target_hover_height,
            "repair_hover_height": self.repair_hover_height,
            "unknown_0xb35f3997": self.unknown_0xb35f3997,
            "abort_repair_damage": self.abort_repair_damage,
            "repair_effect": self.repair_effect,
            "contact_visor_effect": self.contact_visor_effect,
            "elsc_0xbe36e228": self.elsc_0xbe36e228,
            "elsc_0x24a4fc9e": self.elsc_0x24a4fc9e,
            "unknown_0xe1f030d5": self.unknown_0xe1f030d5,
            "unknown_0xfb72f91e": self.unknown_0xfb72f91e,
            "damage_info_0xfe138b07": self.damage_info_0xfe138b07.to_json(),
            "damage_info_0xaa19d1dc": self.damage_info_0xaa19d1dc.to_json(),
        }


def _decode_damage_info_0xfe138b07(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0xaa19d1dc(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xE9553FFA: ("unknown_0xe9553ffa", structs.decode_BIG_bool_),
    0x1C893F54: ("is_initially_cloaked", structs.decode_BIG_bool_),
    0x388BC31F: ("cloak_time", structs.decode_BIG_f),
    0x4319C840: ("decloak_time", structs.decode_BIG_f),
    0x3BCBE7E2: ("re_cloak_time", structs.decode_BIG_f),
    0x91C8BA81: ("dodge_damage_threshold", structs.decode_BIG_f),
    0x47BE3298: ("dodge_chance", structs.decode_BIG_f),
    0xD4DEC629: ("flight_max_speed", structs.decode_BIG_f),
    0x7A2BB377: ("flight_acceleration", structs.decode_BIG_f),
    0x70130FE6: ("target_hover_height", structs.decode_BIG_f),
    0xFCC4E240: ("repair_hover_height", structs.decode_BIG_f),
    0xB35F3997: ("unknown_0xb35f3997", structs.decode_BIG_f),
    0xEBA0C5F7: ("abort_repair_damage", structs.decode_BIG_f),
    0x9F4E6A36: ("repair_effect", structs.decode_BIG_Q),
    0x0DE136F7: ("contact_visor_effect", structs.decode_BIG_Q),
    0xBE36E228: ("elsc_0xbe36e228", structs.decode_BIG_Q),
    0x24A4FC9E: ("elsc_0x24a4fc9e", structs.decode_BIG_Q),
    0xE1F030D5: ("unknown_0xe1f030d5", structs.decode_BIG_f),
    0xFB72F91E: ("unknown_0xfb72f91e", structs.decode_BIG_f),
    0xFE138B07: ("damage_info_0xfe138b07", _decode_damage_info_0xfe138b07),
    0xAA19D1DC: ("damage_info_0xaa19d1dc", _decode_damage_info_0xaa19d1dc),
}
