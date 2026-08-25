# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.PuddleControlPhaseData import PuddleControlPhaseData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PuddleControlDataJson(typing_extensions.TypedDict):
        unknown: float
        bounding_box_scale: float
        puddle_control_phase_data_0xae0e60e2: json_util.JsonObject
        puddle_control_phase_data_0x1fd78dd3: json_util.JsonObject
        puddle_control_phase_data_0x5d4158a7: json_util.JsonObject
        puddle_control_phase_data_0xda4488bf: json_util.JsonObject
        puddle_control_phase_data_0x57b054de: json_util.JsonObject
        start_sound: int


@dataclasses.dataclass()
class PuddleControlData(BaseProperty):
    unknown: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0B3A08C9, original_name="Unknown"),
        },
    )
    bounding_box_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x14BFDEA6, original_name="BoundingBoxScale"),
        },
    )
    puddle_control_phase_data_0xae0e60e2: PuddleControlPhaseData = dataclasses.field(
        default_factory=PuddleControlPhaseData,
        metadata={
            "reflection": FieldReflection[PuddleControlPhaseData](
                PuddleControlPhaseData,
                id=0xAE0E60E2,
                original_name="PuddleControlPhaseData",
                from_json=PuddleControlPhaseData.from_json,
                to_json=PuddleControlPhaseData.to_json,
            ),
        },
    )
    puddle_control_phase_data_0x1fd78dd3: PuddleControlPhaseData = dataclasses.field(
        default_factory=PuddleControlPhaseData,
        metadata={
            "reflection": FieldReflection[PuddleControlPhaseData](
                PuddleControlPhaseData,
                id=0x1FD78DD3,
                original_name="PuddleControlPhaseData",
                from_json=PuddleControlPhaseData.from_json,
                to_json=PuddleControlPhaseData.to_json,
            ),
        },
    )
    puddle_control_phase_data_0x5d4158a7: PuddleControlPhaseData = dataclasses.field(
        default_factory=PuddleControlPhaseData,
        metadata={
            "reflection": FieldReflection[PuddleControlPhaseData](
                PuddleControlPhaseData,
                id=0x5D4158A7,
                original_name="PuddleControlPhaseData",
                from_json=PuddleControlPhaseData.from_json,
                to_json=PuddleControlPhaseData.to_json,
            ),
        },
    )
    puddle_control_phase_data_0xda4488bf: PuddleControlPhaseData = dataclasses.field(
        default_factory=PuddleControlPhaseData,
        metadata={
            "reflection": FieldReflection[PuddleControlPhaseData](
                PuddleControlPhaseData,
                id=0xDA4488BF,
                original_name="PuddleControlPhaseData",
                from_json=PuddleControlPhaseData.from_json,
                to_json=PuddleControlPhaseData.to_json,
            ),
        },
    )
    puddle_control_phase_data_0x57b054de: PuddleControlPhaseData = dataclasses.field(
        default_factory=PuddleControlPhaseData,
        metadata={
            "reflection": FieldReflection[PuddleControlPhaseData](
                PuddleControlPhaseData,
                id=0x57B054DE,
                original_name="PuddleControlPhaseData",
                from_json=PuddleControlPhaseData.from_json,
                to_json=PuddleControlPhaseData.to_json,
            ),
        },
    )
    start_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA8CC48B3, original_name="StartSound"),
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
        if property_count != 8:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0B3A08C9
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14BFDEA6
        bounding_box_scale = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE0E60E2
        puddle_control_phase_data_0xae0e60e2 = PuddleControlPhaseData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1FD78DD3
        puddle_control_phase_data_0x1fd78dd3 = PuddleControlPhaseData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D4158A7
        puddle_control_phase_data_0x5d4158a7 = PuddleControlPhaseData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDA4488BF
        puddle_control_phase_data_0xda4488bf = PuddleControlPhaseData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x57B054DE
        puddle_control_phase_data_0x57b054de = PuddleControlPhaseData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA8CC48B3
        start_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            unknown,
            bounding_box_scale,
            puddle_control_phase_data_0xae0e60e2,
            puddle_control_phase_data_0x1fd78dd3,
            puddle_control_phase_data_0x5d4158a7,
            puddle_control_phase_data_0xda4488bf,
            puddle_control_phase_data_0x57b054de,
            start_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\x0b:\x08\xc9")  # 0xb3a08c9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\x14\xbf\xde\xa6")  # 0x14bfdea6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.bounding_box_scale))

        data.write(b"\xae\x0e`\xe2")  # 0xae0e60e2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.puddle_control_phase_data_0xae0e60e2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1f\xd7\x8d\xd3")  # 0x1fd78dd3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.puddle_control_phase_data_0x1fd78dd3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"]AX\xa7")  # 0x5d4158a7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.puddle_control_phase_data_0x5d4158a7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdaD\x88\xbf")  # 0xda4488bf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.puddle_control_phase_data_0xda4488bf.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"W\xb0T\xde")  # 0x57b054de
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.puddle_control_phase_data_0x57b054de.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa8\xccH\xb3")  # 0xa8cc48b3
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.start_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PuddleControlDataJson", data)
        return cls(
            unknown=json_data["unknown"],
            bounding_box_scale=json_data["bounding_box_scale"],
            puddle_control_phase_data_0xae0e60e2=PuddleControlPhaseData.from_json(
                json_data["puddle_control_phase_data_0xae0e60e2"]
            ),
            puddle_control_phase_data_0x1fd78dd3=PuddleControlPhaseData.from_json(
                json_data["puddle_control_phase_data_0x1fd78dd3"]
            ),
            puddle_control_phase_data_0x5d4158a7=PuddleControlPhaseData.from_json(
                json_data["puddle_control_phase_data_0x5d4158a7"]
            ),
            puddle_control_phase_data_0xda4488bf=PuddleControlPhaseData.from_json(
                json_data["puddle_control_phase_data_0xda4488bf"]
            ),
            puddle_control_phase_data_0x57b054de=PuddleControlPhaseData.from_json(
                json_data["puddle_control_phase_data_0x57b054de"]
            ),
            start_sound=json_data["start_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown": self.unknown,
            "bounding_box_scale": self.bounding_box_scale,
            "puddle_control_phase_data_0xae0e60e2": self.puddle_control_phase_data_0xae0e60e2.to_json(),
            "puddle_control_phase_data_0x1fd78dd3": self.puddle_control_phase_data_0x1fd78dd3.to_json(),
            "puddle_control_phase_data_0x5d4158a7": self.puddle_control_phase_data_0x5d4158a7.to_json(),
            "puddle_control_phase_data_0xda4488bf": self.puddle_control_phase_data_0xda4488bf.to_json(),
            "puddle_control_phase_data_0x57b054de": self.puddle_control_phase_data_0x57b054de.to_json(),
            "start_sound": self.start_sound,
        }


def _decode_puddle_control_phase_data_0xae0e60e2(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_puddle_control_phase_data_0x1fd78dd3(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_puddle_control_phase_data_0x5d4158a7(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_puddle_control_phase_data_0xda4488bf(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


def _decode_puddle_control_phase_data_0x57b054de(
    data: typing.BinaryIO, game: Game, property_size: int
) -> PuddleControlPhaseData:
    return PuddleControlPhaseData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0B3A08C9: ("unknown", structs.decode_BIG_f),
    0x14BFDEA6: ("bounding_box_scale", structs.decode_BIG_f),
    0xAE0E60E2: ("puddle_control_phase_data_0xae0e60e2", _decode_puddle_control_phase_data_0xae0e60e2),
    0x1FD78DD3: ("puddle_control_phase_data_0x1fd78dd3", _decode_puddle_control_phase_data_0x1fd78dd3),
    0x5D4158A7: ("puddle_control_phase_data_0x5d4158a7", _decode_puddle_control_phase_data_0x5d4158a7),
    0xDA4488BF: ("puddle_control_phase_data_0xda4488bf", _decode_puddle_control_phase_data_0xda4488bf),
    0x57B054DE: ("puddle_control_phase_data_0x57b054de", _decode_puddle_control_phase_data_0x57b054de),
    0xA8CC48B3: ("start_sound", structs.decode_BIG_Q),
}
