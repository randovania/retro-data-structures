# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PIDConvergenceJson(typing_extensions.TypedDict):
        pid_type: int
        k_p: float
        k_i: float
        k_d: float


class PIDType(enum.IntEnum):
    Unknown1 = 1220683900
    Unknown2 = 1517782930

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xD0810123, 0xE82B99E1, 0xCCF2CAB2, 0x706CD96C)


@dataclasses.dataclass()
class PIDConvergence(BaseProperty):
    pid_type: PIDType = dataclasses.field(
        default=PIDType.Unknown2,
        metadata={
            "reflection": FieldReflection[PIDType](
                PIDType, id=0xD0810123, original_name="PIDType", from_json=PIDType.from_json, to_json=PIDType.to_json
            ),
        },
    )
    k_p: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE82B99E1, original_name="kP"),
        },
    )
    k_i: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCCF2CAB2, original_name="kI"),
        },
    )
    k_d: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x706CD96C, original_name="kD"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHLLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(40))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            PIDType(dec[2]),
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\xd0\x81\x01#")  # 0xd0810123
        data.write(b"\x00\x04")  # size
        self.pid_type.to_stream(data, game)

        data.write(b"\xe8+\x99\xe1")  # 0xe82b99e1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.k_p))

        data.write(b"\xcc\xf2\xca\xb2")  # 0xccf2cab2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.k_i))

        data.write(b"pl\xd9l")  # 0x706cd96c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.k_d))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PIDConvergenceJson", data)
        return cls(
            pid_type=PIDType.from_json(json_data["pid_type"]),
            k_p=json_data["k_p"],
            k_i=json_data["k_i"],
            k_d=json_data["k_d"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "pid_type": self.pid_type.to_json(),
            "k_p": self.k_p,
            "k_i": self.k_i,
            "k_d": self.k_d,
        }


def _decode_pid_type(data: typing.BinaryIO, game: Game, property_size: int) -> PIDType:
    return PIDType.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD0810123: ("pid_type", _decode_pid_type),
    0xE82B99E1: ("k_p", structs.decode_BIG_f),
    0xCCF2CAB2: ("k_i", structs.decode_BIG_f),
    0x706CD96C: ("k_d", structs.decode_BIG_f),
}
