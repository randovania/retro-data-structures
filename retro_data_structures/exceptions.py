class UnknownAssetId(Exception):
    def __init__(self, asset_id):
        super().__init__(f"Unknown asset id 0x{asset_id:08X}")
        self.asset_id = asset_id


class InvalidAssetId(Exception):
    def __init__(self, asset_id, reason: str):
        super().__init__(f"Unable to decode asset id 0x{asset_id:08X}: {reason}")
        self.asset_id = asset_id
        self.reason = reason