# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.UnknownStruct29 import UnknownStruct29
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class FederationDataJson(typing_extensions.TypedDict):
        can_blink: bool
        unknown_struct29: json_util.JsonObject
        unknown: bool


@dataclasses.dataclass()
class FederationData(BaseProperty):
    can_blink: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5C747710, original_name="CanBlink"),
        },
    )
    unknown_struct29: UnknownStruct29 = dataclasses.field(
        default_factory=UnknownStruct29,
        metadata={
            "reflection": FieldReflection[UnknownStruct29](
                UnknownStruct29,
                id=0x6E58D714,
                original_name="UnknownStruct29",
                from_json=UnknownStruct29.from_json,
                to_json=UnknownStruct29.to_json,
            ),
        },
    )
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0F31FDAE, original_name="Unknown"),
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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C747710
        can_blink = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E58D714
        unknown_struct29 = UnknownStruct29.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F31FDAE
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(can_blink, unknown_struct29, unknown)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\\tw\x10")  # 0x5c747710
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.can_blink))

        data.write(b"nX\xd7\x14")  # 0x6e58d714
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct29.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0f1\xfd\xae")  # 0xf31fdae
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FederationDataJson", data)
        return cls(
            can_blink=json_data["can_blink"],
            unknown_struct29=UnknownStruct29.from_json(json_data["unknown_struct29"]),
            unknown=json_data["unknown"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "can_blink": self.can_blink,
            "unknown_struct29": self.unknown_struct29.to_json(),
            "unknown": self.unknown,
        }


def _decode_unknown_struct29(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct29:
    return UnknownStruct29.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5C747710: ("can_blink", structs.decode_BIG_bool_),
    0x6E58D714: ("unknown_struct29", _decode_unknown_struct29),
    0x0F31FDAE: ("unknown", structs.decode_BIG_bool_),
}
