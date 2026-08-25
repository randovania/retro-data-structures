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

    class TweakGui_MovieVolumesJson(typing_extensions.TypedDict):
        unknown_0xae149646: int
        unknown_0xc1a2e858: int
        unknown_0x138c3bb8: int
        unknown_0xe5587648: int
        unknown_0x9ed00248: int
        unknown_0x6f135424: int
        unknown_0xdb2260b7: int
        unknown_0xf38093f5: int


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xAE149646, 0xC1A2E858, 0x138C3BB8, 0xE5587648, 0x9ED00248, 0x6F135424, 0xDB2260B7, 0xF38093F5)


@dataclasses.dataclass()
class TweakGui_MovieVolumes(BaseProperty):
    unknown_0xae149646: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xAE149646, original_name="Unknown"),
        },
    )
    unknown_0xc1a2e858: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xC1A2E858, original_name="Unknown"),
        },
    )
    unknown_0x138c3bb8: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x138C3BB8, original_name="Unknown"),
        },
    )
    unknown_0xe5587648: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xE5587648, original_name="Unknown"),
        },
    )
    unknown_0x9ed00248: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x9ED00248, original_name="Unknown"),
        },
    )
    unknown_0x6f135424: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0x6F135424, original_name="Unknown"),
        },
    )
    unknown_0xdb2260b7: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xDB2260B7, original_name="Unknown"),
        },
    )
    unknown_0xf38093f5: int = dataclasses.field(
        default=127,
        metadata={
            "reflection": FieldReflection[int](int, id=0xF38093F5, original_name="Unknown"),
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

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHlLHlLHlLHlLHlLHlLHlLHl")

        dec = _FAST_FORMAT.unpack(data.read(80))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x08")  # 8 properties

        data.write(b"\xae\x14\x96F")  # 0xae149646
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xae149646))

        data.write(b"\xc1\xa2\xe8X")  # 0xc1a2e858
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc1a2e858))

        data.write(b"\x13\x8c;\xb8")  # 0x138c3bb8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x138c3bb8))

        data.write(b"\xe5XvH")  # 0xe5587648
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe5587648))

        data.write(b"\x9e\xd0\x02H")  # 0x9ed00248
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9ed00248))

        data.write(b"o\x13T$")  # 0x6f135424
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6f135424))

        data.write(b'\xdb"`\xb7')  # 0xdb2260b7
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xdb2260b7))

        data.write(b"\xf3\x80\x93\xf5")  # 0xf38093f5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.unknown_0xf38093f5))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_MovieVolumesJson", data)
        return cls(
            unknown_0xae149646=json_data["unknown_0xae149646"],
            unknown_0xc1a2e858=json_data["unknown_0xc1a2e858"],
            unknown_0x138c3bb8=json_data["unknown_0x138c3bb8"],
            unknown_0xe5587648=json_data["unknown_0xe5587648"],
            unknown_0x9ed00248=json_data["unknown_0x9ed00248"],
            unknown_0x6f135424=json_data["unknown_0x6f135424"],
            unknown_0xdb2260b7=json_data["unknown_0xdb2260b7"],
            unknown_0xf38093f5=json_data["unknown_0xf38093f5"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "unknown_0xae149646": self.unknown_0xae149646,
            "unknown_0xc1a2e858": self.unknown_0xc1a2e858,
            "unknown_0x138c3bb8": self.unknown_0x138c3bb8,
            "unknown_0xe5587648": self.unknown_0xe5587648,
            "unknown_0x9ed00248": self.unknown_0x9ed00248,
            "unknown_0x6f135424": self.unknown_0x6f135424,
            "unknown_0xdb2260b7": self.unknown_0xdb2260b7,
            "unknown_0xf38093f5": self.unknown_0xf38093f5,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xAE149646: ("unknown_0xae149646", structs.decode_BIG_l),
    0xC1A2E858: ("unknown_0xc1a2e858", structs.decode_BIG_l),
    0x138C3BB8: ("unknown_0x138c3bb8", structs.decode_BIG_l),
    0xE5587648: ("unknown_0xe5587648", structs.decode_BIG_l),
    0x9ED00248: ("unknown_0x9ed00248", structs.decode_BIG_l),
    0x6F135424: ("unknown_0x6f135424", structs.decode_BIG_l),
    0xDB2260B7: ("unknown_0xdb2260b7", structs.decode_BIG_l),
    0xF38093F5: ("unknown_0xf38093f5", structs.decode_BIG_l),
}
