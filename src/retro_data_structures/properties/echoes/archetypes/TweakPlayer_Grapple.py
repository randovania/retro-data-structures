# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.common.archetypes.TweakPlayer_GrappleBeam import TweakPlayer_GrappleBeam
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class TweakPlayer_GrappleJson(typing_extensions.TypedDict):
        grapple_distance: float
        grapple_beam_length: float
        grapple_swing_time: float
        grapple_max_velocity: float
        grapple_camera_speed: float
        grapple_pull_close_distance: float
        grapple_pull_dampen_distance: float
        grapple_pull_velocity: float
        grapple_pull_camera_speed: float
        grapple_turn_rate: float
        grapple_jump_force: float
        grapple_release_time: float
        grapple_control_scheme: int
        grapple_hold_orbit_button: bool
        grapple_turn_controls_reversed: bool
        beam: json_util.JsonObject


@dataclasses.dataclass()
class TweakPlayer_Grapple(BaseProperty):
    grapple_distance: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA726316B, original_name="GrappleDistance"),
        },
    )
    grapple_beam_length: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x33E79B51, original_name="GrappleBeamLength"),
        },
    )
    grapple_swing_time: float = dataclasses.field(
        default=3.299999952316284,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9DD3E88B, original_name="GrappleSwingTime"),
        },
    )
    grapple_max_velocity: float = dataclasses.field(
        default=23.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFB605BA4, original_name="GrappleMaxVelocity"),
        },
    )
    grapple_camera_speed: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFE98B8E9, original_name="GrappleCameraSpeed"),
        },
    )
    grapple_pull_close_distance: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9210A25E, original_name="GrapplePullCloseDistance"),
        },
    )
    grapple_pull_dampen_distance: float = dataclasses.field(
        default=2.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBE0C8B5E, original_name="GrapplePullDampenDistance"),
        },
    )
    grapple_pull_velocity: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2603A0BE, original_name="GrapplePullVelocity"),
        },
    )
    grapple_pull_camera_speed: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5B98A3BD, original_name="GrapplePullCameraSpeed"),
        },
    )
    grapple_turn_rate: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x87D4B5D6, original_name="GrappleTurnRate"),
        },
    )
    grapple_jump_force: float = dataclasses.field(
        default=13.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB7F82A9F, original_name="GrappleJumpForce"),
        },
    )
    grapple_release_time: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x395478A8, original_name="GrappleReleaseTime"),
        },
    )
    grapple_control_scheme: int = dataclasses.field(
        default=2,
        metadata={
            "reflection": FieldReflection[int](int, id=0x93C013C9, original_name="GrappleControlScheme"),
        },
    )
    grapple_hold_orbit_button: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x8EEED636, original_name="GrappleHoldOrbitButton"),
        },
    )
    grapple_turn_controls_reversed: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE1EB12E2, original_name="GrappleTurnControlsReversed"),
        },
    )
    beam: TweakPlayer_GrappleBeam = dataclasses.field(
        default_factory=TweakPlayer_GrappleBeam,
        metadata={
            "reflection": FieldReflection[TweakPlayer_GrappleBeam](
                TweakPlayer_GrappleBeam,
                id=0xAE1FC47C,
                original_name="Beam",
                from_json=TweakPlayer_GrappleBeam.from_json,
                to_json=TweakPlayer_GrappleBeam.to_json,
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
        if property_count != 16:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA726316B
        grapple_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33E79B51
        grapple_beam_length = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9DD3E88B
        grapple_swing_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFB605BA4
        grapple_max_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFE98B8E9
        grapple_camera_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9210A25E
        grapple_pull_close_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE0C8B5E
        grapple_pull_dampen_distance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2603A0BE
        grapple_pull_velocity = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5B98A3BD
        grapple_pull_camera_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87D4B5D6
        grapple_turn_rate = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB7F82A9F
        grapple_jump_force = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x395478A8
        grapple_release_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93C013C9
        grapple_control_scheme = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8EEED636
        grapple_hold_orbit_button = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE1EB12E2
        grapple_turn_controls_reversed = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAE1FC47C
        beam = TweakPlayer_GrappleBeam.from_stream(data, game, property_size)

        return cls(
            grapple_distance,
            grapple_beam_length,
            grapple_swing_time,
            grapple_max_velocity,
            grapple_camera_speed,
            grapple_pull_close_distance,
            grapple_pull_dampen_distance,
            grapple_pull_velocity,
            grapple_pull_camera_speed,
            grapple_turn_rate,
            grapple_jump_force,
            grapple_release_time,
            grapple_control_scheme,
            grapple_hold_orbit_button,
            grapple_turn_controls_reversed,
            beam,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x10")  # 16 properties

        data.write(b"\xa7&1k")  # 0xa726316b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_distance))

        data.write(b"3\xe7\x9bQ")  # 0x33e79b51
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_beam_length))

        data.write(b"\x9d\xd3\xe8\x8b")  # 0x9dd3e88b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_swing_time))

        data.write(b"\xfb`[\xa4")  # 0xfb605ba4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_max_velocity))

        data.write(b"\xfe\x98\xb8\xe9")  # 0xfe98b8e9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_camera_speed))

        data.write(b"\x92\x10\xa2^")  # 0x9210a25e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_pull_close_distance))

        data.write(b"\xbe\x0c\x8b^")  # 0xbe0c8b5e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_pull_dampen_distance))

        data.write(b"&\x03\xa0\xbe")  # 0x2603a0be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_pull_velocity))

        data.write(b"[\x98\xa3\xbd")  # 0x5b98a3bd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_pull_camera_speed))

        data.write(b"\x87\xd4\xb5\xd6")  # 0x87d4b5d6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_turn_rate))

        data.write(b"\xb7\xf8*\x9f")  # 0xb7f82a9f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_jump_force))

        data.write(b"9Tx\xa8")  # 0x395478a8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.grapple_release_time))

        data.write(b"\x93\xc0\x13\xc9")  # 0x93c013c9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.grapple_control_scheme))

        data.write(b"\x8e\xee\xd66")  # 0x8eeed636
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.grapple_hold_orbit_button))

        data.write(b"\xe1\xeb\x12\xe2")  # 0xe1eb12e2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.grapple_turn_controls_reversed))

        data.write(b"\xae\x1f\xc4|")  # 0xae1fc47c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_GrappleJson", data)
        return cls(
            grapple_distance=json_data["grapple_distance"],
            grapple_beam_length=json_data["grapple_beam_length"],
            grapple_swing_time=json_data["grapple_swing_time"],
            grapple_max_velocity=json_data["grapple_max_velocity"],
            grapple_camera_speed=json_data["grapple_camera_speed"],
            grapple_pull_close_distance=json_data["grapple_pull_close_distance"],
            grapple_pull_dampen_distance=json_data["grapple_pull_dampen_distance"],
            grapple_pull_velocity=json_data["grapple_pull_velocity"],
            grapple_pull_camera_speed=json_data["grapple_pull_camera_speed"],
            grapple_turn_rate=json_data["grapple_turn_rate"],
            grapple_jump_force=json_data["grapple_jump_force"],
            grapple_release_time=json_data["grapple_release_time"],
            grapple_control_scheme=json_data["grapple_control_scheme"],
            grapple_hold_orbit_button=json_data["grapple_hold_orbit_button"],
            grapple_turn_controls_reversed=json_data["grapple_turn_controls_reversed"],
            beam=TweakPlayer_GrappleBeam.from_json(json_data["beam"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "grapple_distance": self.grapple_distance,
            "grapple_beam_length": self.grapple_beam_length,
            "grapple_swing_time": self.grapple_swing_time,
            "grapple_max_velocity": self.grapple_max_velocity,
            "grapple_camera_speed": self.grapple_camera_speed,
            "grapple_pull_close_distance": self.grapple_pull_close_distance,
            "grapple_pull_dampen_distance": self.grapple_pull_dampen_distance,
            "grapple_pull_velocity": self.grapple_pull_velocity,
            "grapple_pull_camera_speed": self.grapple_pull_camera_speed,
            "grapple_turn_rate": self.grapple_turn_rate,
            "grapple_jump_force": self.grapple_jump_force,
            "grapple_release_time": self.grapple_release_time,
            "grapple_control_scheme": self.grapple_control_scheme,
            "grapple_hold_orbit_button": self.grapple_hold_orbit_button,
            "grapple_turn_controls_reversed": self.grapple_turn_controls_reversed,
            "beam": self.beam.to_json(),
        }


def _decode_beam(data: typing.BinaryIO, game: Game, property_size: int) -> TweakPlayer_GrappleBeam:
    return TweakPlayer_GrappleBeam.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA726316B: ("grapple_distance", structs.decode_BIG_f),
    0x33E79B51: ("grapple_beam_length", structs.decode_BIG_f),
    0x9DD3E88B: ("grapple_swing_time", structs.decode_BIG_f),
    0xFB605BA4: ("grapple_max_velocity", structs.decode_BIG_f),
    0xFE98B8E9: ("grapple_camera_speed", structs.decode_BIG_f),
    0x9210A25E: ("grapple_pull_close_distance", structs.decode_BIG_f),
    0xBE0C8B5E: ("grapple_pull_dampen_distance", structs.decode_BIG_f),
    0x2603A0BE: ("grapple_pull_velocity", structs.decode_BIG_f),
    0x5B98A3BD: ("grapple_pull_camera_speed", structs.decode_BIG_f),
    0x87D4B5D6: ("grapple_turn_rate", structs.decode_BIG_f),
    0xB7F82A9F: ("grapple_jump_force", structs.decode_BIG_f),
    0x395478A8: ("grapple_release_time", structs.decode_BIG_f),
    0x93C013C9: ("grapple_control_scheme", structs.decode_BIG_l),
    0x8EEED636: ("grapple_hold_orbit_button", structs.decode_BIG_bool_),
    0xE1EB12E2: ("grapple_turn_controls_reversed", structs.decode_BIG_bool_),
    0xAE1FC47C: ("beam", _decode_beam),
}
