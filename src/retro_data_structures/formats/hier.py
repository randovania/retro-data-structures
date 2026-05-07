from __future__ import annotations

import dataclasses
import typing

import construct
from construct import Aligned, Const, Construct, Int32ub, PrefixedArray, Struct

from retro_data_structures.base_resource import AssetId, AssetType, BaseResource, Dependency
from retro_data_structures.common_types import AssetId32, String
from retro_data_structures.formats import Strg

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

    from retro_data_structures.game_check import Game

HIER = Aligned(
    32,
    Struct(
        magic=Const(b"HIER"),
        entries=PrefixedArray(
            Int32ub,
            Struct(
                string_table_id=AssetId32,
                name=String,
                scan_id=AssetId32,
                parent_id=Int32ub,
            ),
        ),
    ),
    b"\xff",
)


@dataclasses.dataclass()
class HierEntry:
    string_table_id: typing.Annotated[AssetId, Strg]
    name: str
    scan_id: AssetId

    parent_id: int
    """Is 0xFFFFFFFF when there's no parent."""


class Hier(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return HIER

    @classmethod
    def resource_type(cls) -> AssetType:
        return "DUMB"

    __hash__ = None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Hier) and self._raw == other._raw

    @property
    def entries(self) -> tuple[HierEntry, ...]:
        return tuple(
            HierEntry(
                string_table_id=entry.string_table_id,
                name=entry.name,
                scan_id=entry.scan_id,
                parent_id=entry.parent_id,
            )
            for entry in self._raw.entries
        )

    @entries.setter
    def entries(self, value: Iterable[HierEntry]) -> None:
        self._raw.entries = construct.ListContainer(
            [
                construct.Container(
                    string_table_id=entry.string_table_id,
                    name=entry.name,
                    scan_id=entry.scan_id,
                    parent_id=entry.parent_id,
                )
                for entry in value
            ]
        )

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for entry in self.raw.entries:
            yield from self.asset_manager.get_dependencies_for_asset(entry.string_table_id)
