from typing import Any

from construct import EnumIntegerString
from construct.lib import ListContainer, Container


def convert_to_raw_python(value) -> Any:
    if callable(value):
        value = value()

    if isinstance(value, ListContainer):
        return [convert_to_raw_python(item) for item in value]

    if isinstance(value, Container):
        return {key: convert_to_raw_python(item) for key, item in value.items() if not key.startswith("_")}

    if isinstance(value, EnumIntegerString):
        return str(value)

    return value
