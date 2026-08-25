# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct40Json(typing_extensions.TypedDict):
        main: int
        left: int
        right: int
        joint: str
        extend: json_util.JsonObject
        retract: json_util.JsonObject
        unknown_0x2eb71b6b: float
        unknown_0x25bd39c0: float
        open_time: float
        open_damage: float
        look_around_time: float
        unknown_0x193c048f: float
        stunned_time: float
        target_deploy_sound: int
        target_retract_sound: int


@dataclasses.dataclass()
class UnknownStruct40(BaseProperty):
    main: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0xC2376579, original_name="Main"),
        },
    )
    left: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x05032ED4, original_name="Left"),
        },
    )
    right: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CMDL"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x671DBFB5, original_name="Right"),
        },
    )
    joint: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x828932C1, original_name="Joint"),
        },
    )
    extend: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0xBFF185FA, original_name="Extend", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    retract: Spline = dataclasses.field(
        default_factory=Spline,
        metadata={
            "reflection": FieldReflection[Spline](
                Spline, id=0x1C846646, original_name="Retract", from_json=Spline.from_json, to_json=Spline.to_json
            ),
        },
    )
    unknown_0x2eb71b6b: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2EB71B6B, original_name="Unknown"),
        },
    )
    unknown_0x25bd39c0: float = dataclasses.field(
        default=3.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x25BD39C0, original_name="Unknown"),
        },
    )
    open_time: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFD54C300, original_name="OpenTime"),
        },
    )
    open_damage: float = dataclasses.field(
        default=100.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7EF9A719, original_name="OpenDamage"),
        },
    )
    look_around_time: float = dataclasses.field(
        default=1.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x257FE26E, original_name="LookAroundTime"),
        },
    )
    unknown_0x193c048f: float = dataclasses.field(
        default=0.5,
        metadata={
            "reflection": FieldReflection[float](float, id=0x193C048F, original_name="Unknown"),
        },
    )
    stunned_time: float = dataclasses.field(
        default=4.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8105ECFD, original_name="StunnedTime"),
        },
    )
    target_deploy_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x375F1663, original_name="TargetDeploySound"),
        },
    )
    target_retract_sound: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": ["CAUD"],
            "reflection": FieldReflection[AssetId](AssetId, id=0x68A51ABB, original_name="TargetRetractSound"),
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
        if property_count != 15:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC2376579
        main = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05032ED4
        left = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x671DBFB5
        right = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x828932C1
        joint = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBFF185FA
        extend = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1C846646
        retract = Spline.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2EB71B6B
        unknown_0x2eb71b6b = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25BD39C0
        unknown_0x25bd39c0 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFD54C300
        open_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7EF9A719
        open_damage = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x257FE26E
        look_around_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x193C048F
        unknown_0x193c048f = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8105ECFD
        stunned_time = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x375F1663
        target_deploy_sound = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68A51ABB
        target_retract_sound = structs.BIG_Q.unpack(data.read(8))[0]

        return cls(
            main,
            left,
            right,
            joint,
            extend,
            retract,
            unknown_0x2eb71b6b,
            unknown_0x25bd39c0,
            open_time,
            open_damage,
            look_around_time,
            unknown_0x193c048f,
            stunned_time,
            target_deploy_sound,
            target_retract_sound,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x0f")  # 15 properties

        data.write(b"\xc27ey")  # 0xc2376579
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.main))

        data.write(b"\x05\x03.\xd4")  # 0x5032ed4
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.left))

        data.write(b"g\x1d\xbf\xb5")  # 0x671dbfb5
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.right))

        data.write(b"\x82\x892\xc1")  # 0x828932c1
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.joint.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xbf\xf1\x85\xfa")  # 0xbff185fa
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.extend.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x1c\x84fF")  # 0x1c846646
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.retract.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b".\xb7\x1bk")  # 0x2eb71b6b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2eb71b6b))

        data.write(b"%\xbd9\xc0")  # 0x25bd39c0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x25bd39c0))

        data.write(b"\xfdT\xc3\x00")  # 0xfd54c300
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.open_time))

        data.write(b"~\xf9\xa7\x19")  # 0x7ef9a719
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.open_damage))

        data.write(b"%\x7f\xe2n")  # 0x257fe26e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.look_around_time))

        data.write(b"\x19<\x04\x8f")  # 0x193c048f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x193c048f))

        data.write(b"\x81\x05\xec\xfd")  # 0x8105ecfd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.stunned_time))

        data.write(b"7_\x16c")  # 0x375f1663
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.target_deploy_sound))

        data.write(b"h\xa5\x1a\xbb")  # 0x68a51abb
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.target_retract_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct40Json", data)
        return cls(
            main=json_data["main"],
            left=json_data["left"],
            right=json_data["right"],
            joint=json_data["joint"],
            extend=Spline.from_json(json_data["extend"]),
            retract=Spline.from_json(json_data["retract"]),
            unknown_0x2eb71b6b=json_data["unknown_0x2eb71b6b"],
            unknown_0x25bd39c0=json_data["unknown_0x25bd39c0"],
            open_time=json_data["open_time"],
            open_damage=json_data["open_damage"],
            look_around_time=json_data["look_around_time"],
            unknown_0x193c048f=json_data["unknown_0x193c048f"],
            stunned_time=json_data["stunned_time"],
            target_deploy_sound=json_data["target_deploy_sound"],
            target_retract_sound=json_data["target_retract_sound"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "main": self.main,
            "left": self.left,
            "right": self.right,
            "joint": self.joint,
            "extend": self.extend.to_json(),
            "retract": self.retract.to_json(),
            "unknown_0x2eb71b6b": self.unknown_0x2eb71b6b,
            "unknown_0x25bd39c0": self.unknown_0x25bd39c0,
            "open_time": self.open_time,
            "open_damage": self.open_damage,
            "look_around_time": self.look_around_time,
            "unknown_0x193c048f": self.unknown_0x193c048f,
            "stunned_time": self.stunned_time,
            "target_deploy_sound": self.target_deploy_sound,
            "target_retract_sound": self.target_retract_sound,
        }


def _decode_joint(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_extend(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_retract(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xC2376579: ("main", structs.decode_BIG_Q),
    0x05032ED4: ("left", structs.decode_BIG_Q),
    0x671DBFB5: ("right", structs.decode_BIG_Q),
    0x828932C1: ("joint", _decode_joint),
    0xBFF185FA: ("extend", _decode_extend),
    0x1C846646: ("retract", _decode_retract),
    0x2EB71B6B: ("unknown_0x2eb71b6b", structs.decode_BIG_f),
    0x25BD39C0: ("unknown_0x25bd39c0", structs.decode_BIG_f),
    0xFD54C300: ("open_time", structs.decode_BIG_f),
    0x7EF9A719: ("open_damage", structs.decode_BIG_f),
    0x257FE26E: ("look_around_time", structs.decode_BIG_f),
    0x193C048F: ("unknown_0x193c048f", structs.decode_BIG_f),
    0x8105ECFD: ("stunned_time", structs.decode_BIG_f),
    0x375F1663: ("target_deploy_sound", structs.decode_BIG_Q),
    0x68A51ABB: ("target_retract_sound", structs.decode_BIG_Q),
}
