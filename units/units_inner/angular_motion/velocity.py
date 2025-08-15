"""Module for the angular velocity class."""

# ruff: noqa: TID252

from typing import overload

from ..angle import Unit as AngleUnit
from ..angle import get_unit_abbreviation as get_angle_unit_abbreviation
from ..angle import (
    get_unit_delta_per_radian as get_angle_unit_delta_per_radian,
)
from ..angle import get_unit_name as get_angle_unit_name
from ..time import Unit as TimeUnit
from ..time import get_unit_abbreviation as get_time_unit_abbreviation
from ..time import get_unit_delta_per_second as get_time_unit_delta_per_second
from ..time import get_unit_name as get_time_unit_name


class Velocity:
    """The speed in a certain direction of angular motion."""

    def __init__(
        self, value: float, angle_unit: AngleUnit, time_unit: TimeUnit
    ) -> None:
        """Initialise a new angular velocity."""
        self._value = value
        self._angle_unit = angle_unit
        self._time_unit = time_unit

    def as_unit(self, angle_unit: AngleUnit, time_unit: TimeUnit) -> float:
        """Return the angular velocity in the specified units."""
        internal_angle_unit_delta_per_radian = get_angle_unit_delta_per_radian(
            self._angle_unit
        )
        internal_time_unit_delta_per_second = get_time_unit_delta_per_second(
            self._time_unit
        )
        internal_unit_to_radian_per_second_factor = (
            internal_time_unit_delta_per_second / internal_angle_unit_delta_per_radian
        )
        value_as_radian_per_second = (
            internal_unit_to_radian_per_second_factor * self._value
        )
        external_angle_unit_delta_per_radian = get_angle_unit_delta_per_radian(
            angle_unit
        )
        external_time_unit_delta_per_second = get_time_unit_delta_per_second(time_unit)
        radian_per_second_to_external_unit_factor = (
            external_angle_unit_delta_per_radian / external_time_unit_delta_per_second
        )
        return radian_per_second_to_external_unit_factor * value_as_radian_per_second

    def __mul__(self, value: float) -> "Velocity":
        """Return a angular velocity scaled by the value."""
        scaled_value = self._value * value
        return Velocity(scaled_value, self._angle_unit, self._time_unit)

    def __rmul__(self, value: float) -> "Velocity":
        """Return a angular velocity scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Velocity": ...

    @overload
    def __truediv__(self, other: "Velocity") -> float: ...

    def __truediv__(self, other: "float | Velocity") -> "Velocity | float":
        """Return a scaled angular velocity or the ratio between the angular velocities.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a angular velocity scaled by the
          inverse of the value
        - If the argument is a angular velocity, return the ratio between the two
          angular velocities
        """
        if isinstance(other, Velocity):
            value_as_radian_per_second = self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
            other_value_as_radian_per_second = other.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND
            )
            return value_as_radian_per_second / other_value_as_radian_per_second

        return (1 / other) * self

    def __add__(self, other: "Velocity") -> "Velocity":
        """Return the sum of two angular velocities."""
        value_as_radian_per_second = self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        other_value_as_radian_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        value_sum_as_radian_per_second = (
            value_as_radian_per_second + other_value_as_radian_per_second
        )
        return Velocity(
            value_sum_as_radian_per_second, AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __sub__(self, other: "Velocity") -> "Velocity":
        """Return the difference of two angular velocities."""
        value_as_radian_per_second = self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        other_value_as_radian_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        value_difference_as_radian_per_second = (
            value_as_radian_per_second - other_value_as_radian_per_second
        )
        return Velocity(
            value_difference_as_radian_per_second,
            AngleUnit.RADIAN,
            TimeUnit.SECOND,
        )

    def __neg__(self) -> "Velocity":
        """Return the inverse of the angular velocity."""
        return -1 * self

    def __abs__(self) -> "Velocity":
        """Return the absolute version of the angular velocity."""
        absolute_value = abs(self._value)
        return Velocity(absolute_value, self._angle_unit, self._time_unit)

    def __floordiv__(self, other: "Velocity") -> float:
        """Return the floored ratio between the angular velocities."""
        value_as_radian_per_second = self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        other_value_as_radian_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return value_as_radian_per_second // other_value_as_radian_per_second

    def __mod__(self, other: "Velocity") -> float:
        """Return the remainder of the ratio between the angular velocity."""
        value_as_radian_per_second = self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        other_value_as_radian_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return value_as_radian_per_second % other_value_as_radian_per_second

    def __divmod__(self, other: "Velocity") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the velocities."""
        value_as_radian_per_second = self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        other_value_as_radian_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return divmod(value_as_radian_per_second, other_value_as_radian_per_second)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal angular velocities."""
        if not isinstance(other, Velocity):
            return NotImplemented

        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) == other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __lt__(self, other: "Velocity") -> bool:
        """Return whether the angular velocity is less than the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) < other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __le__(self, other: "Velocity") -> bool:
        """Return whether the angular velocity is less than or equal to the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) <= other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __gt__(self, other: "Velocity") -> bool:
        """Return whether the angular velocity is greater than the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) > other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __ge__(self, other: "Velocity") -> bool:
        """Return whether the angular velocity is greater than or equal to the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) >= other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __hash__(self) -> int:
        """Return the hash of the angular velocity.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the angular velocity."""
        return (
            f"{self._value} "
            f"{get_angle_unit_abbreviation(self._angle_unit)}/"
            f"{get_time_unit_abbreviation(self._time_unit)}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the angular velocity for developers."""
        return (
            f"{__class__.__name__}({self._value},"
            f" {get_angle_unit_name(self._angle_unit)},"
            f" {get_time_unit_name(self._time_unit)})"
        )
