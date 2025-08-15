"""Module for the time difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_second,
)


class TimeDelta:
    """The difference between two times."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new time difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the time difference, expressed as the unit."""
        internal_unit_delta_per_second = get_unit_delta_per_second(self._unit)
        value_as_second = self._value / internal_unit_delta_per_second
        external_unit_delta_per_second = get_unit_delta_per_second(unit)
        return external_unit_delta_per_second * value_as_second

    def __mul__(self, value: float) -> "TimeDelta":
        """Return a time difference scaled by the value."""
        scaled_value = self._value * value
        return TimeDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "TimeDelta":
        """Return a time difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "TimeDelta": ...

    @overload
    def __truediv__(self, other: "TimeDelta") -> float: ...

    def __truediv__(self, other: "float | TimeDelta") -> "TimeDelta | float":
        """Return a scaled time difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.

        - If the argument is :py:class:`float`, return a time difference scaled by the
          inverse of the value
        - If the argument is a :py:class:`TimeDelta`, return the ratio between the two
          differences
        """
        if isinstance(other, TimeDelta):
            value_as_second = self.as_unit(Unit.SECOND)
            other_value_as_second = other.as_unit(Unit.SECOND)
            return value_as_second / other_value_as_second

        scaled_value = self._value / other
        return TimeDelta(scaled_value, self._unit)

    def __add__(self, other: "TimeDelta") -> "TimeDelta":
        """Return the sum of the time differences."""
        # This NotImplemented block is here because the case of
        # a TimeDelta + a Time is handled in the __radd__ method in the
        # Time class, otherwise it runs into problems with circular imports
        if not isinstance(other, TimeDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_second = self.as_unit(Unit.SECOND)
        delta_value_as_second = other.as_unit(Unit.SECOND)
        added_value_as_second = value_as_second + delta_value_as_second
        return TimeDelta(added_value_as_second, Unit.SECOND)

    def __sub__(self, delta: "TimeDelta") -> "TimeDelta":
        """Return the difference between the time differences."""
        return self + (-delta)

    def __neg__(self) -> "TimeDelta":
        """Return the inverse of the time difference."""
        inverted_value = -self._value
        return TimeDelta(inverted_value, self._unit)

    def __abs__(self) -> "TimeDelta":
        """Return the absolute version of the time difference."""
        absolute_value = abs(self._value)
        return TimeDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "TimeDelta") -> float:
        """Return the floored ratio between the time differences."""
        value_as_second = self.as_unit(Unit.SECOND)
        other_value_as_second = other.as_unit(Unit.SECOND)
        return value_as_second // other_value_as_second

    def __mod__(self, other: "TimeDelta") -> float:
        """Return the remainder of the ratio between the time differences."""
        value_as_second = self.as_unit(Unit.SECOND)
        other_value_as_second = other.as_unit(Unit.SECOND)
        return value_as_second % other_value_as_second

    def __divmod__(self, other: "TimeDelta") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the time deltas."""
        value_as_second = self.as_unit(Unit.SECOND)
        other_value_as_second = other.as_unit(Unit.SECOND)
        return divmod(value_as_second, other_value_as_second)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal time differences."""
        if not isinstance(other, TimeDelta):
            return NotImplemented

        return self.as_unit(Unit.SECOND) == other.as_unit(Unit.SECOND)

    def __lt__(self, other: "TimeDelta") -> bool:
        """Return whether the time difference is less than the other."""
        return self.as_unit(Unit.SECOND) < other.as_unit(Unit.SECOND)

    def __le__(self, other: "TimeDelta") -> bool:
        """Return whether the time delta is less than or equal to the other."""
        return self.as_unit(Unit.SECOND) <= other.as_unit(Unit.SECOND)

    def __gt__(self, other: "TimeDelta") -> bool:
        """Return whether the time difference is greater than the other."""
        return self.as_unit(Unit.SECOND) > other.as_unit(Unit.SECOND)

    def __ge__(self, other: "TimeDelta") -> bool:
        """Return whether the time delta is greater than or equal to the other."""
        return self.as_unit(Unit.SECOND) >= other.as_unit(Unit.SECOND)

    def __hash__(self) -> int:
        """Return the hash of the time difference."""
        return hash(self.as_unit(Unit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the time difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the time difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
