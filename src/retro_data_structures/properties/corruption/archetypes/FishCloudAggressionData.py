# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FishCloudAggressionDataJson(typing_extensions.TypedDict):
        attack_distance: float
        attack_cone: float
        attack_priority: float
        attack_kill_time: float
        attack_effect: int
        attack_effect_count: int
        attack_effect_scale: float
        attack_effect_rate: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x5EDA8D99, 0xE387D414, 0x8D1CF97A, 0x4E815E64, 0xB258D3E8, 0x39E08C8E, 0x34D4321C, 0x2459FC0A)


@dataclasses.dataclass()
class FishCloudAggressionData(BaseProperty):
    attack_distance: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5EDA8D99, original_name="AttackDistance"),
        },
    )
    attack_cone: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE387D414, original_name="AttackCone"),
        },
    )
    attack_priority: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D1CF97A, original_name="AttackPriority"),
        },
    )
    attack_kill_time: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4E815E64, original_name="AttackKillTime"),
        },
    )
    attack_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB258D3E8, original_name="AttackEffect"),
        },
    )
    attack_effect_count: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x39E08C8E, original_name="AttackEffectCount"),
        },
    )
    attack_effect_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x34D4321C, original_name="AttackEffectScale"),
        },
    )
    attack_effect_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2459FC0A, original_name="AttackEffectRate"),
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
        if property_count != 8:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHQLHlLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(84))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"^\xda\x8d\x99")  # 0x5eda8d99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_distance))

        data.write(b"\xe3\x87\xd4\x14")  # 0xe387d414
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_cone))

        data.write(b"\x8d\x1c\xf9z")  # 0x8d1cf97a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_priority))

        data.write(b"N\x81^d")  # 0x4e815e64
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_kill_time))

        data.write(b"\xb2X\xd3\xe8")  # 0xb258d3e8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.attack_effect))

        data.write(b"9\xe0\x8c\x8e")  # 0x39e08c8e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.attack_effect_count))

        data.write(b"4\xd42\x1c")  # 0x34d4321c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_effect_scale))

        data.write(b"$Y\xfc\n")  # 0x2459fc0a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attack_effect_rate))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FishCloudAggressionDataJson", data)
        return cls(
            attack_distance=json_data["attack_distance"],
            attack_cone=json_data["attack_cone"],
            attack_priority=json_data["attack_priority"],
            attack_kill_time=json_data["attack_kill_time"],
            attack_effect=json_data["attack_effect"],
            attack_effect_count=json_data["attack_effect_count"],
            attack_effect_scale=json_data["attack_effect_scale"],
            attack_effect_rate=json_data["attack_effect_rate"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "attack_distance": self.attack_distance,
            "attack_cone": self.attack_cone,
            "attack_priority": self.attack_priority,
            "attack_kill_time": self.attack_kill_time,
            "attack_effect": self.attack_effect,
            "attack_effect_count": self.attack_effect_count,
            "attack_effect_scale": self.attack_effect_scale,
            "attack_effect_rate": self.attack_effect_rate,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5EDA8D99: ("attack_distance", structs.decode_BIG_f),
    0xE387D414: ("attack_cone", structs.decode_BIG_f),
    0x8D1CF97A: ("attack_priority", structs.decode_BIG_f),
    0x4E815E64: ("attack_kill_time", structs.decode_BIG_f),
    0xB258D3E8: ("attack_effect", structs.decode_BIG_Q),
    0x39E08C8E: ("attack_effect_count", structs.decode_BIG_l),
    0x34D4321C: ("attack_effect_scale", structs.decode_BIG_f),
    0x2459FC0A: ("attack_effect_rate", structs.decode_BIG_f),
}
