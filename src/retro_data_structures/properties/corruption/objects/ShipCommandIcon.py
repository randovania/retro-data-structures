# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ShipCommandIconJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0x11234a3f: bool
        unknown_0x4b198e71: bool
        scannable: bool
        function: int
        disabled_texture: int
        category_texture: int
        specific_function_texture: int
        disabled_animation: json_util.JsonObject
        category_animation: json_util.JsonObject
        function_animation: json_util.JsonObject
        necessary_upgrade: int
        unknown_0x48ef8ade: int
        unknown_0x69a7e62c: float
        scan_sound: int
        executing_sound: int
        missile_empty: int


@dataclasses.dataclass()
class ShipCommandIcon(BaseObjectType):
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
    unknown_0x11234a3f: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x11234A3F, original_name="Unknown"),
        },
    )
    unknown_0x4b198e71: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x4B198E71, original_name="Unknown"),
        },
    )
    scannable: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8B9B584C, original_name="Scannable"),
        },
    )
    function: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x95F8D644, original_name="Function"),
        },
    )
    disabled_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC39F8936, original_name="DisabledTexture"),
        },
    )
    category_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x222CF8EC, original_name="CategoryTexture"),
        },
    )
    specific_function_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x0BF00EB1, original_name="SpecificFunctionTexture"),
        },
    )
    disabled_animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x6D10C987,
                original_name="DisabledAnimation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    category_animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0x97ADB194,
                original_name="CategoryAnimation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    function_animation: AnimationParameters = dataclasses.field(
        default_factory=AnimationParameters,
        metadata={
            "reflection": FieldReflection[AnimationParameters](
                AnimationParameters,
                id=0xA797679C,
                original_name="FunctionAnimation",
                from_json=AnimationParameters.from_json,
                to_json=AnimationParameters.to_json,
            ),
        },
    )
    necessary_upgrade: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0x08072DA5,
                original_name="NecessaryUpgrade",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    unknown_0x48ef8ade: int = dataclasses.field(
        default=4050431932,
        metadata={
            "reflection": FieldReflection[int](int, id=0x48EF8ADE, original_name="Unknown"),
        },
    )  # Choice
    unknown_0x69a7e62c: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x69A7E62C, original_name="Unknown"),
        },
    )
    scan_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xCE6A78C8, original_name="ScanSound"),
        },
    )
    executing_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x515460AC, original_name="ExecutingSound"),
        },
    )
    missile_empty: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x10289804, original_name="MissileEmpty"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SHCI"

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
        assert property_id == 0x11234A3F
        unknown_0x11234a3f = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B198E71
        unknown_0x4b198e71 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B9B584C
        scannable = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95F8D644
        function = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC39F8936
        disabled_texture = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x222CF8EC
        category_texture = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0BF00EB1
        specific_function_texture = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6D10C987
        disabled_animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97ADB194
        category_animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA797679C
        function_animation = AnimationParameters.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08072DA5
        necessary_upgrade = enums.PlayerItemEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48EF8ADE
        unknown_0x48ef8ade = structs.BIG_L.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69A7E62C
        unknown_0x69a7e62c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE6A78C8
        scan_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x515460AC
        executing_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10289804
        missile_empty = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            editor_properties,
            unknown_0x11234a3f,
            unknown_0x4b198e71,
            scannable,
            function,
            disabled_texture,
            category_texture,
            specific_function_texture,
            disabled_animation,
            category_animation,
            function_animation,
            necessary_upgrade,
            unknown_0x48ef8ade,
            unknown_0x69a7e62c,
            scan_sound,
            executing_sound,
            missile_empty,
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

        data.write(b"\x11#J?")  # 0x11234a3f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x11234a3f))

        data.write(b"K\x19\x8eq")  # 0x4b198e71
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4b198e71))

        data.write(b"\x8b\x9bXL")  # 0x8b9b584c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.scannable))

        data.write(b"\x95\xf8\xd6D")  # 0x95f8d644
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.function))

        data.write(b"\xc3\x9f\x896")  # 0xc39f8936
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.disabled_texture))

        data.write(b'",\xf8\xec')  # 0x222cf8ec
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.category_texture))

        data.write(b"\x0b\xf0\x0e\xb1")  # 0xbf00eb1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.specific_function_texture))

        data.write(b"m\x10\xc9\x87")  # 0x6d10c987
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.disabled_animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x97\xad\xb1\x94")  # 0x97adb194
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.category_animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa7\x97g\x9c")  # 0xa797679c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.function_animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x08\x07-\xa5")  # 0x8072da5
        data.write(b"\x00\x04")  # size
        self.necessary_upgrade.to_stream(data, game)

        data.write(b"H\xef\x8a\xde")  # 0x48ef8ade
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.unknown_0x48ef8ade))

        data.write(b"i\xa7\xe6,")  # 0x69a7e62c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x69a7e62c))

        data.write(b"\xcejx\xc8")  # 0xce6a78c8
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.scan_sound))

        data.write(b"QT`\xac")  # 0x515460ac
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.executing_sound))

        data.write(b"\x10(\x98\x04")  # 0x10289804
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.missile_empty))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShipCommandIconJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_0x11234a3f=json_data["unknown_0x11234a3f"],
            unknown_0x4b198e71=json_data["unknown_0x4b198e71"],
            scannable=json_data["scannable"],
            function=json_data["function"],
            disabled_texture=json_data["disabled_texture"],
            category_texture=json_data["category_texture"],
            specific_function_texture=json_data["specific_function_texture"],
            disabled_animation=AnimationParameters.from_json(json_data["disabled_animation"]),
            category_animation=AnimationParameters.from_json(json_data["category_animation"]),
            function_animation=AnimationParameters.from_json(json_data["function_animation"]),
            necessary_upgrade=enums.PlayerItemEnum.from_json(json_data["necessary_upgrade"]),
            unknown_0x48ef8ade=json_data["unknown_0x48ef8ade"],
            unknown_0x69a7e62c=json_data["unknown_0x69a7e62c"],
            scan_sound=json_data["scan_sound"],
            executing_sound=json_data["executing_sound"],
            missile_empty=json_data["missile_empty"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_0x11234a3f": self.unknown_0x11234a3f,
            "unknown_0x4b198e71": self.unknown_0x4b198e71,
            "scannable": self.scannable,
            "function": self.function,
            "disabled_texture": self.disabled_texture,
            "category_texture": self.category_texture,
            "specific_function_texture": self.specific_function_texture,
            "disabled_animation": self.disabled_animation.to_json(),
            "category_animation": self.category_animation.to_json(),
            "function_animation": self.function_animation.to_json(),
            "necessary_upgrade": self.necessary_upgrade.to_json(),
            "unknown_0x48ef8ade": self.unknown_0x48ef8ade,
            "unknown_0x69a7e62c": self.unknown_0x69a7e62c,
            "scan_sound": self.scan_sound,
            "executing_sound": self.executing_sound,
            "missile_empty": self.missile_empty,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_disabled_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_category_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_function_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_necessary_upgrade(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x11234A3F: ("unknown_0x11234a3f", structs.decode_BIG_bool_),
    0x4B198E71: ("unknown_0x4b198e71", structs.decode_BIG_bool_),
    0x8B9B584C: ("scannable", structs.decode_BIG_bool_),
    0x95F8D644: ("function", structs.decode_BIG_l),
    0xC39F8936: ("disabled_texture", structs.decode_BIG_Q),
    0x222CF8EC: ("category_texture", structs.decode_BIG_Q),
    0x0BF00EB1: ("specific_function_texture", structs.decode_BIG_Q),
    0x6D10C987: ("disabled_animation", _decode_disabled_animation),
    0x97ADB194: ("category_animation", _decode_category_animation),
    0xA797679C: ("function_animation", _decode_function_animation),
    0x08072DA5: ("necessary_upgrade", _decode_necessary_upgrade),
    0x48EF8ADE: ("unknown_0x48ef8ade", structs.decode_BIG_L),
    0x69A7E62C: ("unknown_0x69a7e62c", structs.decode_BIG_f),
    0xCE6A78C8: ("scan_sound", structs.decode_BIG_Q),
    0x515460AC: ("executing_sound", structs.decode_BIG_Q),
    0x10289804: ("missile_empty", structs.decode_BIG_Q),
}
