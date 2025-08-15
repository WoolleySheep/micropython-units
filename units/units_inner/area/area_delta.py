"""Module for the area difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_square_metre,
)


class AreaDelta:
    """The difference between two areas."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new area difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the area difference, expressed as the unit."""
        internal_unit_delta_per_square_metre = get_unit_delta_per_square_metre(
            self._unit
        )
        value_as_square_metre = self._value / internal_unit_delta_per_square_metre
        external_unit_delta_per_square_metre = get_unit_delta_per_square_metre(unit)
        return external_unit_delta_per_square_metre * value_as_square_metre

    def __mul__(self, value: float) -> "AreaDelta":
        """Return a area difference scaled by the value."""
        scaled_value = self._value * value
        return AreaDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "AreaDelta":
        """Return a area difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "AreaDelta": ...

    @overload
    def __truediv__(self, other: "AreaDelta") -> float: ...

    def __truediv__(self, other: "float | AreaDelta") -> "AreaDelta | float":
        """Return a scaled area difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a area difference scaled by the
          inverse of the value
        - If the argument is a area difference, return the ratio between the two
          differences
        """
        if isinstance(other, AreaDelta):
            value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
            other_value_as_square_metre = other.as_unit(Unit.SQUARE_METRE)
            return value_as_square_metre / other_value_as_square_metre

        scaled_value = self._value / other
        return AreaDelta(scaled_value, self._unit)

    def __add__(self, other: "AreaDelta") -> "AreaDelta":
        """Return the sum of the area differences."""
        # This NotImplemented block is here because the case of
        # a AreaDelta + a Area is handled in the __radd__ method in the
        # Area class, otherwise it runs into problems with circular imports
        if not isinstance(other, AreaDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
        delta_value_as_square_metre = other.as_unit(Unit.SQUARE_METRE)
        added_value_as_square_metre = (
            value_as_square_metre + delta_value_as_square_metre
        )
        return AreaDelta(added_value_as_square_metre, Unit.SQUARE_METRE)

    def __sub__(self, delta: "AreaDelta") -> "AreaDelta":
        """Return the difference between the area differences."""
        return self + (-delta)

    def __neg__(self) -> "AreaDelta":
        """Return the inverse of the area difference."""
        inverted_value = -self._value
        return AreaDelta(inverted_value, self._unit)

    def __abs__(self) -> "AreaDelta":
        """Return the absolute version of the area difference."""
        absolute_value = abs(self._value)
        return AreaDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "AreaDelta") -> float:
        """Return the floored ratio between the area differences."""
        value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
        other_value_as_square_metre = other.as_unit(Unit.SQUARE_METRE)
        return value_as_square_metre // other_value_as_square_metre

    def __mod__(self, other: "AreaDelta") -> float:
        """Return the remainder of the ratio between the area differences."""
        value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
        other_value_as_square_metre = other.as_unit(Unit.SQUARE_METRE)
        return value_as_square_metre % other_value_as_square_metre

    def __divmod__(self, other: "AreaDelta") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the area deltas."""
        value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
        other_value_as_square_metre = other.as_unit(Unit.SQUARE_METRE)
        return divmod(value_as_square_metre, other_value_as_square_metre)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal area differences."""
        if not isinstance(other, AreaDelta):
            return NotImplemented

        return self.as_unit(Unit.SQUARE_METRE) == other.as_unit(Unit.SQUARE_METRE)

    def __lt__(self, other: "AreaDelta") -> bool:
        """Return whether the area difference is less than the other."""
        return self.as_unit(Unit.SQUARE_METRE) < other.as_unit(Unit.SQUARE_METRE)

    def __le__(self, other: "AreaDelta") -> bool:
        """Return whether the area delta is less than or equal to the other."""
        return self.as_unit(Unit.SQUARE_METRE) <= other.as_unit(Unit.SQUARE_METRE)

    def __gt__(self, other: "AreaDelta") -> bool:
        """Return whether the area difference is greater than the other."""
        return self.as_unit(Unit.SQUARE_METRE) > other.as_unit(Unit.SQUARE_METRE)

    def __ge__(self, other: "AreaDelta") -> bool:
        """Return whether the area delta is greater than or equal to the other."""
        return self.as_unit(Unit.SQUARE_METRE) >= other.as_unit(Unit.SQUARE_METRE)

    def __hash__(self) -> int:
        """Return the hash of the area difference.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.SQUARE_METRE))

    def __str__(self) -> str:
        """Return a string representation of the area difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the area difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
