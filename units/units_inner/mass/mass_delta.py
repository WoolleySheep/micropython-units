"""Module for the mass difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_kilogram,
)


class MassDelta:
    """The difference between two masses."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new mass difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the mass difference, expressed as the unit."""
        internal_unit_delta_per_kilogram = get_unit_delta_per_kilogram(self._unit)
        value_as_kilogram = self._value / internal_unit_delta_per_kilogram
        external_unit_delta_per_kilogram = get_unit_delta_per_kilogram(unit)
        return external_unit_delta_per_kilogram * value_as_kilogram

    def __mul__(self, value: float) -> "MassDelta":
        """Return a mass difference scaled by the value."""
        scaled_value = self._value * value
        return MassDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "MassDelta":
        """Return a mass difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "MassDelta": ...

    @overload
    def __truediv__(self, other: "MassDelta") -> float: ...

    def __truediv__(self, other: "float | MassDelta") -> "MassDelta | float":
        """Return a scaled mass difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a mass difference scaled by the
          inverse of the value
        - If the argument is a mass difference, return the ratio between the two
          differences
        """
        if isinstance(other, MassDelta):
            value_as_kilogram = self.as_unit(Unit.KILOGRAM)
            other_value_as_kilogram = other.as_unit(Unit.KILOGRAM)
            return value_as_kilogram / other_value_as_kilogram

        scaled_value = self._value / other
        return MassDelta(scaled_value, self._unit)

    def __add__(self, other: "MassDelta") -> "MassDelta":
        """Return the sum of the mass differences."""
        # This NotImplemented block is here because the case of
        # a MassDelta + a Mass is handled in the __radd__ method in the
        # Mass class, otherwise it runs into problems with circular imports
        if not isinstance(other, MassDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_kilogram = self.as_unit(Unit.KILOGRAM)
        delta_value_as_kilogram = other.as_unit(Unit.KILOGRAM)
        added_value_as_kilogram = value_as_kilogram + delta_value_as_kilogram
        return MassDelta(added_value_as_kilogram, Unit.KILOGRAM)

    def __sub__(self, delta: "MassDelta") -> "MassDelta":
        """Return the difference between the mass differences."""
        return self + (-delta)

    def __neg__(self) -> "MassDelta":
        """Return the inverse of the mass difference."""
        inverted_value = -self._value
        return MassDelta(inverted_value, self._unit)

    def __abs__(self) -> "MassDelta":
        """Return the absolute version of the mass difference."""
        absolute_value = abs(self._value)
        return MassDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "MassDelta") -> float:
        """Return the floored ratio between the mass differences."""
        value_as_kilogram = self.as_unit(Unit.KILOGRAM)
        other_value_as_kilogram = other.as_unit(Unit.KILOGRAM)
        return value_as_kilogram // other_value_as_kilogram

    def __mod__(self, other: "MassDelta") -> float:
        """Return the remainder of the ratio between the mass differences."""
        value_as_kilogram = self.as_unit(Unit.KILOGRAM)
        other_value_as_kilogram = other.as_unit(Unit.KILOGRAM)
        return value_as_kilogram % other_value_as_kilogram

    def __divmod__(self, other: "MassDelta") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the mass deltas."""
        value_as_kilogram = self.as_unit(Unit.KILOGRAM)
        other_value_as_kilogram = other.as_unit(Unit.KILOGRAM)
        return divmod(value_as_kilogram, other_value_as_kilogram)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal mass differences."""
        if not isinstance(other, MassDelta):
            return NotImplemented

        return self.as_unit(Unit.KILOGRAM) == other.as_unit(Unit.KILOGRAM)

    def __lt__(self, other: "MassDelta") -> bool:
        """Return whether the mass difference is less than the other."""
        return self.as_unit(Unit.KILOGRAM) < other.as_unit(Unit.KILOGRAM)

    def __le__(self, other: "MassDelta") -> bool:
        """Return whether the mass delta is less than or equal to the other."""
        return self.as_unit(Unit.KILOGRAM) <= other.as_unit(Unit.KILOGRAM)

    def __gt__(self, other: "MassDelta") -> bool:
        """Return whether the mass difference is greater than the other."""
        return self.as_unit(Unit.KILOGRAM) > other.as_unit(Unit.KILOGRAM)

    def __ge__(self, other: "MassDelta") -> bool:
        """Return whether the mass delta is greater than or equal to the other."""
        return self.as_unit(Unit.KILOGRAM) >= other.as_unit(Unit.KILOGRAM)

    def __hash__(self) -> int:
        """Return the hash of the mass difference.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.KILOGRAM))

    def __str__(self) -> str:
        """Return a string representation of the mass difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the mass difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
