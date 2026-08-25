# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.UnknownStruct10 import UnknownStruct10
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SpriteStructJson(typing_extensions.TypedDict):
        loop: bool
        unknown_struct10_0x30613ecc: json_util.JsonObject
        unknown_struct10_0x19a98a3e: json_util.JsonObject
        unknown_struct10_0xb7c11baf: json_util.JsonObject
        unknown_struct10_0x4a38e3da: json_util.JsonObject
        unknown_struct10_0xe450724b: json_util.JsonObject
        unknown_struct10_0xcd98c6b9: json_util.JsonObject
        unknown_struct10_0x63f05728: json_util.JsonObject
        unknown_struct10_0xed1a3012: json_util.JsonObject
        unknown_struct10_0x4372a183: json_util.JsonObject
        unknown_struct10_0x2060e2f5: json_util.JsonObject


@dataclasses.dataclass()
class SpriteStruct(BaseProperty):
    loop: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEDA47FF6, original_name="Loop"),
        },
    )
    unknown_struct10_0x30613ecc: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0x30613ECC,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0x19a98a3e: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0x19A98A3E,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0xb7c11baf: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0xB7C11BAF,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0x4a38e3da: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0x4A38E3DA,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0xe450724b: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0xE450724B,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0xcd98c6b9: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0xCD98C6B9,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0x63f05728: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0x63F05728,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0xed1a3012: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0xED1A3012,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0x4372a183: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0x4372A183,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
            ),
        },
    )
    unknown_struct10_0x2060e2f5: UnknownStruct10 = dataclasses.field(
        default_factory=UnknownStruct10,
        metadata={
            "reflection": FieldReflection[UnknownStruct10](
                UnknownStruct10,
                id=0x2060E2F5,
                original_name="UnknownStruct10",
                from_json=UnknownStruct10.from_json,
                to_json=UnknownStruct10.to_json,
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
        if property_count != 11:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEDA47FF6
        loop = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30613ECC
        unknown_struct10_0x30613ecc = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19A98A3E
        unknown_struct10_0x19a98a3e = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7C11BAF
        unknown_struct10_0xb7c11baf = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4A38E3DA
        unknown_struct10_0x4a38e3da = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE450724B
        unknown_struct10_0xe450724b = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCD98C6B9
        unknown_struct10_0xcd98c6b9 = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63F05728
        unknown_struct10_0x63f05728 = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED1A3012
        unknown_struct10_0xed1a3012 = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4372A183
        unknown_struct10_0x4372a183 = UnknownStruct10.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2060E2F5
        unknown_struct10_0x2060e2f5 = UnknownStruct10.from_stream(data, game, property_size)

        return cls(
            loop,
            unknown_struct10_0x30613ecc,
            unknown_struct10_0x19a98a3e,
            unknown_struct10_0xb7c11baf,
            unknown_struct10_0x4a38e3da,
            unknown_struct10_0xe450724b,
            unknown_struct10_0xcd98c6b9,
            unknown_struct10_0x63f05728,
            unknown_struct10_0xed1a3012,
            unknown_struct10_0x4372a183,
            unknown_struct10_0x2060e2f5,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"\xed\xa4\x7f\xf6")  # 0xeda47ff6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.loop))

        data.write(b"0a>\xcc")  # 0x30613ecc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0x30613ecc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\xa9\x8a>")  # 0x19a98a3e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0x19a98a3e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb7\xc1\x1b\xaf")  # 0xb7c11baf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0xb7c11baf.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"J8\xe3\xda")  # 0x4a38e3da
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0x4a38e3da.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe4PrK")  # 0xe450724b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0xe450724b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcd\x98\xc6\xb9")  # 0xcd98c6b9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0xcd98c6b9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"c\xf0W(")  # 0x63f05728
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0x63f05728.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\x1a0\x12")  # 0xed1a3012
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0xed1a3012.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Cr\xa1\x83")  # 0x4372a183
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0x4372a183.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b" `\xe2\xf5")  # 0x2060e2f5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct10_0x2060e2f5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpriteStructJson", data)
        return cls(
            loop=json_data["loop"],
            unknown_struct10_0x30613ecc=UnknownStruct10.from_json(json_data["unknown_struct10_0x30613ecc"]),
            unknown_struct10_0x19a98a3e=UnknownStruct10.from_json(json_data["unknown_struct10_0x19a98a3e"]),
            unknown_struct10_0xb7c11baf=UnknownStruct10.from_json(json_data["unknown_struct10_0xb7c11baf"]),
            unknown_struct10_0x4a38e3da=UnknownStruct10.from_json(json_data["unknown_struct10_0x4a38e3da"]),
            unknown_struct10_0xe450724b=UnknownStruct10.from_json(json_data["unknown_struct10_0xe450724b"]),
            unknown_struct10_0xcd98c6b9=UnknownStruct10.from_json(json_data["unknown_struct10_0xcd98c6b9"]),
            unknown_struct10_0x63f05728=UnknownStruct10.from_json(json_data["unknown_struct10_0x63f05728"]),
            unknown_struct10_0xed1a3012=UnknownStruct10.from_json(json_data["unknown_struct10_0xed1a3012"]),
            unknown_struct10_0x4372a183=UnknownStruct10.from_json(json_data["unknown_struct10_0x4372a183"]),
            unknown_struct10_0x2060e2f5=UnknownStruct10.from_json(json_data["unknown_struct10_0x2060e2f5"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "loop": self.loop,
            "unknown_struct10_0x30613ecc": self.unknown_struct10_0x30613ecc.to_json(),
            "unknown_struct10_0x19a98a3e": self.unknown_struct10_0x19a98a3e.to_json(),
            "unknown_struct10_0xb7c11baf": self.unknown_struct10_0xb7c11baf.to_json(),
            "unknown_struct10_0x4a38e3da": self.unknown_struct10_0x4a38e3da.to_json(),
            "unknown_struct10_0xe450724b": self.unknown_struct10_0xe450724b.to_json(),
            "unknown_struct10_0xcd98c6b9": self.unknown_struct10_0xcd98c6b9.to_json(),
            "unknown_struct10_0x63f05728": self.unknown_struct10_0x63f05728.to_json(),
            "unknown_struct10_0xed1a3012": self.unknown_struct10_0xed1a3012.to_json(),
            "unknown_struct10_0x4372a183": self.unknown_struct10_0x4372a183.to_json(),
            "unknown_struct10_0x2060e2f5": self.unknown_struct10_0x2060e2f5.to_json(),
        }


def _decode_unknown_struct10_0x30613ecc(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0x19a98a3e(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0xb7c11baf(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0x4a38e3da(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0xe450724b(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0xcd98c6b9(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0x63f05728(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0xed1a3012(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0x4372a183(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


def _decode_unknown_struct10_0x2060e2f5(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct10:
    return UnknownStruct10.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xEDA47FF6: ("loop", structs.decode_BIG_bool_),
    0x30613ECC: ("unknown_struct10_0x30613ecc", _decode_unknown_struct10_0x30613ecc),
    0x19A98A3E: ("unknown_struct10_0x19a98a3e", _decode_unknown_struct10_0x19a98a3e),
    0xB7C11BAF: ("unknown_struct10_0xb7c11baf", _decode_unknown_struct10_0xb7c11baf),
    0x4A38E3DA: ("unknown_struct10_0x4a38e3da", _decode_unknown_struct10_0x4a38e3da),
    0xE450724B: ("unknown_struct10_0xe450724b", _decode_unknown_struct10_0xe450724b),
    0xCD98C6B9: ("unknown_struct10_0xcd98c6b9", _decode_unknown_struct10_0xcd98c6b9),
    0x63F05728: ("unknown_struct10_0x63f05728", _decode_unknown_struct10_0x63f05728),
    0xED1A3012: ("unknown_struct10_0xed1a3012", _decode_unknown_struct10_0xed1a3012),
    0x4372A183: ("unknown_struct10_0x4372a183", _decode_unknown_struct10_0x4372a183),
    0x2060E2F5: ("unknown_struct10_0x2060e2f5", _decode_unknown_struct10_0x2060e2f5),
}
