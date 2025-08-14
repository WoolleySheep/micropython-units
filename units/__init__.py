"""Package for physical quantity modules and classes."""

from .units_inner.flow_rate import MassFlowRate, VolumetricFlowRate
from .units_inner.length import Length, LengthDelta, NegativeLengthValueError
from .units_inner.length import Unit as DistanceUnit
from .units_inner.linear_motion import Acceleration, Displacement, Velocity
from .units_inner.mass import Mass, MassDelta, NegativeMassValueError
from .units_inner.mass import Unit as MassUnit
from .units_inner.pressure import NegativePressureValueError, Pressure, PressureDelta
from .units_inner.pressure import Unit as PressureUnit
from .units_inner.temperature import (
    BelowAbsoluteZeroError,
    Temperature,
    TemperatureDelta,
)
from .units_inner.temperature import Unit as TemperatureUnit
from .units_inner.time import NegativeTimeValueError, Time, TimeDelta
from .units_inner.time import Unit as TimeUnit
from .units_inner.volume import NegativeVolumeValueError, Volume, VolumeDelta
from .units_inner.volume import Unit as VolumeUnit

__all__ = [
    "Acceleration",
    "BelowAbsoluteZeroError",
    "Displacement",
    "DistanceUnit",
    "Length",
    "LengthDelta",
    "Mass",
    "MassDelta",
    "MassFlowRate",
    "MassUnit",
    "NegativeLengthValueError",
    "NegativeMassValueError",
    "NegativePressureValueError",
    "NegativeTimeValueError",
    "NegativeVolumeValueError",
    "Pressure",
    "PressureDelta",
    "PressureUnit",
    "Temperature",
    "TemperatureDelta",
    "TemperatureUnit",
    "Time",
    "TimeDelta",
    "TimeUnit",
    "Velocity",
    "Volume",
    "VolumeDelta",
    "VolumeUnit",
    "VolumetricFlowRate",
    "flow_rate",  # pyright: ignore[reportUnsupportedDunderAll]
    "length",  # pyright: ignore[reportUnsupportedDunderAll]
    "linear_motion",  # pyright: ignore[reportUnsupportedDunderAll]
    "pressure",  # pyright: ignore[reportUnsupportedDunderAll]
    "temperature",  # pyright: ignore[reportUnsupportedDunderAll]
    "time",  # pyright: ignore[reportUnsupportedDunderAll]
    "volume",  # pyright: ignore[reportUnsupportedDunderAll]
]
