# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game

    class ControlCommandsJson(typing_extensions.TypedDict):
        command: int


class Command(enum.IntEnum):
    Unknown1 = 3901647376
    Unknown2 = 2581939688
    Unknown3 = 2750450586
    Unknown4 = 899849925
    Unknown5 = 109932284
    Unknown6 = 2446731085
    Unknown7 = 3803725138
    Unknown8 = 2690424049
    Unknown9 = 3699295922
    Unknown10 = 3996274175
    Unknown11 = 137873876
    Unknown12 = 2167747411
    Unknown13 = 1231245019
    Unknown14 = 726214613
    Unknown15 = 1423451252
    Unknown16 = 3416415133
    Unknown17 = 4079415854
    Unknown18 = 55864240
    Unknown19 = 3156750812
    Unknown20 = 1848293130
    Unknown21 = 1773328712
    Unknown22 = 4121744237
    Unknown23 = 541928560
    Unknown24 = 1699049272
    Unknown25 = 1875089819
    Unknown26 = 785211435
    Unknown27 = 1067837646
    Unknown28 = 3534481192
    Unknown29 = 1362252510
    Unknown30 = 1135613235
    Unknown31 = 1130843359
    Unknown32 = 1387487870
    Unknown33 = 2991816435
    Unknown34 = 1198525559
    Unknown35 = 994331281
    Unknown36 = 1292212532
    Unknown37 = 3991851469
    Unknown38 = 1233152379
    Unknown39 = 3553892191
    Unknown40 = 2579448604
    Unknown41 = 2930622747
    Unknown42 = 2686272281
    Unknown43 = 4237958029
    Unknown44 = 4155323971
    Unknown45 = 1805149946
    Unknown46 = 3844960534
    Unknown47 = 3521809460
    Unknown48 = 4101879789
    Unknown49 = 2528966795
    Unknown50 = 980624810
    Unknown51 = 343759879
    Unknown52 = 4223842739
    Unknown53 = 283049438
    Unknown54 = 3520575665
    Unknown55 = 600453719
    Unknown56 = 1968064456
    Unknown57 = 3727723490
    Unknown58 = 3098082481
    Unknown59 = 2567258098
    Unknown60 = 2867761147
    Unknown61 = 3479224811
    Unknown62 = 534585026
    Unknown63 = 2992259733
    Unknown64 = 637210426
    Unknown65 = 2159907274
    Unknown66 = 3861243545
    Unknown67 = 2901285394
    Unknown68 = 2051261897
    Unknown69 = 1719198263
    Unknown70 = 340038035
    Unknown71 = 1288278651
    Unknown72 = 3321121544
    Unknown73 = 4107107956
    Unknown74 = 2877067267
    Unknown75 = 652527973
    Unknown76 = 3415844723
    Unknown77 = 1461157841
    Unknown78 = 1789003583
    Unknown79 = 3521624545
    Unknown80 = 3228790715
    Unknown81 = 2800425192
    Unknown82 = 2967516577
    Unknown83 = 996654954
    Unknown84 = 1684683972
    Unknown85 = 1520854483
    Unknown86 = 2724605556
    Unknown87 = 3305003303
    Unknown88 = 2148884262
    Unknown89 = 1360235495
    Unknown90 = 714095169
    Unknown91 = 2053486089
    Unknown92 = 315811492
    Unknown93 = 984481977
    Unknown94 = 3923398827
    Unknown95 = 322153173
    Unknown96 = 764797371
    Unknown97 = 3425615115
    Unknown98 = 3298385702
    Unknown99 = 2228281338
    Invalid1 = 2151003287
    Invalid2 = 156891041
    Invalid3 = 2599178616
    Invalid4 = 3674132153
    Invalid5 = 1530671344
    Invalid6 = 1448630541
    Invalid7 = 1820496063
    Invalid8 = 818144998
    Invalid9 = 3113676861
    Invalid10 = 3808326893
    Invalid11 = 2983710080
    Invalid12 = 3568842610
    Invalid13 = 1948874982
    Invalid14 = 179696054
    Invalid15 = 1301198552
    Invalid16 = 722911627
    Invalid17 = 1603950717
    Invalid18 = 2910162076
    Invalid19 = 1019209684
    Invalid20 = 2248942576
    Invalid21 = 3594513416
    Invalid22 = 177089843
    Invalid23 = 1225243796
    Invalid24 = 794959369
    Invalid25 = 4221452702

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = 0x418B3422


@dataclasses.dataclass()
class ControlCommands(BaseProperty):
    command: Command = dataclasses.field(
        default=Command.Unknown1,
        metadata={
            "reflection": FieldReflection[Command](
                Command, id=0x418B3422, original_name="Command", from_json=Command.from_json, to_json=Command.to_json
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
        if property_count != 1:
            return None

        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct(">LHL")

        dec = _FAST_FORMAT.unpack(data.read(10))
        assert (dec[0]) == _FAST_IDS
        return cls(
            Command(dec[2]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x01")  # 1 properties

        data.write(b'A\x8b4"')  # 0x418b3422
        data.write(b"\x00\x04")  # size
        self.command.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ControlCommandsJson", data)
        return cls(
            command=Command.from_json(json_data["command"]),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "command": self.command.to_json(),
        }


def _decode_command(data: typing.BinaryIO, game: Game, property_size: int) -> Command:
    return Command.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x418B3422: ("command", _decode_command),
}
