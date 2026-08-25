# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct41Json(typing_extensions.TypedDict):
        unknown_0xea4b88c8: float
        unknown_0xaa04f0be: float
        unknown_0x59f8b6d0: float
        unknown_0x460020aa: float
        unknown_0x353abf40: float
        caud_0x2822a8fa: int
        caud_0x95d26130: int
        unknown_0xbfb8336b: json_util.JsonObject
        unknown_0xf79adca8: json_util.JsonObject
        unknown_0x68454cb4: float
        beam_sweep: json_util.JsonObject
        beam_sweep2: json_util.JsonObject
        unknown_0xb2671c2a: int
        beam_track_speed: float
        beam_cancel_range: float
        beam_cancel_time: float
        jump_min_range: float
        jump_max_range: float
        unknown_0xb619c33a: float
        missile_min_range: float
        unknown_0x041abba6: float
        melee_attack_min_range: float
        unknown_0x625f214b: float
        melee_attack_range: float
        unknown_0x3e618127: float
        melee_collide_sound: int
        collision_damage: json_util.JsonObject
        hypermode_effect: str
        hypermode_cycle_time: float
        unknown_0xe64bd01e: float
        unknown_0xd8255983: float


@dataclasses.dataclass()
class UnknownStruct41(BaseProperty):
    unknown_0xea4b88c8: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xEA4B88C8, original_name="Unknown"),
        },
    )
    unknown_0xaa04f0be: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAA04F0BE, original_name="Unknown"),
        },
    )
    unknown_0x59f8b6d0: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x59F8B6D0, original_name="Unknown"),
        },
    )
    unknown_0x460020aa: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x460020AA, original_name="Unknown"),
        },
    )
    unknown_0x353abf40: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x353ABF40, original_name="Unknown"),
        },
    )
    caud_0x2822a8fa: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x2822A8FA, original_name="CAUD"),
        },
    )
    caud_0x95d26130: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x95D26130, original_name="CAUD"),
        },
    )
    unknown_0xbfb8336b: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xBFB8336B, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xf79adca8: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xF79ADCA8, original_name="Unknown", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x68454cb4: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x68454CB4, original_name="Unknown"),
        },
    )
    beam_sweep: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x34DDD21C, original_name="BeamSweep", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    beam_sweep2: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x39705DD6, original_name="BeamSweep2", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0xb2671c2a: int = dataclasses.field(
        default=3,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB2671C2A, original_name="Unknown"),
        },
    )
    beam_track_speed: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x546DAB4C, original_name="BeamTrackSpeed"),
        },
    )
    beam_cancel_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFBDCB40F, original_name="BeamCancelRange"),
        },
    )
    beam_cancel_time: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0D225E0A, original_name="BeamCancelTime"),
        },
    )
    jump_min_range: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCFD57029, original_name="JumpMinRange"),
        },
    )
    jump_max_range: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8F9A085F, original_name="JumpMaxRange"),
        },
    )
    unknown_0xb619c33a: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB619C33A, original_name="Unknown"),
        },
    )
    missile_min_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5ECCB98C, original_name="MissileMinRange"),
        },
    )
    unknown_0x041abba6: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x041ABBA6, original_name="Unknown"),
        },
    )
    melee_attack_min_range: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBEADF2E0, original_name="MeleeAttackMinRange"),
        },
    )
    unknown_0x625f214b: float = dataclasses.field(
        default=25.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x625F214B, original_name="Unknown"),
        },
    )
    melee_attack_range: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC3E43D0E, original_name="MeleeAttackRange"),
        },
    )
    unknown_0x3e618127: float = dataclasses.field(
        default=12.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3E618127, original_name="Unknown"),
        },
    )
    melee_collide_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x095080D9, original_name="MeleeCollideSound"),
        },
    )
    collision_damage: DamageInfo = dataclasses.field(
        default_factory=DamageInfo,
        metadata={
            "reflection": FieldReflection[DamageInfo](
                DamageInfo,
                id=0x0CFD3139,
                original_name="CollisionDamage",
                from_json=DamageInfo.from_json,
                to_json=DamageInfo.to_json,
            ),
        },
    )
    hypermode_effect: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x8062D2F8, original_name="HypermodeEffect"),
        },
    )
    hypermode_cycle_time: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBF26FCFB, original_name="HypermodeCycleTime"),
        },
    )
    unknown_0xe64bd01e: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE64BD01E, original_name="Unknown"),
        },
    )
    unknown_0xd8255983: float = dataclasses.field(
        default=8.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD8255983, original_name="Unknown"),
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
        if property_count != 31:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEA4B88C8
        unknown_0xea4b88c8 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA04F0BE
        unknown_0xaa04f0be = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59F8B6D0
        unknown_0x59f8b6d0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x460020AA
        unknown_0x460020aa = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x353ABF40
        unknown_0x353abf40 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2822A8FA
        caud_0x2822a8fa = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95D26130
        caud_0x95d26130 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFB8336B
        unknown_0xbfb8336b = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF79ADCA8
        unknown_0xf79adca8 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68454CB4
        unknown_0x68454cb4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34DDD21C
        beam_sweep = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39705DD6
        beam_sweep2 = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2671C2A
        unknown_0xb2671c2a = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x546DAB4C
        beam_track_speed = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFBDCB40F
        beam_cancel_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D225E0A
        beam_cancel_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCFD57029
        jump_min_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8F9A085F
        jump_max_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB619C33A
        unknown_0xb619c33a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ECCB98C
        missile_min_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041ABBA6
        unknown_0x041abba6 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBEADF2E0
        melee_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x625F214B
        unknown_0x625f214b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC3E43D0E
        melee_attack_range = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3E618127
        unknown_0x3e618127 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x095080D9
        melee_collide_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0CFD3139
        collision_damage = DamageInfo.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8062D2F8
        hypermode_effect = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBF26FCFB
        hypermode_cycle_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE64BD01E
        unknown_0xe64bd01e = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD8255983
        unknown_0xd8255983 = structs.BIG_f.unpack(data.read(4))[0]

        return cls(
            unknown_0xea4b88c8,
            unknown_0xaa04f0be,
            unknown_0x59f8b6d0,
            unknown_0x460020aa,
            unknown_0x353abf40,
            caud_0x2822a8fa,
            caud_0x95d26130,
            unknown_0xbfb8336b,
            unknown_0xf79adca8,
            unknown_0x68454cb4,
            beam_sweep,
            beam_sweep2,
            unknown_0xb2671c2a,
            beam_track_speed,
            beam_cancel_range,
            beam_cancel_time,
            jump_min_range,
            jump_max_range,
            unknown_0xb619c33a,
            missile_min_range,
            unknown_0x041abba6,
            melee_attack_min_range,
            unknown_0x625f214b,
            melee_attack_range,
            unknown_0x3e618127,
            melee_collide_sound,
            collision_damage,
            hypermode_effect,
            hypermode_cycle_time,
            unknown_0xe64bd01e,
            unknown_0xd8255983,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1f")  # 31 properties

        data.write(b"\xeaK\x88\xc8")  # 0xea4b88c8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xea4b88c8))

        data.write(b"\xaa\x04\xf0\xbe")  # 0xaa04f0be
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xaa04f0be))

        data.write(b"Y\xf8\xb6\xd0")  # 0x59f8b6d0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x59f8b6d0))

        data.write(b"F\x00 \xaa")  # 0x460020aa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x460020aa))

        data.write(b"5:\xbf@")  # 0x353abf40
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x353abf40))

        data.write(b'("\xa8\xfa')  # 0x2822a8fa
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x2822a8fa))

        data.write(b"\x95\xd2a0")  # 0x95d26130
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.caud_0x95d26130))

        data.write(b"\xbf\xb83k")  # 0xbfb8336b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xbfb8336b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xf7\x9a\xdc\xa8")  # 0xf79adca8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0xf79adca8.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"hEL\xb4")  # 0x68454cb4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x68454cb4))

        data.write(b"4\xdd\xd2\x1c")  # 0x34ddd21c
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_sweep.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"9p]\xd6")  # 0x39705dd6
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.beam_sweep2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xb2g\x1c*")  # 0xb2671c2a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb2671c2a))

        data.write(b"Tm\xabL")  # 0x546dab4c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.beam_track_speed))

        data.write(b"\xfb\xdc\xb4\x0f")  # 0xfbdcb40f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.beam_cancel_range))

        data.write(b'\r"^\n')  # 0xd225e0a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.beam_cancel_time))

        data.write(b"\xcf\xd5p)")  # 0xcfd57029
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.jump_min_range))

        data.write(b"\x8f\x9a\x08_")  # 0x8f9a085f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.jump_max_range))

        data.write(b"\xb6\x19\xc3:")  # 0xb619c33a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb619c33a))

        data.write(b"^\xcc\xb9\x8c")  # 0x5eccb98c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.missile_min_range))

        data.write(b"\x04\x1a\xbb\xa6")  # 0x41abba6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x041abba6))

        data.write(b"\xbe\xad\xf2\xe0")  # 0xbeadf2e0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_attack_min_range))

        data.write(b"b_!K")  # 0x625f214b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x625f214b))

        data.write(b"\xc3\xe4=\x0e")  # 0xc3e43d0e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_attack_range))

        data.write(b">a\x81'")  # 0x3e618127
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3e618127))

        data.write(b"\tP\x80\xd9")  # 0x95080d9
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.melee_collide_sound))

        data.write(b"\x0c\xfd19")  # 0xcfd3139
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.collision_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x80b\xd2\xf8")  # 0x8062d2f8
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.hypermode_effect.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbf&\xfc\xfb")  # 0xbf26fcfb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.hypermode_cycle_time))

        data.write(b"\xe6K\xd0\x1e")  # 0xe64bd01e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe64bd01e))

        data.write(b"\xd8%Y\x83")  # 0xd8255983
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd8255983))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct41Json", data)
        return cls(
            unknown_0xea4b88c8=json_data["unknown_0xea4b88c8"],
            unknown_0xaa04f0be=json_data["unknown_0xaa04f0be"],
            unknown_0x59f8b6d0=json_data["unknown_0x59f8b6d0"],
            unknown_0x460020aa=json_data["unknown_0x460020aa"],
            unknown_0x353abf40=json_data["unknown_0x353abf40"],
            caud_0x2822a8fa=json_data["caud_0x2822a8fa"],
            caud_0x95d26130=json_data["caud_0x95d26130"],
            unknown_0xbfb8336b=Spline.from_json(json_data["unknown_0xbfb8336b"]),
            unknown_0xf79adca8=Spline.from_json(json_data["unknown_0xf79adca8"]),
            unknown_0x68454cb4=json_data["unknown_0x68454cb4"],
            beam_sweep=Spline.from_json(json_data["beam_sweep"]),
            beam_sweep2=Spline.from_json(json_data["beam_sweep2"]),
            unknown_0xb2671c2a=json_data["unknown_0xb2671c2a"],
            beam_track_speed=json_data["beam_track_speed"],
            beam_cancel_range=json_data["beam_cancel_range"],
            beam_cancel_time=json_data["beam_cancel_time"],
            jump_min_range=json_data["jump_min_range"],
            jump_max_range=json_data["jump_max_range"],
            unknown_0xb619c33a=json_data["unknown_0xb619c33a"],
            missile_min_range=json_data["missile_min_range"],
            unknown_0x041abba6=json_data["unknown_0x041abba6"],
            melee_attack_min_range=json_data["melee_attack_min_range"],
            unknown_0x625f214b=json_data["unknown_0x625f214b"],
            melee_attack_range=json_data["melee_attack_range"],
            unknown_0x3e618127=json_data["unknown_0x3e618127"],
            melee_collide_sound=json_data["melee_collide_sound"],
            collision_damage=DamageInfo.from_json(json_data["collision_damage"]),
            hypermode_effect=json_data["hypermode_effect"],
            hypermode_cycle_time=json_data["hypermode_cycle_time"],
            unknown_0xe64bd01e=json_data["unknown_0xe64bd01e"],
            unknown_0xd8255983=json_data["unknown_0xd8255983"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xea4b88c8": self.unknown_0xea4b88c8,
            "unknown_0xaa04f0be": self.unknown_0xaa04f0be,
            "unknown_0x59f8b6d0": self.unknown_0x59f8b6d0,
            "unknown_0x460020aa": self.unknown_0x460020aa,
            "unknown_0x353abf40": self.unknown_0x353abf40,
            "caud_0x2822a8fa": self.caud_0x2822a8fa,
            "caud_0x95d26130": self.caud_0x95d26130,
            "unknown_0xbfb8336b": self.unknown_0xbfb8336b.to_json(),
            "unknown_0xf79adca8": self.unknown_0xf79adca8.to_json(),
            "unknown_0x68454cb4": self.unknown_0x68454cb4,
            "beam_sweep": self.beam_sweep.to_json(),
            "beam_sweep2": self.beam_sweep2.to_json(),
            "unknown_0xb2671c2a": self.unknown_0xb2671c2a,
            "beam_track_speed": self.beam_track_speed,
            "beam_cancel_range": self.beam_cancel_range,
            "beam_cancel_time": self.beam_cancel_time,
            "jump_min_range": self.jump_min_range,
            "jump_max_range": self.jump_max_range,
            "unknown_0xb619c33a": self.unknown_0xb619c33a,
            "missile_min_range": self.missile_min_range,
            "unknown_0x041abba6": self.unknown_0x041abba6,
            "melee_attack_min_range": self.melee_attack_min_range,
            "unknown_0x625f214b": self.unknown_0x625f214b,
            "melee_attack_range": self.melee_attack_range,
            "unknown_0x3e618127": self.unknown_0x3e618127,
            "melee_collide_sound": self.melee_collide_sound,
            "collision_damage": self.collision_damage.to_json(),
            "hypermode_effect": self.hypermode_effect,
            "hypermode_cycle_time": self.hypermode_cycle_time,
            "unknown_0xe64bd01e": self.unknown_0xe64bd01e,
            "unknown_0xd8255983": self.unknown_0xd8255983,
        }


def _decode_unknown_0xbfb8336b(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0xf79adca8(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_beam_sweep(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_beam_sweep2(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_collision_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_hypermode_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xEA4B88C8: ("unknown_0xea4b88c8", structs.decode_BIG_f),
    0xAA04F0BE: ("unknown_0xaa04f0be", structs.decode_BIG_f),
    0x59F8B6D0: ("unknown_0x59f8b6d0", structs.decode_BIG_f),
    0x460020AA: ("unknown_0x460020aa", structs.decode_BIG_f),
    0x353ABF40: ("unknown_0x353abf40", structs.decode_BIG_f),
    0x2822A8FA: ("caud_0x2822a8fa", structs.decode_BIG_Q),
    0x95D26130: ("caud_0x95d26130", structs.decode_BIG_Q),
    0xBFB8336B: ("unknown_0xbfb8336b", _decode_unknown_0xbfb8336b),
    0xF79ADCA8: ("unknown_0xf79adca8", _decode_unknown_0xf79adca8),
    0x68454CB4: ("unknown_0x68454cb4", structs.decode_BIG_f),
    0x34DDD21C: ("beam_sweep", _decode_beam_sweep),
    0x39705DD6: ("beam_sweep2", _decode_beam_sweep2),
    0xB2671C2A: ("unknown_0xb2671c2a", structs.decode_BIG_l),
    0x546DAB4C: ("beam_track_speed", structs.decode_BIG_f),
    0xFBDCB40F: ("beam_cancel_range", structs.decode_BIG_f),
    0x0D225E0A: ("beam_cancel_time", structs.decode_BIG_f),
    0xCFD57029: ("jump_min_range", structs.decode_BIG_f),
    0x8F9A085F: ("jump_max_range", structs.decode_BIG_f),
    0xB619C33A: ("unknown_0xb619c33a", structs.decode_BIG_f),
    0x5ECCB98C: ("missile_min_range", structs.decode_BIG_f),
    0x041ABBA6: ("unknown_0x041abba6", structs.decode_BIG_f),
    0xBEADF2E0: ("melee_attack_min_range", structs.decode_BIG_f),
    0x625F214B: ("unknown_0x625f214b", structs.decode_BIG_f),
    0xC3E43D0E: ("melee_attack_range", structs.decode_BIG_f),
    0x3E618127: ("unknown_0x3e618127", structs.decode_BIG_f),
    0x095080D9: ("melee_collide_sound", structs.decode_BIG_Q),
    0x0CFD3139: ("collision_damage", _decode_collision_damage),
    0x8062D2F8: ("hypermode_effect", _decode_hypermode_effect),
    0xBF26FCFB: ("hypermode_cycle_time", structs.decode_BIG_f),
    0xE64BD01E: ("unknown_0xe64bd01e", structs.decode_BIG_f),
    0xD8255983: ("unknown_0xd8255983", structs.decode_BIG_f),
}
