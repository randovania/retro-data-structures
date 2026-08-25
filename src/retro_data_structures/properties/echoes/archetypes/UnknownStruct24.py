# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct24Json(typing_extensions.TypedDict):
        beam_info: json_util.JsonObject
        damage: json_util.JsonObject
        sound: int


@dataclasses.dataclass()
class UnknownStruct24(BaseProperty):
    beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x1598012A,
                original_name="BeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
        },
    )
    damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x337F9524,
                original_name="Damage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x5F7C352E, original_name="Sound"),
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
        if property_count != 3:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1598012A
        beam_info = PlasmaBeamInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "length": 500.0,
                "expansion_speed": 4.0,
                "life_time": 1.0,
                "pulse_speed": 20.0,
                "shutdown_time": 0.25,
                "pulse_effect_scale": 2.0,
                "inner_color": Color(
                    r=0.49803900718688965, g=0.49803900718688965, b=0.49803900718688965, a=0.49803900718688965
                ),
                "outer_color": Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.49803900718688965),
            },
        )

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337F9524
        damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5F7C352E
        sound = structs.BIG_l.unpack(data.read(4))[0]

        return cls(beam_info, damage, sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\x15\x98\x01*")  # 0x1598012a
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_info.to_stream(
            data,
            game,
            default_override={
                "length": 500.0,
                "expansion_speed": 4.0,
                "life_time": 1.0,
                "pulse_speed": 20.0,
                "shutdown_time": 0.25,
                "pulse_effect_scale": 2.0,
                "inner_color": Color(
                    r=0.49803900718688965, g=0.49803900718688965, b=0.49803900718688965, a=0.49803900718688965
                ),
                "outer_color": Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.49803900718688965),
            },
        )
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"3\x7f\x95$")  # 0x337f9524
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_|5.")  # 0x5f7c352e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct24Json", data)
        return cls(
            beam_info=PlasmaBeamInfo.from_json(json_data["beam_info"]),
            damage=DamageInfo.from_json(json_data["damage"]),
            sound=json_data["sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "beam_info": self.beam_info.to_json(),
            "damage": self.damage.to_json(),
            "sound": self.sound,
        }

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.beam_info.dependencies_for, "beam_info", "PlasmaBeamInfo"),
            (self._dependencies_for_sound, "sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct24.{field_name} ({field_type}): {e}")


def _decode_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "length": 500.0,
            "expansion_speed": 4.0,
            "life_time": 1.0,
            "pulse_speed": 20.0,
            "shutdown_time": 0.25,
            "pulse_effect_scale": 2.0,
            "inner_color": Color(
                r=0.49803900718688965, g=0.49803900718688965, b=0.49803900718688965, a=0.49803900718688965
            ),
            "outer_color": Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.49803900718688965),
        },
    )


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1598012A: ("beam_info", _decode_beam_info),
    0x337F9524: ("damage", _decode_damage),
    0x5F7C352E: ("sound", structs.decode_BIG_l),
}
