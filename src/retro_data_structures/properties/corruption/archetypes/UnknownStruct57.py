# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct56 import UnknownStruct56
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct57Json(typing_extensions.TypedDict):
        samus_gun_model: int
        min_roll_time: float
        max_roll_time: float
        min_attack_time: float
        max_attack_time: float
        min_attack_distance: float
        max_attack_distance: float
        unknown_0xce471a01: float
        attack_turn_threshold: float
        unknown_0x4113ffd8: float
        beam_tracking_speed: float
        unknown_struct56: json_util.JsonObject
        beam_attack: json_util.JsonObject
        beam_attack_damage: json_util.JsonObject
        unknown_0xe32082d1: float
        unknown_0xb71164a2: float
        unknown_0x3dc59b72: float
        unknown_0xba9eb1d2: float
        unknown_0xf0397134: float
        unknown_0x5dae4176: float
        radial_melee_damage: json_util.JsonObject
        elsc: int
        unknown_0xe0c37dfa: float


@dataclasses.dataclass()
class UnknownStruct57(BaseProperty):
    samus_gun_model: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x216ED1AD, original_name="SamusGunModel"),
        },
    )
    min_roll_time: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB8BAA8C0, original_name="MinRollTime"),
        },
    )
    max_roll_time: float = dataclasses.field(
        default=6.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE943139D, original_name="MaxRollTime"),
        },
    )
    min_attack_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2EDF3368, original_name="MinAttackTime"),
        },
    )
    max_attack_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7D792B8C, original_name="MaxAttackTime"),
        },
    )
    min_attack_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB825EAA, original_name="MinAttackDistance"),
        },
    )
    max_attack_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA95612C, original_name="MaxAttackDistance"),
        },
    )
    unknown_0xce471a01: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCE471A01, original_name="Unknown"),
        },
    )
    attack_turn_threshold: float = dataclasses.field(
        default=70.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAF2CB0A3, original_name="AttackTurnThreshold"),
        },
    )
    unknown_0x4113ffd8: float = dataclasses.field(
        default=0.6499999761581421,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4113FFD8, original_name="Unknown"),
        },
    )
    beam_tracking_speed: float = dataclasses.field(
        default=9.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2D8A9352, original_name="BeamTrackingSpeed"),
        },
    )
    unknown_struct56: UnknownStruct56 = dataclasses.field(
        default_factory=UnknownStruct56,
        metadata={
            "reflection": FieldReflection[UnknownStruct56](
                UnknownStruct56,
                id=0x84605259,
                original_name="UnknownStruct56",
                from_json=UnknownStruct56.from_json,
                to_json=UnknownStruct56.to_json,
            ),
        },
    )
    beam_attack: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x889672F5,
                original_name="BeamAttack",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    beam_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x202AFAA4,
                original_name="BeamAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xe32082d1: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE32082D1, original_name="Unknown"),
        },
    )
    unknown_0xb71164a2: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB71164A2, original_name="Unknown"),
        },
    )
    unknown_0x3dc59b72: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3DC59B72, original_name="Unknown"),
        },
    )
    unknown_0xba9eb1d2: float = dataclasses.field(
        default=72.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA9EB1D2, original_name="Unknown"),
        },
    )
    unknown_0xf0397134: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF0397134, original_name="Unknown"),
        },
    )
    unknown_0x5dae4176: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5DAE4176, original_name="Unknown"),
        },
    )
    radial_melee_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x5F11893B,
                original_name="RadialMeleeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    elsc: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ELSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xF3FA9B62, original_name="ELSC"),
        },
    )
    unknown_0xe0c37dfa: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE0C37DFA, original_name="Unknown"),
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
        assert property_id == 0x216ED1AD
        samus_gun_model = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8BAA8C0
        min_roll_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE943139D
        max_roll_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2EDF3368
        min_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7D792B8C
        max_attack_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB825EAA
        min_attack_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA95612C
        max_attack_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE471A01
        unknown_0xce471a01 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAF2CB0A3
        attack_turn_threshold = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4113FFD8
        unknown_0x4113ffd8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D8A9352
        beam_tracking_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84605259
        unknown_struct56 = UnknownStruct56.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x889672F5
        beam_attack = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x202AFAA4
        beam_attack_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE32082D1
        unknown_0xe32082d1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB71164A2
        unknown_0xb71164a2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DC59B72
        unknown_0x3dc59b72 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA9EB1D2
        unknown_0xba9eb1d2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF0397134
        unknown_0xf0397134 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5DAE4176
        unknown_0x5dae4176 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F11893B
        radial_melee_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF3FA9B62
        elsc = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0C37DFA
        unknown_0xe0c37dfa = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            samus_gun_model,
            min_roll_time,
            max_roll_time,
            min_attack_time,
            max_attack_time,
            min_attack_distance,
            max_attack_distance,
            unknown_0xce471a01,
            attack_turn_threshold,
            unknown_0x4113ffd8,
            beam_tracking_speed,
            unknown_struct56,
            beam_attack,
            beam_attack_damage,
            unknown_0xe32082d1,
            unknown_0xb71164a2,
            unknown_0x3dc59b72,
            unknown_0xba9eb1d2,
            unknown_0xf0397134,
            unknown_0x5dae4176,
            radial_melee_damage,
            elsc,
            unknown_0xe0c37dfa,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x17")  # 23 properties

        data.write(b"!n\xd1\xad")  # 0x216ed1ad
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.samus_gun_model))

        data.write(b"\xb8\xba\xa8\xc0")  # 0xb8baa8c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_roll_time))

        data.write(b"\xe9C\x13\x9d")  # 0xe943139d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_roll_time))

        data.write(b".\xdf3h")  # 0x2edf3368
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_time))

        data.write(b"}y+\x8c")  # 0x7d792b8c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_time))

        data.write(b"\xfb\x82^\xaa")  # 0xfb825eaa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_attack_distance))

        data.write(b"\xba\x95a,")  # 0xba95612c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_attack_distance))

        data.write(b"\xceG\x1a\x01")  # 0xce471a01
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xce471a01))

        data.write(b"\xaf,\xb0\xa3")  # 0xaf2cb0a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_turn_threshold))

        data.write(b"A\x13\xff\xd8")  # 0x4113ffd8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4113ffd8))

        data.write(b"-\x8a\x93R")  # 0x2d8a9352
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.beam_tracking_speed))

        data.write(b"\x84`RY")  # 0x84605259
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct56.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x88\x96r\xf5")  # 0x889672f5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b" *\xfa\xa4")  # 0x202afaa4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe3 \x82\xd1")  # 0xe32082d1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe32082d1))

        data.write(b"\xb7\x11d\xa2")  # 0xb71164a2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb71164a2))

        data.write(b"=\xc5\x9br")  # 0x3dc59b72
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3dc59b72))

        data.write(b"\xba\x9e\xb1\xd2")  # 0xba9eb1d2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xba9eb1d2))

        data.write(b"\xf09q4")  # 0xf0397134
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf0397134))

        data.write(b"]\xaeAv")  # 0x5dae4176
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5dae4176))

        data.write(b"_\x11\x89;")  # 0x5f11893b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.radial_melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf3\xfa\x9bb")  # 0xf3fa9b62
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.elsc))

        data.write(b"\xe0\xc3}\xfa")  # 0xe0c37dfa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe0c37dfa))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct57Json", data)
        return cls(
            samus_gun_model=json_data["samus_gun_model"],
            min_roll_time=json_data["min_roll_time"],
            max_roll_time=json_data["max_roll_time"],
            min_attack_time=json_data["min_attack_time"],
            max_attack_time=json_data["max_attack_time"],
            min_attack_distance=json_data["min_attack_distance"],
            max_attack_distance=json_data["max_attack_distance"],
            unknown_0xce471a01=json_data["unknown_0xce471a01"],
            attack_turn_threshold=json_data["attack_turn_threshold"],
            unknown_0x4113ffd8=json_data["unknown_0x4113ffd8"],
            beam_tracking_speed=json_data["beam_tracking_speed"],
            unknown_struct56=UnknownStruct56.from_json(json_data["unknown_struct56"]),
            beam_attack=PlasmaBeamInfo.from_json(json_data["beam_attack"]),
            beam_attack_damage=DamageInfo.from_json(json_data["beam_attack_damage"]),
            unknown_0xe32082d1=json_data["unknown_0xe32082d1"],
            unknown_0xb71164a2=json_data["unknown_0xb71164a2"],
            unknown_0x3dc59b72=json_data["unknown_0x3dc59b72"],
            unknown_0xba9eb1d2=json_data["unknown_0xba9eb1d2"],
            unknown_0xf0397134=json_data["unknown_0xf0397134"],
            unknown_0x5dae4176=json_data["unknown_0x5dae4176"],
            radial_melee_damage=DamageInfo.from_json(json_data["radial_melee_damage"]),
            elsc=json_data["elsc"],
            unknown_0xe0c37dfa=json_data["unknown_0xe0c37dfa"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "samus_gun_model": self.samus_gun_model,
            "min_roll_time": self.min_roll_time,
            "max_roll_time": self.max_roll_time,
            "min_attack_time": self.min_attack_time,
            "max_attack_time": self.max_attack_time,
            "min_attack_distance": self.min_attack_distance,
            "max_attack_distance": self.max_attack_distance,
            "unknown_0xce471a01": self.unknown_0xce471a01,
            "attack_turn_threshold": self.attack_turn_threshold,
            "unknown_0x4113ffd8": self.unknown_0x4113ffd8,
            "beam_tracking_speed": self.beam_tracking_speed,
            "unknown_struct56": self.unknown_struct56.to_json(),
            "beam_attack": self.beam_attack.to_json(),
            "beam_attack_damage": self.beam_attack_damage.to_json(),
            "unknown_0xe32082d1": self.unknown_0xe32082d1,
            "unknown_0xb71164a2": self.unknown_0xb71164a2,
            "unknown_0x3dc59b72": self.unknown_0x3dc59b72,
            "unknown_0xba9eb1d2": self.unknown_0xba9eb1d2,
            "unknown_0xf0397134": self.unknown_0xf0397134,
            "unknown_0x5dae4176": self.unknown_0x5dae4176,
            "radial_melee_damage": self.radial_melee_damage.to_json(),
            "elsc": self.elsc,
            "unknown_0xe0c37dfa": self.unknown_0xe0c37dfa,
        }


def _decode_unknown_struct56(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct56:
    return UnknownStruct56.from_stream(data, game, property_size)


def _decode_beam_attack(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_beam_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_radial_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x216ED1AD: ("samus_gun_model", structs.decode_BIG_Q),
    0xB8BAA8C0: ("min_roll_time", structs.decode_BIG_f),
    0xE943139D: ("max_roll_time", structs.decode_BIG_f),
    0x2EDF3368: ("min_attack_time", structs.decode_BIG_f),
    0x7D792B8C: ("max_attack_time", structs.decode_BIG_f),
    0xFB825EAA: ("min_attack_distance", structs.decode_BIG_f),
    0xBA95612C: ("max_attack_distance", structs.decode_BIG_f),
    0xCE471A01: ("unknown_0xce471a01", structs.decode_BIG_f),
    0xAF2CB0A3: ("attack_turn_threshold", structs.decode_BIG_f),
    0x4113FFD8: ("unknown_0x4113ffd8", structs.decode_BIG_f),
    0x2D8A9352: ("beam_tracking_speed", structs.decode_BIG_f),
    0x84605259: ("unknown_struct56", _decode_unknown_struct56),
    0x889672F5: ("beam_attack", _decode_beam_attack),
    0x202AFAA4: ("beam_attack_damage", _decode_beam_attack_damage),
    0xE32082D1: ("unknown_0xe32082d1", structs.decode_BIG_f),
    0xB71164A2: ("unknown_0xb71164a2", structs.decode_BIG_f),
    0x3DC59B72: ("unknown_0x3dc59b72", structs.decode_BIG_f),
    0xBA9EB1D2: ("unknown_0xba9eb1d2", structs.decode_BIG_f),
    0xF0397134: ("unknown_0xf0397134", structs.decode_BIG_f),
    0x5DAE4176: ("unknown_0x5dae4176", structs.decode_BIG_f),
    0x5F11893B: ("radial_melee_damage", _decode_radial_melee_damage),
    0xF3FA9B62: ("elsc", structs.decode_BIG_Q),
    0xE0C37DFA: ("unknown_0xe0c37dfa", structs.decode_BIG_f),
}
