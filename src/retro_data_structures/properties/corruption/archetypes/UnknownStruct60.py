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

    class UnknownStruct60Json(typing_extensions.TypedDict):
        scale: float
        effect: int
        damage: json_util.JsonObject
        collision_size: json_util.JsonValue
        sound: int


@dataclasses.dataclass()
class UnknownStruct60(BaseProperty):
    scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C51A676, original_name="Scale"),
        },
    )
    effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB68C6D96, original_name="Effect"),
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
    collision_size: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x3A3E03BA, original_name="CollisionSize", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA55DACF6, original_name="Sound"),
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
        if property_count != 5:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C51A676
        scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB68C6D96
        effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A3E03BA
        collision_size = Vector.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA55DACF6
        sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(scale, effect, damage, collision_size, sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b",Q\xa6v")  # 0x2c51a676
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scale))

        data.write(b"\xb6\x8cm\x96")  # 0xb68c6d96
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.effect))

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b":>\x03\xba")  # 0x3a3e03ba
        data.write(b"\x00\x0c")  # size
        self.collision_size.to_stream(data, game)

        data.write(b"\xa5]\xac\xf6")  # 0xa55dacf6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct60Json", data)
        return cls(
            scale=json_data["scale"],
            effect=json_data["effect"],
            damage=DamageInfo.from_json(json_data["damage"]),
            collision_size=Vector.from_json(json_data["collision_size"]),
            sound=json_data["sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "scale": self.scale,
            "effect": self.effect,
            "damage": self.damage.to_json(),
            "collision_size": self.collision_size.to_json(),
            "sound": self.sound,
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_collision_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2C51A676: ("scale", structs.decode_BIG_f),
    0xB68C6D96: ("effect", structs.decode_BIG_Q),
    0x337F9524: ("damage", _decode_damage),
    0x3A3E03BA: ("collision_size", _decode_collision_size),
    0xA55DACF6: ("sound", structs.decode_BIG_Q),
}
