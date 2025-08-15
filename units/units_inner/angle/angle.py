"""Module for the angle class."""

import math
from typing import overload

from .angle_delta import AngleDelta
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_radian,
)


def _map_to_unit_circle(value: float, unit: Unit) -> float:
    """Map an angle to the range [0, 2*pi) radians."""
    unit_delta_per_radian = get_unit_delta_per_radian(unit)
    tmp_value = value % (2 * math.pi * unit_delta_per_radian)
    return (
        tmp_value if tmp_value >= 0 else tmp_value + 2 * math.pi * unit_delta_per_radian
    )


class Angle:
    """The opening between two lines in the same plane that meet at a point.

    Angle always in range [0, 2*pi) radians. Values outside this range will be mapped
    into it.

    +--------+--------------------------------+-----------------------------+
    | Range  | INITIALIZATION                 | EQUIVALENT TO               |
    +========+================================+=============================+
    | Within | Angle(185, Unit.DEGREE)        | Angle(185, Unit.DEGREE)     |
    +--------+--------------------------------+-----------------------------+
    | Below  | Angle(-3*math.pi, Unit.RADIAN) | Angle(math.pi, Unit.RADIAN) |
    +--------+--------------------------------+-----------------------------+
    | Above  | Angle(4, Unit.REVOLUTION)      | Angle(0, Unit.REVOLUTION)   |
    +--------+--------------------------------+-----------------------------+
    """

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new angle."""
        self._value = _map_to_unit_circle(value, unit)
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the angle, expressed as the unit."""
        internal_unit_delta_per_radian = get_unit_delta_per_radian(self._unit)
        value_as_radian = self._value / internal_unit_delta_per_radian
        external_unit_delta_per_radian = get_unit_delta_per_radian(unit)
        return external_unit_delta_per_radian * value_as_radian

    def __add__(self, delta: AngleDelta) -> "Angle":
        """Return the sum of the angle and the difference."""
        value_as_radian = self.as_unit(Unit.RADIAN)
        delta_value_as_radian = delta.as_unit(Unit.RADIAN)
        value_sum_as_radian = value_as_radian + delta_value_as_radian
        return Angle(value_sum_as_radian, Unit.RADIAN)

    def __radd__(self, delta: AngleDelta) -> "Angle":
        """Return the sum of the angle and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Angle") -> AngleDelta: ...

    @overload
    def __sub__(self, other: AngleDelta) -> "Angle": ...

    def __sub__(self, other: "Angle | AngleDelta") -> "AngleDelta | Angle":
        """Return the delta between angles or the angle less the delta.

        The behaviour depends upon the type of the argument.
        - If the argument is an angle, return the difference between the two
          angles.
        - If the argument is an angle delta, return the angle less the
          difference.
        """
        value_as_radian = self.as_unit(Unit.RADIAN)
        other_value_as_radian = other.as_unit(Unit.RADIAN)
        value_difference_as_radian = value_as_radian - other_value_as_radian
        return (
            AngleDelta(value_difference_as_radian, Unit.RADIAN)
            if isinstance(other, Angle)
            else Angle(value_difference_as_radian, Unit.RADIAN)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal angles."""
        if not isinstance(other, Angle):
            return NotImplemented

        return self.as_unit(Unit.RADIAN) == other.as_unit(Unit.RADIAN)

    def __hash__(self) -> int:
        """Return the hash of the length.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.RADIAN))

    def __str__(self) -> str:
        """Return a string representation of the length."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the length for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
