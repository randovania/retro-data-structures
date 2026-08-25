# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.TweakBall_BoostBall import TweakBall_BoostBall
from retro_data_structures.properties.common.archetypes.TweakBall_Camera import TweakBall_Camera
from retro_data_structures.properties.common.archetypes.TweakBall_CannonBall import TweakBall_CannonBall
from retro_data_structures.properties.common.archetypes.TweakBall_DeathBall import TweakBall_DeathBall
from retro_data_structures.properties.common.archetypes.TweakBall_Movement import TweakBall_Movement
from retro_data_structures.properties.echoes.archetypes.TweakBall_Misc import TweakBall_Misc
from retro_data_structures.properties.echoes.archetypes.TweakBall_ScrewAttack import TweakBall_ScrewAttack
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class TweakBallJson(typing_extensions.TypedDict):
        instance_name: str
        movement: json_util.JsonObject
        camera: json_util.JsonObject
        misc: json_util.JsonObject
        boost_ball: json_util.JsonObject
        cannon_ball: json_util.JsonObject
        screw_attack: json_util.JsonObject
        death_ball: json_util.JsonObject


@dataclasses.dataclass()
class TweakBall(BaseObjectType):
    instance_name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x7FDA1466, original_name="InstanceName"),
        },
    )
    movement: TweakBall_Movement = dataclasses.field(
        default_factory=TweakBall_Movement,
        metadata={
            "reflection": FieldReflection[TweakBall_Movement](
                TweakBall_Movement,
                id=0x0DEF1FFB,
                original_name="Movement",
                from_json=TweakBall_Movement.from_json,
                to_json=TweakBall_Movement.to_json,
            ),
        },
    )
    camera: TweakBall_Camera = dataclasses.field(
        default_factory=TweakBall_Camera,
        metadata={
            "reflection": FieldReflection[TweakBall_Camera](
                TweakBall_Camera,
                id=0x7AAC09B9,
                original_name="Camera",
                from_json=TweakBall_Camera.from_json,
                to_json=TweakBall_Camera.to_json,
            ),
        },
    )
    misc: TweakBall_Misc = dataclasses.field(
        default_factory=TweakBall_Misc,
        metadata={
            "reflection": FieldReflection[TweakBall_Misc](
                TweakBall_Misc,
                id=0x0C67B730,
                original_name="Misc",
                from_json=TweakBall_Misc.from_json,
                to_json=TweakBall_Misc.to_json,
            ),
        },
    )
    boost_ball: TweakBall_BoostBall = dataclasses.field(
        default_factory=TweakBall_BoostBall,
        metadata={
            "reflection": FieldReflection[TweakBall_BoostBall](
                TweakBall_BoostBall,
                id=0xCB4EA3BF,
                original_name="BoostBall",
                from_json=TweakBall_BoostBall.from_json,
                to_json=TweakBall_BoostBall.to_json,
            ),
        },
    )
    cannon_ball: TweakBall_CannonBall = dataclasses.field(
        default_factory=TweakBall_CannonBall,
        metadata={
            "reflection": FieldReflection[TweakBall_CannonBall](
                TweakBall_CannonBall,
                id=0x5FB9E808,
                original_name="CannonBall",
                from_json=TweakBall_CannonBall.from_json,
                to_json=TweakBall_CannonBall.to_json,
            ),
        },
    )
    screw_attack: TweakBall_ScrewAttack = dataclasses.field(
        default_factory=TweakBall_ScrewAttack,
        metadata={
            "reflection": FieldReflection[TweakBall_ScrewAttack](
                TweakBall_ScrewAttack,
                id=0x4B1C7B7D,
                original_name="ScrewAttack",
                from_json=TweakBall_ScrewAttack.from_json,
                to_json=TweakBall_ScrewAttack.to_json,
            ),
        },
    )
    death_ball: TweakBall_DeathBall = dataclasses.field(
        default_factory=TweakBall_DeathBall,
        metadata={
            "reflection": FieldReflection[TweakBall_DeathBall](
                TweakBall_DeathBall,
                id=0xBB5FC8A4,
                original_name="DeathBall",
                from_json=TweakBall_DeathBall.from_json,
                to_json=TweakBall_DeathBall.to_json,
            ),
        },
    )

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return "TWBL"

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
        if property_count != 8:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7FDA1466
        instance_name = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0DEF1FFB
        movement = TweakBall_Movement.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7AAC09B9
        camera = TweakBall_Camera.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0C67B730
        misc = TweakBall_Misc.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCB4EA3BF
        boost_ball = TweakBall_BoostBall.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5FB9E808
        cannon_ball = TweakBall_CannonBall.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4B1C7B7D
        screw_attack = TweakBall_ScrewAttack.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBB5FC8A4
        death_ball = TweakBall_DeathBall.from_stream(data, game, property_size)

        return cls(instance_name, movement, camera, misc, boost_ball, cannon_ball, screw_attack, death_ball)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\x7f\xda\x14f")  # 0x7fda1466
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.instance_name.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\r\xef\x1f\xfb")  # 0xdef1ffb
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.movement.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"z\xac\t\xb9")  # 0x7aac09b9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0cg\xb70")  # 0xc67b730
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcbN\xa3\xbf")  # 0xcb4ea3bf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.boost_ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"_\xb9\xe8\x08")  # 0x5fb9e808
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.cannon_ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"K\x1c{}")  # 0x4b1c7b7d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.screw_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbb_\xc8\xa4")  # 0xbb5fc8a4
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.death_ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakBallJson", data)
        return cls(
            instance_name=json_data["instance_name"],
            movement=TweakBall_Movement.from_json(json_data["movement"]),
            camera=TweakBall_Camera.from_json(json_data["camera"]),
            misc=TweakBall_Misc.from_json(json_data["misc"]),
            boost_ball=TweakBall_BoostBall.from_json(json_data["boost_ball"]),
            cannon_ball=TweakBall_CannonBall.from_json(json_data["cannon_ball"]),
            screw_attack=TweakBall_ScrewAttack.from_json(json_data["screw_attack"]),
            death_ball=TweakBall_DeathBall.from_json(json_data["death_ball"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "instance_name": self.instance_name,
            "movement": self.movement.to_json(),
            "camera": self.camera.to_json(),
            "misc": self.misc.to_json(),
            "boost_ball": self.boost_ball.to_json(),
            "cannon_ball": self.cannon_ball.to_json(),
            "screw_attack": self.screw_attack.to_json(),
            "death_ball": self.death_ball.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_movement(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_Movement:
    return TweakBall_Movement.from_stream(data, game, property_size)


def _decode_camera(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_Camera:
    return TweakBall_Camera.from_stream(data, game, property_size)


def _decode_misc(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_Misc:
    return TweakBall_Misc.from_stream(data, game, property_size)


def _decode_boost_ball(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_BoostBall:
    return TweakBall_BoostBall.from_stream(data, game, property_size)


def _decode_cannon_ball(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_CannonBall:
    return TweakBall_CannonBall.from_stream(data, game, property_size)


def _decode_screw_attack(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_ScrewAttack:
    return TweakBall_ScrewAttack.from_stream(data, game, property_size)


def _decode_death_ball(data: typing.BinaryIO, game: Game, property_size: int) -> TweakBall_DeathBall:
    return TweakBall_DeathBall.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7FDA1466: ("instance_name", _decode_instance_name),
    0x0DEF1FFB: ("movement", _decode_movement),
    0x7AAC09B9: ("camera", _decode_camera),
    0x0C67B730: ("misc", _decode_misc),
    0xCB4EA3BF: ("boost_ball", _decode_boost_ball),
    0x5FB9E808: ("cannon_ball", _decode_cannon_ball),
    0x4B1C7B7D: ("screw_attack", _decode_screw_attack),
    0xBB5FC8A4: ("death_ball", _decode_death_ball),
}
