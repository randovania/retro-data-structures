# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ConditionalTestJson(typing_extensions.TypedDict):
        boolean: int
        use_connected_as_amount: bool
        player_item: int
        amount_or_capacity: int
        condition: int
        use_connected_as_value: bool
        value: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xDE3E40A3, 0x794F9BEB, 0xD3AF8D72, 0x3BDEA98, 0x70729364, 0xAEB694B4, 0x8DB9398A)


@dataclasses.dataclass()
class ConditionalTest(BaseProperty):
    boolean: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDE3E40A3, original_name="Boolean"),
        },
    )  # Choice
    use_connected_as_amount: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x794F9BEB, original_name="UseConnectedAsAmount"),
        },
    )
    player_item: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0xD3AF8D72,
                original_name="PlayerItem",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    amount_or_capacity: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x03BDEA98, original_name="AmountOrCapacity"),
        },
    )
    condition: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x70729364, original_name="Condition"),
        },
    )
    use_connected_as_value: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAEB694B4, original_name="UseConnectedAsValue"),
        },
    )
    value: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x8DB9398A, original_name="Value"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHLLH?LHLLHlLHlLH?LHl")

        dec = _FAST_FORMAT.unpack(data.read(64))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            enums.PlayerItemEnum(dec[8]),
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xde>@\xa3")  # 0xde3e40a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.boolean))

        data.write(b"yO\x9b\xeb")  # 0x794f9beb
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_connected_as_amount))

        data.write(b"\xd3\xaf\x8dr")  # 0xd3af8d72
        data.write(b"\x00\x04")  # size
        self.player_item.to_stream(data, game)

        data.write(b"\x03\xbd\xea\x98")  # 0x3bdea98
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.amount_or_capacity))

        data.write(b"pr\x93d")  # 0x70729364
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.condition))

        data.write(b"\xae\xb6\x94\xb4")  # 0xaeb694b4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_connected_as_value))

        data.write(b"\x8d\xb99\x8a")  # 0x8db9398a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ConditionalTestJson", data)
        return cls(
            boolean=json_data["boolean"],
            use_connected_as_amount=json_data["use_connected_as_amount"],
            player_item=enums.PlayerItemEnum.from_json(json_data["player_item"]),
            amount_or_capacity=json_data["amount_or_capacity"],
            condition=json_data["condition"],
            use_connected_as_value=json_data["use_connected_as_value"],
            value=json_data["value"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "boolean": self.boolean,
            "use_connected_as_amount": self.use_connected_as_amount,
            "player_item": self.player_item.to_json(),
            "amount_or_capacity": self.amount_or_capacity,
            "condition": self.condition,
            "use_connected_as_value": self.use_connected_as_value,
            "value": self.value,
        }


def _decode_player_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDE3E40A3: ("boolean", structs.decode_BIG_L),
    0x794F9BEB: ("use_connected_as_amount", structs.decode_BIG_bool_),
    0xD3AF8D72: ("player_item", _decode_player_item),
    0x03BDEA98: ("amount_or_capacity", structs.decode_BIG_l),
    0x70729364: ("condition", structs.decode_BIG_l),
    0xAEB694B4: ("use_connected_as_value", structs.decode_BIG_bool_),
    0x8DB9398A: ("value", structs.decode_BIG_l),
}
