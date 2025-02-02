"""Module for helper functions that retrieve info associated with a time unit."""

from typing import Final

from .info import UnitInfo
from .unit import Unit

# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    UnitInfo(
        unit=Unit.SECOND,
        name="second",
        abbreviation="s",
        unit_delta_per_second=1,
    ),
    UnitInfo(
        unit=Unit.MINUTE,
        name="minute",
        abbreviation="min",
        unit_delta_per_second=1 / 60,
    ),
    UnitInfo(
        unit=Unit.HOUR,
        name="hour",
        abbreviation="h",
        unit_delta_per_second=1 / (60 * 60),
    ),
    UnitInfo(
        unit=Unit.MICROSECOND,
        name="microsecond",
        abbreviation="us",
        unit_delta_per_second=1e6,
    ),
    UnitInfo(
        unit=Unit.MILLISECOND,
        name="millisecond",
        abbreviation="ms",
        unit_delta_per_second=1e3,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the time unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the time unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_second(
    unit: Unit,
) -> float:
    """Get the change in time expressed as the unit per 1s.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_pascal
    except KeyError as e:
        raise ValueError from e
