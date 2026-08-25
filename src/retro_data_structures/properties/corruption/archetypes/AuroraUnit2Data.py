# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.UnknownStruct7 import UnknownStruct7
from retro_data_structures.properties.corruption.archetypes.UnknownStruct11 import UnknownStruct11
from retro_data_structures.properties.corruption.archetypes.UnknownStruct12 import UnknownStruct12
from retro_data_structures.properties.corruption.archetypes.UnknownStruct13 import UnknownStruct13
from retro_data_structures.properties.corruption.archetypes.UnknownStruct14 import UnknownStruct14
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class AuroraUnit2DataJson(typing_extensions.TypedDict):
        unknown_0x0a072c48: float
        unknown_0xdde5ac10: float
        flight_max_speed: float
        flight_acceleration: float
        flight_deceleration: float
        dodge_time: float
        dodge_time_variance: float
        dodge_chance: float
        unknown_0xefd78a41: float
        hover_height: float
        min_follow_distance: float
        max_follow_distance: float
        initial_attack_time: float
        attack_time: float
        attack_time_variance: float
        unknown_0x059b46cf: float
        unknown_0x1aa98d7f: float
        junction_vulnerability: json_util.JsonObject
        unknown_struct7: json_util.JsonObject
        unknown_struct11: json_util.JsonObject
        unknown_struct12: json_util.JsonObject
        unknown_struct13: json_util.JsonObject
        unknown_struct14: json_util.JsonObject


@dataclasses.dataclass()
class AuroraUnit2Data(BaseProperty):
    unknown_0x0a072c48: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0A072C48, original_name="Unknown"),
        },
    )
    unknown_0xdde5ac10: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDDE5AC10, original_name="Unknown"),
        },
    )
    flight_max_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4DEC629, original_name="FlightMaxSpeed"),
        },
    )
    flight_acceleration: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A2BB377, original_name="FlightAcceleration"),
        },
    )
    flight_deceleration: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDD14361F, original_name="FlightDeceleration"),
        },
    )
    dodge_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x67625BEF, original_name="DodgeTime"),
        },
    )
    dodge_time_variance: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x34B97EDB, original_name="DodgeTimeVariance"),
        },
    )
    dodge_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47BE3298, original_name="DodgeChance"),
        },
    )
    unknown_0xefd78a41: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEFD78A41, original_name="Unknown"),
        },
    )
    hover_height: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC75998AA, original_name="HoverHeight"),
        },
    )
    min_follow_distance: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x93716A88, original_name="MinFollowDistance"),
        },
    )
    max_follow_distance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD266550E, original_name="MaxFollowDistance"),
        },
    )
    initial_attack_time: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x446EFCAD, original_name="InitialAttackTime"),
        },
    )
    attack_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDCA1E8B6, original_name="AttackTime"),
        },
    )
    attack_time_variance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F269614, original_name="AttackTimeVariance"),
        },
    )
    unknown_0x059b46cf: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x059B46CF, original_name="Unknown"),
        },
    )
    unknown_0x1aa98d7f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1AA98D7F, original_name="Unknown"),
        },
    )
    junction_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xFDD2FE20,
                original_name="JunctionVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    unknown_struct7: UnknownStruct7 = dataclasses.field(
        default_factory=UnknownStruct7,
        metadata={
            "reflection": FieldReflection[UnknownStruct7](
                UnknownStruct7,
                id=0xC108CFA0,
                original_name="UnknownStruct7",
                from_json=UnknownStruct7.from_json,
                to_json=UnknownStruct7.to_json,
            ),
        },
    )
    unknown_struct11: UnknownStruct11 = dataclasses.field(
        default_factory=UnknownStruct11,
        metadata={
            "reflection": FieldReflection[UnknownStruct11](
                UnknownStruct11,
                id=0x91502686,
                original_name="UnknownStruct11",
                from_json=UnknownStruct11.from_json,
                to_json=UnknownStruct11.to_json,
            ),
        },
    )
    unknown_struct12: UnknownStruct12 = dataclasses.field(
        default_factory=UnknownStruct12,
        metadata={
            "reflection": FieldReflection[UnknownStruct12](
                UnknownStruct12,
                id=0xAD62C993,
                original_name="UnknownStruct12",
                from_json=UnknownStruct12.from_json,
                to_json=UnknownStruct12.to_json,
            ),
        },
    )
    unknown_struct13: UnknownStruct13 = dataclasses.field(
        default_factory=UnknownStruct13,
        metadata={
            "reflection": FieldReflection[UnknownStruct13](
                UnknownStruct13,
                id=0x03A319DF,
                original_name="UnknownStruct13",
                from_json=UnknownStruct13.from_json,
                to_json=UnknownStruct13.to_json,
            ),
        },
    )
    unknown_struct14: UnknownStruct14 = dataclasses.field(
        default_factory=UnknownStruct14,
        metadata={
            "reflection": FieldReflection[UnknownStruct14](
                UnknownStruct14,
                id=0x9DD3BB57,
                original_name="UnknownStruct14",
                from_json=UnknownStruct14.from_json,
                to_json=UnknownStruct14.to_json,
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
        if property_count != 23:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0A072C48
        unknown_0x0a072c48 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDDE5AC10
        unknown_0xdde5ac10 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4DEC629
        flight_max_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7A2BB377
        flight_acceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDD14361F
        flight_deceleration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67625BEF
        dodge_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34B97EDB
        dodge_time_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47BE3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEFD78A41
        unknown_0xefd78a41 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC75998AA
        hover_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93716A88
        min_follow_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD266550E
        max_follow_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x446EFCAD
        initial_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDCA1E8B6
        attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9F269614
        attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x059B46CF
        unknown_0x059b46cf = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1AA98D7F
        unknown_0x1aa98d7f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFDD2FE20
        junction_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC108CFA0
        unknown_struct7 = UnknownStruct7.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91502686
        unknown_struct11 = UnknownStruct11.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAD62C993
        unknown_struct12 = UnknownStruct12.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03A319DF
        unknown_struct13 = UnknownStruct13.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9DD3BB57
        unknown_struct14 = UnknownStruct14.from_stream(data, game, property_size)

        return cls(
            unknown_0x0a072c48,
            unknown_0xdde5ac10,
            flight_max_speed,
            flight_acceleration,
            flight_deceleration,
            dodge_time,
            dodge_time_variance,
            dodge_chance,
            unknown_0xefd78a41,
            hover_height,
            min_follow_distance,
            max_follow_distance,
            initial_attack_time,
            attack_time,
            attack_time_variance,
            unknown_0x059b46cf,
            unknown_0x1aa98d7f,
            junction_vulnerability,
            unknown_struct7,
            unknown_struct11,
            unknown_struct12,
            unknown_struct13,
            unknown_struct14,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x17")  # 23 properties

        data.write(b"\n\x07,H")  # 0xa072c48
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a072c48))

        data.write(b"\xdd\xe5\xac\x10")  # 0xdde5ac10
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdde5ac10))

        data.write(b"\xd4\xde\xc6)")  # 0xd4dec629
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flight_max_speed))

        data.write(b"z+\xb3w")  # 0x7a2bb377
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flight_acceleration))

        data.write(b"\xdd\x146\x1f")  # 0xdd14361f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.flight_deceleration))

        data.write(b"gb[\xef")  # 0x67625bef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_time))

        data.write(b"4\xb9~\xdb")  # 0x34b97edb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_time_variance))

        data.write(b"G\xbe2\x98")  # 0x47be3298
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b"\xef\xd7\x8aA")  # 0xefd78a41
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xefd78a41))

        data.write(b"\xc7Y\x98\xaa")  # 0xc75998aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hover_height))

        data.write(b"\x93qj\x88")  # 0x93716a88
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_follow_distance))

        data.write(b"\xd2fU\x0e")  # 0xd266550e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_follow_distance))

        data.write(b"Dn\xfc\xad")  # 0x446efcad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_attack_time))

        data.write(b"\xdc\xa1\xe8\xb6")  # 0xdca1e8b6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_time))

        data.write(b"\x9f&\x96\x14")  # 0x9f269614
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_time_variance))

        data.write(b"\x05\x9bF\xcf")  # 0x59b46cf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x059b46cf))

        data.write(b"\x1a\xa9\x8d\x7f")  # 0x1aa98d7f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1aa98d7f))

        data.write(b"\xfd\xd2\xfe ")  # 0xfdd2fe20
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.junction_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc1\x08\xcf\xa0")  # 0xc108cfa0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x91P&\x86")  # 0x91502686
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct11.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xadb\xc9\x93")  # 0xad62c993
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct12.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x03\xa3\x19\xdf")  # 0x3a319df
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct13.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9d\xd3\xbbW")  # 0x9dd3bb57
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct14.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AuroraUnit2DataJson", data)
        return cls(
            unknown_0x0a072c48=json_data["unknown_0x0a072c48"],
            unknown_0xdde5ac10=json_data["unknown_0xdde5ac10"],
            flight_max_speed=json_data["flight_max_speed"],
            flight_acceleration=json_data["flight_acceleration"],
            flight_deceleration=json_data["flight_deceleration"],
            dodge_time=json_data["dodge_time"],
            dodge_time_variance=json_data["dodge_time_variance"],
            dodge_chance=json_data["dodge_chance"],
            unknown_0xefd78a41=json_data["unknown_0xefd78a41"],
            hover_height=json_data["hover_height"],
            min_follow_distance=json_data["min_follow_distance"],
            max_follow_distance=json_data["max_follow_distance"],
            initial_attack_time=json_data["initial_attack_time"],
            attack_time=json_data["attack_time"],
            attack_time_variance=json_data["attack_time_variance"],
            unknown_0x059b46cf=json_data["unknown_0x059b46cf"],
            unknown_0x1aa98d7f=json_data["unknown_0x1aa98d7f"],
            junction_vulnerability=DamageVulnerability.from_json(json_data["junction_vulnerability"]),
            unknown_struct7=UnknownStruct7.from_json(json_data["unknown_struct7"]),
            unknown_struct11=UnknownStruct11.from_json(json_data["unknown_struct11"]),
            unknown_struct12=UnknownStruct12.from_json(json_data["unknown_struct12"]),
            unknown_struct13=UnknownStruct13.from_json(json_data["unknown_struct13"]),
            unknown_struct14=UnknownStruct14.from_json(json_data["unknown_struct14"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x0a072c48": self.unknown_0x0a072c48,
            "unknown_0xdde5ac10": self.unknown_0xdde5ac10,
            "flight_max_speed": self.flight_max_speed,
            "flight_acceleration": self.flight_acceleration,
            "flight_deceleration": self.flight_deceleration,
            "dodge_time": self.dodge_time,
            "dodge_time_variance": self.dodge_time_variance,
            "dodge_chance": self.dodge_chance,
            "unknown_0xefd78a41": self.unknown_0xefd78a41,
            "hover_height": self.hover_height,
            "min_follow_distance": self.min_follow_distance,
            "max_follow_distance": self.max_follow_distance,
            "initial_attack_time": self.initial_attack_time,
            "attack_time": self.attack_time,
            "attack_time_variance": self.attack_time_variance,
            "unknown_0x059b46cf": self.unknown_0x059b46cf,
            "unknown_0x1aa98d7f": self.unknown_0x1aa98d7f,
            "junction_vulnerability": self.junction_vulnerability.to_json(),
            "unknown_struct7": self.unknown_struct7.to_json(),
            "unknown_struct11": self.unknown_struct11.to_json(),
            "unknown_struct12": self.unknown_struct12.to_json(),
            "unknown_struct13": self.unknown_struct13.to_json(),
            "unknown_struct14": self.unknown_struct14.to_json(),
        }


def _decode_junction_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_unknown_struct7(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct7:
    return UnknownStruct7.from_stream(data, game, property_size)


def _decode_unknown_struct11(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct11:
    return UnknownStruct11.from_stream(data, game, property_size)


def _decode_unknown_struct12(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct12:
    return UnknownStruct12.from_stream(data, game, property_size)


def _decode_unknown_struct13(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct13:
    return UnknownStruct13.from_stream(data, game, property_size)


def _decode_unknown_struct14(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct14:
    return UnknownStruct14.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0A072C48: ("unknown_0x0a072c48", structs.decode_BIG_f),
    0xDDE5AC10: ("unknown_0xdde5ac10", structs.decode_BIG_f),
    0xD4DEC629: ("flight_max_speed", structs.decode_BIG_f),
    0x7A2BB377: ("flight_acceleration", structs.decode_BIG_f),
    0xDD14361F: ("flight_deceleration", structs.decode_BIG_f),
    0x67625BEF: ("dodge_time", structs.decode_BIG_f),
    0x34B97EDB: ("dodge_time_variance", structs.decode_BIG_f),
    0x47BE3298: ("dodge_chance", structs.decode_BIG_f),
    0xEFD78A41: ("unknown_0xefd78a41", structs.decode_BIG_f),
    0xC75998AA: ("hover_height", structs.decode_BIG_f),
    0x93716A88: ("min_follow_distance", structs.decode_BIG_f),
    0xD266550E: ("max_follow_distance", structs.decode_BIG_f),
    0x446EFCAD: ("initial_attack_time", structs.decode_BIG_f),
    0xDCA1E8B6: ("attack_time", structs.decode_BIG_f),
    0x9F269614: ("attack_time_variance", structs.decode_BIG_f),
    0x059B46CF: ("unknown_0x059b46cf", structs.decode_BIG_f),
    0x1AA98D7F: ("unknown_0x1aa98d7f", structs.decode_BIG_f),
    0xFDD2FE20: ("junction_vulnerability", _decode_junction_vulnerability),
    0xC108CFA0: ("unknown_struct7", _decode_unknown_struct7),
    0x91502686: ("unknown_struct11", _decode_unknown_struct11),
    0xAD62C993: ("unknown_struct12", _decode_unknown_struct12),
    0x03A319DF: ("unknown_struct13", _decode_unknown_struct13),
    0x9DD3BB57: ("unknown_struct14", _decode_unknown_struct14),
}
