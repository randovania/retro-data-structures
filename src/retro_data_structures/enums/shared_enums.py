# Generated File
from __future__ import annotations

import retro_data_structures.enums.corruption as _corruption_enums
import retro_data_structures.enums.echoes as _echoes_enums
import retro_data_structures.enums.prime as _prime_enums
import retro_data_structures.enums.prime_remastered as _prime_remastered_enums

ControllerMappingEnum = _prime_enums.ControllerMappingEnum | _echoes_enums.ControllerMappingEnum
Message = _prime_enums.Message | _echoes_enums.Message | _corruption_enums.Message
PlayerItemEnum = (
    _prime_enums.PlayerItemEnum
    | _echoes_enums.PlayerItemEnum
    | _corruption_enums.PlayerItemEnum
    | _prime_remastered_enums.PlayerItemEnum
)
ScanSpeedEnum = _prime_enums.ScanSpeedEnum | _echoes_enums.ScanSpeedEnum | _corruption_enums.ScanSpeedEnum
State = _prime_enums.State | _echoes_enums.State | _corruption_enums.State
WeaponTypeEnum = _prime_enums.WeaponTypeEnum | _echoes_enums.WeaponTypeEnum
