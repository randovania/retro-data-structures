# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class AreaAttributesJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        need_sky: bool
        dark_world: bool
        environment_effects: int
        environment_group_sound: int
        density: float
        normal_lighting: float
        override_sky: int
        phazon_damage: int


class EnvironmentEffects(enum.IntEnum):
    _None = 0
    Snow = 1
    Rain = 2
    Bubbles = 3
    DarkWorld = 4
    Aerie = 5
    ElectricRain = 6

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


class PhazonDamage(enum.IntEnum):
    _None = 0
    Blue = 1
    Orange = 2

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class AreaAttributes(BaseObjectType):
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
    need_sky: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x95D4BEE7, original_name="NeedSky"),
        },
    )
    dark_world: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB24FDE1A, original_name="DarkWorld"),
        },
    )
    environment_effects: EnvironmentEffects = dataclasses.field(
        default=EnvironmentEffects._None,
        metadata={
            "reflection": FieldReflection[EnvironmentEffects](
                EnvironmentEffects,
                id=0x9D0006AB,
                original_name="EnvironmentEffects",
                from_json=EnvironmentEffects.from_json,
                to_json=EnvironmentEffects.to_json,
            ),
        },
    )
    environment_group_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x56263E35, original_name="EnvironmentGroupSound"),
        },
    )
    density: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x64E5FE9F, original_name="Density"),
        },
    )
    normal_lighting: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBA5F801E, original_name="NormalLighting"),
        },
    )
    override_sky: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD208C9FA, original_name="OverrideSky"),
        },
    )
    phazon_damage: PhazonDamage = dataclasses.field(
        default=PhazonDamage._None,
        metadata={
            "reflection": FieldReflection[PhazonDamage](
                PhazonDamage,
                id=0xFFEEBC46,
                original_name="PhazonDamage",
                from_json=PhazonDamage.from_json,
                to_json=PhazonDamage.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "REAA"

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
        if property_count != 9:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95D4BEE7
        need_sky = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB24FDE1A
        dark_world = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D0006AB
        environment_effects = EnvironmentEffects.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56263E35
        environment_group_sound = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64E5FE9F
        density = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBA5F801E
        normal_lighting = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD208C9FA
        override_sky = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFFEEBC46
        phazon_damage = PhazonDamage.from_stream(data, game)

        return cls(
            editor_properties,
            need_sky,
            dark_world,
            environment_effects,
            environment_group_sound,
            density,
            normal_lighting,
            override_sky,
            phazon_damage,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\t")  # 9 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95\xd4\xbe\xe7")  # 0x95d4bee7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.need_sky))

        data.write(b"\xb2O\xde\x1a")  # 0xb24fde1a
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.dark_world))

        data.write(b"\x9d\x00\x06\xab")  # 0x9d0006ab
        data.write(b"\x00\x04")  # size
        self.environment_effects.to_stream(data, game)

        data.write(b"V&>5")  # 0x56263e35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.environment_group_sound))

        data.write(b"d\xe5\xfe\x9f")  # 0x64e5fe9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.density))

        data.write(b"\xba_\x80\x1e")  # 0xba5f801e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.normal_lighting))

        data.write(b"\xd2\x08\xc9\xfa")  # 0xd208c9fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.override_sky))

        data.write(b"\xff\xee\xbcF")  # 0xffeebc46
        data.write(b"\x00\x04")  # size
        self.phazon_damage.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AreaAttributesJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            need_sky=json_data["need_sky"],
            dark_world=json_data["dark_world"],
            environment_effects=EnvironmentEffects.from_json(json_data["environment_effects"]),
            environment_group_sound=json_data["environment_group_sound"],
            density=json_data["density"],
            normal_lighting=json_data["normal_lighting"],
            override_sky=json_data["override_sky"],
            phazon_damage=PhazonDamage.from_json(json_data["phazon_damage"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "need_sky": self.need_sky,
            "dark_world": self.dark_world,
            "environment_effects": self.environment_effects.to_json(),
            "environment_group_sound": self.environment_group_sound,
            "density": self.density,
            "normal_lighting": self.normal_lighting,
            "override_sky": self.override_sky,
            "phazon_damage": self.phazon_damage.to_json(),
        }

    def _dependencies_for_environment_group_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.environment_group_sound)

    def _dependencies_for_override_sky(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.override_sky)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_environment_group_sound, "environment_group_sound", "int"),
            (self._dependencies_for_override_sky, "override_sky", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for AreaAttributes.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_environment_effects(data: typing.BinaryIO, game: Game, property_size: int) -> EnvironmentEffects:
    return EnvironmentEffects.from_stream(data, game)


def _decode_phazon_damage(data: typing.BinaryIO, game: Game, property_size: int) -> PhazonDamage:
    return PhazonDamage.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x95D4BEE7: ("need_sky", structs.decode_BIG_bool_),
    0xB24FDE1A: ("dark_world", structs.decode_BIG_bool_),
    0x9D0006AB: ("environment_effects", _decode_environment_effects),
    0x56263E35: ("environment_group_sound", structs.decode_BIG_l),
    0x64E5FE9F: ("density", structs.decode_BIG_f),
    0xBA5F801E: ("normal_lighting", structs.decode_BIG_f),
    0xD208C9FA: ("override_sky", structs.decode_BIG_L),
    0xFFEEBC46: ("phazon_damage", _decode_phazon_damage),
}
