# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct14Json(typing_extensions.TypedDict):
        unknown_0xa0d037ee: float
        unknown_0x4f522994: float
        shadow_dash_speed: float
        unknown_0x5d02f384: float
        part: int
        audio_playback_parms: json_util.JsonObject
        sound_cloak: json_util.JsonObject
        sound_de_cloak: json_util.JsonObject
        shadow_decoy_vulnerability: json_util.JsonObject
        shadow_dash_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct14(BaseProperty):
    unknown_0xa0d037ee: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA0D037EE, original_name="Unknown"),
        },
    )
    unknown_0x4f522994: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4F522994, original_name="Unknown"),
        },
    )
    shadow_dash_speed: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x87461CC6, original_name="ShadowDashSpeed"),
        },
    )
    unknown_0x5d02f384: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5D02F384, original_name="Unknown"),
        },
    )
    part: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2DC80B4B, original_name="PART"),
        },
    )
    audio_playback_parms: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x03392283,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_cloak: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x9DEDCFF1,
                original_name="Sound_Cloak",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_de_cloak: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xF740E01D,
                original_name="Sound_DeCloak",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    shadow_decoy_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xB2F64BB4,
                original_name="ShadowDecoyVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    shadow_dash_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xED067447,
                original_name="ShadowDashVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
        assert property_id == 0xA0D037EE
        unknown_0xa0d037ee = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F522994
        unknown_0x4f522994 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87461CC6
        shadow_dash_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D02F384
        unknown_0x5d02f384 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DC80B4B
        part = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03392283
        audio_playback_parms = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9DEDCFF1
        sound_cloak = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF740E01D
        sound_de_cloak = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2F64BB4
        shadow_decoy_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED067447
        shadow_dash_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            unknown_0xa0d037ee,
            unknown_0x4f522994,
            shadow_dash_speed,
            unknown_0x5d02f384,
            part,
            audio_playback_parms,
            sound_cloak,
            sound_de_cloak,
            shadow_decoy_vulnerability,
            shadow_dash_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\xa0\xd07\xee")  # 0xa0d037ee
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa0d037ee))

        data.write(b"OR)\x94")  # 0x4f522994
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f522994))

        data.write(b"\x87F\x1c\xc6")  # 0x87461cc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_dash_speed))

        data.write(b"]\x02\xf3\x84")  # 0x5d02f384
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5d02f384))

        data.write(b"-\xc8\x0bK")  # 0x2dc80b4b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b'\x039"\x83')  # 0x3392283
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9d\xed\xcf\xf1")  # 0x9dedcff1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_cloak.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf7@\xe0\x1d")  # 0xf740e01d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_de_cloak.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb2\xf6K\xb4")  # 0xb2f64bb4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shadow_decoy_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xed\x06tG")  # 0xed067447
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shadow_dash_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct14Json", data)
        return cls(
            unknown_0xa0d037ee=json_data["unknown_0xa0d037ee"],
            unknown_0x4f522994=json_data["unknown_0x4f522994"],
            shadow_dash_speed=json_data["shadow_dash_speed"],
            unknown_0x5d02f384=json_data["unknown_0x5d02f384"],
            part=json_data["part"],
            audio_playback_parms=AudioPlaybackParms.from_json(json_data["audio_playback_parms"]),
            sound_cloak=AudioPlaybackParms.from_json(json_data["sound_cloak"]),
            sound_de_cloak=AudioPlaybackParms.from_json(json_data["sound_de_cloak"]),
            shadow_decoy_vulnerability=DamageVulnerability.from_json(json_data["shadow_decoy_vulnerability"]),
            shadow_dash_vulnerability=DamageVulnerability.from_json(json_data["shadow_dash_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xa0d037ee": self.unknown_0xa0d037ee,
            "unknown_0x4f522994": self.unknown_0x4f522994,
            "shadow_dash_speed": self.shadow_dash_speed,
            "unknown_0x5d02f384": self.unknown_0x5d02f384,
            "part": self.part,
            "audio_playback_parms": self.audio_playback_parms.to_json(),
            "sound_cloak": self.sound_cloak.to_json(),
            "sound_de_cloak": self.sound_de_cloak.to_json(),
            "shadow_decoy_vulnerability": self.shadow_decoy_vulnerability.to_json(),
            "shadow_dash_vulnerability": self.shadow_dash_vulnerability.to_json(),
        }

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_part, "part", "AssetId"),
            (self.audio_playback_parms.dependencies_for, "audio_playback_parms", "AudioPlaybackParms"),
            (self.sound_cloak.dependencies_for, "sound_cloak", "AudioPlaybackParms"),
            (self.sound_de_cloak.dependencies_for, "sound_de_cloak", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct14.{field_name} ({field_type}): {e}")


def _decode_audio_playback_parms(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_cloak(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_de_cloak(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_shadow_decoy_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_shadow_dash_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA0D037EE: ("unknown_0xa0d037ee", structs.decode_BIG_f),
    0x4F522994: ("unknown_0x4f522994", structs.decode_BIG_f),
    0x87461CC6: ("shadow_dash_speed", structs.decode_BIG_f),
    0x5D02F384: ("unknown_0x5d02f384", structs.decode_BIG_f),
    0x2DC80B4B: ("part", structs.decode_BIG_L),
    0x03392283: ("audio_playback_parms", _decode_audio_playback_parms),
    0x9DEDCFF1: ("sound_cloak", _decode_sound_cloak),
    0xF740E01D: ("sound_de_cloak", _decode_sound_de_cloak),
    0xB2F64BB4: ("shadow_decoy_vulnerability", _decode_shadow_decoy_vulnerability),
    0xED067447: ("shadow_dash_vulnerability", _decode_shadow_dash_vulnerability),
}
