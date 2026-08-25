# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SafeZoneStructBJson(typing_extensions.TypedDict):
        turn_on_sound: int
        unknown_0xd4839a3f: float
        active_loop_sound: int
        turn_off_sound: int
        player_enter_sound: int
        player_exit_sound: int
        dark_visor_spot_texture: int
        dark_visor_spot_max_size: float
        shell_environment_map: int
        shell1_animated_horiz_rate: float
        shell1_animated_vert_rate: float
        shell1_scale_horiz: float
        shell1_scale_vert: float
        shell1_texture: int
        shell2_animated_horiz_rate: float
        shell2_animated_vert_rate: float
        shell2_scale_horiz: float
        shell2_scale_vert: float
        shell2_texture: int
        shell_color: json_util.JsonValue
        unknown_0xe68b1fa8: json_util.JsonValue


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xC6BFC270,
    0xD4839A3F,
    0xE0903825,
    0xE5567935,
    0x3E854866,
    0xD3EC0993,
    0xD09F83E7,
    0xC496A6A8,
    0x74F8A729,
    0x521382C7,
    0x1BE4426E,
    0x34B2A190,
    0xAD4715A8,
    0x1E712EE2,
    0x24F6BBFA,
    0x229CEF2E,
    0x1D7A1562,
    0xBC3A7FD1,
    0xA3BB422C,
    0x47B4E863,
    0xE68B1FA8,
)


@dataclasses.dataclass()
class SafeZoneStructB(BaseProperty):
    turn_on_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xC6BFC270, original_name="TurnOnSound"),
        },
    )
    unknown_0xd4839a3f: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD4839A3F, original_name="Unknown"),
        },
    )
    active_loop_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE0903825, original_name="ActiveLoopSound"),
        },
    )
    turn_off_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE5567935, original_name="TurnOffSound"),
        },
    )
    player_enter_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x3E854866, original_name="PlayerEnterSound"),
        },
    )
    player_exit_sound: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xD3EC0993, original_name="PlayerExitSound"),
        },
    )
    dark_visor_spot_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD09F83E7, original_name="DarkVisorSpotTexture"),
        },
    )
    dark_visor_spot_max_size: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC496A6A8, original_name="DarkVisorSpotMaxSize"),
        },
    )
    shell_environment_map: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x74F8A729, original_name="ShellEnvironmentMap"),
        },
    )
    shell1_animated_horiz_rate: float = dataclasses.field(
        default=-0.03999999910593033,
        metadata={
            "reflection": FieldReflection[float](float, id=0x521382C7, original_name="Shell1AnimatedHorizRate"),
        },
    )
    shell1_animated_vert_rate: float = dataclasses.field(
        default=-0.029999999329447746,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1BE4426E, original_name="Shell1AnimatedVertRate"),
        },
    )
    shell1_scale_horiz: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x34B2A190, original_name="Shell1ScaleHoriz"),
        },
    )
    shell1_scale_vert: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAD4715A8, original_name="Shell1ScaleVert"),
        },
    )
    shell1_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1E712EE2, original_name="Shell1Texture"),
        },
    )
    shell2_animated_horiz_rate: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x24F6BBFA, original_name="Shell2AnimatedHorizRate"),
        },
    )
    shell2_animated_vert_rate: float = dataclasses.field(
        default=0.029999999329447746,
        metadata={
            "reflection": FieldReflection[float](float, id=0x229CEF2E, original_name="Shell2AnimatedVertRate"),
        },
    )
    shell2_scale_horiz: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1D7A1562, original_name="Shell2ScaleHoriz"),
        },
    )
    shell2_scale_vert: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC3A7FD1, original_name="Shell2ScaleVert"),
        },
    )
    shell2_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xA3BB422C, original_name="Shell2Texture"),
        },
    )
    shell_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.09411799907684326, g=0.49803900718688965, b=0.49803900718688965, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x47B4E863, original_name="ShellColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    unknown_0xe68b1fa8: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.749019980430603, g=0.749019980430603, b=0.749019980430603, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0xE68B1FA8, original_name="Unknown", from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 21:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHfLHlLHlLHlLHlLHLLHfLHLLHfLHfLHfLHfLHLLHfLHfLHfLHfLHLLHffffLHffff")

        dec = _FAST_FORMAT.unpack(data.read(234))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[63],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            Color(*dec[59:63]),
            Color(*dec[65:69]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x15")  # 21 properties

        data.write(b"\xc6\xbf\xc2p")  # 0xc6bfc270
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.turn_on_sound))

        data.write(b"\xd4\x83\x9a?")  # 0xd4839a3f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd4839a3f))

        data.write(b"\xe0\x908%")  # 0xe0903825
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.active_loop_sound))

        data.write(b"\xe5Vy5")  # 0xe5567935
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.turn_off_sound))

        data.write(b">\x85Hf")  # 0x3e854866
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.player_enter_sound))

        data.write(b"\xd3\xec\t\x93")  # 0xd3ec0993
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.player_exit_sound))

        data.write(b"\xd0\x9f\x83\xe7")  # 0xd09f83e7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.dark_visor_spot_texture))

        data.write(b"\xc4\x96\xa6\xa8")  # 0xc496a6a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dark_visor_spot_max_size))

        data.write(b"t\xf8\xa7)")  # 0x74f8a729
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shell_environment_map))

        data.write(b"R\x13\x82\xc7")  # 0x521382c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell1_animated_horiz_rate))

        data.write(b"\x1b\xe4Bn")  # 0x1be4426e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell1_animated_vert_rate))

        data.write(b"4\xb2\xa1\x90")  # 0x34b2a190
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell1_scale_horiz))

        data.write(b"\xadG\x15\xa8")  # 0xad4715a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell1_scale_vert))

        data.write(b"\x1eq.\xe2")  # 0x1e712ee2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shell1_texture))

        data.write(b"$\xf6\xbb\xfa")  # 0x24f6bbfa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell2_animated_horiz_rate))

        data.write(b'"\x9c\xef.')  # 0x229cef2e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell2_animated_vert_rate))

        data.write(b"\x1dz\x15b")  # 0x1d7a1562
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell2_scale_horiz))

        data.write(b"\xbc:\x7f\xd1")  # 0xbc3a7fd1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shell2_scale_vert))

        data.write(b"\xa3\xbbB,")  # 0xa3bb422c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.shell2_texture))

        data.write(b"G\xb4\xe8c")  # 0x47b4e863
        data.write(b"\x00\x10")  # size
        self.shell_color.to_stream(data, game)

        data.write(b"\xe6\x8b\x1f\xa8")  # 0xe68b1fa8
        data.write(b"\x00\x10")  # size
        self.unknown_0xe68b1fa8.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SafeZoneStructBJson", data)
        return cls(
            turn_on_sound=json_data["turn_on_sound"],
            unknown_0xd4839a3f=json_data["unknown_0xd4839a3f"],
            active_loop_sound=json_data["active_loop_sound"],
            turn_off_sound=json_data["turn_off_sound"],
            player_enter_sound=json_data["player_enter_sound"],
            player_exit_sound=json_data["player_exit_sound"],
            dark_visor_spot_texture=json_data["dark_visor_spot_texture"],
            dark_visor_spot_max_size=json_data["dark_visor_spot_max_size"],
            shell_environment_map=json_data["shell_environment_map"],
            shell1_animated_horiz_rate=json_data["shell1_animated_horiz_rate"],
            shell1_animated_vert_rate=json_data["shell1_animated_vert_rate"],
            shell1_scale_horiz=json_data["shell1_scale_horiz"],
            shell1_scale_vert=json_data["shell1_scale_vert"],
            shell1_texture=json_data["shell1_texture"],
            shell2_animated_horiz_rate=json_data["shell2_animated_horiz_rate"],
            shell2_animated_vert_rate=json_data["shell2_animated_vert_rate"],
            shell2_scale_horiz=json_data["shell2_scale_horiz"],
            shell2_scale_vert=json_data["shell2_scale_vert"],
            shell2_texture=json_data["shell2_texture"],
            shell_color=Color.from_json(json_data["shell_color"]),
            unknown_0xe68b1fa8=Color.from_json(json_data["unknown_0xe68b1fa8"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "turn_on_sound": self.turn_on_sound,
            "unknown_0xd4839a3f": self.unknown_0xd4839a3f,
            "active_loop_sound": self.active_loop_sound,
            "turn_off_sound": self.turn_off_sound,
            "player_enter_sound": self.player_enter_sound,
            "player_exit_sound": self.player_exit_sound,
            "dark_visor_spot_texture": self.dark_visor_spot_texture,
            "dark_visor_spot_max_size": self.dark_visor_spot_max_size,
            "shell_environment_map": self.shell_environment_map,
            "shell1_animated_horiz_rate": self.shell1_animated_horiz_rate,
            "shell1_animated_vert_rate": self.shell1_animated_vert_rate,
            "shell1_scale_horiz": self.shell1_scale_horiz,
            "shell1_scale_vert": self.shell1_scale_vert,
            "shell1_texture": self.shell1_texture,
            "shell2_animated_horiz_rate": self.shell2_animated_horiz_rate,
            "shell2_animated_vert_rate": self.shell2_animated_vert_rate,
            "shell2_scale_horiz": self.shell2_scale_horiz,
            "shell2_scale_vert": self.shell2_scale_vert,
            "shell2_texture": self.shell2_texture,
            "shell_color": self.shell_color.to_json(),
            "unknown_0xe68b1fa8": self.unknown_0xe68b1fa8.to_json(),
        }

    def _dependencies_for_turn_on_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.turn_on_sound)

    def _dependencies_for_active_loop_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.active_loop_sound)

    def _dependencies_for_turn_off_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.turn_off_sound)

    def _dependencies_for_player_enter_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.player_enter_sound)

    def _dependencies_for_player_exit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.player_exit_sound)

    def _dependencies_for_dark_visor_spot_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_visor_spot_texture)

    def _dependencies_for_shell_environment_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shell_environment_map)

    def _dependencies_for_shell1_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shell1_texture)

    def _dependencies_for_shell2_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shell2_texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_turn_on_sound, "turn_on_sound", "int"),
            (self._dependencies_for_active_loop_sound, "active_loop_sound", "int"),
            (self._dependencies_for_turn_off_sound, "turn_off_sound", "int"),
            (self._dependencies_for_player_enter_sound, "player_enter_sound", "int"),
            (self._dependencies_for_player_exit_sound, "player_exit_sound", "int"),
            (self._dependencies_for_dark_visor_spot_texture, "dark_visor_spot_texture", "AssetId"),
            (self._dependencies_for_shell_environment_map, "shell_environment_map", "AssetId"),
            (self._dependencies_for_shell1_texture, "shell1_texture", "AssetId"),
            (self._dependencies_for_shell2_texture, "shell2_texture", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SafeZoneStructB.{field_name} ({field_type}): {e}")


def _decode_shell_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xe68b1fa8(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC6BFC270: ("turn_on_sound", structs.decode_BIG_l),
    0xD4839A3F: ("unknown_0xd4839a3f", structs.decode_BIG_f),
    0xE0903825: ("active_loop_sound", structs.decode_BIG_l),
    0xE5567935: ("turn_off_sound", structs.decode_BIG_l),
    0x3E854866: ("player_enter_sound", structs.decode_BIG_l),
    0xD3EC0993: ("player_exit_sound", structs.decode_BIG_l),
    0xD09F83E7: ("dark_visor_spot_texture", structs.decode_BIG_L),
    0xC496A6A8: ("dark_visor_spot_max_size", structs.decode_BIG_f),
    0x74F8A729: ("shell_environment_map", structs.decode_BIG_L),
    0x521382C7: ("shell1_animated_horiz_rate", structs.decode_BIG_f),
    0x1BE4426E: ("shell1_animated_vert_rate", structs.decode_BIG_f),
    0x34B2A190: ("shell1_scale_horiz", structs.decode_BIG_f),
    0xAD4715A8: ("shell1_scale_vert", structs.decode_BIG_f),
    0x1E712EE2: ("shell1_texture", structs.decode_BIG_L),
    0x24F6BBFA: ("shell2_animated_horiz_rate", structs.decode_BIG_f),
    0x229CEF2E: ("shell2_animated_vert_rate", structs.decode_BIG_f),
    0x1D7A1562: ("shell2_scale_horiz", structs.decode_BIG_f),
    0xBC3A7FD1: ("shell2_scale_vert", structs.decode_BIG_f),
    0xA3BB422C: ("shell2_texture", structs.decode_BIG_L),
    0x47B4E863: ("shell_color", _decode_shell_color),
    0xE68B1FA8: ("unknown_0xe68b1fa8", _decode_unknown_0xe68b1fa8),
}
