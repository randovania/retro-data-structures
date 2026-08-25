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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class LODControllerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0x00b17e5f: int
        model01: int
        distance01: float
        model02: int
        distance02: float
        model03: int
        distance03: float
        model04: int
        distance04: float
        model05: int
        distance05: float
        model06: int
        distance06: float
        model07: int
        distance07: float
        model08: int
        distance08: float
        model09: int
        distance09: float
        model10: int
        distance10: float
        unknown_0xb67e3bf9: bool


@dataclasses.dataclass()
class LODController(BaseObjectType):
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
    unknown_0x00b17e5f: int = dataclasses.field(
        default=1,
        metadata={
            "reflection": FieldReflection[int](int, id=0x00B17E5F, original_name="Unknown"),
        },
    )
    model01: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x03BEE47E, original_name="Model01"),
        },
    )
    distance01: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA1018EF9, original_name="Distance01"),
        },
    )
    model02: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x852A96D0, original_name="Model02"),
        },
    )
    distance02: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2795FC57, original_name="Distance02"),
        },
    )
    model03: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x4E764575, original_name="Model03"),
        },
    )
    distance03: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xECC92FF2, original_name="Distance03"),
        },
    )
    model04: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x537375CD, original_name="Model04"),
        },
    )
    distance04: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF1CC1F4A, original_name="Distance04"),
        },
    )
    model05: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x982FA668, original_name="Model05"),
        },
    )
    distance05: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x3A90CCEF, original_name="Distance05"),
        },
    )
    model06: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x1EBBD4C6, original_name="Model06"),
        },
    )
    distance06: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xBC04BE41, original_name="Distance06"),
        },
    )
    model07: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xD5E70763, original_name="Model07"),
        },
    )
    distance07: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x77586DE4, original_name="Distance07"),
        },
    )
    model08: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x24B1B5B6, original_name="Model08"),
        },
    )
    distance08: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x860EDF31, original_name="Distance08"),
        },
    )
    model09: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0xEFED6613, original_name="Model09"),
        },
    )
    distance09: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4D520C94, original_name="Distance09"),
        },
    )
    model10: AssetId = dataclasses.field(
        default=default_asset_id,
        metadata={
            "asset_types": [],
            "reflection": FieldReflection[AssetId](AssetId, id=0x6E953C6F, original_name="Model10"),
        },
    )
    distance10: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCC2A56E8, original_name="Distance10"),
        },
    )
    unknown_0xb67e3bf9: bool = dataclasses.field(
        default=True,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0xB67E3BF9, original_name="Unknown"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "LODC"

    @classmethod
    def modules(cls) -> list[str]:
        return ["RSO_ScriptLODController.rso"]

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
        if property_count != 23:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00B17E5F
        unknown_0x00b17e5f = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03BEE47E
        model01 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA1018EF9
        distance01 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x852A96D0
        model02 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2795FC57
        distance02 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4E764575
        model03 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xECC92FF2
        distance03 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x537375CD
        model04 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xF1CC1F4A
        distance04 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x982FA668
        model05 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3A90CCEF
        distance05 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1EBBD4C6
        model06 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xBC04BE41
        distance06 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xD5E70763
        model07 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77586DE4
        distance07 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24B1B5B6
        model08 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x860EDF31
        distance08 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xEFED6613
        model09 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4D520C94
        distance09 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6E953C6F
        model10 = structs.BIG_Q.unpack(data.read(8))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xCC2A56E8
        distance10 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB67E3BF9
        unknown_0xb67e3bf9 = structs.BIG_bool_.unpack(data.read(1))[0]

        return cls(
            editor_properties,
            unknown_0x00b17e5f,
            model01,
            distance01,
            model02,
            distance02,
            model03,
            distance03,
            model04,
            distance04,
            model05,
            distance05,
            model06,
            distance06,
            model07,
            distance07,
            model08,
            distance08,
            model09,
            distance09,
            model10,
            distance10,
            unknown_0xb67e3bf9,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\x17")  # 23 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x00\xb1~_")  # 0xb17e5f
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x00b17e5f))

        data.write(b"\x03\xbe\xe4~")  # 0x3bee47e
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model01))

        data.write(b"\xa1\x01\x8e\xf9")  # 0xa1018ef9
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance01))

        data.write(b"\x85*\x96\xd0")  # 0x852a96d0
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model02))

        data.write(b"'\x95\xfcW")  # 0x2795fc57
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance02))

        data.write(b"NvEu")  # 0x4e764575
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model03))

        data.write(b"\xec\xc9/\xf2")  # 0xecc92ff2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance03))

        data.write(b"Ssu\xcd")  # 0x537375cd
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model04))

        data.write(b"\xf1\xcc\x1fJ")  # 0xf1cc1f4a
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance04))

        data.write(b"\x98/\xa6h")  # 0x982fa668
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model05))

        data.write(b":\x90\xcc\xef")  # 0x3a90ccef
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance05))

        data.write(b"\x1e\xbb\xd4\xc6")  # 0x1ebbd4c6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model06))

        data.write(b"\xbc\x04\xbeA")  # 0xbc04be41
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance06))

        data.write(b"\xd5\xe7\x07c")  # 0xd5e70763
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model07))

        data.write(b"wXm\xe4")  # 0x77586de4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance07))

        data.write(b"$\xb1\xb5\xb6")  # 0x24b1b5b6
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model08))

        data.write(b"\x86\x0e\xdf1")  # 0x860edf31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance08))

        data.write(b"\xef\xedf\x13")  # 0xefed6613
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model09))

        data.write(b"MR\x0c\x94")  # 0x4d520c94
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance09))

        data.write(b"n\x95<o")  # 0x6e953c6f
        data.write(b"\x00\x08")  # size
        data.write(structs.BIG_Q.pack(self.model10))

        data.write(b"\xcc*V\xe8")  # 0xcc2a56e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.distance10))

        data.write(b"\xb6~;\xf9")  # 0xb67e3bf9
        data.write(b"\x00\x01")  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xb67e3bf9))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LODControllerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            unknown_0x00b17e5f=json_data["unknown_0x00b17e5f"],
            model01=json_data["model01"],
            distance01=json_data["distance01"],
            model02=json_data["model02"],
            distance02=json_data["distance02"],
            model03=json_data["model03"],
            distance03=json_data["distance03"],
            model04=json_data["model04"],
            distance04=json_data["distance04"],
            model05=json_data["model05"],
            distance05=json_data["distance05"],
            model06=json_data["model06"],
            distance06=json_data["distance06"],
            model07=json_data["model07"],
            distance07=json_data["distance07"],
            model08=json_data["model08"],
            distance08=json_data["distance08"],
            model09=json_data["model09"],
            distance09=json_data["distance09"],
            model10=json_data["model10"],
            distance10=json_data["distance10"],
            unknown_0xb67e3bf9=json_data["unknown_0xb67e3bf9"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "unknown_0x00b17e5f": self.unknown_0x00b17e5f,
            "model01": self.model01,
            "distance01": self.distance01,
            "model02": self.model02,
            "distance02": self.distance02,
            "model03": self.model03,
            "distance03": self.distance03,
            "model04": self.model04,
            "distance04": self.distance04,
            "model05": self.model05,
            "distance05": self.distance05,
            "model06": self.model06,
            "distance06": self.distance06,
            "model07": self.model07,
            "distance07": self.distance07,
            "model08": self.model08,
            "distance08": self.distance08,
            "model09": self.model09,
            "distance09": self.distance09,
            "model10": self.model10,
            "distance10": self.distance10,
            "unknown_0xb67e3bf9": self.unknown_0xb67e3bf9,
        }


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x00B17E5F: ("unknown_0x00b17e5f", structs.decode_BIG_l),
    0x03BEE47E: ("model01", structs.decode_BIG_Q),
    0xA1018EF9: ("distance01", structs.decode_BIG_f),
    0x852A96D0: ("model02", structs.decode_BIG_Q),
    0x2795FC57: ("distance02", structs.decode_BIG_f),
    0x4E764575: ("model03", structs.decode_BIG_Q),
    0xECC92FF2: ("distance03", structs.decode_BIG_f),
    0x537375CD: ("model04", structs.decode_BIG_Q),
    0xF1CC1F4A: ("distance04", structs.decode_BIG_f),
    0x982FA668: ("model05", structs.decode_BIG_Q),
    0x3A90CCEF: ("distance05", structs.decode_BIG_f),
    0x1EBBD4C6: ("model06", structs.decode_BIG_Q),
    0xBC04BE41: ("distance06", structs.decode_BIG_f),
    0xD5E70763: ("model07", structs.decode_BIG_Q),
    0x77586DE4: ("distance07", structs.decode_BIG_f),
    0x24B1B5B6: ("model08", structs.decode_BIG_Q),
    0x860EDF31: ("distance08", structs.decode_BIG_f),
    0xEFED6613: ("model09", structs.decode_BIG_Q),
    0x4D520C94: ("distance09", structs.decode_BIG_f),
    0x6E953C6F: ("model10", structs.decode_BIG_Q),
    0xCC2A56E8: ("distance10", structs.decode_BIG_f),
    0xB67E3BF9: ("unknown_0xb67e3bf9", structs.decode_BIG_bool_),
}
