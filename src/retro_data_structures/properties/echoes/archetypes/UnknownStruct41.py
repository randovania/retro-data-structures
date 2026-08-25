# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.archetypes.SandBossStructB import SandBossStructB
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct41Json(typing_extensions.TypedDict):
        sand_boss_struct_b_0xb9784f0e: json_util.JsonObject
        sand_boss_struct_b_0xb8ae1bdc: json_util.JsonObject
        charge_beam_info: json_util.JsonObject


@dataclasses.dataclass()
class UnknownStruct41(BaseProperty):
    sand_boss_struct_b_0xb9784f0e: SandBossStructB = dataclasses.field(
        default_factory=SandBossStructB,
        metadata={
            "reflection": FieldReflection[SandBossStructB](
                SandBossStructB,
                id=0xB9784F0E,
                original_name="SandBossStructB",
                from_json=SandBossStructB.from_json,
                to_json=SandBossStructB.to_json,
            ),
        },
    )
    sand_boss_struct_b_0xb8ae1bdc: SandBossStructB = dataclasses.field(
        default_factory=SandBossStructB,
        metadata={
            "reflection": FieldReflection[SandBossStructB](
                SandBossStructB,
                id=0xB8AE1BDC,
                original_name="SandBossStructB",
                from_json=SandBossStructB.from_json,
                to_json=SandBossStructB.to_json,
            ),
        },
    )
    charge_beam_info: PlasmaBeamInfo = dataclasses.field(
        default_factory=PlasmaBeamInfo,
        metadata={
            "reflection": FieldReflection[PlasmaBeamInfo](
                PlasmaBeamInfo,
                id=0x94DA6435,
                original_name="ChargeBeamInfo",
                from_json=PlasmaBeamInfo.from_json,
                to_json=PlasmaBeamInfo.to_json,
            ),
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
        assert property_id == 0xB9784F0E
        sand_boss_struct_b_0xb9784f0e = SandBossStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB8AE1BDC
        sand_boss_struct_b_0xb8ae1bdc = SandBossStructB.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94DA6435
        charge_beam_info = PlasmaBeamInfo.from_stream(
            data,
            game,
            property_size,
            default_override={
                "length": 500.0,
                "radius": 1.0,
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

        return cls(sand_boss_struct_b_0xb9784f0e, sand_boss_struct_b_0xb8ae1bdc, charge_beam_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x03")  # 3 properties

        data.write(b"\xb9xO\x0e")  # 0xb9784f0e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sand_boss_struct_b_0xb9784f0e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb8\xae\x1b\xdc")  # 0xb8ae1bdc
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.sand_boss_struct_b_0xb8ae1bdc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x94\xdad5")  # 0x94da6435
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.charge_beam_info.to_stream(
            data,
            game,
            default_override={
                "length": 500.0,
                "radius": 1.0,
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

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct41Json", data)
        return cls(
            sand_boss_struct_b_0xb9784f0e=SandBossStructB.from_json(json_data["sand_boss_struct_b_0xb9784f0e"]),
            sand_boss_struct_b_0xb8ae1bdc=SandBossStructB.from_json(json_data["sand_boss_struct_b_0xb8ae1bdc"]),
            charge_beam_info=PlasmaBeamInfo.from_json(json_data["charge_beam_info"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "sand_boss_struct_b_0xb9784f0e": self.sand_boss_struct_b_0xb9784f0e.to_json(),
            "sand_boss_struct_b_0xb8ae1bdc": self.sand_boss_struct_b_0xb8ae1bdc.to_json(),
            "charge_beam_info": self.charge_beam_info.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.sand_boss_struct_b_0xb9784f0e.dependencies_for, "sand_boss_struct_b_0xb9784f0e", "SandBossStructB"),
            (self.sand_boss_struct_b_0xb8ae1bdc.dependencies_for, "sand_boss_struct_b_0xb8ae1bdc", "SandBossStructB"),
            (self.charge_beam_info.dependencies_for, "charge_beam_info", "PlasmaBeamInfo"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct41.{field_name} ({field_type}): {e}")


def _decode_sand_boss_struct_b_0xb9784f0e(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossStructB:
    return SandBossStructB.from_stream(data, game, property_size)


def _decode_sand_boss_struct_b_0xb8ae1bdc(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossStructB:
    return SandBossStructB.from_stream(data, game, property_size)


def _decode_charge_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(
        data,
        game,
        property_size,
        default_override={
            "length": 500.0,
            "radius": 1.0,
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


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB9784F0E: ("sand_boss_struct_b_0xb9784f0e", _decode_sand_boss_struct_b_0xb9784f0e),
    0xB8AE1BDC: ("sand_boss_struct_b_0xb8ae1bdc", _decode_sand_boss_struct_b_0xb8ae1bdc),
    0x94DA6435: ("charge_beam_info", _decode_charge_beam_info),
}
