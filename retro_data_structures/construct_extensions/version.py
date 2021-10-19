import enum
from functools import partial

from construct import EnumIntegerString, IfThenElse, If


def get_version(this, enum_type):
    if "version" not in this:
        return get_version(this["_"], enum_type)
    else:
        if isinstance(this.version, EnumIntegerString):
            return int(this.version)
        if enum_type and isinstance(this.version, str):
            return enum_type[this.version]
        return this.version


def compare_version(version):
    if isinstance(version, enum.Enum):
        return partial(get_version, enum_type=type(version))
    return partial(get_version, enum_type=None)


def WithVersionElse(version, with_subcon, before_subcon):
    return IfThenElse(lambda this: compare_version(version)(this) >= version, with_subcon, before_subcon)


def WithVersion(version, subcon):
    return If(lambda this: compare_version(version)(this) >= version, subcon)


def BeforeVersion(version, subcon):
    return If(lambda this: compare_version(version)(this) < version, subcon)
