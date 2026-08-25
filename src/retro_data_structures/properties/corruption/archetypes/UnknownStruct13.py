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
from retro_data_structures.properties.corruption.archetypes.UnknownStruct7 import UnknownStruct7
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct13Json(typing_extensions.TypedDict):
        beam_info: json_util.JsonObject
        damage: json_util.JsonObject
        attack_duration: float
        attack_duration_variance: float
        turn_speed: float
        movement_speed: float
        unknown_0x569e40ef: float
        unknown_0x682b8867: float
        unknown_0x0acbf084: float
        unknown_0xb638cfa7: float
        unknown_0x18505e36: float
        unknown_struct7: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct13(BaseProperty):
    beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x1598012A,
                original_name="BeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
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
    attack_duration: float = dataclasses.field(
        default=7.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x16342C18, original_name="AttackDuration"),
        },
    )
    attack_duration_variance: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF6BDAFB8, original_name="AttackDurationVariance"),
        },
    )
    turn_speed: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x020C78BB, original_name="TurnSpeed"),
        },
    )
    movement_speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x416F15E8, original_name="MovementSpeed"),
        },
    )
    unknown_0x569e40ef: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x569E40EF, original_name="Unknown"),
        },
    )
    unknown_0x682b8867: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x682B8867, original_name="Unknown"),
        },
    )
    unknown_0x0acbf084: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0ACBF084, original_name="Unknown"),
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
        if property_count != 12:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1598012A
        beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16342C18
        attack_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF6BDAFB8
        attack_duration_variance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020C78BB
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x416F15E8
        movement_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x569E40EF
        unknown_0x569e40ef = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x682B8867
        unknown_0x682b8867 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ACBF084
        unknown_0x0acbf084 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB638CFA7
        unknown_0xb638cfa7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18505E36
        unknown_0x18505e36 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x659DF76D
        unknown_struct7 = UnknownStruct7.from_stream(data, game, property_size)

        return cls(
            beam_info,
            damage,
            attack_duration,
            attack_duration_variance,
            turn_speed,
            movement_speed,
            unknown_0x569e40ef,
            unknown_0x682b8867,
            unknown_0x0acbf084,
            unknown_0xb638cfa7,
            unknown_0x18505e36,
            unknown_struct7,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0c")  # 12 properties

        data.write(b"\x15\x98\x01*")  # 0x1598012a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x164,\x18")  # 0x16342c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_duration))

        data.write(b"\xf6\xbd\xaf\xb8")  # 0xf6bdafb8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_duration_variance))

        data.write(b"\x02\x0cx\xbb")  # 0x20c78bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b"Ao\x15\xe8")  # 0x416f15e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.movement_speed))

        data.write(b"V\x9e@\xef")  # 0x569e40ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x569e40ef))

        data.write(b"h+\x88g")  # 0x682b8867
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x682b8867))

        data.write(b"\n\xcb\xf0\x84")  # 0xacbf084
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0acbf084))

        data.write(b"\xb68\xcf\xa7")  # 0xb638cfa7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb638cfa7))

        data.write(b"\x18P^6")  # 0x18505e36
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x18505e36))

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
        json_data = typing.cast("UnknownStruct13Json", data)
        return cls(
            beam_info=PlasmaBeamInfo.from_json(json_data["beam_info"]),
            damage=DamageInfo.from_json(json_data["damage"]),
            attack_duration=json_data["attack_duration"],
            attack_duration_variance=json_data["attack_duration_variance"],
            turn_speed=json_data["turn_speed"],
            movement_speed=json_data["movement_speed"],
            unknown_0x569e40ef=json_data["unknown_0x569e40ef"],
            unknown_0x682b8867=json_data["unknown_0x682b8867"],
            unknown_0x0acbf084=json_data["unknown_0x0acbf084"],
            unknown_0xb638cfa7=json_data["unknown_0xb638cfa7"],
            unknown_0x18505e36=json_data["unknown_0x18505e36"],
            unknown_struct7=UnknownStruct7.from_json(json_data["unknown_struct7"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "beam_info": self.beam_info.to_json(),
            "damage": self.damage.to_json(),
            "attack_duration": self.attack_duration,
            "attack_duration_variance": self.attack_duration_variance,
            "turn_speed": self.turn_speed,
            "movement_speed": self.movement_speed,
            "unknown_0x569e40ef": self.unknown_0x569e40ef,
            "unknown_0x682b8867": self.unknown_0x682b8867,
            "unknown_0x0acbf084": self.unknown_0x0acbf084,
            "unknown_0xb638cfa7": self.unknown_0xb638cfa7,
            "unknown_0x18505e36": self.unknown_0x18505e36,
            "unknown_struct7": self.unknown_struct7.to_json(),
        }


def _decode_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_unknown_struct7(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct7:
    return UnknownStruct7.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1598012A: ("beam_info", _decode_beam_info),
    0x337F9524: ("damage", _decode_damage),
    0x16342C18: ("attack_duration", structs.decode_BIG_f),
    0xF6BDAFB8: ("attack_duration_variance", structs.decode_BIG_f),
    0x020C78BB: ("turn_speed", structs.decode_BIG_f),
    0x416F15E8: ("movement_speed", structs.decode_BIG_f),
    0x569E40EF: ("unknown_0x569e40ef", structs.decode_BIG_f),
    0x682B8867: ("unknown_0x682b8867", structs.decode_BIG_f),
    0x0ACBF084: ("unknown_0x0acbf084", structs.decode_BIG_f),
    0xB638CFA7: ("unknown_0xb638cfa7", structs.decode_BIG_f),
    0x18505E36: ("unknown_0x18505e36", structs.decode_BIG_f),
    0x659DF76D: ("unknown_struct7", _decode_unknown_struct7),
}
