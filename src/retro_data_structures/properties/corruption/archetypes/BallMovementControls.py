# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class BallMovementControlsJson(typing_extensions.TypedDict):
        roll_forward: json_util.JsonObject
        roll_backward: json_util.JsonObject
        roll_left: json_util.JsonObject
        roll_right: json_util.JsonObject
        boost_ball: json_util.JsonObject
        spider_ball: json_util.JsonObject
        screw_attack: json_util.JsonObject
        spring_ball: json_util.JsonObject


@dataclasses.dataclass()
class BallMovementControls(BaseProperty):
    roll_forward: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xB4F29640,
                original_name="RollForward",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    roll_backward: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xA25009D3,
                original_name="RollBackward",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    roll_left: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x9CBA817B,
                original_name="RollLeft",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    roll_right: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0xCDC3A9CF,
                original_name="RollRight",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    boost_ball: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x2F0E0276,
                original_name="BoostBall",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    spider_ball: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x9A973454,
                original_name="SpiderBall",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    screw_attack: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x8B9F60A3,
                original_name="ScrewAttack",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
            ),
        },
    )
    spring_ball: RevolutionControl = dataclasses.field(
        default_factory=RevolutionControl,
        metadata={
            "reflection": FieldReflection[RevolutionControl](
                RevolutionControl,
                id=0x756A3682,
                original_name="SpringBall",
                from_json=RevolutionControl.from_json,
                to_json=RevolutionControl.to_json,
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
        if property_count != 8:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB4F29640
        roll_forward = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA25009D3
        roll_backward = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9CBA817B
        roll_left = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCDC3A9CF
        roll_right = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2F0E0276
        boost_ball = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9A973454
        spider_ball = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8B9F60A3
        screw_attack = RevolutionControl.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x756A3682
        spring_ball = RevolutionControl.from_stream(data, game, property_size)

        return cls(
            roll_forward, roll_backward, roll_left, roll_right, boost_ball, spider_ball, screw_attack, spring_ball
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\xb4\xf2\x96@")  # 0xb4f29640
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.roll_forward.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xa2P\t\xd3")  # 0xa25009d3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.roll_backward.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9c\xba\x81{")  # 0x9cba817b
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.roll_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcd\xc3\xa9\xcf")  # 0xcdc3a9cf
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.roll_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"/\x0e\x02v")  # 0x2f0e0276
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.boost_ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x9a\x974T")  # 0x9a973454
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spider_ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x8b\x9f`\xa3")  # 0x8b9f60a3
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.screw_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"uj6\x82")  # 0x756a3682
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.spring_ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BallMovementControlsJson", data)
        return cls(
            roll_forward=RevolutionControl.from_json(json_data["roll_forward"]),
            roll_backward=RevolutionControl.from_json(json_data["roll_backward"]),
            roll_left=RevolutionControl.from_json(json_data["roll_left"]),
            roll_right=RevolutionControl.from_json(json_data["roll_right"]),
            boost_ball=RevolutionControl.from_json(json_data["boost_ball"]),
            spider_ball=RevolutionControl.from_json(json_data["spider_ball"]),
            screw_attack=RevolutionControl.from_json(json_data["screw_attack"]),
            spring_ball=RevolutionControl.from_json(json_data["spring_ball"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "roll_forward": self.roll_forward.to_json(),
            "roll_backward": self.roll_backward.to_json(),
            "roll_left": self.roll_left.to_json(),
            "roll_right": self.roll_right.to_json(),
            "boost_ball": self.boost_ball.to_json(),
            "spider_ball": self.spider_ball.to_json(),
            "screw_attack": self.screw_attack.to_json(),
            "spring_ball": self.spring_ball.to_json(),
        }


def _decode_roll_forward(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_roll_backward(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_roll_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_roll_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_boost_ball(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_spider_ball(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_screw_attack(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_spring_ball(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xB4F29640: ("roll_forward", _decode_roll_forward),
    0xA25009D3: ("roll_backward", _decode_roll_backward),
    0x9CBA817B: ("roll_left", _decode_roll_left),
    0xCDC3A9CF: ("roll_right", _decode_roll_right),
    0x2F0E0276: ("boost_ball", _decode_boost_ball),
    0x9A973454: ("spider_ball", _decode_spider_ball),
    0x8B9F60A3: ("screw_attack", _decode_screw_attack),
    0x756A3682: ("spring_ball", _decode_spring_ball),
}
