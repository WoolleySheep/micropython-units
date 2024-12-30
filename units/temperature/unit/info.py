"""Module for the temperature unit info class."""

from .conversion_parameters import UnitConversionParameters
from .unit import Unit


class UnitInfo:
    """Information associated with a particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        conversion_parameters: UnitConversionParameters,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._conversion_parameters = conversion_parameters

    @property
    def unit(self) -> Unit:
        """The unit the information relates to."""
        return self._unit

    @property
    def name(self) -> str:
        """The name of the unit."""
        return self._name

    @property
    def abbreviation(self) -> str:
        """The abbreviation of the unit."""
        return self._abbreviation

    @property
    def conversion_parameters(self) -> UnitConversionParameters:
        """The conversion parameters associated with the unit."""
        return self._conversion_parameters
