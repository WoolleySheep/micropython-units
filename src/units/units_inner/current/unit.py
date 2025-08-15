"""Module for the current units."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A current unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    AMPERE = 1
    MILLIAMPERE = 2
    MICROAMPERE = 3


class _UnitInfo:
    """Information associated with a current particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_ampere: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_ampere = unit_delta_per_ampere

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
    def unit_delta_per_ampere(self) -> float:
        """The change in current expressed as the unit per 1A.

        Equivalent to the gradient of the ampere-vs-unit graph.
        """
        return self._unit_delta_per_ampere


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.AMPERE,
        name="ampere",
        abbreviation="A",
        unit_delta_per_ampere=1,
    ),
    _UnitInfo(
        unit=Unit.MILLIAMPERE,
        name="milliampere",
        abbreviation="mA",
        unit_delta_per_ampere=1_000,
    ),
    _UnitInfo(
        unit=Unit.MICROAMPERE,
        name="microampere",
        abbreviation="uA",
        unit_delta_per_ampere=1_000_000,
    ),
]

# Convert into dictionary for quick lookup
_UNIT_TO_INFO_MAP: Final = {info.unit: info for info in _UNITS_INFO}


def get_name(unit: Unit) -> str:
    """Get the name of the current unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].name
    except KeyError as e:
        raise ValueError from e


def get_abbreviation(unit: Unit) -> str:
    """Get the abbreviation for the current unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_ampere(
    unit: Unit,
) -> float:
    """Get the change in current expressed as the unit per 1A.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_ampere
    except KeyError as e:
        raise ValueError from e
