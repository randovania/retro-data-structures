# Generated File
# ruff: noqa: I001
from __future__ import annotations
import functools
import typing

from retro_data_structures.properties.corruption.objects.Achievement import Achievement
from retro_data_structures.properties.corruption.objects.ActorKeyframe import ActorKeyframe
from retro_data_structures.properties.corruption.objects.Actor import Actor
from retro_data_structures.properties.corruption.objects.AreaDamage import AreaDamage
from retro_data_structures.properties.corruption.objects.AIFuse import AIFuse
from retro_data_structures.properties.corruption.objects.AIHint import AIHint
from retro_data_structures.properties.corruption.objects.AIKeyframe import AIKeyframe
from retro_data_structures.properties.corruption.objects.AITaskPoint import AITaskPoint
from retro_data_structures.properties.corruption.objects.AIWaypoint import AIWaypoint
from retro_data_structures.properties.corruption.objects.AlarmController import AlarmController
from retro_data_structures.properties.corruption.objects.AmbientAI import AmbientAI
from retro_data_structures.properties.corruption.objects.ActorMorph import ActorMorph
from retro_data_structures.properties.corruption.objects.AudioOccluder import AudioOccluder
from retro_data_structures.properties.corruption.objects.AreaStreamedAudioState import AreaStreamedAudioState
from retro_data_structures.properties.corruption.objects.AtomicAlpha import AtomicAlpha
from retro_data_structures.properties.corruption.objects.ActorTransform import ActorTransform
from retro_data_structures.properties.corruption.objects.AuroraUnit1 import AuroraUnit1
from retro_data_structures.properties.corruption.objects.AuroraUnit2 import AuroraUnit2
from retro_data_structures.properties.corruption.objects.AudioVisualizer import AudioVisualizer
from retro_data_structures.properties.corruption.objects.AreaVisitMapController import AreaVisitMapController
from retro_data_structures.properties.corruption.objects.SpiderBallAttractionSurface import SpiderBallAttractionSurface
from retro_data_structures.properties.corruption.objects.BallTrigger import BallTrigger
from retro_data_structures.properties.corruption.objects.SpiderBallWaypoint import SpiderBallWaypoint
from retro_data_structures.properties.corruption.objects.Beam import Beam
from retro_data_structures.properties.corruption.objects.CameraBlurKeyframe import CameraBlurKeyframe
from retro_data_structures.properties.corruption.objects.BlinkWolf import BlinkWolf
from retro_data_structures.properties.corruption.objects.SeedBoss3 import SeedBoss3
from retro_data_structures.properties.corruption.objects.Berserker import Berserker
from retro_data_structures.properties.corruption.objects.BeastRider import BeastRider
from retro_data_structures.properties.corruption.objects.Cable import Cable
from retro_data_structures.properties.corruption.objects.ContextActionButtonPressing import ContextActionButtonPressing
from retro_data_structures.properties.corruption.objects.ContextActionCombinationLock import (
    ContextActionCombinationLock,
)
from retro_data_structures.properties.corruption.objects.ContextActionImageFocus import ContextActionImageFocus
from retro_data_structures.properties.corruption.objects.CameraHint import CameraHint
from retro_data_structures.properties.corruption.objects.CameraPitch import CameraPitch
from retro_data_structures.properties.corruption.objects.CameraShaker import CameraShaker
from retro_data_structures.properties.corruption.objects.CannonBall import CannonBall
from retro_data_structures.properties.corruption.objects.ContextActionWelding import ContextActionWelding
from retro_data_structures.properties.corruption.objects.CinematicCamera import CinematicCamera
from retro_data_structures.properties.corruption.objects.ColorModulate import ColorModulate
from retro_data_structures.properties.corruption.objects.CombatTrooper import CombatTrooper
from retro_data_structures.properties.corruption.objects.ControllerAction import ControllerAction
from retro_data_structures.properties.corruption.objects.Counter import Counter
from retro_data_structures.properties.corruption.objects.CoverPoint import CoverPoint
from retro_data_structures.properties.corruption.objects.CrossAreaRelay import CrossAreaRelay
from retro_data_structures.properties.corruption.objects.ConditionalRelay import ConditionalRelay
from retro_data_structures.properties.corruption.objects.ContextSensitiveAction import ContextSensitiveAction
from retro_data_structures.properties.corruption.objects.ContextSensitiveActivator import ContextSensitiveActivator
from retro_data_structures.properties.corruption.objects.ControlHint import ControlHint
from retro_data_structures.properties.corruption.objects.Debris import Debris
from retro_data_structures.properties.corruption.objects.DefenseMechanoid import DefenseMechanoid
from retro_data_structures.properties.corruption.objects.DistanceFog import DistanceFog
from retro_data_structures.properties.corruption.objects.DialogueMenu import DialogueMenu
from retro_data_structures.properties.corruption.objects.DarkSamusEcho import DarkSamusEcho
from retro_data_structures.properties.corruption.objects.DynamicLight import DynamicLight
from retro_data_structures.properties.corruption.objects.DamageActor import DamageActor
from retro_data_structures.properties.corruption.objects.Dock import Dock
from retro_data_structures.properties.corruption.objects.Door import Door
from retro_data_structures.properties.corruption.objects.DarkSamus import DarkSamus
from retro_data_structures.properties.corruption.objects.DamageableTrigger import DamageableTrigger
from retro_data_structures.properties.corruption.objects.DamageableTriggerOrientated import DamageableTriggerOrientated
from retro_data_structures.properties.corruption.objects.Effect import Effect
from retro_data_structures.properties.corruption.objects.EffectRepulsor import EffectRepulsor
from retro_data_structures.properties.corruption.objects.ElectroMagneticPulse import ElectroMagneticPulse
from retro_data_structures.properties.corruption.objects.EyePod import EyePod
from retro_data_structures.properties.corruption.objects.FargullHatcherSwarm import FargullHatcherSwarm
from retro_data_structures.properties.corruption.objects.FargullHatcher import FargullHatcher
from retro_data_structures.properties.corruption.objects.CameraFilterKeyframe import CameraFilterKeyframe
from retro_data_structures.properties.corruption.objects.FishCloud import FishCloud
from retro_data_structures.properties.corruption.objects.VisorFlare import VisorFlare
from retro_data_structures.properties.corruption.objects.FalsePerspective import FalsePerspective
from retro_data_structures.properties.corruption.objects.FlyingPirate import FlyingPirate
from retro_data_structures.properties.corruption.objects.FogOverlay import FogOverlay
from retro_data_structures.properties.corruption.objects.FogVolume import FogVolume
from retro_data_structures.properties.corruption.objects.Friendly import Friendly
from retro_data_structures.properties.corruption.objects.FishCloudModifier import FishCloudModifier
from retro_data_structures.properties.corruption.objects.FlyerSwarm import FlyerSwarm
from retro_data_structures.properties.corruption.objects.EnvFxDensityController import EnvFxDensityController
from retro_data_structures.properties.corruption.objects.Gandrayda import Gandrayda
from retro_data_structures.properties.corruption.objects.Generator import Generator
from retro_data_structures.properties.corruption.objects.GhorLowerBody import GhorLowerBody
from retro_data_structures.properties.corruption.objects.GhorUpperBody import GhorUpperBody
from retro_data_structures.properties.corruption.objects.GuiMenu import GuiMenu
from retro_data_structures.properties.corruption.objects.GunTurretBase import GunTurretBase
from retro_data_structures.properties.corruption.objects.GunTurretTop import GunTurretTop
from retro_data_structures.properties.corruption.objects.GeneratedObjectDeleter import GeneratedObjectDeleter
from retro_data_structures.properties.corruption.objects.GrapplePoint import GrapplePoint
from retro_data_structures.properties.corruption.objects.GragnolFlyer import GragnolFlyer
from retro_data_structures.properties.corruption.objects.GellSac import GellSac
from retro_data_structures.properties.corruption.objects.GuiScreen import GuiScreen
from retro_data_structures.properties.corruption.objects.GuiSlider import GuiSlider
from retro_data_structures.properties.corruption.objects.GuiWidget import GuiWidget
from retro_data_structures.properties.corruption.objects.HUDHint import HUDHint
from retro_data_structures.properties.corruption.objects.PlayerHint import PlayerHint
from retro_data_structures.properties.corruption.objects.IFT import IFT
from retro_data_structures.properties.corruption.objects.Korakk import Korakk
from retro_data_structures.properties.corruption.objects.KorbaSnatcherSwarm import KorbaSnatcherSwarm
from retro_data_structures.properties.corruption.objects.KorbaMaw import KorbaMaw
from retro_data_structures.properties.corruption.objects.LODController import LODController
from retro_data_structures.properties.corruption.objects.LUAScript import LUAScript
from retro_data_structures.properties.corruption.objects.LightVolume import LightVolume
from retro_data_structures.properties.corruption.objects.HUDMemo import HUDMemo
from retro_data_structures.properties.corruption.objects.MetroidHatcher import MetroidHatcher
from retro_data_structures.properties.corruption.objects.MetroidHopper import MetroidHopper
from retro_data_structures.properties.corruption.objects.MiiAccessory import MiiAccessory
from retro_data_structures.properties.corruption.objects.MinorIng import MinorIng
from retro_data_structures.properties.corruption.objects.MultiModelActor import MultiModelActor
from retro_data_structures.properties.corruption.objects.StreamedMovie import StreamedMovie
from retro_data_structures.properties.corruption.objects.MetroidPhazeoid import MetroidPhazeoid
from retro_data_structures.properties.corruption.objects.Metaree import Metaree
from retro_data_structures.properties.corruption.objects.MemoryRelay import MemoryRelay
from retro_data_structures.properties.corruption.objects.MysteryFlyer import MysteryFlyer
from retro_data_structures.properties.corruption.objects.Nightbarb import Nightbarb
from retro_data_structures.properties.corruption.objects.NoseTurret import NoseTurret
from retro_data_structures.properties.corruption.objects.OptionalAreaAsset import OptionalAreaAsset
from retro_data_structures.properties.corruption.objects.Parasite import Parasite
from retro_data_structures.properties.corruption.objects.Pickup import Pickup
from retro_data_structures.properties.corruption.objects.PathControl import PathControl
from retro_data_structures.properties.corruption.objects.PhysicsDebris import PhysicsDebris
from retro_data_structures.properties.corruption.objects.PirateDrone import PirateDrone
from retro_data_structures.properties.corruption.objects.PlayerGravityScalar import PlayerGravityScalar
from retro_data_structures.properties.corruption.objects.PhazonHarvester import PhazonHarvester
from retro_data_structures.properties.corruption.objects.PhazonPuffer import PhazonPuffer
from retro_data_structures.properties.corruption.objects.Phaazoid import Phaazoid
from retro_data_structures.properties.corruption.objects.PhazonFlyerSwarm import PhazonFlyerSwarm
from retro_data_structures.properties.corruption.objects.PillBug import PillBug
from retro_data_structures.properties.corruption.objects.SpacePirate import SpacePirate
from retro_data_structures.properties.corruption.objects.PlayerActor import PlayerActor
from retro_data_structures.properties.corruption.objects.Platform import Platform
from retro_data_structures.properties.corruption.objects.PhazonLeech import PhazonLeech
from retro_data_structures.properties.corruption.objects.PlayerProxy import PlayerProxy
from retro_data_structures.properties.corruption.objects.PathMeshCtrl import PathMeshCtrl
from retro_data_structures.properties.corruption.objects.PointOfInterest import PointOfInterest
from retro_data_structures.properties.corruption.objects.PhazonPuddle import PhazonPuddle
from retro_data_structures.properties.corruption.objects.PlantScarabSwarm import PlantScarabSwarm
from retro_data_structures.properties.corruption.objects.PhazonTentacle import PhazonTentacle
from retro_data_structures.properties.corruption.objects.PlayerUserAnimPoint import PlayerUserAnimPoint
from retro_data_structures.properties.corruption.objects.Puffer import Puffer
from retro_data_structures.properties.corruption.objects.RadialDamage import RadialDamage
from retro_data_structures.properties.corruption.objects.AreaAttributes import AreaAttributes
from retro_data_structures.properties.corruption.objects.ReptilicusHunter import ReptilicusHunter
from retro_data_structures.properties.corruption.objects.Repulsor import Repulsor
from retro_data_structures.properties.corruption.objects.Ridley1 import Ridley1
from retro_data_structures.properties.corruption.objects.Ripple import Ripple
from retro_data_structures.properties.corruption.objects.RoomAcoustics import RoomAcoustics
from retro_data_structures.properties.corruption.objects.RandomRelay import RandomRelay
from retro_data_structures.properties.corruption.objects.RainSplash import RainSplash
from retro_data_structures.properties.corruption.objects.RumbleEffect import RumbleEffect
from retro_data_structures.properties.corruption.objects.Rundas import Rundas
from retro_data_structures.properties.corruption.objects.StreamedAudioModifier import StreamedAudioModifier
from retro_data_structures.properties.corruption.objects.SamusForm import SamusForm
from retro_data_structures.properties.corruption.objects.SeedBoss2GiantForm import SeedBoss2GiantForm
from retro_data_structures.properties.corruption.objects.SeedBoss2PrimeBot import SeedBoss2PrimeBot
from retro_data_structures.properties.corruption.objects.SeedBoss2BotSwarm import SeedBoss2BotSwarm
from retro_data_structures.properties.corruption.objects.ScanBeam import ScanBeam
from retro_data_structures.properties.corruption.objects.SkyboxModInca import SkyboxModInca
from retro_data_structures.properties.corruption.objects.SeedBoss1Orb import SeedBoss1Orb
from retro_data_structures.properties.corruption.objects.ScanIncoming import ScanIncoming
from retro_data_structures.properties.corruption.objects.SurfaceControl import SurfaceControl
from retro_data_structures.properties.corruption.objects.SeedBoss1 import SeedBoss1
from retro_data_structures.properties.corruption.objects.SteamDrone import SteamDrone
from retro_data_structures.properties.corruption.objects.ShellBug import ShellBug
from retro_data_structures.properties.corruption.objects.ShipBombingRun import ShipBombingRun
from retro_data_structures.properties.corruption.objects.ShipCommandIcon import ShipCommandIcon
from retro_data_structures.properties.corruption.objects.ShipCommandPath import ShipCommandPath
from retro_data_structures.properties.corruption.objects.ShadowProjector import ShadowProjector
from retro_data_structures.properties.corruption.objects.ShipHudControl import ShipHudControl
from retro_data_structures.properties.corruption.objects.Ship import Ship
from retro_data_structures.properties.corruption.objects.ShipProxy import ShipProxy
from retro_data_structures.properties.corruption.objects.SkyRipple import SkyRipple
from retro_data_structures.properties.corruption.objects.ScriptLayerController import ScriptLayerController
from retro_data_structures.properties.corruption.objects.SnagVineHelper import SnagVineHelper
from retro_data_structures.properties.corruption.objects.SoundModifier import SoundModifier
from retro_data_structures.properties.corruption.objects.Sound import Sound
from retro_data_structures.properties.corruption.objects.ShipDecalController import ShipDecalController
from retro_data_structures.properties.corruption.objects.SpecialFunction import SpecialFunction
from retro_data_structures.properties.corruption.objects.Spinner import Spinner
from retro_data_structures.properties.corruption.objects.PositionRelay import PositionRelay
from retro_data_structures.properties.corruption.objects.Sprite import Sprite
from retro_data_structures.properties.corruption.objects.SpawnPoint import SpawnPoint
from retro_data_structures.properties.corruption.objects.SequenceTimer import SequenceTimer
from retro_data_structures.properties.corruption.objects.Relay import Relay
from retro_data_structures.properties.corruption.objects.StreamedAudio import StreamedAudio
from retro_data_structures.properties.corruption.objects.Steam import Steam
from retro_data_structures.properties.corruption.objects.SteamBot import SteamBot
from retro_data_structures.properties.corruption.objects.SteamLord import SteamLord
from retro_data_structures.properties.corruption.objects.Subtitles import Subtitles
from retro_data_structures.properties.corruption.objects.SwarmBot import SwarmBot
from retro_data_structures.properties.corruption.objects.ScrewAttackWallJumpTarget import ScrewAttackWallJumpTarget
from retro_data_structures.properties.corruption.objects.WallCrawlerSwarm import WallCrawlerSwarm
from retro_data_structures.properties.corruption.objects.Switch import Switch
from retro_data_structures.properties.corruption.objects.WorldTeleporter import WorldTeleporter
from retro_data_structures.properties.corruption.objects.TargetingPoint import TargetingPoint
from retro_data_structures.properties.corruption.objects.Timer import Timer
from retro_data_structures.properties.corruption.objects.TimeKeyframe import TimeKeyframe
from retro_data_structures.properties.corruption.objects.TeamAI import TeamAI
from retro_data_structures.properties.corruption.objects.Trigger import Trigger
from retro_data_structures.properties.corruption.objects.TextPane import TextPane
from retro_data_structures.properties.corruption.objects.VisorGoo import VisorGoo
from retro_data_structures.properties.corruption.objects.VolGroup import VolGroup
from retro_data_structures.properties.corruption.objects.Water import Water
from retro_data_structures.properties.corruption.objects.Waypoint import Waypoint
from retro_data_structures.properties.corruption.objects.VenomWeed import VenomWeed
from retro_data_structures.properties.corruption.objects.WorldAttributes import WorldAttributes
from retro_data_structures.properties.corruption.objects.WorldLightFader import WorldLightFader
from retro_data_structures.properties.corruption.objects.WeaponGenerator import WeaponGenerator
from retro_data_structures.properties.corruption.objects.WorldTeleporterAttributes import WorldTeleporterAttributes
from retro_data_structures.properties.corruption.objects.WorldTransitionChoiceRelay import WorldTransitionChoiceRelay

if typing.TYPE_CHECKING:
    from retro_data_structures.properties.base_property import BaseObjectType

_FOUR_CC_MAPPING: dict[str, type[BaseObjectType]] = {
    "ACHI": Achievement,
    "ACKF": ActorKeyframe,
    "ACTR": Actor,
    "ADMG": AreaDamage,
    "AIFZ": AIFuse,
    "AIHT": AIHint,
    "AIKF": AIKeyframe,
    "AITP": AITaskPoint,
    "AIWP": AIWaypoint,
    "ALRM": AlarmController,
    "AMIA": AmbientAI,
    "AMOR": ActorMorph,
    "AOCL": AudioOccluder,
    "ASAS": AreaStreamedAudioState,
    "ATMA": AtomicAlpha,
    "ATRN": ActorTransform,
    "AUR1": AuroraUnit1,
    "AUR2": AuroraUnit2,
    "AVIS": AudioVisualizer,
    "AVMC": AreaVisitMapController,
    "BALS": SpiderBallAttractionSurface,
    "BALT": BallTrigger,
    "BALW": SpiderBallWaypoint,
    "BEAM": Beam,
    "BLUR": CameraBlurKeyframe,
    "BLWF": BlinkWolf,
    "BOS3": SeedBoss3,
    "BSKR": Berserker,
    "BSTR": BeastRider,
    "CABL": Cable,
    "CABP": ContextActionButtonPressing,
    "CACL": ContextActionCombinationLock,
    "CAIF": ContextActionImageFocus,
    "CAMH": CameraHint,
    "CAMP": CameraPitch,
    "CAMS": CameraShaker,
    "CANB": CannonBall,
    "CAWL": ContextActionWelding,
    "CINE": CinematicCamera,
    "CLRM": ColorModulate,
    "CMBT": CombatTrooper,
    "CNTA": ControllerAction,
    "CNTR": Counter,
    "COVR": CoverPoint,
    "CRAR": CrossAreaRelay,
    "CRLY": ConditionalRelay,
    "CSAC": ContextSensitiveAction,
    "CSAT": ContextSensitiveActivator,
    "CTLH": ControlHint,
    "DEBR": Debris,
    "DEFM": DefenseMechanoid,
    "DFOG": DistanceFog,
    "DGMN": DialogueMenu,
    "DKSE": DarkSamusEcho,
    "DLHT": DynamicLight,
    "DMGA": DamageActor,
    "DOCK": Dock,
    "DOOR": Door,
    "DRKS": DarkSamus,
    "DTRG": DamageableTrigger,
    "DTRO": DamageableTriggerOrientated,
    "EFCT": Effect,
    "EFTR": EffectRepulsor,
    "EMPU": ElectroMagneticPulse,
    "EYEP": EyePod,
    "FGHS": FargullHatcherSwarm,
    "FGHT": FargullHatcher,
    "FILT": CameraFilterKeyframe,
    "FISH": FishCloud,
    "FLAR": VisorFlare,
    "FLPS": FalsePerspective,
    "FLYP": FlyingPirate,
    "FOGO": FogOverlay,
    "FOGV": FogVolume,
    "FRND": Friendly,
    "FSHM": FishCloudModifier,
    "FSWM": FlyerSwarm,
    "FXDC": EnvFxDensityController,
    "GAND": Gandrayda,
    "GENR": Generator,
    "GHOR": GhorLowerBody,
    "GHRU": GhorUpperBody,
    "GMNU": GuiMenu,
    "GNTB": GunTurretBase,
    "GNTT": GunTurretTop,
    "GOBD": GeneratedObjectDeleter,
    "GRAP": GrapplePoint,
    "GRFL": GragnolFlyer,
    "GSAC": GellSac,
    "GSCR": GuiScreen,
    "GSLD": GuiSlider,
    "GWIG": GuiWidget,
    "HHNT": HUDHint,
    "HINT": PlayerHint,
    "IFTC": IFT,
    "KRAK": Korakk,
    "KRBA": KorbaSnatcherSwarm,
    "KRBM": KorbaMaw,
    "LODC": LODController,
    "LUAX": LUAScript,
    "LVOL": LightVolume,
    "MEMO": HUDMemo,
    "MHAT": MetroidHatcher,
    "MHOP": MetroidHopper,
    "MIIA": MiiAccessory,
    "MINI": MinorIng,
    "MMDL": MultiModelActor,
    "MOVI": StreamedMovie,
    "MPHZ": MetroidPhazeoid,
    "MREE": Metaree,
    "MRLY": MemoryRelay,
    "MYSF": MysteryFlyer,
    "NBAR": Nightbarb,
    "NOTU": NoseTurret,
    "OPAA": OptionalAreaAsset,
    "PARA": Parasite,
    "PCKP": Pickup,
    "PCTL": PathControl,
    "PDBR": PhysicsDebris,
    "PDRN": PirateDrone,
    "PGVS": PlayerGravityScalar,
    "PHHR": PhazonHarvester,
    "PHPF": PhazonPuffer,
    "PHZD": Phaazoid,
    "PHZS": PhazonFlyerSwarm,
    "PILL": PillBug,
    "PIRT": SpacePirate,
    "PLAC": PlayerActor,
    "PLAT": Platform,
    "PLCH": PhazonLeech,
    "PLPX": PlayerProxy,
    "PMCT": PathMeshCtrl,
    "POIN": PointOfInterest,
    "PPDL": PhazonPuddle,
    "PSSM": PlantScarabSwarm,
    "PTNT": PhazonTentacle,
    "PUAP": PlayerUserAnimPoint,
    "PUFR": Puffer,
    "RADD": RadialDamage,
    "REAA": AreaAttributes,
    "REPH": ReptilicusHunter,
    "REPL": Repulsor,
    "RID1": Ridley1,
    "RIPL": Ripple,
    "RMAC": RoomAcoustics,
    "RRLY": RandomRelay,
    "RSPL": RainSplash,
    "RUMB": RumbleEffect,
    "RUND": Rundas,
    "SAMD": StreamedAudioModifier,
    "SAMF": SamusForm,
    "SB2G": SeedBoss2GiantForm,
    "SB2P": SeedBoss2PrimeBot,
    "SB2X": SeedBoss2BotSwarm,
    "SBEM": ScanBeam,
    "SBMI": SkyboxModInca,
    "SBO1": SeedBoss1Orb,
    "SCIC": ScanIncoming,
    "SCTL": SurfaceControl,
    "SDB1": SeedBoss1,
    "SDRN": SteamDrone,
    "SHBG": ShellBug,
    "SHBR": ShipBombingRun,
    "SHCI": ShipCommandIcon,
    "SHCP": ShipCommandPath,
    "SHDW": ShadowProjector,
    "SHHC": ShipHudControl,
    "SHIP": Ship,
    "SHPX": ShipProxy,
    "SKRP": SkyRipple,
    "SLCT": ScriptLayerController,
    "SNAG": SnagVineHelper,
    "SNDM": SoundModifier,
    "SOND": Sound,
    "SPDC": ShipDecalController,
    "SPFN": SpecialFunction,
    "SPIN": Spinner,
    "SPRL": PositionRelay,
    "SPRT": Sprite,
    "SPWN": SpawnPoint,
    "SQTR": SequenceTimer,
    "SRLY": Relay,
    "STAU": StreamedAudio,
    "STEM": Steam,
    "STMB": SteamBot,
    "STML": SteamLord,
    "SUBT": Subtitles,
    "SWBT": SwarmBot,
    "SWJT": ScrewAttackWallJumpTarget,
    "SWRM": WallCrawlerSwarm,
    "SWTC": Switch,
    "TEL1": WorldTeleporter,
    "TGPT": TargetingPoint,
    "TIMR": Timer,
    "TKEY": TimeKeyframe,
    "TMAI": TeamAI,
    "TRGR": Trigger,
    "TXPN": TextPane,
    "VGOO": VisorGoo,
    "VOLG": VolGroup,
    "WATR": Water,
    "WAYP": Waypoint,
    "WEED": VenomWeed,
    "WLDA": WorldAttributes,
    "WLIT": WorldLightFader,
    "WPNG": WeaponGenerator,
    "WTAT": WorldTeleporterAttributes,
    "WTCR": WorldTransitionChoiceRelay,
}


@functools.cache
def get_object(four_cc: str) -> type[BaseObjectType]:
    return _FOUR_CC_MAPPING[four_cc]
