# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MiscControls_UnknownStruct1Json(typing_extensions.TypedDict):
        unknown_0x10699c6f: json_util.JsonObject
        unknown_0x50de5441: json_util.JsonObject
        unknown_0xa9a26569: json_util.JsonObject
        unknown_0x6f71adf7: json_util.JsonObject


@dataclasses.dataclass()
class MiscControls_UnknownStruct1(BaseProperty):
    unknown_0x10699c6f: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x10699C6F,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x50de5441: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x50DE5441,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xa9a26569: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xA9A26569,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x6f71adf7: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x6F71ADF7,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
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
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10699C6F
        unknown_0x10699c6f = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50DE5441
        unknown_0x50de5441 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA9A26569
        unknown_0xa9a26569 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6F71ADF7
        unknown_0x6f71adf7 = RevolutionControl.from_stream(data, game, property_size)

        return cls(unknown_0x10699c6f, unknown_0x50de5441, unknown_0xa9a26569, unknown_0x6f71adf7)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\x10i\x9co")  # 0x10699c6f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x10699c6f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"P\xdeTA")  # 0x50de5441
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x50de5441.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa9\xa2ei")  # 0xa9a26569
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xa9a26569.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"oq\xad\xf7")  # 0x6f71adf7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x6f71adf7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MiscControls_UnknownStruct1Json", data)
        return cls(
            unknown_0x10699c6f=RevolutionControl.from_json(json_data["unknown_0x10699c6f"]),
            unknown_0x50de5441=RevolutionControl.from_json(json_data["unknown_0x50de5441"]),
            unknown_0xa9a26569=RevolutionControl.from_json(json_data["unknown_0xa9a26569"]),
            unknown_0x6f71adf7=RevolutionControl.from_json(json_data["unknown_0x6f71adf7"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x10699c6f": self.unknown_0x10699c6f.to_json(),
            "unknown_0x50de5441": self.unknown_0x50de5441.to_json(),
            "unknown_0xa9a26569": self.unknown_0xa9a26569.to_json(),
            "unknown_0x6f71adf7": self.unknown_0x6f71adf7.to_json(),
        }


def _decode_unknown_0x10699c6f(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x50de5441(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xa9a26569(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x6f71adf7(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x10699C6F: ("unknown_0x10699c6f", _decode_unknown_0x10699c6f),
    0x50DE5441: ("unknown_0x50de5441", _decode_unknown_0x50de5441),
    0xA9A26569: ("unknown_0xa9a26569", _decode_unknown_0xa9a26569),
    0x6F71ADF7: ("unknown_0x6f71adf7", _decode_unknown_0x6f71adf7),
}
