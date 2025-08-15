"""Module for the area class."""

from typing import overload

from .area_delta import AreaDelta
from .exceptions import NegativeAreaValueError
from .unit import Unit, get_abbreviation, get_name, get_unit_delta_per_square_metre


class Area:
    """The measure of a two-dimensional space."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new area."""
        if value < 0:
            raise NegativeAreaValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the area, expressed as the unit."""
        internal_unit_delta_per_square_metre = get_unit_delta_per_square_metre(
            self._unit
        )
        value_as_square_metre = self._value / internal_unit_delta_per_square_metre
        external_unit_delta_per_square_meter = get_unit_delta_per_square_metre(unit)
        return external_unit_delta_per_square_meter * value_as_square_metre

    def __add__(self, delta: AreaDelta) -> "Area":
        """Return the sum of the area and the difference."""
        value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
        delta_value_as_square_metre = delta.as_unit(Unit.SQUARE_METRE)
        value_sum_as_square_metre = value_as_square_metre + delta_value_as_square_metre
        return Area(value_sum_as_square_metre, Unit.SQUARE_METRE)

    def __radd__(self, delta: AreaDelta) -> "Area":
        """Return the sum of the area and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Area") -> AreaDelta: ...

    @overload
    def __sub__(self, other: AreaDelta) -> "Area": ...

    def __sub__(self, other: "Area | AreaDelta") -> "AreaDelta | Area":
        """Return the delta between areas or the area less the delta.

        The behaviour depends upon the type of the argument.
        - If the argument is a area, return the difference between the two
          areas.
        - If the argument is a area difference, return the area less the
          difference.
        """
        value_as_square_metre = self.as_unit(Unit.SQUARE_METRE)
        other_value_as_square_metre = other.as_unit(Unit.SQUARE_METRE)
        value_difference_as_square_metre = (
            value_as_square_metre - other_value_as_square_metre
        )
        return (
            AreaDelta(value_difference_as_square_metre, Unit.SQUARE_METRE)
            if isinstance(other, Area)
            else Area(value_difference_as_square_metre, Unit.SQUARE_METRE)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal areas."""
        if not isinstance(other, Area):
            return NotImplemented

        return self.as_unit(Unit.SQUARE_METRE) == other.as_unit(Unit.SQUARE_METRE)

    def __lt__(self, other: "Area") -> bool:
        """Return whether the area is less than the other."""
        return self.as_unit(Unit.SQUARE_METRE) < other.as_unit(Unit.SQUARE_METRE)

    def __le__(self, other: "Area") -> bool:
        """Return whether the area is less than or equal to the other."""
        return self.as_unit(Unit.SQUARE_METRE) <= other.as_unit(Unit.SQUARE_METRE)

    def __gt__(self, other: "Area") -> bool:
        """Return whether the area is greater than the other."""
        return self.as_unit(Unit.SQUARE_METRE) > other.as_unit(Unit.SQUARE_METRE)

    def __ge__(self, other: "Area") -> bool:
        """Return whether the area is greater than or equal to the other."""
        return self.as_unit(Unit.SQUARE_METRE) >= other.as_unit(Unit.SQUARE_METRE)

    def __hash__(self) -> int:
        """Return the hash of the area.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.SQUARE_METRE))

    def __str__(self) -> str:
        """Return a string representation of the area."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the area for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
