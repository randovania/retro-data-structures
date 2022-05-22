from retro_data_structures.base_resource import AssetId


class AssetReference:
    asset_id: AssetId
    description: str
    is_custom: bool

    def __init__(self, asset_id: AssetId, description: str, is_custom: bool):
        self.asset_id = asset_id
        self.description = description
        self.is_custom = is_custom

    def __repr__(self):
        return "AssetReference<{self.description}, {self.asset_id:08x}>".format(self=self)
