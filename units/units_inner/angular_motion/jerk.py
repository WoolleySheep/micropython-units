"""Module for the angular jerk class."""

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


class Jerk:
    """The rate of change of the angular jerk of an object with respect to time."""

    def __init__(  # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        value: float,
        angle_unit: AngleUnit,
        first_time_unit: TimeUnit,
        second_time_unit: TimeUnit | None = None,
        third_time_unit: TimeUnit | None = None,
    ) -> None:
        """Initialise a new angular jerk.

        If a second time unit is not provided, the first time unit will be reused.
        If the third time unit is not provided, the second time unit will be reused
        (or the first, if the second is also not provided).
        """
        self._value = value
        self._angle_unit = angle_unit
        self._first_time_unit = first_time_unit
        self._second_time_unit = (
            second_time_unit if second_time_unit is not None else first_time_unit
        )
        self._third_time_unit = (
            third_time_unit if third_time_unit is not None else self._second_time_unit
        )

    def as_unit(  # pylint: disable=too-many-locals
        self,
        angle_unit: AngleUnit,
        first_time_unit: TimeUnit,
        second_time_unit: TimeUnit | None = None,
        third_time_unit: TimeUnit | None = None,
    ) -> float:
        """Return the angular jerk in the specified units.

        If a second time unit is not provided, the first time unit will be reused.
        If the third time unit is not provided, the second time unit will be reused
        (or the first, if the second is also not provided).
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
        internal_third_time_unit_delta_per_second = get_time_unit_delta_per_second(
            self._third_time_unit
        )
        internal_unit_to_radian_per_second_cubed_factor = (
            internal_third_time_unit_delta_per_second
            * internal_second_time_unit_delta_per_second
            * internal_first_time_unit_delta_per_second
            / internal_angle_unit_delta_per_radian
        )
        value_as_radian_per_second_cubed = (
            internal_unit_to_radian_per_second_cubed_factor * self._value
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
        external_third_time_unit_delta_per_second = (
            get_time_unit_delta_per_second(third_time_unit)
            if third_time_unit is not None
            else external_second_time_unit_delta_per_second
        )
        radian_per_second_cubed_to_external_unit_factor = (
            external_angle_unit_delta_per_radian
            / (
                external_first_time_unit_delta_per_second
                * external_second_time_unit_delta_per_second
                * external_third_time_unit_delta_per_second
            )
        )
        return (
            radian_per_second_cubed_to_external_unit_factor
            * value_as_radian_per_second_cubed
        )

    def __mul__(self, value: float) -> "Jerk":
        """Return an angular jerk scaled by the value."""
        scaled_value = self._value * value
        return Jerk(
            scaled_value,
            self._angle_unit,
            self._first_time_unit,
            self._second_time_unit,
            self._third_time_unit,
        )

    def __rmul__(self, value: float) -> "Jerk":
        """Return an angular jerk scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Jerk": ...

    @overload
    def __truediv__(self, other: "Jerk") -> float: ...

    def __truediv__(self, other: "float | Jerk") -> "Jerk | float":
        """Return a scaled angular jerk or the ratio between the angular jerks.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return an angular jerk scaled by the
          inverse of the value
        - If the argument is an angular jerk, return the ratio between the two
          angular jerks
        """
        if isinstance(other, Jerk):
            value_as_radian_per_second_cubed = self.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND
            )
            other_value_as_radian_per_second_cubed = other.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND
            )
            return (
                value_as_radian_per_second_cubed
                / other_value_as_radian_per_second_cubed
            )

        return (1 / other) * self

    def __add__(self, other: "Jerk") -> "Jerk":
        """Return the sum of two angular jerks."""
        value_as_radian_per_second_cubed = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_cubed = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        value_sum_as_radian_per_second_cubed = (
            value_as_radian_per_second_cubed + other_value_as_radian_per_second_cubed
        )
        return Jerk(
            value_sum_as_radian_per_second_cubed,
            AngleUnit.RADIAN,
            TimeUnit.SECOND,
        )

    def __sub__(self, other: "Jerk") -> "Jerk":
        """Return the difference of two angular jerks."""
        value_as_radian_per_second_cubed = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_cubed = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        value_difference_as_radian_per_second_cubed = (
            value_as_radian_per_second_cubed - other_value_as_radian_per_second_cubed
        )
        return Jerk(
            value_difference_as_radian_per_second_cubed,
            AngleUnit.RADIAN,
            TimeUnit.SECOND,
        )

    def __neg__(self) -> "Jerk":
        """Return the inverse of the angular jerk."""
        return -1 * self

    def __abs__(self) -> "Jerk":
        """Return the absolute version of the angular jerk."""
        absolute_value = abs(self._value)
        return Jerk(
            absolute_value,
            self._angle_unit,
            self._first_time_unit,
            self._second_time_unit,
        )

    def __floordiv__(self, other: "Jerk") -> float:
        """Return the floored ratio between the angular jerks."""
        value_as_radian_per_second_cubed = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_cubed = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return (
            value_as_radian_per_second_cubed // other_value_as_radian_per_second_cubed
        )

    def __mod__(self, other: "Jerk") -> float:
        """Return the remainder of the ratio between the angular jerk."""
        value_as_radian_per_second_cubed = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_cubed = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return value_as_radian_per_second_cubed % other_value_as_radian_per_second_cubed

    def __divmod__(self, other: "Jerk") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the angular jerks."""
        value_as_radian_per_second_cubed = self.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        other_value_as_radian_per_second_cubed = other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )
        return divmod(
            value_as_radian_per_second_cubed,
            other_value_as_radian_per_second_cubed,
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal angular jerks."""
        if not isinstance(other, Jerk):
            return NotImplemented

        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) == other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __lt__(self, other: "Jerk") -> bool:
        """Return whether the angular jerk is less than the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) < other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __le__(self, other: "Jerk") -> bool:
        """Return whether the angular jerk is less than or equal to the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) <= other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __gt__(self, other: "Jerk") -> bool:
        """Return whether the angular jerk is greater than the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) > other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __ge__(self, other: "Jerk") -> bool:
        """Return whether the angular jerk is greater than or equal to the other."""
        return self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND) >= other.as_unit(
            AngleUnit.RADIAN, TimeUnit.SECOND
        )

    def __hash__(self) -> int:
        """Return the hash of the angular jerk.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the angular jerk."""
        return (
            f"{self._value} "
            f"{get_angle_unit_abbreviation(self._angle_unit)}/"
            f"{get_time_unit_abbreviation(self._first_time_unit)}/"
            f"{get_time_unit_abbreviation(self._second_time_unit)}/"
            f"{get_time_unit_abbreviation(self._third_time_unit)}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the angular jerk for developers."""
        return (
            f"{__class__.__name__}({self._value},"
            f" {get_angle_unit_name(self._angle_unit)},"
            f" {get_time_unit_name(self._first_time_unit)}),"
            f" {get_time_unit_name(self._second_time_unit)},"
            f" {get_time_unit_name(self._third_time_unit)})"
        )
