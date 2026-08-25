# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakTargeting_UnknownStruct2Json(typing_extensions.TypedDict):
        unknown_0x4b435047: float
        unknown_0x0ece183c: float
        unknown_0xab03dcb9: float
        unknown_0xc0120b9e: float
        unknown_0xf5230e61: float
        unknown_0x70caf349: float
        unknown_0x955a5177: float
        unknown_0x95ed96c2: float
        unknown_0x138b3979: json_util.JsonObject
        unknown_0xdfa46325: json_util.JsonObject


@dataclasses.dataclass()
class TweakTargeting_UnknownStruct2(BaseProperty):
    unknown_0x4b435047: float = dataclasses.field(
        default=500.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B435047, original_name="Unknown"),
        },
    )
    unknown_0x0ece183c: float = dataclasses.field(
        default=-0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0ECE183C, original_name="Unknown"),
        },
    )
    unknown_0xab03dcb9: float = dataclasses.field(
        default=0.6000000238418579,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAB03DCB9, original_name="Unknown"),
        },
    )
    unknown_0xc0120b9e: float = dataclasses.field(
        default=0.44999998807907104,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC0120B9E, original_name="Unknown"),
        },
    )
    unknown_0xf5230e61: float = dataclasses.field(
        default=0.75,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF5230E61, original_name="Unknown"),
        },
    )
    unknown_0x70caf349: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x70CAF349, original_name="Unknown"),
        },
    )
    unknown_0x955a5177: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x955A5177, original_name="Unknown"),
        },
    )
    unknown_0x95ed96c2: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x95ED96C2, original_name="Unknown"),
        },
    )
    unknown_0x138b3979: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x138B3979, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xdfa46325: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xDFA46325, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B435047
        unknown_0x4b435047 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ECE183C
        unknown_0x0ece183c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAB03DCB9
        unknown_0xab03dcb9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC0120B9E
        unknown_0xc0120b9e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5230E61
        unknown_0xf5230e61 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70CAF349
        unknown_0x70caf349 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x955A5177
        unknown_0x955a5177 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95ED96C2
        unknown_0x95ed96c2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x138B3979
        unknown_0x138b3979 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDFA46325
        unknown_0xdfa46325 = Spline.from_stream(data, game, property_size)

        return cls(
            unknown_0x4b435047,
            unknown_0x0ece183c,
            unknown_0xab03dcb9,
            unknown_0xc0120b9e,
            unknown_0xf5230e61,
            unknown_0x70caf349,
            unknown_0x955a5177,
            unknown_0x95ed96c2,
            unknown_0x138b3979,
            unknown_0xdfa46325,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"KCPG")  # 0x4b435047
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4b435047))

        data.write(b"\x0e\xce\x18<")  # 0xece183c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0ece183c))

        data.write(b"\xab\x03\xdc\xb9")  # 0xab03dcb9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xab03dcb9))

        data.write(b"\xc0\x12\x0b\x9e")  # 0xc0120b9e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc0120b9e))

        data.write(b"\xf5#\x0ea")  # 0xf5230e61
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf5230e61))

        data.write(b"p\xca\xf3I")  # 0x70caf349
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x70caf349))

        data.write(b"\x95ZQw")  # 0x955a5177
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x955a5177))

        data.write(b"\x95\xed\x96\xc2")  # 0x95ed96c2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95ed96c2))

        data.write(b"\x13\x8b9y")  # 0x138b3979
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x138b3979.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdf\xa4c%")  # 0xdfa46325
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xdfa46325.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_UnknownStruct2Json", data)
        return cls(
            unknown_0x4b435047=json_data["unknown_0x4b435047"],
            unknown_0x0ece183c=json_data["unknown_0x0ece183c"],
            unknown_0xab03dcb9=json_data["unknown_0xab03dcb9"],
            unknown_0xc0120b9e=json_data["unknown_0xc0120b9e"],
            unknown_0xf5230e61=json_data["unknown_0xf5230e61"],
            unknown_0x70caf349=json_data["unknown_0x70caf349"],
            unknown_0x955a5177=json_data["unknown_0x955a5177"],
            unknown_0x95ed96c2=json_data["unknown_0x95ed96c2"],
            unknown_0x138b3979=Spline.from_json(json_data["unknown_0x138b3979"]),
            unknown_0xdfa46325=Spline.from_json(json_data["unknown_0xdfa46325"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x4b435047": self.unknown_0x4b435047,
            "unknown_0x0ece183c": self.unknown_0x0ece183c,
            "unknown_0xab03dcb9": self.unknown_0xab03dcb9,
            "unknown_0xc0120b9e": self.unknown_0xc0120b9e,
            "unknown_0xf5230e61": self.unknown_0xf5230e61,
            "unknown_0x70caf349": self.unknown_0x70caf349,
            "unknown_0x955a5177": self.unknown_0x955a5177,
            "unknown_0x95ed96c2": self.unknown_0x95ed96c2,
            "unknown_0x138b3979": self.unknown_0x138b3979.to_json(),
            "unknown_0xdfa46325": self.unknown_0xdfa46325.to_json(),
        }


def _decode_unknown_0x138b3979(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0xdfa46325(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4B435047: ("unknown_0x4b435047", structs.decode_BIG_f),
    0x0ECE183C: ("unknown_0x0ece183c", structs.decode_BIG_f),
    0xAB03DCB9: ("unknown_0xab03dcb9", structs.decode_BIG_f),
    0xC0120B9E: ("unknown_0xc0120b9e", structs.decode_BIG_f),
    0xF5230E61: ("unknown_0xf5230e61", structs.decode_BIG_f),
    0x70CAF349: ("unknown_0x70caf349", structs.decode_BIG_f),
    0x955A5177: ("unknown_0x955a5177", structs.decode_BIG_f),
    0x95ED96C2: ("unknown_0x95ed96c2", structs.decode_BIG_f),
    0x138B3979: ("unknown_0x138b3979", _decode_unknown_0x138b3979),
    0xDFA46325: ("unknown_0xdfa46325", _decode_unknown_0xdfa46325),
}
