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

    class TweakPlayerGun_RicochetDamage_FactorJson(typing_extensions.TypedDict):
        power_beam: float
        plasma_beam: float
        nova_beam: float
        phazon_beam: float
        missile: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x5D623269, 0xDB0A9583, 0x3BD757E2, 0xF668C245, 0x1234CD8)


@dataclasses.dataclass()
class TweakPlayerGun_RicochetDamage_Factor(BaseProperty):
    power_beam: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5D623269, original_name="PowerBeam"),
        },
    )
    plasma_beam: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDB0A9583, original_name="PlasmaBeam"),
        },
    )
    nova_beam: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3BD757E2, original_name="NovaBeam"),
        },
    )
    phazon_beam: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF668C245, original_name="PhazonBeam"),
        },
    )
    missile: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x01234CD8, original_name="Missile"),
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
        if property_count != 5:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHfLHfLHfLHf")

        dec = _FAST_FORMAT.unpack(data.read(50))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x05")  # 5 properties

        data.write(b"]b2i")  # 0x5d623269
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.power_beam))

        data.write(b"\xdb\n\x95\x83")  # 0xdb0a9583
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.plasma_beam))

        data.write(b";\xd7W\xe2")  # 0x3bd757e2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.nova_beam))

        data.write(b"\xf6h\xc2E")  # 0xf668c245
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_beam))

        data.write(b"\x01#L\xd8")  # 0x1234cd8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.missile))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_RicochetDamage_FactorJson", data)
        return cls(
            power_beam=json_data["power_beam"],
            plasma_beam=json_data["plasma_beam"],
            nova_beam=json_data["nova_beam"],
            phazon_beam=json_data["phazon_beam"],
            missile=json_data["missile"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "power_beam": self.power_beam,
            "plasma_beam": self.plasma_beam,
            "nova_beam": self.nova_beam,
            "phazon_beam": self.phazon_beam,
            "missile": self.missile,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5D623269: ("power_beam", structs.decode_BIG_f),
    0xDB0A9583: ("plasma_beam", structs.decode_BIG_f),
    0x3BD757E2: ("nova_beam", structs.decode_BIG_f),
    0xF668C245: ("phazon_beam", structs.decode_BIG_f),
    0x01234CD8: ("missile", structs.decode_BIG_f),
}
