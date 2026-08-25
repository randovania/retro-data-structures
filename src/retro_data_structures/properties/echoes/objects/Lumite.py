# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class LumiteJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        unknown_0x2d9ebd7f: float
        unknown_0x6dd1c509: float
        small_shot_projectile: int
        small_shot_damage: json_util.JsonObject
        unknown_0x6d5356bb: float
        unknown_0x2d1c2ecd: float
        big_shot_projectile: int
        big_shot_damage: json_util.JsonObject
        trail_effect: int
        sunlight_enter_exit_effect: int
        unknown_0xe05d93ef: float
        unknown_0x47691396: float
        phase_in_sound: int
        phase_out_sound: int


@dataclasses.dataclass()
class Lumite(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    patterned: PatternedAITypedef = dataclasses.field(
        default_factory=PatternedAITypedef,
        metadata={
            "reflection": FieldReflection[PatternedAITypedef](
                PatternedAITypedef,
                id=0xB3774750,
                original_name="Patterned",
                from_json=PatternedAITypedef.from_json,
                to_json=PatternedAITypedef.to_json,
            ),
        },
    )
    actor_information: ActorParameters = dataclasses.field(
        default_factory=ActorParameters,
        metadata={
            "reflection": FieldReflection[ActorParameters](
                ActorParameters,
                id=0x7E397FED,
                original_name="ActorInformation",
                from_json=ActorParameters.from_json,
                to_json=ActorParameters.to_json,
            ),
        },
    )
    unknown_0x2d9ebd7f: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2D9EBD7F, original_name="Unknown"),
        },
    )
    unknown_0x6dd1c509: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6DD1C509, original_name="Unknown"),
        },
    )
    small_shot_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x48157453, original_name="SmallShotProjectile"),
        },
    )
    small_shot_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x7307C36B,
                original_name="SmallShotDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x6d5356bb: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6D5356BB, original_name="Unknown"),
        },
    )
    unknown_0x2d1c2ecd: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2D1C2ECD, original_name="Unknown"),
        },
    )
    big_shot_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD05B1D24, original_name="BigShotProjectile"),
        },
    )
    big_shot_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xBDFE699D,
                original_name="BigShotDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    trail_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x36EEE791, original_name="TrailEffect"),
        },
    )
    sunlight_enter_exit_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD2879EBB, original_name="SunlightEnterExitEffect"),
        },
    )
    unknown_0xe05d93ef: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE05D93EF, original_name="Unknown"),
        },
    )
    unknown_0x47691396: float = dataclasses.field(
        default=45.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x47691396, original_name="Unknown"),
        },
    )
    phase_in_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xA4231323, original_name="PhaseInSound"),
        },
    )
    phase_out_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x3AAF7871, original_name="PhaseOutSound"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "LUMI"

    @classmethod
    def modules(cls) -> list[str]:
        return ["Lumite.rel"]

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 17:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(
            data,
            game,
            property_size,
            default_override={
                "leash_radius": 100.0,
                "collision_radius": 0.10000000149011612,
                "collision_height": 0.10000000149011612,
                "step_up_height": 1.0,
                "creature_size": 1,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D9EBD7F
        unknown_0x2d9ebd7f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6DD1C509
        unknown_0x6dd1c509 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48157453
        small_shot_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7307C36B
        small_shot_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D5356BB
        unknown_0x6d5356bb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D1C2ECD
        unknown_0x2d1c2ecd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD05B1D24
        big_shot_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBDFE699D
        big_shot_damage = DamageInfo.from_stream(
            data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0}
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36EEE791
        trail_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD2879EBB
        sunlight_enter_exit_effect = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE05D93EF
        unknown_0xe05d93ef = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47691396
        unknown_0x47691396 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4231323
        phase_in_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3AAF7871
        phase_out_sound = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            unknown_0x2d9ebd7f,
            unknown_0x6dd1c509,
            small_shot_projectile,
            small_shot_damage,
            unknown_0x6d5356bb,
            unknown_0x2d1c2ecd,
            big_shot_projectile,
            big_shot_damage,
            trail_effect,
            sunlight_enter_exit_effect,
            unknown_0xe05d93ef,
            unknown_0x47691396,
            phase_in_sound,
            phase_out_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x11")  # 17 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb3wGP")  # 0xb3774750
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.patterned.to_stream(
            data,
            game,
            default_override={
                "leash_radius": 100.0,
                "collision_radius": 0.10000000149011612,
                "collision_height": 0.10000000149011612,
                "step_up_height": 1.0,
                "creature_size": 1,
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"~9\x7f\xed")  # 0x7e397fed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"-\x9e\xbd\x7f")  # 0x2d9ebd7f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2d9ebd7f))

        data.write(b"m\xd1\xc5\t")  # 0x6dd1c509
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6dd1c509))

        data.write(b"H\x15tS")  # 0x48157453
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.small_shot_projectile))

        data.write(b"s\x07\xc3k")  # 0x7307c36b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.small_shot_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"mSV\xbb")  # 0x6d5356bb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6d5356bb))

        data.write(b"-\x1c.\xcd")  # 0x2d1c2ecd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2d1c2ecd))

        data.write(b"\xd0[\x1d$")  # 0xd05b1d24
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.big_shot_projectile))

        data.write(b"\xbd\xfei\x9d")  # 0xbdfe699d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.big_shot_damage.to_stream(data, game, default_override={"di_weapon_type": 11, "di_damage": 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"6\xee\xe7\x91")  # 0x36eee791
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.trail_effect))

        data.write(b"\xd2\x87\x9e\xbb")  # 0xd2879ebb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.sunlight_enter_exit_effect))

        data.write(b"\xe0]\x93\xef")  # 0xe05d93ef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe05d93ef))

        data.write(b"Gi\x13\x96")  # 0x47691396
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x47691396))

        data.write(b"\xa4#\x13#")  # 0xa4231323
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.phase_in_sound))

        data.write(b":\xafxq")  # 0x3aaf7871
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.phase_out_sound))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LumiteJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            unknown_0x2d9ebd7f=json_data["unknown_0x2d9ebd7f"],
            unknown_0x6dd1c509=json_data["unknown_0x6dd1c509"],
            small_shot_projectile=json_data["small_shot_projectile"],
            small_shot_damage=DamageInfo.from_json(json_data["small_shot_damage"]),
            unknown_0x6d5356bb=json_data["unknown_0x6d5356bb"],
            unknown_0x2d1c2ecd=json_data["unknown_0x2d1c2ecd"],
            big_shot_projectile=json_data["big_shot_projectile"],
            big_shot_damage=DamageInfo.from_json(json_data["big_shot_damage"]),
            trail_effect=json_data["trail_effect"],
            sunlight_enter_exit_effect=json_data["sunlight_enter_exit_effect"],
            unknown_0xe05d93ef=json_data["unknown_0xe05d93ef"],
            unknown_0x47691396=json_data["unknown_0x47691396"],
            phase_in_sound=json_data["phase_in_sound"],
            phase_out_sound=json_data["phase_out_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "unknown_0x2d9ebd7f": self.unknown_0x2d9ebd7f,
            "unknown_0x6dd1c509": self.unknown_0x6dd1c509,
            "small_shot_projectile": self.small_shot_projectile,
            "small_shot_damage": self.small_shot_damage.to_json(),
            "unknown_0x6d5356bb": self.unknown_0x6d5356bb,
            "unknown_0x2d1c2ecd": self.unknown_0x2d1c2ecd,
            "big_shot_projectile": self.big_shot_projectile,
            "big_shot_damage": self.big_shot_damage.to_json(),
            "trail_effect": self.trail_effect,
            "sunlight_enter_exit_effect": self.sunlight_enter_exit_effect,
            "unknown_0xe05d93ef": self.unknown_0xe05d93ef,
            "unknown_0x47691396": self.unknown_0x47691396,
            "phase_in_sound": self.phase_in_sound,
            "phase_out_sound": self.phase_out_sound,
        }

    def _dependencies_for_small_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.small_shot_projectile)

    def _dependencies_for_big_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.big_shot_projectile)

    def _dependencies_for_trail_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.trail_effect)

    def _dependencies_for_sunlight_enter_exit_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sunlight_enter_exit_effect)

    def _dependencies_for_phase_in_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.phase_in_sound)

    def _dependencies_for_phase_out_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.phase_out_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_small_shot_projectile, "small_shot_projectile", "AssetId"),
            (self._dependencies_for_big_shot_projectile, "big_shot_projectile", "AssetId"),
            (self._dependencies_for_trail_effect, "trail_effect", "AssetId"),
            (self._dependencies_for_sunlight_enter_exit_effect, "sunlight_enter_exit_effect", "AssetId"),
            (self._dependencies_for_phase_in_sound, "phase_in_sound", "int"),
            (self._dependencies_for_phase_out_sound, "phase_out_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for Lumite.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "leash_radius": 100.0,
            "collision_radius": 0.10000000149011612,
            "collision_height": 0.10000000149011612,
            "step_up_height": 1.0,
            "creature_size": 1,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_small_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0})


def _decode_big_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={"di_weapon_type": 11, "di_damage": 5.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0x2D9EBD7F: ("unknown_0x2d9ebd7f", structs.decode_BIG_f),
    0x6DD1C509: ("unknown_0x6dd1c509", structs.decode_BIG_f),
    0x48157453: ("small_shot_projectile", structs.decode_BIG_L),
    0x7307C36B: ("small_shot_damage", _decode_small_shot_damage),
    0x6D5356BB: ("unknown_0x6d5356bb", structs.decode_BIG_f),
    0x2D1C2ECD: ("unknown_0x2d1c2ecd", structs.decode_BIG_f),
    0xD05B1D24: ("big_shot_projectile", structs.decode_BIG_L),
    0xBDFE699D: ("big_shot_damage", _decode_big_shot_damage),
    0x36EEE791: ("trail_effect", structs.decode_BIG_L),
    0xD2879EBB: ("sunlight_enter_exit_effect", structs.decode_BIG_L),
    0xE05D93EF: ("unknown_0xe05d93ef", structs.decode_BIG_f),
    0x47691396: ("unknown_0x47691396", structs.decode_BIG_f),
    0xA4231323: ("phase_in_sound", structs.decode_BIG_l),
    0x3AAF7871: ("phase_out_sound", structs.decode_BIG_l),
}
