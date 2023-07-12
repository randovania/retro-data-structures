from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from retro_data_structures.base_resource import AssetId


def format_asset_id(asset_id: AssetId) -> str:
    if isinstance(asset_id, int):
        return f"0x{asset_id:08X}"
    else:
        return str(asset_id)


class UnknownAssetId(Exception):
    def __init__(self, asset_id: AssetId, name: str | None = None):
        msg = f"Unknown asset id {format_asset_id(asset_id)}"
        if isinstance(name, str):
            msg += f" ({name})"
        super().__init__(msg)
        self.asset_id = asset_id


class InvalidAssetId(Exception):
    def __init__(self, asset_id, reason: str):
        super().__init__(f"Unable to decode asset id {format_asset_id(asset_id)}: {reason}")
        self.asset_id = asset_id
        self.reason = reason


class DependenciesHandledElsewhere(Exception):
    pass
