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

    class TweakBall_PhazonBallJson(typing_extensions.TypedDict):
        phazon_ball_damage_delay: float
        phazon_ball_damage: json_util.JsonObject


@dataclasses.dataclass()
class TweakBall_PhazonBall(BaseProperty):
    phazon_ball_damage_delay: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47FFD5D6, original_name="PhazonBallDamageDelay"),
        },
    )
    phazon_ball_damage: TDamageInfo = dataclasses.field(
        default_factory=TDamageInfo,
        metadata={
            "reflection": FieldReflection[TDamageInfo](
                TDamageInfo,
                id=0x7EFF0EB1,
                original_name="PhazonBallDamage",
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
        assert property_id == 0x47FFD5D6
        phazon_ball_damage_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7EFF0EB1
        phazon_ball_damage = TDamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "weapon_type": 5,
                "damage_amount": 50.0,
                "radius_damage_amount": 50.0,
                "damage_radius": 5.0,
            },
        )

        return cls(phazon_ball_damage_delay, phazon_ball_damage)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"G\xff\xd5\xd6")  # 0x47ffd5d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_ball_damage_delay))

        data.write(b"~\xff\x0e\xb1")  # 0x7eff0eb1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phazon_ball_damage.to_stream(
            data,
            game,
            default_override={
                "weapon_type": 5,
                "damage_amount": 50.0,
                "radius_damage_amount": 50.0,
                "damage_radius": 5.0,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakBall_PhazonBallJson", data)
        return cls(
            phazon_ball_damage_delay=json_data["phazon_ball_damage_delay"],
            phazon_ball_damage=TDamageInfo.from_json(json_data["phazon_ball_damage"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "phazon_ball_damage_delay": self.phazon_ball_damage_delay,
            "phazon_ball_damage": self.phazon_ball_damage.to_json(),
        }


def _decode_phazon_ball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"weapon_type": 5, "damage_amount": 50.0, "radius_damage_amount": 50.0, "damage_radius": 5.0},
    )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x47FFD5D6: ("phazon_ball_damage_delay", structs.decode_BIG_f),
    0x7EFF0EB1: ("phazon_ball_damage", _decode_phazon_ball_damage),
}
