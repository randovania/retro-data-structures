# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.UnknownStruct2 import UnknownStruct2
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class EmperorIngStage3StructBJson(typing_extensions.TypedDict):
        min_health_percentage: float
        unknown_0x95e7a2c2: float
        unknown_0x76ba1c18: float
        unknown_struct2_0x3826ec75: json_util.JsonObject
        unknown_struct2_0x93bf1106: json_util.JsonObject
        unknown_struct2_0xc4b88b80: json_util.JsonObject
        unknown_struct2_0x32c6dc77: json_util.JsonObject
        unknown_struct2_0xc6e7b293: json_util.JsonObject
        unknown_struct2_0x20746b56: json_util.JsonObject
        unknown_struct2_0x2ab44adb: json_util.JsonObject
        unknown_struct2_0xe2e78a78: json_util.JsonObject


@dataclasses.dataclass()
class EmperorIngStage3StructB(BaseProperty):
    min_health_percentage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDFEA46B3, original_name="MinHealthPercentage"),
        },
    )
    unknown_0x95e7a2c2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95E7A2C2, original_name="Unknown"),
        },
    )
    unknown_0x76ba1c18: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x76BA1C18, original_name="Unknown"),
        },
    )
    unknown_struct2_0x3826ec75: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0x3826EC75,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0x93bf1106: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0x93BF1106,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0xc4b88b80: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0xC4B88B80,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0x32c6dc77: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0x32C6DC77,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0xc6e7b293: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0xC6E7B293,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0x20746b56: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0x20746B56,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0x2ab44adb: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0x2AB44ADB,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
            ),
        },
    )
    unknown_struct2_0xe2e78a78: UnknownStruct2 = dataclasses.field(
        default_factory=UnknownStruct2,
        metadata={
            "reflection": FieldReflection[UnknownStruct2](
                UnknownStruct2,
                id=0xE2E78A78,
                original_name="UnknownStruct2",
                from_json=UnknownStruct2.from_json,
                to_json=UnknownStruct2.to_json,
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
        assert property_id == 0xDFEA46B3
        min_health_percentage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95E7A2C2
        unknown_0x95e7a2c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76BA1C18
        unknown_0x76ba1c18 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3826EC75
        unknown_struct2_0x3826ec75 = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93BF1106
        unknown_struct2_0x93bf1106 = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC4B88B80
        unknown_struct2_0xc4b88b80 = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32C6DC77
        unknown_struct2_0x32c6dc77 = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC6E7B293
        unknown_struct2_0xc6e7b293 = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20746B56
        unknown_struct2_0x20746b56 = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2AB44ADB
        unknown_struct2_0x2ab44adb = UnknownStruct2.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2E78A78
        unknown_struct2_0xe2e78a78 = UnknownStruct2.from_stream(data, game, property_size)

        return cls(
            min_health_percentage,
            unknown_0x95e7a2c2,
            unknown_0x76ba1c18,
            unknown_struct2_0x3826ec75,
            unknown_struct2_0x93bf1106,
            unknown_struct2_0xc4b88b80,
            unknown_struct2_0x32c6dc77,
            unknown_struct2_0xc6e7b293,
            unknown_struct2_0x20746b56,
            unknown_struct2_0x2ab44adb,
            unknown_struct2_0xe2e78a78,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"\xdf\xeaF\xb3")  # 0xdfea46b3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.min_health_percentage))

        data.write(b"\x95\xe7\xa2\xc2")  # 0x95e7a2c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95e7a2c2))

        data.write(b"v\xba\x1c\x18")  # 0x76ba1c18
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x76ba1c18))

        data.write(b"8&\xecu")  # 0x3826ec75
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0x3826ec75.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x93\xbf\x11\x06")  # 0x93bf1106
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0x93bf1106.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc4\xb8\x8b\x80")  # 0xc4b88b80
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0xc4b88b80.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"2\xc6\xdcw")  # 0x32c6dc77
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0x32c6dc77.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc6\xe7\xb2\x93")  # 0xc6e7b293
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0xc6e7b293.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b" tkV")  # 0x20746b56
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0x20746b56.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"*\xb4J\xdb")  # 0x2ab44adb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0x2ab44adb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe2\xe7\x8ax")  # 0xe2e78a78
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct2_0xe2e78a78.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EmperorIngStage3StructBJson", data)
        return cls(
            min_health_percentage=json_data["min_health_percentage"],
            unknown_0x95e7a2c2=json_data["unknown_0x95e7a2c2"],
            unknown_0x76ba1c18=json_data["unknown_0x76ba1c18"],
            unknown_struct2_0x3826ec75=UnknownStruct2.from_json(json_data["unknown_struct2_0x3826ec75"]),
            unknown_struct2_0x93bf1106=UnknownStruct2.from_json(json_data["unknown_struct2_0x93bf1106"]),
            unknown_struct2_0xc4b88b80=UnknownStruct2.from_json(json_data["unknown_struct2_0xc4b88b80"]),
            unknown_struct2_0x32c6dc77=UnknownStruct2.from_json(json_data["unknown_struct2_0x32c6dc77"]),
            unknown_struct2_0xc6e7b293=UnknownStruct2.from_json(json_data["unknown_struct2_0xc6e7b293"]),
            unknown_struct2_0x20746b56=UnknownStruct2.from_json(json_data["unknown_struct2_0x20746b56"]),
            unknown_struct2_0x2ab44adb=UnknownStruct2.from_json(json_data["unknown_struct2_0x2ab44adb"]),
            unknown_struct2_0xe2e78a78=UnknownStruct2.from_json(json_data["unknown_struct2_0xe2e78a78"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "min_health_percentage": self.min_health_percentage,
            "unknown_0x95e7a2c2": self.unknown_0x95e7a2c2,
            "unknown_0x76ba1c18": self.unknown_0x76ba1c18,
            "unknown_struct2_0x3826ec75": self.unknown_struct2_0x3826ec75.to_json(),
            "unknown_struct2_0x93bf1106": self.unknown_struct2_0x93bf1106.to_json(),
            "unknown_struct2_0xc4b88b80": self.unknown_struct2_0xc4b88b80.to_json(),
            "unknown_struct2_0x32c6dc77": self.unknown_struct2_0x32c6dc77.to_json(),
            "unknown_struct2_0xc6e7b293": self.unknown_struct2_0xc6e7b293.to_json(),
            "unknown_struct2_0x20746b56": self.unknown_struct2_0x20746b56.to_json(),
            "unknown_struct2_0x2ab44adb": self.unknown_struct2_0x2ab44adb.to_json(),
            "unknown_struct2_0xe2e78a78": self.unknown_struct2_0xe2e78a78.to_json(),
        }


def _decode_unknown_struct2_0x3826ec75(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0x93bf1106(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0xc4b88b80(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0x32c6dc77(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0xc6e7b293(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0x20746b56(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0x2ab44adb(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


def _decode_unknown_struct2_0xe2e78a78(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct2:
    return UnknownStruct2.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xDFEA46B3: ("min_health_percentage", structs.decode_BIG_f),
    0x95E7A2C2: ("unknown_0x95e7a2c2", structs.decode_BIG_f),
    0x76BA1C18: ("unknown_0x76ba1c18", structs.decode_BIG_f),
    0x3826EC75: ("unknown_struct2_0x3826ec75", _decode_unknown_struct2_0x3826ec75),
    0x93BF1106: ("unknown_struct2_0x93bf1106", _decode_unknown_struct2_0x93bf1106),
    0xC4B88B80: ("unknown_struct2_0xc4b88b80", _decode_unknown_struct2_0xc4b88b80),
    0x32C6DC77: ("unknown_struct2_0x32c6dc77", _decode_unknown_struct2_0x32c6dc77),
    0xC6E7B293: ("unknown_struct2_0xc6e7b293", _decode_unknown_struct2_0xc6e7b293),
    0x20746B56: ("unknown_struct2_0x20746b56", _decode_unknown_struct2_0x20746b56),
    0x2AB44ADB: ("unknown_struct2_0x2ab44adb", _decode_unknown_struct2_0x2ab44adb),
    0xE2E78A78: ("unknown_struct2_0xe2e78a78", _decode_unknown_struct2_0xe2e78a78),
}
