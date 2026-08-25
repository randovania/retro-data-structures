# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import struct
import typing

import typing_extensions

import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SpecialFunctionJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        function: int
        string_parm: str
        value_parm: float
        value_parm2: float
        value_parm3: float
        value_parm4: float
        int_parm1: int
        int_parm2: int
        inventory_item_parm: int
        sound1: int
        sound2: int
        sound3: int


class Function(enum.IntEnum):
    What = 0
    PlayerFollowLocator = 1
    SpinnerControllerUnused = 2
    ObjectFollowLocator = 3
    Function4Unused = 4
    InventoryActivator = 5
    MapStation = 6
    SaveStationCheckpoint = 7
    IntroBossRingControllerUnused = 8
    ViewFrustumTester = 9
    ShotSpinnerControllerUnused = 10
    EscapeSequence = 11
    BossEnergyBar = 12
    EndGame = 13
    HUDFadeInUnused = 14
    CinematicSkip = 15
    ScriptLayerControllerUnused = 16
    RainSimulatorUnused = 17
    AreaDamageUnused = 18
    ObjectFollowObject = 19
    RedundantHintSystem = 20
    DropBombUnused = 21
    Function22Unused = 22
    MissileStationUnused = 23
    BillboardUnused = 24
    PlayerInAreaRelay = 25
    HUDTargetUnused = 26
    FogFader = 27
    EnterLogbookScreenUnused = 28
    PowerBombStationUnused = 29
    Ending = 30
    FusionRelayUnused = 31
    WeaponSwitchUnused = 32
    LaunchPlayer = 33
    Function34Unused = 34
    Darkworld = 35
    Function36Unused = 36
    Function37Unused = 37
    Function38Unused = 38
    Function39Unused = 39
    SetNumPlayers___RemoveHackedEffect = 40
    EnableCannonBallDamage = 41
    ModifyInventoryAmount = 42
    IncrementDecrementPlayersJoinedCount = 43
    SetInventoryAmount = 44
    SetInventoryAmountAndCapacity = 45
    Function46Unused = 46
    AutomaticSunPlacement = 47
    Function48Unused = 48
    WipeOnOff___ = 49
    Function50Unused = 50
    InventoryLost = 51
    Function52Unused = 52
    SunGenerator = 53
    SkyFader = 54
    OcclusionRelay = 55
    MultiplayerCountdown = 56
    ScaleSZ = 57
    Attach___ = 58
    Function59Unused = 59
    ExtraRenderClipPlane = 60
    VisorBlowout = 61
    AreaAutoLoadController = 62
    GameStateSysVar = 63
    GameStateEnvVar = 64
    PlaySelectedMusicMultiplayer = 65
    TranslatorDoorLocation = 66
    CinematicSkipSignal = 67
    RemoveRezbitVirus = 68
    Credits = 69

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


@dataclasses.dataclass()
class SpecialFunction(BaseObjectType):
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
    function: Function = dataclasses.field(
        default=Function.What,
        metadata={
            "reflection": FieldReflection[Function](
                Function,
                id=0x95F8D644,
                original_name="Function",
                from_json=Function.from_json,
                to_json=Function.to_json,
            ),
        },
    )
    string_parm: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x9D7A576D, original_name="StringParm"),
        },
    )
    value_parm: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x19028099, original_name="ValueParm"),
        },
    )
    value_parm2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x2C93AAF5, original_name="ValueParm2"),
        },
    )
    value_parm3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xE7CF7950, original_name="ValueParm3"),
        },
    )
    value_parm4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0xFACA49E8, original_name="ValueParm4"),
        },
    )
    int_parm1: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xA734F8A5, original_name="IntParm1"),
        },
    )
    int_parm2: int = dataclasses.field(
        default=0,
        metadata={
            "reflection": FieldReflection[int](int, id=0xB581574B, original_name="IntParm2"),
        },
    )
    inventory_item_parm: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0x3FA164BC,
                original_name="InventoryItemParm",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    sound1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xA4EE16BF, original_name="Sound1"),
        },
    )
    sound2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x227A6411, original_name="Sound2"),
        },
    )
    sound3: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0xE926B7B4, original_name="Sound3"),
        },
    )

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return "SPFN"

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
        if property_count != 13:
            return None

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255A4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={"active": True})

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95F8D644
        function = Function.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9D7A576D
        string_parm = data.read(property_size)[:-1].decode("utf-8")

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19028099
        value_parm = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2C93AAF5
        value_parm2 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE7CF7950
        value_parm3 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xFACA49E8
        value_parm4 = structs.BIG_f.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA734F8A5
        int_parm1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xB581574B
        int_parm2 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3FA164BC
        inventory_item_parm = enums.PlayerItemEnum.from_stream(data, game)

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xA4EE16BF
        sound1 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x227A6411
        sound2 = structs.BIG_l.unpack(data.read(4))[0]

        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xE926B7B4
        sound3 = structs.BIG_l.unpack(data.read(4))[0]

        return cls(
            editor_properties,
            function,
            string_parm,
            value_parm,
            value_parm2,
            value_parm3,
            value_parm4,
            int_parm1,
            int_parm2,
            inventory_item_parm,
            sound1,
            sound2,
            sound3,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\xff\xff\xff\xff")  # struct object id
        root_size_offset = data.tell()
        data.write(b"\x00\x00")  # placeholder for root struct size
        data.write(b"\x00\r")  # 13 properties

        data.write(b"%ZE\x80")  # 0x255a4580
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={"active": True})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x95\xf8\xd6D")  # 0x95f8d644
        data.write(b"\x00\x04")  # size
        self.function.to_stream(data, game)

        data.write(b"\x9dzWm")  # 0x9d7a576d
        before = data.tell()
        data.write(b"\x00\x00")  # size placeholder
        data.write(self.string_parm.encode("utf-8"))
        data.write(b"\x00")
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x19\x02\x80\x99")  # 0x19028099
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.value_parm))

        data.write(b",\x93\xaa\xf5")  # 0x2c93aaf5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.value_parm2))

        data.write(b"\xe7\xcfyP")  # 0xe7cf7950
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.value_parm3))

        data.write(b"\xfa\xcaI\xe8")  # 0xfaca49e8
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_f.pack(self.value_parm4))

        data.write(b"\xa74\xf8\xa5")  # 0xa734f8a5
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.int_parm1))

        data.write(b"\xb5\x81WK")  # 0xb581574b
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.int_parm2))

        data.write(b"?\xa1d\xbc")  # 0x3fa164bc
        data.write(b"\x00\x04")  # size
        self.inventory_item_parm.to_stream(data, game)

        data.write(b"\xa4\xee\x16\xbf")  # 0xa4ee16bf
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound1))

        data.write(b'"zd\x11')  # 0x227a6411
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound2))

        data.write(b"\xe9&\xb7\xb4")  # 0xe926b7b4
        data.write(b"\x00\x04")  # size
        data.write(structs.BIG_l.pack(self.sound3))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpecialFunctionJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data["editor_properties"]),
            function=Function.from_json(json_data["function"]),
            string_parm=json_data["string_parm"],
            value_parm=json_data["value_parm"],
            value_parm2=json_data["value_parm2"],
            value_parm3=json_data["value_parm3"],
            value_parm4=json_data["value_parm4"],
            int_parm1=json_data["int_parm1"],
            int_parm2=json_data["int_parm2"],
            inventory_item_parm=enums.PlayerItemEnum.from_json(json_data["inventory_item_parm"]),
            sound1=json_data["sound1"],
            sound2=json_data["sound2"],
            sound3=json_data["sound3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "editor_properties": self.editor_properties.to_json(),
            "function": self.function.to_json(),
            "string_parm": self.string_parm,
            "value_parm": self.value_parm,
            "value_parm2": self.value_parm2,
            "value_parm3": self.value_parm3,
            "value_parm4": self.value_parm4,
            "int_parm1": self.int_parm1,
            "int_parm2": self.int_parm2,
            "inventory_item_parm": self.inventory_item_parm.to_json(),
            "sound1": self.sound1,
            "sound2": self.sound2,
            "sound3": self.sound3,
        }

    def _dependencies_for_sound1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound1)

    def _dependencies_for_sound2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound2)

    def _dependencies_for_sound3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound3)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_sound1, "sound1", "int"),
            (self._dependencies_for_sound2, "sound2", "int"),
            (self._dependencies_for_sound3, "sound3", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(f"Error finding dependencies for SpecialFunction.{field_name} ({field_type}): {e}")


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={"active": True})


def _decode_function(data: typing.BinaryIO, game: Game, property_size: int) -> Function:
    return Function.from_stream(data, game)


def _decode_string_parm(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8")


def _decode_inventory_item_parm(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255A4580: ("editor_properties", _decode_editor_properties),
    0x95F8D644: ("function", _decode_function),
    0x9D7A576D: ("string_parm", _decode_string_parm),
    0x19028099: ("value_parm", structs.decode_BIG_f),
    0x2C93AAF5: ("value_parm2", structs.decode_BIG_f),
    0xE7CF7950: ("value_parm3", structs.decode_BIG_f),
    0xFACA49E8: ("value_parm4", structs.decode_BIG_f),
    0xA734F8A5: ("int_parm1", structs.decode_BIG_l),
    0xB581574B: ("int_parm2", structs.decode_BIG_l),
    0x3FA164BC: ("inventory_item_parm", _decode_inventory_item_parm),
    0xA4EE16BF: ("sound1", structs.decode_BIG_l),
    0x227A6411: ("sound2", structs.decode_BIG_l),
    0xE926B7B4: ("sound3", structs.decode_BIG_l),
}
