"""Module for the time unit enum."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A time unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    SECOND = 1
    MINUTE = 2
    HOUR = 3
    MICROSECOND = 4
    MILLISECOND = 5


class _UnitInfo:
    """Information associated with a time particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_second: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_second = unit_delta_per_second

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
        """The change in time expressed as the unit per 1s.

        Equivalent to the gradient of the second-vs-unit graph.
        """
        return self._unit_delta_per_second


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.SECOND,
        name="second",
        abbreviation="s",
        unit_delta_per_second=1,
    ),
    _UnitInfo(
        unit=Unit.MINUTE,
        name="minute",
        abbreviation="min",
        unit_delta_per_second=1 / 60,
    ),
    _UnitInfo(
        unit=Unit.HOUR,
        name="hour",
        abbreviation="h",
        unit_delta_per_second=1 / (60 * 60),
    ),
    _UnitInfo(
        unit=Unit.MICROSECOND,
        name="microsecond",
        abbreviation="us",
        unit_delta_per_second=1e6,
    ),
    _UnitInfo(
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
        return _UNIT_TO_INFO_MAP[unit].abbreviation
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
