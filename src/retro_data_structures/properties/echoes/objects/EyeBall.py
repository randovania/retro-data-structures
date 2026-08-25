# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.color import Color
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

    class EyeBallJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        close_time: float
        fire_wait_time: float
        projectile: int
        ray_damage: json_util.JsonObject
        plasma_burn: int
        plasma_pulse: int
        plasma_texture: int
        plasma_glow: int
        laser_inner_color: json_util.JsonValue
        laser_outer_color: json_util.JsonValue
        unknown_0x81d14be8: int
        unknown_0x6e1320d6: int
        unknown_0x85249bd5: int
        unknown_0x6ae6f0eb: int
        laser_sound: int
        should_be_triggered: bool
        max_audible_distance: float
        drop_off: float


@dataclasses.dataclass()
class EyeBall(BaseObjectType):
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
    close_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD0D88EA6, original_name="CloseTime"),
        },
    )
    fire_wait_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC00CF821, original_name="FireWaitTime"),
        },
    )
    projectile: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEF485DB9, original_name="Projectile"),
        },
    )
    ray_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x22A9F2D2,
                original_name="RayDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    plasma_burn: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xBC19549C, original_name="PlasmaBurn"),
        },
    )
    plasma_pulse: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x28CD86FA, original_name="PlasmaPulse"),
        },
    )
    plasma_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD7A1121D, original_name="PlasmaTexture"),
        },
    )
    plasma_glow: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xB7AA958E, original_name="PlasmaGlow"),
        },
    )
    laser_inner_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x643E5052, original_name="LaserInnerColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    laser_outer_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE11643DD, original_name="LaserOuterColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0x81d14be8: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x81D14BE8, original_name="Unknown"),
        },
    )
    unknown_0x6e1320d6: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6E1320D6, original_name="Unknown"),
        },
    )
    unknown_0x85249bd5: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x85249BD5, original_name="Unknown"),
        },
    )
    unknown_0x6ae6f0eb: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6AE6F0EB, original_name="Unknown"),
        },
    )
    laser_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE4780219, original_name="LaserSound"),
        },
    )
    should_be_triggered: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2E603DED, original_name="ShouldBeTriggered"),
        },
    )
    max_audible_distance: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x214E48A0, original_name="MaxAudibleDistance"),
        },
    )
    drop_off: float = dataclasses.field(
        default=0.20000000298023224,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08BF2E54, original_name="DropOff"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "EYEB"

    @classmethod
    def modules(cls) -> list[str]:
        return ["EyeBall.rel"]

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
        if property_count != 21:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7E397FED
        actor_information = ActorParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD0D88EA6
        close_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC00CF821
        fire_wait_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEF485DB9
        projectile = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22A9F2D2
        ray_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC19549C
        plasma_burn = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28CD86FA
        plasma_pulse = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD7A1121D
        plasma_texture = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7AA958E
        plasma_glow = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x643E5052
        laser_inner_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE11643DD
        laser_outer_color = Color.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81D14BE8
        unknown_0x81d14be8 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E1320D6
        unknown_0x6e1320d6 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85249BD5
        unknown_0x85249bd5 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6AE6F0EB
        unknown_0x6ae6f0eb = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE4780219
        laser_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2E603DED
        should_be_triggered = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214E48A0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08BF2E54
        drop_off = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            patterned,
            actor_information,
            close_time,
            fire_wait_time,
            projectile,
            ray_damage,
            plasma_burn,
            plasma_pulse,
            plasma_texture,
            plasma_glow,
            laser_inner_color,
            laser_outer_color,
            unknown_0x81d14be8,
            unknown_0x6e1320d6,
            unknown_0x85249bd5,
            unknown_0x6ae6f0eb,
            laser_sound,
            should_be_triggered,
            max_audible_distance,
            drop_off,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x15")  # 21 properties

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
        self.patterned.to_stream(data, game)
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

        data.write(b"\xd0\xd8\x8e\xa6")  # 0xd0d88ea6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.close_time))

        data.write(b"\xc0\x0c\xf8!")  # 0xc00cf821
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fire_wait_time))

        data.write(b"\xefH]\xb9")  # 0xef485db9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b'"\xa9\xf2\xd2')  # 0x22a9f2d2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ray_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbc\x19T\x9c")  # 0xbc19549c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.plasma_burn))

        data.write(b"(\xcd\x86\xfa")  # 0x28cd86fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.plasma_pulse))

        data.write(b"\xd7\xa1\x12\x1d")  # 0xd7a1121d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.plasma_texture))

        data.write(b"\xb7\xaa\x95\x8e")  # 0xb7aa958e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.plasma_glow))

        data.write(b"d>PR")  # 0x643e5052
        data.write(b"\x00\x10")  # size
        self.laser_inner_color.to_stream(data, game)

        data.write(b"\xe1\x16C\xdd")  # 0xe11643dd
        data.write(b"\x00\x10")  # size
        self.laser_outer_color.to_stream(data, game)

        data.write(b"\x81\xd1K\xe8")  # 0x81d14be8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x81d14be8))

        data.write(b"n\x13 \xd6")  # 0x6e1320d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6e1320d6))

        data.write(b"\x85$\x9b\xd5")  # 0x85249bd5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x85249bd5))

        data.write(b"j\xe6\xf0\xeb")  # 0x6ae6f0eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6ae6f0eb))

        data.write(b"\xe4x\x02\x19")  # 0xe4780219
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.laser_sound))

        data.write(b".`=\xed")  # 0x2e603ded
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.should_be_triggered))

        data.write(b"!NH\xa0")  # 0x214e48a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b"\x08\xbf.T")  # 0x8bf2e54
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.drop_off))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EyeBallJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            patterned=PatternedAITypedef.from_json(json_data["patterned"]),
            actor_information=ActorParameters.from_json(json_data["actor_information"]),
            close_time=json_data["close_time"],
            fire_wait_time=json_data["fire_wait_time"],
            projectile=json_data["projectile"],
            ray_damage=DamageInfo.from_json(json_data["ray_damage"]),
            plasma_burn=json_data["plasma_burn"],
            plasma_pulse=json_data["plasma_pulse"],
            plasma_texture=json_data["plasma_texture"],
            plasma_glow=json_data["plasma_glow"],
            laser_inner_color=Color.from_json(json_data["laser_inner_color"]),
            laser_outer_color=Color.from_json(json_data["laser_outer_color"]),
            unknown_0x81d14be8=json_data["unknown_0x81d14be8"],
            unknown_0x6e1320d6=json_data["unknown_0x6e1320d6"],
            unknown_0x85249bd5=json_data["unknown_0x85249bd5"],
            unknown_0x6ae6f0eb=json_data["unknown_0x6ae6f0eb"],
            laser_sound=json_data["laser_sound"],
            should_be_triggered=json_data["should_be_triggered"],
            max_audible_distance=json_data["max_audible_distance"],
            drop_off=json_data["drop_off"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "patterned": self.patterned.to_json(),
            "actor_information": self.actor_information.to_json(),
            "close_time": self.close_time,
            "fire_wait_time": self.fire_wait_time,
            "projectile": self.projectile,
            "ray_damage": self.ray_damage.to_json(),
            "plasma_burn": self.plasma_burn,
            "plasma_pulse": self.plasma_pulse,
            "plasma_texture": self.plasma_texture,
            "plasma_glow": self.plasma_glow,
            "laser_inner_color": self.laser_inner_color.to_json(),
            "laser_outer_color": self.laser_outer_color.to_json(),
            "unknown_0x81d14be8": self.unknown_0x81d14be8,
            "unknown_0x6e1320d6": self.unknown_0x6e1320d6,
            "unknown_0x85249bd5": self.unknown_0x85249bd5,
            "unknown_0x6ae6f0eb": self.unknown_0x6ae6f0eb,
            "laser_sound": self.laser_sound,
            "should_be_triggered": self.should_be_triggered,
            "max_audible_distance": self.max_audible_distance,
            "drop_off": self.drop_off,
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_plasma_burn(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.plasma_burn)

    def _dependencies_for_plasma_pulse(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.plasma_pulse)

    def _dependencies_for_plasma_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.plasma_texture)

    def _dependencies_for_plasma_glow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.plasma_glow)

    def _dependencies_for_laser_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.laser_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_plasma_burn, "plasma_burn", "AssetId"),
            (self._dependencies_for_plasma_pulse, "plasma_pulse", "AssetId"),
            (self._dependencies_for_plasma_texture, "plasma_texture", "AssetId"),
            (self._dependencies_for_plasma_glow, "plasma_glow", "AssetId"),
            (self._dependencies_for_laser_sound, "laser_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for EyeBall.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_ray_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_laser_inner_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_laser_outer_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xB3774750: ("patterned", _decode_patterned),
    0x7E397FED: ("actor_information", _decode_actor_information),
    0xD0D88EA6: ("close_time", structs.decode_BIG_f),
    0xC00CF821: ("fire_wait_time", structs.decode_BIG_f),
    0xEF485DB9: ("projectile", structs.decode_BIG_L),
    0x22A9F2D2: ("ray_damage", _decode_ray_damage),
    0xBC19549C: ("plasma_burn", structs.decode_BIG_L),
    0x28CD86FA: ("plasma_pulse", structs.decode_BIG_L),
    0xD7A1121D: ("plasma_texture", structs.decode_BIG_L),
    0xB7AA958E: ("plasma_glow", structs.decode_BIG_L),
    0x643E5052: ("laser_inner_color", _decode_laser_inner_color),
    0xE11643DD: ("laser_outer_color", _decode_laser_outer_color),
    0x81D14BE8: ("unknown_0x81d14be8", structs.decode_BIG_l),
    0x6E1320D6: ("unknown_0x6e1320d6", structs.decode_BIG_l),
    0x85249BD5: ("unknown_0x85249bd5", structs.decode_BIG_l),
    0x6AE6F0EB: ("unknown_0x6ae6f0eb", structs.decode_BIG_l),
    0xE4780219: ("laser_sound", structs.decode_BIG_l),
    0x2E603DED: ("should_be_triggered", structs.decode_BIG_bool_),
    0x214E48A0: ("max_audible_distance", structs.decode_BIG_f),
    0x08BF2E54: ("drop_off", structs.decode_BIG_f),
}
