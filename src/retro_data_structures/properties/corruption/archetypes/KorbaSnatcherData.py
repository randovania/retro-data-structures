# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class KorbaSnatcherDataJson(typing_extensions.TypedDict):
        player_attach_distance: float
        unknown_0xa2efcada: int
        unknown_0x37e9d29b: int
        unknown_0xb827744f: float
        unknown_0x010f2e81: float
        unknown_0xf7e350db: float
        morphball_roll_speed_multiplier: float
        unknown_0x05a571a0: float
        unknown_0x8abb2662: float
        unknown_0x04d6c440: float
        korba_death_particle_effect: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0xA350F15A,
    0xA2EFCADA,
    0x37E9D29B,
    0xB827744F,
    0x10F2E81,
    0xF7E350DB,
    0xC7EC3D7B,
    0x5A571A0,
    0x8ABB2662,
    0x4D6C440,
    0x973BF0CA,
)


@dataclasses.dataclass()
class KorbaSnatcherData(BaseProperty):
    player_attach_distance: float = dataclasses.field(
        default=0.800000011920929,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA350F15A, original_name="PlayerAttachDistance"),
        },
    )
    unknown_0xa2efcada: int = dataclasses.field(
        default=5,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA2EFCADA, original_name="Unknown"),
        },
    )
    unknown_0x37e9d29b: int = dataclasses.field(
        default=8,
        metadata={
            "reflection": FieldReflection[int](int, id=0x37E9D29B, original_name="Unknown"),
        },
    )
    unknown_0xb827744f: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB827744F, original_name="Unknown"),
        },
    )
    unknown_0x010f2e81: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x010F2E81, original_name="Unknown"),
        },
    )
    unknown_0xf7e350db: float = dataclasses.field(
        default=2000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF7E350DB, original_name="Unknown"),
        },
    )
    morphball_roll_speed_multiplier: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC7EC3D7B, original_name="MorphballRollSpeedMultiplier"),
        },
    )
    unknown_0x05a571a0: float = dataclasses.field(
        default=0.30000001192092896,
        metadata={
            "reflection": FieldReflection[float](float, id=0x05A571A0, original_name="Unknown"),
        },
    )
    unknown_0x8abb2662: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8ABB2662, original_name="Unknown"),
        },
    )
    unknown_0x04d6c440: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x04D6C440, original_name="Unknown"),
        },
    )
    korba_death_particle_effect: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["PART"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x973BF0CA, original_name="KorbaDeathParticleEffect"),
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
        if property_count != 11:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHfLHlLHlLHfLHfLHfLHfLHfLHfLHfLHQ")

        dec = _FAST_FORMAT.unpack(data.read(114))
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0b")  # 11 properties

        data.write(b"\xa3P\xf1Z")  # 0xa350f15a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.player_attach_distance))

        data.write(b"\xa2\xef\xca\xda")  # 0xa2efcada
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa2efcada))

        data.write(b"7\xe9\xd2\x9b")  # 0x37e9d29b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x37e9d29b))

        data.write(b"\xb8'tO")  # 0xb827744f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb827744f))

        data.write(b"\x01\x0f.\x81")  # 0x10f2e81
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x010f2e81))

        data.write(b"\xf7\xe3P\xdb")  # 0xf7e350db
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf7e350db))

        data.write(b"\xc7\xec={")  # 0xc7ec3d7b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.morphball_roll_speed_multiplier))

        data.write(b"\x05\xa5q\xa0")  # 0x5a571a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x05a571a0))

        data.write(b"\x8a\xbb&b")  # 0x8abb2662
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8abb2662))

        data.write(b"\x04\xd6\xc4@")  # 0x4d6c440
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x04d6c440))

        data.write(b"\x97;\xf0\xca")  # 0x973bf0ca
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.korba_death_particle_effect))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KorbaSnatcherDataJson", data)
        return cls(
            player_attach_distance=json_data["player_attach_distance"],
            unknown_0xa2efcada=json_data["unknown_0xa2efcada"],
            unknown_0x37e9d29b=json_data["unknown_0x37e9d29b"],
            unknown_0xb827744f=json_data["unknown_0xb827744f"],
            unknown_0x010f2e81=json_data["unknown_0x010f2e81"],
            unknown_0xf7e350db=json_data["unknown_0xf7e350db"],
            morphball_roll_speed_multiplier=json_data["morphball_roll_speed_multiplier"],
            unknown_0x05a571a0=json_data["unknown_0x05a571a0"],
            unknown_0x8abb2662=json_data["unknown_0x8abb2662"],
            unknown_0x04d6c440=json_data["unknown_0x04d6c440"],
            korba_death_particle_effect=json_data["korba_death_particle_effect"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "player_attach_distance": self.player_attach_distance,
            "unknown_0xa2efcada": self.unknown_0xa2efcada,
            "unknown_0x37e9d29b": self.unknown_0x37e9d29b,
            "unknown_0xb827744f": self.unknown_0xb827744f,
            "unknown_0x010f2e81": self.unknown_0x010f2e81,
            "unknown_0xf7e350db": self.unknown_0xf7e350db,
            "morphball_roll_speed_multiplier": self.morphball_roll_speed_multiplier,
            "unknown_0x05a571a0": self.unknown_0x05a571a0,
            "unknown_0x8abb2662": self.unknown_0x8abb2662,
            "unknown_0x04d6c440": self.unknown_0x04d6c440,
            "korba_death_particle_effect": self.korba_death_particle_effect,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA350F15A: ("player_attach_distance", structs.decode_BIG_f),
    0xA2EFCADA: ("unknown_0xa2efcada", structs.decode_BIG_l),
    0x37E9D29B: ("unknown_0x37e9d29b", structs.decode_BIG_l),
    0xB827744F: ("unknown_0xb827744f", structs.decode_BIG_f),
    0x010F2E81: ("unknown_0x010f2e81", structs.decode_BIG_f),
    0xF7E350DB: ("unknown_0xf7e350db", structs.decode_BIG_f),
    0xC7EC3D7B: ("morphball_roll_speed_multiplier", structs.decode_BIG_f),
    0x05A571A0: ("unknown_0x05a571a0", structs.decode_BIG_f),
    0x8ABB2662: ("unknown_0x8abb2662", structs.decode_BIG_f),
    0x04D6C440: ("unknown_0x04d6c440", structs.decode_BIG_f),
    0x973BF0CA: ("korba_death_particle_effect", structs.decode_BIG_Q),
}
