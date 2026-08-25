# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.CameraShakerEnvelope import CameraShakerEnvelope
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class CameraShakerDataJson(typing_extensions.TypedDict):
        flags_camera_shaker: int
        attenuation_distance: float
        duration: float
        audio_effect: int
        horizontal_motion: json_util.JsonObject
        vertical_motion: json_util.JsonObject
        forward_motion: json_util.JsonObject


@dataclasses.dataclass()
class CameraShakerData(BaseProperty):
    flags_camera_shaker: int = dataclasses.field(
        default=48,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC3E75C5F, original_name="FlagsCameraShaker"),
        },
    )  # Flagset
    attenuation_distance: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4D283AC5, original_name="AttenuationDistance"),
        },
    )
    duration: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
        },
    )
    audio_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC2ACB79E, original_name="AudioEffect"),
        },
    )
    horizontal_motion: CameraShakerEnvelope = dataclasses.field(
        default_factory=CameraShakerEnvelope,
        metadata={
            "reflection": FieldReflection[CameraShakerEnvelope](
                CameraShakerEnvelope,
                id=0xD9EB71E0,
                original_name="HorizontalMotion",
                from_json=CameraShakerEnvelope.from_json,
                to_json=CameraShakerEnvelope.to_json,
            ),
        },
    )
    vertical_motion: CameraShakerEnvelope = dataclasses.field(
        default_factory=CameraShakerEnvelope,
        metadata={
            "reflection": FieldReflection[CameraShakerEnvelope](
                CameraShakerEnvelope,
                id=0xC5B09632,
                original_name="VerticalMotion",
                from_json=CameraShakerEnvelope.from_json,
                to_json=CameraShakerEnvelope.to_json,
            ),
        },
    )
    forward_motion: CameraShakerEnvelope = dataclasses.field(
        default_factory=CameraShakerEnvelope,
        metadata={
            "reflection": FieldReflection[CameraShakerEnvelope](
                CameraShakerEnvelope,
                id=0x21B704E3,
                original_name="ForwardMotion",
                from_json=CameraShakerEnvelope.from_json,
                to_json=CameraShakerEnvelope.to_json,
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
        assert property_id == 0xC3E75C5F
        flags_camera_shaker = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D283AC5
        attenuation_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B51E23F
        duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2ACB79E
        audio_effect = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD9EB71E0
        horizontal_motion = CameraShakerEnvelope.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC5B09632
        vertical_motion = CameraShakerEnvelope.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21B704E3
        forward_motion = CameraShakerEnvelope.from_stream(data, game, property_size)

        return cls(
            flags_camera_shaker,
            attenuation_distance,
            duration,
            audio_effect,
            horizontal_motion,
            vertical_motion,
            forward_motion,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"\xc3\xe7\\_")  # 0xc3e75c5f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.flags_camera_shaker))

        data.write(b"M(:\xc5")  # 0x4d283ac5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.attenuation_distance))

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b"\xc2\xac\xb7\x9e")  # 0xc2acb79e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.audio_effect))

        data.write(b"\xd9\xebq\xe0")  # 0xd9eb71e0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.horizontal_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc5\xb0\x962")  # 0xc5b09632
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vertical_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"!\xb7\x04\xe3")  # 0x21b704e3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.forward_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraShakerDataJson", data)
        return cls(
            flags_camera_shaker=json_data["flags_camera_shaker"],
            attenuation_distance=json_data["attenuation_distance"],
            duration=json_data["duration"],
            audio_effect=json_data["audio_effect"],
            horizontal_motion=CameraShakerEnvelope.from_json(json_data["horizontal_motion"]),
            vertical_motion=CameraShakerEnvelope.from_json(json_data["vertical_motion"]),
            forward_motion=CameraShakerEnvelope.from_json(json_data["forward_motion"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "flags_camera_shaker": self.flags_camera_shaker,
            "attenuation_distance": self.attenuation_distance,
            "duration": self.duration,
            "audio_effect": self.audio_effect,
            "horizontal_motion": self.horizontal_motion.to_json(),
            "vertical_motion": self.vertical_motion.to_json(),
            "forward_motion": self.forward_motion.to_json(),
        }


def _decode_horizontal_motion(data: typing.BinaryIO, game: Game, property_size: int) -> CameraShakerEnvelope:
    return CameraShakerEnvelope.from_stream(data, game, property_size)


def _decode_vertical_motion(data: typing.BinaryIO, game: Game, property_size: int) -> CameraShakerEnvelope:
    return CameraShakerEnvelope.from_stream(data, game, property_size)


def _decode_forward_motion(data: typing.BinaryIO, game: Game, property_size: int) -> CameraShakerEnvelope:
    return CameraShakerEnvelope.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC3E75C5F: ("flags_camera_shaker", structs.decode_BIG_L),
    0x4D283AC5: ("attenuation_distance", structs.decode_BIG_f),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
    0xC2ACB79E: ("audio_effect", structs.decode_BIG_Q),
    0xD9EB71E0: ("horizontal_motion", _decode_horizontal_motion),
    0xC5B09632: ("vertical_motion", _decode_vertical_motion),
    0x21B704E3: ("forward_motion", _decode_forward_motion),
}
