"""Module for helper functions that retrieve info associated with a temperature unit."""

from typing import Final

from .conversion_parameters import UnitConversionParameters
from .info import UnitInfo
from .unit import Unit

# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    UnitInfo(
        unit=Unit.KELVIN,
        name="kelvin",
        abbreviation="K",
        conversion_parameters=UnitConversionParameters(1, 0),
    ),
    UnitInfo(
        unit=Unit.CELSIUS,
        name="celsius",
        abbreviation="C",
        conversion_parameters=UnitConversionParameters(1, -273.15),
    ),
    UnitInfo(
        unit=Unit.FAHRENHEIT,
        name="fahrenheit",
        abbreviation="F",
        conversion_parameters=UnitConversionParameters(9 / 5, -459.67),
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the temperature unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the temperature unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_kelvin_to_unit_conversion_parameters(
    unit: Unit,
) -> UnitConversionParameters:
    """Get the parameters to convert a value from kelvin to the temperature unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].conversion_parameters
    except KeyError as e:
        raise ValueError from e
