# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class LightParametersJson(typing_extensions.TypedDict):
        cast_shadow: bool
        shadow_scale: float
        unknown_0xecda4163: int
        shadow_alpha: float
        max_shadow_height: float
        ambient_color: json_util.JsonValue
        unknown_0xa71810e9: bool
        world_lighting_options: int
        light_recalculation: int
        lighting_position_offset: json_util.JsonValue
        num_dynamic_lights: int
        num_area_lights: int
        use_old_lighting: bool
        ignore_ambient_lighting: bool
        use_light_set: int


class WorldLightingOptions(enum.IntEnum):
    Unknown1 = 0
    NormalWorldLighting = 1
    Unknown2 = 2
    DisableWorldLighting = 3

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


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xCD639B46,
    0x1D011A39,
    0xECDA4163,
    0x3E2CD38D,
    0x328E31B,
    0xA33E5B0E,
    0xA71810E9,
    0x6B5E7509,
    0x628E6AC3,
    0xD19DE775,
    0xCAC1E778,
    0x67F4D3DE,
    0xFB7A7ABB,
    0x61A940D6,
    0x1F715FD3,
)


@dataclasses.dataclass()
class LightParameters(BaseProperty):
    cast_shadow: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xCD639B46, original_name="CastShadow"),
        },
    )
    shadow_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1D011A39, original_name="ShadowScale"),
        },
    )
    unknown_0xecda4163: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xECDA4163, original_name="Unknown"),
        },
    )
    shadow_alpha: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E2CD38D, original_name="ShadowAlpha"),
        },
    )
    max_shadow_height: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0328E31B, original_name="MaxShadowHeight"),
        },
    )
    ambient_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xA33E5B0E, original_name="AmbientColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xa71810e9: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xA71810E9, original_name="Unknown"),
        },
    )
    world_lighting_options: WorldLightingOptions = dataclasses.field(
        default=WorldLightingOptions.NormalWorldLighting,
        metadata={
            "reflection": FieldReflection[WorldLightingOptions](
                WorldLightingOptions,
                id=0x6B5E7509,
                original_name="World Lighting Options",
                from_json=WorldLightingOptions.from_json,
                to_json=WorldLightingOptions.to_json,
            ),
        },
    )
    light_recalculation: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x628E6AC3, original_name="LightRecalculation"),
        },
    )  # Choice
    lighting_position_offset: Vector = dataclasses.field(
        default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0),
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0xD19DE775,
                original_name="LightingPositionOffset",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    num_dynamic_lights: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0xCAC1E778, original_name="NumDynamicLights"),
        },
    )
    num_area_lights: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x67F4D3DE, original_name="NumAreaLights"),
        },
    )
    use_old_lighting: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFB7A7ABB, original_name="UseOldLighting"),
        },
    )
    ignore_ambient_lighting: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x61A940D6, original_name="IgnoreAmbientLighting"),
        },
    )
    use_light_set: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x1F715FD3, original_name="UseLightSet"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LHfLHlLHfLHfLHffffLH?LHLLHLLHfffLHlLHlLH?LH?LHl")

        dec = _FAST_FORMAT.unpack(data.read(158))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            Color(*dec[17:21]),
            dec[23],
            WorldLightingOptions(dec[26]),
            dec[29],
            Vector(*dec[32:35]),
            dec[37],
            dec[40],
            dec[43],
            dec[46],
            dec[49],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\xcdc\x9bF")  # 0xcd639b46
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.cast_shadow))

        data.write(b"\x1d\x01\x1a9")  # 0x1d011a39
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_scale))

        data.write(b"\xec\xdaAc")  # 0xecda4163
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xecda4163))

        data.write(b">,\xd3\x8d")  # 0x3e2cd38d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shadow_alpha))

        data.write(b"\x03(\xe3\x1b")  # 0x328e31b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.max_shadow_height))

        data.write(b"\xa3>[\x0e")  # 0xa33e5b0e
        data.write(b"\x00\x10")  # size
        self.ambient_color.to_stream(data, game)

        data.write(b"\xa7\x18\x10\xe9")  # 0xa71810e9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa71810e9))

        data.write(b"k^u\t")  # 0x6b5e7509
        data.write(b"\x00\x04")  # size
        self.world_lighting_options.to_stream(data, game)

        data.write(b"b\x8ej\xc3")  # 0x628e6ac3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.light_recalculation))

        data.write(b"\xd1\x9d\xe7u")  # 0xd19de775
        data.write(b"\x00\x0c")  # size
        self.lighting_position_offset.to_stream(data, game)

        data.write(b"\xca\xc1\xe7x")  # 0xcac1e778
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.num_dynamic_lights))

        data.write(b"g\xf4\xd3\xde")  # 0x67f4d3de
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.num_area_lights))

        data.write(b"\xfbzz\xbb")  # 0xfb7a7abb
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.use_old_lighting))

        data.write(b"a\xa9@\xd6")  # 0x61a940d6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.ignore_ambient_lighting))

        data.write(b"\x1fq_\xd3")  # 0x1f715fd3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.use_light_set))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LightParametersJson", data)
        return cls(
            cast_shadow=json_data["cast_shadow"],
            shadow_scale=json_data["shadow_scale"],
            unknown_0xecda4163=json_data["unknown_0xecda4163"],
            shadow_alpha=json_data["shadow_alpha"],
            max_shadow_height=json_data["max_shadow_height"],
            ambient_color=Color.from_json(json_data["ambient_color"]),
            unknown_0xa71810e9=json_data["unknown_0xa71810e9"],
            world_lighting_options=WorldLightingOptions.from_json(json_data["world_lighting_options"]),
            light_recalculation=json_data["light_recalculation"],
            lighting_position_offset=Vector.from_json(json_data["lighting_position_offset"]),
            num_dynamic_lights=json_data["num_dynamic_lights"],
            num_area_lights=json_data["num_area_lights"],
            use_old_lighting=json_data["use_old_lighting"],
            ignore_ambient_lighting=json_data["ignore_ambient_lighting"],
            use_light_set=json_data["use_light_set"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "cast_shadow": self.cast_shadow,
            "shadow_scale": self.shadow_scale,
            "unknown_0xecda4163": self.unknown_0xecda4163,
            "shadow_alpha": self.shadow_alpha,
            "max_shadow_height": self.max_shadow_height,
            "ambient_color": self.ambient_color.to_json(),
            "unknown_0xa71810e9": self.unknown_0xa71810e9,
            "world_lighting_options": self.world_lighting_options.to_json(),
            "light_recalculation": self.light_recalculation,
            "lighting_position_offset": self.lighting_position_offset.to_json(),
            "num_dynamic_lights": self.num_dynamic_lights,
            "num_area_lights": self.num_area_lights,
            "use_old_lighting": self.use_old_lighting,
            "ignore_ambient_lighting": self.ignore_ambient_lighting,
            "use_light_set": self.use_light_set,
        }


def _decode_ambient_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_world_lighting_options(data: typing.BinaryIO, game: Game, property_size: int) -> WorldLightingOptions:
    return WorldLightingOptions.from_stream(data, game)


def _decode_lighting_position_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCD639B46: ("cast_shadow", structs.decode_BIG_bool_),
    0x1D011A39: ("shadow_scale", structs.decode_BIG_f),
    0xECDA4163: ("unknown_0xecda4163", structs.decode_BIG_l),
    0x3E2CD38D: ("shadow_alpha", structs.decode_BIG_f),
    0x0328E31B: ("max_shadow_height", structs.decode_BIG_f),
    0xA33E5B0E: ("ambient_color", _decode_ambient_color),
    0xA71810E9: ("unknown_0xa71810e9", structs.decode_BIG_bool_),
    0x6B5E7509: ("world_lighting_options", _decode_world_lighting_options),
    0x628E6AC3: ("light_recalculation", structs.decode_BIG_L),
    0xD19DE775: ("lighting_position_offset", _decode_lighting_position_offset),
    0xCAC1E778: ("num_dynamic_lights", structs.decode_BIG_l),
    0x67F4D3DE: ("num_area_lights", structs.decode_BIG_l),
    0xFB7A7ABB: ("use_old_lighting", structs.decode_BIG_bool_),
    0x61A940D6: ("ignore_ambient_lighting", structs.decode_BIG_bool_),
    0x1F715FD3: ("use_light_set", structs.decode_BIG_l),
}
