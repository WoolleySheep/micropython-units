"""Module for the volumetric flow rate class."""

# ruff: noqa: TID252

from typing import overload

from ..time import TimeDelta
from ..time import Unit as TimeUnit
from ..time import get_unit_abbreviation as get_time_unit_abbreviation
from ..time import get_unit_delta_per_second as get_time_unit_delta_per_second
from ..time import get_unit_name as get_time_unit_name
from ..volume import Unit as VolumeUnit
from ..volume import VolumeDelta
from ..volume import get_unit_abbreviation as get_volume_unit_abbreviation
from ..volume import (
    get_unit_delta_per_cubic_meter as get_volume_unit_delta_per_cubic_meter,
)
from ..volume import get_unit_name as get_volume_unit_name
from .exceptions import ZeroTimeIntervalDivisionError


class VolumetricFlowRate:
    """The volume of a gas or liquid that flows in a certain amount of time."""

    @classmethod
    def from_quantities(
        cls, volume: VolumeDelta, time: TimeDelta
    ) -> "VolumetricFlowRate":
        """Return a flow rate given a change in volume over an interval of time."""
        value_in_cubic_meter = volume.as_unit(VolumeUnit.CUBIC_METER)
        value_in_second = time.as_unit(TimeUnit.SECOND)
        try:
            value = value_in_cubic_meter / value_in_second
        except ZeroDivisionError as e:
            raise ZeroTimeIntervalDivisionError from e
        return cls(value, VolumeUnit.CUBIC_METER, TimeUnit.SECOND)

    def __init__(
        self, value: float, volume_unit: VolumeUnit, time_unit: TimeUnit
    ) -> None:
        """Initialise a new flow rate."""
        self._value = value
        self._volume_unit = volume_unit
        self._time_unit = time_unit

    def as_unit(self, volume_unit: VolumeUnit, time_unit: TimeUnit) -> float:
        """Return the flow rate in the specified units."""
        internal_volume_unit_delta_per_cubic_meter = (
            get_volume_unit_delta_per_cubic_meter(self._volume_unit)
        )
        internal_time_unit_delta_per_second = get_time_unit_delta_per_second(
            self._time_unit
        )
        internal_unit_to_cubic_meter_per_second_factor = (
            internal_time_unit_delta_per_second
            / internal_volume_unit_delta_per_cubic_meter
        )
        value_as_cubic_meter_per_second = (
            internal_unit_to_cubic_meter_per_second_factor * self._value
        )
        external_volume_unit_delta_per_cubic_meter = (
            get_volume_unit_delta_per_cubic_meter(volume_unit)
        )
        external_time_unit_delta_per_second = get_time_unit_delta_per_second(time_unit)
        cubic_meter_per_second_to_internal_unit_factor = (
            external_volume_unit_delta_per_cubic_meter
            / external_time_unit_delta_per_second
        )
        return (
            cubic_meter_per_second_to_internal_unit_factor
            * value_as_cubic_meter_per_second
        )

    def __mul__(self, value: float) -> "VolumetricFlowRate":
        """Return a flow rate scaled by the value."""
        scaled_value = self._value * value
        return VolumetricFlowRate(scaled_value, self._volume_unit, self._time_unit)

    def __rmul__(self, value: float) -> "VolumetricFlowRate":
        """Return a flow rate scaled by the value."""
        return self * value

    @overload
    def __truediv__(self, other: float) -> "VolumetricFlowRate": ...

    @overload
    def __truediv__(self, other: "VolumetricFlowRate") -> float: ...

    def __truediv__(
        self, other: "float | VolumetricFlowRate"
    ) -> "VolumetricFlowRate | float":
        """Return a scaled flow rate or the ratio between the flow rates.

        The behaviour depends upon the type of the argument.
        - If the argument is scalar, return a flow rate scaled by the
          inverse of the value
        - If the argument is a flow rate, return the ratio between the two
          flow rates
        """
        if isinstance(other, VolumetricFlowRate):
            value_as_cubic_meter_per_second = self.as_unit(
                VolumeUnit.CUBIC_METER, TimeUnit.SECOND
            )
            other_value_as_cubic_meter_per_second = other.as_unit(
                VolumeUnit.CUBIC_METER, TimeUnit.SECOND
            )
            return (
                value_as_cubic_meter_per_second / other_value_as_cubic_meter_per_second
            )

        return (1 / other) * self

    def __add__(self, other: "VolumetricFlowRate") -> "VolumetricFlowRate":
        """Return the sum of two flow rates."""
        value_as_cubic_meter_per_second = self.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        other_value_as_cubic_meter_per_second = other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        value_sum_as_cubic_meter_per_second = (
            value_as_cubic_meter_per_second + other_value_as_cubic_meter_per_second
        )
        return VolumetricFlowRate(
            value_sum_as_cubic_meter_per_second, VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )

    def __sub__(self, other: "VolumetricFlowRate") -> "VolumetricFlowRate":
        """Return the difference of two flow rates."""
        value_as_cubic_meter_per_second = self.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        other_value_as_cubic_meter_per_second = other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        value_difference_as_cubic_meter_per_second = (
            value_as_cubic_meter_per_second - other_value_as_cubic_meter_per_second
        )
        return VolumetricFlowRate(
            value_difference_as_cubic_meter_per_second,
            VolumeUnit.CUBIC_METER,
            TimeUnit.SECOND,
        )

    def __neg__(self) -> "VolumetricFlowRate":
        """Return the inverse of the flow rate."""
        return -1 * self

    def __abs__(self) -> "VolumetricFlowRate":
        """Return the absolute version of the flow rate."""
        absolute_value = abs(self._value)
        return VolumetricFlowRate(absolute_value, self._volume_unit, self._time_unit)

    def __floordiv__(self, other: "VolumetricFlowRate") -> float:
        """Return the floored ratio between the flow rates."""
        value_as_cubic_meter_per_second = self.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        other_value_as_cubic_meter_per_second = other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        return value_as_cubic_meter_per_second // other_value_as_cubic_meter_per_second

    def __mod__(self, other: "VolumetricFlowRate") -> float:
        """Return the remainder of the ratio between the flow rate."""
        value_as_cubic_meter_per_second = self.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        other_value_as_cubic_meter_per_second = other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        return value_as_cubic_meter_per_second % other_value_as_cubic_meter_per_second

    def __divmod__(self, other: "VolumetricFlowRate") -> tuple[float, float]:
        """Return the quotient & remainder of the ratio between the flow rates."""
        value_as_cubic_meter_per_second = self.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        other_value_as_cubic_meter_per_second = other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )
        return divmod(
            value_as_cubic_meter_per_second, other_value_as_cubic_meter_per_second
        )

    def __eq__(self, other: object) -> bool:
        """Return whether the objects are equal flow rates."""
        return isinstance(other, VolumetricFlowRate) and self.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        ) == other.as_unit(VolumeUnit.CUBIC_METER, TimeUnit.SECOND)

    def __lt__(self, other: "VolumetricFlowRate") -> bool:
        """Return whether the flow rate is less than the other."""
        return self.as_unit(VolumeUnit.CUBIC_METER, TimeUnit.SECOND) < other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )

    def __le__(self, other: "VolumetricFlowRate") -> bool:
        """Return whether the flow rate is less than or equal to the other."""
        return self.as_unit(VolumeUnit.CUBIC_METER, TimeUnit.SECOND) <= other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )

    def __gt__(self, other: "VolumetricFlowRate") -> bool:
        """Return whether the flow rate is greater than the other."""
        return self.as_unit(VolumeUnit.CUBIC_METER, TimeUnit.SECOND) > other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )

    def __ge__(self, other: "VolumetricFlowRate") -> bool:
        """Return whether the flow rate is greater than or equal to the other."""
        return self.as_unit(VolumeUnit.CUBIC_METER, TimeUnit.SECOND) >= other.as_unit(
            VolumeUnit.CUBIC_METER, TimeUnit.SECOND
        )

    def __hash__(self) -> int:
        """Return the hash of the flow rate.

        NB: Exercise the usual caution around a hash of a floating point number.
        """
        return hash(self.as_unit(VolumeUnit.CUBIC_METER, TimeUnit.SECOND))

    def __str__(self) -> str:
        """Return a string representation of the flow rate."""
        return (
            f"{self._value} "
            f"{get_volume_unit_abbreviation(self._volume_unit)}/"
            f"{get_time_unit_abbreviation(self._time_unit)}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the volume for developers."""
        return (
            f"{__class__.__name__}({self._value},"
            f" {get_volume_unit_name(self._volume_unit)},"
            f" {get_time_unit_name(self._time_unit)})"
        )
