"""Module for helper functions that retrieve info associated with a pressure unit."""

from typing import Final

from .constants import STANDARD_ATMOSPHERIC_PRESSURE_AS_PASCAL
from .info import UnitInfo
from .unit import Unit

# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    UnitInfo(
        unit=Unit.PASCAL,
        name="pascal",
        abbreviation="Pa",
        unit_delta_per_pascal=1,
    ),
    UnitInfo(
        unit=Unit.POUND_PER_SQUARE_INCH,
        name="pound-per-square-inch",
        abbreviation="PSI",
        unit_delta_per_pascal=0.00014503773773,
    ),
    UnitInfo(
        unit=Unit.BAR,
        name="bar",
        abbreviation="bar",
        unit_delta_per_pascal=1 / 100_000,
    ),
    UnitInfo(
        unit=Unit.ATMOSPHERE,
        name="atmosphere",
        abbreviation="atm",
        unit_delta_per_pascal=1 / STANDARD_ATMOSPHERIC_PRESSURE_AS_PASCAL,
    ),
    UnitInfo(
        unit=Unit.MILLIMETER_OF_MERCURY,
        name="millimeter-of-mercury",
        abbreviation="mmHg",
        unit_delta_per_pascal=1 / 133.322387415,
    ),
    UnitInfo(
        unit=Unit.KILOPASCAL,
        name="kilopascal",
        abbreviation="kPa",
        unit_delta_per_pascal=1 / 1_000,
    ),
    UnitInfo(
        unit=Unit.MILLIBAR,
        name="millibar",
        abbreviation="mbar",
        unit_delta_per_pascal=1 / 100,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the pressure unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the pressure unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_pascal(
    unit: Unit,
) -> float:
    """Get the change in pressure expressed as the unit per 1Pa.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_pascal
    except KeyError as e:
        raise ValueError from e
