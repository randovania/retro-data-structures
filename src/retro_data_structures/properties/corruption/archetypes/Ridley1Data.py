# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class Ridley1DataJson(typing_extensions.TypedDict):
        unknown_0xa0460b5e: float
        unknown_0xf33b0dd4: float
        unknown_0xa59260dd: float
        unknown_0x5bbdbc45: float
        unknown_0xbc1564b9: float
        damage_info_0xe82166db: json_util.JsonObject
        below_beam_damage: json_util.JsonObject
        unknown_0xf616d87b: float
        below_bite_damage: json_util.JsonObject
        damage_info_0x54031e21: json_util.JsonObject
        unknown_0xb5194095: float
        in_hand_bite_damage: json_util.JsonObject
        unknown_0xddd0212a: float
        damage_info_0x6bb8e35c: json_util.JsonObject
        unknown_0xf4c13980: float
        in_hand_slap_damage: json_util.JsonObject
        unknown_0xa4cb7b3c: float
        damage_info_0x742287f5: json_util.JsonObject
        unknown_0xbe3b8e93: float
        damage_info_0x78f4a916: json_util.JsonObject
        damage_info_0x76f0f23b: json_util.JsonObject
        damage_info_0x77edd892: json_util.JsonObject
        above_missile_damage: json_util.JsonObject
        above_fireball_damage: json_util.JsonObject
        unknown_0x4fa2bce1: float


@dataclasses.dataclass()
class Ridley1Data(BaseProperty):
    unknown_0xa0460b5e: float = dataclasses.field(
        default=90.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA0460B5E, original_name="Unknown"),
        },
    )
    unknown_0xf33b0dd4: float = dataclasses.field(
        default=65.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF33B0DD4, original_name="Unknown"),
        },
    )
    unknown_0xa59260dd: float = dataclasses.field(
        default=60.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA59260DD, original_name="Unknown"),
        },
    )
    unknown_0x5bbdbc45: float = dataclasses.field(
        default=35.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5BBDBC45, original_name="Unknown"),
        },
    )
    unknown_0xbc1564b9: float = dataclasses.field(
        default=1000.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC1564B9, original_name="Unknown"),
        },
    )
    damage_info_0xe82166db: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xE82166DB,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    below_beam_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x36307B98,
                original_name="BelowBeamDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xf616d87b: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF616D87B, original_name="Unknown"),
        },
    )
    below_bite_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xFAB0199E,
                original_name="BelowBiteDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x54031e21: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x54031E21,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xb5194095: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5194095, original_name="Unknown"),
        },
    )
    in_hand_bite_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xD55917A9,
                original_name="InHandBiteDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xddd0212a: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDDD0212A, original_name="Unknown"),
        },
    )
    damage_info_0x6bb8e35c: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x6BB8E35C,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xf4c13980: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF4C13980, original_name="Unknown"),
        },
    )
    in_hand_slap_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x47D4427E,
                original_name="InHandSlapDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xa4cb7b3c: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA4CB7B3C, original_name="Unknown"),
        },
    )
    damage_info_0x742287f5: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x742287F5,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0xbe3b8e93: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBE3B8E93, original_name="Unknown"),
        },
    )
    damage_info_0x78f4a916: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x78F4A916,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x76f0f23b: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x76F0F23B,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    damage_info_0x77edd892: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x77EDD892,
                original_name="DamageInfo",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    above_missile_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0xB6C739D2,
                original_name="AboveMissileDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    above_fireball_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x79350AC0,
                original_name="AboveFireballDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    unknown_0x4fa2bce1: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4FA2BCE1, original_name="Unknown"),
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
        if property_count != 25:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA0460B5E
        unknown_0xa0460b5e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF33B0DD4
        unknown_0xf33b0dd4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA59260DD
        unknown_0xa59260dd = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5BBDBC45
        unknown_0x5bbdbc45 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC1564B9
        unknown_0xbc1564b9 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE82166DB
        damage_info_0xe82166db = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36307B98
        below_beam_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF616D87B
        unknown_0xf616d87b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFAB0199E
        below_bite_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54031E21
        damage_info_0x54031e21 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5194095
        unknown_0xb5194095 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD55917A9
        in_hand_bite_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDDD0212A
        unknown_0xddd0212a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6BB8E35C
        damage_info_0x6bb8e35c = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF4C13980
        unknown_0xf4c13980 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47D4427E
        in_hand_slap_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4CB7B3C
        unknown_0xa4cb7b3c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742287F5
        damage_info_0x742287f5 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE3B8E93
        unknown_0xbe3b8e93 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78F4A916
        damage_info_0x78f4a916 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76F0F23B
        damage_info_0x76f0f23b = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77EDD892
        damage_info_0x77edd892 = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB6C739D2
        above_missile_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79350AC0
        above_fireball_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4FA2BCE1
        unknown_0x4fa2bce1 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            unknown_0xa0460b5e,
            unknown_0xf33b0dd4,
            unknown_0xa59260dd,
            unknown_0x5bbdbc45,
            unknown_0xbc1564b9,
            damage_info_0xe82166db,
            below_beam_damage,
            unknown_0xf616d87b,
            below_bite_damage,
            damage_info_0x54031e21,
            unknown_0xb5194095,
            in_hand_bite_damage,
            unknown_0xddd0212a,
            damage_info_0x6bb8e35c,
            unknown_0xf4c13980,
            in_hand_slap_damage,
            unknown_0xa4cb7b3c,
            damage_info_0x742287f5,
            unknown_0xbe3b8e93,
            damage_info_0x78f4a916,
            damage_info_0x76f0f23b,
            damage_info_0x77edd892,
            above_missile_damage,
            above_fireball_damage,
            unknown_0x4fa2bce1,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x19")  # 25 properties

        data.write(b"\xa0F\x0b^")  # 0xa0460b5e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa0460b5e))

        data.write(b"\xf3;\r\xd4")  # 0xf33b0dd4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf33b0dd4))

        data.write(b"\xa5\x92`\xdd")  # 0xa59260dd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa59260dd))

        data.write(b"[\xbd\xbcE")  # 0x5bbdbc45
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5bbdbc45))

        data.write(b"\xbc\x15d\xb9")  # 0xbc1564b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc1564b9))

        data.write(b"\xe8!f\xdb")  # 0xe82166db
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0xe82166db.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"60{\x98")  # 0x36307b98
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.below_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf6\x16\xd8{")  # 0xf616d87b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf616d87b))

        data.write(b"\xfa\xb0\x19\x9e")  # 0xfab0199e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.below_bite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"T\x03\x1e!")  # 0x54031e21
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x54031e21.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb5\x19@\x95")  # 0xb5194095
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5194095))

        data.write(b"\xd5Y\x17\xa9")  # 0xd55917a9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.in_hand_bite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xdd\xd0!*")  # 0xddd0212a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xddd0212a))

        data.write(b"k\xb8\xe3\\")  # 0x6bb8e35c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x6bb8e35c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf4\xc19\x80")  # 0xf4c13980
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf4c13980))

        data.write(b"G\xd4B~")  # 0x47d4427e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.in_hand_slap_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa4\xcb{<")  # 0xa4cb7b3c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa4cb7b3c))

        data.write(b't"\x87\xf5')  # 0x742287f5
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x742287f5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbe;\x8e\x93")  # 0xbe3b8e93
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbe3b8e93))

        data.write(b"x\xf4\xa9\x16")  # 0x78f4a916
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x78f4a916.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"v\xf0\xf2;")  # 0x76f0f23b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x76f0f23b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"w\xed\xd8\x92")  # 0x77edd892
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.damage_info_0x77edd892.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb6\xc79\xd2")  # 0xb6c739d2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.above_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"y5\n\xc0")  # 0x79350ac0
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.above_fireball_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"O\xa2\xbc\xe1")  # 0x4fa2bce1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4fa2bce1))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("Ridley1DataJson", data)
        return cls(
            unknown_0xa0460b5e=json_data["unknown_0xa0460b5e"],
            unknown_0xf33b0dd4=json_data["unknown_0xf33b0dd4"],
            unknown_0xa59260dd=json_data["unknown_0xa59260dd"],
            unknown_0x5bbdbc45=json_data["unknown_0x5bbdbc45"],
            unknown_0xbc1564b9=json_data["unknown_0xbc1564b9"],
            damage_info_0xe82166db=DamageInfo.from_json(json_data["damage_info_0xe82166db"]),
            below_beam_damage=DamageInfo.from_json(json_data["below_beam_damage"]),
            unknown_0xf616d87b=json_data["unknown_0xf616d87b"],
            below_bite_damage=DamageInfo.from_json(json_data["below_bite_damage"]),
            damage_info_0x54031e21=DamageInfo.from_json(json_data["damage_info_0x54031e21"]),
            unknown_0xb5194095=json_data["unknown_0xb5194095"],
            in_hand_bite_damage=DamageInfo.from_json(json_data["in_hand_bite_damage"]),
            unknown_0xddd0212a=json_data["unknown_0xddd0212a"],
            damage_info_0x6bb8e35c=DamageInfo.from_json(json_data["damage_info_0x6bb8e35c"]),
            unknown_0xf4c13980=json_data["unknown_0xf4c13980"],
            in_hand_slap_damage=DamageInfo.from_json(json_data["in_hand_slap_damage"]),
            unknown_0xa4cb7b3c=json_data["unknown_0xa4cb7b3c"],
            damage_info_0x742287f5=DamageInfo.from_json(json_data["damage_info_0x742287f5"]),
            unknown_0xbe3b8e93=json_data["unknown_0xbe3b8e93"],
            damage_info_0x78f4a916=DamageInfo.from_json(json_data["damage_info_0x78f4a916"]),
            damage_info_0x76f0f23b=DamageInfo.from_json(json_data["damage_info_0x76f0f23b"]),
            damage_info_0x77edd892=DamageInfo.from_json(json_data["damage_info_0x77edd892"]),
            above_missile_damage=DamageInfo.from_json(json_data["above_missile_damage"]),
            above_fireball_damage=DamageInfo.from_json(json_data["above_fireball_damage"]),
            unknown_0x4fa2bce1=json_data["unknown_0x4fa2bce1"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xa0460b5e": self.unknown_0xa0460b5e,
            "unknown_0xf33b0dd4": self.unknown_0xf33b0dd4,
            "unknown_0xa59260dd": self.unknown_0xa59260dd,
            "unknown_0x5bbdbc45": self.unknown_0x5bbdbc45,
            "unknown_0xbc1564b9": self.unknown_0xbc1564b9,
            "damage_info_0xe82166db": self.damage_info_0xe82166db.to_json(),
            "below_beam_damage": self.below_beam_damage.to_json(),
            "unknown_0xf616d87b": self.unknown_0xf616d87b,
            "below_bite_damage": self.below_bite_damage.to_json(),
            "damage_info_0x54031e21": self.damage_info_0x54031e21.to_json(),
            "unknown_0xb5194095": self.unknown_0xb5194095,
            "in_hand_bite_damage": self.in_hand_bite_damage.to_json(),
            "unknown_0xddd0212a": self.unknown_0xddd0212a,
            "damage_info_0x6bb8e35c": self.damage_info_0x6bb8e35c.to_json(),
            "unknown_0xf4c13980": self.unknown_0xf4c13980,
            "in_hand_slap_damage": self.in_hand_slap_damage.to_json(),
            "unknown_0xa4cb7b3c": self.unknown_0xa4cb7b3c,
            "damage_info_0x742287f5": self.damage_info_0x742287f5.to_json(),
            "unknown_0xbe3b8e93": self.unknown_0xbe3b8e93,
            "damage_info_0x78f4a916": self.damage_info_0x78f4a916.to_json(),
            "damage_info_0x76f0f23b": self.damage_info_0x76f0f23b.to_json(),
            "damage_info_0x77edd892": self.damage_info_0x77edd892.to_json(),
            "above_missile_damage": self.above_missile_damage.to_json(),
            "above_fireball_damage": self.above_fireball_damage.to_json(),
            "unknown_0x4fa2bce1": self.unknown_0x4fa2bce1,
        }


def _decode_damage_info_0xe82166db(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_below_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_below_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x54031e21(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_in_hand_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x6bb8e35c(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_in_hand_slap_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x742287f5(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x78f4a916(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x76f0f23b(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info_0x77edd892(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_above_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_above_fireball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xA0460B5E: ("unknown_0xa0460b5e", structs.decode_BIG_f),
    0xF33B0DD4: ("unknown_0xf33b0dd4", structs.decode_BIG_f),
    0xA59260DD: ("unknown_0xa59260dd", structs.decode_BIG_f),
    0x5BBDBC45: ("unknown_0x5bbdbc45", structs.decode_BIG_f),
    0xBC1564B9: ("unknown_0xbc1564b9", structs.decode_BIG_f),
    0xE82166DB: ("damage_info_0xe82166db", _decode_damage_info_0xe82166db),
    0x36307B98: ("below_beam_damage", _decode_below_beam_damage),
    0xF616D87B: ("unknown_0xf616d87b", structs.decode_BIG_f),
    0xFAB0199E: ("below_bite_damage", _decode_below_bite_damage),
    0x54031E21: ("damage_info_0x54031e21", _decode_damage_info_0x54031e21),
    0xB5194095: ("unknown_0xb5194095", structs.decode_BIG_f),
    0xD55917A9: ("in_hand_bite_damage", _decode_in_hand_bite_damage),
    0xDDD0212A: ("unknown_0xddd0212a", structs.decode_BIG_f),
    0x6BB8E35C: ("damage_info_0x6bb8e35c", _decode_damage_info_0x6bb8e35c),
    0xF4C13980: ("unknown_0xf4c13980", structs.decode_BIG_f),
    0x47D4427E: ("in_hand_slap_damage", _decode_in_hand_slap_damage),
    0xA4CB7B3C: ("unknown_0xa4cb7b3c", structs.decode_BIG_f),
    0x742287F5: ("damage_info_0x742287f5", _decode_damage_info_0x742287f5),
    0xBE3B8E93: ("unknown_0xbe3b8e93", structs.decode_BIG_f),
    0x78F4A916: ("damage_info_0x78f4a916", _decode_damage_info_0x78f4a916),
    0x76F0F23B: ("damage_info_0x76f0f23b", _decode_damage_info_0x76f0f23b),
    0x77EDD892: ("damage_info_0x77edd892", _decode_damage_info_0x77edd892),
    0xB6C739D2: ("above_missile_damage", _decode_above_missile_damage),
    0x79350AC0: ("above_fireball_damage", _decode_above_fireball_damage),
    0x4FA2BCE1: ("unknown_0x4fa2bce1", structs.decode_BIG_f),
}
