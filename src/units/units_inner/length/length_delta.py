"""Module for the length difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_metre,
)


class LengthDelta:
    """The difference between two lengths."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new length difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the length difference, expressed as the unit."""
        internal_unit_delta_per_metre = get_unit_delta_per_metre(self._unit)
        value_as_metre = self._value / internal_unit_delta_per_metre
        external_unit_delta_per_metre = get_unit_delta_per_metre(unit)
        return external_unit_delta_per_metre * value_as_metre

    def __mul__(self, value: float) -> "LengthDelta":
        """Return a length difference scaled by the value."""
        scaled_value = self._value * value
        return LengthDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "LengthDelta":
        """Return a length difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "LengthDelta": ...

    @overload
    def __truediv__(self, other: "LengthDelta") -> float: ...

    def __truediv__(self, other: "float | LengthDelta") -> "LengthDelta | float":
        """Return a scaled length difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.

        - If the argument is :py:class:`float`, return a length difference scaled by the
          inverse of the value
        - If the argument is a :py:class:`LengthDelta`, return the ratio between the two
          differences
        """
        if isinstance(other, LengthDelta):
            value_as_metre = self.as_unit(Unit.METRE)
            other_value_as_metre = other.as_unit(Unit.METRE)
            return value_as_metre / other_value_as_metre

        scaled_value = self._value / other
        return LengthDelta(scaled_value, self._unit)

    def __add__(self, other: "LengthDelta") -> "LengthDelta":
        """Return the sum of the length differences."""
        # This NotImplemented block is here because the case of
        # a LengthDelta + a Length is handled in the __radd__ method in the
        # Length class, otherwise it runs into problems with circular imports
        if not isinstance(other, LengthDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_metre = self.as_unit(Unit.METRE)
        delta_value_as_metre = other.as_unit(Unit.METRE)
        added_value_as_metre = value_as_metre + delta_value_as_metre
        return LengthDelta(added_value_as_metre, Unit.METRE)

    def __sub__(self, delta: "LengthDelta") -> "LengthDelta":
        """Return the difference between the length differences."""
        return self + (-delta)

    def __neg__(self) -> "LengthDelta":
        """Return the inverse of the length difference."""
        inverted_value = -self._value
        return LengthDelta(inverted_value, self._unit)

    def __abs__(self) -> "LengthDelta":
        """Return the absolute version of the length difference."""
        absolute_value = abs(self._value)
        return LengthDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "LengthDelta") -> float:
        """Return the floored ratio between the length differences."""
        value_as_metre = self.as_unit(Unit.METRE)
        other_value_as_metre = other.as_unit(Unit.METRE)
        return value_as_metre // other_value_as_metre

    def __mod__(self, other: "LengthDelta") -> float:
        """Return the remainder of the ratio between the length differences."""
        value_as_metre = self.as_unit(Unit.METRE)
        other_value_as_metre = other.as_unit(Unit.METRE)
        return value_as_metre % other_value_as_metre

    def __divmod__(self, other: "LengthDelta") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the length deltas."""
        value_as_metre = self.as_unit(Unit.METRE)
        other_value_as_metre = other.as_unit(Unit.METRE)
        return divmod(value_as_metre, other_value_as_metre)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal length differences."""
        if not isinstance(other, LengthDelta):
            return NotImplemented

        return self.as_unit(Unit.METRE) == other.as_unit(Unit.METRE)

    def __lt__(self, other: "LengthDelta") -> bool:
        """Return whether the length difference is less than the other."""
        return self.as_unit(Unit.METRE) < other.as_unit(Unit.METRE)

    def __le__(self, other: "LengthDelta") -> bool:
        """Return whether the length difference is less than or equal to the other."""
        return self.as_unit(Unit.METRE) <= other.as_unit(Unit.METRE)

    def __gt__(self, other: "LengthDelta") -> bool:
        """Return whether the length difference is greater than the other."""
        return self.as_unit(Unit.METRE) > other.as_unit(Unit.METRE)

    def __ge__(self, other: "LengthDelta") -> bool:
        """Return whether the length delta is greater than or equal to the other."""
        return self.as_unit(Unit.METRE) >= other.as_unit(Unit.METRE)

    def __hash__(self) -> int:
        """Return the hash of the length difference."""
        return hash(self.as_unit(Unit.METRE))

    def __str__(self) -> str:
        """Return a string representation of the length difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the length difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
