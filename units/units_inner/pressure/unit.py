"""Module for the pressure units."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object

STANDARD_ATMOSPHERIC_PRESSURE_AS_PASCAL: Final = 101_325


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A pressure unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    PASCAL = 1
    POUND_PER_SQUARE_INCH = 2
    BAR = 3
    ATMOSPHERE = 4
    MILLIMETRE_OF_MERCURY = 5
    KILOPASCAL = 6
    MILLIBAR = 7


class _UnitInfo:
    """Information associated with a pressure particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_pascal: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_pascal = unit_delta_per_pascal

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
    def unit_delta_per_pascal(self) -> float:
        """The change in pressure expressed as the unit per 1Pa.

        Equivalent to the gradient of the pascal-vs-unit graph.
        """
        return self._unit_delta_per_pascal


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.PASCAL,
        name="pascal",
        abbreviation="Pa",
        unit_delta_per_pascal=1,
    ),
    _UnitInfo(
        unit=Unit.POUND_PER_SQUARE_INCH,
        name="pound-per-square-inch",
        abbreviation="PSI",
        unit_delta_per_pascal=0.00014503773773,
    ),
    _UnitInfo(
        unit=Unit.BAR,
        name="bar",
        abbreviation="bar",
        unit_delta_per_pascal=1 / 100_000,
    ),
    _UnitInfo(
        unit=Unit.ATMOSPHERE,
        name="atmosphere",
        abbreviation="atm",
        unit_delta_per_pascal=1 / STANDARD_ATMOSPHERIC_PRESSURE_AS_PASCAL,
    ),
    _UnitInfo(
        unit=Unit.MILLIMETRE_OF_MERCURY,
        name="millimetre-of-mercury",
        abbreviation="mmHg",
        unit_delta_per_pascal=1 / 133.322387415,
    ),
    _UnitInfo(
        unit=Unit.KILOPASCAL,
        name="kilopascal",
        abbreviation="kPa",
        unit_delta_per_pascal=1 / 1_000,
    ),
    _UnitInfo(
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
        return _UNIT_TO_INFO_MAP[unit].abbreviation
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
