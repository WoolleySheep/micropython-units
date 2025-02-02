"""Module for the volume unit enum."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to also update:
# - The info list in helpers.py
# - The `test_get_X_value_as_unit` test in `test_X.py` and `test_X_delta.py`
class Unit(IntEnum):
    """A volume unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    CUBIC_METER = 1
    LITRE = 2
    MILLILITRE = 3
    MICROLITRE = 4
