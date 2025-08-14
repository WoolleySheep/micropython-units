"""Module for the pressure units."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A distance unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    METRE = 1
    CENTIMETRE = 2
    MILLIMETRE = 3
    YARD = 4
    FOOT = 5
    INCH = 6


class _UnitInfo:
    """Information associated with a particular distance unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_metre: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_metre = unit_delta_per_metre

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
    def unit_delta_per_metre(self) -> float:
        """The change in distance expressed as the unit per 1m.

        Equivalent to the gradient of the metre-vs-unit graph.
        """
        return self._unit_delta_per_metre


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.METRE,
        name="metre",
        abbreviation="m",
        unit_delta_per_metre=1,
    ),
    _UnitInfo(
        unit=Unit.CENTIMETRE,
        name="centimetre",
        abbreviation="cm",
        unit_delta_per_metre=100,
    ),
    _UnitInfo(
        unit=Unit.MILLIMETRE,
        name="millimetre",
        abbreviation="mm",
        unit_delta_per_metre=1_000,
    ),
    _UnitInfo(
        unit=Unit.YARD,
        name="yard",
        abbreviation="yd",
        unit_delta_per_metre=1.09361329834,
    ),
    _UnitInfo(
        unit=Unit.FOOT,
        name="foot",
        abbreviation="ft",
        unit_delta_per_metre=3.28083989501,
    ),
    _UnitInfo(
        unit=Unit.INCH,
        name="inch",
        abbreviation="in",
        unit_delta_per_metre=39.3700787402,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the distance unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the distance unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_metre(
    unit: Unit,
) -> float:
    """Get the change in distance expressed as the unit per 1Pa.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_metre
    except KeyError as e:
        raise ValueError from e
