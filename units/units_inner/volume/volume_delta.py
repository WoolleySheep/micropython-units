"""Module for the volume difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_cubic_metre,
)


class VolumeDelta:
    """The difference between two volumes."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new volume difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the volume difference, expressed as the unit."""
        internal_unit_delta_per_cubic_metre = get_unit_delta_per_cubic_metre(self._unit)
        value_as_cubic_metre = self._value / internal_unit_delta_per_cubic_metre
        external_unit_delta_per_cubic_metre = get_unit_delta_per_cubic_metre(unit)
        return external_unit_delta_per_cubic_metre * value_as_cubic_metre

    def __mul__(self, value: float) -> "VolumeDelta":
        """Return a volume difference scaled by the value."""
        scaled_value = self._value * value
        return VolumeDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "VolumeDelta":
        """Return a volume difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "VolumeDelta": ...

    @overload
    def __truediv__(self, other: "VolumeDelta") -> float: ...

    def __truediv__(self, other: "float | VolumeDelta") -> "VolumeDelta | float":
        """Return a scaled volume difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a volume difference scaled by the
          inverse of the value
        - If the argument is a volume difference, return the ratio between the two
          differences
        """
        if isinstance(other, VolumeDelta):
            value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
            other_value_as_cubic_metre = other.as_unit(Unit.CUBIC_METRE)
            return value_as_cubic_metre / other_value_as_cubic_metre

        scaled_value = self._value / other
        return VolumeDelta(scaled_value, self._unit)

    def __add__(self, other: "VolumeDelta") -> "VolumeDelta":
        """Return the sum of the volume differences."""
        # This NotImplemented block is here because the case of
        # a VolumeDelta + a Volume is handled in the __radd__ method in the
        # Volume class, otherwise it runs into problems with circular imports
        if not isinstance(other, VolumeDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
        delta_value_as_cubic_metre = other.as_unit(Unit.CUBIC_METRE)
        added_value_as_cubic_metre = value_as_cubic_metre + delta_value_as_cubic_metre
        return VolumeDelta(added_value_as_cubic_metre, Unit.CUBIC_METRE)

    def __sub__(self, delta: "VolumeDelta") -> "VolumeDelta":
        """Return the difference between the volume differences."""
        return self + (-delta)

    def __neg__(self) -> "VolumeDelta":
        """Return the inverse of the volume difference."""
        inverted_value = -self._value
        return VolumeDelta(inverted_value, self._unit)

    def __abs__(self) -> "VolumeDelta":
        """Return the absolute version of the volume difference."""
        absolute_value = abs(self._value)
        return VolumeDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "VolumeDelta") -> float:
        """Return the floored ratio between the volume differences."""
        value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
        other_value_as_cubic_metre = other.as_unit(Unit.CUBIC_METRE)
        return value_as_cubic_metre // other_value_as_cubic_metre

    def __mod__(self, other: "VolumeDelta") -> float:
        """Return the remainder of the ratio between the volume differences."""
        value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
        other_value_as_cubic_metre = other.as_unit(Unit.CUBIC_METRE)
        return value_as_cubic_metre % other_value_as_cubic_metre

    def __divmod__(self, other: "VolumeDelta") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the volume deltas."""
        value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
        other_value_as_cubic_metre = other.as_unit(Unit.CUBIC_METRE)
        return divmod(value_as_cubic_metre, other_value_as_cubic_metre)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal volume differences."""
        if not isinstance(other, VolumeDelta):
            return NotImplemented

        return self.as_unit(Unit.CUBIC_METRE) == other.as_unit(Unit.CUBIC_METRE)

    def __lt__(self, other: "VolumeDelta") -> bool:
        """Return whether the volume difference is less than the other."""
        return self.as_unit(Unit.CUBIC_METRE) < other.as_unit(Unit.CUBIC_METRE)

    def __le__(self, other: "VolumeDelta") -> bool:
        """Return whether the volume delta is less than or equal to the other."""
        return self.as_unit(Unit.CUBIC_METRE) <= other.as_unit(Unit.CUBIC_METRE)

    def __gt__(self, other: "VolumeDelta") -> bool:
        """Return whether the volume difference is greater than the other."""
        return self.as_unit(Unit.CUBIC_METRE) > other.as_unit(Unit.CUBIC_METRE)

    def __ge__(self, other: "VolumeDelta") -> bool:
        """Return whether the volume delta is greater than or equal to the other."""
        return self.as_unit(Unit.CUBIC_METRE) >= other.as_unit(Unit.CUBIC_METRE)

    def __hash__(self) -> int:
        """Return the hash of the volume difference.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.CUBIC_METRE))

    def __str__(self) -> str:
        """Return a string representation of the volume difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the volume difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
