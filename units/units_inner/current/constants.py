"""Module for current constants."""

from typing import Final

from .current import Current
from .unit import Unit

ZERO: Final = Current(0, Unit.AMPERE)
