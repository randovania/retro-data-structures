# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class AITaskPointJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        stay_forever: bool
        unknown_0xb553cda1: float
        unknown_0x53336240: float
        unknown_0x12341132: bool
        unknown_0xaaccd7cd: int
        idle_animation: int
        unknown_0x799f6f58: int
        unknown_0x121045f5: float
        unknown_0xf470ea14: float
        unknown_0x7aa31371: int
        unknown_0x0ac4d7ad: int
        unknown_0x03d511b9: int
        unknown_0x2bd321da: int
        unknown_0x2b3bd997: int
        unknown_0xc36101f6: int
        unknown_0x3fa8c740: int
        unknown_0x3aca31d7: int
        unknown_0xe5d4d300: int
        is_combat_task: bool
        unknown_0x2cf6f605: bool
        unknown_0x81591346: bool
        unknown_0xf874aa52: bool
        align_ai: bool
        unknown_0x2340b043: bool


@dataclasses.dataclass()
class AITaskPoint(BaseObjectType):
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
    stay_forever: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x56941EB7, original_name="StayForever"),
        },
    )
    unknown_0xb553cda1: float = dataclasses.field(
        default=1.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB553CDA1, original_name="Unknown"),
        },
    )
    unknown_0x53336240: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x53336240, original_name="Unknown"),
        },
    )
    unknown_0x12341132: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x12341132, original_name="Unknown"),
        },
    )
    unknown_0xaaccd7cd: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAACCD7CD, original_name="Unknown"),
        },
    )
    idle_animation: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA2A5B38F, original_name="IdleAnimation"),
        },
    )
    unknown_0x799f6f58: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x799F6F58, original_name="Unknown"),
        },
    )
    unknown_0x121045f5: float = dataclasses.field(
        default=5.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x121045F5, original_name="Unknown"),
        },
    )
    unknown_0xf470ea14: float = dataclasses.field(
        default=10.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF470EA14, original_name="Unknown"),
        },
    )
    unknown_0x7aa31371: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x7AA31371, original_name="Unknown"),
        },
    )
    unknown_0x0ac4d7ad: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x0AC4D7AD, original_name="Unknown"),
        },
    )
    unknown_0x03d511b9: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x03D511B9, original_name="Unknown"),
        },
    )
    unknown_0x2bd321da: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2BD321DA, original_name="Unknown"),
        },
    )
    unknown_0x2b3bd997: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x2B3BD997, original_name="Unknown"),
        },
    )
    unknown_0xc36101f6: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC36101F6, original_name="Unknown"),
        },
    )
    unknown_0x3fa8c740: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3FA8C740, original_name="Unknown"),
        },
    )
    unknown_0x3aca31d7: int = dataclasses.field(
        default=-1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x3ACA31D7, original_name="Unknown"),
        },
    )
    unknown_0xe5d4d300: int = dataclasses.field(
        default=8,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE5D4D300, original_name="Unknown"),
        },
    )
    is_combat_task: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2528F442, original_name="IsCombatTask"),
        },
    )
    unknown_0x2cf6f605: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2CF6F605, original_name="Unknown"),
        },
    )
    unknown_0x81591346: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x81591346, original_name="Unknown"),
        },
    )
    unknown_0xf874aa52: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xF874AA52, original_name="Unknown"),
        },
    )
    align_ai: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x5C20CF58, original_name="AlignAI"),
        },
    )
    unknown_0x2340b043: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x2340B043, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "AITP"

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
        if property_count != 25:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56941EB7
        stay_forever = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB553CDA1
        unknown_0xb553cda1 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53336240
        unknown_0x53336240 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12341132
        unknown_0x12341132 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xAACCD7CD
        unknown_0xaaccd7cd = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA2A5B38F
        idle_animation = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x799F6F58
        unknown_0x799f6f58 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x121045F5
        unknown_0x121045f5 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF470EA14
        unknown_0xf470ea14 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7AA31371
        unknown_0x7aa31371 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0AC4D7AD
        unknown_0x0ac4d7ad = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03D511B9
        unknown_0x03d511b9 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2BD321DA
        unknown_0x2bd321da = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2B3BD997
        unknown_0x2b3bd997 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xC36101F6
        unknown_0xc36101f6 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FA8C740
        unknown_0x3fa8c740 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ACA31D7
        unknown_0x3aca31d7 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE5D4D300
        unknown_0xe5d4d300 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2528F442
        is_combat_task = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2CF6F605
        unknown_0x2cf6f605 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81591346
        unknown_0x81591346 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF874AA52
        unknown_0xf874aa52 = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5C20CF58
        align_ai = structs.BIG_bool_.unpack(data.read(1))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2340B043
        unknown_0x2340b043 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            stay_forever,
            unknown_0xb553cda1,
            unknown_0x53336240,
            unknown_0x12341132,
            unknown_0xaaccd7cd,
            idle_animation,
            unknown_0x799f6f58,
            unknown_0x121045f5,
            unknown_0xf470ea14,
            unknown_0x7aa31371,
            unknown_0x0ac4d7ad,
            unknown_0x03d511b9,
            unknown_0x2bd321da,
            unknown_0x2b3bd997,
            unknown_0xc36101f6,
            unknown_0x3fa8c740,
            unknown_0x3aca31d7,
            unknown_0xe5d4d300,
            is_combat_task,
            unknown_0x2cf6f605,
            unknown_0x81591346,
            unknown_0xf874aa52,
            align_ai,
            unknown_0x2340b043,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x19")  # 25 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"V\x94\x1e\xb7")  # 0x56941eb7
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.stay_forever))

        data.write(b"\xb5S\xcd\xa1")  # 0xb553cda1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb553cda1))

        data.write(b"S3b@")  # 0x53336240
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x53336240))

        data.write(b"\x124\x112")  # 0x12341132
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x12341132))

        data.write(b"\xaa\xcc\xd7\xcd")  # 0xaaccd7cd
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xaaccd7cd))

        data.write(b"\xa2\xa5\xb3\x8f")  # 0xa2a5b38f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.idle_animation))

        data.write(b"y\x9foX")  # 0x799f6f58
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x799f6f58))

        data.write(b"\x12\x10E\xf5")  # 0x121045f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x121045f5))

        data.write(b"\xf4p\xea\x14")  # 0xf470ea14
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf470ea14))

        data.write(b"z\xa3\x13q")  # 0x7aa31371
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7aa31371))

        data.write(b"\n\xc4\xd7\xad")  # 0xac4d7ad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x0ac4d7ad))

        data.write(b"\x03\xd5\x11\xb9")  # 0x3d511b9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x03d511b9))

        data.write(b"+\xd3!\xda")  # 0x2bd321da
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2bd321da))

        data.write(b"+;\xd9\x97")  # 0x2b3bd997
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x2b3bd997))

        data.write(b"\xc3a\x01\xf6")  # 0xc36101f6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc36101f6))

        data.write(b"?\xa8\xc7@")  # 0x3fa8c740
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x3fa8c740))

        data.write(b":\xca1\xd7")  # 0x3aca31d7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x3aca31d7))

        data.write(b"\xe5\xd4\xd3\x00")  # 0xe5d4d300
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe5d4d300))

        data.write(b"%(\xf4B")  # 0x2528f442
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.is_combat_task))

        data.write(b",\xf6\xf6\x05")  # 0x2cf6f605
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2cf6f605))

        data.write(b"\x81Y\x13F")  # 0x81591346
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x81591346))

        data.write(b"\xf8t\xaaR")  # 0xf874aa52
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf874aa52))

        data.write(b"\\ \xcfX")  # 0x5c20cf58
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.align_ai))

        data.write(b"#@\xb0C")  # 0x2340b043
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2340b043))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AITaskPointJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            stay_forever=json_data["stay_forever"],
            unknown_0xb553cda1=json_data["unknown_0xb553cda1"],
            unknown_0x53336240=json_data["unknown_0x53336240"],
            unknown_0x12341132=json_data["unknown_0x12341132"],
            unknown_0xaaccd7cd=json_data["unknown_0xaaccd7cd"],
            idle_animation=json_data["idle_animation"],
            unknown_0x799f6f58=json_data["unknown_0x799f6f58"],
            unknown_0x121045f5=json_data["unknown_0x121045f5"],
            unknown_0xf470ea14=json_data["unknown_0xf470ea14"],
            unknown_0x7aa31371=json_data["unknown_0x7aa31371"],
            unknown_0x0ac4d7ad=json_data["unknown_0x0ac4d7ad"],
            unknown_0x03d511b9=json_data["unknown_0x03d511b9"],
            unknown_0x2bd321da=json_data["unknown_0x2bd321da"],
            unknown_0x2b3bd997=json_data["unknown_0x2b3bd997"],
            unknown_0xc36101f6=json_data["unknown_0xc36101f6"],
            unknown_0x3fa8c740=json_data["unknown_0x3fa8c740"],
            unknown_0x3aca31d7=json_data["unknown_0x3aca31d7"],
            unknown_0xe5d4d300=json_data["unknown_0xe5d4d300"],
            is_combat_task=json_data["is_combat_task"],
            unknown_0x2cf6f605=json_data["unknown_0x2cf6f605"],
            unknown_0x81591346=json_data["unknown_0x81591346"],
            unknown_0xf874aa52=json_data["unknown_0xf874aa52"],
            align_ai=json_data["align_ai"],
            unknown_0x2340b043=json_data["unknown_0x2340b043"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "stay_forever": self.stay_forever,
            "unknown_0xb553cda1": self.unknown_0xb553cda1,
            "unknown_0x53336240": self.unknown_0x53336240,
            "unknown_0x12341132": self.unknown_0x12341132,
            "unknown_0xaaccd7cd": self.unknown_0xaaccd7cd,
            "idle_animation": self.idle_animation,
            "unknown_0x799f6f58": self.unknown_0x799f6f58,
            "unknown_0x121045f5": self.unknown_0x121045f5,
            "unknown_0xf470ea14": self.unknown_0xf470ea14,
            "unknown_0x7aa31371": self.unknown_0x7aa31371,
            "unknown_0x0ac4d7ad": self.unknown_0x0ac4d7ad,
            "unknown_0x03d511b9": self.unknown_0x03d511b9,
            "unknown_0x2bd321da": self.unknown_0x2bd321da,
            "unknown_0x2b3bd997": self.unknown_0x2b3bd997,
            "unknown_0xc36101f6": self.unknown_0xc36101f6,
            "unknown_0x3fa8c740": self.unknown_0x3fa8c740,
            "unknown_0x3aca31d7": self.unknown_0x3aca31d7,
            "unknown_0xe5d4d300": self.unknown_0xe5d4d300,
            "is_combat_task": self.is_combat_task,
            "unknown_0x2cf6f605": self.unknown_0x2cf6f605,
            "unknown_0x81591346": self.unknown_0x81591346,
            "unknown_0xf874aa52": self.unknown_0xf874aa52,
            "align_ai": self.align_ai,
            "unknown_0x2340b043": self.unknown_0x2340b043,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x56941EB7: ("stay_forever", structs.decode_BIG_bool_),
    0xB553CDA1: ("unknown_0xb553cda1", structs.decode_BIG_f),
    0x53336240: ("unknown_0x53336240", structs.decode_BIG_f),
    0x12341132: ("unknown_0x12341132", structs.decode_BIG_bool_),
    0xAACCD7CD: ("unknown_0xaaccd7cd", structs.decode_BIG_l),
    0xA2A5B38F: ("idle_animation", structs.decode_BIG_l),
    0x799F6F58: ("unknown_0x799f6f58", structs.decode_BIG_l),
    0x121045F5: ("unknown_0x121045f5", structs.decode_BIG_f),
    0xF470EA14: ("unknown_0xf470ea14", structs.decode_BIG_f),
    0x7AA31371: ("unknown_0x7aa31371", structs.decode_BIG_l),
    0x0AC4D7AD: ("unknown_0x0ac4d7ad", structs.decode_BIG_l),
    0x03D511B9: ("unknown_0x03d511b9", structs.decode_BIG_l),
    0x2BD321DA: ("unknown_0x2bd321da", structs.decode_BIG_l),
    0x2B3BD997: ("unknown_0x2b3bd997", structs.decode_BIG_l),
    0xC36101F6: ("unknown_0xc36101f6", structs.decode_BIG_l),
    0x3FA8C740: ("unknown_0x3fa8c740", structs.decode_BIG_l),
    0x3ACA31D7: ("unknown_0x3aca31d7", structs.decode_BIG_l),
    0xE5D4D300: ("unknown_0xe5d4d300", structs.decode_BIG_l),
    0x2528F442: ("is_combat_task", structs.decode_BIG_bool_),
    0x2CF6F605: ("unknown_0x2cf6f605", structs.decode_BIG_bool_),
    0x81591346: ("unknown_0x81591346", structs.decode_BIG_bool_),
    0xF874AA52: ("unknown_0xf874aa52", structs.decode_BIG_bool_),
    0x5C20CF58: ("align_ai", structs.decode_BIG_bool_),
    0x2340B043: ("unknown_0x2340b043", structs.decode_BIG_bool_),
}
