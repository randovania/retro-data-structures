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
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class DarkTrooperJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        ing_possession_data: json_util.JsonObject
        flotsam: bool
        avoid_down_frames: bool
        melee_attack_min_range: float
        melee_attack_max_range: float
        melee_attack_damage: json_util.JsonObject
        unknown: float
        ranged_attack_min_range: float
        ranged_attack_max_range: float
        ranged_attack_damage: json_util.JsonObject
        ranged_attack_projectile: int
        ragdoll_impact_sound: int
        fires_missiles: bool
        missile_projectile: int
        missile_damage: json_util.JsonObject
        scannable_info_when_attacking: int


@dataclasses.dataclass()
class DarkTrooper(BaseObjectType):
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
    ing_possession_data: IngPossessionData = dataclasses.field(
        default_factory=IngPossessionData,
        metadata={
            "reflection": FieldReflection[IngPossessionData](
                IngPossessionData,
                id=0xE61748ED,
                original_name="IngPossessionData",
                from_json=IngPossessionData.from_json,
                to_json=IngPossessionData.to_json,
            ),
        },
    )
    flotsam: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC1D1E465, original_name="Flotsam"),
        },
    )
    avoid_down_frames: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xEBAFEB27, original_name="AvoidDownFrames"),
        },
    )
    melee_attack_min_range: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBEADF2E0, original_name="MeleeAttackMinRange"),
        },
    )
    melee_attack_max_range: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFEE28A96, original_name="MeleeAttackMaxRange"),
        },
    )
    melee_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4D790EE9,
                original_name="MeleeAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2DCA199D, original_name="Unknown"),
        },
    )
    ranged_attack_min_range: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x51223A03, original_name="RangedAttackMinRange"),
        },
    )
    ranged_attack_max_range: float = dataclasses.field(
        default=18.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x116D4275, original_name="RangedAttackMaxRange"),
        },
    )
    ranged_attack_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x98F9A308,
                original_name="RangedAttackDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    ranged_attack_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB8432896, original_name="RangedAttackProjectile"),
        },
    )
    ragdoll_impact_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x49727753, original_name="RagdollImpactSound"),
        },
    )
    fires_missiles: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC9FB6A85, original_name="FiresMissiles"),
        },
    )
    missile_projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x70E97166, original_name="MissileProjectile"),
        },
    )
    missile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x258CFB4D,
                original_name="MissileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    scannable_info_when_attacking: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["SCAN"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8B6F9B43, original_name="ScannableInfoWhenAttacking"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "DKTR"

    @classmethod
    def modules(cls) -> list[str]:
        return ["PirateRagDoll.rel", "DarkTrooper.rel"]

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
        if property_count != 19:
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
                "collision_radius": 0.5,
                "collision_height": 1.600000023841858,
                "step_up_height": 1.0,
                "creature_size": 1,
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE61748ED
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC1D1E465
        flotsam = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEBAFEB27
        avoid_down_frames = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBEADF2E0
        melee_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFEE28A96
        melee_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D790EE9
        melee_attack_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2DCA199D
        unknown = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51223A03
        ranged_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x116D4275
        ranged_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98F9A308
        ranged_attack_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8432896
        ranged_attack_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49727753
        ragdoll_impact_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9FB6A85
        fires_missiles = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70E97166
        missile_projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258CFB4D
        missile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B6F9B43
        scannable_info_when_attacking = structs.BIG_L.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            ing_possession_data,
            flotsam,
            avoid_down_frames,
            melee_attack_min_range,
            melee_attack_max_range,
            melee_attack_damage,
            unknown,
            ranged_attack_min_range,
            ranged_attack_max_range,
            ranged_attack_damage,
            ranged_attack_projectile,
            ragdoll_impact_sound,
            fires_missiles,
            missile_projectile,
            missile_damage,
            scannable_info_when_attacking,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x13")  # 19 properties

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
                "collision_radius": 0.5,
                "collision_height": 1.600000023841858,
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

        data.write(b"\xe6\x17H\xed")  # 0xe61748ed
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xc1\xd1\xe4e")  # 0xc1d1e465
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.flotsam))

        data.write(b"\xeb\xaf\xeb'")  # 0xebafeb27
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.avoid_down_frames))

        data.write(b"\xbe\xad\xf2\xe0")  # 0xbeadf2e0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_attack_min_range))

        data.write(b"\xfe\xe2\x8a\x96")  # 0xfee28a96
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_attack_max_range))

        data.write(b"My\x0e\xe9")  # 0x4d790ee9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.melee_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"-\xca\x19\x9d")  # 0x2dca199d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'Q":\x03')  # 0x51223a03
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ranged_attack_min_range))

        data.write(b"\x11mBu")  # 0x116d4275
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ranged_attack_max_range))

        data.write(b"\x98\xf9\xa3\x08")  # 0x98f9a308
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ranged_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb8C(\x96")  # 0xb8432896
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.ranged_attack_projectile))

        data.write(b"IrwS")  # 0x49727753
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.ragdoll_impact_sound))

        data.write(b"\xc9\xfbj\x85")  # 0xc9fb6a85
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.fires_missiles))

        data.write(b"p\xe9qf")  # 0x70e97166
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.missile_projectile))

        data.write(b"%\x8c\xfbM")  # 0x258cfb4d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8bo\x9bC")  # 0x8b6f9b43
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.scannable_info_when_attacking))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkTrooperJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            ing_possession_data=IngPossessionData.from_json(json_data["ing_possession_data"]),
            flotsam=json_data["flotsam"],
            avoid_down_frames=json_data["avoid_down_frames"],
            melee_attack_min_range=json_data["melee_attack_min_range"],
            melee_attack_max_range=json_data["melee_attack_max_range"],
            melee_attack_damage=DamageInfo.from_json(json_data["melee_attack_damage"]),
            unknown=json_data["unknown"],
            ranged_attack_min_range=json_data["ranged_attack_min_range"],
            ranged_attack_max_range=json_data["ranged_attack_max_range"],
            ranged_attack_damage=DamageInfo.from_json(json_data["ranged_attack_damage"]),
            ranged_attack_projectile=json_data["ranged_attack_projectile"],
            ragdoll_impact_sound=json_data["ragdoll_impact_sound"],
            fires_missiles=json_data["fires_missiles"],
            missile_projectile=json_data["missile_projectile"],
            missile_damage=DamageInfo.from_json(json_data["missile_damage"]),
            scannable_info_when_attacking=json_data["scannable_info_when_attacking"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "ing_possession_data": self.ing_possession_data.to_json(),
            "flotsam": self.flotsam,
            "avoid_down_frames": self.avoid_down_frames,
            "melee_attack_min_range": self.melee_attack_min_range,
            "melee_attack_max_range": self.melee_attack_max_range,
            "melee_attack_damage": self.melee_attack_damage.to_json(),
            "unknown": self.unknown,
            "ranged_attack_min_range": self.ranged_attack_min_range,
            "ranged_attack_max_range": self.ranged_attack_max_range,
            "ranged_attack_damage": self.ranged_attack_damage.to_json(),
            "ranged_attack_projectile": self.ranged_attack_projectile,
            "ragdoll_impact_sound": self.ragdoll_impact_sound,
            "fires_missiles": self.fires_missiles,
            "missile_projectile": self.missile_projectile,
            "missile_damage": self.missile_damage.to_json(),
            "scannable_info_when_attacking": self.scannable_info_when_attacking,
        }

    def _dependencies_for_ranged_attack_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ranged_attack_projectile)

    def _dependencies_for_ragdoll_impact_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.ragdoll_impact_sound)

    def _dependencies_for_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile_projectile)

    def _dependencies_for_scannable_info_when_attacking(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_when_attacking)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
            (self._dependencies_for_ranged_attack_projectile, "ranged_attack_projectile", "AssetId"),
            (self._dependencies_for_ragdoll_impact_sound, "ragdoll_impact_sound", "int"),
            (self._dependencies_for_missile_projectile, "missile_projectile", "AssetId"),
            (self._dependencies_for_scannable_info_when_attacking, "scannable_info_when_attacking", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for DarkTrooper.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(
        data,
        game,
        property_size,
        default_override={
            "leash_radius": 100.0,
            "collision_radius": 0.5,
            "collision_height": 1.600000023841858,
            "step_up_height": 1.0,
            "creature_size": 1,
        },
    )


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_melee_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ranged_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xE61748ED: ("ing_possession_data", _decode_ing_possession_data),
    0xC1D1E465: ("flotsam", structs.decode_BIG_bool_),
    0xEBAFEB27: ("avoid_down_frames", structs.decode_BIG_bool_),
    0xBEADF2E0: ("melee_attack_min_range", structs.decode_BIG_f),
    0xFEE28A96: ("melee_attack_max_range", structs.decode_BIG_f),
    0x4D790EE9: ("melee_attack_damage", _decode_melee_attack_damage),
    0x2DCA199D: ("unknown", structs.decode_BIG_f),
    0x51223A03: ("ranged_attack_min_range", structs.decode_BIG_f),
    0x116D4275: ("ranged_attack_max_range", structs.decode_BIG_f),
    0x98F9A308: ("ranged_attack_damage", _decode_ranged_attack_damage),
    0xB8432896: ("ranged_attack_projectile", structs.decode_BIG_L),
    0x49727753: ("ragdoll_impact_sound", structs.decode_BIG_l),
    0xC9FB6A85: ("fires_missiles", structs.decode_BIG_bool_),
    0x70E97166: ("missile_projectile", structs.decode_BIG_L),
    0x258CFB4D: ("missile_damage", _decode_missile_damage),
    0x8B6F9B43: ("scannable_info_when_attacking", structs.decode_BIG_L),
}
