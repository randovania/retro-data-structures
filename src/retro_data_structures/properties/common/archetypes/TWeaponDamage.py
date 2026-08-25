# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.common.archetypes.TDamageInfo import TDamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TWeaponDamageJson(typing_extensions.TypedDict):
        normal: json_util.JsonObject
        charged: json_util.JsonObject


@dataclasses.dataclass()
class TWeaponDamage(BaseProperty):
    normal: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0x8AC4278A,
                original_name="Normal",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
            ),
        },
    )
    charged: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0xC9AC01D2,
                original_name="Charged",
                from_json=TDamageInfo.from_json,
                to_json=TDamageInfo.to_json,
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
        if property_count != 2:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8AC4278A
        normal = TDamageInfo.from_stream(
            data, game, property_size, default_override={"damage_amount": 50.0, "radius_damage_amount": 25.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9AC01D2
        charged = TDamageInfo.from_stream(
            data, game, property_size, default_override={"damage_amount": 50.0, "radius_damage_amount": 25.0}
        )

        return cls(normal, charged)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\x8a\xc4'\x8a")  # 0x8ac4278a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.normal.to_stream(data, game, default_override={"damage_amount": 50.0, "radius_damage_amount": 25.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc9\xac\x01\xd2")  # 0xc9ac01d2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.charged.to_stream(data, game, default_override={"damage_amount": 50.0, "radius_damage_amount": 25.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TWeaponDamageJson", data)
        return cls(
            normal=TDamageInfo.from_json(json_data["normal"]),
            charged=TDamageInfo.from_json(json_data["charged"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "normal": self.normal.to_json(),
            "charged": self.charged.to_json(),
        }


def _decode_normal(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data, game, property_size, default_override={"damage_amount": 50.0, "radius_damage_amount": 25.0}
    )


def _decode_charged(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data, game, property_size, default_override={"damage_amount": 50.0, "radius_damage_amount": 25.0}
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8AC4278A: ("normal", _decode_normal),
    0xC9AC01D2: ("charged", _decode_charged),
}
