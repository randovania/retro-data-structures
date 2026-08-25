# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.UnknownStruct16 import UnknownStruct16
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct17Json(typing_extensions.TypedDict):
        unknown_0xb5af7831: float
        unknown_0xac65eb7a: float
        unknown_0x4f3855a0: float
        unknown_0x08c0b02c: float
        unknown_0x695f68c7: float
        unknown_0xd061ff99: float
        pause_duration_min: float
        pause_duration_max: float
        chance_to_double_dash: float
        unknown_struct16: json_util.JsonObject
        unknown_0x3ff87a8c: bool
        unknown_0x49b9936d: bool
        unknown_0xc96b8223: bool
        unknown_0x53fdcb5b: bool
        unknown_0x0d7ef013: bool
        unknown_0xaa85c885: bool
        pause: float
        taunt: float
        look_around: bool
        melee_attack: float
        melee_dash: float
        scatter_shot: float
        unknown_0x94f48974: float
        dive_attack: float
        unknown_0xb2c1e4fa: bool
        unknown_0xf5cf3c0f: bool
        normal_missile: float
        missile_jump: float
        super_missile: float
        unknown_0xe63286eb: float
        unknown_0x4aae6186: float
        sweep_beam: float
        boost_ball: float
        unknown_0x2d7551e6: bool
        phazon_attack: float
        phazon_enrage: float
        unknown_0x911a2476: bool


@dataclasses.dataclass()
class UnknownStruct17(BaseProperty):
    unknown_0xb5af7831: float = dataclasses.field(
        default=-1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB5AF7831, original_name="Unknown"),
        },
    )
    unknown_0xac65eb7a: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAC65EB7A, original_name="Unknown"),
        },
    )
    unknown_0x4f3855a0: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4F3855A0, original_name="Unknown"),
        },
    )
    unknown_0x08c0b02c: float = dataclasses.field(
        default=2.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x08C0B02C, original_name="Unknown"),
        },
    )
    unknown_0x695f68c7: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x695F68C7, original_name="Unknown"),
        },
    )
    unknown_0xd061ff99: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD061FF99, original_name="Unknown"),
        },
    )
    pause_duration_min: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x97DBD42A, original_name="PauseDurationMin"),
        },
    )
    pause_duration_max: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x71BB7BCB, original_name="PauseDurationMax"),
        },
    )
    chance_to_double_dash: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB751778B, original_name="ChanceToDoubleDash"),
        },
    )
    unknown_struct16: UnknownStruct16 = dataclasses.field(
        default_factory=UnknownStruct16,
        metadata={
            "reflection": FieldReflection[UnknownStruct16](
                UnknownStruct16,
                id=0xD6740348,
                original_name="UnknownStruct16",
                from_json=UnknownStruct16.from_json,
                to_json=UnknownStruct16.to_json,
            ),
        },
    )
    unknown_0x3ff87a8c: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x3FF87A8C, original_name="Unknown"),
        },
    )
    unknown_0x49b9936d: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x49B9936D, original_name="Unknown"),
        },
    )
    unknown_0xc96b8223: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xC96B8223, original_name="Unknown"),
        },
    )
    unknown_0x53fdcb5b: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x53FDCB5B, original_name="Unknown"),
        },
    )
    unknown_0x0d7ef013: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0D7EF013, original_name="Unknown"),
        },
    )
    unknown_0xaa85c885: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xAA85C885, original_name="Unknown"),
        },
    )
    pause: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x80F7E605, original_name="Pause"),
        },
    )
    taunt: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x479F6A4F, original_name="Taunt"),
        },
    )
    look_around: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x778791F5, original_name="LookAround"),
        },
    )
    melee_attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCE4C4668, original_name="MeleeAttack"),
        },
    )
    melee_dash: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x5951A03F, original_name="MeleeDash"),
        },
    )
    scatter_shot: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x94615651, original_name="ScatterShot"),
        },
    )
    unknown_0x94f48974: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x94F48974, original_name="Unknown"),
        },
    )
    dive_attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6E40FB76, original_name="DiveAttack"),
        },
    )
    unknown_0xb2c1e4fa: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB2C1E4FA, original_name="Unknown"),
        },
    )
    unknown_0xf5cf3c0f: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF5CF3C0F, original_name="Unknown"),
        },
    )
    normal_missile: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6847EFA7, original_name="NormalMissile"),
        },
    )
    missile_jump: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x083FD602, original_name="MissileJump"),
        },
    )
    super_missile: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xDB21402F, original_name="SuperMissile"),
        },
    )
    unknown_0xe63286eb: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE63286EB, original_name="Unknown"),
        },
    )
    unknown_0x4aae6186: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4AAE6186, original_name="Unknown"),
        },
    )
    sweep_beam: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2BD1C15B, original_name="SweepBeam"),
        },
    )
    boost_ball: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB53693FA, original_name="BoostBall"),
        },
    )
    unknown_0x2d7551e6: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2D7551E6, original_name="Unknown"),
        },
    )
    phazon_attack: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x93A876F3, original_name="PhazonAttack"),
        },
    )
    phazon_enrage: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAEA228B9, original_name="PhazonEnrage"),
        },
    )
    unknown_0x911a2476: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x911A2476, original_name="Unknown"),
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
        if property_count != 37:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB5AF7831
        unknown_0xb5af7831 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAC65EB7A
        unknown_0xac65eb7a = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4F3855A0
        unknown_0x4f3855a0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08C0B02C
        unknown_0x08c0b02c = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x695F68C7
        unknown_0x695f68c7 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD061FF99
        unknown_0xd061ff99 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97DBD42A
        pause_duration_min = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71BB7BCB
        pause_duration_max = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB751778B
        chance_to_double_dash = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD6740348
        unknown_struct16 = UnknownStruct16.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FF87A8C
        unknown_0x3ff87a8c = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49B9936D
        unknown_0x49b9936d = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC96B8223
        unknown_0xc96b8223 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53FDCB5B
        unknown_0x53fdcb5b = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0D7EF013
        unknown_0x0d7ef013 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAA85C885
        unknown_0xaa85c885 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80F7E605
        pause = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x479F6A4F
        taunt = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x778791F5
        look_around = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCE4C4668
        melee_attack = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5951A03F
        melee_dash = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94615651
        scatter_shot = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94F48974
        unknown_0x94f48974 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E40FB76
        dive_attack = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB2C1E4FA
        unknown_0xb2c1e4fa = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF5CF3C0F
        unknown_0xf5cf3c0f = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6847EFA7
        normal_missile = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x083FD602
        missile_jump = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xDB21402F
        super_missile = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE63286EB
        unknown_0xe63286eb = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4AAE6186
        unknown_0x4aae6186 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BD1C15B
        sweep_beam = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB53693FA
        boost_ball = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2D7551E6
        unknown_0x2d7551e6 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93A876F3
        phazon_attack = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAEA228B9
        phazon_enrage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x911A2476
        unknown_0x911a2476 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            unknown_0xb5af7831,
            unknown_0xac65eb7a,
            unknown_0x4f3855a0,
            unknown_0x08c0b02c,
            unknown_0x695f68c7,
            unknown_0xd061ff99,
            pause_duration_min,
            pause_duration_max,
            chance_to_double_dash,
            unknown_struct16,
            unknown_0x3ff87a8c,
            unknown_0x49b9936d,
            unknown_0xc96b8223,
            unknown_0x53fdcb5b,
            unknown_0x0d7ef013,
            unknown_0xaa85c885,
            pause,
            taunt,
            look_around,
            melee_attack,
            melee_dash,
            scatter_shot,
            unknown_0x94f48974,
            dive_attack,
            unknown_0xb2c1e4fa,
            unknown_0xf5cf3c0f,
            normal_missile,
            missile_jump,
            super_missile,
            unknown_0xe63286eb,
            unknown_0x4aae6186,
            sweep_beam,
            boost_ball,
            unknown_0x2d7551e6,
            phazon_attack,
            phazon_enrage,
            unknown_0x911a2476,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00%")  # 37 properties

        data.write(b"\xb5\xafx1")  # 0xb5af7831
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5af7831))

        data.write(b"\xace\xebz")  # 0xac65eb7a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xac65eb7a))

        data.write(b"O8U\xa0")  # 0x4f3855a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f3855a0))

        data.write(b"\x08\xc0\xb0,")  # 0x8c0b02c
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x08c0b02c))

        data.write(b"i_h\xc7")  # 0x695f68c7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x695f68c7))

        data.write(b"\xd0a\xff\x99")  # 0xd061ff99
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd061ff99))

        data.write(b"\x97\xdb\xd4*")  # 0x97dbd42a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pause_duration_min))

        data.write(b"q\xbb{\xcb")  # 0x71bb7bcb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pause_duration_max))

        data.write(b"\xb7Qw\x8b")  # 0xb751778b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.chance_to_double_dash))

        data.write(b"\xd6t\x03H")  # 0xd6740348
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_struct16.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"?\xf8z\x8c")  # 0x3ff87a8c
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3ff87a8c))

        data.write(b"I\xb9\x93m")  # 0x49b9936d
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x49b9936d))

        data.write(b"\xc9k\x82#")  # 0xc96b8223
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xc96b8223))

        data.write(b"S\xfd\xcb[")  # 0x53fdcb5b
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x53fdcb5b))

        data.write(b"\r~\xf0\x13")  # 0xd7ef013
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x0d7ef013))

        data.write(b"\xaa\x85\xc8\x85")  # 0xaa85c885
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xaa85c885))

        data.write(b"\x80\xf7\xe6\x05")  # 0x80f7e605
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.pause))

        data.write(b"G\x9fjO")  # 0x479f6a4f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.taunt))

        data.write(b"w\x87\x91\xf5")  # 0x778791f5
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.look_around))

        data.write(b"\xceLFh")  # 0xce4c4668
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_attack))

        data.write(b"YQ\xa0?")  # 0x5951a03f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.melee_dash))

        data.write(b"\x94aVQ")  # 0x94615651
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.scatter_shot))

        data.write(b"\x94\xf4\x89t")  # 0x94f48974
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x94f48974))

        data.write(b"n@\xfbv")  # 0x6e40fb76
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.dive_attack))

        data.write(b"\xb2\xc1\xe4\xfa")  # 0xb2c1e4fa
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xb2c1e4fa))

        data.write(b"\xf5\xcf<\x0f")  # 0xf5cf3c0f
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf5cf3c0f))

        data.write(b"hG\xef\xa7")  # 0x6847efa7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.normal_missile))

        data.write(b"\x08?\xd6\x02")  # 0x83fd602
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.missile_jump))

        data.write(b"\xdb!@/")  # 0xdb21402f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.super_missile))

        data.write(b"\xe62\x86\xeb")  # 0xe63286eb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe63286eb))

        data.write(b"J\xaea\x86")  # 0x4aae6186
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4aae6186))

        data.write(b"+\xd1\xc1[")  # 0x2bd1c15b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.sweep_beam))

        data.write(b"\xb56\x93\xfa")  # 0xb53693fa
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.boost_ball))

        data.write(b"-uQ\xe6")  # 0x2d7551e6
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2d7551e6))

        data.write(b"\x93\xa8v\xf3")  # 0x93a876f3
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_attack))

        data.write(b"\xae\xa2(\xb9")  # 0xaea228b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.phazon_enrage))

        data.write(b"\x91\x1a$v")  # 0x911a2476
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x911a2476))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct17Json", data)
        return cls(
            unknown_0xb5af7831=json_data["unknown_0xb5af7831"],
            unknown_0xac65eb7a=json_data["unknown_0xac65eb7a"],
            unknown_0x4f3855a0=json_data["unknown_0x4f3855a0"],
            unknown_0x08c0b02c=json_data["unknown_0x08c0b02c"],
            unknown_0x695f68c7=json_data["unknown_0x695f68c7"],
            unknown_0xd061ff99=json_data["unknown_0xd061ff99"],
            pause_duration_min=json_data["pause_duration_min"],
            pause_duration_max=json_data["pause_duration_max"],
            chance_to_double_dash=json_data["chance_to_double_dash"],
            unknown_struct16=UnknownStruct16.from_json(json_data["unknown_struct16"]),
            unknown_0x3ff87a8c=json_data["unknown_0x3ff87a8c"],
            unknown_0x49b9936d=json_data["unknown_0x49b9936d"],
            unknown_0xc96b8223=json_data["unknown_0xc96b8223"],
            unknown_0x53fdcb5b=json_data["unknown_0x53fdcb5b"],
            unknown_0x0d7ef013=json_data["unknown_0x0d7ef013"],
            unknown_0xaa85c885=json_data["unknown_0xaa85c885"],
            pause=json_data["pause"],
            taunt=json_data["taunt"],
            look_around=json_data["look_around"],
            melee_attack=json_data["melee_attack"],
            melee_dash=json_data["melee_dash"],
            scatter_shot=json_data["scatter_shot"],
            unknown_0x94f48974=json_data["unknown_0x94f48974"],
            dive_attack=json_data["dive_attack"],
            unknown_0xb2c1e4fa=json_data["unknown_0xb2c1e4fa"],
            unknown_0xf5cf3c0f=json_data["unknown_0xf5cf3c0f"],
            normal_missile=json_data["normal_missile"],
            missile_jump=json_data["missile_jump"],
            super_missile=json_data["super_missile"],
            unknown_0xe63286eb=json_data["unknown_0xe63286eb"],
            unknown_0x4aae6186=json_data["unknown_0x4aae6186"],
            sweep_beam=json_data["sweep_beam"],
            boost_ball=json_data["boost_ball"],
            unknown_0x2d7551e6=json_data["unknown_0x2d7551e6"],
            phazon_attack=json_data["phazon_attack"],
            phazon_enrage=json_data["phazon_enrage"],
            unknown_0x911a2476=json_data["unknown_0x911a2476"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xb5af7831": self.unknown_0xb5af7831,
            "unknown_0xac65eb7a": self.unknown_0xac65eb7a,
            "unknown_0x4f3855a0": self.unknown_0x4f3855a0,
            "unknown_0x08c0b02c": self.unknown_0x08c0b02c,
            "unknown_0x695f68c7": self.unknown_0x695f68c7,
            "unknown_0xd061ff99": self.unknown_0xd061ff99,
            "pause_duration_min": self.pause_duration_min,
            "pause_duration_max": self.pause_duration_max,
            "chance_to_double_dash": self.chance_to_double_dash,
            "unknown_struct16": self.unknown_struct16.to_json(),
            "unknown_0x3ff87a8c": self.unknown_0x3ff87a8c,
            "unknown_0x49b9936d": self.unknown_0x49b9936d,
            "unknown_0xc96b8223": self.unknown_0xc96b8223,
            "unknown_0x53fdcb5b": self.unknown_0x53fdcb5b,
            "unknown_0x0d7ef013": self.unknown_0x0d7ef013,
            "unknown_0xaa85c885": self.unknown_0xaa85c885,
            "pause": self.pause,
            "taunt": self.taunt,
            "look_around": self.look_around,
            "melee_attack": self.melee_attack,
            "melee_dash": self.melee_dash,
            "scatter_shot": self.scatter_shot,
            "unknown_0x94f48974": self.unknown_0x94f48974,
            "dive_attack": self.dive_attack,
            "unknown_0xb2c1e4fa": self.unknown_0xb2c1e4fa,
            "unknown_0xf5cf3c0f": self.unknown_0xf5cf3c0f,
            "normal_missile": self.normal_missile,
            "missile_jump": self.missile_jump,
            "super_missile": self.super_missile,
            "unknown_0xe63286eb": self.unknown_0xe63286eb,
            "unknown_0x4aae6186": self.unknown_0x4aae6186,
            "sweep_beam": self.sweep_beam,
            "boost_ball": self.boost_ball,
            "unknown_0x2d7551e6": self.unknown_0x2d7551e6,
            "phazon_attack": self.phazon_attack,
            "phazon_enrage": self.phazon_enrage,
            "unknown_0x911a2476": self.unknown_0x911a2476,
        }


def _decode_unknown_struct16(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct16:
    return UnknownStruct16.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB5AF7831: ("unknown_0xb5af7831", structs.decode_BIG_f),
    0xAC65EB7A: ("unknown_0xac65eb7a", structs.decode_BIG_f),
    0x4F3855A0: ("unknown_0x4f3855a0", structs.decode_BIG_f),
    0x08C0B02C: ("unknown_0x08c0b02c", structs.decode_BIG_f),
    0x695F68C7: ("unknown_0x695f68c7", structs.decode_BIG_f),
    0xD061FF99: ("unknown_0xd061ff99", structs.decode_BIG_f),
    0x97DBD42A: ("pause_duration_min", structs.decode_BIG_f),
    0x71BB7BCB: ("pause_duration_max", structs.decode_BIG_f),
    0xB751778B: ("chance_to_double_dash", structs.decode_BIG_f),
    0xD6740348: ("unknown_struct16", _decode_unknown_struct16),
    0x3FF87A8C: ("unknown_0x3ff87a8c", structs.decode_BIG_bool_),
    0x49B9936D: ("unknown_0x49b9936d", structs.decode_BIG_bool_),
    0xC96B8223: ("unknown_0xc96b8223", structs.decode_BIG_bool_),
    0x53FDCB5B: ("unknown_0x53fdcb5b", structs.decode_BIG_bool_),
    0x0D7EF013: ("unknown_0x0d7ef013", structs.decode_BIG_bool_),
    0xAA85C885: ("unknown_0xaa85c885", structs.decode_BIG_bool_),
    0x80F7E605: ("pause", structs.decode_BIG_f),
    0x479F6A4F: ("taunt", structs.decode_BIG_f),
    0x778791F5: ("look_around", structs.decode_BIG_bool_),
    0xCE4C4668: ("melee_attack", structs.decode_BIG_f),
    0x5951A03F: ("melee_dash", structs.decode_BIG_f),
    0x94615651: ("scatter_shot", structs.decode_BIG_f),
    0x94F48974: ("unknown_0x94f48974", structs.decode_BIG_f),
    0x6E40FB76: ("dive_attack", structs.decode_BIG_f),
    0xB2C1E4FA: ("unknown_0xb2c1e4fa", structs.decode_BIG_bool_),
    0xF5CF3C0F: ("unknown_0xf5cf3c0f", structs.decode_BIG_bool_),
    0x6847EFA7: ("normal_missile", structs.decode_BIG_f),
    0x083FD602: ("missile_jump", structs.decode_BIG_f),
    0xDB21402F: ("super_missile", structs.decode_BIG_f),
    0xE63286EB: ("unknown_0xe63286eb", structs.decode_BIG_f),
    0x4AAE6186: ("unknown_0x4aae6186", structs.decode_BIG_f),
    0x2BD1C15B: ("sweep_beam", structs.decode_BIG_f),
    0xB53693FA: ("boost_ball", structs.decode_BIG_f),
    0x2D7551E6: ("unknown_0x2d7551e6", structs.decode_BIG_bool_),
    0x93A876F3: ("phazon_attack", structs.decode_BIG_f),
    0xAEA228B9: ("phazon_enrage", structs.decode_BIG_f),
    0x911A2476: ("unknown_0x911a2476", structs.decode_BIG_bool_),
}
