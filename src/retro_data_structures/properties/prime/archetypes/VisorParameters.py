# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class VisorParametersJson(typing_extensions.TypedDict):
        unknown: bool
        scan_through: bool
        visor_flags: int


class VisorFlags(enum.IntFlag):
    Combat = 1
    Scan = 2
    Thermal = 4
    XRay = 8

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


@dataclasses.dataclass()
class VisorParameters(BaseProperty):
    unknown: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="Unknown"),
        },
    )
    scan_through: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000001, original_name="ScanThrough"),
        },
    )
    visor_flags: VisorFlags = dataclasses.field(
        default=VisorFlags(0),
        metadata={
            "reflection": FieldReflection[VisorFlags](
                VisorFlags,
                id=0x00000002,
                original_name="VisorFlags",
                from_json=VisorFlags.from_json,
                to_json=VisorFlags.to_json,
            ),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
        scan_through = structs.BIG_bool_.unpack(data.read(1))[0]
        visor_flags = VisorFlags.from_stream(data, game)
        return cls(unknown, scan_through, visor_flags)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.unknown))
        data.write(structs.BIG_bool_.pack(self.scan_through))
        self.visor_flags.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VisorParametersJson", data)
        return cls(
            unknown=json_data["unknown"],
            scan_through=json_data["scan_through"],
            visor_flags=VisorFlags.from_json(json_data["visor_flags"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown": self.unknown,
            "scan_through": self.scan_through,
            "visor_flags": self.visor_flags.to_json(),
        }
