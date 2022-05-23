from typing import Optional

from retro_data_structures.base_resource import AssetId


class UnknownAssetId(Exception):
    def __init__(self, asset_id: AssetId, name: Optional[str] = None):
        msg = f"Unknown asset id 0x{asset_id:08X}"
        if isinstance(name, str):
            msg += f" ({name})"
        super().__init__(msg)
        self.asset_id = asset_id


class InvalidAssetId(Exception):
    def __init__(self, asset_id, reason: str):
        super().__init__(f"Unable to decode asset id 0x{asset_id:08X}: {reason}")
        self.asset_id = asset_id
        self.reason = reason