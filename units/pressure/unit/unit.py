"""Module for the pressure unit enum."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A pressure unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    PASCAL = 1
    POUND_PER_SQUARE_INCH = 2
    BAR = 3
    ATMOSPHERE = 4
    MILLIMETER_OF_MERCURY = 5
    KILOPASCAL = 6
    MILLIBAR = 7