"""Module for the volume unit enum."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A volume unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    CUBIC_METRE = 1
    LITRE = 2
    MILLILITRE = 3
    MICROLITRE = 4


class _UnitInfo:
    """Information associated with a volume particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_cubic_metre: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_cubic_metre = unit_delta_per_cubic_metre

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
        """The change in volume expressed as the unit per 1m^3.

        Equivalent to the gradient of the cubic-metre-vs-unit graph.
        """
        return self._unit_delta_per_cubic_metre


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.CUBIC_METRE,
        name="cubic metre",
        abbreviation="m^3",
        unit_delta_per_cubic_metre=1,
    ),
    _UnitInfo(
        unit=Unit.LITRE,
        name="litre",
        abbreviation="L",
        unit_delta_per_cubic_metre=1e3,
    ),
    _UnitInfo(
        unit=Unit.MILLILITRE,
        name="millilitre",
        abbreviation="mL",
        unit_delta_per_cubic_metre=1e6,
    ),
    _UnitInfo(
        unit=Unit.MICROLITRE,
        name="microlitre",
        abbreviation="uL",
        unit_delta_per_cubic_metre=1e9,
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
        return _UNIT_TO_INFO_MAP[unit].abbreviation
    except KeyError as e:
        raise ValueError from e


def get_unit_delta_per_cubic_metre(
    unit: Unit,
) -> float:
    """Get the change in volume expressed as the unit per 1m^3.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].unit_delta_per_metre
    except KeyError as e:
        raise ValueError from e
