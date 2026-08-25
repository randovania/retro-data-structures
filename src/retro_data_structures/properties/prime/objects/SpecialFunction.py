# Generated File
# ruff: noqa: F841, E501, PLR0915, PLW0603, PLR0912
from __future__ import annotations

import dataclasses
import enum
import typing

import typing_extensions

import retro_data_structures.enums.prime as enums
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.prime.archetypes.LayerSwitch import LayerSwitch
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from retro_data_structures import json_util
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency
    from retro_data_structures.game_check import Game

    class SpecialFunctionJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        function: int
        string_param: str
        value_param: float
        value_param2: float
        value_param3: float
        unnamed_0x00000008: json_util.JsonObject
        unnamed_0x00000009: int
        active: bool
        value_param4: float
        sound1: int
        sound2: int
        sound3: int


class Function(enum.IntEnum):
    Null = 0
    PlayerFollowLocator = 1
    SpinnerController = 2
    ObjectFollowLocator = 3
    ChaffTarget = 4
    InventoryActivator = 5
    MapStation = 6
    SaveStation = 7
    IntroBossRingController = 8
    ViewFrustumTester = 9
    ShotSpinnerController = 10
    EscapeSequence = 11
    BossEnergyBar = 12
    EndGame = 13
    HUDFadeIn = 14
    CinematicSkip = 15
    ScriptLayerController = 16
    RainSimulator = 17
    AreaDamage = 18
    ObjectFollowObject = 19
    RedundantHintSystem = 20
    DropBomb = 21
    ScaleActor = 22
    MissileStation = 23
    Billboard = 24
    PlayerInAreaRelay = 25
    HUDTarget = 26
    FogFader = 27
    EnterLogbook = 28
    PowerBombStation = 29
    Ending = 30
    FusionRelay = 31
    WeaponSwitch = 32
    FogVolume = 33
    RadialDamage = 34
    EnvFxDensityController = 35
    RumbleEffect = 36

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
    name: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000000, original_name="Name"),
        },
    )
    position: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000001, original_name="Position", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    rotation: Vector = dataclasses.field(
        default_factory=Vector,
        metadata={
            "reflection": FieldReflection[Vector](
                Vector, id=0x00000002, original_name="Rotation", from_json=Vector.from_json, to_json=Vector.to_json
            ),
        },
    )
    function: Function = dataclasses.field(
        default=Function.Null,
        metadata={
            "reflection": FieldReflection[Function](
                Function,
                id=0x00000003,
                original_name="Function",
                from_json=Function.from_json,
                to_json=Function.to_json,
            ),
        },
    )
    string_param: str = dataclasses.field(
        default="",
        metadata={
            "reflection": FieldReflection[str](str, id=0x00000004, original_name="StringParam"),
        },
    )
    value_param: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000005, original_name="ValueParam"),
        },
    )
    value_param2: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000006, original_name="ValueParam2"),
        },
    )
    value_param3: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x00000007, original_name="ValueParam3"),
        },
    )
    unnamed_0x00000008: LayerSwitch = dataclasses.field(
        default_factory=LayerSwitch,
        metadata={
            "reflection": FieldReflection[LayerSwitch](
                LayerSwitch,
                id=0x00000008,
                original_name="8",
                from_json=LayerSwitch.from_json,
                to_json=LayerSwitch.to_json,
            ),
        },
    )
    unnamed_0x00000009: enums.PlayerItemEnum = dataclasses.field(
        default=enums.PlayerItemEnum.PowerBeam,
        metadata={
            "reflection": FieldReflection[enums.PlayerItemEnum](
                enums.PlayerItemEnum,
                id=0x00000009,
                original_name="9",
                from_json=enums.PlayerItemEnum.from_json,
                to_json=enums.PlayerItemEnum.to_json,
            ),
        },
    )
    active: bool = dataclasses.field(
        default=False,
        metadata={
            "reflection": FieldReflection[bool](bool, id=0x0000000A, original_name="Active"),
        },
    )
    value_param4: float = dataclasses.field(
        default=0.0,
        metadata={
            "reflection": FieldReflection[float](float, id=0x0000000B, original_name="ValueParam4"),
        },
    )
    sound1: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000C, original_name="Sound1"),
        },
    )
    sound2: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000D, original_name="Sound2"),
        },
    )
    sound3: int = dataclasses.field(
        default=0,
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](int, id=0x0000000E, original_name="Sound3"),
        },
    )

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x3A

    @classmethod
    def from_stream(
        cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None
    ) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        function = Function.from_stream(data, game)
        string_param = b"".join(iter(lambda: data.read(1), b"\x00")).decode("utf-8")
        value_param = structs.BIG_f.unpack(data.read(4))[0]
        value_param2 = structs.BIG_f.unpack(data.read(4))[0]
        value_param3 = structs.BIG_f.unpack(data.read(4))[0]
        unnamed_0x00000008 = LayerSwitch.from_stream(data, game, property_size)
        unnamed_0x00000009 = enums.PlayerItemEnum.from_stream(data, game)
        active = structs.BIG_bool_.unpack(data.read(1))[0]
        value_param4 = structs.BIG_f.unpack(data.read(4))[0]
        sound1 = structs.BIG_l.unpack(data.read(4))[0]
        sound2 = structs.BIG_l.unpack(data.read(4))[0]
        sound3 = structs.BIG_l.unpack(data.read(4))[0]
        return cls(
            name,
            position,
            rotation,
            function,
            string_param,
            value_param,
            value_param2,
            value_param3,
            unnamed_0x00000008,
            unnamed_0x00000009,
            active,
            value_param4,
            sound1,
            sound2,
            sound3,
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b"\x00\x00\x00\x0f")  # 15 properties
        data.write(self.name.encode("utf-8"))
        data.write(b"\x00")
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.function.to_stream(data, game)
        data.write(self.string_param.encode("utf-8"))
        data.write(b"\x00")
        data.write(structs.BIG_f.pack(self.value_param))
        data.write(structs.BIG_f.pack(self.value_param2))
        data.write(structs.BIG_f.pack(self.value_param3))
        self.unnamed_0x00000008.to_stream(data, game)
        self.unnamed_0x00000009.to_stream(data, game)
        data.write(structs.BIG_bool_.pack(self.active))
        data.write(structs.BIG_f.pack(self.value_param4))
        data.write(structs.BIG_l.pack(self.sound1))
        data.write(structs.BIG_l.pack(self.sound2))
        data.write(structs.BIG_l.pack(self.sound3))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpecialFunctionJson", data)
        return cls(
            name=json_data["name"],
            position=Vector.from_json(json_data["position"]),
            rotation=Vector.from_json(json_data["rotation"]),
            function=Function.from_json(json_data["function"]),
            string_param=json_data["string_param"],
            value_param=json_data["value_param"],
            value_param2=json_data["value_param2"],
            value_param3=json_data["value_param3"],
            unnamed_0x00000008=LayerSwitch.from_json(json_data["unnamed_0x00000008"]),
            unnamed_0x00000009=enums.PlayerItemEnum.from_json(json_data["unnamed_0x00000009"]),
            active=json_data["active"],
            value_param4=json_data["value_param4"],
            sound1=json_data["sound1"],
            sound2=json_data["sound2"],
            sound3=json_data["sound3"],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            "name": self.name,
            "position": self.position.to_json(),
            "rotation": self.rotation.to_json(),
            "function": self.function.to_json(),
            "string_param": self.string_param,
            "value_param": self.value_param,
            "value_param2": self.value_param2,
            "value_param3": self.value_param3,
            "unnamed_0x00000008": self.unnamed_0x00000008.to_json(),
            "unnamed_0x00000009": self.unnamed_0x00000009.to_json(),
            "active": self.active,
            "value_param4": self.value_param4,
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
