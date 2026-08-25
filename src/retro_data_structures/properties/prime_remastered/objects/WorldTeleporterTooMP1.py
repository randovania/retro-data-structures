# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing
import uuid

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime_remastered.archetypes.AnimSetMP1 import AnimSetMP1
from retro_data_structures.properties.prime_remastered.archetypes.VectorMP1 import VectorMP1
from retro_data_structures.properties.prime_remastered.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.prime_remastered.core.PooledString import PooledString

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class WorldTeleporterTooMP1Json(typing_extensions.TypedDict):
        world: str
        area: str
        animation_information: json_util.JsonObject
        player_scale: json_util.JsonObject
        platform: str
        platform_scale: json_util.JsonObject
        shaft_scale: json_util.JsonObject
        unk_str: json_util.JsonObject
        unk_bool1: bool
        sound: str
        volume: int
        upward_elevator: bool
        text: str
        pan: int
        unk_bool2: bool
        char_fade_in_time: float
        chars_per_second: float
        delay_before_show: float
        show_text_instead_of_cutscene: bool
        unk_float1: float
        unk_float2: float
        unk_float3: float


def _from_json_world(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_area(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_platform(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_sound(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _from_json_text(data: json_util.JsonValue) -> AssetId:
    json_data = typing.cast("str", data)
    return uuid.UUID(json_data)


def _to_json_world(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_area(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_platform(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_sound(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


def _to_json_text(obj: AssetId) -> json_util.JsonValue:
    return str(obj)


@dataclasses.dataclass()
class WorldTeleporterTooMP1(BaseProperty):
    world: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ROOM"],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0xD49A517F, original_name="World", from_json=_from_json_world, to_json=_to_json_world
            ),
        },
    )
    area: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["ROOM"],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0x9A5FFB6C, original_name="Area", from_json=_from_json_area, to_json=_to_json_area
            ),
        },
    )
    animation_information: AnimSetMP1 = dataclasses.field(
        default_factory=AnimSetMP1,
        metadata={
            "reflection": FieldReflection[AnimSetMP1](
                AnimSetMP1,
                id=0x6AEAEE72,
                original_name="AnimationInformation",
                from_json=AnimSetMP1.from_json,
                to_json=AnimSetMP1.to_json,
            ),
        },
    )
    player_scale: VectorMP1 = dataclasses.field(
        default_factory=VectorMP1,
        metadata={
            "reflection": FieldReflection[VectorMP1](
                VectorMP1,
                id=0xC2536679,
                original_name="PlayerScale",
                from_json=VectorMP1.from_json,
                to_json=VectorMP1.to_json,
            ),
        },
    )
    platform: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](
                AssetId,
                id=0xA7B31F8E,
                original_name="Platform",
                from_json=_from_json_platform,
                to_json=_to_json_platform,
            ),
        },
    )
    platform_scale: VectorMP1 = dataclasses.field(
        default_factory=VectorMP1,
        metadata={
            "reflection": FieldReflection[VectorMP1](
                VectorMP1,
                id=0x4FB5E821,
                original_name="PlatformScale",
                from_json=VectorMP1.from_json,
                to_json=VectorMP1.to_json,
            ),
        },
    )
    shaft_scale: VectorMP1 = dataclasses.field(
        default_factory=VectorMP1,
        metadata={
            "reflection": FieldReflection[VectorMP1](
                VectorMP1,
                id=0xBB3AE62A,
                original_name="ShaftScale",
                from_json=VectorMP1.from_json,
                to_json=VectorMP1.to_json,
            ),
        },
    )
    unk_str: PooledString = dataclasses.field(
        default_factory=PooledString,
        metadata={
            "reflection": FieldReflection[PooledString](
                PooledString,
                id=0xB8D54E2C,
                original_name="UnkStr",
                from_json=PooledString.from_json,
                to_json=PooledString.to_json,
            ),
        },
    )
    unk_bool1: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA6931C09, original_name="UnkBool1"),
        },
    )
    sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0x5407BB23, original_name="Sound", from_json=_from_json_sound, to_json=_to_json_sound
            ),
        },
    )
    volume: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x82955270, original_name="Volume"),
        },
    )
    upward_elevator: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x03FA3EA7, original_name="UpwardElevator"),
        },
    )
    text: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](
                AssetId, id=0x980B33E8, original_name="Text", from_json=_from_json_text, to_json=_to_json_text
            ),
        },
    )
    pan: int = dataclasses.field(
        default=64,
        metadata={
            "reflection": FieldReflection[int](int, id=0x838C35FF, original_name="Pan"),
        },
    )
    unk_bool2: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x952E3BAD, original_name="UnkBool2"),
        },
    )
    char_fade_in_time: float = dataclasses.field(
        default=0.009999999776482582,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5558F09D, original_name="CharFadeInTime"),
        },
    )
    chars_per_second: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEEFC68E9, original_name="CharsPerSecond"),
        },
    )
    delay_before_show: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA936D90D, original_name="DelayBeforeShow"),
        },
    )
    show_text_instead_of_cutscene: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x1B68A003, original_name="ShowTextInsteadOfCutscene"),
        },
    )
    unk_float1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x53B5754B, original_name="UnkFloat1"),
        },
    )
    unk_float2: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x977347D4, original_name="UnkFloat2"),
        },
    )
    unk_float3: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDC35E803, original_name="UnkFloat3"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_count = structs.LITTLE_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
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
        if property_count != 22:
            return None

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xD49A517F
        world = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x9A5FFB6C
        area = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x6AEAEE72
        animation_information = AnimSetMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xC2536679
        player_scale = VectorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xA7B31F8E
        platform = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x4FB5E821
        platform_scale = VectorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xBB3AE62A
        shaft_scale = VectorMP1.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xB8D54E2C
        unk_str = PooledString.from_stream(data, game, property_size)

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xA6931C09
        unk_bool1 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x5407BB23
        sound = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x82955270
        volume = structs.LITTLE_l.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x03FA3EA7
        upward_elevator = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x980B33E8
        text = uuid.UUID(bytes_le=data.read(16))

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x838C35FF
        pan = structs.LITTLE_l.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x952E3BAD
        unk_bool2 = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x5558F09D
        char_fade_in_time = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xEEFC68E9
        chars_per_second = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xA936D90D
        delay_before_show = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x1B68A003
        show_text_instead_of_cutscene = structs.LITTLE_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x53B5754B
        unk_float1 = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0x977347D4
        unk_float2 = structs.LITTLE_f.unpack(data.read(4))[0]

        property_id, property_size = structs.LITTLE_LH.unpack(data.read(6))
        assert property_id == 0xDC35E803
        unk_float3 = structs.LITTLE_f.unpack(data.read(4))[0]

        return cls(
            world,
            area,
            animation_information,
            player_scale,
            platform,
            platform_scale,
            shaft_scale,
            unk_str,
            unk_bool1,
            sound,
            volume,
            upward_elevator,
            text,
            pan,
            unk_bool2,
            char_fade_in_time,
            chars_per_second,
            delay_before_show,
            show_text_instead_of_cutscene,
            unk_float1,
            unk_float2,
            unk_float3,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b"\x06\x00")  # 6 properties
        num_properties_written = 6

        data.write(b"\x7fQ\x9a\xd4")  # 0xd49a517f
        data.write(b"\x10\x00")  # size
        data.write(self.world.bytes_le)

        data.write(b"l\xfb_\x9a")  # 0x9a5ffb6c
        data.write(b"\x10\x00")  # size
        data.write(self.area.bytes_le)

        data.write(b"r\xee\xeaj")  # 0x6aeaee72
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"yfS\xc2")  # 0xc2536679
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.player_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        if self.platform != default_override.get("platform", default_asset_id):
            num_properties_written += 1
            data.write(b"\x8e\x1f\xb3\xa7")  # 0xa7b31f8e
            data.write(b"\x10\x00")  # size
            data.write(self.platform.bytes_le)

        data.write(b"!\xe8\xb5O")  # 0x4fb5e821
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.platform_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"*\xe6:\xbb")  # 0xbb3ae62a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shaft_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.LITTLE_H.pack(after - before - 2))
        data.seek(after)

        if self.unk_str != default_override.get("unk_str", PooledString()):
            num_properties_written += 1
            data.write(b",N\xd5\xb8")  # 0xb8d54e2c
            before = data.tell()
            data.write(b"\x00\x00")  # size placeholder
            self.unk_str.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.LITTLE_H.pack(after - before - 2))
            data.seek(after)

        if self.unk_bool1 != default_override.get("unk_bool1", True):
            num_properties_written += 1
            data.write(b"\t\x1c\x93\xa6")  # 0xa6931c09
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool1))

        if self.sound != default_override.get("sound", default_asset_id):
            num_properties_written += 1
            data.write(b"#\xbb\x07T")  # 0x5407bb23
            data.write(b"\x10\x00")  # size
            data.write(self.sound.bytes_le)

        if self.volume != default_override.get("volume", 127):
            num_properties_written += 1
            data.write(b"pR\x95\x82")  # 0x82955270
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_l.pack(self.volume))

        if self.upward_elevator != default_override.get("upward_elevator", False):
            num_properties_written += 1
            data.write(b"\xa7>\xfa\x03")  # 0x3fa3ea7
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.upward_elevator))

        if self.text != default_override.get("text", default_asset_id):
            num_properties_written += 1
            data.write(b"\xe83\x0b\x98")  # 0x980b33e8
            data.write(b"\x10\x00")  # size
            data.write(self.text.bytes_le)

        if self.pan != default_override.get("pan", 64):
            num_properties_written += 1
            data.write(b"\xff5\x8c\x83")  # 0x838c35ff
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_l.pack(self.pan))

        if self.unk_bool2 != default_override.get("unk_bool2", False):
            num_properties_written += 1
            data.write(b"\xad;.\x95")  # 0x952e3bad
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.unk_bool2))

        if self.char_fade_in_time != default_override.get("char_fade_in_time", 0.009999999776482582):
            num_properties_written += 1
            data.write(b"\x9d\xf0XU")  # 0x5558f09d
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.char_fade_in_time))

        if self.chars_per_second != default_override.get("chars_per_second", 8.0):
            num_properties_written += 1
            data.write(b"\xe9h\xfc\xee")  # 0xeefc68e9
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.chars_per_second))

        if self.delay_before_show != default_override.get("delay_before_show", 0.0):
            num_properties_written += 1
            data.write(b"\r\xd96\xa9")  # 0xa936d90d
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.delay_before_show))

        if self.show_text_instead_of_cutscene != default_override.get("show_text_instead_of_cutscene", False):
            num_properties_written += 1
            data.write(b"\x03\xa0h\x1b")  # 0x1b68a003
            data.write(b"\x01\x00")  # size
            data.write(structs.LITTLE_bool_.pack(self.show_text_instead_of_cutscene))

        if self.unk_float1 != default_override.get("unk_float1", 0.0):
            num_properties_written += 1
            data.write(b"Ku\xb5S")  # 0x53b5754b
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float1))

        if self.unk_float2 != default_override.get("unk_float2", 2.0):
            num_properties_written += 1
            data.write(b"\xd4Gs\x97")  # 0x977347d4
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float2))

        if self.unk_float3 != default_override.get("unk_float3", 3.0):
            num_properties_written += 1
            data.write(b"\x03\xe85\xdc")  # 0xdc35e803
            data.write(b"\x04\x00")  # size
            data.write(structs.LITTLE_f.pack(self.unk_float3))

        if num_properties_written != 6:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack("<H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WorldTeleporterTooMP1Json", data)
        return cls(
            world=uuid.UUID(json_data["world"]),
            area=uuid.UUID(json_data["area"]),
            animation_information=AnimSetMP1.from_json(json_data["animation_information"]),
            player_scale=VectorMP1.from_json(json_data["player_scale"]),
            platform=uuid.UUID(json_data["platform"]),
            platform_scale=VectorMP1.from_json(json_data["platform_scale"]),
            shaft_scale=VectorMP1.from_json(json_data["shaft_scale"]),
            unk_str=PooledString.from_json(json_data["unk_str"]),
            unk_bool1=json_data["unk_bool1"],
            sound=uuid.UUID(json_data["sound"]),
            volume=json_data["volume"],
            upward_elevator=json_data["upward_elevator"],
            text=uuid.UUID(json_data["text"]),
            pan=json_data["pan"],
            unk_bool2=json_data["unk_bool2"],
            char_fade_in_time=json_data["char_fade_in_time"],
            chars_per_second=json_data["chars_per_second"],
            delay_before_show=json_data["delay_before_show"],
            show_text_instead_of_cutscene=json_data["show_text_instead_of_cutscene"],
            unk_float1=json_data["unk_float1"],
            unk_float2=json_data["unk_float2"],
            unk_float3=json_data["unk_float3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "world": str(self.world),
            "area": str(self.area),
            "animation_information": self.animation_information.to_json(),
            "player_scale": self.player_scale.to_json(),
            "platform": str(self.platform),
            "platform_scale": self.platform_scale.to_json(),
            "shaft_scale": self.shaft_scale.to_json(),
            "unk_str": self.unk_str.to_json(),
            "unk_bool1": self.unk_bool1,
            "sound": str(self.sound),
            "volume": self.volume,
            "upward_elevator": self.upward_elevator,
            "text": str(self.text),
            "pan": self.pan,
            "unk_bool2": self.unk_bool2,
            "char_fade_in_time": self.char_fade_in_time,
            "chars_per_second": self.chars_per_second,
            "delay_before_show": self.delay_before_show,
            "show_text_instead_of_cutscene": self.show_text_instead_of_cutscene,
            "unk_float1": self.unk_float1,
            "unk_float2": self.unk_float2,
            "unk_float3": self.unk_float3,
        }


def _decode_world(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_area(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimSetMP1:
    return AnimSetMP1.from_stream(data, game, property_size)


def _decode_player_scale(data: typing.BinaryIO, game: Game, property_size: int) -> VectorMP1:
    return VectorMP1.from_stream(data, game, property_size)


def _decode_platform(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_platform_scale(data: typing.BinaryIO, game: Game, property_size: int) -> VectorMP1:
    return VectorMP1.from_stream(data, game, property_size)


def _decode_shaft_scale(data: typing.BinaryIO, game: Game, property_size: int) -> VectorMP1:
    return VectorMP1.from_stream(data, game, property_size)


def _decode_unk_str(data: typing.BinaryIO, game: Game, property_size: int) -> PooledString:
    return PooledString.from_stream(data, game, property_size)


def _decode_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


def _decode_text(data: typing.BinaryIO, game: Game, property_size: int) -> AssetId:
    return uuid.UUID(bytes_le=data.read(16))


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xD49A517F: ("world", _decode_world),
    0x9A5FFB6C: ("area", _decode_area),
    0x6AEAEE72: ("animation_information", _decode_animation_information),
    0xC2536679: ("player_scale", _decode_player_scale),
    0xA7B31F8E: ("platform", _decode_platform),
    0x4FB5E821: ("platform_scale", _decode_platform_scale),
    0xBB3AE62A: ("shaft_scale", _decode_shaft_scale),
    0xB8D54E2C: ("unk_str", _decode_unk_str),
    0xA6931C09: ("unk_bool1", structs.decode_LITTLE_bool_),
    0x5407BB23: ("sound", _decode_sound),
    0x82955270: ("volume", structs.decode_LITTLE_l),
    0x03FA3EA7: ("upward_elevator", structs.decode_LITTLE_bool_),
    0x980B33E8: ("text", _decode_text),
    0x838C35FF: ("pan", structs.decode_LITTLE_l),
    0x952E3BAD: ("unk_bool2", structs.decode_LITTLE_bool_),
    0x5558F09D: ("char_fade_in_time", structs.decode_LITTLE_f),
    0xEEFC68E9: ("chars_per_second", structs.decode_LITTLE_f),
    0xA936D90D: ("delay_before_show", structs.decode_LITTLE_f),
    0x1B68A003: ("show_text_instead_of_cutscene", structs.decode_LITTLE_bool_),
    0x53B5754B: ("unk_float1", structs.decode_LITTLE_f),
    0x977347D4: ("unk_float2", structs.decode_LITTLE_f),
    0xDC35E803: ("unk_float3", structs.decode_LITTLE_f),
}
