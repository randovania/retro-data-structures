# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class KorakkDataJson(typing_extensions.TypedDict):
        unknown_0x27b15c35: float
        unknown_0x6c6b5700: int
        mouth_vulnerability: json_util.JsonObject
        tongue_damage: json_util.JsonObject
        morphball_bite_damage: json_util.JsonObject
        damage_info_0x77941011: json_util.JsonObject
        damage_info_0x4d07f7b1: json_util.JsonObject
        phazon_lance_damage: json_util.JsonObject
        damage_info_0x8333b35f: json_util.JsonObject
        stab_damage: json_util.JsonObject


@dataclasses.dataclass()
class KorakkData(BaseProperty):
    unknown_0x27b15c35: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x27B15C35, original_name="Unknown"),
        },
    )
    unknown_0x6c6b5700: int = dataclasses.field(
        default=4,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6C6B5700, original_name="Unknown"),
        },
    )
    mouth_vulnerability: DamageVulnerability = dataclasses.field(
        default_factory=DamageVulnerability,
        metadata={
            "reflection": FieldReflection[DamageVulnerability](
                DamageVulnerability,
                id=0xED7EDCA3,
                original_name="MouthVulnerability",
                from_json=DamageVulnerability.from_json,
                to_json=DamageVulnerability.to_json,
            ),
        },
    )
    tongue_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xDA5E9630,
                original_name="TongueDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    morphball_bite_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x508F7177,
                original_name="MorphballBiteDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x77941011: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x77941011,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x4d07f7b1: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x4D07F7B1,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    phazon_lance_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x21A2121D,
                original_name="PhazonLanceDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x8333b35f: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x8333B35F,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    stab_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x946016A9,
                original_name="StabDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
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
        if property_count != 10:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27B15C35
        unknown_0x27b15c35 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6C6B5700
        unknown_0x6c6b5700 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xED7EDCA3
        mouth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDA5E9630
        tongue_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x508F7177
        morphball_bite_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77941011
        damage_info_0x77941011 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D07F7B1
        damage_info_0x4d07f7b1 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21A2121D
        phazon_lance_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8333B35F
        damage_info_0x8333b35f = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x946016A9
        stab_damage = DamageInfo.from_stream(data, game, property_size)

        return cls(
            unknown_0x27b15c35,
            unknown_0x6c6b5700,
            mouth_vulnerability,
            tongue_damage,
            morphball_bite_damage,
            damage_info_0x77941011,
            damage_info_0x4d07f7b1,
            phazon_lance_damage,
            damage_info_0x8333b35f,
            stab_damage,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"'\xb1\\5")  # 0x27b15c35
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x27b15c35))

        data.write(b"lkW\x00")  # 0x6c6b5700
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6c6b5700))

        data.write(b"\xed~\xdc\xa3")  # 0xed7edca3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.mouth_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xda^\x960")  # 0xda5e9630
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.tongue_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"P\x8fqw")  # 0x508f7177
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.morphball_bite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\x94\x10\x11")  # 0x77941011
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x77941011.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"M\x07\xf7\xb1")  # 0x4d07f7b1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x4d07f7b1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"!\xa2\x12\x1d")  # 0x21a2121d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.phazon_lance_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x833\xb3_")  # 0x8333b35f
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x8333b35f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x94`\x16\xa9")  # 0x946016a9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.stab_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KorakkDataJson", data)
        return cls(
            unknown_0x27b15c35=json_data["unknown_0x27b15c35"],
            unknown_0x6c6b5700=json_data["unknown_0x6c6b5700"],
            mouth_vulnerability=DamageVulnerability.from_json(json_data["mouth_vulnerability"]),
            tongue_damage=DamageInfo.from_json(json_data["tongue_damage"]),
            morphball_bite_damage=DamageInfo.from_json(json_data["morphball_bite_damage"]),
            damage_info_0x77941011=DamageInfo.from_json(json_data["damage_info_0x77941011"]),
            damage_info_0x4d07f7b1=DamageInfo.from_json(json_data["damage_info_0x4d07f7b1"]),
            phazon_lance_damage=DamageInfo.from_json(json_data["phazon_lance_damage"]),
            damage_info_0x8333b35f=DamageInfo.from_json(json_data["damage_info_0x8333b35f"]),
            stab_damage=DamageInfo.from_json(json_data["stab_damage"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x27b15c35": self.unknown_0x27b15c35,
            "unknown_0x6c6b5700": self.unknown_0x6c6b5700,
            "mouth_vulnerability": self.mouth_vulnerability.to_json(),
            "tongue_damage": self.tongue_damage.to_json(),
            "morphball_bite_damage": self.morphball_bite_damage.to_json(),
            "damage_info_0x77941011": self.damage_info_0x77941011.to_json(),
            "damage_info_0x4d07f7b1": self.damage_info_0x4d07f7b1.to_json(),
            "phazon_lance_damage": self.phazon_lance_damage.to_json(),
            "damage_info_0x8333b35f": self.damage_info_0x8333b35f.to_json(),
            "stab_damage": self.stab_damage.to_json(),
        }


def _decode_mouth_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_tongue_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_morphball_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x77941011(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x4d07f7b1(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_lance_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x8333b35f(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_stab_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x27B15C35: ("unknown_0x27b15c35", structs.decode_BIG_f),
    0x6C6B5700: ("unknown_0x6c6b5700", structs.decode_BIG_l),
    0xED7EDCA3: ("mouth_vulnerability", _decode_mouth_vulnerability),
    0xDA5E9630: ("tongue_damage", _decode_tongue_damage),
    0x508F7177: ("morphball_bite_damage", _decode_morphball_bite_damage),
    0x77941011: ("damage_info_0x77941011", _decode_damage_info_0x77941011),
    0x4D07F7B1: ("damage_info_0x4d07f7b1", _decode_damage_info_0x4d07f7b1),
    0x21A2121D: ("phazon_lance_damage", _decode_phazon_lance_damage),
    0x8333B35F: ("damage_info_0x8333b35f", _decode_damage_info_0x8333b35f),
    0x946016A9: ("stab_damage", _decode_stab_damage),
}
