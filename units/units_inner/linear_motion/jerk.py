"""Module for the jerk class."""

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
from ..time import (
    get_unit_delta_per_second as get_time_unit_delta_per_second,
)
from ..time import get_unit_name as get_time_unit_name


class Jerk:
    """The rate of change of the jerk of an object with respect to time."""

    def __init__(  # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        value: float,
        distance_unit: DistanceUnit,
        first_time_unit: TimeUnit,
        second_time_unit: TimeUnit | None = None,
        third_time_unit: TimeUnit | None = None,
    ) -> None:
        """Initialise a new jerk.

        If a second time unit is not provided, the first time unit will be reused.
        If the third time unit is not provided, the second time unit will be reused
        (or the first, if the second is also not provided).
        """
        self._value = value
        self._distance_unit = distance_unit
        self._first_time_unit = first_time_unit
        self._second_time_unit = (
            second_time_unit if second_time_unit is not None else first_time_unit
        )
        self._third_time_unit = (
            third_time_unit if third_time_unit is not None else self._second_time_unit
        )

    def as_unit(  # pylint: disable=too-many-locals
        self,
        distance_unit: DistanceUnit,
        first_time_unit: TimeUnit,
        second_time_unit: TimeUnit | None = None,
        third_time_unit: TimeUnit | None = None,
    ) -> float:
        """Return the jerk in the specified units.

        If a second time unit is not provided, the first time unit will be reused.
        If the third time unit is not provided, the second time unit will be reused
        (or the first, if the second is also not provided).
        """
        internal_distance_unit_delta_per_metre = get_distance_unit_delta_per_metre(
            self._distance_unit
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
        internal_unit_to_metre_per_second_cubed_factor = (
            internal_third_time_unit_delta_per_second
            * internal_second_time_unit_delta_per_second
            * internal_first_time_unit_delta_per_second
            / internal_distance_unit_delta_per_metre
        )
        value_as_metre_per_second_cubed = (
            internal_unit_to_metre_per_second_cubed_factor * self._value
        )
        external_distance_unit_delta_per_metre = get_distance_unit_delta_per_metre(
            distance_unit
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
        metre_per_second_cubed_to_external_unit_factor = (
            external_distance_unit_delta_per_metre
            / (
                external_first_time_unit_delta_per_second
                * external_second_time_unit_delta_per_second
                * external_third_time_unit_delta_per_second
            )
        )
        return (
            metre_per_second_cubed_to_external_unit_factor
            * value_as_metre_per_second_cubed
        )

    def __mul__(self, value: float) -> "Jerk":
        """Return an jerk scaled by the value."""
        scaled_value = self._value * value
        return Jerk(
            scaled_value,
            self._distance_unit,
            self._first_time_unit,
            self._second_time_unit,
            self._third_time_unit,
        )

    def __rmul__(self, value: float) -> "Jerk":
        """Return an jerk scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Jerk": ...

    @overload
    def __truediv__(self, other: "Jerk") -> float: ...

    def __truediv__(self, other: "float | Jerk") -> "Jerk | float":
        """Return a scaled jerk or the ratio between the jerks.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return an jerk scaled by the
          inverse of the value
        - If the argument is an jerk, return the ratio between the two
          jerks
        """
        if isinstance(other, Jerk):
            value_as_metre_per_second_cubed = self.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND
            )
            other_value_as_metre_per_second_cubed = other.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND
            )
            return (
                value_as_metre_per_second_cubed / other_value_as_metre_per_second_cubed
            )

        return (1 / other) * self

    def __add__(self, other: "Jerk") -> "Jerk":
        """Return the sum of two jerks."""
        value_as_metre_per_second_cubed = self.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        other_value_as_metre_per_second_cubed = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        value_sum_as_metre_per_second_cubed = (
            value_as_metre_per_second_cubed + other_value_as_metre_per_second_cubed
        )
        return Jerk(
            value_sum_as_metre_per_second_cubed,
            DistanceUnit.METRE,
            TimeUnit.SECOND,
        )

    def __sub__(self, other: "Jerk") -> "Jerk":
        """Return the difference of two jerks."""
        value_as_metre_per_second_cubed = self.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        other_value_as_metre_per_second_cubed = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        value_difference_as_metre_per_second_cubed = (
            value_as_metre_per_second_cubed - other_value_as_metre_per_second_cubed
        )
        return Jerk(
            value_difference_as_metre_per_second_cubed,
            DistanceUnit.METRE,
            TimeUnit.SECOND,
        )

    def __neg__(self) -> "Jerk":
        """Return the inverse of the jerk."""
        return -1 * self

    def __abs__(self) -> "Jerk":
        """Return the absolute version of the jerk."""
        absolute_value = abs(self._value)
        return Jerk(
            absolute_value,
            self._distance_unit,
            self._first_time_unit,
            self._second_time_unit,
        )

    def __floordiv__(self, other: "Jerk") -> float:
        """Return the floored ratio between the jerks."""
        value_as_metre_per_second_cubed = self.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        other_value_as_metre_per_second_cubed = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        return value_as_metre_per_second_cubed // other_value_as_metre_per_second_cubed

    def __mod__(self, other: "Jerk") -> float:
        """Return the remainder of the ratio between the jerk."""
        value_as_metre_per_second_cubed = self.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        other_value_as_metre_per_second_cubed = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        return value_as_metre_per_second_cubed % other_value_as_metre_per_second_cubed

    def __divmod__(self, other: "Jerk") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the jerks."""
        value_as_metre_per_second_cubed = self.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        other_value_as_metre_per_second_cubed = other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )
        return divmod(
            value_as_metre_per_second_cubed,
            other_value_as_metre_per_second_cubed,
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal jerks."""
        if not isinstance(other, Jerk):
            return NotImplemented

        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) == other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __lt__(self, other: "Jerk") -> bool:
        """Return whether the jerk is less than the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) < other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __le__(self, other: "Jerk") -> bool:
        """Return whether the jerk is less than or equal to the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) <= other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __gt__(self, other: "Jerk") -> bool:
        """Return whether the jerk is greater than the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) > other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __ge__(self, other: "Jerk") -> bool:
        """Return whether the jerk is greater than or equal to the other."""
        return self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND) >= other.as_unit(
            DistanceUnit.METRE, TimeUnit.SECOND
        )

    def __hash__(self) -> int:
        """Return the hash of the jerk.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(DistanceUnit.METRE, TimeUnit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the jerk."""
        return (
            f"{self._value} "
            f"{get_distance_unit_abbreviation(self._distance_unit)}/"
            f"{get_time_unit_abbreviation(self._first_time_unit)}/"
            f"{get_time_unit_abbreviation(self._second_time_unit)}/"
            f"{get_time_unit_abbreviation(self._third_time_unit)}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the jerk for developers."""
        return (
            f"{__class__.__name__}({self._value},"
            f" {get_distance_unit_name(self._distance_unit)},"
            f" {get_time_unit_name(self._first_time_unit)}),"
            f" {get_time_unit_name(self._second_time_unit)},"
            f" {get_time_unit_name(self._third_time_unit)})"
        )
