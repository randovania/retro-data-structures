# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.Convergence import Convergence
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ChasePositionJson(typing_extensions.TypedDict):
        angle: float
        distance: float
        z_offset: float
        angular_convergence: json_util.JsonObject


@dataclasses.dataclass()
class ChasePosition(BaseProperty):
    angle: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x382A1973, original_name="Angle"),
        },
    )
    distance: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3BF43BE, original_name="Distance"),
        },
    )
    z_offset: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8033F9A3, original_name="ZOffset"),
        },
    )
    angular_convergence: Convergence = dataclasses.field(
        default_factory=Convergence,
        metadata={
            "reflection": FieldReflection[Convergence](
                Convergence,
                id=0x69114952,
                original_name="AngularConvergence",
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
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x382A1973
        angle = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3BF43BE
        distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8033F9A3
        z_offset = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69114952
        angular_convergence = Convergence.from_stream(data, game, property_size)

        return cls(angle, distance, z_offset, angular_convergence)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"8*\x19s")  # 0x382a1973
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.angle))

        data.write(b"\xc3\xbfC\xbe")  # 0xc3bf43be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance))

        data.write(b"\x803\xf9\xa3")  # 0x8033f9a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.z_offset))

        data.write(b"i\x11IR")  # 0x69114952
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.angular_convergence.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ChasePositionJson", data)
        return cls(
            angle=json_data["angle"],
            distance=json_data["distance"],
            z_offset=json_data["z_offset"],
            angular_convergence=Convergence.from_json(json_data["angular_convergence"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "angle": self.angle,
            "distance": self.distance,
            "z_offset": self.z_offset,
            "angular_convergence": self.angular_convergence.to_json(),
        }


def _decode_angular_convergence(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x382A1973: ("angle", structs.decode_BIG_f),
    0xC3BF43BE: ("distance", structs.decode_BIG_f),
    0x8033F9A3: ("z_offset", structs.decode_BIG_f),
    0x69114952: ("angular_convergence", _decode_angular_convergence),
}
