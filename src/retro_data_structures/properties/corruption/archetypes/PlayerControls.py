# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.archetypes.BallMiscControls import BallMiscControls
from retro_data_structures.properties.corruption.archetypes.BallMovementControls import BallMovementControls
from retro_data_structures.properties.corruption.archetypes.CameraControls import CameraControls
from retro_data_structures.properties.corruption.archetypes.DebugControls import DebugControls
from retro_data_structures.properties.corruption.archetypes.MiscControls import MiscControls
from retro_data_structures.properties.corruption.archetypes.PlayerMiscControls import PlayerMiscControls
from retro_data_structures.properties.corruption.archetypes.PlayerMovementControls import PlayerMovementControls
from retro_data_structures.properties.corruption.archetypes.PlayerWeaponControls import PlayerWeaponControls
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class PlayerControlsJson(typing_extensions.TypedDict):
        unknown_0x4cf2b66e: json_util.JsonObject
        unknown_0x478b6c20: json_util.JsonObject
        unknown_0x49bd3f51: json_util.JsonObject
        unknown_0x61fe67a1: int
        ball_movement: json_util.JsonObject
        ball_misc: json_util.JsonObject
        unknown_0xd1777bf7: int
        camera: json_util.JsonObject
        misc: json_util.JsonObject
        debug: json_util.JsonObject


@dataclasses.dataclass()
class PlayerControls(BaseProperty):
    unknown_0x4cf2b66e: PlayerMovementControls = dataclasses.field(
        default_factory=PlayerMovementControls,
        metadata={
            "reflection": FieldReflection[PlayerMovementControls](
                PlayerMovementControls,
                id=0x4CF2B66E,
                original_name="Unknown",
                from_json=PlayerMovementControls.from_json,
                to_json=PlayerMovementControls.to_json,
            ),
        },
    )
    unknown_0x478b6c20: PlayerWeaponControls = dataclasses.field(
        default_factory=PlayerWeaponControls,
        metadata={
            "reflection": FieldReflection[PlayerWeaponControls](
                PlayerWeaponControls,
                id=0x478B6C20,
                original_name="Unknown",
                from_json=PlayerWeaponControls.from_json,
                to_json=PlayerWeaponControls.to_json,
            ),
        },
    )
    unknown_0x49bd3f51: PlayerMiscControls = dataclasses.field(
        default_factory=PlayerMiscControls,
        metadata={
            "reflection": FieldReflection[PlayerMiscControls](
                PlayerMiscControls,
                id=0x49BD3F51,
                original_name="Unknown",
                from_json=PlayerMiscControls.from_json,
                to_json=PlayerMiscControls.to_json,
            ),
        },
    )
    unknown_0x61fe67a1: int = dataclasses.field(
        default=61,
        metadata={
            "reflection": FieldReflection[int](int, id=0x61FE67A1, original_name="Unknown"),
        },
    )
    ball_movement: BallMovementControls = dataclasses.field(
        default_factory=BallMovementControls,
        metadata={
            "reflection": FieldReflection[BallMovementControls](
                BallMovementControls,
                id=0x1681D3E9,
                original_name="BallMovement",
                from_json=BallMovementControls.from_json,
                to_json=BallMovementControls.to_json,
            ),
        },
    )
    ball_misc: BallMiscControls = dataclasses.field(
        default_factory=BallMiscControls,
        metadata={
            "reflection": FieldReflection[BallMiscControls](
                BallMiscControls,
                id=0x0265E569,
                original_name="BallMisc",
                from_json=BallMiscControls.from_json,
                to_json=BallMiscControls.to_json,
            ),
        },
    )
    unknown_0xd1777bf7: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xD1777BF7, original_name="Unknown"),
        },
    )
    camera: CameraControls = dataclasses.field(
        default_factory=CameraControls,
        metadata={
            "reflection": FieldReflection[CameraControls](
                CameraControls,
                id=0x40E350AD,
                original_name="Camera",
                from_json=CameraControls.from_json,
                to_json=CameraControls.to_json,
            ),
        },
    )
    misc: MiscControls = dataclasses.field(
        default_factory=MiscControls,
        metadata={
            "reflection": FieldReflection[MiscControls](
                MiscControls,
                id=0xBE77DED2,
                original_name="Misc",
                from_json=MiscControls.from_json,
                to_json=MiscControls.to_json,
            ),
        },
    )
    debug: DebugControls = dataclasses.field(
        default_factory=DebugControls,
        metadata={
            "reflection": FieldReflection[DebugControls](
                DebugControls,
                id=0x47069911,
                original_name="Debug",
                from_json=DebugControls.from_json,
                to_json=DebugControls.to_json,
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
        assert property_id == 0x4CF2B66E
        unknown_0x4cf2b66e = PlayerMovementControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x478B6C20
        unknown_0x478b6c20 = PlayerWeaponControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49BD3F51
        unknown_0x49bd3f51 = PlayerMiscControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61FE67A1
        unknown_0x61fe67a1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1681D3E9
        ball_movement = BallMovementControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0265E569
        ball_misc = BallMiscControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD1777BF7
        unknown_0xd1777bf7 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40E350AD
        camera = CameraControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBE77DED2
        misc = MiscControls.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47069911
        debug = DebugControls.from_stream(data, game, property_size)

        return cls(
            unknown_0x4cf2b66e,
            unknown_0x478b6c20,
            unknown_0x49bd3f51,
            unknown_0x61fe67a1,
            ball_movement,
            ball_misc,
            unknown_0xd1777bf7,
            camera,
            misc,
            debug,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\n")  # 10 properties

        data.write(b"L\xf2\xb6n")  # 0x4cf2b66e
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x4cf2b66e.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"G\x8bl ")  # 0x478b6c20
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x478b6c20.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"I\xbd?Q")  # 0x49bd3f51
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.unknown_0x49bd3f51.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"a\xfeg\xa1")  # 0x61fe67a1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x61fe67a1))

        data.write(b"\x16\x81\xd3\xe9")  # 0x1681d3e9
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_movement.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x02e\xe5i")  # 0x265e569
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.ball_misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xd1w{\xf7")  # 0xd1777bf7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd1777bf7))

        data.write(b"@\xe3P\xad")  # 0x40e350ad
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbew\xde\xd2")  # 0xbe77ded2
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"G\x06\x99\x11")  # 0x47069911
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.debug.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerControlsJson", data)
        return cls(
            unknown_0x4cf2b66e=PlayerMovementControls.from_json(json_data["unknown_0x4cf2b66e"]),
            unknown_0x478b6c20=PlayerWeaponControls.from_json(json_data["unknown_0x478b6c20"]),
            unknown_0x49bd3f51=PlayerMiscControls.from_json(json_data["unknown_0x49bd3f51"]),
            unknown_0x61fe67a1=json_data["unknown_0x61fe67a1"],
            ball_movement=BallMovementControls.from_json(json_data["ball_movement"]),
            ball_misc=BallMiscControls.from_json(json_data["ball_misc"]),
            unknown_0xd1777bf7=json_data["unknown_0xd1777bf7"],
            camera=CameraControls.from_json(json_data["camera"]),
            misc=MiscControls.from_json(json_data["misc"]),
            debug=DebugControls.from_json(json_data["debug"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0x4cf2b66e": self.unknown_0x4cf2b66e.to_json(),
            "unknown_0x478b6c20": self.unknown_0x478b6c20.to_json(),
            "unknown_0x49bd3f51": self.unknown_0x49bd3f51.to_json(),
            "unknown_0x61fe67a1": self.unknown_0x61fe67a1,
            "ball_movement": self.ball_movement.to_json(),
            "ball_misc": self.ball_misc.to_json(),
            "unknown_0xd1777bf7": self.unknown_0xd1777bf7,
            "camera": self.camera.to_json(),
            "misc": self.misc.to_json(),
            "debug": self.debug.to_json(),
        }


def _decode_unknown_0x4cf2b66e(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerMovementControls:
    return PlayerMovementControls.from_stream(data, game, property_size)


def _decode_unknown_0x478b6c20(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerWeaponControls:
    return PlayerWeaponControls.from_stream(data, game, property_size)


def _decode_unknown_0x49bd3f51(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerMiscControls:
    return PlayerMiscControls.from_stream(data, game, property_size)


def _decode_ball_movement(data: typing.BinaryIO, game: Game, property_size: int) -> BallMovementControls:
    return BallMovementControls.from_stream(data, game, property_size)


def _decode_ball_misc(data: typing.BinaryIO, game: Game, property_size: int) -> BallMiscControls:
    return BallMiscControls.from_stream(data, game, property_size)


def _decode_camera(data: typing.BinaryIO, game: Game, property_size: int) -> CameraControls:
    return CameraControls.from_stream(data, game, property_size)


def _decode_misc(data: typing.BinaryIO, game: Game, property_size: int) -> MiscControls:
    return MiscControls.from_stream(data, game, property_size)


def _decode_debug(data: typing.BinaryIO, game: Game, property_size: int) -> DebugControls:
    return DebugControls.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4CF2B66E: ("unknown_0x4cf2b66e", _decode_unknown_0x4cf2b66e),
    0x478B6C20: ("unknown_0x478b6c20", _decode_unknown_0x478b6c20),
    0x49BD3F51: ("unknown_0x49bd3f51", _decode_unknown_0x49bd3f51),
    0x61FE67A1: ("unknown_0x61fe67a1", structs.decode_BIG_l),
    0x1681D3E9: ("ball_movement", _decode_ball_movement),
    0x0265E569: ("ball_misc", _decode_ball_misc),
    0xD1777BF7: ("unknown_0xd1777bf7", structs.decode_BIG_l),
    0x40E350AD: ("camera", _decode_camera),
    0xBE77DED2: ("misc", _decode_misc),
    0x47069911: ("debug", _decode_debug),
}
