"""Module for the time class."""

from typing import overload

from .exceptions import NegativeLengthValueError
from .length_delta import LengthDelta
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_metre,
)


class Length:
    """The measure of distance."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new length.

        Raises:
            NegativeLengthValueError: The negative value produced a length less than 0m.
        """
        if value < 0:
            raise NegativeLengthValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the length, expressed as the unit."""
        internal_unit_delta_per_metre = get_unit_delta_per_metre(self._unit)
        value_as_metre = self._value / internal_unit_delta_per_metre
        external_unit_delta_per_metre = get_unit_delta_per_metre(unit)
        return external_unit_delta_per_metre * value_as_metre

    def __add__(self, delta: LengthDelta) -> "Length":
        """Return the sum of the length and the difference.

        Raises:
            NegativeLengthValueError: The sum of the length and the difference was less
                than 0m.
        """
        value_as_metre = self.as_unit(Unit.METRE)
        delta_value_as_metre = delta.as_unit(Unit.METRE)
        value_sum_as_metre = value_as_metre + delta_value_as_metre
        return Length(value_sum_as_metre, Unit.METRE)

    def __radd__(self, delta: LengthDelta) -> "Length":
        """Return the sum of the length and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Length") -> LengthDelta: ...

    @overload
    def __sub__(self, other: LengthDelta) -> "Length": ...

    def __sub__(self, other: "Length | LengthDelta") -> "LengthDelta | Length":
        """Return the delta between lengths or the length less the delta.

        The behaviour depends upon the type of the argument.

        - If the argument is a :py:class:`Length`, return the difference between the two
          lengths.
        - If the argument is a :py:class:`LengthDelta`, return the length less the
          difference.

        Raises:
            NegativeLengthValueError: The length minus the difference was less
                than 0m. Error can only be raised when other is a
                :py:class:`LengthDelta`.
        """
        value_as_metre = self.as_unit(Unit.METRE)
        other_value_as_metre = other.as_unit(Unit.METRE)
        value_difference_as_metre = value_as_metre - other_value_as_metre
        return (
            LengthDelta(value_difference_as_metre, Unit.METRE)
            if isinstance(other, Length)
            else Length(value_difference_as_metre, Unit.METRE)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal lengths."""
        if not isinstance(other, Length):
            return NotImplemented

        return self.as_unit(Unit.METRE) == other.as_unit(Unit.METRE)

    def __lt__(self, other: "Length") -> bool:
        """Return whether the length is less than the other."""
        return self.as_unit(Unit.METRE) < other.as_unit(Unit.METRE)

    def __le__(self, other: "Length") -> bool:
        """Return whether the length is less than or equal to the other."""
        return self.as_unit(Unit.METRE) <= other.as_unit(Unit.METRE)

    def __gt__(self, other: "Length") -> bool:
        """Return whether the length is greater than the other."""
        return self.as_unit(Unit.METRE) > other.as_unit(Unit.METRE)

    def __ge__(self, other: "Length") -> bool:
        """Return whether the length is greater than or equal to the other."""
        return self.as_unit(Unit.METRE) >= other.as_unit(Unit.METRE)

    def __hash__(self) -> int:
        """Return the hash of the length."""
        return hash(self.as_unit(Unit.METRE))

    def __str__(self) -> str:
        """Return a string representation of the length."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the length for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
