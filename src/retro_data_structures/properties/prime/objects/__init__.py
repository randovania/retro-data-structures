# Generated File
# ruff: noqa: I001
from __future__ import annotations
import functools
import typing

from retro_data_structures.properties.prime.objects.Actor import Actor
from retro_data_structures.properties.prime.objects.Waypoint import Waypoint
from retro_data_structures.properties.prime.objects.Door import Door
from retro_data_structures.properties.prime.objects.Trigger import Trigger
from retro_data_structures.properties.prime.objects.Timer import Timer
from retro_data_structures.properties.prime.objects.Counter import Counter
from retro_data_structures.properties.prime.objects.Effect import Effect
from retro_data_structures.properties.prime.objects.Platform import Platform
from retro_data_structures.properties.prime.objects.Sound import Sound
from retro_data_structures.properties.prime.objects.Generator import Generator
from retro_data_structures.properties.prime.objects.Dock import Dock
from retro_data_structures.properties.prime.objects.Camera import Camera
from retro_data_structures.properties.prime.objects.CameraWaypoint import CameraWaypoint
from retro_data_structures.properties.prime.objects.NewIntroBoss import NewIntroBoss
from retro_data_structures.properties.prime.objects.SpawnPoint import SpawnPoint
from retro_data_structures.properties.prime.objects.CameraHint import CameraHint
from retro_data_structures.properties.prime.objects.Pickup import Pickup
from retro_data_structures.properties.prime.objects.MemoryRelay import MemoryRelay
from retro_data_structures.properties.prime.objects.RandomRelay import RandomRelay
from retro_data_structures.properties.prime.objects.Relay import Relay
from retro_data_structures.properties.prime.objects.Beetle import Beetle
from retro_data_structures.properties.prime.objects.HUDMemo import HUDMemo
from retro_data_structures.properties.prime.objects.CameraFilterKeyframe import CameraFilterKeyframe
from retro_data_structures.properties.prime.objects.CameraBlurKeyframe import CameraBlurKeyframe
from retro_data_structures.properties.prime.objects.DamageableTrigger import DamageableTrigger
from retro_data_structures.properties.prime.objects.Debris import Debris
from retro_data_structures.properties.prime.objects.CameraShaker import CameraShaker
from retro_data_structures.properties.prime.objects.ActorKeyframe import ActorKeyframe
from retro_data_structures.properties.prime.objects.Water import Water
from retro_data_structures.properties.prime.objects.WarWasp import WarWasp
from retro_data_structures.properties.prime.objects.SpacePirate import SpacePirate
from retro_data_structures.properties.prime.objects.FlyingPirate import FlyingPirate
from retro_data_structures.properties.prime.objects.ElitePirate import ElitePirate
from retro_data_structures.properties.prime.objects.MetroidBeta import MetroidBeta
from retro_data_structures.properties.prime.objects.ChozoGhost import ChozoGhost
from retro_data_structures.properties.prime.objects.CoverPoint import CoverPoint
from retro_data_structures.properties.prime.objects.SpiderBallWaypoint import SpiderBallWaypoint
from retro_data_structures.properties.prime.objects.BloodFlower import BloodFlower
from retro_data_structures.properties.prime.objects.FlickerBat import FlickerBat
from retro_data_structures.properties.prime.objects.PathCamera import PathCamera
from retro_data_structures.properties.prime.objects.GrapplePoint import GrapplePoint
from retro_data_structures.properties.prime.objects.PuddleSpore import PuddleSpore
from retro_data_structures.properties.prime.objects.DebugCameraWaypoint import DebugCameraWaypoint
from retro_data_structures.properties.prime.objects.SpiderBallAttractionSurface import SpiderBallAttractionSurface
from retro_data_structures.properties.prime.objects.PuddleToadGamma import PuddleToadGamma
from retro_data_structures.properties.prime.objects.DistanceFog import DistanceFog
from retro_data_structures.properties.prime.objects.FireFlea import FireFlea
from retro_data_structures.properties.prime.objects.MetareeAlpha import MetareeAlpha
from retro_data_structures.properties.prime.objects.DockAreaChange import DockAreaChange
from retro_data_structures.properties.prime.objects.ActorRotate import ActorRotate
from retro_data_structures.properties.prime.objects.SpecialFunction import SpecialFunction
from retro_data_structures.properties.prime.objects.SpankWeed import SpankWeed
from retro_data_structures.properties.prime.objects.Parasite import Parasite
from retro_data_structures.properties.prime.objects.PlayerHint import PlayerHint
from retro_data_structures.properties.prime.objects.Ripper import Ripper
from retro_data_structures.properties.prime.objects.PickupGenerator import PickupGenerator
from retro_data_structures.properties.prime.objects.AIKeyframe import AIKeyframe
from retro_data_structures.properties.prime.objects.PointOfInterest import PointOfInterest
from retro_data_structures.properties.prime.objects.Drone import Drone
from retro_data_structures.properties.prime.objects.MetroidAlpha import MetroidAlpha
from retro_data_structures.properties.prime.objects.DebrisExtended import DebrisExtended
from retro_data_structures.properties.prime.objects.Steam import Steam
from retro_data_structures.properties.prime.objects.Ripple import Ripple
from retro_data_structures.properties.prime.objects.BallTrigger import BallTrigger
from retro_data_structures.properties.prime.objects.TargetingPoint import TargetingPoint
from retro_data_structures.properties.prime.objects.ElectroMagneticPulse import ElectroMagneticPulse
from retro_data_structures.properties.prime.objects.IceSheegoth import IceSheegoth
from retro_data_structures.properties.prime.objects.PlayerActor import PlayerActor
from retro_data_structures.properties.prime.objects.Flaahgra import Flaahgra
from retro_data_structures.properties.prime.objects.AreaAttributes import AreaAttributes
from retro_data_structures.properties.prime.objects.FishCloud import FishCloud
from retro_data_structures.properties.prime.objects.FishCloudModifier import FishCloudModifier
from retro_data_structures.properties.prime.objects.VisorFlare import VisorFlare
from retro_data_structures.properties.prime.objects.WorldTeleporter import WorldTeleporter
from retro_data_structures.properties.prime.objects.VisorGoo import VisorGoo
from retro_data_structures.properties.prime.objects.JellyZap import JellyZap
from retro_data_structures.properties.prime.objects.ControllerAction import ControllerAction
from retro_data_structures.properties.prime.objects.Switch import Switch
from retro_data_structures.properties.prime.objects.PlayerStateChange import PlayerStateChange
from retro_data_structures.properties.prime.objects.Thardus import Thardus
from retro_data_structures.properties.prime.objects.WallCrawlerSwarm import WallCrawlerSwarm
from retro_data_structures.properties.prime.objects.AIJumpPoint import AIJumpPoint
from retro_data_structures.properties.prime.objects.FlaahgraTentacle import FlaahgraTentacle
from retro_data_structures.properties.prime.objects.RoomAcoustics import RoomAcoustics
from retro_data_structures.properties.prime.objects.ColorModulate import ColorModulate
from retro_data_structures.properties.prime.objects.ThardusRockProjectile import ThardusRockProjectile
from retro_data_structures.properties.prime.objects.Midi import Midi
from retro_data_structures.properties.prime.objects.StreamedAudio import StreamedAudio
from retro_data_structures.properties.prime.objects.Repulsor import Repulsor
from retro_data_structures.properties.prime.objects.GunTurret import GunTurret
from retro_data_structures.properties.prime.objects.FogVolume import FogVolume
from retro_data_structures.properties.prime.objects.Babygoth import Babygoth
from retro_data_structures.properties.prime.objects.Eyeball import Eyeball
from retro_data_structures.properties.prime.objects.RadialDamage import RadialDamage
from retro_data_structures.properties.prime.objects.CameraPitchVolume import CameraPitchVolume
from retro_data_structures.properties.prime.objects.EnvFxDensityController import EnvFxDensityController
from retro_data_structures.properties.prime.objects.Magdolite import Magdolite
from retro_data_structures.properties.prime.objects.TeamAIMgr import TeamAIMgr
from retro_data_structures.properties.prime.objects.SnakeWeedSwarm import SnakeWeedSwarm
from retro_data_structures.properties.prime.objects.ActorContraption import ActorContraption
from retro_data_structures.properties.prime.objects.Oculus import Oculus
from retro_data_structures.properties.prime.objects.Geemer import Geemer
from retro_data_structures.properties.prime.objects.SpindleCamera import SpindleCamera
from retro_data_structures.properties.prime.objects.AtomicAlpha import AtomicAlpha
from retro_data_structures.properties.prime.objects.CameraHintTrigger import CameraHintTrigger
from retro_data_structures.properties.prime.objects.RumbleEffect import RumbleEffect
from retro_data_structures.properties.prime.objects.AmbientAI import AmbientAI
from retro_data_structures.properties.prime.objects.AtomicBeta import AtomicBeta
from retro_data_structures.properties.prime.objects.IceZoomer import IceZoomer
from retro_data_structures.properties.prime.objects.Puffer import Puffer
from retro_data_structures.properties.prime.objects.Tryclops import Tryclops
from retro_data_structures.properties.prime.objects.Ridley import Ridley
from retro_data_structures.properties.prime.objects.Seedling import Seedling
from retro_data_structures.properties.prime.objects.ThermalHeatFader import ThermalHeatFader
from retro_data_structures.properties.prime.objects.Burrower import Burrower
from retro_data_structures.properties.prime.objects.ScriptBeam import ScriptBeam
from retro_data_structures.properties.prime.objects.WorldLightFader import WorldLightFader
from retro_data_structures.properties.prime.objects.MetroidPrimeStage2 import MetroidPrimeStage2
from retro_data_structures.properties.prime.objects.MetroidPrimeStage1 import MetroidPrimeStage1
from retro_data_structures.properties.prime.objects.MazeNode import MazeNode
from retro_data_structures.properties.prime.objects.OmegaPirate import OmegaPirate
from retro_data_structures.properties.prime.objects.PhazonPool import PhazonPool
from retro_data_structures.properties.prime.objects.PhazonHealingNodule import PhazonHealingNodule
from retro_data_structures.properties.prime.objects.NewCameraShaker import NewCameraShaker
from retro_data_structures.properties.prime.objects.ShadowProjector import ShadowProjector
from retro_data_structures.properties.prime.objects.EnergyBall import EnergyBall

if typing.TYPE_CHECKING:
    from retro_data_structures.properties.base_property import BaseObjectType

_FOUR_CC_MAPPING: dict[int, type[BaseObjectType]] = {
    0x0: Actor,
    0x2: Waypoint,
    0x3: Door,
    0x4: Trigger,
    0x5: Timer,
    0x6: Counter,
    0x7: Effect,
    0x8: Platform,
    0x9: Sound,
    0xA: Generator,
    0xB: Dock,
    0xC: Camera,
    0xD: CameraWaypoint,
    0xE: NewIntroBoss,
    0xF: SpawnPoint,
    0x10: CameraHint,
    0x11: Pickup,
    0x13: MemoryRelay,
    0x14: RandomRelay,
    0x15: Relay,
    0x16: Beetle,
    0x17: HUDMemo,
    0x18: CameraFilterKeyframe,
    0x19: CameraBlurKeyframe,
    0x1A: DamageableTrigger,
    0x1B: Debris,
    0x1C: CameraShaker,
    0x1D: ActorKeyframe,
    0x20: Water,
    0x21: WarWasp,
    0x24: SpacePirate,
    0x25: FlyingPirate,
    0x26: ElitePirate,
    0x27: MetroidBeta,
    0x28: ChozoGhost,
    0x2A: CoverPoint,
    0x2C: SpiderBallWaypoint,
    0x2D: BloodFlower,
    0x2E: FlickerBat,
    0x2F: PathCamera,
    0x30: GrapplePoint,
    0x31: PuddleSpore,
    0x32: DebugCameraWaypoint,
    0x33: SpiderBallAttractionSurface,
    0x34: PuddleToadGamma,
    0x35: DistanceFog,
    0x36: FireFlea,
    0x37: MetareeAlpha,
    0x38: DockAreaChange,
    0x39: ActorRotate,
    0x3A: SpecialFunction,
    0x3B: SpankWeed,
    0x3D: Parasite,
    0x3E: PlayerHint,
    0x3F: Ripper,
    0x40: PickupGenerator,
    0x41: AIKeyframe,
    0x42: PointOfInterest,
    0x43: Drone,
    0x44: MetroidAlpha,
    0x45: DebrisExtended,
    0x46: Steam,
    0x47: Ripple,
    0x48: BallTrigger,
    0x49: TargetingPoint,
    0x4A: ElectroMagneticPulse,
    0x4B: IceSheegoth,
    0x4C: PlayerActor,
    0x4D: Flaahgra,
    0x4E: AreaAttributes,
    0x4F: FishCloud,
    0x50: FishCloudModifier,
    0x51: VisorFlare,
    0x52: WorldTeleporter,
    0x53: VisorGoo,
    0x54: JellyZap,
    0x55: ControllerAction,
    0x56: Switch,
    0x57: PlayerStateChange,
    0x58: Thardus,
    0x5A: WallCrawlerSwarm,
    0x5B: AIJumpPoint,
    0x5C: FlaahgraTentacle,
    0x5D: RoomAcoustics,
    0x5E: ColorModulate,
    0x5F: ThardusRockProjectile,
    0x60: Midi,
    0x61: StreamedAudio,
    0x62: WorldTeleporter,
    0x63: Repulsor,
    0x64: GunTurret,
    0x65: FogVolume,
    0x66: Babygoth,
    0x67: Eyeball,
    0x68: RadialDamage,
    0x69: CameraPitchVolume,
    0x6A: EnvFxDensityController,
    0x6B: Magdolite,
    0x6C: TeamAIMgr,
    0x6D: SnakeWeedSwarm,
    0x6E: ActorContraption,
    0x6F: Oculus,
    0x70: Geemer,
    0x71: SpindleCamera,
    0x72: AtomicAlpha,
    0x73: CameraHintTrigger,
    0x74: RumbleEffect,
    0x75: AmbientAI,
    0x77: AtomicBeta,
    0x78: IceZoomer,
    0x79: Puffer,
    0x7A: Tryclops,
    0x7B: Ridley,
    0x7C: Seedling,
    0x7D: ThermalHeatFader,
    0x7F: Burrower,
    0x81: ScriptBeam,
    0x82: WorldLightFader,
    0x83: MetroidPrimeStage2,
    0x84: MetroidPrimeStage1,
    0x85: MazeNode,
    0x86: OmegaPirate,
    0x87: PhazonPool,
    0x88: PhazonHealingNodule,
    0x89: NewCameraShaker,
    0x8A: ShadowProjector,
    0x8B: EnergyBall,
}


@functools.cache
def get_object(four_cc: int) -> type[BaseObjectType]:
    return _FOUR_CC_MAPPING[four_cc]
