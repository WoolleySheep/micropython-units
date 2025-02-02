"""Module for helper functions that retrieve info associated with a volume unit."""

from typing import Final

from .info import UnitInfo
from .unit import Unit

# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    UnitInfo(
        unit=Unit.CUBIC_METER,
        name="cubic meter",
        abbreviation="m^3",
        unit_delta_per_cubic_meter=1,
    ),
    UnitInfo(
        unit=Unit.LITRE,
        name="litre",
        abbreviation="L",
        unit_delta_per_cubic_meter=1_000,
    ),
    UnitInfo(
        unit=Unit.MILLILITRE,
        name="millilitre",
        abbreviation="mL",
        unit_delta_per_cubic_meter=1_000_000,
    ),
    UnitInfo(
        unit=Unit.MICROLITRE,
        name="microlitre",
        abbreviation="uL",
        unit_delta_per_cubic_meter=1_000_000_000,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the volume unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the volume unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_cubic_meter(
    unit: Unit,
) -> float:
    """Get the change in volume expressed as the unit per 1m^3.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_pascal
    except KeyError as e:
        raise ValueError from e
