# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class HyperModeJson(typing_extensions.TypedDict):
        hyper_mode_tank: bool
        hyper_mode_beam: bool
        hyper_mode_grapple: bool
        hyper_mode_missile: bool
        hyper_mode_ball: bool
        hyper_mode_permanent: bool
        hyper_mode_phaaze: bool
        hyper_mode_original: bool
        hyper_mode_charge: bool


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xACBDA45C, 0x9C30FF96, 0x26A85DF4, 0xE5B6CB66, 0xE981E1EB, 0xFE9B2803, 0xECD5261F, 0x2A05E6D9, 0xC9328BE2)


@dataclasses.dataclass()
class HyperMode(BaseProperty):
    hyper_mode_tank: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xACBDA45C, original_name="HyperModeTank"),
        },
    )
    hyper_mode_beam: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9C30FF96, original_name="HyperModeBeam"),
        },
    )
    hyper_mode_grapple: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x26A85DF4, original_name="HyperModeGrapple"),
        },
    )
    hyper_mode_missile: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE5B6CB66, original_name="HyperModeMissile"),
        },
    )
    hyper_mode_ball: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xE981E1EB, original_name="HyperModeBall"),
        },
    )
    hyper_mode_permanent: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xFE9B2803, original_name="HyperModePermanent"),
        },
    )
    hyper_mode_phaaze: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xECD5261F, original_name="HyperModePhaaze"),
        },
    )
    hyper_mode_original: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2A05E6D9, original_name="HyperModeOriginal"),
        },
    )
    hyper_mode_charge: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC9328BE2, original_name="HyperModeCharge"),
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
        if property_count != 9:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LH?LH?LH?LH?LH?LH?LH?LH?LH?")

        dec = _FAST_FORMAT.unpack(data.read(63))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24]) == _FAST_IDS
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\t")  # 9 properties

        data.write(b"\xac\xbd\xa4\\")  # 0xacbda45c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_tank))

        data.write(b"\x9c0\xff\x96")  # 0x9c30ff96
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_beam))

        data.write(b"&\xa8]\xf4")  # 0x26a85df4
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_grapple))

        data.write(b"\xe5\xb6\xcbf")  # 0xe5b6cb66
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_missile))

        data.write(b"\xe9\x81\xe1\xeb")  # 0xe981e1eb
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_ball))

        data.write(b"\xfe\x9b(\x03")  # 0xfe9b2803
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_permanent))

        data.write(b"\xec\xd5&\x1f")  # 0xecd5261f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_phaaze))

        data.write(b"*\x05\xe6\xd9")  # 0x2a05e6d9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_original))

        data.write(b"\xc92\x8b\xe2")  # 0xc9328be2
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_charge))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("HyperModeJson", data)
        return cls(
            hyper_mode_tank=json_data["hyper_mode_tank"],
            hyper_mode_beam=json_data["hyper_mode_beam"],
            hyper_mode_grapple=json_data["hyper_mode_grapple"],
            hyper_mode_missile=json_data["hyper_mode_missile"],
            hyper_mode_ball=json_data["hyper_mode_ball"],
            hyper_mode_permanent=json_data["hyper_mode_permanent"],
            hyper_mode_phaaze=json_data["hyper_mode_phaaze"],
            hyper_mode_original=json_data["hyper_mode_original"],
            hyper_mode_charge=json_data["hyper_mode_charge"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hyper_mode_tank": self.hyper_mode_tank,
            "hyper_mode_beam": self.hyper_mode_beam,
            "hyper_mode_grapple": self.hyper_mode_grapple,
            "hyper_mode_missile": self.hyper_mode_missile,
            "hyper_mode_ball": self.hyper_mode_ball,
            "hyper_mode_permanent": self.hyper_mode_permanent,
            "hyper_mode_phaaze": self.hyper_mode_phaaze,
            "hyper_mode_original": self.hyper_mode_original,
            "hyper_mode_charge": self.hyper_mode_charge,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xACBDA45C: ("hyper_mode_tank", structs.decode_BIG_bool_),
    0x9C30FF96: ("hyper_mode_beam", structs.decode_BIG_bool_),
    0x26A85DF4: ("hyper_mode_grapple", structs.decode_BIG_bool_),
    0xE5B6CB66: ("hyper_mode_missile", structs.decode_BIG_bool_),
    0xE981E1EB: ("hyper_mode_ball", structs.decode_BIG_bool_),
    0xFE9B2803: ("hyper_mode_permanent", structs.decode_BIG_bool_),
    0xECD5261F: ("hyper_mode_phaaze", structs.decode_BIG_bool_),
    0x2A05E6D9: ("hyper_mode_original", structs.decode_BIG_bool_),
    0xC9328BE2: ("hyper_mode_charge", structs.decode_BIG_bool_),
}
