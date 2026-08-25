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

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class KorbaMawDataJson(typing_extensions.TypedDict):
        bite_damage: json_util.JsonObject
        unknown_0x200f67e7: float
        unknown_0xe54de3e1: float
        unknown_0x8a821fee: float


@dataclasses.dataclass()
class KorbaMawData(BaseProperty):
    bite_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xDF636C4B,
                original_name="BiteDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x200f67e7: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x200F67E7, original_name="Unknown"),
        },
    )
    unknown_0xe54de3e1: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE54DE3E1, original_name="Unknown"),
        },
    )
    unknown_0x8a821fee: float = dataclasses.field(
        default=2.799999952316284,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8A821FEE, original_name="Unknown"),
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
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF636C4B
        bite_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x200F67E7
        unknown_0x200f67e7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE54DE3E1
        unknown_0xe54de3e1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8A821FEE
        unknown_0x8a821fee = structs.BIG_f.unpack(data.read(4))[0]

        return cls(bite_damage, unknown_0x200f67e7, unknown_0xe54de3e1, unknown_0x8a821fee)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\xdfclK")  # 0xdf636c4b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.bite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b" \x0fg\xe7")  # 0x200f67e7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x200f67e7))

        data.write(b"\xe5M\xe3\xe1")  # 0xe54de3e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe54de3e1))

        data.write(b"\x8a\x82\x1f\xee")  # 0x8a821fee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8a821fee))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KorbaMawDataJson", data)
        return cls(
            bite_damage=DamageInfo.from_json(json_data["bite_damage"]),
            unknown_0x200f67e7=json_data["unknown_0x200f67e7"],
            unknown_0xe54de3e1=json_data["unknown_0xe54de3e1"],
            unknown_0x8a821fee=json_data["unknown_0x8a821fee"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "bite_damage": self.bite_damage.to_json(),
            "unknown_0x200f67e7": self.unknown_0x200f67e7,
            "unknown_0xe54de3e1": self.unknown_0xe54de3e1,
            "unknown_0x8a821fee": self.unknown_0x8a821fee,
        }


def _decode_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDF636C4B: ("bite_damage", _decode_bite_damage),
    0x200F67E7: ("unknown_0x200f67e7", structs.decode_BIG_f),
    0xE54DE3E1: ("unknown_0xe54de3e1", structs.decode_BIG_f),
    0x8A821FEE: ("unknown_0x8a821fee", structs.decode_BIG_f),
}
