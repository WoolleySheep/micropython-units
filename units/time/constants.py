"""Module for time constants."""

from typing import Final

from .time import Time
from .unit import Unit

ZERO: Final = Time(0, Unit.SECOND)
