"""Module for the temperature class."""

from typing import Final, overload

from .exceptions import BelowAbsoluteZeroError
from .temperature_delta import TemperatureDelta
from .unit import (
    Unit,
    get_abbreviation,
    get_kelvin_to_unit_conversion_parameters,
    get_name,
)

ABSOLUTE_ZERO_AS_KELVIN: Final = 0


class Temperature:
    """Quantitatively expresses the attribute of hotness or coldness."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new temperature.

        Raises:
            BelowAbsoluteZeroError: The value and unit produced an invalid temperature
                less than absolute zero.
        """
        unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(unit)
        value_as_kelvin = (
            value - unit_conversion_parameters.absolute_zero_offset
        ) / unit_conversion_parameters.unit_delta_per_degree_kelvin
        if value_as_kelvin < ABSOLUTE_ZERO_AS_KELVIN:
            raise BelowAbsoluteZeroError(value=value, unit=unit)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the temperature, expressed as the unit."""
        internal_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            self._unit,
        )
        value_as_kelvin = (
            self._value - internal_unit_conversion_parameters.absolute_zero_offset
        ) / internal_unit_conversion_parameters.unit_delta_per_degree_kelvin

        external_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            unit,
        )
        return (
            external_unit_conversion_parameters.unit_delta_per_degree_kelvin
            * value_as_kelvin
            + external_unit_conversion_parameters.absolute_zero_offset
        )

    def __add__(self, delta: TemperatureDelta) -> "Temperature":
        """Return the sum of the temperature and the difference.

        Raises:
            BelowAbsoluteZeroError: The sum of the temperature and the difference was
                less than absolute zero.
        """
        value_as_kelvin = self.as_unit(Unit.KELVIN)
        delta_value_as_kelvin = delta.as_unit(Unit.KELVIN)
        value_sum_as_kelvin = value_as_kelvin + delta_value_as_kelvin
        return Temperature(value_sum_as_kelvin, Unit.KELVIN)

    def __radd__(self, delta: TemperatureDelta) -> "Temperature":
        """Return the sum of the temperature and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Temperature") -> TemperatureDelta: ...

    @overload
    def __sub__(self, other: TemperatureDelta) -> "Temperature": ...

    def __sub__(
        self,
        other: "Temperature | TemperatureDelta",
    ) -> "TemperatureDelta | Temperature":
        """Return the delta between temperatures or the temperature less the delta.

        The behaviour depends upon the type of the argument.

        - If the argument is a :py:class:`Temperature`, return the difference between
          the two temperatures.
        - If the argument is a :py:class:`TemperatureDelta`, return the temperature less
          the difference.

        Raises:
            BelowAbsoluteZeroError: The temperature minus the difference was less than
                absolute zero.Error can only be raised when other is a
                :py:class:`TemperatureDelta`.
        """
        value_as_kelvin = self.as_unit(Unit.KELVIN)
        other_value_as_kelvin = other.as_unit(Unit.KELVIN)
        value_difference_as_kelvin = value_as_kelvin - other_value_as_kelvin
        return (
            TemperatureDelta(value_difference_as_kelvin, Unit.KELVIN)
            if isinstance(other, Temperature)
            else Temperature(value_difference_as_kelvin, Unit.KELVIN)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal temperatures."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.as_unit(Unit.KELVIN) == other.as_unit(Unit.KELVIN)

    def __lt__(self, other: "Temperature") -> bool:
        """Return whether the temperature is less than the other."""
        return self.as_unit(Unit.KELVIN) < other.as_unit(Unit.KELVIN)

    def __le__(self, other: "Temperature") -> bool:
        """Return whether the temperature is less than or equal to the other."""
        return self.as_unit(Unit.KELVIN) <= other.as_unit(Unit.KELVIN)

    def __gt__(self, other: "Temperature") -> bool:
        """Return whether the temperature is greater than the other."""
        return self.as_unit(Unit.KELVIN) > other.as_unit(Unit.KELVIN)

    def __ge__(self, other: "Temperature") -> bool:
        """Return whether the temperature is greater than or equal to the other."""
        return self.as_unit(Unit.KELVIN) >= other.as_unit(Unit.KELVIN)

    def __hash__(self) -> int:
        """Return the hash of the temperature."""
        return hash(self.as_unit(Unit.KELVIN))

    def __str__(self) -> str:
        """Return a string representation of the temperature."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the temperature for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
