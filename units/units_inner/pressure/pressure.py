"""Module for the pressure class."""

from typing import overload

from .exceptions import NegativePressureValueError
from .pressure_delta import PressureDelta
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_pascal,
)


class Pressure:
    """The force applied per unit area over which that force is distributed."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new pressure."""
        if value < 0:
            raise NegativePressureValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the pressure, expressed as the unit."""
        internal_unit_delta_per_pascal = get_unit_delta_per_pascal(self._unit)
        value_as_pascal = self._value / internal_unit_delta_per_pascal
        external_unit_delta_per_pascal = get_unit_delta_per_pascal(unit)
        return external_unit_delta_per_pascal * value_as_pascal

    def __add__(self, delta: PressureDelta) -> "Pressure":
        """Return the sum of the pressure and the difference."""
        value_as_pascal = self.as_unit(Unit.PASCAL)
        delta_value_as_pascal = delta.as_unit(Unit.PASCAL)
        value_sum_as_pascal = value_as_pascal + delta_value_as_pascal
        return Pressure(value_sum_as_pascal, Unit.PASCAL)

    def __radd__(self, delta: PressureDelta) -> "Pressure":
        """Return the sum of the pressure and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Pressure") -> PressureDelta: ...

    @overload
    def __sub__(self, other: PressureDelta) -> "Pressure": ...

    def __sub__(self, other: "Pressure | PressureDelta") -> "PressureDelta | Pressure":
        """Return the delta between pressures or the pressure less the delta.

        The behaviour depends upon the type of the argument.
        - If the argument is a pressure, return the difference between the two
          pressures.
        - If the argument is a pressure difference, return the pressure less the
          difference.
        """
        value_as_pascal = self.as_unit(Unit.PASCAL)
        other_value_as_pascal = other.as_unit(Unit.PASCAL)
        value_difference_as_pascal = value_as_pascal - other_value_as_pascal
        return (
            PressureDelta(value_difference_as_pascal, Unit.PASCAL)
            if isinstance(other, Pressure)
            else Pressure(value_difference_as_pascal, Unit.PASCAL)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal pressures."""
        if not isinstance(other, Pressure):
            return NotImplemented

        return self.as_unit(Unit.PASCAL) == other.as_unit(Unit.PASCAL)

    def __lt__(self, other: "Pressure") -> bool:
        """Return whether the pressure is less than the other."""
        return self.as_unit(Unit.PASCAL) < other.as_unit(Unit.PASCAL)

    def __le__(self, other: "Pressure") -> bool:
        """Return whether the pressure is less than or equal to the other."""
        return self.as_unit(Unit.PASCAL) <= other.as_unit(Unit.PASCAL)

    def __gt__(self, other: "Pressure") -> bool:
        """Return whether the pressure is greater than the other."""
        return self.as_unit(Unit.PASCAL) > other.as_unit(Unit.PASCAL)

    def __ge__(self, other: "Pressure") -> bool:
        """Return whether the pressure is greater than or equal to the other."""
        return self.as_unit(Unit.PASCAL) >= other.as_unit(Unit.PASCAL)

    def __hash__(self) -> int:
        """Return the hash of the pressure.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.PASCAL))

    def __str__(self) -> str:
        """Return a string representation of the pressure."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the pressure for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
