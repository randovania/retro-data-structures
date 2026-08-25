# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.Convergence import Convergence
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ColliderPositionJson(typing_extensions.TypedDict):
        collider_position_type: int
        distance: float
        backwards_distance: float
        z_offset: float
        distance_convergence: json_util.JsonObject
        centroid_convergence: json_util.JsonObject
        camera_convergence: json_util.JsonObject


class ColliderPositionType(enum.IntEnum):
    Unknown1 = 3074795145

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
class ColliderPosition(BaseProperty):
    collider_position_type: ColliderPositionType = dataclasses.field(
        default=ColliderPositionType.Unknown1,
        metadata={
            "reflection": FieldReflection[ColliderPositionType](
                ColliderPositionType,
                id=0xE2AE470C,
                original_name="ColliderPositionType",
                from_json=ColliderPositionType.from_json,
                to_json=ColliderPositionType.to_json,
            ),
        },
    )
    distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3BF43BE, original_name="Distance"),
        },
    )
    backwards_distance: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7562BEE, original_name="BackwardsDistance"),
        },
    )
    z_offset: float = dataclasses.field(
        default=2.7360000610351562,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8033F9A3, original_name="ZOffset"),
        },
    )
    distance_convergence: Convergence = dataclasses.field(
        default_factory=Convergence,
        metadata={
            "reflection": FieldReflection[Convergence](
                Convergence,
                id=0xB11D9E90,
                original_name="DistanceConvergence",
                from_json=Convergence.from_json,
                to_json=Convergence.to_json,
            ),
        },
    )
    centroid_convergence: Convergence = dataclasses.field(
        default_factory=Convergence,
        metadata={
            "reflection": FieldReflection[Convergence](
                Convergence,
                id=0x81D49C61,
                original_name="CentroidConvergence",
                from_json=Convergence.from_json,
                to_json=Convergence.to_json,
            ),
        },
    )
    camera_convergence: Convergence = dataclasses.field(
        default_factory=Convergence,
        metadata={
            "reflection": FieldReflection[Convergence](
                Convergence,
                id=0x51B11F91,
                original_name="CameraConvergence",
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
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE2AE470C
        collider_position_type = ColliderPositionType.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3BF43BE
        distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7562BEE
        backwards_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8033F9A3
        z_offset = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB11D9E90
        distance_convergence = Convergence.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81D49C61
        centroid_convergence = Convergence.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51B11F91
        camera_convergence = Convergence.from_stream(data, game, property_size)

        return cls(
            collider_position_type,
            distance,
            backwards_distance,
            z_offset,
            distance_convergence,
            centroid_convergence,
            camera_convergence,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xe2\xaeG\x0c")  # 0xe2ae470c
        data.write(b"\x00\x04")  # size
        self.collider_position_type.to_stream(data, game)

        data.write(b"\xc3\xbfC\xbe")  # 0xc3bf43be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance))

        data.write(b"\xe7V+\xee")  # 0xe7562bee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.backwards_distance))

        data.write(b"\x803\xf9\xa3")  # 0x8033f9a3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.z_offset))

        data.write(b"\xb1\x1d\x9e\x90")  # 0xb11d9e90
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.distance_convergence.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x81\xd4\x9ca")  # 0x81d49c61
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.centroid_convergence.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Q\xb1\x1f\x91")  # 0x51b11f91
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera_convergence.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ColliderPositionJson", data)
        return cls(
            collider_position_type=ColliderPositionType.from_json(json_data["collider_position_type"]),
            distance=json_data["distance"],
            backwards_distance=json_data["backwards_distance"],
            z_offset=json_data["z_offset"],
            distance_convergence=Convergence.from_json(json_data["distance_convergence"]),
            centroid_convergence=Convergence.from_json(json_data["centroid_convergence"]),
            camera_convergence=Convergence.from_json(json_data["camera_convergence"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "collider_position_type": self.collider_position_type.to_json(),
            "distance": self.distance,
            "backwards_distance": self.backwards_distance,
            "z_offset": self.z_offset,
            "distance_convergence": self.distance_convergence.to_json(),
            "centroid_convergence": self.centroid_convergence.to_json(),
            "camera_convergence": self.camera_convergence.to_json(),
        }


def _decode_collider_position_type(data: typing.BinaryIO, game: Game, property_size: int) -> ColliderPositionType:
    return ColliderPositionType.from_stream(data, game)


def _decode_distance_convergence(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


def _decode_centroid_convergence(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


def _decode_camera_convergence(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xE2AE470C: ("collider_position_type", _decode_collider_position_type),
    0xC3BF43BE: ("distance", structs.decode_BIG_f),
    0xE7562BEE: ("backwards_distance", structs.decode_BIG_f),
    0x8033F9A3: ("z_offset", structs.decode_BIG_f),
    0xB11D9E90: ("distance_convergence", _decode_distance_convergence),
    0x81D49C61: ("centroid_convergence", _decode_centroid_convergence),
    0x51B11F91: ("camera_convergence", _decode_camera_convergence),
}
