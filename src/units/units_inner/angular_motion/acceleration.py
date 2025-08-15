"""Module for the angular acceleration class."""

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
from ..time import (
    get_unit_delta_per_second as get_time_unit_delta_per_second,
)
from ..time import get_unit_name as get_time_unit_name


class Acceleration:
    """The rate of change of the angular velocity of an object wrt time."""

    def __init__(
        self,
        value: float,
        angle_unit: AngleUnit,
        first_time_unit: TimeUnit,
        second_time_unit: TimeUnit | None = None,
    ) -> None:
        """Initialise a new angular acceleration.

        If a second time unit is not provided, the first time unit will be reused.
        """
        self._value = value
        self._angle_unit = angle_unit
        self._first_time_unit = first_time_unit
        self._second_time_unit = (
            second_time_unit if second_time_unit is not None else first_time_unit
        )

    def as_unit(
        self,
        angle_unit: AngleUnit,
        first_time_unit: TimeUnit,
        second_time_unit: TimeUnit | None = None,
    ) -> float:
        """Return the angular acceleration in the specified units.

        If a second time unit is not provided, the first time unit will be reused.
        """
        internal_angle_unit_delta_per_radian = get_angle_unit_delta_per_radian(
            self._angle_unit
        )
        internal_first_time_unit_delta_per_second = get_time_unit_delta_per_second(
            self._first_time_unit
        )
        internal_second_time_unit_delta_per_second = get_time_unit_delta_per_second(
            self._second_time_unit
        )
        internal_unit_to_radian_per_second_per_second_factor = (
            internal_second_time_unit_delta_per_second
            * internal_first_time_unit_delta_per_second
            / internal_angle_unit_delta_per_radian
        )
        value_as_radian_per_second_per_second = (
            internal_unit_to_radian_per_second_per_second_factor * self._value
        )
        external_angle_unit_delta_per_radian = get_angle_unit_delta_per_radian(
            angle_unit
        )
        external_first_time_unit_delta_per_second = get_time_unit_delta_per_second(
            first_time_unit
        )
        external_second_time_unit_delta_per_second = (
            get_time_unit_delta_per_second(second_time_unit)
            if second_time_unit is not None
            else external_first_time_unit_delta_per_second
        )
        radian_per_second_per_second_to_external_unit_factor = (
            external_angle_unit_delta_per_radian
            / (
                external_first_time_unit_delta_per_second
                * external_second_time_unit_delta_per_second
            )
        )
        return (
            radian_per_second_per_second_to_external_unit_factor
            * value_as_radian_per_second_per_second
        )

    def __mul__(self, value: float) -> "Acceleration":
        """Return an angular acceleration scaled by the value."""
        scaled_value = self._value * value
        return Acceleration(
            scaled_value,
            self._angle_unit,
            self._first_time_unit,
            self._second_time_unit,
        )

    def __rmul__(self, value: float) -> "Acceleration":
        """Return an angular acceleration scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Acceleration": ...

    @overload
    def __truediv__(self, other: "Acceleration") -> float: ...

    def __truediv__(self, other: "float | Acceleration") -> "Acceleration | float":
        """Return a scaled angular acceleration or the ratio between the accelerations.

        The behaviour depends upon the type of the argument.

        - If the argument is a :py:class:`float`, return an angular acceleration scaled
          by the inverse of the value
        - If the argument is a :py:class:`Acceleration`, return the ratio between the
          two angular accelerations
        """
        if isinstance(other, Acceleration):
            value_as_radian_per_second_per_second = self.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND
            )
            other_value_as_radian_per_second_per_second = other.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND
            )
            return (
                value_as_radian_per_second_per_second
                / other_value_as_radian_per_second_per_second
            )

        return (1 / other) * self

    def __add__(self, other: "Acceleration") -> "Acceleration":
        """Return the sum of two angular accelerations."""
        value_as_radian_per_second_per_second = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        value_sum_as_radian_per_second_per_second = (
            value_as_radian_per_second_per_second
            + other_value_as_radian_per_second_per_second
        )
        return Acceleration(
            value_sum_as_radian_per_second_per_second,
            AngleUnit.RADIAN,
            TimeUnit.SECOND,
        )

    def __sub__(self, other: "Acceleration") -> "Acceleration":
        """Return the difference of two angular accelerations."""
        value_as_radian_per_second_per_second = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        value_difference_as_radian_per_second_per_second = (
            value_as_radian_per_second_per_second
            - other_value_as_radian_per_second_per_second
        )
        return Acceleration(
            value_difference_as_radian_per_second_per_second,
            AngleUnit.RADIAN,
            TimeUnit.SECOND,
        )

    def __neg__(self) -> "Acceleration":
        """Return the inverse of the angular acceleration."""
        return -1 * self

    def __abs__(self) -> "Acceleration":
        """Return the absolute version of the angular acceleration."""
        absolute_value = abs(self._value)
        return Acceleration(
            absolute_value,
            self._angle_unit,
            self._first_time_unit,
            self._second_time_unit,
        )

    def __floordiv__(self, other: "Acceleration") -> float:
        """Return the floored ratio between the angular accelerations."""
        value_as_radian_per_second_per_second = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return (
            value_as_radian_per_second_per_second
            // other_value_as_radian_per_second_per_second
        )

    def __mod__(self, other: "Acceleration") -> float:
        """Return the remainder of the ratio between the angular acceleration."""
        value_as_radian_per_second_per_second = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return (
            value_as_radian_per_second_per_second
            % other_value_as_radian_per_second_per_second
        )

    def __divmod__(self, other: "Acceleration") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio tbwn angular accelerations."""
        value_as_radian_per_second_per_second = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_per_second = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return divmod(
            value_as_radian_per_second_per_second,
            other_value_as_radian_per_second_per_second,
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal angular accelerations."""
        if not isinstance(other, Acceleration):
            return NotImplemented

        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) == other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __lt__(self, other: "Acceleration") -> bool:
        """Return whether the angular acceleration is less than the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) < other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __le__(self, other: "Acceleration") -> bool:
        """Return whether the angular acceleration is less than or equal to other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) <= other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __gt__(self, other: "Acceleration") -> bool:
        """Return whether the angular acceleration is greater than the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) > other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __ge__(self, other: "Acceleration") -> bool:
        """Return whether the angular acceleration is greater than or equal to other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) >= other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __hash__(self) -> int:
        """Return the hash of the angular acceleration."""
        return hash(self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the angular acceleration."""
        return (
            f"{self._value} "
            f"{get_angle_unit_abbreviation(self._angle_unit)}/"
            f"{get_time_unit_abbreviation(self._first_time_unit)}/"
            f"{get_time_unit_abbreviation(self._second_time_unit)}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the angular acceleration for developers."""
        return (
            f"{__class__.__name__}({self._value},"
            f" {get_angle_unit_name(self._angle_unit)},"
            f" {get_time_unit_name(self._first_time_unit)}),"
            f" {get_time_unit_name(self._second_time_unit)})"
        )
