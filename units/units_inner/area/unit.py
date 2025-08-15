"""Module for the area unit enum."""

# ruff: noqa: TID252

from typing import TYPE_CHECKING, Final

from ..length import Unit as DistanceUnit
from ..length import get_unit_abbreviation as get_distance_unit_abbreviation
from ..length import get_unit_delta_per_metre as get_distance_unit_delta_per_metre
from ..length import get_unit_name as get_distance_unit_name

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """An area unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    SQUARE_METRE = 1
    SQUARE_CENTIMETRE = 2
    SQUARE_MILLIMETRE = 3
    SQUARE_YARD = 4
    SQUARE_FOOT = 5
    SQUARE_INCH = 6


class _UnitInfo:
    """Information associated with a area particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_square_metre: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_square_metre = unit_delta_per_square_metre

    @property
    def unit(self) -> Unit:
        """The unit the information relates to."""
        return self._unit

    @property
    def name(self) -> str:
        """The name of the unit."""
        return self._name

    @property
    def abbreviation(self) -> str:
        """The abbreviation of the unit."""
        return self._abbreviation

    @property
    def unit_delta_per_square_metre(self) -> float:
        """The change in area expressed as the unit per 1m^2.

        Equivalent to the gradient of the square-metre-vs-unit graph.
        """
        return self._unit_delta_per_square_metre


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.SQUARE_METRE,
        name=f"square {get_distance_unit_name(DistanceUnit.METRE)}",
        abbreviation=f"{get_distance_unit_abbreviation(DistanceUnit.METRE)}^2",
        unit_delta_per_square_metre=get_distance_unit_delta_per_metre(
            DistanceUnit.METRE
        )
        ** 2,
    ),
    _UnitInfo(
        unit=Unit.SQUARE_CENTIMETRE,
        name=f"square {get_distance_unit_name(DistanceUnit.CENTIMETRE)}",
        abbreviation=f"{get_distance_unit_abbreviation(DistanceUnit.CENTIMETRE)}^2",
        unit_delta_per_square_metre=get_distance_unit_delta_per_metre(
            DistanceUnit.CENTIMETRE
        )
        ** 2,
    ),
    _UnitInfo(
        unit=Unit.SQUARE_MILLIMETRE,
        name=f"square {get_distance_unit_name(DistanceUnit.MILLIMETRE)}",
        abbreviation=f"{get_distance_unit_abbreviation(DistanceUnit.MILLIMETRE)}^2",
        unit_delta_per_square_metre=get_distance_unit_delta_per_metre(
            DistanceUnit.MILLIMETRE
        )
        ** 2,
    ),
    _UnitInfo(
        unit=Unit.SQUARE_YARD,
        name=f"square {get_distance_unit_name(DistanceUnit.YARD)}",
        abbreviation=f"{get_distance_unit_abbreviation(DistanceUnit.YARD)}^2",
        unit_delta_per_square_metre=get_distance_unit_delta_per_metre(DistanceUnit.YARD)
        ** 2,
    ),
    _UnitInfo(
        unit=Unit.SQUARE_FOOT,
        name=f"square {get_distance_unit_name(DistanceUnit.FOOT)}",
        abbreviation=f"{get_distance_unit_abbreviation(DistanceUnit.FOOT)}^2",
        unit_delta_per_square_metre=get_distance_unit_delta_per_metre(DistanceUnit.FOOT)
        ** 2,
    ),
    _UnitInfo(
        unit=Unit.SQUARE_INCH,
        name=f"square {get_distance_unit_name(DistanceUnit.INCH)}",
        abbreviation=f"{get_distance_unit_abbreviation(DistanceUnit.INCH)}^2",
        unit_delta_per_square_metre=get_distance_unit_delta_per_metre(DistanceUnit.INCH)
        ** 2,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the area unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the area unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_square_metre(
    unit: Unit,
) -> float:
    """Get the change in area expressed as the unit per 1m^2.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_square_metre
    except KeyError as e:
        raise ValueError from e
