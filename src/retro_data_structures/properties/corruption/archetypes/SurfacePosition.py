# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.Convergence import Convergence
from retro_data_structures.properties.corruption.archetypes.OffsetInterpolant import OffsetInterpolant
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class SurfacePositionJson(typing_extensions.TypedDict):
        flags_surface_position: int
        player_offset: json_util.JsonObject
        convergence: json_util.JsonObject


@dataclasses.dataclass()
class SurfacePosition(BaseProperty):
    flags_surface_position: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9D99B2E3, original_name="FlagsSurfacePosition"),
        },
    )  # Flagset
    player_offset: OffsetInterpolant = dataclasses.field(
        default_factory=OffsetInterpolant,
        metadata={
            "reflection": FieldReflection[OffsetInterpolant](
                OffsetInterpolant,
                id=0xE69C51D7,
                original_name="PlayerOffset",
                from_json=OffsetInterpolant.from_json,
                to_json=OffsetInterpolant.to_json,
            ),
        },
    )
    convergence: Convergence = dataclasses.field(
        default_factory=Convergence,
        metadata={
            "reflection": FieldReflection[Convergence](
                Convergence,
                id=0x959108A5,
                original_name="Convergence",
                from_json=Convergence.from_json,
                to_json=Convergence.to_json,
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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D99B2E3
        flags_surface_position = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE69C51D7
        player_offset = OffsetInterpolant.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x959108A5
        convergence = Convergence.from_stream(data, game, property_size)

        return cls(flags_surface_position, player_offset, convergence)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\x9d\x99\xb2\xe3")  # 0x9d99b2e3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_surface_position))

        data.write(b"\xe6\x9cQ\xd7")  # 0xe69c51d7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.player_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95\x91\x08\xa5")  # 0x959108a5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.convergence.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SurfacePositionJson", data)
        return cls(
            flags_surface_position=json_data["flags_surface_position"],
            player_offset=OffsetInterpolant.from_json(json_data["player_offset"]),
            convergence=Convergence.from_json(json_data["convergence"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "flags_surface_position": self.flags_surface_position,
            "player_offset": self.player_offset.to_json(),
            "convergence": self.convergence.to_json(),
        }


def _decode_player_offset(data: typing.BinaryIO, game: Game, property_size: int) -> OffsetInterpolant:
    return OffsetInterpolant.from_stream(data, game, property_size)


def _decode_convergence(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x9D99B2E3: ("flags_surface_position", structs.decode_BIG_L),
    0xE69C51D7: ("player_offset", _decode_player_offset),
    0x959108A5: ("convergence", _decode_convergence),
}
