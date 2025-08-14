"""Module for the temperature difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_kelvin_to_unit_conversion_parameters,
    get_name,
)


class TemperatureDelta:
    """The difference between two temperatures."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new temperature difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the temperature difference, expressed as the unit."""
        internal_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            self._unit,
        )

        value_as_kelvin = (
            self._value
            / internal_unit_conversion_parameters.unit_delta_per_degree_kelvin
        )

        external_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            unit,
        )
        return (
            external_unit_conversion_parameters.unit_delta_per_degree_kelvin
            * value_as_kelvin
        )

    def __mul__(self, value: float) -> "TemperatureDelta":
        """Return a temperature difference scaled by the value."""
        scaled_value = self._value * value
        return TemperatureDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "TemperatureDelta":
        """Return a temperature difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "TemperatureDelta": ...

    @overload
    def __truediv__(self, other: "TemperatureDelta") -> float: ...

    def __truediv__(
        self,
        other: "float | TemperatureDelta",
    ) -> "TemperatureDelta | float":
        """Return a scaled temperature difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a temperature difference scaled by the
          inverse of the value
        - If the argument is a temperature difference, return the ratio between the two
          differences
        """
        if isinstance(other, TemperatureDelta):
            value_as_kelvin = self.as_unit(Unit.KELVIN)
            other_value_as_kelvin = other.as_unit(Unit.KELVIN)
            return value_as_kelvin / other_value_as_kelvin

        scaled_value = self._value / other
        return TemperatureDelta(scaled_value, self._unit)

    def __add__(self, other: "TemperatureDelta") -> "TemperatureDelta":
        """Return the sum of the temperature differences."""
        # This NotImplemented block is here because the case of
        # a TemperatureDelta + a Temperature is handled in the __radd__ method in the
        # Temperature class, otherwise it runs into problems with circular imports
        if not isinstance(other, TemperatureDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_kelvin = self.as_unit(Unit.KELVIN)
        delta_value_as_kelvin = other.as_unit(Unit.KELVIN)
        added_value_as_kelvin = value_as_kelvin + delta_value_as_kelvin
        return TemperatureDelta(added_value_as_kelvin, Unit.KELVIN)

    def __sub__(self, delta: "TemperatureDelta") -> "TemperatureDelta":
        """Return the difference between the temperature differences."""
        return self + (-delta)

    def __neg__(self) -> "TemperatureDelta":
        """Return the inverse of the temperature difference."""
        inverted_value = -self._value
        return TemperatureDelta(inverted_value, self._unit)

    def __abs__(self) -> "TemperatureDelta":
        """Return the absolute version of the temperature difference."""
        absolute_value = abs(self._value)
        return TemperatureDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "TemperatureDelta") -> float:
        """Return the floored ratio between the temperature differences."""
        value_as_kelvin = self.as_unit(Unit.KELVIN)
        other_value_as_kelvin = other.as_unit(Unit.KELVIN)
        return value_as_kelvin // other_value_as_kelvin

    def __mod__(self, other: "TemperatureDelta") -> float:
        """Return the remainder of the ratio between the temperature differences."""
        value_as_kelvin = self.as_unit(Unit.KELVIN)
        other_value_as_kelvin = other.as_unit(Unit.KELVIN)
        return value_as_kelvin % other_value_as_kelvin

    def __divmod__(self, other: "TemperatureDelta") -> tuple[float, float]:
        """Return the quotient and remainder of the ratio between the temp deltas."""
        value_as_kelvin = self.as_unit(Unit.KELVIN)
        other_value_as_kelvin = other.as_unit(Unit.KELVIN)
        return divmod(value_as_kelvin, other_value_as_kelvin)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal temperature differences."""
        if not isinstance(other, TemperatureDelta):
            return NotImplemented

        return self.as_unit(Unit.KELVIN) == other.as_unit(Unit.KELVIN)

    def __lt__(self, other: "TemperatureDelta") -> bool:
        """Return whether the temperature difference is less than the other."""
        return self.as_unit(Unit.KELVIN) < other.as_unit(Unit.KELVIN)

    def __le__(self, other: "TemperatureDelta") -> bool:
        """Return whether the temperature delta is less than or equal to the other."""
        return self.as_unit(Unit.KELVIN) <= other.as_unit(Unit.KELVIN)

    def __gt__(self, other: "TemperatureDelta") -> bool:
        """Return whether the temperature difference is greater than the other."""
        return self.as_unit(Unit.KELVIN) > other.as_unit(Unit.KELVIN)

    def __ge__(self, other: "TemperatureDelta") -> bool:
        """Return whether the temperature delta is greater than or equal to other."""
        return self.as_unit(Unit.KELVIN) >= other.as_unit(Unit.KELVIN)

    def __hash__(self) -> int:
        """Return the hash of the temperature difference.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.KELVIN))

    def __str__(self) -> str:
        """Return a string representation of the temperature difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the temperature difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
