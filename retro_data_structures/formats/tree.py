from construct import Enum, Hex, Struct, Const, Int32ub, Byte, PrefixedArray
from retro_data_structures.common_types import FourCC, String
from retro_data_structures.formats.script_object import ScriptInstance
from retro_data_structures.game_check import AssetIdCorrect
import enum

class InventorySlots(enum.IntEnum):
    PowerBeam = 0x00
    DarkBeam = 0x01
    LightBeam = 0x02
    AnnihilatorBeam = 0x03

    SuperMissile = 0x04
    Darkburst = 0x05
    Sunburst = 0x06
    SonicBoom = 0x07

    CombatVisor = 0x08
    ScanVisor = 0x09
    DarkVisor = 0x0A
    EchoVisor = 0x0B

    VariaSuit = 0x0C
    DarkSuit = 0x0D
    LightSuit = 0x0E

    MorphBall = 0x0F
    BoostBall = 0x10
    SpiderBall = 0x11
    MorphBallBombs = 0x12

    ChargeBeam = 0x16
    GrappleBeam = 0x17
    SpaceJumpBoots = 0x18
    GravityBoost = 0x19
    SeekerMissile = 0x1A
    ScrewAttack = 0x1B
    PowerBomb = 0x1C
    MissileLauncher = 0x1D
    BeamAmmoExpansion = 0x1E
    EnergyTank = 0x20

    SkyTempleKey1 = 0x21
    SkyTempleKey2 = 0x22
    SkyTempleKey3 = 0x23
    SkyTempleKey4 = 0x24
    SkyTempleKey5 = 0x25
    SkyTempleKey6 = 0x26
    SkyTempleKey7 = 0x27
    SkyTempleKey8 = 0x28
    SkyTempleKey9 = 0x29

    DarkAgonKey1 = 0x2A
    DarkAgonKey2 = 0x2B
    DarkAgonKey3 = 0x2C

    DarkTorvusKey1 = 0x2D
    DarkTorvusKey2 = 0x2E
    DarkTorvusKey3 = 0x2F

    IngHiveKey1 = 0x30
    IngHiveKey2 = 0x31
    IngHiveKey3 = 0x32

    EnergyTransferModule = 0x33
    BeamCombo = 0x34

TREE = Struct(
    "magic" / Const("TREE", FourCC),
    "root_node_id" / Int32ub,
    "unknown" / Const(1, Byte),
    "nodes" / PrefixedArray(Int32ub, ScriptInstance)
)