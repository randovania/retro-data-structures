# Generated File
# ruff: noqa: I001
from __future__ import annotations
import functools
import typing

from retro_data_structures.properties.echoes.objects.ActorKeyframe import ActorKeyframe
from retro_data_structures.properties.echoes.objects.AdvancedCounter import AdvancedCounter
from retro_data_structures.properties.echoes.objects.Actor import Actor
from retro_data_structures.properties.echoes.objects.AreaDamage import AreaDamage
from retro_data_structures.properties.echoes.objects.AIHint import AIHint
from retro_data_structures.properties.echoes.objects.AIKeyframe import AIKeyframe
from retro_data_structures.properties.echoes.objects.AIMannedTurret import AIMannedTurret
from retro_data_structures.properties.echoes.objects.AIWaypoint import AIWaypoint
from retro_data_structures.properties.echoes.objects.AIJumpPoint import AIJumpPoint
from retro_data_structures.properties.echoes.objects.AmbientAI import AmbientAI
from retro_data_structures.properties.echoes.objects.ActorRotate import ActorRotate
from retro_data_structures.properties.echoes.objects.AtomicAlpha import AtomicAlpha
from retro_data_structures.properties.echoes.objects.AtomicBeta import AtomicBeta
from retro_data_structures.properties.echoes.objects.SpiderBallAttractionSurface import SpiderBallAttractionSurface
from retro_data_structures.properties.echoes.objects.BallTrigger import BallTrigger
from retro_data_structures.properties.echoes.objects.SpiderBallWaypoint import SpiderBallWaypoint
from retro_data_structures.properties.echoes.objects.Blogg import Blogg
from retro_data_structures.properties.echoes.objects.CameraBlurKeyframe import CameraBlurKeyframe
from retro_data_structures.properties.echoes.objects.Brizgee import Brizgee
from retro_data_structures.properties.echoes.objects.BacteriaSwarm import BacteriaSwarm
from retro_data_structures.properties.echoes.objects.CameraHint import CameraHint
from retro_data_structures.properties.echoes.objects.CameraPitch import CameraPitch
from retro_data_structures.properties.echoes.objects.Camera import Camera
from retro_data_structures.properties.echoes.objects.CameraShaker import CameraShaker
from retro_data_structures.properties.echoes.objects.CameraWaypoint import CameraWaypoint
from retro_data_structures.properties.echoes.objects.CannonBall import CannonBall
from retro_data_structures.properties.echoes.objects.ChozoGhost import ChozoGhost
from retro_data_structures.properties.echoes.objects.ColorModulate import ColorModulate
from retro_data_structures.properties.echoes.objects.CommandoPirate import CommandoPirate
from retro_data_structures.properties.echoes.objects.ControllerAction import ControllerAction
from retro_data_structures.properties.echoes.objects.Counter import Counter
from retro_data_structures.properties.echoes.objects.Coin import Coin
from retro_data_structures.properties.echoes.objects.CoverPoint import CoverPoint
from retro_data_structures.properties.echoes.objects.Crystallite import Crystallite
from retro_data_structures.properties.echoes.objects.ConditionalRelay import ConditionalRelay
from retro_data_structures.properties.echoes.objects.ControlHint import ControlHint
from retro_data_structures.properties.echoes.objects.DestructibleBarrier import DestructibleBarrier
from retro_data_structures.properties.echoes.objects.Debris import Debris
from retro_data_structures.properties.echoes.objects.DebrisExtended import DebrisExtended
from retro_data_structures.properties.echoes.objects.DistanceFog import DistanceFog
from retro_data_structures.properties.echoes.objects.DigitalGuardianHead import DigitalGuardianHead
from retro_data_structures.properties.echoes.objects.DigitalGuardian import DigitalGuardian
from retro_data_structures.properties.echoes.objects.DarkTrooper import DarkTrooper
from retro_data_structures.properties.echoes.objects.DynamicLight import DynamicLight
from retro_data_structures.properties.echoes.objects.DamageActor import DamageActor
from retro_data_structures.properties.echoes.objects.Dock import Dock
from retro_data_structures.properties.echoes.objects.Door import Door
from retro_data_structures.properties.echoes.objects.DarkCommando import DarkCommando
from retro_data_structures.properties.echoes.objects.DarkSamus import DarkSamus
from retro_data_structures.properties.echoes.objects.DarkSamusBattleStage import DarkSamusBattleStage
from retro_data_structures.properties.echoes.objects.DamageableTrigger import DamageableTrigger
from retro_data_structures.properties.echoes.objects.DamageableTriggerOrientated import DamageableTriggerOrientated
from retro_data_structures.properties.echoes.objects.Effect import Effect
from retro_data_structures.properties.echoes.objects.EmperorIngStage2Tentacle import EmperorIngStage2Tentacle
from retro_data_structures.properties.echoes.objects.EMPulse import EMPulse
from retro_data_structures.properties.echoes.objects.EmperorIngStage1 import EmperorIngStage1
from retro_data_structures.properties.echoes.objects.EmperorIngStage3 import EmperorIngStage3
from retro_data_structures.properties.echoes.objects.ElitePirate import ElitePirate
from retro_data_structures.properties.echoes.objects.EyeBall import EyeBall
from retro_data_structures.properties.echoes.objects.ForgottenObject import ForgottenObject
from retro_data_structures.properties.echoes.objects.CameraFilterKeyframe import CameraFilterKeyframe
from retro_data_structures.properties.echoes.objects.FishCloud import FishCloud
from retro_data_structures.properties.echoes.objects.VisorFlare import VisorFlare
from retro_data_structures.properties.echoes.objects.FrontEndDataNetwork import FrontEndDataNetwork
from retro_data_structures.properties.echoes.objects.FogOverlay import FogOverlay
from retro_data_structures.properties.echoes.objects.FogVolume import FogVolume
from retro_data_structures.properties.echoes.objects.FlyingPirate import FlyingPirate
from retro_data_structures.properties.echoes.objects.FishCloudModifier import FishCloudModifier
from retro_data_structures.properties.echoes.objects.FlyerSwarm import FlyerSwarm
from retro_data_structures.properties.echoes.objects.EnvFxDensityController import EnvFxDensityController
from retro_data_structures.properties.echoes.objects.Glowbug import Glowbug
from retro_data_structures.properties.echoes.objects.Generator import Generator
from retro_data_structures.properties.echoes.objects.GuiMenu import GuiMenu
from retro_data_structures.properties.echoes.objects.GunTurretBase import GunTurretBase
from retro_data_structures.properties.echoes.objects.GunTurretTop import GunTurretTop
from retro_data_structures.properties.echoes.objects.GuiPlayerJoinManager import GuiPlayerJoinManager
from retro_data_structures.properties.echoes.objects.GrapplePoint import GrapplePoint
from retro_data_structures.properties.echoes.objects.Grenchler import Grenchler
from retro_data_structures.properties.echoes.objects.GuiScreen import GuiScreen
from retro_data_structures.properties.echoes.objects.GuiSlider import GuiSlider
from retro_data_structures.properties.echoes.objects.GuiWidget import GuiWidget
from retro_data_structures.properties.echoes.objects.HUDHint import HUDHint
from retro_data_structures.properties.echoes.objects.PlayerHint import PlayerHint
from retro_data_structures.properties.echoes.objects.IngBoostBallGuardian import IngBoostBallGuardian
from retro_data_structures.properties.echoes.objects.IngBlobSwarm import IngBlobSwarm
from retro_data_structures.properties.echoes.objects.Ing import Ing
from retro_data_structures.properties.echoes.objects.IngPuddle import IngPuddle
from retro_data_structures.properties.echoes.objects.IngSpiderballGuardian import IngSpiderballGuardian
from retro_data_structures.properties.echoes.objects.IngSpaceJumpGuardian import IngSpaceJumpGuardian
from retro_data_structures.properties.echoes.objects.IngSnatchingSwarm import IngSnatchingSwarm
from retro_data_structures.properties.echoes.objects.Kralee import Kralee
from retro_data_structures.properties.echoes.objects.Krocuss import Krocuss
from retro_data_structures.properties.echoes.objects.Lumite import Lumite
from retro_data_structures.properties.echoes.objects.HUDMemo import HUDMemo
from retro_data_structures.properties.echoes.objects.Midi import Midi
from retro_data_structures.properties.echoes.objects.MediumIng import MediumIng
from retro_data_structures.properties.echoes.objects.MinorIng import MinorIng
from retro_data_structures.properties.echoes.objects.StreamedMovie import StreamedMovie
from retro_data_structures.properties.echoes.objects.Metaree import Metaree
from retro_data_structures.properties.echoes.objects.MemoryRelay import MemoryRelay
from retro_data_structures.properties.echoes.objects.MetareeSwarm import MetareeSwarm
from retro_data_structures.properties.echoes.objects.MetroidAlpha import MetroidAlpha
from retro_data_structures.properties.echoes.objects.MysteryFlyer import MysteryFlyer
from retro_data_structures.properties.echoes.objects.OctapedeSegment import OctapedeSegment
from retro_data_structures.properties.echoes.objects.Parasite import Parasite
from retro_data_structures.properties.echoes.objects.PathCamera import PathCamera
from retro_data_structures.properties.echoes.objects.Pickup import Pickup
from retro_data_structures.properties.echoes.objects.PillBug import PillBug
from retro_data_structures.properties.echoes.objects.SpacePirate import SpacePirate
from retro_data_structures.properties.echoes.objects.PickupGenerator import PickupGenerator
from retro_data_structures.properties.echoes.objects.PlayerActor import PlayerActor
from retro_data_structures.properties.echoes.objects.Platform import Platform
from retro_data_structures.properties.echoes.objects.PlayerController import PlayerController
from retro_data_structures.properties.echoes.objects.PlayerTurret import PlayerTurret
from retro_data_structures.properties.echoes.objects.PathMeshCtrl import PathMeshCtrl
from retro_data_structures.properties.echoes.objects.PointOfInterest import PointOfInterest
from retro_data_structures.properties.echoes.objects.PortalTransition import PortalTransition
from retro_data_structures.properties.echoes.objects.PlayerStateChange import PlayerStateChange
from retro_data_structures.properties.echoes.objects.PlantScarabSwarm import PlantScarabSwarm
from retro_data_structures.properties.echoes.objects.Puffer import Puffer
from retro_data_structures.properties.echoes.objects.RadialDamage import RadialDamage
from retro_data_structures.properties.echoes.objects.RubiksPuzzle import RubiksPuzzle
from retro_data_structures.properties.echoes.objects.AreaAttributes import AreaAttributes
from retro_data_structures.properties.echoes.objects.Repulsor import Repulsor
from retro_data_structures.properties.echoes.objects.Rezbit import Rezbit
from retro_data_structures.properties.echoes.objects.Ripple import Ripple
from retro_data_structures.properties.echoes.objects.Ripper import Ripper
from retro_data_structures.properties.echoes.objects.RoomAcoustics import RoomAcoustics
from retro_data_structures.properties.echoes.objects.RiftPortal import RiftPortal
from retro_data_structures.properties.echoes.objects.RandomRelay import RandomRelay
from retro_data_structures.properties.echoes.objects.RsfAudio import RsfAudio
from retro_data_structures.properties.echoes.objects.RumbleEffect import RumbleEffect
from retro_data_structures.properties.echoes.objects.SafeZone import SafeZone
from retro_data_structures.properties.echoes.objects.SwampBossStage1 import SwampBossStage1
from retro_data_structures.properties.echoes.objects.SwampBossStage2 import SwampBossStage2
from retro_data_structures.properties.echoes.objects.ScanTreeInventory import ScanTreeInventory
from retro_data_structures.properties.echoes.objects.ScanTreeMenu import ScanTreeMenu
from retro_data_structures.properties.echoes.objects.ScanTreeCategory import ScanTreeCategory
from retro_data_structures.properties.echoes.objects.ScanTreeSlider import ScanTreeSlider
from retro_data_structures.properties.echoes.objects.ScanTreeScan import ScanTreeScan
from retro_data_structures.properties.echoes.objects.SafeZoneCrystal import SafeZoneCrystal
from retro_data_structures.properties.echoes.objects.ShadowProjector import ShadowProjector
from retro_data_structures.properties.echoes.objects.Shredder import Shredder
from retro_data_structures.properties.echoes.objects.Shrieker import Shrieker
from retro_data_structures.properties.echoes.objects.Silhouette import Silhouette
from retro_data_structures.properties.echoes.objects.SkyRipple import SkyRipple
from retro_data_structures.properties.echoes.objects.ScriptLayerController import ScriptLayerController
from retro_data_structures.properties.echoes.objects.SnakeWeedSwarm import SnakeWeedSwarm
from retro_data_structures.properties.echoes.objects.SandBoss import SandBoss
from retro_data_structures.properties.echoes.objects.SoundModifier import SoundModifier
from retro_data_structures.properties.echoes.objects.ScannableObjectInfo import ScannableObjectInfo
from retro_data_structures.properties.echoes.objects.Sound import Sound
from retro_data_structures.properties.echoes.objects.SporbBase import SporbBase
from retro_data_structures.properties.echoes.objects.SporbNeedle import SporbNeedle
from retro_data_structures.properties.echoes.objects.SporbProjectile import SporbProjectile
from retro_data_structures.properties.echoes.objects.SporbTop import SporbTop
from retro_data_structures.properties.echoes.objects.SpecialFunction import SpecialFunction
from retro_data_structures.properties.echoes.objects.Spinner import Spinner
from retro_data_structures.properties.echoes.objects.SplitterMainChassis import SplitterMainChassis
from retro_data_structures.properties.echoes.objects.SplitterCommandModule import SplitterCommandModule
from retro_data_structures.properties.echoes.objects.SpindleCamera import SpindleCamera
from retro_data_structures.properties.echoes.objects.SpankWeed import SpankWeed
from retro_data_structures.properties.echoes.objects.PuddleSpore import PuddleSpore
from retro_data_structures.properties.echoes.objects.Splinter import Splinter
from retro_data_structures.properties.echoes.objects.SpawnPoint import SpawnPoint
from retro_data_structures.properties.echoes.objects.SequenceTimer import SequenceTimer
from retro_data_structures.properties.echoes.objects.Relay import Relay
from retro_data_structures.properties.echoes.objects.StreamedAudio import StreamedAudio
from retro_data_structures.properties.echoes.objects.Steam import Steam
from retro_data_structures.properties.echoes.objects.StoneToad import StoneToad
from retro_data_structures.properties.echoes.objects.Subtitle import Subtitle
from retro_data_structures.properties.echoes.objects.SurfaceCamera import SurfaceCamera
from retro_data_structures.properties.echoes.objects.Switch import Switch
from retro_data_structures.properties.echoes.objects.WorldTeleporter import WorldTeleporter
from retro_data_structures.properties.echoes.objects.TargetingPoint import TargetingPoint
from retro_data_structures.properties.echoes.objects.Timer import Timer
from retro_data_structures.properties.echoes.objects.TimeKeyframe import TimeKeyframe
from retro_data_structures.properties.echoes.objects.TeamAI import TeamAI
from retro_data_structures.properties.echoes.objects.TriggerEllipsoid import TriggerEllipsoid
from retro_data_structures.properties.echoes.objects.TriggerOrientated import TriggerOrientated
from retro_data_structures.properties.echoes.objects.Trigger import Trigger
from retro_data_structures.properties.echoes.objects.Tryclops import Tryclops
from retro_data_structures.properties.echoes.objects.TweakAutoMapper import TweakAutoMapper
from retro_data_structures.properties.echoes.objects.TweakBall import TweakBall
from retro_data_structures.properties.echoes.objects.TweakPlayerControls import TweakPlayerControls
from retro_data_structures.properties.echoes.objects.TweakCameraBob import TweakCameraBob
from retro_data_structures.properties.echoes.objects.TweakGuiColors import TweakGuiColors
from retro_data_structures.properties.echoes.objects.TweakGame import TweakGame
from retro_data_structures.properties.echoes.objects.TweakGui import TweakGui
from retro_data_structures.properties.echoes.objects.TweakPlayer import TweakPlayer
from retro_data_structures.properties.echoes.objects.TweakParticle import TweakParticle
from retro_data_structures.properties.echoes.objects.TweakPlayerGun import TweakPlayerGun
from retro_data_structures.properties.echoes.objects.TweakPlayerRes import TweakPlayerRes
from retro_data_structures.properties.echoes.objects.TweakSlideShow import TweakSlideShow
from retro_data_structures.properties.echoes.objects.TweakTargeting import TweakTargeting
from retro_data_structures.properties.echoes.objects.TextPane import TextPane
from retro_data_structures.properties.echoes.objects.VisorGoo import VisorGoo
from retro_data_structures.properties.echoes.objects.Water import Water
from retro_data_structures.properties.echoes.objects.Waypoint import Waypoint
from retro_data_structures.properties.echoes.objects.WispTentacle import WispTentacle
from retro_data_structures.properties.echoes.objects.WorldLightFader import WorldLightFader
from retro_data_structures.properties.echoes.objects.WallWalker import WallWalker
from retro_data_structures.properties.echoes.objects.Sandworm import Sandworm

if typing.TYPE_CHECKING:
    from retro_data_structures.properties.base_property import BaseObjectType

_FOUR_CC_MAPPING: dict[str, type[BaseObjectType]] = {
    "ACKF": ActorKeyframe,
    "ACNT": AdvancedCounter,
    "ACTR": Actor,
    "ADMG": AreaDamage,
    "AIHT": AIHint,
    "AIKF": AIKeyframe,
    "AIMT": AIMannedTurret,
    "AIWP": AIWaypoint,
    "AJMP": AIJumpPoint,
    "AMIA": AmbientAI,
    "AROT": ActorRotate,
    "ATMA": AtomicAlpha,
    "ATMB": AtomicBeta,
    "BALS": SpiderBallAttractionSurface,
    "BALT": BallTrigger,
    "BALW": SpiderBallWaypoint,
    "BLOG": Blogg,
    "BLUR": CameraBlurKeyframe,
    "BRZG": Brizgee,
    "BSWM": BacteriaSwarm,
    "CAMH": CameraHint,
    "CAMP": CameraPitch,
    "CAMR": Camera,
    "CAMS": CameraShaker,
    "CAMW": CameraWaypoint,
    "CANB": CannonBall,
    "CHOG": ChozoGhost,
    "CLRM": ColorModulate,
    "CMDO": CommandoPirate,
    "CNTA": ControllerAction,
    "CNTR": Counter,
    "COIN": Coin,
    "COVR": CoverPoint,
    "CRLT": Crystallite,
    "CRLY": ConditionalRelay,
    "CTLH": ControlHint,
    "DBAR": DestructibleBarrier,
    "DBR1": Debris,
    "DBR2": DebrisExtended,
    "DFOG": DistanceFog,
    "DGHD": DigitalGuardianHead,
    "DGRD": DigitalGuardian,
    "DKTR": DarkTrooper,
    "DLHT": DynamicLight,
    "DMGA": DamageActor,
    "DOCK": Dock,
    "DOOR": Door,
    "DRKC": DarkCommando,
    "DRKS": DarkSamus,
    "DSBS": DarkSamusBattleStage,
    "DTRG": DamageableTrigger,
    "DTRO": DamageableTriggerOrientated,
    "EFCT": Effect,
    "EM2T": EmperorIngStage2Tentacle,
    "EMPU": EMPulse,
    "EMS1": EmperorIngStage1,
    "EMS3": EmperorIngStage3,
    "EPRT": ElitePirate,
    "EYEB": EyeBall,
    "FGTO": ForgottenObject,
    "FILT": CameraFilterKeyframe,
    "FISH": FishCloud,
    "FLAR": VisorFlare,
    "FNWK": FrontEndDataNetwork,
    "FOGO": FogOverlay,
    "FOGV": FogVolume,
    "FPRT": FlyingPirate,
    "FSHM": FishCloudModifier,
    "FSWM": FlyerSwarm,
    "FXDC": EnvFxDensityController,
    "GBUG": Glowbug,
    "GENR": Generator,
    "GMNU": GuiMenu,
    "GNTB": GunTurretBase,
    "GNTT": GunTurretTop,
    "GPJN": GuiPlayerJoinManager,
    "GRAP": GrapplePoint,
    "GRCH": Grenchler,
    "GSCR": GuiScreen,
    "GSLD": GuiSlider,
    "GWIG": GuiWidget,
    "HHNT": HUDHint,
    "HINT": PlayerHint,
    "IBBG": IngBoostBallGuardian,
    "IBSM": IngBlobSwarm,
    "INGS": Ing,
    "IPUD": IngPuddle,
    "ISBG": IngSpiderballGuardian,
    "ISJG": IngSpaceJumpGuardian,
    "ISSW": IngSnatchingSwarm,
    "KRAL": Kralee,
    "KROC": Krocuss,
    "LUMI": Lumite,
    "MEMO": HUDMemo,
    "MIDI": Midi,
    "MING": MediumIng,
    "MNNG": MinorIng,
    "MOVI": StreamedMovie,
    "MREE": Metaree,
    "MRLY": MemoryRelay,
    "MSWM": MetareeSwarm,
    "MTDA": MetroidAlpha,
    "MYSF": MysteryFlyer,
    "OCTS": OctapedeSegment,
    "PARA": Parasite,
    "PCAM": PathCamera,
    "PCKP": Pickup,
    "PILB": PillBug,
    "PIRT": SpacePirate,
    "PKGN": PickupGenerator,
    "PLAC": PlayerActor,
    "PLAT": Platform,
    "PLCT": PlayerController,
    "PLRT": PlayerTurret,
    "PMCT": PathMeshCtrl,
    "POIN": PointOfInterest,
    "PRTT": PortalTransition,
    "PSCH": PlayerStateChange,
    "PSSM": PlantScarabSwarm,
    "PUFR": Puffer,
    "RADD": RadialDamage,
    "RBPZ": RubiksPuzzle,
    "REAA": AreaAttributes,
    "REPL": Repulsor,
    "REZB": Rezbit,
    "RIPL": Ripple,
    "RIPR": Ripper,
    "RMAC": RoomAcoustics,
    "RPTL": RiftPortal,
    "RRLY": RandomRelay,
    "RSFA": RsfAudio,
    "RUMB": RumbleEffect,
    "SAFE": SafeZone,
    "SBS1": SwampBossStage1,
    "SBS2": SwampBossStage2,
    "SCIN": ScanTreeInventory,
    "SCMN": ScanTreeMenu,
    "SCND": ScanTreeCategory,
    "SCSL": ScanTreeSlider,
    "SCSN": ScanTreeScan,
    "SFZC": SafeZoneCrystal,
    "SHDW": ShadowProjector,
    "SHRD": Shredder,
    "SHRK": Shrieker,
    "SILH": Silhouette,
    "SKRP": SkyRipple,
    "SLCT": ScriptLayerController,
    "SNAK": SnakeWeedSwarm,
    "SNDB": SandBoss,
    "SNDM": SoundModifier,
    "SNFO": ScannableObjectInfo,
    "SOND": Sound,
    "SPBB": SporbBase,
    "SPBN": SporbNeedle,
    "SPBP": SporbProjectile,
    "SPBT": SporbTop,
    "SPFN": SpecialFunction,
    "SPIN": Spinner,
    "SPLL": SplitterMainChassis,
    "SPLU": SplitterCommandModule,
    "SPND": SpindleCamera,
    "SPNK": SpankWeed,
    "SPOR": PuddleSpore,
    "SPTR": Splinter,
    "SPWN": SpawnPoint,
    "SQTR": SequenceTimer,
    "SRLY": Relay,
    "STAU": StreamedAudio,
    "STEM": Steam,
    "STOD": StoneToad,
    "SUBT": Subtitle,
    "SURC": SurfaceCamera,
    "SWTC": Switch,
    "TEL1": WorldTeleporter,
    "TGPT": TargetingPoint,
    "TIMR": Timer,
    "TKEY": TimeKeyframe,
    "TMAI": TeamAI,
    "TRGE": TriggerEllipsoid,
    "TRGO": TriggerOrientated,
    "TRGR": Trigger,
    "TRYC": Tryclops,
    "TWAM": TweakAutoMapper,
    "TWBL": TweakBall,
    "TWC2": TweakPlayerControls,
    "TWCB": TweakCameraBob,
    "TWGC": TweakGuiColors,
    "TWGM": TweakGame,
    "TWGU": TweakGui,
    "TWP2": TweakPlayer,
    "TWPA": TweakParticle,
    "TWPC": TweakPlayerControls,
    "TWPG": TweakPlayerGun,
    "TWPL": TweakPlayer,
    "TWPM": TweakPlayerGun,
    "TWPR": TweakPlayerRes,
    "TWSS": TweakSlideShow,
    "TWTG": TweakTargeting,
    "TXPN": TextPane,
    "VGOO": VisorGoo,
    "WATR": Water,
    "WAYP": Waypoint,
    "WISP": WispTentacle,
    "WLIT": WorldLightFader,
    "WLWK": WallWalker,
    "WORM": Sandworm,
}


@functools.cache
def get_object(four_cc: str) -> type[BaseObjectType]:
    return _FOUR_CC_MAPPING[four_cc]
