"""Module for helper functions that retrieve info associated with a mass unit."""

from typing import Final

from .info import UnitInfo
from .unit import Unit

# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    UnitInfo(
        unit=Unit.KILOGRAM,
        name="kilogram",
        abbreviation="kg",
        unit_delta_per_kilogram=1,
    ),
    UnitInfo(
        unit=Unit.GRAM,
        name="gram",
        abbreviation="g",
        unit_delta_per_kilogram=1_000,
    ),
    UnitInfo(
        unit=Unit.MILLIGRAM,
        name="milligram",
        abbreviation="mg",
        unit_delta_per_kilogram=1_000_000,
    ),
    UnitInfo(
        unit=Unit.POUND,
        name="pound",
        abbreviation="lb",
        unit_delta_per_kilogram=2.20462262185,
    ),
    UnitInfo(
        unit=Unit.OUNCE,
        name="ounce",
        abbreviation="oz",
        unit_delta_per_kilogram=35.2739619496,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the mass unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the mass unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_kilogram(
    unit: Unit,
) -> float:
    """Get the change in mass expressed as the unit per 1kg.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_kilogram
    except KeyError as e:
        raise ValueError from e
