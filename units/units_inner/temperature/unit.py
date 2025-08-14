"""Module for the temperature unit enum."""

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A temperature unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    CELSIUS = 1
    KELVIN = 2
    FAHRENHEIT = 3


class _UnitConversionParameters:
    """Parameters required to convert a value from kelvin to a unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit_delta_per_degree_kelvin: float,
        absolute_zero_offset: float,
    ) -> None:
        """Initialise a new pair of conversion parameters."""
        self._unit_delta_per_degree_kelvin = unit_delta_per_degree_kelvin
        self._absolute_zero_offset = absolute_zero_offset

    @property
    def unit_delta_per_degree_kelvin(self) -> float:
        """The change in temperature expressed as the unit per 1 degree K.

        Equivalent to the gradient of the kelvin-vs-unit graph.
        """
        return self._unit_delta_per_degree_kelvin

    @property
    def absolute_zero_offset(self) -> float:
        """The temperature expressed as the unit at absolute zero.

        Equivalent to the y-intercept of the kelvin-vs-unit graph.
        """
        return self._absolute_zero_offset


class _UnitInfo:
    """Information associated with a particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        conversion_parameters: _UnitConversionParameters,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._conversion_parameters = conversion_parameters

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
    def conversion_parameters(self) -> _UnitConversionParameters:
        """The conversion parameters associated with the unit."""
        return self._conversion_parameters


# All info is entered here to create a SSoT
_UNITS_INFO: Final = [
    _UnitInfo(
        unit=Unit.KELVIN,
        name="kelvin",
        abbreviation="K",
        conversion_parameters=_UnitConversionParameters(1, 0),
    ),
    _UnitInfo(
        unit=Unit.CELSIUS,
        name="celsius",
        abbreviation="C",
        conversion_parameters=_UnitConversionParameters(1, -273.15),
    ),
    _UnitInfo(
        unit=Unit.FAHRENHEIT,
        name="fahrenheit",
        abbreviation="F",
        conversion_parameters=_UnitConversionParameters(9 / 5, -459.67),
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
) -> _UnitConversionParameters:
    """Get the parameters to convert a value from kelvin to the temperature unit.

    Not intended for public use.
    """
    try:
        return _UNIT_TO_INFO_MAP[unit].conversion_parameters
    except KeyError as e:
        raise ValueError from e
