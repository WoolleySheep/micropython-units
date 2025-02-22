"""Module for the volume unit info class."""

from .unit import Unit


class UnitInfo:
    """Information associated with a volume particular unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit: Unit,
        name: str,
        abbreviation: str,
        unit_delta_per_cubic_meter: float,
    ) -> None:
        """Initialise a collection of info associated with a unit."""
        self._unit = unit
        self._name = name
        self._abbreviation = abbreviation
        self._unit_delta_per_cubic_meter = unit_delta_per_cubic_meter

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
    def unit_delta_per_pascal(self) -> float:
        """The change in volume expressed as the unit per 1m^3.

        Equivalent to the gradient of the cubic-meter-vs-unit graph.
        """
        return self._unit_delta_per_cubic_meter
