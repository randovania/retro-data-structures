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
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TriggerInfoJson(typing_extensions.TypedDict):
        unknown_0x97c0611f: int
        unknown_0x50224907: int
        unknown_0x46cc1b48: bool
        damage_spline: json_util.JsonObject
        damage: json_util.JsonObject
        force_field: json_util.JsonValue


@dataclasses.dataclass()
class TriggerInfo(BaseProperty):
    unknown_0x97c0611f: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x97C0611F, original_name="Unknown"),
        },
    )  # Flagset
    unknown_0x50224907: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x50224907, original_name="Unknown"),
        },
    )
    unknown_0x46cc1b48: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x46CC1B48, original_name="Unknown"),
        },
    )
    damage_spline: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xFA873A67, original_name="DamageSpline", from_json=Spline.from_json, to_json=Spline.to_json
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
    force_field: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x20927E9B, original_name="ForceField", from_json=Vector.from_json, to_json=Vector.to_json
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
        if property_count != 6:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97C0611F
        unknown_0x97c0611f = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50224907
        unknown_0x50224907 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46CC1B48
        unknown_0x46cc1b48 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFA873A67
        damage_spline = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20927E9B
        force_field = Vector.from_stream(data, game, property_size)

        return cls(unknown_0x97c0611f, unknown_0x50224907, unknown_0x46cc1b48, damage_spline, damage, force_field)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"\x97\xc0a\x1f")  # 0x97c0611f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x97c0611f))

        data.write(b'P"I\x07')  # 0x50224907
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x50224907))

        data.write(b"F\xcc\x1bH")  # 0x46cc1b48
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x46cc1b48))

        data.write(b"\xfa\x87:g")  # 0xfa873a67
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_spline.to_stream(data, game)
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

        data.write(b" \x92~\x9b")  # 0x20927e9b
        data.write(b"\x00\x0c")  # size
        self.force_field.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TriggerInfoJson", data)
        return cls(
            unknown_0x97c0611f=json_data["unknown_0x97c0611f"],
            unknown_0x50224907=json_data["unknown_0x50224907"],
            unknown_0x46cc1b48=json_data["unknown_0x46cc1b48"],
            damage_spline=Spline.from_json(json_data["damage_spline"]),
            damage=DamageInfo.from_json(json_data["damage"]),
            force_field=Vector.from_json(json_data["force_field"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x97c0611f": self.unknown_0x97c0611f,
            "unknown_0x50224907": self.unknown_0x50224907,
            "unknown_0x46cc1b48": self.unknown_0x46cc1b48,
            "damage_spline": self.damage_spline.to_json(),
            "damage": self.damage.to_json(),
            "force_field": self.force_field.to_json(),
        }


def _decode_damage_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_force_field(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x97C0611F: ("unknown_0x97c0611f", structs.decode_BIG_L),
    0x50224907: ("unknown_0x50224907", structs.decode_BIG_l),
    0x46CC1B48: ("unknown_0x46cc1b48", structs.decode_BIG_bool_),
    0xFA873A67: ("damage_spline", _decode_damage_spline),
    0x337F9524: ("damage", _decode_damage),
    0x20927E9B: ("force_field", _decode_force_field),
}
