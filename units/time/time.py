"""Module for the time class."""

from typing import overload

from .exceptions import NegativeTimeValueError
from .time_delta import TimeDelta
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_second,
)


class Time:
    """The measure in which events can be ordered from the past into the future."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new time."""
        if value < 0:
            raise NegativeTimeValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the time, expressed as the unit."""
        internal_unit_delta_per_second = get_unit_delta_per_second(self._unit)
        value_as_second = self._value / internal_unit_delta_per_second
        external_unit_delta_per_second = get_unit_delta_per_second(unit)
        return external_unit_delta_per_second * value_as_second

    def __add__(self, delta: TimeDelta) -> "Time":
        """Return the sum of the time and the difference."""
        value_as_second = self.as_unit(Unit.SECOND)
        delta_value_as_second = delta.as_unit(Unit.SECOND)
        value_sum_as_second = value_as_second + delta_value_as_second
        return Time(value_sum_as_second, Unit.SECOND)

    def __radd__(self, delta: TimeDelta) -> "Time":
        """Return the sum of the time and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Time") -> TimeDelta: ...

    @overload
    def __sub__(self, other: TimeDelta) -> "Time": ...

    def __sub__(self, other: "Time | TimeDelta") -> "TimeDelta | Time":
        """Return the delta between times or the time less the delta.

        The behaviour depends upon the type of the argument.
        - If the argument is a time, return the difference between the two
          times.
        - If the argument is a time difference, return the time less the
          difference.
        """
        value_as_second = self.as_unit(Unit.SECOND)
        other_value_as_second = other.as_unit(Unit.SECOND)
        value_difference_as_second = value_as_second - other_value_as_second
        return (
            TimeDelta(value_difference_as_second, Unit.SECOND)
            if isinstance(other, Time)
            else Time(value_difference_as_second, Unit.SECOND)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal times."""
        return isinstance(other, Time) and self.as_unit(
            Unit.SECOND,
        ) == other.as_unit(Unit.SECOND)

    def __lt__(self, other: "Time") -> bool:
        """Return whether the time is less than the other."""
        return self.as_unit(Unit.SECOND) < other.as_unit(Unit.SECOND)

    def __le__(self, other: "Time") -> bool:
        """Return whether the time is less than or equal to the other."""
        return self.as_unit(Unit.SECOND) <= other.as_unit(Unit.SECOND)

    def __gt__(self, other: "Time") -> bool:
        """Return whether the time is greater than the other."""
        return self.as_unit(Unit.SECOND) > other.as_unit(Unit.SECOND)

    def __ge__(self, other: "Time") -> bool:
        """Return whether the time is greater than or equal to the other."""
        return self.as_unit(Unit.SECOND) >= other.as_unit(Unit.SECOND)

    def __hash__(self) -> int:
        """Return the hash of the time.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the time."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the time for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
