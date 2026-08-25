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

    class PlasmaBeamInfoJson(typing_extensions.TypedDict):
        unknown: int
        weapon_system: int
        contact_effect: int
        pulse_effect: int
        beam_texture: int
        glow_texture: int
        length: float
        radius: float
        expansion_speed: float
        life_time: float
        pulse_speed: float
        shutdown_time: float
        contact_effect_scale: float
        pulse_effect_scale: float
        travel_speed: float
        inner_color: json_util.JsonValue
        outer_color: json_util.JsonValue
        beam_streaks: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xFF713AAD,
    0x459AE4A8,
    0x4F387C49,
    0xDDD52E3A,
    0xC6F229C6,
    0x8F1A76C3,
    0xC26C291C,
    0x78C507EB,
    0xEC773D1D,
    0xB02DE555,
    0x5180181E,
    0x72A96252,
    0x855ED9B9,
    0xB8652FE4,
    0x3FED5E52,
    0x1AFB2B73,
    0x9FD338FC,
    0xAEB31AF3,
)


@dataclasses.dataclass()
class PlasmaBeamInfo(BaseProperty):
    unknown: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xFF713AAD, original_name="Unknown"),
        },
    )
    weapon_system: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["WPSC"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x459AE4A8, original_name="WeaponSystem"),
        },
    )
    contact_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4F387C49, original_name="ContactEffect"),
        },
    )
    pulse_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xDDD52E3A, original_name="PulseEffect"),
        },
    )
    beam_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC6F229C6, original_name="BeamTexture"),
        },
    )
    glow_texture: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["TXTR"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x8F1A76C3, original_name="GlowTexture"),
        },
    )
    length: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC26C291C, original_name="Length"),
        },
    )
    radius: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x78C507EB, original_name="Radius"),
        },
    )
    expansion_speed: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEC773D1D, original_name="ExpansionSpeed"),
        },
    )
    life_time: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB02DE555, original_name="LifeTime"),
        },
    )
    pulse_speed: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5180181E, original_name="PulseSpeed"),
        },
    )
    shutdown_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x72A96252, original_name="ShutdownTime"),
        },
    )
    contact_effect_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x855ED9B9, original_name="ContactEffectScale"),
        },
    )
    pulse_effect_scale: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB8652FE4, original_name="PulseEffectScale"),
        },
    )
    travel_speed: float = dataclasses.field(
        default=150.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3FED5E52, original_name="TravelSpeed"),
        },
    )
    inner_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x1AFB2B73, original_name="InnerColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    outer_color: Color = dataclasses.field(
        default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0),
        metadata={
            "reflection": FieldReflection[Color](
                Color, id=0x9FD338FC, original_name="OuterColor", from_json=Color.from_json, to_json=Color.to_json
            ),
        },
    )
    beam_streaks: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xAEB31AF3, original_name="BeamStreaks"),
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
        if property_count != 18:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHLLHLLHLLHLLHLLHfLHfLHfLHfLHfLHfLHfLHfLHfLHffffLHffffLHL")

        dec = _FAST_FORMAT.unpack(data.read(204))
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
            dec[51],
            dec[57],
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
            Color(*dec[47:51]),
            Color(*dec[53:57]),
            dec[59],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x12")  # 18 properties

        data.write(b"\xffq:\xad")  # 0xff713aad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown))

        data.write(b"E\x9a\xe4\xa8")  # 0x459ae4a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.weapon_system))

        data.write(b"O8|I")  # 0x4f387c49
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.contact_effect))

        data.write(b"\xdd\xd5.:")  # 0xddd52e3a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.pulse_effect))

        data.write(b"\xc6\xf2)\xc6")  # 0xc6f229c6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.beam_texture))

        data.write(b"\x8f\x1av\xc3")  # 0x8f1a76c3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.glow_texture))

        data.write(b"\xc2l)\x1c")  # 0xc26c291c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.length))

        data.write(b"x\xc5\x07\xeb")  # 0x78c507eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.radius))

        data.write(b"\xecw=\x1d")  # 0xec773d1d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.expansion_speed))

        data.write(b"\xb0-\xe5U")  # 0xb02de555
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.life_time))

        data.write(b"Q\x80\x18\x1e")  # 0x5180181e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pulse_speed))

        data.write(b"r\xa9bR")  # 0x72a96252
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.shutdown_time))

        data.write(b"\x85^\xd9\xb9")  # 0x855ed9b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.contact_effect_scale))

        data.write(b"\xb8e/\xe4")  # 0xb8652fe4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pulse_effect_scale))

        data.write(b"?\xed^R")  # 0x3fed5e52
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.travel_speed))

        data.write(b"\x1a\xfb+s")  # 0x1afb2b73
        data.write(b"\x00\x10")  # size
        self.inner_color.to_stream(data, game)

        data.write(b"\x9f\xd38\xfc")  # 0x9fd338fc
        data.write(b"\x00\x10")  # size
        self.outer_color.to_stream(data, game)

        data.write(b"\xae\xb3\x1a\xf3")  # 0xaeb31af3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_L.pack(self.beam_streaks))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlasmaBeamInfoJson", data)
        return cls(
            unknown=json_data["unknown"],
            weapon_system=json_data["weapon_system"],
            contact_effect=json_data["contact_effect"],
            pulse_effect=json_data["pulse_effect"],
            beam_texture=json_data["beam_texture"],
            glow_texture=json_data["glow_texture"],
            length=json_data["length"],
            radius=json_data["radius"],
            expansion_speed=json_data["expansion_speed"],
            life_time=json_data["life_time"],
            pulse_speed=json_data["pulse_speed"],
            shutdown_time=json_data["shutdown_time"],
            contact_effect_scale=json_data["contact_effect_scale"],
            pulse_effect_scale=json_data["pulse_effect_scale"],
            travel_speed=json_data["travel_speed"],
            inner_color=Color.from_json(json_data["inner_color"]),
            outer_color=Color.from_json(json_data["outer_color"]),
            beam_streaks=json_data["beam_streaks"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown": self.unknown,
            "weapon_system": self.weapon_system,
            "contact_effect": self.contact_effect,
            "pulse_effect": self.pulse_effect,
            "beam_texture": self.beam_texture,
            "glow_texture": self.glow_texture,
            "length": self.length,
            "radius": self.radius,
            "expansion_speed": self.expansion_speed,
            "life_time": self.life_time,
            "pulse_speed": self.pulse_speed,
            "shutdown_time": self.shutdown_time,
            "contact_effect_scale": self.contact_effect_scale,
            "pulse_effect_scale": self.pulse_effect_scale,
            "travel_speed": self.travel_speed,
            "inner_color": self.inner_color.to_json(),
            "outer_color": self.outer_color.to_json(),
            "beam_streaks": self.beam_streaks,
        }

    def _dependencies_for_weapon_system(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_system)

    def _dependencies_for_contact_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.contact_effect)

    def _dependencies_for_pulse_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pulse_effect)

    def _dependencies_for_beam_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_texture)

    def _dependencies_for_glow_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.glow_texture)

    def _dependencies_for_beam_streaks(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_streaks)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_weapon_system, "weapon_system", "AssetId"),
            (self._dependencies_for_contact_effect, "contact_effect", "AssetId"),
            (self._dependencies_for_pulse_effect, "pulse_effect", "AssetId"),
            (self._dependencies_for_beam_texture, "beam_texture", "AssetId"),
            (self._dependencies_for_glow_texture, "glow_texture", "AssetId"),
            (self._dependencies_for_beam_streaks, "beam_streaks", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for PlasmaBeamInfo.{field_name} ({field_type}): {e}")


def _decode_inner_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_outer_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xFF713AAD: ("unknown", structs.decode_BIG_l),
    0x459AE4A8: ("weapon_system", structs.decode_BIG_L),
    0x4F387C49: ("contact_effect", structs.decode_BIG_L),
    0xDDD52E3A: ("pulse_effect", structs.decode_BIG_L),
    0xC6F229C6: ("beam_texture", structs.decode_BIG_L),
    0x8F1A76C3: ("glow_texture", structs.decode_BIG_L),
    0xC26C291C: ("length", structs.decode_BIG_f),
    0x78C507EB: ("radius", structs.decode_BIG_f),
    0xEC773D1D: ("expansion_speed", structs.decode_BIG_f),
    0xB02DE555: ("life_time", structs.decode_BIG_f),
    0x5180181E: ("pulse_speed", structs.decode_BIG_f),
    0x72A96252: ("shutdown_time", structs.decode_BIG_f),
    0x855ED9B9: ("contact_effect_scale", structs.decode_BIG_f),
    0xB8652FE4: ("pulse_effect_scale", structs.decode_BIG_f),
    0x3FED5E52: ("travel_speed", structs.decode_BIG_f),
    0x1AFB2B73: ("inner_color", _decode_inner_color),
    0x9FD338FC: ("outer_color", _decode_outer_color),
    0xAEB31AF3: ("beam_streaks", structs.decode_BIG_L),
}
