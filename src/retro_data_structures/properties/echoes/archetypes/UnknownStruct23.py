# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class UnknownStruct23Json(typing_extensions.TypedDict):
        loop_duration: float
        destroy_percentage: int
        shock_wave_info: json_util.JsonObject
        sound: int


@dataclasses.dataclass()
class UnknownStruct23(BaseProperty):
    loop_duration: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCEE68723, original_name="LoopDuration"),
        },
    )
    destroy_percentage: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0x01274D6E, original_name="DestroyPercentage"),
        },
    )
    shock_wave_info: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0x8F4787CB,
                original_name="ShockWaveInfo",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x25AF490E, original_name="Sound"),
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
        if property_count != 4:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCEE68723
        loop_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01274D6E
        destroy_percentage = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F4787CB
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25AF490E
        sound = structs.BIG_l.unpack(data.read(4))[0]

        return cls(loop_duration, destroy_percentage, shock_wave_info, sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x04")  # 4 properties

        data.write(b"\xce\xe6\x87#")  # 0xcee68723
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.loop_duration))

        data.write(b"\x01'Mn")  # 0x1274d6e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.destroy_percentage))

        data.write(b"\x8fG\x87\xcb")  # 0x8f4787cb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"%\xafI\x0e")  # 0x25af490e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct23Json", data)
        return cls(
            loop_duration=json_data["loop_duration"],
            destroy_percentage=json_data["destroy_percentage"],
            shock_wave_info=ShockWaveInfo.from_json(json_data["shock_wave_info"]),
            sound=json_data["sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "loop_duration": self.loop_duration,
            "destroy_percentage": self.destroy_percentage,
            "shock_wave_info": self.shock_wave_info.to_json(),
            "sound": self.sound,
        }

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.shock_wave_info.dependencies_for, "shock_wave_info", "ShockWaveInfo"),
            (self._dependencies_for_sound, "sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for UnknownStruct23.{field_name} ({field_type}): {e}")


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xCEE68723: ("loop_duration", structs.decode_BIG_f),
    0x01274D6E: ("destroy_percentage", structs.decode_BIG_l),
    0x8F4787CB: ("shock_wave_info", _decode_shock_wave_info),
    0x25AF490E: ("sound", structs.decode_BIG_l),
}
