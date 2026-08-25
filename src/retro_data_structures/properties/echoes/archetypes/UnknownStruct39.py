# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct39Json(typing_extensions.TypedDict):
        start_state: int
        explosion_damage: json_util.JsonObject
        min_height: float
        max_height: float
        min_down_height: float
        max_down_height: float
        separation_distance: float
        min_life_time: float
        max_life_time: float
        normal_knockback: float
        heavy_knockback: float
        knockback_decline: float
        is_dark_shredder: bool
        desired_distance: float


@dataclasses.dataclass()
class UnknownStruct39(BaseProperty):
    start_state: int = dataclasses.field(
        default=10,
        metadata={
            "reflection": FieldReflection[int](int, id=0x46D866D1, original_name="StartState"),
        },
    )
    explosion_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xDEFF74EA,
                original_name="ExplosionDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    min_height: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC6C4232C, original_name="MinHeight"),
        },
    )
    max_height: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7FE2B85D, original_name="MaxHeight"),
        },
    )
    min_down_height: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x10BE8AD3, original_name="MinDownHeight"),
        },
    )
    max_down_height: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x43189237, original_name="MaxDownHeight"),
        },
    )
    separation_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x01559F27, original_name="SeparationDistance"),
        },
    )
    min_life_time: float = dataclasses.field(
        default=14.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x07DCD404, original_name="MinLifeTime"),
        },
    )
    max_life_time: float = dataclasses.field(
        default=16.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x56256F59, original_name="MaxLifeTime"),
        },
    )
    normal_knockback: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3061976C, original_name="NormalKnockback"),
        },
    )
    heavy_knockback: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x93A80AA2, original_name="HeavyKnockback"),
        },
    )
    knockback_decline: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4C6B2421, original_name="KnockbackDecline"),
        },
    )
    is_dark_shredder: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCFF9971B, original_name="IsDarkShredder"),
        },
    )
    desired_distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x60BE35A1, original_name="DesiredDistance"),
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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46D866D1
        start_state = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDEFF74EA
        explosion_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6C4232C
        min_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FE2B85D
        max_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10BE8AD3
        min_down_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43189237
        max_down_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01559F27
        separation_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07DCD404
        min_life_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56256F59
        max_life_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3061976C
        normal_knockback = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93A80AA2
        heavy_knockback = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4C6B2421
        knockback_decline = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFF9971B
        is_dark_shredder = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60BE35A1
        desired_distance = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            start_state,
            explosion_damage,
            min_height,
            max_height,
            min_down_height,
            max_down_height,
            separation_distance,
            min_life_time,
            max_life_time,
            normal_knockback,
            heavy_knockback,
            knockback_decline,
            is_dark_shredder,
            desired_distance,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"F\xd8f\xd1")  # 0x46d866d1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.start_state))

        data.write(b"\xde\xfft\xea")  # 0xdeff74ea
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.explosion_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\xc4#,")  # 0xc6c4232c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_height))

        data.write(b"\x7f\xe2\xb8]")  # 0x7fe2b85d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_height))

        data.write(b"\x10\xbe\x8a\xd3")  # 0x10be8ad3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_down_height))

        data.write(b"C\x18\x927")  # 0x43189237
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_down_height))

        data.write(b"\x01U\x9f'")  # 0x1559f27
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.separation_distance))

        data.write(b"\x07\xdc\xd4\x04")  # 0x7dcd404
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_life_time))

        data.write(b"V%oY")  # 0x56256f59
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_life_time))

        data.write(b"0a\x97l")  # 0x3061976c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.normal_knockback))

        data.write(b"\x93\xa8\n\xa2")  # 0x93a80aa2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.heavy_knockback))

        data.write(b"Lk$!")  # 0x4c6b2421
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.knockback_decline))

        data.write(b"\xcf\xf9\x97\x1b")  # 0xcff9971b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_dark_shredder))

        data.write(b"`\xbe5\xa1")  # 0x60be35a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.desired_distance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct39Json", data)
        return cls(
            start_state=json_data["start_state"],
            explosion_damage=DamageInfo.from_json(json_data["explosion_damage"]),
            min_height=json_data["min_height"],
            max_height=json_data["max_height"],
            min_down_height=json_data["min_down_height"],
            max_down_height=json_data["max_down_height"],
            separation_distance=json_data["separation_distance"],
            min_life_time=json_data["min_life_time"],
            max_life_time=json_data["max_life_time"],
            normal_knockback=json_data["normal_knockback"],
            heavy_knockback=json_data["heavy_knockback"],
            knockback_decline=json_data["knockback_decline"],
            is_dark_shredder=json_data["is_dark_shredder"],
            desired_distance=json_data["desired_distance"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "start_state": self.start_state,
            "explosion_damage": self.explosion_damage.to_json(),
            "min_height": self.min_height,
            "max_height": self.max_height,
            "min_down_height": self.min_down_height,
            "max_down_height": self.max_down_height,
            "separation_distance": self.separation_distance,
            "min_life_time": self.min_life_time,
            "max_life_time": self.max_life_time,
            "normal_knockback": self.normal_knockback,
            "heavy_knockback": self.heavy_knockback,
            "knockback_decline": self.knockback_decline,
            "is_dark_shredder": self.is_dark_shredder,
            "desired_distance": self.desired_distance,
        }


def _decode_explosion_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x46D866D1: ("start_state", structs.decode_BIG_l),
    0xDEFF74EA: ("explosion_damage", _decode_explosion_damage),
    0xC6C4232C: ("min_height", structs.decode_BIG_f),
    0x7FE2B85D: ("max_height", structs.decode_BIG_f),
    0x10BE8AD3: ("min_down_height", structs.decode_BIG_f),
    0x43189237: ("max_down_height", structs.decode_BIG_f),
    0x01559F27: ("separation_distance", structs.decode_BIG_f),
    0x07DCD404: ("min_life_time", structs.decode_BIG_f),
    0x56256F59: ("max_life_time", structs.decode_BIG_f),
    0x3061976C: ("normal_knockback", structs.decode_BIG_f),
    0x93A80AA2: ("heavy_knockback", structs.decode_BIG_f),
    0x4C6B2421: ("knockback_decline", structs.decode_BIG_f),
    0xCFF9971B: ("is_dark_shredder", structs.decode_BIG_bool_),
    0x60BE35A1: ("desired_distance", structs.decode_BIG_f),
}
