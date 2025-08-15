"""Module for voltage constants."""

from typing import Final

from .unit import Unit
from .voltage import Voltage

ZERO: Final = Voltage(0, Unit.VOLT)
