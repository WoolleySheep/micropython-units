"""Module for pressure constants."""

from typing import Final

from .pressure import Pressure
from .unit import STANDARD_ATMOSPHERIC_PRESSURE_AS_PASCAL, Unit

ABSOLUTE_ZERO: Final = Pressure(0, Unit.PASCAL)
STANDARD_ATMOSPHERE: Final = Pressure(
    STANDARD_ATMOSPHERIC_PRESSURE_AS_PASCAL, Unit.PASCAL
)
