"""Module for the temperature unit enum."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enum import IntEnum
else:
    IntEnum = object


# NB: When adding a new unit, be sure to add it to the info list in helpers.py
class Unit(IntEnum):
    """A temperature unit.

    NB: Micropython does not yet support enums. The desired behaviour
    (enumerated options embedded in the type system) can be mostly
    replicated by substituting IntEnum for object at runtime, which
    is what has been done here.
    """

    CELSIUS = 1
    KELVIN = 2
    FAHRENHEIT = 3
