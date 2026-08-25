# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class AudioPlaybackParmsJson(typing_extensions.TypedDict):
        maximum_distance: float
        fall_off: float
        sound_id: int
        max_volume: int
        min_volume: int
        use_room_acoustics: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xE449F72, 0x72531867, 0xAF85A374, 0xC712847C, 0x57619496, 0x85707354)


@dataclasses.dataclass()
class AudioPlaybackParms(BaseProperty):
    maximum_distance: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0E449F72, original_name="MaximumDistance"),
        },
    )
    fall_off: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72531867, original_name="FallOff"),
        },
    )
    sound_id: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xAF85A374, original_name="Sound_Id"),
        },
    )
    max_volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC712847C, original_name="MaxVolume"),
        },
    )
    min_volume: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x57619496, original_name="MinVolume"),
        },
    )
    use_room_acoustics: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x85707354, original_name="UseRoomAcoustics"),
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
        if property_count != 6:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHlLHlLHlLH?")

        dec = _FAST_FORMAT.unpack(data.read(57))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"\x0eD\x9fr")  # 0xe449f72
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.maximum_distance))

        data.write(b"rS\x18g")  # 0x72531867
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fall_off))

        data.write(b"\xaf\x85\xa3t")  # 0xaf85a374
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound_id))

        data.write(b"\xc7\x12\x84|")  # 0xc712847c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.max_volume))

        data.write(b"Wa\x94\x96")  # 0x57619496
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.min_volume))

        data.write(b"\x85psT")  # 0x85707354
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_room_acoustics))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AudioPlaybackParmsJson", data)
        return cls(
            maximum_distance=json_data["maximum_distance"],
            fall_off=json_data["fall_off"],
            sound_id=json_data["sound_id"],
            max_volume=json_data["max_volume"],
            min_volume=json_data["min_volume"],
            use_room_acoustics=json_data["use_room_acoustics"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "maximum_distance": self.maximum_distance,
            "fall_off": self.fall_off,
            "sound_id": self.sound_id,
            "max_volume": self.max_volume,
            "min_volume": self.min_volume,
            "use_room_acoustics": self.use_room_acoustics,
        }

    def _dependencies_for_sound_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_sound_id(asset_manager)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0E449F72: ("maximum_distance", structs.decode_BIG_f),
    0x72531867: ("fall_off", structs.decode_BIG_f),
    0xAF85A374: ("sound_id", structs.decode_BIG_l),
    0xC712847C: ("max_volume", structs.decode_BIG_l),
    0x57619496: ("min_volume", structs.decode_BIG_l),
    0x85707354: ("use_room_acoustics", structs.decode_BIG_bool_),
}
