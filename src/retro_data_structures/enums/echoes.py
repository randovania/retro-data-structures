"""
Generated file.
"""

from __future__ import annotations

import enum
import typing

import typing_extensions

from retro_data_structures.properties import structs

if typing.TYPE_CHECKING:
    from retro_data_structures import json_util
    from retro_data_structures.game_check import Game


class State(enum.Enum):
    NonZero = "!ZER"
    Active = "ACTV"
    AILogicState1 = "AIS1"
    AILogicState2 = "AIS2"
    AILogicState3 = "AIS3"
    Approach = "APRC"
    Arrived = "ARRV"
    AttachedCollisionObject = "ATCL"
    AttachedAnimatedObject = "ATOB"
    Attack = "ATTK"
    BallIceXDamage = "BIDG"
    BallXDamage = "BXDG"
    Closed = "CLOS"
    Connect = "CONN"
    CPLR = "CPLR"
    CameraPath = "CPTH"
    CameraTarget = "CTGT"
    CameraTime = "CTIM"
    Damage = "DAMG"
    DamageAnnihilator = "DANN"
    DamageAI = "DBAI"
    DamageBoostBall = "DBAL"
    DamageBomb = "DBMB"
    DamageCannonBall = "DCAN"
    DamageDark = "DDRK"
    Dead = "DEAD"
    DefaultState = "DFST"
    DeGenerate = "DGNR"
    DamageLight = "DLGT"
    DamageMissile = "DMIS"
    DamagePowerBomb = "DPBM"
    DamagePhazon = "DPHZ"
    DamagePower = "DPWR"
    DarkXDamage = "DRKX"
    DamageScrew = "DSCW"
    Entered = "ENTR"
    Exited = "EXIT"
    Footstep = "FOOT"
    Freeze = "FREZ"
    Generate = "GRNT"
    InheritBounds = "IBND"
    Inactive = "ICTV"
    IceXDamage = "IDMG"
    Inside = "INSD"
    InternalState00 = "IS00"
    InternalState01 = "IS01"
    InternalState02 = "IS02"
    InternalState03 = "IS03"
    InternalState04 = "IS04"
    InternalState05 = "IS05"
    InternalState06 = "IS06"
    InternalState07 = "IS07"
    InternalState08 = "IS08"
    InternalState09 = "IS09"
    InternalState10 = "IS10"
    InternalState11 = "IS11"
    InternalState12 = "IS12"
    InternalState13 = "IS13"
    InternalState14 = "IS14"
    InternalState15 = "IS15"
    InternalState16 = "IS16"
    InternalState17 = "IS17"
    InternalState18 = "IS18"
    InternalState19 = "IS19"
    Left = "LEFT"
    MaxReached = "MAXR"
    Modify = "MDFY"
    Open = "OPEN"
    Play = "PLAY"
    PressA = "PRSA"
    PressB = "PRSB"
    PressStart = "PRST"
    PressX = "PRSX"
    PressY = "PRSY"
    PressZ = "PRSZ"
    Patrol = "PTRL"
    DeathRattle = "RATL"
    SpawnResidue = "RDUE"
    ReflectedDamage = "REFD"
    ResistedDamage = "RESD"
    Right = "RGHT"
    Retreat = "RTRT"
    ScanDone = "SCND"
    ScanSource = "SCNS"
    Sequence = "SQNC"
    UnFreeze = "UFRZ"
    Up = "UP  "
    XDamage = "XDMG"
    InBack = "XINB"
    InFront = "XINF"
    Zero = "ZERO"

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (str))
        return cls(data)

    def to_json(self) -> str:
        return self.value


class Message(enum.Enum):
    Action = "ACTN"
    Activate = "ACTV"
    Alert = "ALRT"
    Arrive = "ARRV"
    Attach = "ATCH"
    Close = "CLOS"
    ClearOriginator = "CORG"
    Deactivate = "DCTV"
    Decrement = "DECR"
    Escape = "ESCP"
    Follow = "FOLW"
    InternalMessage00 = "IM00"
    InternalMessage01 = "IM01"
    InternalMessage02 = "IM02"
    InternalMessage03 = "IM03"
    InternalMessage04 = "IM04"
    InternalMessage05 = "IM05"
    InternalMessage06 = "IM06"
    InternalMessage07 = "IM07"
    InternalMessage08 = "IM08"
    InternalMessage09 = "IM09"
    InternalMessage10 = "IM10"
    InternalMessage11 = "IM11"
    InternalMessage12 = "IM12"
    InternalMessage13 = "IM13"
    InternalMessage14 = "IM14"
    Increment = "INCR"
    Kill = "KILL"
    Left = "LEFT"
    Load = "LOAD"
    Lock = "LOCK"
    Next = "NEXT"
    Open = "OPEN"
    Play = "PLAY"
    Reset = "RSET"
    ResetAndStart = "RSTS"
    SetToMax = "SMAX"
    SetOriginator = "SORG"
    Stop = "STOP"
    StopAndReset = "STPR"
    Start = "STRT"
    ToggleActive = "TCTV"
    Unlock = "ULCK"
    Unload = "ULOD"
    Clear = "XCLR"
    Delete = "XDEL"
    XDamage = "XDMG"
    SetToZero = "ZERO"

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (str))
        return cls(data)

    def to_json(self) -> str:
        return self.value


class ControllerActionCommandEnum(enum.IntEnum):
    _None = 0
    Forward = 1
    Backward = 2
    TurnLeft = 3
    TurnRight = 4
    StrafeLeft = 5
    StrafeRight = 6
    LookLeft = 7
    LookRight = 8
    LookUp = 9
    LookDown = 10
    Jump = 11
    Jump2 = 12
    FireBeam = 13
    FireBeam2 = 14
    AutoFireBeamDeprecated = 15
    ChargeBeam = 16
    ChargeBeam2 = 17
    UseItem = 18
    AimUpDeprecated = 19
    AimDownDeprecated = 20
    CycleBeamUpDeprecated = 21
    CycleBeamDownDeprecated = 22
    CycleItemDeprecated = 23
    SelectPowerBeam = 24
    SelectDarkBeam = 25
    SelectLightBeam = 26
    SelectAnnihilatorBeam = 27
    GunToggleHolsterDeprecated = 28
    OrbitCloseDeprecated = 29
    OrbitFar = 30
    OrbitObject = 31
    OrbitSelectDeprecated = 32
    OrbitConfirmDeprecated = 33
    OrbitLeft = 34
    OrbitRight = 35
    OrbitUp = 36
    OrbitDown = 37
    HoldLook1 = 38
    HoldLook2Deprecated = 39
    LookZoomIn = 40
    LookZoomOut = 41
    HoldAimDeprecated = 42
    MapCircleUp = 43
    MapCircleDown = 44
    MapCircleLeft = 45
    MapCircleRight = 46
    MapMoveForward = 47
    MapMoveBack = 48
    MapMoveLeft = 49
    MapMoveRight = 50
    MapZoomIn = 51
    MapZoomOut = 52
    SpiderBall = 53
    ChaseCamera = 54
    EchoVisor = 55
    DarkVisor = 56
    ScanVisor = 57
    CombatVisor = 58
    VisorMenuDeprecated = 59
    CycleVisorUpDeprecated = 60
    CycleVisorDownDeprecated = 61
    DarkVisorToggleDeprecated = 62
    Crosshairs = 63
    Unknown1Deprecated = 64
    UseShieldDeprecated = 65
    ScanItem = 66
    InventoryScreen = 67
    MapScreen = 68
    OptionsScreen = 69
    LogScreen = 70
    Unknown2 = 71
    Unknown3 = 72
    BoostBall = 73
    Morph = 74
    Unmorph = 75

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


class ControllerMappingEnum(enum.IntEnum):
    _None = 0
    LeftStickUp = 1
    LeftStickDown = 2
    LeftStickLeft = 3
    LeftStickRight = 4
    RightStickUp = 5
    RightStickDown = 6
    RightStickLeft = 7
    RightStickRight = 8
    LeftTrigger = 9
    RightTrigger = 10
    DPadUp = 11
    DPadDown = 12
    DPadLeft = 13
    DPadRight = 14
    AButton = 15
    BButton = 16
    XButton = 17
    YButton = 18
    ZButton = 19
    LeftTriggerPress = 20
    RightTriggerPress = 21
    Start = 22

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


class InventorySlotEnum(enum.IntEnum):
    PowerBeam = 0
    DarkBeam = 1
    LightBeam = 2
    AnnihilatorBeam = 3
    SuperMissile = 4
    Darkburst = 5
    Sunburst = 6
    SonicBoom = 7
    CombatVisor = 8
    ScanVisor = 9
    DarkVisor = 10
    EchoVisor = 11
    VariaSuit = 12
    DarkSuit = 13
    LightSuit = 14
    MorphBall = 15
    BoostBall = 16
    SpiderBall = 17
    MorphBallBomb = 18
    LightBomb = 19
    DarkBomb = 20
    AnnihilatorBomb = 21
    ChargeBeam = 22
    GrappleBeam = 23
    SpaceJumpBoots = 24
    GravityBoost = 25
    SeekerLauncher = 26
    ScrewAttack = 27
    PowerBomb = 28
    Missile = 29
    DarkAmmo = 30
    LightAmmo = 31
    EnergyTank = 32
    SkyTempleKey1 = 33
    SkyTempleKey2 = 34
    SkyTempleKey3 = 35
    SkyTempleKey4 = 36
    SkyTempleKey5 = 37
    SkyTempleKey6 = 38
    SkyTempleKey7 = 39
    SkyTempleKey8 = 40
    SkyTempleKey9 = 41
    DarkAgonKey1 = 42
    DarkAgonKey2 = 43
    DarkAgonKey3 = 44
    DarkTorvusKey1 = 45
    DarkTorvusKey2 = 46
    DarkTorvusKey3 = 47
    IngHiveKey1 = 48
    IngHiveKey2 = 49
    IngHiveKey3 = 50
    EnergyTransferModule = 51
    BeamCombo = 52

    @classmethod
    def _missing_(cls, value: object) -> InventorySlotEnum:
        obj = int.__new__(cls, value)  # type: ignore[call-overload]
        obj._name_ = f"Unknown_{value}"
        obj._value_ = value
        return obj

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


class PlayerItemEnum(enum.IntEnum):
    PowerBeam = 0
    DarkBeam = 1
    LightBeam = 2
    AnnihilatorBeam = 3
    SuperMissile = 4
    Darkburst = 5
    Sunburst = 6
    SonicBoom = 7
    CombatVisor = 8
    ScanVisor = 9
    DarkVisor = 10
    EchoVisor = 11
    VariaSuit = 12
    DarkSuit = 13
    LightSuit = 14
    MorphBall = 15
    BoostBall = 16
    SpiderBall = 17
    MorphBallBomb = 18
    LightBomb = 19
    DarkBomb = 20
    AnnihilatorBomb = 21
    ChargeBeam = 22
    GrappleBeam = 23
    SpaceJumpBoots = 24
    GravityBoost = 25
    SeekerLauncher = 26
    ScrewAttack = 27
    EnergyTransferModulePickup = 28
    SkyTempleKey1 = 29
    SkyTempleKey2 = 30
    SkyTempleKey3 = 31
    DarkAgonKey1 = 32
    DarkAgonKey2 = 33
    DarkAgonKey3 = 34
    DarkTorvusKey1 = 35
    DarkTorvusKey2 = 36
    DarkTorvusKey3 = 37
    IngHiveKey1 = 38
    IngHiveKey2 = 39
    IngHiveKey3 = 40
    HealthRefill = 41
    EnergyTank = 42
    PowerBomb = 43
    Missile = 44
    DarkAmmo = 45
    LightAmmo = 46
    ItemPercentage = 47
    NumPlayersJoined = 48
    NumPlayersInOptionsMenu = 49
    MiscCounter3 = 50
    MiscCounter4 = 51
    SwitchWeaponPower = 52
    SwitchWeaponDark = 53
    SwitchWeaponLight = 54
    SwitchWeaponAnnihilator = 55
    MultiChargeUpgrade = 56
    Invisibility = 57
    AmpDamage = 58
    Invincibility = 59
    UnknownItem60 = 60
    UnknownItem61 = 61
    UnknownItem62 = 62
    UnknownItem63 = 63
    FragCount = 64
    DiedCount = 65
    ArchenemyCount = 66
    PersistentCounter1 = 67
    PersistentCounter2 = 68
    PersistentCounter3 = 69
    PersistentCounter4 = 70
    PersistentCounter5 = 71
    PersistentCounter6 = 72
    PersistentCounter7 = 73
    PersistentCounter8 = 74
    SwitchVisorCombat = 75
    SwitchVisorScan = 76
    SwitchVisorDark = 77
    SwitchVisorEcho = 78
    CoinAmplifier = 79
    CoinCounter = 80
    UnlimitedMissiles = 81
    UnlimitedBeamAmmo = 82
    DarkShield = 83
    LightShield = 84
    AbsorbAttack = 85
    DeathBall = 86
    ScanVirus = 87
    VisorStatic = 88
    DisableBeamAmmo = 89
    DisableMissiles = 90
    DisableMorphBall = 91
    DisableBall = 92
    DisableSpaceJump = 93
    UnknownItem94 = 94
    HackedEffect = 95
    CannonBall = 96
    VioletTranslator = 97
    AmberTranslator = 98
    EmeraldTranslator = 99
    CobaltTranslator = 100
    SkyTempleKey4 = 101
    SkyTempleKey5 = 102
    SkyTempleKey6 = 103
    SkyTempleKey7 = 104
    SkyTempleKey8 = 105
    SkyTempleKey9 = 106
    EnergyTransferModuleInventory = 107
    ChargeCombo = 108

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


class ScanSpeedEnum(enum.IntEnum):
    Normal = 0
    Slow = 1

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


class WeaponTypeEnum(enum.IntEnum):
    Power = 0
    Dark = 1
    Light = 2
    Annihilator = 3
    Bomb = 4
    PowerBomb = 5
    Missile = 6
    BoostBall = 7
    CannonBall = 8
    ScrewAttack = 9
    Phazon = 10
    AI = 11
    PoisonWater1 = 12
    PoisonWater2 = 13
    Lava = 14
    Hot = 15
    Cold = 16
    AreaDark = 17
    AreaLight = 18
    UnknownSource = 19
    SafeZone = 20

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
