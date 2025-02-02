"""Module for volume constants."""

from typing import Final

from .unit import Unit
from .volume import Volume

ZERO: Final = Volume(0, Unit.CUBIC_METER)
