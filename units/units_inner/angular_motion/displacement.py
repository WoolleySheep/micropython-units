"""Module for the angular displacement class."""

# ruff: noqa: TID252

from typing import overload

from ..angle import Unit as AngleUnit
from ..angle import (
    get_unit_abbreviation,
    get_unit_delta_per_radian,
    get_unit_name,
)


class Displacement:
    """The difference between the final & initial position of an angular trajectory."""

    def __init__(self, value: float, unit: AngleUnit) -> None:
        """Initialise a new angular displacement."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: AngleUnit) -> float:
        """Get the angular displacement, expressed as the unit."""
        internal_unit_delta_per_radian = get_unit_delta_per_radian(self._unit)
        value_as_radian = self._value / internal_unit_delta_per_radian
        external_unit_delta_per_radian = get_unit_delta_per_radian(unit)
        return external_unit_delta_per_radian * value_as_radian

    def __mul__(self, value: float) -> "Displacement":
        """Return a angular displacement scaled by the value."""
        scaled_value = self._value * value
        return Displacement(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "Displacement":
        """Return a angular displacement scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Displacement": ...

    @overload
    def __truediv__(self, other: "Displacement") -> float: ...

    def __truediv__(self, other: "float | Displacement") -> "Displacement | float":
        """Return a scaled angular displacement or the ratio between the displacements.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a angular displacement scaled by the
          inverse of the value
        - If the argument is a angular displacement, return the ratio between the two
          angular displacements
        """
        if isinstance(other, Displacement):
            value_as_radian = self.as_unit(AngleUnit.RADIAN)
            other_value_as_radian = other.as_unit(AngleUnit.RADIAN)
            return value_as_radian / other_value_as_radian

        scaled_value = self._value / other
        return Displacement(scaled_value, self._unit)

    def __add__(self, other: "Displacement") -> "Displacement":
        """Return the sum of the angular displacements."""
        value_as_radian = self.as_unit(AngleUnit.RADIAN)
        delta_value_as_radian = other.as_unit(AngleUnit.RADIAN)
        added_value_as_radian = value_as_radian + delta_value_as_radian
        return Displacement(added_value_as_radian, AngleUnit.RADIAN)

    def __sub__(self, delta: "Displacement") -> "Displacement":
        """Return the difference between the angular displacements."""
        return self + (-delta)

    def __neg__(self) -> "Displacement":
        """Return the inverse of the angular displacement."""
        inverted_value = -self._value
        return Displacement(inverted_value, self._unit)

    def __abs__(self) -> "Displacement":
        """Return the absolute version of the angular displacement."""
        absolute_value = abs(self._value)
        return Displacement(absolute_value, self._unit)

    def __floordiv__(self, other: "Displacement") -> float:
        """Return the floored ratio between the angular displacements."""
        value_as_radian = self.as_unit(AngleUnit.RADIAN)
        other_value_as_radian = other.as_unit(AngleUnit.RADIAN)
        return value_as_radian // other_value_as_radian

    def __mod__(self, other: "Displacement") -> float:
        """Return the remainder of the ratio between the angular displacements."""
        value_as_radian = self.as_unit(AngleUnit.RADIAN)
        other_value_as_radian = other.as_unit(AngleUnit.RADIAN)
        return value_as_radian % other_value_as_radian

    def __divmod__(self, other: "Displacement") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio btwn the displacements."""
        value_as_radian = self.as_unit(AngleUnit.RADIAN)
        other_value_as_radian = other.as_unit(AngleUnit.RADIAN)
        return divmod(value_as_radian, other_value_as_radian)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal angular displacements."""
        if not isinstance(other, Displacement):
            return NotImplemented

        return self.as_unit(AngleUnit.RADIAN) == other.as_unit(AngleUnit.RADIAN)

    def __lt__(self, other: "Displacement") -> bool:
        """Return whether the angular displacement is less than the other."""
        return self.as_unit(AngleUnit.RADIAN) < other.as_unit(AngleUnit.RADIAN)

    def __le__(self, other: "Displacement") -> bool:
        """Return whether the angular displacement is less than or equal to other."""
        return self.as_unit(AngleUnit.RADIAN) <= other.as_unit(AngleUnit.RADIAN)

    def __gt__(self, other: "Displacement") -> bool:
        """Return whether the angular displacement is greater than the other."""
        return self.as_unit(AngleUnit.RADIAN) > other.as_unit(AngleUnit.RADIAN)

    def __ge__(self, other: "Displacement") -> bool:
        """Return whether the angular displacement is greater than or equal to other."""
        return self.as_unit(AngleUnit.RADIAN) >= other.as_unit(AngleUnit.RADIAN)

    def __hash__(self) -> int:
        """Return the hash of the angular displacement.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(AngleUnit.RADIAN))

    def __str__(self) -> str:
        """Return a string representation of the angular displacement."""
        return f"{self._value} {get_unit_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the angular displacement for devs."""
        return f"{__class__.__name__}({self._value}, {get_unit_name(self._unit)})"
