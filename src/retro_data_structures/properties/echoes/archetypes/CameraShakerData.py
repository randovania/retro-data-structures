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
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class CameraShakerDataJson(typing_extensions.TypedDict):
        flags_camera_shaker: int
        attenuation_distance: float
        horizontal_motion: json_util.JsonObject
        vertical_motion: json_util.JsonObject
        forward_motion: json_util.JsonObject
        duration: float
        audio_effect: int


@dataclasses.dataclass()
class CameraShakerData(BaseProperty):
    flags_camera_shaker: int = dataclasses.field(
        default=16,
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
    horizontal_motion: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0xF122CD97,
                original_name="HorizontalMotion",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    vertical_motion: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline,
                id=0x2927E544,
                original_name="VerticalMotion",
                from_json=Spline.from_json,
                to_json=Spline.to_json,
            ),
        },
    )
    forward_motion: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x7CFA4678, original_name="ForwardMotion", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    duration: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8B51E23F, original_name="Duration"),
        },
    )
    audio_effect: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x388D2E46, original_name="AudioEffect"),
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
        assert property_id == 0xF122CD97
        horizontal_motion = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2927E544
        vertical_motion = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7CFA4678
        forward_motion = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B51E23F
        duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388D2E46
        audio_effect = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            flags_camera_shaker,
            attenuation_distance,
            horizontal_motion,
            vertical_motion,
            forward_motion,
            duration,
            audio_effect,
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

        data.write(b'\xf1"\xcd\x97')  # 0xf122cd97
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.horizontal_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")'\xe5D")  # 0x2927e544
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.vertical_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"|\xfaFx")  # 0x7cfa4678
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.forward_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8bQ\xe2?")  # 0x8b51e23f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b"8\x8d.F")  # 0x388d2e46
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.audio_effect))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraShakerDataJson", data)
        return cls(
            flags_camera_shaker=json_data["flags_camera_shaker"],
            attenuation_distance=json_data["attenuation_distance"],
            horizontal_motion=Spline.from_json(json_data["horizontal_motion"]),
            vertical_motion=Spline.from_json(json_data["vertical_motion"]),
            forward_motion=Spline.from_json(json_data["forward_motion"]),
            duration=json_data["duration"],
            audio_effect=json_data["audio_effect"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "flags_camera_shaker": self.flags_camera_shaker,
            "attenuation_distance": self.attenuation_distance,
            "horizontal_motion": self.horizontal_motion.to_json(),
            "vertical_motion": self.vertical_motion.to_json(),
            "forward_motion": self.forward_motion.to_json(),
            "duration": self.duration,
            "audio_effect": self.audio_effect,
        }

    def _dependencies_for_audio_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.audio_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_audio_effect(asset_manager)


def _decode_horizontal_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_vertical_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_forward_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC3E75C5F: ("flags_camera_shaker", structs.decode_BIG_L),
    0x4D283AC5: ("attenuation_distance", structs.decode_BIG_f),
    0xF122CD97: ("horizontal_motion", _decode_horizontal_motion),
    0x2927E544: ("vertical_motion", _decode_vertical_motion),
    0x7CFA4678: ("forward_motion", _decode_forward_motion),
    0x8B51E23F: ("duration", structs.decode_BIG_f),
    0x388D2E46: ("audio_effect", structs.decode_BIG_l),
}
