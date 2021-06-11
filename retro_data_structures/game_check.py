"""
For checking which game is being parsed
"""

import construct
from construct import IfThenElse

from retro_data_structures import common_types

get_current_game = construct.this["_params"]["game_hack"]
is_prime1 = (get_current_game + 0 == 1)
is_prime2 = (get_current_game + 0 == 2)
is_prime3 = (get_current_game + 0 == 3)
uses_asset_id_32 = (get_current_game < 3)
uses_lzo = (get_current_game >= 2)

AssetIdCorrect = IfThenElse(uses_asset_id_32, common_types.AssetId32, common_types.AssetId64)
ObjectTagCorrect = IfThenElse(uses_asset_id_32, common_types.ObjectTag_32, common_types.ObjectTag_64)
