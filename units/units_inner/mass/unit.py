"""Module for the mass units."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A mass unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    KILOGRAM = 1
    GRAM = 2
    MILLIGRAM = 3
    POUND = 4
    OUNCE = 5


class _UnitInfo:
    """Information associated with a mass particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_kilogram: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_kilogram = unit_delta_per_kilogram

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
    def unit_delta_per_kilogram(self) -> float:
        """The change in mass expressed as the unit per 1kg.

        Equivalent to the gradient of the kilogram-vs-unit graph.
        """
        return self._unit_delta_per_kilogram


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.KILOGRAM,
        name="kilogram",
        abbreviation="kg",
        unit_delta_per_kilogram=1,
    ),
    _UnitInfo(
        unit=Unit.GRAM,
        name="gram",
        abbreviation="g",
        unit_delta_per_kilogram=1_000,
    ),
    _UnitInfo(
        unit=Unit.MILLIGRAM,
        name="milligram",
        abbreviation="mg",
        unit_delta_per_kilogram=1_000_000,
    ),
    _UnitInfo(
        unit=Unit.POUND,
        name="pound",
        abbreviation="lb",
        unit_delta_per_kilogram=2.20462262185,
    ),
    _UnitInfo(
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
