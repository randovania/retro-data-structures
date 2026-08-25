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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct47Json(typing_extensions.TypedDict):
        attack_speed: float
        delay_time: float
        drop_delay: float
        launch_speed: float
        drop_height: float
        radius_damage: json_util.JsonObject
        collision_offset: json_util.JsonValue
        turn_sound: int
        explode_range: float


@dataclasses.dataclass()
class UnknownStruct47(BaseProperty):
    attack_speed: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C0A2BC8, original_name="AttackSpeed"),
        },
    )
    delay_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E16E012, original_name="DelayTime"),
        },
    )
    drop_delay: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0097F282, original_name="DropDelay"),
        },
    )
    launch_speed: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x31381A17, original_name="LaunchSpeed"),
        },
    )
    drop_height: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x38A5566F, original_name="DropHeight"),
        },
    )
    radius_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x086D58DD,
                original_name="RadiusDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    collision_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x2E686C2A,
                original_name="CollisionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    turn_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC4C39403, original_name="TurnSound"),
        },
    )
    explode_range: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9A9A39B3, original_name="ExplodeRange"),
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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C0A2BC8
        attack_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8E16E012
        delay_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0097F282
        drop_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31381A17
        launch_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38A5566F
        drop_height = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x086D58DD
        radius_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E686C2A
        collision_offset = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4C39403
        turn_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A9A39B3
        explode_range = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            attack_speed,
            delay_time,
            drop_delay,
            launch_speed,
            drop_height,
            radius_damage,
            collision_offset,
            turn_sound,
            explode_range,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"l\n+\xc8")  # 0x6c0a2bc8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_speed))

        data.write(b"\x8e\x16\xe0\x12")  # 0x8e16e012
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.delay_time))

        data.write(b"\x00\x97\xf2\x82")  # 0x97f282
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.drop_delay))

        data.write(b"18\x1a\x17")  # 0x31381a17
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.launch_speed))

        data.write(b"8\xa5Vo")  # 0x38a5566f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.drop_height))

        data.write(b"\x08mX\xdd")  # 0x86d58dd
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.radius_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b".hl*")  # 0x2e686c2a
        data.write(b"\x00\x0c")  # size
        self.collision_offset.to_stream(data, game)

        data.write(b"\xc4\xc3\x94\x03")  # 0xc4c39403
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.turn_sound))

        data.write(b"\x9a\x9a9\xb3")  # 0x9a9a39b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.explode_range))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct47Json", data)
        return cls(
            attack_speed=json_data["attack_speed"],
            delay_time=json_data["delay_time"],
            drop_delay=json_data["drop_delay"],
            launch_speed=json_data["launch_speed"],
            drop_height=json_data["drop_height"],
            radius_damage=DamageInfo.from_json(json_data["radius_damage"]),
            collision_offset=Vector.from_json(json_data["collision_offset"]),
            turn_sound=json_data["turn_sound"],
            explode_range=json_data["explode_range"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "attack_speed": self.attack_speed,
            "delay_time": self.delay_time,
            "drop_delay": self.drop_delay,
            "launch_speed": self.launch_speed,
            "drop_height": self.drop_height,
            "radius_damage": self.radius_damage.to_json(),
            "collision_offset": self.collision_offset.to_json(),
            "turn_sound": self.turn_sound,
            "explode_range": self.explode_range,
        }


def _decode_radius_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6C0A2BC8: ("attack_speed", structs.decode_BIG_f),
    0x8E16E012: ("delay_time", structs.decode_BIG_f),
    0x0097F282: ("drop_delay", structs.decode_BIG_f),
    0x31381A17: ("launch_speed", structs.decode_BIG_f),
    0x38A5566F: ("drop_height", structs.decode_BIG_f),
    0x086D58DD: ("radius_damage", _decode_radius_damage),
    0x2E686C2A: ("collision_offset", _decode_collision_offset),
    0xC4C39403: ("turn_sound", structs.decode_BIG_Q),
    0x9A9A39B3: ("explode_range", structs.decode_BIG_f),
}
