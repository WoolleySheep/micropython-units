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
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the pressure difference, expressed as the unit."""
        internal_unit_delta_per_pascal = get_unit_delta_per_pascal(self._unit)
        value_as_pascal = self._value / internal_unit_delta_per_pascal
        external_unit_delta_per_pascal = get_unit_delta_per_pascal(unit)
        return external_unit_delta_per_pascal * value_as_pascal

    def __mul__(self, multiplier: float) -> "PressureDelta":
        scaled_value = self._value * multiplier
        return PressureDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "PressureDelta":
        return self * value

    @overload
    def __truediv__(self, other: float) -> "PressureDelta": ...

    @overload
    def __truediv__(self, other: "PressureDelta") -> float: ...

    def __truediv__(self, other: "float | PressureDelta") -> "PressureDelta | float":
        if isinstance(other, PressureDelta):
            value_as_pascal = self.as_unit(Unit.PASCAL)
            other_value_as_pascal = other.as_unit(Unit.PASCAL)
            return value_as_pascal / other_value_as_pascal

        scaled_value = self._value / other
        return PressureDelta(scaled_value, self._unit)

    def __add__(self, other: "PressureDelta") -> "PressureDelta":
        # This is here because the case of a PressureDelta + a Pressure is
        # handled in the __radd__ method in the Pressure class, otherwise it
        # runs into problems with circular imports
        if not isinstance(other, PressureDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_pascal = self.as_unit(Unit.PASCAL)
        delta_value_as_pascal = other.as_unit(Unit.PASCAL)
        added_value_as_pascal = value_as_pascal + delta_value_as_pascal
        return PressureDelta(added_value_as_pascal, Unit.PASCAL)

    def __sub__(self, delta: "PressureDelta") -> "PressureDelta":
        return self + (-delta)

    def __neg__(self) -> "PressureDelta":
        inverted_value = -self._value
        return PressureDelta(inverted_value, self._unit)

    def __abs__(self) -> "PressureDelta":
        absolute_value = abs(self._value)
        return PressureDelta(absolute_value, self._unit)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, PressureDelta) and self.as_unit(
            Unit.PASCAL
        ) == other.as_unit(Unit.PASCAL)

    def __lt__(self, other: "PressureDelta") -> bool:
        return self.as_unit(Unit.PASCAL) < other.as_unit(Unit.PASCAL)

    def __le__(self, other: "PressureDelta") -> bool:
        return self.as_unit(Unit.PASCAL) <= other.as_unit(Unit.PASCAL)

    def __gt__(self, other: "PressureDelta") -> bool:
        return self.as_unit(Unit.PASCAL) > other.as_unit(Unit.PASCAL)

    def __ge__(self, other: "PressureDelta") -> bool:
        return self.as_unit(Unit.PASCAL) >= other.as_unit(Unit.PASCAL)

    def __str__(self) -> str:
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
