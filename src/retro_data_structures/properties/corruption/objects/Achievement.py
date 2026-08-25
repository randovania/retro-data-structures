# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.BonusCredit import BonusCredit
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class AchievementJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        bonus_credit: json_util.JsonObject
        achievement: int
        normal_difficulty: bool
        hard_difficulty: bool
        elite_difficulty: bool
        bonus_credit_string: int


class AchievementEnum(enum.IntEnum):
    Unknown1 = 1290095210
    Unknown2 = 1741167017
    Unknown3 = 1941731395
    Unknown4 = 1847676886
    Unknown5 = 42311112
    Unknown6 = 2302821108
    Unknown7 = 3685060452
    Unknown8 = 2575337497
    Unknown9 = 977778753
    Unknown10 = 1741569191
    Unknown11 = 3796894174
    Unknown12 = 2288784460
    Unknown13 = 2046095677
    Unknown14 = 3347275427
    Unknown15 = 1815168570
    Unknown16 = 1015929027
    Unknown17 = 105107473
    Unknown18 = 80518716
    Unknown19 = 1831985480
    Unknown20 = 1831093832
    Unknown21 = 4096595954
    Unknown22 = 2200577892
    Unknown23 = 1437187765
    Unknown24 = 291959200
    Unknown25 = 3841084878
    Unknown26 = 3936228971
    Unknown27 = 246361685
    Unknown28 = 761891303
    Unknown29 = 3831947482
    Unknown30 = 1643699619
    Unknown31 = 1845492504
    Unknown32 = 3065393673
    Unknown33 = 2316897795
    Unknown34 = 3682273482
    Unknown35 = 2320145227
    Unknown36 = 2373462654
    Unknown37 = 2327213834
    Unknown38 = 3078454223
    Unknown39 = 923107635
    Unknown40 = 964468362
    Unknown41 = 3917812391
    Unknown42 = 3278886900
    Unknown43 = 1516668494
    Unknown44 = 761378520
    Unknown45 = 3986936146
    Unknown46 = 311100150
    Unknown47 = 1276826815
    Unknown48 = 3582734640
    Unknown49 = 159852610
    Unknown50 = 3670289904
    Unknown51 = 3035079377
    Unknown52 = 2621245633
    Unknown53 = 87316859
    Unknown54 = 1915972077
    Unknown55 = 3965189198
    Unknown56 = 675653541
    Unknown57 = 1583013528
    Unknown58 = 3845519601
    Unknown59 = 1020841902
    Unknown60 = 2754677268
    Unknown61 = 2238270125
    Unknown62 = 2159809142
    Unknown63 = 3026027834
    Unknown64 = 1534640759
    Unknown65 = 260599856
    Unknown66 = 118390863
    Unknown67 = 1657177142
    Unknown68 = 1896894749
    Unknown69 = 3803117518
    Unknown70 = 1923499191
    Unknown71 = 2458173973
    Unknown72 = 335555508
    Unknown73 = 3394623414
    Unknown74 = 800279568
    Unknown75 = 392796523
    Unknown76 = 3511454777
    Unknown77 = 1611981353
    Unknown78 = 1331676611
    Unknown79 = 4154542500
    Unknown80 = 3931564681
    Unknown81 = 380595334
    Unknown82 = 470973530
    Unknown83 = 2698926786
    Unknown84 = 2439373502

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class Achievement(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(
        default_factory=EditorProperties,
        metadata={
            "reflection": FieldReflection[EditorProperties](
                EditorProperties,
                id=0x255A4580,
                original_name="EditorProperties",
                from_json=EditorProperties.from_json,
                to_json=EditorProperties.to_json,
            ),
        },
    )
    bonus_credit: BonusCredit = dataclasses.field(
        default_factory=BonusCredit,
        metadata={
            "reflection": FieldReflection[BonusCredit](
                BonusCredit,
                id=0x7AAC9E22,
                original_name="BonusCredit",
                from_json=BonusCredit.from_json,
                to_json=BonusCredit.to_json,
            ),
        },
    )
    achievement: AchievementEnum = dataclasses.field(
        default=AchievementEnum.Unknown84,
        metadata={
            "reflection": FieldReflection[AchievementEnum](
                AchievementEnum,
                id=0x058D2DDB,
                original_name="Achievement",
                from_json=AchievementEnum.from_json,
                to_json=AchievementEnum.to_json,
            ),
        },
    )
    normal_difficulty: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x974F4AA1, original_name="NormalDifficulty"),
        },
    )
    hard_difficulty: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0F8CF6FF, original_name="HardDifficulty"),
        },
    )
    elite_difficulty: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x9B8903EB, original_name="EliteDifficulty"),
        },
    )
    bonus_credit_string: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["STRG"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD6A0CFF1, original_name="BonusCreditString"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "ACHI"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_ScriptAchievement.rso"]

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 7:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7AAC9E22
        bonus_credit = BonusCredit.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x058D2DDB
        achievement = AchievementEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x974F4AA1
        normal_difficulty = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0F8CF6FF
        hard_difficulty = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9B8903EB
        elite_difficulty = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6A0CFF1
        bonus_credit_string = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            editor_properties,
            bonus_credit,
            achievement,
            normal_difficulty,
            hard_difficulty,
            elite_difficulty,
            bonus_credit_string,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x07")  # 7 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'z\xac\x9e"')  # 0x7aac9e22
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.bonus_credit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x05\x8d-\xdb")  # 0x58d2ddb
        data.write(b"\x00\x04")  # size
        self.achievement.to_stream(data, game)

        data.write(b"\x97OJ\xa1")  # 0x974f4aa1
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.normal_difficulty))

        data.write(b"\x0f\x8c\xf6\xff")  # 0xf8cf6ff
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.hard_difficulty))

        data.write(b"\x9b\x89\x03\xeb")  # 0x9b8903eb
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.elite_difficulty))

        data.write(b"\xd6\xa0\xcf\xf1")  # 0xd6a0cff1
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.bonus_credit_string))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AchievementJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            bonus_credit=BonusCredit.from_json(json_data["bonus_credit"]),
            achievement=AchievementEnum.from_json(json_data["achievement"]),
            normal_difficulty=json_data["normal_difficulty"],
            hard_difficulty=json_data["hard_difficulty"],
            elite_difficulty=json_data["elite_difficulty"],
            bonus_credit_string=json_data["bonus_credit_string"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "bonus_credit": self.bonus_credit.to_json(),
            "achievement": self.achievement.to_json(),
            "normal_difficulty": self.normal_difficulty,
            "hard_difficulty": self.hard_difficulty,
            "elite_difficulty": self.elite_difficulty,
            "bonus_credit_string": self.bonus_credit_string,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_bonus_credit(data: typing.BinaryIO, game: Game, property_size: int) -> BonusCredit:
    return BonusCredit.from_stream(data, game, property_size)


def _decode_achievement(data: typing.BinaryIO, game: Game, property_size: int) -> AchievementEnum:
    return AchievementEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x7AAC9E22: ("bonus_credit", _decode_bonus_credit),
    0x058D2DDB: ("achievement", _decode_achievement),
    0x974F4AA1: ("normal_difficulty", structs.decode_BIG_bool_),
    0x0F8CF6FF: ("hard_difficulty", structs.decode_BIG_bool_),
    0x9B8903EB: ("elite_difficulty", structs.decode_BIG_bool_),
    0xD6A0CFF1: ("bonus_credit_string", structs.decode_BIG_Q),
}
