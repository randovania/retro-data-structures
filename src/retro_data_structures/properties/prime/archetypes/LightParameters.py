# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
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
        tessellation: int
        shadow_alpha: float
        max_shadow_height: float
        ambient_color: json_util.JsonValue
        make_lights: bool
        use_world_lighting: int
        light_recalculation: int
        lighting_position: json_util.JsonValue
        num_dynamic_lights: int
        num_area_lights: int
        ignore_ambient_lighting: bool
        use_light_set: int


class UseWorldLighting(enum.IntEnum):
    Unknown1 = 0
    NormalWorldLighting = 1
    Unknown2 = 2
    DisableWorldLighting = 3
    Unknown3 = 4
    Unknown4 = 5

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


class LightRecalculation(enum.IntEnum):
    Never = 0
    _8Frames = 1
    _4Frames = 2
    EveryFrame = 3

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
class LightParameters(BaseProperty):
    cast_shadow: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000000, original_name="CastShadow"),
        },
    )
    shadow_scale: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000001, original_name="ShadowScale"),
        },
    )
    tessellation: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00000002, original_name="Tessellation"),
        },
    )
    shadow_alpha: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000003, original_name="ShadowAlpha"),
        },
    )
    max_shadow_height: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000004, original_name="MaxShadowHeight"),
        },
    )
    ambient_color: Color = dataclasses.field(
        default_factory=Color,
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x00000005, original_name="AmbientColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    make_lights: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x00000006, original_name="MakeLights"),
        },
    )
    use_world_lighting: UseWorldLighting = dataclasses.field(
        default=UseWorldLighting.Unknown1,
        metadata={
            "reflection": FieldReflection[UseWorldLighting](
                UseWorldLighting,
                id=0x00000007,
                original_name="UseWorldLighting",
                from_json=UseWorldLighting.from_json,
                to_json=UseWorldLighting.to_json,
            ),
        },
    )
    light_recalculation: LightRecalculation = dataclasses.field(
        default=LightRecalculation.Never,
        metadata={
            "reflection": FieldReflection[LightRecalculation](
                LightRecalculation,
                id=0x00000008,
                original_name="LightRecalculation",
                from_json=LightRecalculation.from_json,
                to_json=LightRecalculation.to_json,
            ),
        },
    )
    lighting_position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector,
                id=0x00000009,
                original_name="LightingPosition",
                from_json=Vector.from_json,
                to_json=Vector.to_json,
            ),
        },
    )
    num_dynamic_lights: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000A, original_name="NumDynamicLights"),
        },
    )
    num_area_lights: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000B, original_name="NumAreaLights"),
        },
    )
    ignore_ambient_lighting: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000C, original_name="IgnoreAmbientLighting"),
        },
    )
    use_light_set: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="UseLightSet"),
        },
    )

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        cast_shadow = structs.BIG_bool_.unpack(data.read(1))[0]
        shadow_scale = structs.BIG_f.unpack(data.read(4))[0]
        tessellation = structs.BIG_l.unpack(data.read(4))[0]
        shadow_alpha = structs.BIG_f.unpack(data.read(4))[0]
        max_shadow_height = structs.BIG_f.unpack(data.read(4))[0]
        ambient_color = Color.from_stream(data, game, property_size)
        make_lights = structs.BIG_bool_.unpack(data.read(1))[0]
        use_world_lighting = UseWorldLighting.from_stream(data, game)
        light_recalculation = LightRecalculation.from_stream(data, game)
        lighting_position = Vector.from_stream(data, game, property_size)
        num_dynamic_lights = structs.BIG_l.unpack(data.read(4))[0]
        num_area_lights = structs.BIG_l.unpack(data.read(4))[0]
        ignore_ambient_lighting = structs.BIG_bool_.unpack(data.read(1))[0]
        use_light_set = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            cast_shadow,
            shadow_scale,
            tessellation,
            shadow_alpha,
            max_shadow_height,
            ambient_color,
            make_lights,
            use_world_lighting,
            light_recalculation,
            lighting_position,
            num_dynamic_lights,
            num_area_lights,
            ignore_ambient_lighting,
            use_light_set,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_bool_.pack(self.cast_shadow))
        data.write(structs.BIG_f.pack(self.shadow_scale))
        data.write(structs.BIG_l.pack(self.tessellation))
        data.write(structs.BIG_f.pack(self.shadow_alpha))
        data.write(structs.BIG_f.pack(self.max_shadow_height))
        self.ambient_color.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.make_lights))
        self.use_world_lighting.to_stream(data, game)
        self.light_recalculation.to_stream(data, game)
        self.lighting_position.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.num_dynamic_lights))
        data.write(structs.BIG_l.pack(self.num_area_lights))
        data.write(structs.BIG_bool_.pack(self.ignore_ambient_lighting))
        data.write(structs.BIG_l.pack(self.use_light_set))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LightParametersJson", data)
        return cls(
            cast_shadow=json_data["cast_shadow"],
            shadow_scale=json_data["shadow_scale"],
            tessellation=json_data["tessellation"],
            shadow_alpha=json_data["shadow_alpha"],
            max_shadow_height=json_data["max_shadow_height"],
            ambient_color=Color.from_json(json_data["ambient_color"]),
            make_lights=json_data["make_lights"],
            use_world_lighting=UseWorldLighting.from_json(json_data["use_world_lighting"]),
            light_recalculation=LightRecalculation.from_json(json_data["light_recalculation"]),
            lighting_position=Vector.from_json(json_data["lighting_position"]),
            num_dynamic_lights=json_data["num_dynamic_lights"],
            num_area_lights=json_data["num_area_lights"],
            ignore_ambient_lighting=json_data["ignore_ambient_lighting"],
            use_light_set=json_data["use_light_set"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "cast_shadow": self.cast_shadow,
            "shadow_scale": self.shadow_scale,
            "tessellation": self.tessellation,
            "shadow_alpha": self.shadow_alpha,
            "max_shadow_height": self.max_shadow_height,
            "ambient_color": self.ambient_color.to_json(),
            "make_lights": self.make_lights,
            "use_world_lighting": self.use_world_lighting.to_json(),
            "light_recalculation": self.light_recalculation.to_json(),
            "lighting_position": self.lighting_position.to_json(),
            "num_dynamic_lights": self.num_dynamic_lights,
            "num_area_lights": self.num_area_lights,
            "ignore_ambient_lighting": self.ignore_ambient_lighting,
            "use_light_set": self.use_light_set,
        }
