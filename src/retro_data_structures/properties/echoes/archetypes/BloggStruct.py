# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BloggStructJson(typing_extensions.TypedDict):
        unknown_0x3e505ddb: int
        unknown_0x118f1e46: int
        unknown_0x6e603df2: float
        unknown_0x1e74f1ec: float
        unknown_0xecba9fb2: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x3E505DDB, 0x118F1E46, 0x6E603DF2, 0x1E74F1EC, 0xECBA9FB2)


@dataclasses.dataclass()
class BloggStruct(BaseProperty):
    unknown_0x3e505ddb: int = dataclasses.field(
        default=-2143184152,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3E505DDB, original_name="Unknown"),
        },
    )
    unknown_0x118f1e46: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x118F1E46, original_name="Unknown"),
        },
    )
    unknown_0x6e603df2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6E603DF2, original_name="Unknown"),
        },
    )
    unknown_0x1e74f1ec: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1E74F1EC, original_name="Unknown"),
        },
    )
    unknown_0xecba9fb2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xECBA9FB2, original_name="Unknown"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHlLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(50))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b">P]\xdb")  # 0x3e505ddb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x3e505ddb))

        data.write(b"\x11\x8f\x1eF")  # 0x118f1e46
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x118f1e46))

        data.write(b"n`=\xf2")  # 0x6e603df2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6e603df2))

        data.write(b"\x1et\xf1\xec")  # 0x1e74f1ec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1e74f1ec))

        data.write(b"\xec\xba\x9f\xb2")  # 0xecba9fb2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xecba9fb2))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BloggStructJson", data)
        return cls(
            unknown_0x3e505ddb=json_data["unknown_0x3e505ddb"],
            unknown_0x118f1e46=json_data["unknown_0x118f1e46"],
            unknown_0x6e603df2=json_data["unknown_0x6e603df2"],
            unknown_0x1e74f1ec=json_data["unknown_0x1e74f1ec"],
            unknown_0xecba9fb2=json_data["unknown_0xecba9fb2"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x3e505ddb": self.unknown_0x3e505ddb,
            "unknown_0x118f1e46": self.unknown_0x118f1e46,
            "unknown_0x6e603df2": self.unknown_0x6e603df2,
            "unknown_0x1e74f1ec": self.unknown_0x1e74f1ec,
            "unknown_0xecba9fb2": self.unknown_0xecba9fb2,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3E505DDB: ("unknown_0x3e505ddb", structs.decode_BIG_l),
    0x118F1E46: ("unknown_0x118f1e46", structs.decode_BIG_l),
    0x6E603DF2: ("unknown_0x6e603df2", structs.decode_BIG_f),
    0x1E74F1EC: ("unknown_0x1e74f1ec", structs.decode_BIG_f),
    0xECBA9FB2: ("unknown_0xecba9fb2", structs.decode_BIG_f),
}
