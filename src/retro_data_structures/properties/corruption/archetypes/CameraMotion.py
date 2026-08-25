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

    class CameraMotionJson(typing_extensions.TypedDict):
        motion_type: json_util.JsonObject
        collision_type: int


@dataclasses.dataclass()
class CameraMotion(BaseProperty):
    motion_type: Convergence = dataclasses.field(
        default_factory=Convergence,
        metadata={
            "reflection": FieldReflection[Convergence](
                Convergence,
                id=0xC1547AF3,
                original_name="MotionType",
                from_json=Convergence.from_json,
                to_json=Convergence.to_json,
            ),
        },
    )
    collision_type: int = dataclasses.field(
        default=2969932169,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB674EA3D, original_name="CollisionType"),
        },
    )  # Choice

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
        if property_count != 2:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC1547AF3
        motion_type = Convergence.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB674EA3D
        collision_type = structs.BIG_L.unpack(data.read(4))[0]

        return cls(motion_type, collision_type)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x02")  # 2 properties

        data.write(b"\xc1Tz\xf3")  # 0xc1547af3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.motion_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb6t\xea=")  # 0xb674ea3d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.collision_type))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraMotionJson", data)
        return cls(
            motion_type=Convergence.from_json(json_data["motion_type"]),
            collision_type=json_data["collision_type"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "motion_type": self.motion_type.to_json(),
            "collision_type": self.collision_type,
        }


def _decode_motion_type(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC1547AF3: ("motion_type", _decode_motion_type),
    0xB674EA3D: ("collision_type", structs.decode_BIG_L),
}
