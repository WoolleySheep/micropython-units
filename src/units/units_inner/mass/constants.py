"""Module for mass constants."""

from typing import Final

from .mass import Mass
from .unit import Unit

ZERO: Final = Mass(0, Unit.KILOGRAM)
