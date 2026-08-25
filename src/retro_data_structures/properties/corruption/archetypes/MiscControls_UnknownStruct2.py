# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MiscControls_UnknownStruct2Json(typing_extensions.TypedDict):
        unknown_0x67739b75: int
        unknown_0xa5e20450: json_util.JsonObject
        unknown_0xa74987ff: json_util.JsonObject
        unknown_0x73eb9d04: json_util.JsonObject


@dataclasses.dataclass()
class MiscControls_UnknownStruct2(BaseProperty):
    unknown_0x67739b75: enums.MiscControls_UnknownEnum1Enum = dataclasses.field(
        default=enums.MiscControls_UnknownEnum1Enum.Unknown1,
        metadata={
            "reflection": FieldReflection[enums.MiscControls_UnknownEnum1Enum](
                enums.MiscControls_UnknownEnum1Enum,
                id=0x67739B75,
                original_name="Unknown",
                from_json=enums.MiscControls_UnknownEnum1Enum.from_json,
                to_json=enums.MiscControls_UnknownEnum1Enum.to_json,
            ),
        },
    )
    unknown_0xa5e20450: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xA5E20450,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0xa74987ff: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xA74987FF,
                original_name="Unknown",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    unknown_0x73eb9d04: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x73EB9D04,
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
        assert property_id == 0x67739B75
        unknown_0x67739b75 = enums.MiscControls_UnknownEnum1Enum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA5E20450
        unknown_0xa5e20450 = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA74987FF
        unknown_0xa74987ff = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73EB9D04
        unknown_0x73eb9d04 = RevolutionControl.from_stream(data, game, property_size)

        return cls(unknown_0x67739b75, unknown_0xa5e20450, unknown_0xa74987ff, unknown_0x73eb9d04)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"gs\x9bu")  # 0x67739b75
        data.write(b"\x00\x04")  # size
        self.unknown_0x67739b75.to_stream(data, game)

        data.write(b"\xa5\xe2\x04P")  # 0xa5e20450
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xa5e20450.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa7I\x87\xff")  # 0xa74987ff
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xa74987ff.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"s\xeb\x9d\x04")  # 0x73eb9d04
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x73eb9d04.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MiscControls_UnknownStruct2Json", data)
        return cls(
            unknown_0x67739b75=enums.MiscControls_UnknownEnum1Enum.from_json(json_data["unknown_0x67739b75"]),
            unknown_0xa5e20450=RevolutionControl.from_json(json_data["unknown_0xa5e20450"]),
            unknown_0xa74987ff=RevolutionControl.from_json(json_data["unknown_0xa74987ff"]),
            unknown_0x73eb9d04=RevolutionControl.from_json(json_data["unknown_0x73eb9d04"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x67739b75": self.unknown_0x67739b75.to_json(),
            "unknown_0xa5e20450": self.unknown_0xa5e20450.to_json(),
            "unknown_0xa74987ff": self.unknown_0xa74987ff.to_json(),
            "unknown_0x73eb9d04": self.unknown_0x73eb9d04.to_json(),
        }


def _decode_unknown_0x67739b75(
    data: typing.BinaryIO, game: Game, property_size: int
) -> enums.MiscControls_UnknownEnum1Enum:
    return enums.MiscControls_UnknownEnum1Enum.from_stream(data, game)


def _decode_unknown_0xa5e20450(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0xa74987ff(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_unknown_0x73eb9d04(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x67739B75: ("unknown_0x67739b75", _decode_unknown_0x67739b75),
    0xA5E20450: ("unknown_0xa5e20450", _decode_unknown_0xa5e20450),
    0xA74987FF: ("unknown_0xa74987ff", _decode_unknown_0xa74987ff),
    0x73EB9D04: ("unknown_0x73eb9d04", _decode_unknown_0x73eb9d04),
}
