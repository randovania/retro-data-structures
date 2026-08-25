# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.IngSpiderballGuardianStruct import IngSpiderballGuardianStruct
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct31Json(typing_extensions.TypedDict):
        ing_spiderball_guardian_struct_0x152db484: json_util.JsonObject
        ing_spiderball_guardian_struct_0x2d163ff7: json_util.JsonObject
        ing_spiderball_guardian_struct_0x8c2fbb19: json_util.JsonObject
        ing_spiderball_guardian_struct_0x5d612911: json_util.JsonObject
        ing_spiderball_guardian_struct_0xfc58adff: json_util.JsonObject
        ing_spiderball_guardian_struct_0xc463268c: json_util.JsonObject
        damage_radius: float
        proximity_damage: json_util.JsonObject
        unknown: float
        audio_playback_parms_0xaed23abc: json_util.JsonObject
        sound_spiderball_rolling: json_util.JsonObject
        audio_playback_parms_0xcee38f10: json_util.JsonObject
        audio_playback_parms_0x796fa303: json_util.JsonObject
        sound_enter_stunned: json_util.JsonObject
        audio_playback_parms_0x44c1f241: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct31(BaseProperty):
    ing_spiderball_guardian_struct_0x152db484: IngSpiderballGuardianStruct = dataclasses.field(
        default_factory=IngSpiderballGuardianStruct,
        metadata={
            "reflection": FieldReflection[IngSpiderballGuardianStruct](
                IngSpiderballGuardianStruct,
                id=0x152DB484,
                original_name="IngSpiderballGuardianStruct",
                from_json=IngSpiderballGuardianStruct.from_json,
                to_json=IngSpiderballGuardianStruct.to_json,
            ),
        },
    )
    ing_spiderball_guardian_struct_0x2d163ff7: IngSpiderballGuardianStruct = dataclasses.field(
        default_factory=IngSpiderballGuardianStruct,
        metadata={
            "reflection": FieldReflection[IngSpiderballGuardianStruct](
                IngSpiderballGuardianStruct,
                id=0x2D163FF7,
                original_name="IngSpiderballGuardianStruct",
                from_json=IngSpiderballGuardianStruct.from_json,
                to_json=IngSpiderballGuardianStruct.to_json,
            ),
        },
    )
    ing_spiderball_guardian_struct_0x8c2fbb19: IngSpiderballGuardianStruct = dataclasses.field(
        default_factory=IngSpiderballGuardianStruct,
        metadata={
            "reflection": FieldReflection[IngSpiderballGuardianStruct](
                IngSpiderballGuardianStruct,
                id=0x8C2FBB19,
                original_name="IngSpiderballGuardianStruct",
                from_json=IngSpiderballGuardianStruct.from_json,
                to_json=IngSpiderballGuardianStruct.to_json,
            ),
        },
    )
    ing_spiderball_guardian_struct_0x5d612911: IngSpiderballGuardianStruct = dataclasses.field(
        default_factory=IngSpiderballGuardianStruct,
        metadata={
            "reflection": FieldReflection[IngSpiderballGuardianStruct](
                IngSpiderballGuardianStruct,
                id=0x5D612911,
                original_name="IngSpiderballGuardianStruct",
                from_json=IngSpiderballGuardianStruct.from_json,
                to_json=IngSpiderballGuardianStruct.to_json,
            ),
        },
    )
    ing_spiderball_guardian_struct_0xfc58adff: IngSpiderballGuardianStruct = dataclasses.field(
        default_factory=IngSpiderballGuardianStruct,
        metadata={
            "reflection": FieldReflection[IngSpiderballGuardianStruct](
                IngSpiderballGuardianStruct,
                id=0xFC58ADFF,
                original_name="IngSpiderballGuardianStruct",
                from_json=IngSpiderballGuardianStruct.from_json,
                to_json=IngSpiderballGuardianStruct.to_json,
            ),
        },
    )
    ing_spiderball_guardian_struct_0xc463268c: IngSpiderballGuardianStruct = dataclasses.field(
        default_factory=IngSpiderballGuardianStruct,
        metadata={
            "reflection": FieldReflection[IngSpiderballGuardianStruct](
                IngSpiderballGuardianStruct,
                id=0xC463268C,
                original_name="IngSpiderballGuardianStruct",
                from_json=IngSpiderballGuardianStruct.from_json,
                to_json=IngSpiderballGuardianStruct.to_json,
            ),
        },
    )
    damage_radius: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0F598739, original_name="DamageRadius"),
        },
    )
    proximity_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xBA78D281,
                original_name="ProximityDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x32133B39, original_name="Unknown"),
        },
    )
    audio_playback_parms_0xaed23abc: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xAED23ABC,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_spiderball_rolling: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x3A5E2F52,
                original_name="Sound_SpiderballRolling",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0xcee38f10: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xCEE38F10,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x796fa303: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x796FA303,
                original_name="AudioPlaybackParms",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_enter_stunned: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xD5F3E9C4,
                original_name="Sound_EnterStunned",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    audio_playback_parms_0x44c1f241: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x44C1F241,
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
        if property_count != 15:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x152DB484
        ing_spiderball_guardian_struct_0x152db484 = IngSpiderballGuardianStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D163FF7
        ing_spiderball_guardian_struct_0x2d163ff7 = IngSpiderballGuardianStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8C2FBB19
        ing_spiderball_guardian_struct_0x8c2fbb19 = IngSpiderballGuardianStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5D612911
        ing_spiderball_guardian_struct_0x5d612911 = IngSpiderballGuardianStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFC58ADFF
        ing_spiderball_guardian_struct_0xfc58adff = IngSpiderballGuardianStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC463268C
        ing_spiderball_guardian_struct_0xc463268c = IngSpiderballGuardianStruct.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F598739
        damage_radius = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA78D281
        proximity_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 40.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32133B39
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAED23ABC
        audio_playback_parms_0xaed23abc = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A5E2F52
        sound_spiderball_rolling = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEE38F10
        audio_playback_parms_0xcee38f10 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x796FA303
        audio_playback_parms_0x796fa303 = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5F3E9C4
        sound_enter_stunned = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44C1F241
        audio_playback_parms_0x44c1f241 = AudioPlaybackParms.from_stream(data, game, property_size)

        return cls(
            ing_spiderball_guardian_struct_0x152db484,
            ing_spiderball_guardian_struct_0x2d163ff7,
            ing_spiderball_guardian_struct_0x8c2fbb19,
            ing_spiderball_guardian_struct_0x5d612911,
            ing_spiderball_guardian_struct_0xfc58adff,
            ing_spiderball_guardian_struct_0xc463268c,
            damage_radius,
            proximity_damage,
            unknown,
            audio_playback_parms_0xaed23abc,
            sound_spiderball_rolling,
            audio_playback_parms_0xcee38f10,
            audio_playback_parms_0x796fa303,
            sound_enter_stunned,
            audio_playback_parms_0x44c1f241,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\x15-\xb4\x84")  # 0x152db484
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_spiderball_guardian_struct_0x152db484.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"-\x16?\xf7")  # 0x2d163ff7
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_spiderball_guardian_struct_0x2d163ff7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8c/\xbb\x19")  # 0x8c2fbb19
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_spiderball_guardian_struct_0x8c2fbb19.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"]a)\x11")  # 0x5d612911
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_spiderball_guardian_struct_0x5d612911.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfcX\xad\xff")  # 0xfc58adff
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_spiderball_guardian_struct_0xfc58adff.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc4c&\x8c")  # 0xc463268c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_spiderball_guardian_struct_0xc463268c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0fY\x879")  # 0xf598739
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.damage_radius))

        data.write(b"\xbax\xd2\x81")  # 0xba78d281
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.proximity_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 40.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"2\x13;9")  # 0x32133b39
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xae\xd2:\xbc")  # 0xaed23abc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0xaed23abc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b":^/R")  # 0x3a5e2f52
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_spiderball_rolling.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xce\xe3\x8f\x10")  # 0xcee38f10
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0xcee38f10.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"yo\xa3\x03")  # 0x796fa303
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x796fa303.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd5\xf3\xe9\xc4")  # 0xd5f3e9c4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_enter_stunned.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"D\xc1\xf2A")  # 0x44c1f241
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.audio_playback_parms_0x44c1f241.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct31Json", data)
        return cls(
            ing_spiderball_guardian_struct_0x152db484=IngSpiderballGuardianStruct.from_json(
                json_data["ing_spiderball_guardian_struct_0x152db484"]
            ),
            ing_spiderball_guardian_struct_0x2d163ff7=IngSpiderballGuardianStruct.from_json(
                json_data["ing_spiderball_guardian_struct_0x2d163ff7"]
            ),
            ing_spiderball_guardian_struct_0x8c2fbb19=IngSpiderballGuardianStruct.from_json(
                json_data["ing_spiderball_guardian_struct_0x8c2fbb19"]
            ),
            ing_spiderball_guardian_struct_0x5d612911=IngSpiderballGuardianStruct.from_json(
                json_data["ing_spiderball_guardian_struct_0x5d612911"]
            ),
            ing_spiderball_guardian_struct_0xfc58adff=IngSpiderballGuardianStruct.from_json(
                json_data["ing_spiderball_guardian_struct_0xfc58adff"]
            ),
            ing_spiderball_guardian_struct_0xc463268c=IngSpiderballGuardianStruct.from_json(
                json_data["ing_spiderball_guardian_struct_0xc463268c"]
            ),
            damage_radius=json_data["damage_radius"],
            proximity_damage=DamageInfo.from_json(json_data["proximity_damage"]),
            unknown=json_data["unknown"],
            audio_playback_parms_0xaed23abc=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0xaed23abc"]),
            sound_spiderball_rolling=AudioPlaybackParms.from_json(json_data["sound_spiderball_rolling"]),
            audio_playback_parms_0xcee38f10=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0xcee38f10"]),
            audio_playback_parms_0x796fa303=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x796fa303"]),
            sound_enter_stunned=AudioPlaybackParms.from_json(json_data["sound_enter_stunned"]),
            audio_playback_parms_0x44c1f241=AudioPlaybackParms.from_json(json_data["audio_playback_parms_0x44c1f241"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "ing_spiderball_guardian_struct_0x152db484": self.ing_spiderball_guardian_struct_0x152db484.to_json(),
            "ing_spiderball_guardian_struct_0x2d163ff7": self.ing_spiderball_guardian_struct_0x2d163ff7.to_json(),
            "ing_spiderball_guardian_struct_0x8c2fbb19": self.ing_spiderball_guardian_struct_0x8c2fbb19.to_json(),
            "ing_spiderball_guardian_struct_0x5d612911": self.ing_spiderball_guardian_struct_0x5d612911.to_json(),
            "ing_spiderball_guardian_struct_0xfc58adff": self.ing_spiderball_guardian_struct_0xfc58adff.to_json(),
            "ing_spiderball_guardian_struct_0xc463268c": self.ing_spiderball_guardian_struct_0xc463268c.to_json(),
            "damage_radius": self.damage_radius,
            "proximity_damage": self.proximity_damage.to_json(),
            "unknown": self.unknown,
            "audio_playback_parms_0xaed23abc": self.audio_playback_parms_0xaed23abc.to_json(),
            "sound_spiderball_rolling": self.sound_spiderball_rolling.to_json(),
            "audio_playback_parms_0xcee38f10": self.audio_playback_parms_0xcee38f10.to_json(),
            "audio_playback_parms_0x796fa303": self.audio_playback_parms_0x796fa303.to_json(),
            "sound_enter_stunned": self.sound_enter_stunned.to_json(),
            "audio_playback_parms_0x44c1f241": self.audio_playback_parms_0x44c1f241.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (
                self.audio_playback_parms_0xaed23abc.dependencies_for,
                "audio_playback_parms_0xaed23abc",
                "AudioPlaybackParms",
            ),
            (self.sound_spiderball_rolling.dependencies_for, "sound_spiderball_rolling", "AudioPlaybackParms"),
            (
                self.audio_playback_parms_0xcee38f10.dependencies_for,
                "audio_playback_parms_0xcee38f10",
                "AudioPlaybackParms",
            ),
            (
                self.audio_playback_parms_0x796fa303.dependencies_for,
                "audio_playback_parms_0x796fa303",
                "AudioPlaybackParms",
            ),
            (self.sound_enter_stunned.dependencies_for, "sound_enter_stunned", "AudioPlaybackParms"),
            (
                self.audio_playback_parms_0x44c1f241.dependencies_for,
                "audio_playback_parms_0x44c1f241",
                "AudioPlaybackParms",
            ),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct31.{field_name} ({field_type}): {e}")


def _decode_ing_spiderball_guardian_struct_0x152db484(
    data: typing.BinaryIO, game: Game, property_size: int
) -> IngSpiderballGuardianStruct:
    return IngSpiderballGuardianStruct.from_stream(data, game, property_size)


def _decode_ing_spiderball_guardian_struct_0x2d163ff7(
    data: typing.BinaryIO, game: Game, property_size: int
) -> IngSpiderballGuardianStruct:
    return IngSpiderballGuardianStruct.from_stream(data, game, property_size)


def _decode_ing_spiderball_guardian_struct_0x8c2fbb19(
    data: typing.BinaryIO, game: Game, property_size: int
) -> IngSpiderballGuardianStruct:
    return IngSpiderballGuardianStruct.from_stream(data, game, property_size)


def _decode_ing_spiderball_guardian_struct_0x5d612911(
    data: typing.BinaryIO, game: Game, property_size: int
) -> IngSpiderballGuardianStruct:
    return IngSpiderballGuardianStruct.from_stream(data, game, property_size)


def _decode_ing_spiderball_guardian_struct_0xfc58adff(
    data: typing.BinaryIO, game: Game, property_size: int
) -> IngSpiderballGuardianStruct:
    return IngSpiderballGuardianStruct.from_stream(data, game, property_size)


def _decode_ing_spiderball_guardian_struct_0xc463268c(
    data: typing.BinaryIO, game: Game, property_size: int
) -> IngSpiderballGuardianStruct:
    return IngSpiderballGuardianStruct.from_stream(data, game, property_size)


def _decode_proximity_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 40.0, "di_knock_back_power": 10.0},
    )


def _decode_audio_playback_parms_0xaed23abc(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_spiderball_rolling(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0xcee38f10(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x796fa303(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_enter_stunned(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x44c1f241(
    data: typing.BinaryIO, game: Game, property_size: int
) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x152DB484: ("ing_spiderball_guardian_struct_0x152db484", _decode_ing_spiderball_guardian_struct_0x152db484),
    0x2D163FF7: ("ing_spiderball_guardian_struct_0x2d163ff7", _decode_ing_spiderball_guardian_struct_0x2d163ff7),
    0x8C2FBB19: ("ing_spiderball_guardian_struct_0x8c2fbb19", _decode_ing_spiderball_guardian_struct_0x8c2fbb19),
    0x5D612911: ("ing_spiderball_guardian_struct_0x5d612911", _decode_ing_spiderball_guardian_struct_0x5d612911),
    0xFC58ADFF: ("ing_spiderball_guardian_struct_0xfc58adff", _decode_ing_spiderball_guardian_struct_0xfc58adff),
    0xC463268C: ("ing_spiderball_guardian_struct_0xc463268c", _decode_ing_spiderball_guardian_struct_0xc463268c),
    0x0F598739: ("damage_radius", structs.decode_BIG_f),
    0xBA78D281: ("proximity_damage", _decode_proximity_damage),
    0x32133B39: ("unknown", structs.decode_BIG_f),
    0xAED23ABC: ("audio_playback_parms_0xaed23abc", _decode_audio_playback_parms_0xaed23abc),
    0x3A5E2F52: ("sound_spiderball_rolling", _decode_sound_spiderball_rolling),
    0xCEE38F10: ("audio_playback_parms_0xcee38f10", _decode_audio_playback_parms_0xcee38f10),
    0x796FA303: ("audio_playback_parms_0x796fa303", _decode_audio_playback_parms_0x796fa303),
    0xD5F3E9C4: ("sound_enter_stunned", _decode_sound_enter_stunned),
    0x44C1F241: ("audio_playback_parms_0x44c1f241", _decode_audio_playback_parms_0x44c1f241),
}
