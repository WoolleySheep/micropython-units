"""Module for the absolute zero temperature constant."""

from typing import Final

from .temperature import ABSOLUTE_ZERO_AS_KELVIN, Temperature
from .unit import Unit

ABSOLUTE_ZERO: Final = Temperature(ABSOLUTE_ZERO_AS_KELVIN, Unit.KELVIN)
