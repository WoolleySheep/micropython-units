"""Module for the voltage class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_volt,
)


class Voltage:
    """The difference in electric potential between two points."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new voltage."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the voltage, expressed as the unit."""
        internal_unit_delta_per_volt = get_unit_delta_per_volt(self._unit)
        value_as_volt = self._value / internal_unit_delta_per_volt
        external_unit_delta_per_volt = get_unit_delta_per_volt(unit)
        return external_unit_delta_per_volt * value_as_volt

    def __mul__(self, value: float) -> "Voltage":
        """Return a voltage scaled by the value."""
        scaled_value = self._value * value
        return Voltage(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "Voltage":
        """Return a voltage scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Voltage": ...

    @overload
    def __truediv__(self, other: "Voltage") -> float: ...

    def __truediv__(self, other: "float | Voltage") -> "Voltage | float":
        """Return a scaled voltage or the ratio between the voltages.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a voltage scaled by the
          inverse of the value
        - If the argument is a voltage, return the ratio between the two
          voltages
        """
        if isinstance(other, Voltage):
            value_as_volt = self.as_unit(Unit.VOLT)
            other_value_as_volt = other.as_unit(Unit.VOLT)
            return value_as_volt / other_value_as_volt

        scaled_value = self._value / other
        return Voltage(scaled_value, self._unit)

    def __add__(self, other: "Voltage") -> "Voltage":
        """Return the sum of the voltages."""
        value_as_volt = self.as_unit(Unit.VOLT)
        other_value_as_volt = other.as_unit(Unit.VOLT)
        added_value_as_volt = value_as_volt + other_value_as_volt
        return Voltage(added_value_as_volt, Unit.VOLT)

    def __sub__(self, delta: "Voltage") -> "Voltage":
        """Return the difference between the voltages."""
        return self + (-delta)

    def __neg__(self) -> "Voltage":
        """Return the inverse of the voltage."""
        inverted_value = -self._value
        return Voltage(inverted_value, self._unit)

    def __abs__(self) -> "Voltage":
        """Return the absolute version of the voltage."""
        absolute_value = abs(self._value)
        return Voltage(absolute_value, self._unit)

    def __floordiv__(self, other: "Voltage") -> float:
        """Return the floored ratio between the voltages."""
        value_as_volt = self.as_unit(Unit.VOLT)
        other_value_as_volt = other.as_unit(Unit.VOLT)
        return value_as_volt // other_value_as_volt

    def __mod__(self, other: "Voltage") -> float:
        """Return the remainder of the ratio between the voltages."""
        value_as_volt = self.as_unit(Unit.VOLT)
        other_value_as_volt = other.as_unit(Unit.VOLT)
        return value_as_volt % other_value_as_volt

    def __divmod__(self, other: "Voltage") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the voltages."""
        value_as_volt = self.as_unit(Unit.VOLT)
        other_value_as_volt = other.as_unit(Unit.VOLT)
        return divmod(value_as_volt, other_value_as_volt)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal voltages."""
        if not isinstance(other, Voltage):
            return NotImplemented

        return self.as_unit(Unit.VOLT) == other.as_unit(Unit.VOLT)

    def __lt__(self, other: "Voltage") -> bool:
        """Return whether the voltage is less than the other."""
        return self.as_unit(Unit.VOLT) < other.as_unit(Unit.VOLT)

    def __le__(self, other: "Voltage") -> bool:
        """Return whether the voltage is less than or equal to the other."""
        return self.as_unit(Unit.VOLT) <= other.as_unit(Unit.VOLT)

    def __gt__(self, other: "Voltage") -> bool:
        """Return whether the voltage is greater than the other."""
        return self.as_unit(Unit.VOLT) > other.as_unit(Unit.VOLT)

    def __ge__(self, other: "Voltage") -> bool:
        """Return whether the voltage is greater than or equal to the other."""
        return self.as_unit(Unit.VOLT) >= other.as_unit(Unit.VOLT)

    def __hash__(self) -> int:
        """Return the hash of the voltage.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.VOLT))

    def __str__(self) -> str:
        """Return a string representation of the voltage."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the voltage for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
