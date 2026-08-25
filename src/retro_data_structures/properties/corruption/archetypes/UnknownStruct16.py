# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct16Json(typing_extensions.TypedDict):
        damage: json_util.JsonObject
        damage_box_size: json_util.JsonValue
        unknown: float
        max_length: float
        burn_damage: float
        burn_duration: float
        damage_delay: float


@dataclasses.dataclass()
class UnknownStruct16(BaseProperty):
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
    damage_box_size: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=1.0, y=1.0, z=2.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x86368613, original_name="DamageBoxSize", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    unknown: float = dataclasses.field(
        default=215.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF2C3FC10, original_name="Unknown"),
        },
    )
    max_length: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7F30924C, original_name="MaxLength"),
        },
    )
    burn_damage: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCF201BFA, original_name="BurnDamage"),
        },
    )
    burn_duration: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x88137FA8, original_name="BurnDuration"),
        },
    )
    damage_delay: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8F4FB79D, original_name="DamageDelay"),
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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_damage": 5.0, "di_knock_back_power": 10.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86368613
        damage_box_size = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF2C3FC10
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7F30924C
        max_length = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCF201BFA
        burn_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88137FA8
        burn_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F4FB79D
        damage_delay = structs.BIG_f.unpack(data.read(4))[0]

        return cls(damage, damage_box_size, unknown, max_length, burn_damage, burn_duration, damage_delay)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game, default_override={"di_damage": 5.0, "di_knock_back_power": 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x866\x86\x13")  # 0x86368613
        data.write(b"\x00\x0c")  # size
        self.damage_box_size.to_stream(data, game)

        data.write(b"\xf2\xc3\xfc\x10")  # 0xf2c3fc10
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x7f0\x92L")  # 0x7f30924c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_length))

        data.write(b"\xcf \x1b\xfa")  # 0xcf201bfa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burn_damage))

        data.write(b"\x88\x13\x7f\xa8")  # 0x88137fa8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.burn_duration))

        data.write(b"\x8fO\xb7\x9d")  # 0x8f4fb79d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_delay))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct16Json", data)
        return cls(
            damage=DamageInfo.from_json(json_data["damage"]),
            damage_box_size=Vector.from_json(json_data["damage_box_size"]),
            unknown=json_data["unknown"],
            max_length=json_data["max_length"],
            burn_damage=json_data["burn_damage"],
            burn_duration=json_data["burn_duration"],
            damage_delay=json_data["damage_delay"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "damage": self.damage.to_json(),
            "damage_box_size": self.damage_box_size.to_json(),
            "unknown": self.unknown,
            "max_length": self.max_length,
            "burn_damage": self.burn_damage,
            "burn_duration": self.burn_duration,
            "damage_delay": self.damage_delay,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data, game, property_size, default_override={"di_damage": 5.0, "di_knock_back_power": 10.0}
    )


def _decode_damage_box_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x337F9524: ("damage", _decode_damage),
    0x86368613: ("damage_box_size", _decode_damage_box_size),
    0xF2C3FC10: ("unknown", structs.decode_BIG_f),
    0x7F30924C: ("max_length", structs.decode_BIG_f),
    0xCF201BFA: ("burn_damage", structs.decode_BIG_f),
    0x88137FA8: ("burn_duration", structs.decode_BIG_f),
    0x8F4FB79D: ("damage_delay", structs.decode_BIG_f),
}
