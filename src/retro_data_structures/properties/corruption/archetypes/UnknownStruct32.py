# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class UnknownStruct32Json(typing_extensions.TypedDict):
        initial_morph_time: float
        rundas_to_ghor: float
        rundas_to_gandrayda: float
        unknown_0x8e975bd2: float
        unknown_0xf848fa88: float
        ghor_to_gandrayda: float
        ghor_to_swarm: float
        unknown_0x9fa5117d: float
        unknown_0xc98d5dff: float
        gandrayda_to_ghor: float
        gandrayda_to_rundas: float
        gandrayda_to_swarm: float
        unknown_0xcbbd9a4e: float
        unknown_0x106d3edb: float
        unknown_0xa2675081: float
        unknown_0x413aee5b: float
        swarm_to_rundas: float
        swarm_to_gandrayda: float
        unknown_0x73ac8586: float
        unknown_0x704c4fc6: float
        unknown_0xc0597dc2: float
        unknown_0x4b605ddb: float
        unknown_0x931ea2ea: float
        unknown_0x7a11bb7b: float
        unknown_0xb4089be1: float
        unknown_0x118f6e87: float
        unknown_0x68737a67: float
        unknown_0xa771b575: float
        unknown_0x672a5c88: float


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (
    0x45161109,
    0xD26C1CAD,
    0x51B285B8,
    0x8E975BD2,
    0xF848FA88,
    0x824B8661,
    0xAB7E85A0,
    0x9FA5117D,
    0xC98D5DFF,
    0x99911B85,
    0x9F6FE573,
    0x8D7C6103,
    0xCBBD9A4E,
    0x106D3EDB,
    0xA2675081,
    0x413AEE5B,
    0x6C091AAF,
    0x20235A31,
    0x73AC8586,
    0x704C4FC6,
    0xC0597DC2,
    0x4B605DDB,
    0x931EA2EA,
    0x7A11BB7B,
    0xB4089BE1,
    0x118F6E87,
    0x68737A67,
    0xA771B575,
    0x672A5C88,
)


@dataclasses.dataclass()
class UnknownStruct32(BaseProperty):
    initial_morph_time: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x45161109, original_name="InitialMorphTime"),
        },
    )
    rundas_to_ghor: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xD26C1CAD, original_name="RundasToGhor"),
        },
    )
    rundas_to_gandrayda: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x51B285B8, original_name="RundasToGandrayda"),
        },
    )
    unknown_0x8e975bd2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8E975BD2, original_name="Unknown"),
        },
    )
    unknown_0xf848fa88: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xF848FA88, original_name="Unknown"),
        },
    )
    ghor_to_gandrayda: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x824B8661, original_name="GhorToGandrayda"),
        },
    )
    ghor_to_swarm: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xAB7E85A0, original_name="GhorToSwarm"),
        },
    )
    unknown_0x9fa5117d: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9FA5117D, original_name="Unknown"),
        },
    )
    unknown_0xc98d5dff: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC98D5DFF, original_name="Unknown"),
        },
    )
    gandrayda_to_ghor: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x99911B85, original_name="GandraydaToGhor"),
        },
    )
    gandrayda_to_rundas: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x9F6FE573, original_name="GandraydaToRundas"),
        },
    )
    gandrayda_to_swarm: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x8D7C6103, original_name="GandraydaToSwarm"),
        },
    )
    unknown_0xcbbd9a4e: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xCBBD9A4E, original_name="Unknown"),
        },
    )
    unknown_0x106d3edb: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x106D3EDB, original_name="Unknown"),
        },
    )
    unknown_0xa2675081: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA2675081, original_name="Unknown"),
        },
    )
    unknown_0x413aee5b: float = dataclasses.field(
        default=30.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x413AEE5B, original_name="Unknown"),
        },
    )
    swarm_to_rundas: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x6C091AAF, original_name="SwarmToRundas"),
        },
    )
    swarm_to_gandrayda: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x20235A31, original_name="SwarmToGandrayda"),
        },
    )
    unknown_0x73ac8586: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x73AC8586, original_name="Unknown"),
        },
    )
    unknown_0x704c4fc6: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x704C4FC6, original_name="Unknown"),
        },
    )
    unknown_0xc0597dc2: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xC0597DC2, original_name="Unknown"),
        },
    )
    unknown_0x4b605ddb: float = dataclasses.field(
        default=40.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x4B605DDB, original_name="Unknown"),
        },
    )
    unknown_0x931ea2ea: float = dataclasses.field(
        default=20.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x931EA2EA, original_name="Unknown"),
        },
    )
    unknown_0x7a11bb7b: float = dataclasses.field(
        default=80.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x7A11BB7B, original_name="Unknown"),
        },
    )
    unknown_0xb4089be1: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xB4089BE1, original_name="Unknown"),
        },
    )
    unknown_0x118f6e87: float = dataclasses.field(
        default=15.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x118F6E87, original_name="Unknown"),
        },
    )
    unknown_0x68737a67: float = dataclasses.field(
        default=85.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x68737A67, original_name="Unknown"),
        },
    )
    unknown_0xa771b575: float = dataclasses.field(
        default=50.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xA771B575, original_name="Unknown"),
        },
    )
    unknown_0x672a5c88: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x672A5C88, original_name="Unknown"),
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
        if property_count != 29:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(
                ">LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHf"
            )

        dec = _FAST_FORMAT.unpack(data.read(290))
        assert (
            dec[0],
            dec[3],
            dec[6],
            dec[9],
            dec[12],
            dec[15],
            dec[18],
            dec[21],
            dec[24],
            dec[27],
            dec[30],
            dec[33],
            dec[36],
            dec[39],
            dec[42],
            dec[45],
            dec[48],
            dec[51],
            dec[54],
            dec[57],
            dec[60],
            dec[63],
            dec[66],
            dec[69],
            dec[72],
            dec[75],
            dec[78],
            dec[81],
            dec[84],
        ) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
            dec[65],
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            dec[86],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x1d")  # 29 properties

        data.write(b"E\x16\x11\t")  # 0x45161109
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.initial_morph_time))

        data.write(b"\xd2l\x1c\xad")  # 0xd26c1cad
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rundas_to_ghor))

        data.write(b"Q\xb2\x85\xb8")  # 0x51b285b8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.rundas_to_gandrayda))

        data.write(b"\x8e\x97[\xd2")  # 0x8e975bd2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8e975bd2))

        data.write(b"\xf8H\xfa\x88")  # 0xf848fa88
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf848fa88))

        data.write(b"\x82K\x86a")  # 0x824b8661
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ghor_to_gandrayda))

        data.write(b"\xab~\x85\xa0")  # 0xab7e85a0
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.ghor_to_swarm))

        data.write(b"\x9f\xa5\x11}")  # 0x9fa5117d
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9fa5117d))

        data.write(b"\xc9\x8d]\xff")  # 0xc98d5dff
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc98d5dff))

        data.write(b"\x99\x91\x1b\x85")  # 0x99911b85
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gandrayda_to_ghor))

        data.write(b"\x9fo\xe5s")  # 0x9f6fe573
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gandrayda_to_rundas))

        data.write(b"\x8d|a\x03")  # 0x8d7c6103
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.gandrayda_to_swarm))

        data.write(b"\xcb\xbd\x9aN")  # 0xcbbd9a4e
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcbbd9a4e))

        data.write(b"\x10m>\xdb")  # 0x106d3edb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x106d3edb))

        data.write(b"\xa2gP\x81")  # 0xa2675081
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa2675081))

        data.write(b"A:\xee[")  # 0x413aee5b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x413aee5b))

        data.write(b"l\t\x1a\xaf")  # 0x6c091aaf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.swarm_to_rundas))

        data.write(b" #Z1")  # 0x20235a31
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.swarm_to_gandrayda))

        data.write(b"s\xac\x85\x86")  # 0x73ac8586
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x73ac8586))

        data.write(b"pLO\xc6")  # 0x704c4fc6
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x704c4fc6))

        data.write(b"\xc0Y}\xc2")  # 0xc0597dc2
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc0597dc2))

        data.write(b"K`]\xdb")  # 0x4b605ddb
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4b605ddb))

        data.write(b"\x93\x1e\xa2\xea")  # 0x931ea2ea
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x931ea2ea))

        data.write(b"z\x11\xbb{")  # 0x7a11bb7b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7a11bb7b))

        data.write(b"\xb4\x08\x9b\xe1")  # 0xb4089be1
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb4089be1))

        data.write(b"\x11\x8fn\x87")  # 0x118f6e87
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x118f6e87))

        data.write(b"hszg")  # 0x68737a67
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x68737a67))

        data.write(b"\xa7q\xb5u")  # 0xa771b575
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa771b575))

        data.write(b"g*\\\x88")  # 0x672a5c88
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.unknown_0x672a5c88))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("UnknownStruct32Json", data)
        return cls(
            initial_morph_time=json_data["initial_morph_time"],
            rundas_to_ghor=json_data["rundas_to_ghor"],
            rundas_to_gandrayda=json_data["rundas_to_gandrayda"],
            unknown_0x8e975bd2=json_data["unknown_0x8e975bd2"],
            unknown_0xf848fa88=json_data["unknown_0xf848fa88"],
            ghor_to_gandrayda=json_data["ghor_to_gandrayda"],
            ghor_to_swarm=json_data["ghor_to_swarm"],
            unknown_0x9fa5117d=json_data["unknown_0x9fa5117d"],
            unknown_0xc98d5dff=json_data["unknown_0xc98d5dff"],
            gandrayda_to_ghor=json_data["gandrayda_to_ghor"],
            gandrayda_to_rundas=json_data["gandrayda_to_rundas"],
            gandrayda_to_swarm=json_data["gandrayda_to_swarm"],
            unknown_0xcbbd9a4e=json_data["unknown_0xcbbd9a4e"],
            unknown_0x106d3edb=json_data["unknown_0x106d3edb"],
            unknown_0xa2675081=json_data["unknown_0xa2675081"],
            unknown_0x413aee5b=json_data["unknown_0x413aee5b"],
            swarm_to_rundas=json_data["swarm_to_rundas"],
            swarm_to_gandrayda=json_data["swarm_to_gandrayda"],
            unknown_0x73ac8586=json_data["unknown_0x73ac8586"],
            unknown_0x704c4fc6=json_data["unknown_0x704c4fc6"],
            unknown_0xc0597dc2=json_data["unknown_0xc0597dc2"],
            unknown_0x4b605ddb=json_data["unknown_0x4b605ddb"],
            unknown_0x931ea2ea=json_data["unknown_0x931ea2ea"],
            unknown_0x7a11bb7b=json_data["unknown_0x7a11bb7b"],
            unknown_0xb4089be1=json_data["unknown_0xb4089be1"],
            unknown_0x118f6e87=json_data["unknown_0x118f6e87"],
            unknown_0x68737a67=json_data["unknown_0x68737a67"],
            unknown_0xa771b575=json_data["unknown_0xa771b575"],
            unknown_0x672a5c88=json_data["unknown_0x672a5c88"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "initial_morph_time": self.initial_morph_time,
            "rundas_to_ghor": self.rundas_to_ghor,
            "rundas_to_gandrayda": self.rundas_to_gandrayda,
            "unknown_0x8e975bd2": self.unknown_0x8e975bd2,
            "unknown_0xf848fa88": self.unknown_0xf848fa88,
            "ghor_to_gandrayda": self.ghor_to_gandrayda,
            "ghor_to_swarm": self.ghor_to_swarm,
            "unknown_0x9fa5117d": self.unknown_0x9fa5117d,
            "unknown_0xc98d5dff": self.unknown_0xc98d5dff,
            "gandrayda_to_ghor": self.gandrayda_to_ghor,
            "gandrayda_to_rundas": self.gandrayda_to_rundas,
            "gandrayda_to_swarm": self.gandrayda_to_swarm,
            "unknown_0xcbbd9a4e": self.unknown_0xcbbd9a4e,
            "unknown_0x106d3edb": self.unknown_0x106d3edb,
            "unknown_0xa2675081": self.unknown_0xa2675081,
            "unknown_0x413aee5b": self.unknown_0x413aee5b,
            "swarm_to_rundas": self.swarm_to_rundas,
            "swarm_to_gandrayda": self.swarm_to_gandrayda,
            "unknown_0x73ac8586": self.unknown_0x73ac8586,
            "unknown_0x704c4fc6": self.unknown_0x704c4fc6,
            "unknown_0xc0597dc2": self.unknown_0xc0597dc2,
            "unknown_0x4b605ddb": self.unknown_0x4b605ddb,
            "unknown_0x931ea2ea": self.unknown_0x931ea2ea,
            "unknown_0x7a11bb7b": self.unknown_0x7a11bb7b,
            "unknown_0xb4089be1": self.unknown_0xb4089be1,
            "unknown_0x118f6e87": self.unknown_0x118f6e87,
            "unknown_0x68737a67": self.unknown_0x68737a67,
            "unknown_0xa771b575": self.unknown_0xa771b575,
            "unknown_0x672a5c88": self.unknown_0x672a5c88,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x45161109: ("initial_morph_time", structs.decode_BIG_f),
    0xD26C1CAD: ("rundas_to_ghor", structs.decode_BIG_f),
    0x51B285B8: ("rundas_to_gandrayda", structs.decode_BIG_f),
    0x8E975BD2: ("unknown_0x8e975bd2", structs.decode_BIG_f),
    0xF848FA88: ("unknown_0xf848fa88", structs.decode_BIG_f),
    0x824B8661: ("ghor_to_gandrayda", structs.decode_BIG_f),
    0xAB7E85A0: ("ghor_to_swarm", structs.decode_BIG_f),
    0x9FA5117D: ("unknown_0x9fa5117d", structs.decode_BIG_f),
    0xC98D5DFF: ("unknown_0xc98d5dff", structs.decode_BIG_f),
    0x99911B85: ("gandrayda_to_ghor", structs.decode_BIG_f),
    0x9F6FE573: ("gandrayda_to_rundas", structs.decode_BIG_f),
    0x8D7C6103: ("gandrayda_to_swarm", structs.decode_BIG_f),
    0xCBBD9A4E: ("unknown_0xcbbd9a4e", structs.decode_BIG_f),
    0x106D3EDB: ("unknown_0x106d3edb", structs.decode_BIG_f),
    0xA2675081: ("unknown_0xa2675081", structs.decode_BIG_f),
    0x413AEE5B: ("unknown_0x413aee5b", structs.decode_BIG_f),
    0x6C091AAF: ("swarm_to_rundas", structs.decode_BIG_f),
    0x20235A31: ("swarm_to_gandrayda", structs.decode_BIG_f),
    0x73AC8586: ("unknown_0x73ac8586", structs.decode_BIG_f),
    0x704C4FC6: ("unknown_0x704c4fc6", structs.decode_BIG_f),
    0xC0597DC2: ("unknown_0xc0597dc2", structs.decode_BIG_f),
    0x4B605DDB: ("unknown_0x4b605ddb", structs.decode_BIG_f),
    0x931EA2EA: ("unknown_0x931ea2ea", structs.decode_BIG_f),
    0x7A11BB7B: ("unknown_0x7a11bb7b", structs.decode_BIG_f),
    0xB4089BE1: ("unknown_0xb4089be1", structs.decode_BIG_f),
    0x118F6E87: ("unknown_0x118f6e87", structs.decode_BIG_f),
    0x68737A67: ("unknown_0x68737a67", structs.decode_BIG_f),
    0xA771B575: ("unknown_0xa771b575", structs.decode_BIG_f),
    0x672A5C88: ("unknown_0x672a5c88", structs.decode_BIG_f),
}
