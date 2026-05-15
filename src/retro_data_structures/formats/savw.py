"""
The SAVW format describes save data in the Metroid Prime series and Donkey Kong Country Returns.

Reference: https://wiki.axiodl.com/w/SAVW_(File_Format)
"""

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

import construct
from construct import Const, If, Int32ub, PrefixedArray

from retro_data_structures.adapters.enum_adapter import EnumAdapter
from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, Dependency
from retro_data_structures.common_types import GUID, String
from retro_data_structures.construct_extensions.alignment import AlignTo
from retro_data_structures.formats.script_object import InstanceId
from retro_data_structures.game_check import AssetIdCorrect, Game

if typing.TYPE_CHECKING:
    import uuid

    from retro_data_structures.formats.mlvl import Mlvl


class SavwVersion(enum.IntEnum):
    PRIME_1 = 3
    PRIME_2 = 5
    PRIME_3 = 6
    DKCR = 8


class _ConstructDataclass(typing.Protocol):
    @classmethod
    def parse(cls, raw: construct.Container) -> typing.Self: ...

    def build(self) -> construct.Container: ...


def dataclass_construct(subcon: construct.Construct, cls: type[_ConstructDataclass]) -> construct.Construct:
    return construct.ExprAdapter(
        subcon,
        decoder=lambda obj, ctx: cls.parse(obj),
        encoder=lambda obj, ctx: obj.build(),
    )


_SavedStateDescriptorConstruct = construct.Struct(
    guid=If(construct.this._root.version >= 6, GUID),
    instance_id=Int32ub,
)


@dataclass(frozen=True)
class SavedStateDescriptor:
    instance_id: InstanceId
    guid: uuid.UUID | None = None

    @classmethod
    def parse(cls, raw: construct.Container) -> typing.Self:
        return cls(
            instance_id=InstanceId(raw.instance_id),
            guid=raw.guid,
        )

    def build(self) -> construct.Container:
        return construct.Container(
            {
                "instance_id": self.instance_id,
                "guid": self.guid,
            }
        )


SavedStateDescriptorConstruct = dataclass_construct(_SavedStateDescriptorConstruct, SavedStateDescriptor)


_LayerToggleConstruct = construct.Struct(
    area_id=Int32ub,
    layer_index=Int32ub,
)


@dataclass(frozen=True)
class LayerToggle:
    area_id: int
    layer_index: int

    @classmethod
    def parse(cls, raw: construct.Container) -> typing.Self:
        return cls(area_id=raw.area_id, layer_index=raw.layer_index)

    def build(self) -> construct.Container:
        return construct.Container(
            {
                "area_id": self.area_id,
                "layer_index": self.layer_index,
            }
        )


LayerToggleConstruct = dataclass_construct(_LayerToggleConstruct, LayerToggle)

_ScannableObjectConstruct = construct.Struct(
    scan_asset_id=AssetIdCorrect,
    logbook_category=Int32ub,
)


@dataclass(frozen=True)
class ScannableObject:
    scan_asset_id: AssetId
    logbook_category: int = 0

    @classmethod
    def parse(cls, raw: construct.Container) -> typing.Self:
        return cls(scan_asset_id=raw.scan_asset_id, logbook_category=raw.logbook_category)

    def build(self) -> construct.Container:
        return construct.Container(
            {
                "scan_asset_id": self.scan_asset_id,
                "logbook_category": self.logbook_category,
            }
        )


ScannableObjectConstruct = dataclass_construct(_ScannableObjectConstruct, ScannableObject)


_EnvVarConstruct = construct.Struct(
    name=String,
    # Based on the wiki, these are always 0, 1 and 0 respectively. Their use is unknown.
    unk_a=Int32ub,
    unk_b=Int32ub,
    unk_c=Int32ub,
)


@dataclass(frozen=True)
class EnvVar:
    name: str
    _unk_a: int = 0
    _unk_b: int = 1
    _unk_c: int = 0

    @classmethod
    def parse(cls, raw: construct.Container) -> typing.Self:
        return cls(
            name=raw.name,
            _unk_a=raw.unk_a,
            _unk_b=raw.unk_b,
            _unk_c=raw.unk_c,
        )

    def build(self) -> construct.Container:
        return construct.Container(
            {
                "name": self.name,
                "unk_a": self._unk_a,
                "unk_b": self._unk_b,
                "unk_c": self._unk_c,
            }
        )


EnvVarConstruct = dataclass_construct(_EnvVarConstruct, EnvVar)


def _before_corruption(ctx: construct.Container) -> bool:
    return ctx.version < SavwVersion.PRIME_3


def _before_dkcr(ctx: construct.Container) -> bool:
    return ctx.version < SavwVersion.DKCR


def _starting_echoes(ctx: construct.Container) -> bool:
    return ctx.version >= SavwVersion.PRIME_2


def _echoes_or_corruption(ctx: construct.Container) -> bool:
    return ctx.version in {SavwVersion.PRIME_2, SavwVersion.PRIME_3}


def _starting_dkcr(ctx: construct.Container) -> bool:
    return ctx.version >= SavwVersion.DKCR


SAVW = construct.Struct(
    _magic=Const(0xC001D00D, Int32ub),
    version=EnumAdapter(SavwVersion),
    area_count=Int32ub,
    cinematic_skips=PrefixedArray(Int32ub, SavedStateDescriptorConstruct),
    memory_relays=PrefixedArray(Int32ub, SavedStateDescriptorConstruct),
    layer_toggles=If(_before_corruption, PrefixedArray(Int32ub, LayerToggleConstruct)),
    doors=If(_before_dkcr, PrefixedArray(Int32ub, SavedStateDescriptorConstruct)),
    scannable_objects=If(_before_dkcr, PrefixedArray(Int32ub, ScannableObjectConstruct)),
    system_state_env_vars=If(_starting_echoes, PrefixedArray(Int32ub, EnvVarConstruct)),
    game_state_env_vars=If(_starting_echoes, PrefixedArray(Int32ub, EnvVarConstruct)),
    unmappable_objects=If(_echoes_or_corruption, PrefixedArray(Int32ub, SavedStateDescriptorConstruct)),
    puzzle_pieces=If(_starting_dkcr, PrefixedArray(Int32ub, SavedStateDescriptorConstruct)),
    _align=AlignTo(lambda this: 64 if this.version >= SavwVersion.PRIME_3 else 32, b"\xff"),
    _end=construct.Terminated,
)


class Savw(BaseResource):
    @classmethod
    def resource_type(cls) -> AssetType:
        return "SAVW"

    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return SAVW

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        yield from []

    @property
    def version(self) -> SavwVersion:
        return self.raw.version

    @property
    def area_count(self) -> int:
        return self.raw.area_count

    @area_count.setter
    def area_count(self, value: int) -> None:
        self.raw.area_count = value

    @property
    def cinematic_skips(self) -> list[SavedStateDescriptor]:
        return self.raw.cinematic_skips

    @cinematic_skips.setter
    def cinematic_skips(self, value: list[SavedStateDescriptor]) -> None:
        self.raw.cinematic_skips = value

    @property
    def memory_relays(self) -> list[SavedStateDescriptor]:
        return self.raw.memory_relays

    @memory_relays.setter
    def memory_relays(self, value: list[SavedStateDescriptor]) -> None:
        self.raw.memory_relays = value

    @property
    def layer_toggles(self) -> list[LayerToggle]:
        return self.raw.layer_toggles

    @layer_toggles.setter
    def layer_toggles(self, value: list[LayerToggle]) -> None:
        self.raw.layer_toggles = value

    @property
    def doors(self) -> list[SavedStateDescriptor]:
        return self.raw.doors

    @doors.setter
    def doors(self, value: list[SavedStateDescriptor]) -> None:
        self.raw.doors = value

    @property
    def scannable_objects(self) -> list[ScannableObject]:
        return self.raw.scannable_objects

    @scannable_objects.setter
    def scannable_objects(self, value: list[ScannableObject]) -> None:
        self.raw.scannable_objects = value

    @property
    def system_state_env_vars(self) -> list[EnvVar]:
        return self.raw.system_state_env_vars

    @system_state_env_vars.setter
    def system_state_env_vars(self, value: list[EnvVar]) -> None:
        self.raw.system_state_env_vars = value

    @property
    def game_state_env_vars(self) -> list[EnvVar]:
        return self.raw.game_state_env_vars

    @game_state_env_vars.setter
    def game_state_env_vars(self, value: list[EnvVar]) -> None:
        self.raw.game_state_env_vars = value

    @property
    def unmappable_objects(self) -> list[SavedStateDescriptor]:
        return self.raw.unmappable_objects

    @unmappable_objects.setter
    def unmappable_objects(self, value: list[SavedStateDescriptor]) -> None:
        self.raw.unmappable_objects = value

    @property
    def puzzle_pieces(self) -> list[SavedStateDescriptor]:
        return self.raw.puzzle_pieces

    @puzzle_pieces.setter
    def puzzle_pieces(self, value: list[SavedStateDescriptor]) -> None:
        self.raw.puzzle_pieces = value

    def rebuild(self, mlvl: Mlvl) -> None:
        """
        Rebuilds this SAVW from scratch, iterating through the areas in
        its world to populate its various fields.
        """
        match self.version:
            case SavwVersion.PRIME_1:
                self._rebuild_p1(mlvl)
            case SavwVersion.PRIME_2:
                self._rebuild_p2(mlvl)
            case SavwVersion.PRIME_3:
                self._rebuild_p3(mlvl)
            case SavwVersion.DKCR:
                self._rebuild_dkcr(mlvl)

    def _rebuild_p1(self, mlvl: Mlvl) -> None:
        raise NotImplementedError

    def _rebuild_p2(self, mlvl: Mlvl) -> None:
        from retro_data_structures.properties.echoes.objects import Camera, Door, MemoryRelay, SpecialFunction
        from retro_data_structures.properties.echoes.objects.Camera import FlagsCinematicCamera
        from retro_data_structures.properties.echoes.objects.SpecialFunction import Function

        self.cinematic_skips = []
        self.memory_relays = []
        self.layer_toggles = []
        self.doors = []
        self.scannable_objects = []
        self.system_state_env_vars = []
        self.game_state_env_vars = []
        self.unmappable_objects = []

        self.area_count = mlvl.area_count

        for area in mlvl.areas:
            # scannable objects
            for dep in area.dependencies.all_dependencies:
                if dep.type == "SCAN" and dep.id not in self.scannable_objects:
                    self.scannable_objects.append(ScannableObject(dep.id))

            for instance in area.all_instances:
                # cinematic skips
                if instance.script_type == Camera:
                    flags = instance.get_properties_as(Camera).flags_cinematic_camera
                    if flags & FlagsCinematicCamera.CinematicSkip:
                        self.cinematic_skips.append(SavedStateDescriptor(instance.id))

                # memory relays
                elif instance.script_type == MemoryRelay:
                    self.memory_relays.append(SavedStateDescriptor(instance.id))

                # layer toggles
                # elif instance.script_type == ScriptLayerController:
                #     # we actually skip these. apparently they're always empty in echoes
                #     pass

                # doors
                elif instance.script_type == Door:
                    self.doors.append(SavedStateDescriptor(instance.id))

                elif instance.script_type == SpecialFunction:
                    sf_props = instance.get_properties_as(SpecialFunction)

                    match sf_props.function:
                        # system state env vars
                        case Function.GameStateSysVar:
                            self.system_state_env_vars.append(EnvVar(sf_props.string_parm))

                        # game state env vars
                        case Function.GameStateEnvVar:
                            self.game_state_env_vars.append(EnvVar(sf_props.string_parm))

                        # unmappable objects
                        case Function.TranslatorDoorLocation:
                            self.unmappable_objects.append(SavedStateDescriptor(instance.id))

    def _rebuild_p3(self, mlvl: Mlvl) -> None:
        raise NotImplementedError

    def _rebuild_dkcr(self, mlvl: Mlvl) -> None:
        raise NotImplementedError
