"""Module for the mass class."""

from typing import overload

from .exceptions import NegativeMassValueError
from .mass_delta import MassDelta
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_kilogram,
)


class Mass:
    """The force applied per unit area over which that force is distributed."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new mass.

        Raises:
            NegativeMassValueError: The negative value produced a mass less than 0kg.
        """
        if value < 0:
            raise NegativeMassValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the mass, expressed as the unit."""
        internal_unit_delta_per_kilogram = get_unit_delta_per_kilogram(self._unit)
        value_as_kilogram = self._value / internal_unit_delta_per_kilogram
        external_unit_delta_per_kilogram = get_unit_delta_per_kilogram(unit)
        return external_unit_delta_per_kilogram * value_as_kilogram

    def __add__(self, delta: MassDelta) -> "Mass":
        """Return the sum of the mass and the difference.

        Raises:
            NegativeMassValueError: The sum of the mass and the difference was less
                than 0kg.
        """
        value_as_kilogram = self.as_unit(Unit.KILOGRAM)
        delta_value_as_kilogram = delta.as_unit(Unit.KILOGRAM)
        value_sum_as_kilogram = value_as_kilogram + delta_value_as_kilogram
        return Mass(value_sum_as_kilogram, Unit.KILOGRAM)

    def __radd__(self, delta: MassDelta) -> "Mass":
        """Return the sum of the mass and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Mass") -> MassDelta: ...

    @overload
    def __sub__(self, other: MassDelta) -> "Mass": ...

    def __sub__(self, other: "Mass | MassDelta") -> "MassDelta | Mass":
        """Return the delta between mass or the mass less the delta.

        The behaviour depends upon the type of the argument.

        - If the argument is a :py:class:`Mass`, return the difference between the two
          masses.
        - If the argument is a :py:class:`MassDelta`, return the mass less the
          difference.

        Raises:
            NegativeMassValueError: The mass minus the difference was less
                than 0kg. Only possible when other is a MassDelta.
        """
        value_as_kilogram = self.as_unit(Unit.KILOGRAM)
        other_value_as_kilogram = other.as_unit(Unit.KILOGRAM)
        value_difference_as_kilogram = value_as_kilogram - other_value_as_kilogram
        return (
            MassDelta(value_difference_as_kilogram, Unit.KILOGRAM)
            if isinstance(other, Mass)
            else Mass(value_difference_as_kilogram, Unit.KILOGRAM)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal masses."""
        if not isinstance(other, Mass):
            return NotImplemented

        return self.as_unit(Unit.KILOGRAM) == other.as_unit(Unit.KILOGRAM)

    def __lt__(self, other: "Mass") -> bool:
        """Return whether the mass is less than the other."""
        return self.as_unit(Unit.KILOGRAM) < other.as_unit(Unit.KILOGRAM)

    def __le__(self, other: "Mass") -> bool:
        """Return whether the mass is less than or equal to the other."""
        return self.as_unit(Unit.KILOGRAM) <= other.as_unit(Unit.KILOGRAM)

    def __gt__(self, other: "Mass") -> bool:
        """Return whether the mass is greater than the other."""
        return self.as_unit(Unit.KILOGRAM) > other.as_unit(Unit.KILOGRAM)

    def __ge__(self, other: "Mass") -> bool:
        """Return whether the mass is greater than or equal to the other."""
        return self.as_unit(Unit.KILOGRAM) >= other.as_unit(Unit.KILOGRAM)

    def __hash__(self) -> int:
        """Return the hash of the mass."""
        return hash(self.as_unit(Unit.KILOGRAM))

    def __str__(self) -> str:
        """Return a string representation of the mass."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the mass for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
