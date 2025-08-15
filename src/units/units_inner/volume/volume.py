"""Module for the volume class."""

from typing import overload

from .exceptions import NegativeVolumeValueError
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_cubic_metre,
)
from .volume_delta import VolumeDelta


class Volume:
    """The measure of a three-dimensional space."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new volume.

        Raises:
            NegativeVolumeValueError: The negative value produced a volume less than
                0m^3.
        """
        if value < 0:
            raise NegativeVolumeValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Return the volume, expressed as the unit."""
        internal_unit_delta_per_cubic_metre = get_unit_delta_per_cubic_metre(self._unit)
        value_as_cubic_metre = self._value / internal_unit_delta_per_cubic_metre
        external_unit_delta_per_cubic_metre = get_unit_delta_per_cubic_metre(unit)
        return external_unit_delta_per_cubic_metre * value_as_cubic_metre

    def __add__(self, delta: VolumeDelta) -> "Volume":
        """Return the sum of the volume and the difference.

        Raises:
            NegativeVolumeValueError: The sum of the volume and the difference was less
                than 0m^3.
        """
        value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
        delta_value_as_cubic_metre = delta.as_unit(Unit.CUBIC_METRE)
        value_sum_as_cubic_metre = value_as_cubic_metre + delta_value_as_cubic_metre
        return Volume(value_sum_as_cubic_metre, Unit.CUBIC_METRE)

    def __radd__(self, delta: VolumeDelta) -> "Volume":
        """Return the sum of the volume and the difference."""
        return self + delta

    @overload
    def __sub__(self, other: "Volume") -> VolumeDelta: ...

    @overload
    def __sub__(self, other: VolumeDelta) -> "Volume": ...

    def __sub__(self, other: "Volume | VolumeDelta") -> "VolumeDelta | Volume":
        """Return the delta between volumes or the volume less the delta.

        The behaviour depends upon the type of the argument.

        - If the argument is a :py:class:`Volume`, return the difference between the two
          volumes.
        - If the argument is a :py:class:`VolumeDelta`, return the volume less the
          difference.

        Raises:
            NegativeVolumeValueError: The volume minus the difference was less
                than 0m^3. Error can only be raised when other is a
                :py:class:`VolumeDelta`.
        """
        value_as_cubic_metre = self.as_unit(Unit.CUBIC_METRE)
        other_value_as_cubic_metre = other.as_unit(Unit.CUBIC_METRE)
        value_difference_as_cubic_metre = (
            value_as_cubic_metre - other_value_as_cubic_metre
        )
        return (
            VolumeDelta(value_difference_as_cubic_metre, Unit.CUBIC_METRE)
            if isinstance(other, Volume)
            else Volume(value_difference_as_cubic_metre, Unit.CUBIC_METRE)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal volumes."""
        if not isinstance(other, Volume):
            return NotImplemented

        return self.as_unit(Unit.CUBIC_METRE) == other.as_unit(Unit.CUBIC_METRE)

    def __lt__(self, other: "Volume") -> bool:
        """Return whether the volume is less than the other."""
        return self.as_unit(Unit.CUBIC_METRE) < other.as_unit(Unit.CUBIC_METRE)

    def __le__(self, other: "Volume") -> bool:
        """Return whether the volume is less than or equal to the other."""
        return self.as_unit(Unit.CUBIC_METRE) <= other.as_unit(Unit.CUBIC_METRE)

    def __gt__(self, other: "Volume") -> bool:
        """Return whether the volume is greater than the other."""
        return self.as_unit(Unit.CUBIC_METRE) > other.as_unit(Unit.CUBIC_METRE)

    def __ge__(self, other: "Volume") -> bool:
        """Return whether the volume is greater than or equal to the other."""
        return self.as_unit(Unit.CUBIC_METRE) >= other.as_unit(Unit.CUBIC_METRE)

    def __hash__(self) -> int:
        """Return the hash of the volume."""
        return hash(self.as_unit(Unit.CUBIC_METRE))

    def __str__(self) -> str:
        """Return a string representation of the volume."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the volume for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
