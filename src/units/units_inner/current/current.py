"""Module for the current class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_ampere,
)


class Current:
    """The flow of charged particles through an electrical conductor."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new current."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the current, expressed as the unit."""
        internal_unit_delta_per_ampere = get_unit_delta_per_ampere(self._unit)
        value_as_ampere = self._value / internal_unit_delta_per_ampere
        external_unit_delta_per_ampere = get_unit_delta_per_ampere(unit)
        return external_unit_delta_per_ampere * value_as_ampere

    def __mul__(self, value: float) -> "Current":
        """Return a current scaled by the value."""
        scaled_value = self._value * value
        return Current(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "Current":
        """Return a current scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Current": ...

    @overload
    def __truediv__(self, other: "Current") -> float: ...

    def __truediv__(self, other: "float | Current") -> "Current | float":
        """Return a scaled current or the ratio between the currents.

        The behaviour depends upon the type of the argument.

        - If the argument is :py:class:`float`, return a current scaled by the
          inverse of the value
        - If the argument is a :py:class:`Current`, return the ratio between the two
          currents
        """
        if isinstance(other, Current):
            value_as_ampere = self.as_unit(Unit.AMPERE)
            other_value_as_ampere = other.as_unit(Unit.AMPERE)
            return value_as_ampere / other_value_as_ampere

        scaled_value = self._value / other
        return Current(scaled_value, self._unit)

    def __add__(self, other: "Current") -> "Current":
        """Return the sum of the currents."""
        value_as_ampere = self.as_unit(Unit.AMPERE)
        other_value_as_ampere = other.as_unit(Unit.AMPERE)
        added_value_as_ampere = value_as_ampere + other_value_as_ampere
        return Current(added_value_as_ampere, Unit.AMPERE)

    def __sub__(self, delta: "Current") -> "Current":
        """Return the difference between the currents."""
        return self + (-delta)

    def __neg__(self) -> "Current":
        """Return the inverse of the current."""
        inverted_value = -self._value
        return Current(inverted_value, self._unit)

    def __abs__(self) -> "Current":
        """Return the absolute version of the current."""
        absolute_value = abs(self._value)
        return Current(absolute_value, self._unit)

    def __floordiv__(self, other: "Current") -> float:
        """Return the floored ratio between the currents."""
        value_as_ampere = self.as_unit(Unit.AMPERE)
        other_value_as_ampere = other.as_unit(Unit.AMPERE)
        return value_as_ampere // other_value_as_ampere

    def __mod__(self, other: "Current") -> float:
        """Return the remainder of the ratio between the currents."""
        value_as_ampere = self.as_unit(Unit.AMPERE)
        other_value_as_ampere = other.as_unit(Unit.AMPERE)
        return value_as_ampere % other_value_as_ampere

    def __divmod__(self, other: "Current") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the currents."""
        value_as_ampere = self.as_unit(Unit.AMPERE)
        other_value_as_ampere = other.as_unit(Unit.AMPERE)
        return divmod(value_as_ampere, other_value_as_ampere)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal currents."""
        if not isinstance(other, Current):
            return NotImplemented

        return self.as_unit(Unit.AMPERE) == other.as_unit(Unit.AMPERE)

    def __lt__(self, other: "Current") -> bool:
        """Return whether the current is less than the other."""
        return self.as_unit(Unit.AMPERE) < other.as_unit(Unit.AMPERE)

    def __le__(self, other: "Current") -> bool:
        """Return whether the current is less than or equal to the other."""
        return self.as_unit(Unit.AMPERE) <= other.as_unit(Unit.AMPERE)

    def __gt__(self, other: "Current") -> bool:
        """Return whether the current is greater than the other."""
        return self.as_unit(Unit.AMPERE) > other.as_unit(Unit.AMPERE)

    def __ge__(self, other: "Current") -> bool:
        """Return whether the current is greater than or equal to the other."""
        return self.as_unit(Unit.AMPERE) >= other.as_unit(Unit.AMPERE)

    def __hash__(self) -> int:
        """Return the hash of the current."""
        return hash(self.as_unit(Unit.AMPERE))

    def __str__(self) -> str:
        """Return a string representation of the current."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the current for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
