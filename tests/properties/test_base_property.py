from __future__ import annotations

import dataclasses

from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.echoes.archetypes.Vector2f import Vector2f
from retro_data_structures.properties.field_reflection import FieldReflection, get_reflection


@dataclasses.dataclass
class DummyProperty(BaseProperty):
    other_property: Vector2f = dataclasses.field(
        metadata={
            "reflection": FieldReflection[Vector2f](
                Vector2f,
                id=0x0,
                original_name="other_property",
                from_json=Vector2f.from_json,
                to_json=Vector2f.to_json,
            ),
        }
    )
    str_annotation: int = dataclasses.field(
        metadata={
            "asset_types": ["MREA"],
            "reflection": FieldReflection[int](
                int,
                id=0x1,
                original_name="str_annotation",
            ),
        }
    )
    sound: int = dataclasses.field(
        metadata={
            "sound": True,
            "reflection": FieldReflection[int](
                int,
                id=0x2,
                original_name="sound",
            ),
        }
    )
    union: int | None = dataclasses.field(
        default=0xFFFFFFFF,
        metadata={
            "reflection": FieldReflection[int | None](
                int,
                id=0x3,
                original_name="union",
            )
        },
    )


def test_dependencies(prime2_asset_manager):
    from retro_data_structures.base_resource import Dependency

    dummy = DummyProperty(
        Vector2f(),
        0xFFFFFFFF,
        1,
        0x07E36D6F,  # some random RULE
    )

    dependencies = list(dummy.dependencies_for(prime2_asset_manager))
    assert dependencies == [
        Dependency("AGSC", 0xC8739BEC),
        Dependency("RULE", 0x9C1232E2),
        Dependency("RULE", 0x07E36D6F),
    ]


def test_get_reflection():
    reflection = get_reflection(DummyProperty)

    assert reflection == {
        "other_property": FieldReflection[Vector2f](
            Vector2f,
            id=0x0,
            original_name="other_property",
            from_json=Vector2f.from_json,
            to_json=Vector2f.to_json,
        ),
        "str_annotation": FieldReflection[int](
            int,
            id=0x1,
            original_name="str_annotation",
        ),
        "sound": FieldReflection[int](
            int,
            id=0x2,
            original_name="sound",
        ),
        "union": FieldReflection[int | None](
            int,
            id=0x3,
            original_name="union",
        ),
    }
