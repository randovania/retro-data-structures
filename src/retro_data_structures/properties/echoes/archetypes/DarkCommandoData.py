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
from retro_data_structures.properties.echoes.archetypes.UnknownStruct12 import UnknownStruct12
from retro_data_structures.properties.echoes.archetypes.UnknownStruct13 import UnknownStruct13
from retro_data_structures.properties.echoes.archetypes.UnknownStruct14 import UnknownStruct14
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DarkCommandoDataJson(typing_extensions.TypedDict):
        lurk_chance: float
        taunt_chance: float
        unknown: float
        charge_beam_attack_chance: float
        blade_damage: json_util.JsonObject
        sound_impact_rag_doll: json_util.JsonObject
        sound_hurled_death: json_util.JsonObject
        unknown_struct12: json_util.JsonObject
        unknown_struct13: json_util.JsonObject
        unknown_struct14: json_util.JsonObject


@dataclasses.dataclass()
class DarkCommandoData(BaseProperty):
    lurk_chance: float = dataclasses.field(
        default=12.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA4858F7D, original_name="LurkChance"),
        },
    )
    taunt_chance: float = dataclasses.field(
        default=12.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA77F6212, original_name="TauntChance"),
        },
    )
    unknown: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x48EAC726, original_name="Unknown"),
        },
    )
    charge_beam_attack_chance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB6921AC3, original_name="ChargeBeamAttackChance"),
        },
    )
    blade_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xA5912430,
                original_name="BladeDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound_impact_rag_doll: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0xA269EA39,
                original_name="Sound_ImpactRagDoll",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    sound_hurled_death: AudioPlaybackParms = dataclasses.field(
        default_factory=AudioPlaybackParms,
        metadata={
            "reflection": FieldReflection[AudioPlaybackParms](
                AudioPlaybackParms,
                id=0x4EB673BE,
                original_name="Sound_HurledDeath",
                from_json=AudioPlaybackParms.from_json,
                to_json=AudioPlaybackParms.to_json,
            ),
        },
    )
    unknown_struct12: UnknownStruct12 = dataclasses.field(
        default_factory=UnknownStruct12,
        metadata={
            "reflection": FieldReflection[UnknownStruct12](
                UnknownStruct12,
                id=0x5EC7F2BA,
                original_name="UnknownStruct12",
                from_json=UnknownStruct12.from_json,
                to_json=UnknownStruct12.to_json,
            ),
        },
    )
    unknown_struct13: UnknownStruct13 = dataclasses.field(
        default_factory=UnknownStruct13,
        metadata={
            "reflection": FieldReflection[UnknownStruct13](
                UnknownStruct13,
                id=0xE6C64015,
                original_name="UnknownStruct13",
                from_json=UnknownStruct13.from_json,
                to_json=UnknownStruct13.to_json,
            ),
        },
    )
    unknown_struct14: UnknownStruct14 = dataclasses.field(
        default_factory=UnknownStruct14,
        metadata={
            "reflection": FieldReflection[UnknownStruct14](
                UnknownStruct14,
                id=0x18247AEC,
                original_name="UnknownStruct14",
                from_json=UnknownStruct14.from_json,
                to_json=UnknownStruct14.to_json,
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
        assert property_id == 0xA4858F7D
        lurk_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA77F6212
        taunt_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48EAC726
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6921AC3
        charge_beam_attack_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA5912430
        blade_damage = DamageInfo.from_stream(
            data,
            game,
            property_size,
            default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA269EA39
        sound_impact_rag_doll = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4EB673BE
        sound_hurled_death = AudioPlaybackParms.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5EC7F2BA
        unknown_struct12 = UnknownStruct12.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE6C64015
        unknown_struct13 = UnknownStruct13.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18247AEC
        unknown_struct14 = UnknownStruct14.from_stream(data, game, property_size)

        return cls(
            lurk_chance,
            taunt_chance,
            unknown,
            charge_beam_attack_chance,
            blade_damage,
            sound_impact_rag_doll,
            sound_hurled_death,
            unknown_struct12,
            unknown_struct13,
            unknown_struct14,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"\xa4\x85\x8f}")  # 0xa4858f7d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.lurk_chance))

        data.write(b"\xa7\x7fb\x12")  # 0xa77f6212
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.taunt_chance))

        data.write(b"H\xea\xc7&")  # 0x48eac726
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b"\xb6\x92\x1a\xc3")  # 0xb6921ac3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.charge_beam_attack_chance))

        data.write(b"\xa5\x91$0")  # 0xa5912430
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.blade_damage.to_stream(
            data, game, default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0}
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa2i\xea9")  # 0xa269ea39
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_impact_rag_doll.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"N\xb6s\xbe")  # 0x4eb673be
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sound_hurled_death.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"^\xc7\xf2\xba")  # 0x5ec7f2ba
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct12.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe6\xc6@\x15")  # 0xe6c64015
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct13.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x18$z\xec")  # 0x18247aec
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct14.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkCommandoDataJson", data)
        return cls(
            lurk_chance=json_data["lurk_chance"],
            taunt_chance=json_data["taunt_chance"],
            unknown=json_data["unknown"],
            charge_beam_attack_chance=json_data["charge_beam_attack_chance"],
            blade_damage=DamageInfo.from_json(json_data["blade_damage"]),
            sound_impact_rag_doll=AudioPlaybackParms.from_json(json_data["sound_impact_rag_doll"]),
            sound_hurled_death=AudioPlaybackParms.from_json(json_data["sound_hurled_death"]),
            unknown_struct12=UnknownStruct12.from_json(json_data["unknown_struct12"]),
            unknown_struct13=UnknownStruct13.from_json(json_data["unknown_struct13"]),
            unknown_struct14=UnknownStruct14.from_json(json_data["unknown_struct14"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "lurk_chance": self.lurk_chance,
            "taunt_chance": self.taunt_chance,
            "unknown": self.unknown,
            "charge_beam_attack_chance": self.charge_beam_attack_chance,
            "blade_damage": self.blade_damage.to_json(),
            "sound_impact_rag_doll": self.sound_impact_rag_doll.to_json(),
            "sound_hurled_death": self.sound_hurled_death.to_json(),
            "unknown_struct12": self.unknown_struct12.to_json(),
            "unknown_struct13": self.unknown_struct13.to_json(),
            "unknown_struct14": self.unknown_struct14.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.sound_impact_rag_doll.dependencies_for, "sound_impact_rag_doll", "AudioPlaybackParms"),
            (self.sound_hurled_death.dependencies_for, "sound_hurled_death", "AudioPlaybackParms"),
            (self.unknown_struct12.dependencies_for, "unknown_struct12", "UnknownStruct12"),
            (self.unknown_struct13.dependencies_for, "unknown_struct13", "UnknownStruct13"),
            (self.unknown_struct14.dependencies_for, "unknown_struct14", "UnknownStruct14"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for DarkCommandoData.{field_name} ({field_type}): {e}")


def _decode_blade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(
        data,
        game,
        property_size,
        default_override={"di_weapon_type": 11, "di_damage": 20.0, "di_knock_back_power": 10.0},
    )


def _decode_sound_impact_rag_doll(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_hurled_death(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_unknown_struct12(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct12:
    return UnknownStruct12.from_stream(data, game, property_size)


def _decode_unknown_struct13(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct13:
    return UnknownStruct13.from_stream(data, game, property_size)


def _decode_unknown_struct14(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct14:
    return UnknownStruct14.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA4858F7D: ("lurk_chance", structs.decode_BIG_f),
    0xA77F6212: ("taunt_chance", structs.decode_BIG_f),
    0x48EAC726: ("unknown", structs.decode_BIG_f),
    0xB6921AC3: ("charge_beam_attack_chance", structs.decode_BIG_f),
    0xA5912430: ("blade_damage", _decode_blade_damage),
    0xA269EA39: ("sound_impact_rag_doll", _decode_sound_impact_rag_doll),
    0x4EB673BE: ("sound_hurled_death", _decode_sound_hurled_death),
    0x5EC7F2BA: ("unknown_struct12", _decode_unknown_struct12),
    0xE6C64015: ("unknown_struct13", _decode_unknown_struct13),
    0x18247AEC: ("unknown_struct14", _decode_unknown_struct14),
}
