"""Module for the angle difference class."""

import math

from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_radian,
)


def _map_to_unit_circle(value: float, unit: Unit) -> float:
    """Map an angle to the range [-pi, pi) radians."""
    unit_delta_per_radian = get_unit_delta_per_radian(unit)
    tmp_value = value % (2 * math.pi * unit_delta_per_radian)
    if tmp_value < -math.pi * unit_delta_per_radian:
        return tmp_value + 2 * math.pi * unit_delta_per_radian
    if tmp_value >= math.pi * unit_delta_per_radian:
        return tmp_value - 2 * math.pi * unit_delta_per_radian
    return tmp_value


class AngleDelta:
    """The difference between two angles.

    Angle always in range [-pi, pi) radians. Values outside this range will be mapped
    into it.

    +--------+-----------------------------------+-----------------------------------+
    | Range  | INITIALIZATION                    | EQUIVALENT TO                     |
    +========+===================================+===================================+
    | Within | AngleDelta(-40, Unit.DEGREE)      | AngleDelta(-40, Unit.DEGREE)      |
    +--------+-----------------------------------+-----------------------------------+
    | Below  | AngleDelta(-3*pi, Unit.RADIAN)    | AngleDelta(pi, Unit.RADIAN)       |
    +--------+-----------------------------------+-----------------------------------+
    | Above  | AngleDelta(3.75, Unit.REVOLUTION) | AngleDelta(-0.25, Unit.REVOLUTION)|
    +--------+-------------------------------------+---------------------------------+
    """

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new angle difference."""
        self._value = _map_to_unit_circle(value, unit)
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the angle difference, expressed as the unit."""
        internal_unit_delta_per_radian = get_unit_delta_per_radian(self._unit)
        value_as_radian = self._value / internal_unit_delta_per_radian
        external_unit_delta_per_radian = get_unit_delta_per_radian(unit)
        return external_unit_delta_per_radian * value_as_radian

    def __add__(self, other: "AngleDelta") -> "AngleDelta":
        """Return the sum of the angle differences."""
        # This NotImplemented block is here because the case of
        # a AngleDelta + an Angle is handled in the __radd__ method in the
        # Angle class, otherwise it runs into problems with circular imports
        if not isinstance(other, AngleDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_radian = self.as_unit(Unit.RADIAN)
        delta_value_as_radian = other.as_unit(Unit.RADIAN)
        added_value_as_radian = value_as_radian + delta_value_as_radian
        return AngleDelta(added_value_as_radian, Unit.RADIAN)

    def __sub__(self, delta: "AngleDelta") -> "AngleDelta":
        """Return the difference between the angle differences."""
        return self + (-delta)

    def __neg__(self) -> "AngleDelta":
        """Return the inverse of the angle difference."""
        inverted_value = -self._value
        return AngleDelta(inverted_value, self._unit)

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal angle differences."""
        if not isinstance(other, AngleDelta):
            return NotImplemented

        return self.as_unit(Unit.RADIAN) == other.as_unit(Unit.RADIAN)

    def __hash__(self) -> int:
        """Return the hash of the angle difference.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.RADIAN))

    def __str__(self) -> str:
        """Return a string representation of the angle difference."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the angle difference for devs."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
