# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct36Json(typing_extensions.TypedDict):
        audio_playback_parms_0x4f904909: json_util.JsonObject
        audio_playback_parms_0x82e108de: json_util.JsonObject
        audio_playback_parms_0xdf090545: json_util.JsonObject
        audio_playback_parms_0x3dd5b3cf: json_util.JsonObject
        audio_playback_parms_0xf82231bb: json_util.JsonObject
        audio_playback_parms_0x009e3658: json_util.JsonObject
        audio_playback_parms_0x62bd75b1: json_util.JsonObject
        unknown: float
        audio_playback_parms_0x32969cba: json_util.JsonObject
        audio_playback_parms_0x597d2ac9: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct36(BaseProperty):
    audio_playback_parms_0x4f904909: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x4F904909,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x82e108de: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x82E108DE,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0xdf090545: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xDF090545,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x3dd5b3cf: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x3DD5B3CF,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0xf82231bb: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xF82231BB,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x009e3658: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x009E3658,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x62bd75b1: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x62BD75B1,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7714BAEC, original_name="Unknown"),
        },
    )
    audio_playback_parms_0x32969cba: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x32969CBA,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x597d2ac9: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x597D2AC9,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F904909
        audio_playback_parms_0x4f904909 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82E108DE
        audio_playback_parms_0x82e108de = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDF090545
        audio_playback_parms_0xdf090545 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3DD5B3CF
        audio_playback_parms_0x3dd5b3cf = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF82231BB
        audio_playback_parms_0xf82231bb = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x009E3658
        audio_playback_parms_0x009e3658 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62BD75B1
        audio_playback_parms_0x62bd75b1 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7714BAEC
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32969CBA
        audio_playback_parms_0x32969cba = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x597D2AC9
        audio_playback_parms_0x597d2ac9 = AudioPlaybackParms.from_stream(data, game, property_size)

        return cls(
            audio_playback_parms_0x4f904909,
            audio_playback_parms_0x82e108de,
            audio_playback_parms_0xdf090545,
            audio_playback_parms_0x3dd5b3cf,
            audio_playback_parms_0xf82231bb,
            audio_playback_parms_0x009e3658,
            audio_playback_parms_0x62bd75b1,
            unknown,
            audio_playback_parms_0x32969cba,
            audio_playback_parms_0x597d2ac9,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"O\x90I\t")  # 0x4f904909
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x4f904909.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x82\xe1\x08\xde")  # 0x82e108de
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x82e108de.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdf\t\x05E")  # 0xdf090545
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0xdf090545.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"=\xd5\xb3\xcf")  # 0x3dd5b3cf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x3dd5b3cf.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf8"1\xbb')  # 0xf82231bb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0xf82231bb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\x9e6X")  # 0x9e3658
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x009e3658.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"b\xbdu\xb1")  # 0x62bd75b1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x62bd75b1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\x14\xba\xec")  # 0x7714baec
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"2\x96\x9c\xba")  # 0x32969cba
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x32969cba.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Y}*\xc9")  # 0x597d2ac9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x597d2ac9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct36Json", data)
        return cls(
            audio_playback_parms_0x4f904909=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x4f904909"]),
            audio_playback_parms_0x82e108de=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x82e108de"]),
            audio_playback_parms_0xdf090545=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0xdf090545"]),
            audio_playback_parms_0x3dd5b3cf=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x3dd5b3cf"]),
            audio_playback_parms_0xf82231bb=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0xf82231bb"]),
            audio_playback_parms_0x009e3658=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x009e3658"]),
            audio_playback_parms_0x62bd75b1=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x62bd75b1"]),
            unknown=json_data["unknown"],
            audio_playback_parms_0x32969cba=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x32969cba"]),
            audio_playback_parms_0x597d2ac9=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x597d2ac9"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "audio_playback_parms_0x4f904909": self.audio_playback_parms_0x4f904909.to_json(),
            "audio_playback_parms_0x82e108de": self.audio_playback_parms_0x82e108de.to_json(),
            "audio_playback_parms_0xdf090545": self.audio_playback_parms_0xdf090545.to_json(),
            "audio_playback_parms_0x3dd5b3cf": self.audio_playback_parms_0x3dd5b3cf.to_json(),
            "audio_playback_parms_0xf82231bb": self.audio_playback_parms_0xf82231bb.to_json(),
            "audio_playback_parms_0x009e3658": self.audio_playback_parms_0x009e3658.to_json(),
            "audio_playback_parms_0x62bd75b1": self.audio_playback_parms_0x62bd75b1.to_json(),
            "unknown": self.unknown,
            "audio_playback_parms_0x32969cba": self.audio_playback_parms_0x32969cba.to_json(),
            "audio_playback_parms_0x597d2ac9": self.audio_playback_parms_0x597d2ac9.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (
                self.audio_playback_parms_0x4f904909.dependencies_for,
                "audio_playback_parms_0x4f904909",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x82e108de.dependencies_for,
                "audio_playback_parms_0x82e108de",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0xdf090545.dependencies_for,
                "audio_playback_parms_0xdf090545",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x3dd5b3cf.dependencies_for,
                "audio_playback_parms_0x3dd5b3cf",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0xf82231bb.dependencies_for,
                "audio_playback_parms_0xf82231bb",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x009e3658.dependencies_for,
                "audio_playback_parms_0x009e3658",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x62bd75b1.dependencies_for,
                "audio_playback_parms_0x62bd75b1",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x32969cba.dependencies_for,
                "audio_playback_parms_0x32969cba",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x597d2ac9.dependencies_for,
                "audio_playback_parms_0x597d2ac9",
                "AudioPlaybackParms",
            ),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct36.{field_name} ({field_type}): {e}")


def _decode_audio_playback_parms_0x4f904909(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x82e108de(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0xdf090545(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x3dd5b3cf(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0xf82231bb(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x009e3658(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x62bd75b1(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x32969cba(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x597d2ac9(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4F904909: ("audio_playback_parms_0x4f904909", _decode_audio_playback_parms_0x4f904909),
    0x82E108DE: ("audio_playback_parms_0x82e108de", _decode_audio_playback_parms_0x82e108de),
    0xDF090545: ("audio_playback_parms_0xdf090545", _decode_audio_playback_parms_0xdf090545),
    0x3DD5B3CF: ("audio_playback_parms_0x3dd5b3cf", _decode_audio_playback_parms_0x3dd5b3cf),
    0xF82231BB: ("audio_playback_parms_0xf82231bb", _decode_audio_playback_parms_0xf82231bb),
    0x009E3658: ("audio_playback_parms_0x009e3658", _decode_audio_playback_parms_0x009e3658),
    0x62BD75B1: ("audio_playback_parms_0x62bd75b1", _decode_audio_playback_parms_0x62bd75b1),
    0x7714BAEC: ("unknown", structs.decode_BIG_f),
    0x32969CBA: ("audio_playback_parms_0x32969cba", _decode_audio_playback_parms_0x32969cba),
    0x597D2AC9: ("audio_playback_parms_0x597d2ac9", _decode_audio_playback_parms_0x597d2ac9),
}
