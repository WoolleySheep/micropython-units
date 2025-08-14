"""Module for the pressure difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_pascal,
)


class PressureDelta:
    """The difference between two pressures."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new pressure difference."""
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the pressure difference, expressed as the unit."""
        internal_unit_delta_per_pascal = get_unit_delta_per_pascal(self._unit)
        value_as_pascal = self._value / internal_unit_delta_per_pascal
        external_unit_delta_per_pascal = get_unit_delta_per_pascal(unit)
        return external_unit_delta_per_pascal * value_as_pascal

    def __mul__(self, value: float) -> "PressureDelta":
        """Return a pressure difference scaled by the value."""
        scaled_value = self._value * value
        return PressureDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "PressureDelta":
        """Return a pressure difference scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "PressureDelta": ...

    @overload
    def __truediv__(self, other: "PressureDelta") -> float: ...

    def __truediv__(self, other: "float | PressureDelta") -> "PressureDelta | float":
        """Return a scaled pressure difference or the ratio between the differences.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a pressure difference scaled by the
          inverse of the value
        - If the argument is a pressure difference, return the ratio between the two
          differences
        """
        if isinstance(other, PressureDelta):
            value_as_pascal = self.as_unit(Unit.PASCAL)
            other_value_as_pascal = other.as_unit(Unit.PASCAL)
            return value_as_pascal / other_value_as_pascal

        scaled_value = self._value / other
        return PressureDelta(scaled_value, self._unit)

    def __add__(self, other: "PressureDelta") -> "PressureDelta":
        """Return the sum of the pressure differences."""
        # This NotImplemented block is here because the case of
        # a PressureDelta + a Pressure is handled in the __radd__ method in the
        # Pressure class, otherwise it runs into problems with circular imports
        if not isinstance(other, PressureDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_pascal = self.as_unit(Unit.PASCAL)
        delta_value_as_pascal = other.as_unit(Unit.PASCAL)
        added_value_as_pascal = value_as_pascal + delta_value_as_pascal
        return PressureDelta(added_value_as_pascal, Unit.PASCAL)

    def __sub__(self, delta: "PressureDelta") -> "PressureDelta":
        """Return the difference between the pressure differences."""
        return self + (-delta)

    def __neg__(self) -> "PressureDelta":
        """Return the inverse of the pressure difference."""
        inverted_value = -self._value
        return PressureDelta(inverted_value, self._unit)

    def __abs__(self) -> "PressureDelta":
        """Return the absolute version of the pressure difference."""
        absolute_value = abs(self._value)
        return PressureDelta(absolute_value, self._unit)

    def __floordiv__(self, other: "PressureDelta") -> float:
        """Return the floored ratio between the pressure differences."""
        value_as_pascal = self.as_unit(Unit.PASCAL)
        other_value_as_pascal = other.as_unit(Unit.PASCAL)
        return value_as_pascal // other_value_as_pascal

    def __mod__(self, other: "PressureDelta") -> float:
        """Return the remainder of the ratio between the pressure differences."""
        value_as_pascal = self.as_unit(Unit.PASCAL)
        other_value_as_pascal = other.as_unit(Unit.PASCAL)
        return value_as_pascal % other_value_as_pascal

    def __divmod__(self, other: "PressureDelta") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the pressure deltas."""
        value_as_pascal = self.as_unit(Unit.PASCAL)
        other_value_as_pascal = other.as_unit(Unit.PASCAL)
        return divmod(value_as_pascal, other_value_as_pascal)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal pressure differences."""
        if not isinstance(other, PressureDelta):
            return NotImplemented

        return self.as_unit(Unit.PASCAL) == other.as_unit(Unit.PASCAL)

    def __lt__(self, other: "PressureDelta") -> bool:
        """Return whether the pressure difference is less than the other."""
        return self.as_unit(Unit.PASCAL) < other.as_unit(Unit.PASCAL)

    def __le__(self, other: "PressureDelta") -> bool:
        """Return whether the pressure delta is less than or equal to the other."""
        return self.as_unit(Unit.PASCAL) <= other.as_unit(Unit.PASCAL)

    def __gt__(self, other: "PressureDelta") -> bool:
        """Return whether the pressure difference is greater than the other."""
        return self.as_unit(Unit.PASCAL) > other.as_unit(Unit.PASCAL)

    def __ge__(self, other: "PressureDelta") -> bool:
        """Return whether the pressure delta is greater than or equal to the other."""
        return self.as_unit(Unit.PASCAL) >= other.as_unit(Unit.PASCAL)

    def __hash__(self) -> int:
        """Return the hash of the pressure difference.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.PASCAL))

    def __str__(self) -> str:
        """Return a string representation of the pressure difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the pressure difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
