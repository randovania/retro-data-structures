# Generated File
from __future__ import annotations

from retro_data_structures.properties.common.archetypes.DynamicLightFalloff import DynamicLightFalloff
from retro_data_structures.properties.common.archetypes.DynamicLightIntensity import DynamicLightIntensity
from retro_data_structures.properties.common.archetypes.DynamicLightMotionSpline import DynamicLightMotionSpline
from retro_data_structures.properties.common.archetypes.DynamicLightParent import DynamicLightParent
from retro_data_structures.properties.common.archetypes.DynamicLightSpotlight import DynamicLightSpotlight
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.common.archetypes.GuiWidgetProperties import GuiWidgetProperties
from retro_data_structures.properties.common.archetypes.RotationSplines import RotationSplines
from retro_data_structures.properties.common.archetypes.ScaleSplines import ScaleSplines
from retro_data_structures.properties.common.archetypes.SplineType import SplineType
from retro_data_structures.properties.common.archetypes.TBallTransitionResources import TBallTransitionResources
from retro_data_structures.properties.common.archetypes.TBeamInfo import TBeamInfo
from retro_data_structures.properties.common.archetypes.TDamageInfo import TDamageInfo
from retro_data_structures.properties.common.archetypes.TGunResources import TGunResources
from retro_data_structures.properties.common.archetypes.TIcon_Configurations import TIcon_Configurations
from retro_data_structures.properties.common.archetypes.Transform import Transform
from retro_data_structures.properties.common.archetypes.TweakBall_BoostBall import TweakBall_BoostBall
from retro_data_structures.properties.common.archetypes.TweakBall_Camera import TweakBall_Camera
from retro_data_structures.properties.common.archetypes.TweakBall_CannonBall import TweakBall_CannonBall
from retro_data_structures.properties.common.archetypes.TweakBall_DeathBall import TweakBall_DeathBall
from retro_data_structures.properties.common.archetypes.TweakBall_Movement import TweakBall_Movement
from retro_data_structures.properties.common.archetypes.TweakGui_Completion import TweakGui_Completion
from retro_data_structures.properties.common.archetypes.TweakGui_Credits import TweakGui_Credits
from retro_data_structures.properties.common.archetypes.TweakGui_HudColorTypedef import TweakGui_HudColorTypedef
from retro_data_structures.properties.common.archetypes.TweakGui_MovieVolumes import TweakGui_MovieVolumes
from retro_data_structures.properties.common.archetypes.TweakGui_ScannableObjectDownloadTimes import (
    TweakGui_ScannableObjectDownloadTimes,
)
from retro_data_structures.properties.common.archetypes.TweakGui_VisorColorSchemeTypedef import (
    TweakGui_VisorColorSchemeTypedef,
)
from retro_data_structures.properties.common.archetypes.TweakGuiColors_Multiplayer import TweakGuiColors_Multiplayer
from retro_data_structures.properties.common.archetypes.TweakGuiColors_TurretHudTypedef import (
    TweakGuiColors_TurretHudTypedef,
)
from retro_data_structures.properties.common.archetypes.TweakPlayer_Collision import TweakPlayer_Collision
from retro_data_structures.properties.common.archetypes.TweakPlayer_FirstPersonCamera import (
    TweakPlayer_FirstPersonCamera,
)
from retro_data_structures.properties.common.archetypes.TweakPlayer_Frozen import TweakPlayer_Frozen
from retro_data_structures.properties.common.archetypes.TweakPlayer_GrappleBeam import TweakPlayer_GrappleBeam
from retro_data_structures.properties.common.archetypes.TweakPlayer_Orbit import TweakPlayer_Orbit
from retro_data_structures.properties.common.archetypes.TweakPlayer_Shield import TweakPlayer_Shield
from retro_data_structures.properties.common.archetypes.TweakPlayerGun_Arm_Position import TweakPlayerGun_Arm_Position
from retro_data_structures.properties.common.archetypes.TweakPlayerGun_Holstering import TweakPlayerGun_Holstering
from retro_data_structures.properties.common.archetypes.TweakPlayerGun_Position import TweakPlayerGun_Position
from retro_data_structures.properties.common.archetypes.TweakTargeting_Charge_Gauge import TweakTargeting_Charge_Gauge
from retro_data_structures.properties.common.archetypes.TweakTargeting_LockDagger import TweakTargeting_LockDagger
from retro_data_structures.properties.common.archetypes.TweakTargeting_LockFire import TweakTargeting_LockFire
from retro_data_structures.properties.common.archetypes.TweakTargeting_OuterBeamIcon import TweakTargeting_OuterBeamIcon
from retro_data_structures.properties.common.archetypes.TweakTargeting_Scan import TweakTargeting_Scan
from retro_data_structures.properties.common.archetypes.TWeaponDamage import TWeaponDamage

__all__ = [
    "DynamicLightFalloff",
    "DynamicLightIntensity",
    "DynamicLightMotionSpline",
    "DynamicLightParent",
    "DynamicLightSpotlight",
    "EditorProperties",
    "GuiWidgetProperties",
    "RotationSplines",
    "ScaleSplines",
    "SplineType",
    "TBallTransitionResources",
    "TBeamInfo",
    "TDamageInfo",
    "TGunResources",
    "TIcon_Configurations",
    "TWeaponDamage",
    "Transform",
    "TweakBall_BoostBall",
    "TweakBall_Camera",
    "TweakBall_CannonBall",
    "TweakBall_DeathBall",
    "TweakBall_Movement",
    "TweakGuiColors_Multiplayer",
    "TweakGuiColors_TurretHudTypedef",
    "TweakGui_Completion",
    "TweakGui_Credits",
    "TweakGui_HudColorTypedef",
    "TweakGui_MovieVolumes",
    "TweakGui_ScannableObjectDownloadTimes",
    "TweakGui_VisorColorSchemeTypedef",
    "TweakPlayerGun_Arm_Position",
    "TweakPlayerGun_Holstering",
    "TweakPlayerGun_Position",
    "TweakPlayer_Collision",
    "TweakPlayer_FirstPersonCamera",
    "TweakPlayer_Frozen",
    "TweakPlayer_GrappleBeam",
    "TweakPlayer_Orbit",
    "TweakPlayer_Shield",
    "TweakTargeting_Charge_Gauge",
    "TweakTargeting_LockDagger",
    "TweakTargeting_LockFire",
    "TweakTargeting_OuterBeamIcon",
    "TweakTargeting_Scan",
]
