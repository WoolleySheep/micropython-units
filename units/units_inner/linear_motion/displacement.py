"""Module for the displacement class."""

# ruff: noqa: TID252

from typing import overload

from ..length import Unit as DistanceUnit
from ..length import (
    get_unit_abbreviation,
    get_unit_delta_per_metre,
    get_unit_name,
)


class Displacement:
    """The difference between the final and initial position of a trajectory."""

    def __init__(self, value: float, unit: DistanceUnit) -> None:
        """Initialise a new displacement."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: DistanceUnit) -> float:
        """Get the displacement, expressed as the unit."""
        internal_unit_delta_per_metre = get_unit_delta_per_metre(self._unit)
        value_as_metre = self._value / internal_unit_delta_per_metre
        external_unit_delta_per_metre = get_unit_delta_per_metre(unit)
        return external_unit_delta_per_metre * value_as_metre

    def __mul__(self, value: float) -> "Displacement":
        """Return a displacement scaled by the value."""
        scaled_value = self._value * value
        return Displacement(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "Displacement":
        """Return a displacement scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "Displacement": ...

    @overload
    def __truediv__(self, other: "Displacement") -> float: ...

    def __truediv__(self, other: "float | Displacement") -> "Displacement | float":
        """Return a scaled displacement or the ratio between the displacements.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a displacement scaled by the
          inverse of the value
        - If the argument is a displacement, return the ratio between the two
          displacements
        """
        if isinstance(other, Displacement):
            value_as_metre = self.as_unit(DistanceUnit.METRE)
            other_value_as_metre = other.as_unit(DistanceUnit.METRE)
            return value_as_metre / other_value_as_metre

        scaled_value = self._value / other
        return Displacement(scaled_value, self._unit)

    def __add__(self, other: "Displacement") -> "Displacement":
        """Return the sum of the displacements."""
        value_as_metre = self.as_unit(DistanceUnit.METRE)
        delta_value_as_metre = other.as_unit(DistanceUnit.METRE)
        added_value_as_metre = value_as_metre + delta_value_as_metre
        return Displacement(added_value_as_metre, DistanceUnit.METRE)

    def __sub__(self, delta: "Displacement") -> "Displacement":
        """Return the difference between the displacements."""
        return self + (-delta)

    def __neg__(self) -> "Displacement":
        """Return the inverse of the displacement."""
        inverted_value = -self._value
        return Displacement(inverted_value, self._unit)

    def __abs__(self) -> "Displacement":
        """Return the absolute version of the displacement."""
        absolute_value = abs(self._value)
        return Displacement(absolute_value, self._unit)

    def __floordiv__(self, other: "Displacement") -> float:
        """Return the floored ratio between the displacements."""
        value_as_metre = self.as_unit(DistanceUnit.METRE)
        other_value_as_metre = other.as_unit(DistanceUnit.METRE)
        return value_as_metre // other_value_as_metre

    def __mod__(self, other: "Displacement") -> float:
        """Return the remainder of the ratio between the displacements."""
        value_as_metre = self.as_unit(DistanceUnit.METRE)
        other_value_as_metre = other.as_unit(DistanceUnit.METRE)
        return value_as_metre % other_value_as_metre

    def __divmod__(self, other: "Displacement") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the displacements."""
        value_as_metre = self.as_unit(DistanceUnit.METRE)
        other_value_as_metre = other.as_unit(DistanceUnit.METRE)
        return divmod(value_as_metre, other_value_as_metre)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal displacements."""
        if not isinstance(other, Displacement):
            return NotImplemented

        return self.as_unit(DistanceUnit.METRE) == other.as_unit(DistanceUnit.METRE)

    def __lt__(self, other: "Displacement") -> bool:
        """Return whether the displacement is less than the other."""
        return self.as_unit(DistanceUnit.METRE) < other.as_unit(DistanceUnit.METRE)

    def __le__(self, other: "Displacement") -> bool:
        """Return whether the displacement is less than or equal to the other."""
        return self.as_unit(DistanceUnit.METRE) <= other.as_unit(DistanceUnit.METRE)

    def __gt__(self, other: "Displacement") -> bool:
        """Return whether the displacement is greater than the other."""
        return self.as_unit(DistanceUnit.METRE) > other.as_unit(DistanceUnit.METRE)

    def __ge__(self, other: "Displacement") -> bool:
        """Return whether the displacement is greater than or equal to the other."""
        return self.as_unit(DistanceUnit.METRE) >= other.as_unit(DistanceUnit.METRE)

    def __hash__(self) -> int:
        """Return the hash of the displacement.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(DistanceUnit.METRE))

    def __str__(self) -> str:
        """Return a string representation of the displacement."""
        return f"{self._value} {get_unit_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the displacement for devs."""
        return f"{__class__.__name__}({self._value}, {get_unit_name(self._unit)})"
