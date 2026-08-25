# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class MetroidHopperStructJson(typing_extensions.TypedDict):
        hypermode_shockwave: json_util.JsonObject
        hypermode_chance: float
        hypermode_duration: float
        hypermode_delay: float
        hyper_mode_initial_delay: float
        hypermode_vulnerability: json_util.JsonObject


@dataclasses.dataclass()
class MetroidHopperStruct(BaseProperty):
    hypermode_shockwave: ShockWaveInfo = dataclasses.field(
        default_factory=ShockWaveInfo,
        metadata={
            "reflection": FieldReflection[ShockWaveInfo](
                ShockWaveInfo,
                id=0xF8E45E84,
                original_name="HypermodeShockwave",
                from_json=ShockWaveInfo.from_json,
                to_json=ShockWaveInfo.to_json,
            ),
        },
    )
    hypermode_chance: float = dataclasses.field(
        default=0.10000000149011612,
        metadata={
            "reflection": FieldReflection[float](float, id=0x1CA04D70, original_name="HypermodeChance"),
        },
    )
    hypermode_duration: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D508CA7, original_name="HypermodeDuration"),
        },
    )
    hypermode_delay: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC9BA4746, original_name="HypermodeDelay"),
        },
    )
    hyper_mode_initial_delay: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE174F463, original_name="HyperModeInitialDelay"),
        },
    )
    hypermode_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xD1522831,
                original_name="HypermodeVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
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
        if property_count != 6:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF8E45E84
        hypermode_shockwave = ShockWaveInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1CA04D70
        hypermode_chance = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8D508CA7
        hypermode_duration = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC9BA4746
        hypermode_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE174F463
        hyper_mode_initial_delay = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1522831
        hypermode_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        return cls(
            hypermode_shockwave,
            hypermode_chance,
            hypermode_duration,
            hypermode_delay,
            hyper_mode_initial_delay,
            hypermode_vulnerability,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x06")  # 6 properties

        data.write(b"\xf8\xe4^\x84")  # 0xf8e45e84
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hypermode_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1c\xa0Mp")  # 0x1ca04d70
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hypermode_chance))

        data.write(b"\x8dP\x8c\xa7")  # 0x8d508ca7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hypermode_duration))

        data.write(b"\xc9\xbaGF")  # 0xc9ba4746
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hypermode_delay))

        data.write(b"\xe1t\xf4c")  # 0xe174f463
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_initial_delay))

        data.write(b"\xd1R(1")  # 0xd1522831
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.hypermode_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidHopperStructJson", data)
        return cls(
            hypermode_shockwave=ShockWaveInfo.from_json(json_data["hypermode_shockwave"]),
            hypermode_chance=json_data["hypermode_chance"],
            hypermode_duration=json_data["hypermode_duration"],
            hypermode_delay=json_data["hypermode_delay"],
            hyper_mode_initial_delay=json_data["hyper_mode_initial_delay"],
            hypermode_vulnerability=DamageVulnerability.from_json(json_data["hypermode_vulnerability"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "hypermode_shockwave": self.hypermode_shockwave.to_json(),
            "hypermode_chance": self.hypermode_chance,
            "hypermode_duration": self.hypermode_duration,
            "hypermode_delay": self.hypermode_delay,
            "hyper_mode_initial_delay": self.hyper_mode_initial_delay,
            "hypermode_vulnerability": self.hypermode_vulnerability.to_json(),
        }


def _decode_hypermode_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_hypermode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xF8E45E84: ("hypermode_shockwave", _decode_hypermode_shockwave),
    0x1CA04D70: ("hypermode_chance", structs.decode_BIG_f),
    0x8D508CA7: ("hypermode_duration", structs.decode_BIG_f),
    0xC9BA4746: ("hypermode_delay", structs.decode_BIG_f),
    0xE174F463: ("hyper_mode_initial_delay", structs.decode_BIG_f),
    0xD1522831: ("hypermode_vulnerability", _decode_hypermode_vulnerability),
}
