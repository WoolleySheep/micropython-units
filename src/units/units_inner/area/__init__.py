"""Package for area-related classes and constants."""

from .area import Area
from .area_delta import AreaDelta
from .constants import ZERO
from .exceptions import NegativeAreaValueError
from .unit import Unit, get_unit_delta_per_square_metre
from .unit import get_abbreviation as get_unit_abbreviation
from .unit import get_name as get_unit_name

__all__ = [
    "ZERO",
    "Area",
    "AreaDelta",
    "NegativeAreaValueError",
    "Unit",
    "get_unit_abbreviation",
    "get_unit_delta_per_square_metre",
    "get_unit_name",
]
