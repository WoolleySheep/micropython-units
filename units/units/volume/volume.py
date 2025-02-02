"""Module for the volume class."""

from typing import overload

from .exceptions import NegativeVolumeValueError
from .unit import (
    Unit,
    get_abbreviation,
    get_name,
    get_unit_delta_per_cubic_meter,
)
from .volume_delta import VolumeDelta


class Volume:
    """The measure of a three-dimensional space."""

    def __init__(self, value: float, unit: Unit) -> None:
        """Initialise a new volume."""
        if value < 0:
            raise NegativeVolumeValueError(value=value)

        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the volume, expressed as the unit."""
        internal_unit_delta_per_cubic_meter = get_unit_delta_per_cubic_meter(self._unit)
        value_as_cubic_meter = self._value / internal_unit_delta_per_cubic_meter
        external_unit_delta_per_cubic_meter = get_unit_delta_per_cubic_meter(unit)
        return external_unit_delta_per_cubic_meter * value_as_cubic_meter

    def __add__(self, delta: VolumeDelta) -> "Volume":
        """Return the sum of the volume and the difference."""
        value_as_cubic_meter = self.as_unit(Unit.CUBIC_METER)
        delta_value_as_cubic_meter = delta.as_unit(Unit.CUBIC_METER)
        value_sum_as_cubic_meter = value_as_cubic_meter + delta_value_as_cubic_meter
        return Volume(value_sum_as_cubic_meter, Unit.CUBIC_METER)

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
        - If the argument is a volume, return the difference between the two
          volumes.
        - If the argument is a volume difference, return the volume less the
          difference.
        """
        value_as_cubic_meter = self.as_unit(Unit.CUBIC_METER)
        other_value_as_cubic_meter = other.as_unit(Unit.CUBIC_METER)
        value_difference_as_cubic_meter = (
            value_as_cubic_meter - other_value_as_cubic_meter
        )
        return (
            VolumeDelta(value_difference_as_cubic_meter, Unit.CUBIC_METER)
            if isinstance(other, Volume)
            else Volume(value_difference_as_cubic_meter, Unit.CUBIC_METER)
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal volumes."""
        return isinstance(other, Volume) and self.as_unit(
            Unit.CUBIC_METER,
        ) == other.as_unit(Unit.CUBIC_METER)

    def __lt__(self, other: "Volume") -> bool:
        """Return whether the volume is less than the other."""
        return self.as_unit(Unit.CUBIC_METER) < other.as_unit(Unit.CUBIC_METER)

    def __le__(self, other: "Volume") -> bool:
        """Return whether the volume is less than or equal to the other."""
        return self.as_unit(Unit.CUBIC_METER) <= other.as_unit(Unit.CUBIC_METER)

    def __gt__(self, other: "Volume") -> bool:
        """Return whether the volume is greater than the other."""
        return self.as_unit(Unit.CUBIC_METER) > other.as_unit(Unit.CUBIC_METER)

    def __ge__(self, other: "Volume") -> bool:
        """Return whether the volume is greater than or equal to the other."""
        return self.as_unit(Unit.CUBIC_METER) >= other.as_unit(Unit.CUBIC_METER)

    def __hash__(self) -> int:
        """Return the hash of the volume.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(Unit.CUBIC_METER))

    def __str__(self) -> str:
        """Return a string representation of the volume."""
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        """Return a string representation of the volume for developers."""
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
