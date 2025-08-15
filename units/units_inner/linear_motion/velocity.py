"""Module for the velocity class."""

# ruff: noqa: TID252

from typing import overload

from ..length import Unit as DistanceUnit
from ..length import get_unit_abbreviation as get_distance_unit_abbreviation
from ..length import (
    get_unit_delta_per_metre as get_distance_unit_delta_per_metre,
)
from ..length import get_unit_name as get_distance_unit_name
from ..time import Unit as TimeUnit
from ..time import get_unit_abbreviation as get_time_unit_abbreviation
from ..time import get_unit_delta_per_second as get_time_unit_delta_per_second
from ..time import get_unit_name as get_time_unit_name


class Velocity:
    """The rate of change of the displacement of an object wrt time."""

    def __init__(
        self, value: float, distance_unit: DistanceUnit, time_unit: TimeUnit
    ) -> None:
        """Initialise a new velocity."""
        self._value = value
        self._distance_unit = distance_unit
        self._time_unit = time_unit

    def as_unit(self, distance_unit: DistanceUnit, time_unit: TimeUnit) -> float:
        """Return the velocity in the specified units."""
        internal_distance_unit_delta_per_metre = get_distance_unit_delta_per_metre(
            self._distance_unit
        )
        internal_time_unit_delta_per_second = get_time_unit_delta_per_second(
            self._time_unit
        )
        internal_unit_to_metre_per_second_factor = (
            internal_time_unit_delta_per_second / internal_distance_unit_delta_per_metre
        )
        value_as_metre_per_second = (
            internal_unit_to_metre_per_second_factor * self._value
        )
        external_distance_unit_delta_per_metre = get_distance_unit_delta_per_metre(
            distance_unit
        )
        external_time_unit_delta_per_second = get_time_unit_delta_per_second(time_unit)
        metre_per_second_to_external_unit_factor = (
            external_distance_unit_delta_per_metre / external_time_unit_delta_per_second
        )
        return metre_per_second_to_external_unit_factor * value_as_metre_per_second

    def __mul__(self, value: float) -> "Velocity":
        """Return a velocity scaled by the value."""
        scaled_value = self._value * value
        return Velocity(scaled_value, self._distance_unit, self._time_unit)

    def __rmul__(self, value: float) -> "Velocity":
        """Return a velocity scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Velocity": ...

    @overload
    def __truediv__(self, other: "Velocity") -> float: ...

    def __truediv__(self, other: "float | Velocity") -> "Velocity | float":
        """Return a scaled velocity or the ratio between the velocities.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a velocity scaled by the
          inverse of the value
        - If the argument is a velocity, return the ratio between the two
          velocities
        """
        if isinstance(other, Velocity):
            value_as_metre_per_second = self.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND
            )
            other_value_as_metre_per_second = other.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND
            )
            return value_as_metre_per_second / other_value_as_metre_per_second

        return (1 / other) * self

    def __add__(self, other: "Velocity") -> "Velocity":
        """Return the sum of two velocities."""
        value_as_metre_per_second = self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        other_value_as_metre_per_second = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        value_sum_as_metre_per_second = (
            value_as_metre_per_second + other_value_as_metre_per_second
        )
        return Velocity(
            value_sum_as_metre_per_second, DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __sub__(self, other: "Velocity") -> "Velocity":
        """Return the difference of two velocities."""
        value_as_metre_per_second = self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        other_value_as_metre_per_second = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        value_difference_as_metre_per_second = (
            value_as_metre_per_second - other_value_as_metre_per_second
        )
        return Velocity(
            value_difference_as_metre_per_second,
            DistanceUnit.METRE,
            TimeUnit.SECOND,
        )

    def __neg__(self) -> "Velocity":
        """Return the inverse of the velocity."""
        return -1 * self

    def __abs__(self) -> "Velocity":
        """Return the absolute version of the velocity."""
        absolute_value = abs(self._value)
        return Velocity(absolute_value, self._distance_unit, self._time_unit)

    def __floordiv__(self, other: "Velocity") -> float:
        """Return the floored ratio between the velocities."""
        value_as_metre_per_second = self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        other_value_as_metre_per_second = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        return value_as_metre_per_second // other_value_as_metre_per_second

    def __mod__(self, other: "Velocity") -> float:
        """Return the remainder of the ratio between the velocity."""
        value_as_metre_per_second = self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        other_value_as_metre_per_second = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        return value_as_metre_per_second % other_value_as_metre_per_second

    def __divmod__(self, other: "Velocity") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the velocities."""
        value_as_metre_per_second = self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        other_value_as_metre_per_second = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        return divmod(value_as_metre_per_second, other_value_as_metre_per_second)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal velocities."""
        if not isinstance(other, Velocity):
            return NotImplemented

        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) == other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __lt__(self, other: "Velocity") -> bool:
        """Return whether the velocity is less than the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) < other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __le__(self, other: "Velocity") -> bool:
        """Return whether the velocity is less than or equal to the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) <= other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __gt__(self, other: "Velocity") -> bool:
        """Return whether the velocity is greater than the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) > other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __ge__(self, other: "Velocity") -> bool:
        """Return whether the velocity is greater than or equal to the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) >= other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __hash__(self) -> int:
        """Return the hash of the velocity.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the velocity."""
        return (
            f"{self._value} "
            f"{get_distance_unit_abbreviation(self._distance_unit)}/"
            f"{get_time_unit_abbreviation(self._time_unit)}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the velocity for developers."""
        return (
            f"{__class__.__name__}({self._value},"
            f" {get_distance_unit_name(self._distance_unit)},"
            f" {get_time_unit_name(self._time_unit)})"
        )
