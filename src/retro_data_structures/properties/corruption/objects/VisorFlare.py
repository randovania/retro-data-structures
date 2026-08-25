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
from retro_data_structures.properties.corruption.archetypes.FlareDef import FlareDef
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class VisorFlareJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        blend_mode: int
        constant_scale: bool
        fade_time: float
        fade_factor: float
        rotate_factor: float
        combat_visor_mode: int
        unknown: bool
        no_occlusion_test: bool
        flare1: json_util.JsonObject
        flare2: json_util.JsonObject
        flare3: json_util.JsonObject
        flare4: json_util.JsonObject
        flare5: json_util.JsonObject


@dataclasses.dataclass()
class VisorFlare(BaseObjectType):
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
    blend_mode: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCB13EF46, original_name="BlendMode"),
        },
    )
    constant_scale: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE0C5FC06, original_name="ConstantScale"),
        },
    )
    fade_time: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4124C4C, original_name="FadeTime"),
        },
    )
    fade_factor: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD6FB31BF, original_name="FadeFactor"),
        },
    )
    rotate_factor: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3161F38C, original_name="RotateFactor"),
        },
    )
    combat_visor_mode: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x43B503A6, original_name="CombatVisorMode"),
        },
    )
    unknown: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA51F243E, original_name="Unknown"),
        },
    )
    no_occlusion_test: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x050881A9, original_name="NoOcclusionTest"),
        },
    )
    flare1: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef, id=0x3C257223, original_name="Flare1", from_json=FlareDef.from_json, to_json=FlareDef.to_json
            ),
        },
    )
    flare2: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef, id=0x05A84EE6, original_name="Flare2", from_json=FlareDef.from_json, to_json=FlareDef.to_json
            ),
        },
    )
    flare3: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef, id=0x12D35AA5, original_name="Flare3", from_json=FlareDef.from_json, to_json=FlareDef.to_json
            ),
        },
    )
    flare4: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef, id=0x76B2376C, original_name="Flare4", from_json=FlareDef.from_json, to_json=FlareDef.to_json
            ),
        },
    )
    flare5: FlareDef = dataclasses.field(
        default_factory=FlareDef,
        metadata={
            "reflection": FieldReflection[FlareDef](
                FlareDef, id=0x61C9232F, original_name="Flare5", from_json=FlareDef.from_json, to_json=FlareDef.to_json
            ),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "FLAR"

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
        if property_count != 14:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB13EF46
        blend_mode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE0C5FC06
        constant_scale = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD4124C4C
        fade_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6FB31BF
        fade_factor = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3161F38C
        rotate_factor = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43B503A6
        combat_visor_mode = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA51F243E
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x050881A9
        no_occlusion_test = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3C257223
        flare1 = FlareDef.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05A84EE6
        flare2 = FlareDef.from_stream(data, game, property_size, default_override={"position": 0.25})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12D35AA5
        flare3 = FlareDef.from_stream(data, game, property_size, default_override={"position": 0.5})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76B2376C
        flare4 = FlareDef.from_stream(data, game, property_size, default_override={"position": 0.75})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61C9232F
        flare5 = FlareDef.from_stream(data, game, property_size, default_override={"position": 1.0})

        return cls(
            editor_properties,
            blend_mode,
            constant_scale,
            fade_time,
            fade_factor,
            rotate_factor,
            combat_visor_mode,
            unknown,
            no_occlusion_test,
            flare1,
            flare2,
            flare3,
            flare4,
            flare5,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x0e")  # 14 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcb\x13\xefF")  # 0xcb13ef46
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.blend_mode))

        data.write(b"\xe0\xc5\xfc\x06")  # 0xe0c5fc06
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.constant_scale))

        data.write(b"\xd4\x12LL")  # 0xd4124c4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_time))

        data.write(b"\xd6\xfb1\xbf")  # 0xd6fb31bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.fade_factor))

        data.write(b"1a\xf3\x8c")  # 0x3161f38c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rotate_factor))

        data.write(b"C\xb5\x03\xa6")  # 0x43b503a6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.combat_visor_mode))

        data.write(b"\xa5\x1f$>")  # 0xa51f243e
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b"\x05\x08\x81\xa9")  # 0x50881a9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.no_occlusion_test))

        data.write(b"<%r#")  # 0x3c257223
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flare1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x05\xa8N\xe6")  # 0x5a84ee6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flare2.to_stream(data, game, default_override={"position": 0.25})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x12\xd3Z\xa5")  # 0x12d35aa5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flare3.to_stream(data, game, default_override={"position": 0.5})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"v\xb27l")  # 0x76b2376c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flare4.to_stream(data, game, default_override={"position": 0.75})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"a\xc9#/")  # 0x61c9232f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.flare5.to_stream(data, game, default_override={"position": 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("VisorFlareJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            blend_mode=json_data["blend_mode"],
            constant_scale=json_data["constant_scale"],
            fade_time=json_data["fade_time"],
            fade_factor=json_data["fade_factor"],
            rotate_factor=json_data["rotate_factor"],
            combat_visor_mode=json_data["combat_visor_mode"],
            unknown=json_data["unknown"],
            no_occlusion_test=json_data["no_occlusion_test"],
            flare1=FlareDef.from_json(json_data["flare1"]),
            flare2=FlareDef.from_json(json_data["flare2"]),
            flare3=FlareDef.from_json(json_data["flare3"]),
            flare4=FlareDef.from_json(json_data["flare4"]),
            flare5=FlareDef.from_json(json_data["flare5"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "blend_mode": self.blend_mode,
            "constant_scale": self.constant_scale,
            "fade_time": self.fade_time,
            "fade_factor": self.fade_factor,
            "rotate_factor": self.rotate_factor,
            "combat_visor_mode": self.combat_visor_mode,
            "unknown": self.unknown,
            "no_occlusion_test": self.no_occlusion_test,
            "flare1": self.flare1.to_json(),
            "flare2": self.flare2.to_json(),
            "flare3": self.flare3.to_json(),
            "flare4": self.flare4.to_json(),
            "flare5": self.flare5.to_json(),
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_flare1(data: typing.BinaryIO, game: Game, property_size: int) -> FlareDef:
    return FlareDef.from_stream(data, game, property_size)


def _decode_flare2(data: typing.BinaryIO, game: Game, property_size: int) -> FlareDef:
    return FlareDef.from_stream(data, game, property_size, default_override={"position": 0.25})


def _decode_flare3(data: typing.BinaryIO, game: Game, property_size: int) -> FlareDef:
    return FlareDef.from_stream(data, game, property_size, default_override={"position": 0.5})


def _decode_flare4(data: typing.BinaryIO, game: Game, property_size: int) -> FlareDef:
    return FlareDef.from_stream(data, game, property_size, default_override={"position": 0.75})


def _decode_flare5(data: typing.BinaryIO, game: Game, property_size: int) -> FlareDef:
    return FlareDef.from_stream(data, game, property_size, default_override={"position": 1.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0xCB13EF46: ("blend_mode", structs.decode_BIG_l),
    0xE0C5FC06: ("constant_scale", structs.decode_BIG_bool_),
    0xD4124C4C: ("fade_time", structs.decode_BIG_f),
    0xD6FB31BF: ("fade_factor", structs.decode_BIG_f),
    0x3161F38C: ("rotate_factor", structs.decode_BIG_f),
    0x43B503A6: ("combat_visor_mode", structs.decode_BIG_l),
    0xA51F243E: ("unknown", structs.decode_BIG_bool_),
    0x050881A9: ("no_occlusion_test", structs.decode_BIG_bool_),
    0x3C257223: ("flare1", _decode_flare1),
    0x05A84EE6: ("flare2", _decode_flare2),
    0x12D35AA5: ("flare3", _decode_flare3),
    0x76B2376C: ("flare4", _decode_flare4),
    0x61C9232F: ("flare5", _decode_flare5),
}
