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
    Acquired = "ACQU"
    Active = "ACTV"
    AILogicState1 = "AIS1"
    AILogicState2 = "AIS2"
    AILogicState3 = "AIS3"
    AnimOver = "ANMO"
    AnimStart = "ANMS"
    Approach = "APRC"
    Arrived = "ARRV"
    AttachedCollisionObject = "ATCL"
    AttachedAnimatedObject = "ATOB"
    AttachedPath = "ATPA"
    Attack = "ATTK"
    BezierSpline = "BEZR"
    BallIceXDamage = "BIDG"
    BeginScan = "BSCN"
    BSpline = "BSPL"
    BallXDamage = "BXDG"
    CameraInsuranceTarget = "CINT"
    Closed = "CLOS"
    Connect = "CONN"
    CameraPath = "CPTH"
    CatmullRomSpline = "CROM"
    CameraTarget = "CTGT"
    CameraTime = "CTIM"
    Damage = "DAMG"
    DamageBomb = "DBMB"
    Dead = "DEAD"
    DeGenerate = "DGNR"
    Down = "DOWN"
    DarkXDamage = "DRKX"
    Entered = "ENTR"
    EndScan = "ESCN"
    Exited = "EXIT"
    Footstep = "FOOT"
    FOVPath = "FOVP"
    Freeze = "FREZ"
    Generate0 = "GRN0"
    Generate1 = "GRN1"
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
    InternalState20 = "IS20"
    InternalState21 = "IS21"
    InternalState22 = "IS22"
    InternalState23 = "IS23"
    InternalState24 = "IS24"
    InternalState25 = "IS25"
    InternalState26 = "IS26"
    InternalState27 = "IS27"
    InternalState28 = "IS28"
    InternalState29 = "IS29"
    InternalState30 = "IS30"
    InternalState31 = "IS31"
    InternalState32 = "IS32"
    InternalState33 = "IS33"
    InternalState34 = "IS34"
    InternalState35 = "IS35"
    InternalState36 = "IS36"
    InternalState37 = "IS37"
    InternalState38 = "IS38"
    InternalState39 = "IS39"
    InternalState40 = "IS40"
    InternalState41 = "IS41"
    InternalState44 = "IS44"
    InternalState45 = "IS45"
    InternalState46 = "IS46"
    InternalState47 = "IS47"
    InternalState48 = "IS48"
    DrawAfter = "LDWA"
    DrawBefore = "LDWB"
    Left = "LEFT"
    LinearSpline = "LINR"
    Locked = "LOCK"
    ThinkAfter = "LTKA"
    ThinkBefore = "LTKB"
    MaxReached = "MAXR"
    Modify = "MDFY"
    MotionPath = "MOTP"
    MotionSpline = "MOTS"
    Next = "NEXT"
    Open = "OPEN"
    OrbitObject = "ORBO"
    Play = "PLAY"
    PlayerPath = "PLRP"
    PressA = "PRSA"
    PressB = "PRSB"
    PressStart = "PRST"
    PressX = "PRSX"
    PressY = "PRSY"
    PressZ = "PRSZ"
    Patrol = "PTRL"
    DeathRattle = "RATL"
    RCRM = "RCRM"
    SpawnResidue = "RDUE"
    ReflectedDamage = "REFD"
    ResistedDamage = "RESD"
    Right = "RGHT"
    Relay = "RLAY"
    RotationOver = "ROTO"
    RotationStart = "ROTS"
    Retreat = "RTRT"
    ScanDone = "SCND"
    ScanSource = "SCNS"
    SE01 = "SE01"
    SE02 = "SE02"
    SE03 = "SE03"
    Slave = "SLAV"
    SpawnLargeCreatures = "SLCR"
    SpawnMediumCreatures = "SMCR"
    Sequence = "SQNC"
    SpawnSmallCreatures = "SSCR"
    TargetObject = "TGTO"
    TargetPath = "TGTP"
    TargetSpline = "TGTS"
    UnFreeze = "UFRZ"
    Unlocked = "ULCK"
    Up = "UP  "
    WLTE = "WLTE"
    BackToFront = "XB2F"
    XDamage = "XDMG"
    FrontToBack = "XF2B"
    InBack = "XINB"
    InFront = "XINF"
    Outside = "XOUT"
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
    Arrived = "ARRV"
    Attach = "ATCH"
    AttachInstance = "ATCI"
    Close = "CLOS"
    ClearOriginator = "CORG"
    Deactivate = "DCTV"
    Decrement = "DECR"
    Down = "DOWN"
    Escape = "ESCP"
    FadeIn = "FADI"
    FadeOut = "FADO"
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
    InternalMessage15 = "IM15"
    InternalMessage16 = "IM16"
    InternalMessage17 = "IM17"
    InternalMessage18 = "IM18"
    InternalMessage19 = "IM19"
    InternalMessage20 = "IM20"
    InternalMessage21 = "IM21"
    InternalMessage22 = "IM22"
    InternalMessage23 = "IM23"
    InternalMessage24 = "IM24"
    InternalMessage25 = "IM25"
    InternalMessage26 = "IM26"
    InternalMessage27 = "IM27"
    InternalMessage28 = "IM28"
    InternalMessage42 = "IM42"
    InternalMessage43 = "IM43"
    Increment = "INCR"
    Kill = "KILL"
    Left = "LEFT"
    Load = "LOAD"
    Lock = "LOCK"
    Next = "NEXT"
    _None = "NONE"
    Off = "OFF "
    On = "ON  "
    Open = "OPEN"
    Play = "PLAY"
    Right = "RGHT"
    ResetMovement = "RMOV"
    ResetAngle = "RSAN"
    Reset = "RSET"
    ResetPath = "RSTP"
    ResetAndStart = "RSTS"
    StopAllSounds = "SALL"
    StopAllLoopedSounds = "SALP"
    SetToMax = "SMAX"
    SetOriginator = "SORG"
    Stop = "STOP"
    StopAndReset = "STPR"
    Start = "STRT"
    ToggleActive = "TCTV"
    ToggleOpen = "TOPN"
    Unlock = "ULCK"
    Unload = "ULOD"
    Up = "UP  "
    AreaLoaded = "XALD"
    AcidOnVisor = "XAOV"
    AIUpdateDisabled = "XAUD"
    AreaUnloading = "XAUL"
    Clear = "XCLR"
    Create = "XCRT"
    Delete = "XDEL"
    XDamage = "XDMG"
    EnteredFluid = "XENF"
    XENT = "XENT"
    EnteredPhazonPool = "XEPZ"
    ExitedFluid = "XEXF"
    Falling = "XFAL"
    HitObject = "XHIT"
    InsideFluid = "XINF"
    InShrubbery = "XINS"
    InsidePhazonPool = "XIPZ"
    Launching = "XLAU"
    Landed = "XLND"
    LandedOnStaticGround = "XLSG"
    OffGround = "XOFF"
    OnDirt = "XOND"
    OnIce = "XONI"
    OnOrganic = "XONO"
    OnPlatform = "XONP"
    XRDG = "XRDG"
    WorldLoaded = "XWLD"
    XXDG = "XXDG"
    ExitedPhazonPool = "XXPZ"
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


class BerserkerEnumEnum(enum.IntEnum):
    Unknown1 = 2457151020
    Unknown2 = 2362448510
    Unknown3 = 2161792701
    Unknown4 = 4046075334

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


class CableEnumEnum(enum.IntEnum):
    Unknown1 = 2161975732
    Unknown2 = 617560305
    Unknown3 = 590757843

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


class DamageableTriggerEnumEnum(enum.IntEnum):
    Unknown1 = 498294111
    Unknown2 = 1637064024
    Unknown3 = 945710146
    Unknown4 = 210876390

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


class HyperModeTypeEnum(enum.IntEnum):
    Unknown1 = 2781966248
    Unknown2 = 440171881
    Unknown3 = 4246244689

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


class MiscControls_UnknownEnum1Enum(enum.IntEnum):
    Unknown1 = 3138569503
    Unknown2 = 3604958465
    Unknown3 = 1504980732
    Unknown4 = 3891005505
    Unknown5 = 4199960577

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


class PhysicalControlEnum(enum.IntEnum):
    Unknown1 = 538784560
    Unknown2 = 3795023653
    Unknown3 = 2527082480
    Unknown4 = 262760010
    Unknown5 = 1706296828
    Unknown6 = 4240266310
    Unknown7 = 3978335045
    Unknown8 = 371522223
    Unknown9 = 1096604377
    Unknown10 = 680639111
    Unknown11 = 667200906
    Unknown12 = 2697488232
    Unknown13 = 1761263604
    Unknown14 = 2435665866
    Unknown15 = 1593512693
    Unknown16 = 514168199
    Unknown17 = 1496847900
    Unknown18 = 830697549
    Unknown19 = 2753380155
    Unknown20 = 2017321684
    Unknown21 = 1170446731
    Unknown22 = 3704277041
    Unknown23 = 3114222144
    Unknown24 = 1405012678
    Unknown25 = 2759137981
    Unknown26 = 2577594915
    Unknown27 = 1462419467
    Unknown28 = 1295727496
    Unknown29 = 888257540
    Unknown30 = 732122331
    Unknown31 = 1712867438
    Unknown32 = 2411151363
    Unknown33 = 1133573905
    Unknown34 = 1168863462
    Unknown35 = 3776455486
    Unknown36 = 2014409348
    Unknown37 = 2238942206
    Unknown38 = 4067736424
    Unknown39 = 2195767795
    Unknown40 = 1803414226
    Unknown41 = 2678677379
    Unknown42 = 1705403104
    Unknown43 = 1923125713
    Unknown44 = 438438636
    Unknown45 = 713052917
    Unknown46 = 1276650918
    Unknown47 = 4150513473
    Unknown48 = 620168925
    Unknown49 = 3133194335
    Unknown50 = 2481737266
    Unknown51 = 530264547
    Unknown52 = 4118034785
    Unknown53 = 3915798836
    Unknown54 = 2620818456
    Unknown55 = 3291423487
    Unknown56 = 4205769547
    Unknown57 = 4018211503
    Unknown58 = 4242657632
    Unknown59 = 2593197220
    Unknown60 = 2591663667
    Unknown61 = 391300525
    Unknown62 = 1938441096
    Unknown63 = 1047334326

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


class PhysicalControlBooleanEnum(enum.IntEnum):
    Unknown1 = 3437305164
    Unknown2 = 1743300625
    Unknown3 = 3272702804

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
    PowerBeam = 4218679992
    PlasmaBeam = 2477616633
    NovaBeam = 1352706725
    ChargeUpgrade = 893945120
    Missile = 2452465320
    IceMissile = 2431700692
    SeekerMissile = 3086280557
    GrappleBeamPull = 1906007133
    GrappleBeamSwing = 522801372
    GrappleBeamVoltage = 536233745
    Bomb = 3112660177
    CombatVisor = 2523287191
    ScanVisor = 3016416327
    CommandVisor = 1943434474
    XRayVisor = 1714103130
    DoubleJump = 2512389418
    ScrewAttack = 3654131422
    SuitType = 3492481752
    Energy = 649447109
    HypermodeEnergy = 496397544
    EnergyTank = 3010129117
    ItemPercentage = 1347001155
    Fuses = 2881244206
    Fuse1 = 862874770
    Fuse2 = 2858892584
    Fuse3 = 3714059710
    Fuse4 = 1124374557
    Fuse5 = 872654987
    Fuse6 = 2903177521
    Fuse7 = 3658336679
    Fuse8 = 1253233718
    Fuse9 = 1035330720
    MorphBall = 1211073077
    BoostBall = 2988161223
    SpiderBall = 1296127826
    HyperModeTank = 1432926409
    HyperModeBeam = 1239982508
    HyperModeMissile = 1364547232
    HyperModeBall = 2353547179
    HyperModeGrapple = 2270562373
    HyperModePermanent = 2414588173
    HyperModePhaaze = 4110398365
    HyperModeOriginal = 3854177617
    ShipGrapple = 1470237978
    ShipMissile = 2174833663
    FaceCorruptionLevel = 2109957860
    PhazonBall = 1373743611
    CannonBall = 2070581050
    ActivateMorphballBoost = 3022734302
    HyperShot = 2307731988
    CommandVisorJammed = 1065514078
    Stat_EnemiesKilled = 3227265003
    Stat_ShotsFired = 2966561623
    Stat_DamageReceived = 3809976091
    Stat_DataSaves = 4187912088
    Stat_HypermodeUses = 1141429883
    Stat_CommandoKills = 1206369514
    Stat_TinCanHighScore = 574164774
    Stat_TinCanCurrentScore = 951995458

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


class RevolutionControlTypeEnum(enum.IntEnum):
    Unknown1 = 1989807457
    Unknown2 = 3492954719
    Unknown3 = 2606158878
    Unknown4 = 1231291285
    Unknown5 = 3555293293
    Unknown6 = 1272469130
    Unknown7 = 3663496210

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


class RevolutionControl_UnknownEnum1Enum(enum.IntEnum):
    Unknown1 = 2597642428
    Unknown2 = 1190654113
    Unknown3 = 2373762245
    Unknown4 = 2784335752
    Unknown5 = 1553256326
    Unknown6 = 3438239968
    Unknown7 = 2352913090
    Unknown8 = 4049356512
    Unknown9 = 3952457493
    Unknown10 = 3273432152
    Unknown11 = 2212135243
    Unknown12 = 329330221

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


class RevolutionControl_UnknownEnum2Enum(enum.IntEnum):
    Unknown1 = 1154737403
    Unknown2 = 967762110
    Unknown3 = 1744548478

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


class RevolutionVirtualControlEnum(enum.IntEnum):
    Unknown1 = 2997493716
    Unknown2 = 288465778
    Unknown3 = 4009748226
    Unknown4 = 3635765891
    Unknown5 = 891244416
    Unknown6 = 2689619302
    Unknown7 = 837808268
    Unknown8 = 21086754
    Unknown9 = 396303202
    Unknown10 = 3664856383
    Unknown11 = 3484034738
    Unknown12 = 733602211
    Unknown13 = 3559541428
    Unknown14 = 1097158738
    Unknown15 = 280637756
    Unknown16 = 3031673392

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


class TweakGui_UnknownEnum1Enum(enum.IntEnum):
    Unknown1 = 4043628561
    Unknown2 = 1745727915
    Unknown3 = 520782141
    Unknown4 = 2171475102
    Unknown5 = 4134085640
    Unknown6 = 1868592562
    Unknown7 = 4292831267
    Unknown8 = 1285035198

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


class TweakPlayer_AimStuff_UnknownEnum1Enum(enum.IntEnum):
    Unknown1 = 3836570269
    Unknown2 = 3796405200
    Unknown3 = 4233376783

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


class TweakPlayer_AimStuff_UnknownEnum2Enum(enum.IntEnum):
    Unknown1 = 2531440486
    Unknown2 = 313036472
    Unknown3 = 576609856
    Unknown4 = 2183082095

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


class UnknownEnum1Enum(enum.IntEnum):
    Unknown1 = 1990589437
    Unknown2 = 2503861812
    Unknown3 = 2707747667

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
