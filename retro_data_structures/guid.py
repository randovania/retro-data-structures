"""
Wiki: https://wiki.axiodl.com/w/GUID
"""

from construct import Array, Int64ub

GUID = Array(2, Int64ub)
