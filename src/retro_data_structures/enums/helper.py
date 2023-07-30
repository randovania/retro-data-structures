from __future__ import annotations

import retro_data_structures.enums.corruption as _corruption_enums
import retro_data_structures.enums.echoes as _echoes_enums
import retro_data_structures.enums.prime as _prime_enums
import retro_data_structures.enums.shared_enums as _shared_enums
from retro_data_structures.game_check import Game

STATE_PER_GAME: dict[Game, type[_shared_enums.State]] = {
    Game.PRIME: _prime_enums.State,
    Game.ECHOES: _echoes_enums.State,
    Game.CORRUPTION: _corruption_enums.State,
}

MESSAGE_PER_GAME: dict[Game, type[_shared_enums.Message]] = {
    Game.PRIME: _prime_enums.Message,
    Game.ECHOES: _echoes_enums.Message,
    Game.CORRUPTION: _corruption_enums.Message,
}
