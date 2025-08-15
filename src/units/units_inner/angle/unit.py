"""Module for the angle units."""

import math
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A angle unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    RADIAN = 1
    DEGREE = 2
    REVOLUTION = 3


class _UnitInfo:
    """Information associated with a particular angle unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_radian: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_radian = unit_delta_per_radian

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
    def unit_delta_per_radian(self) -> float:
        """The change in angle expressed as the unit per 1rad.

        Equivalent to the gradient of the radian-vs-unit graph.
        """
        return self._unit_delta_per_radian


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.RADIAN,
        name="radian",
        abbreviation="rad",
        unit_delta_per_radian=1,
    ),
    _UnitInfo(
        unit=Unit.DEGREE,
        name="degree",
        abbreviation="deg",
        unit_delta_per_radian=180 / math.pi,
    ),
    _UnitInfo(
        unit=Unit.REVOLUTION,
        name="revolution",
        abbreviation="rev",
        unit_delta_per_radian=1 / (2 * math.pi),
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the angle unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the angle unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_radian(
    unit: Unit,
) -> float:
    """Get the change in angle expressed as the unit per 1rad.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_radian
    except KeyError as e:
        raise ValueError from e
