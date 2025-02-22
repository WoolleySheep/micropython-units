"""Module for the temperature unit conversion parameters class."""


class UnitConversionParameters:
    """Parameters required to convert a value from kelvin to a unit.

    Not intended for public use.
    """

    def __init__(
        self,
        unit_delta_per_degree_kelvin: float,
        absolute_zero_offset: float,
    ) -> None:
        """Initialise a new pair of conversion parameters."""
        self._unit_delta_per_degree_kelvin = unit_delta_per_degree_kelvin
        self._absolute_zero_offset = absolute_zero_offset

    @property
    def unit_delta_per_degree_kelvin(self) -> float:
        """The change in temperature expressed as the unit per 1 degree K.

        Equivalent to the gradient of the kelvin-vs-unit graph.
        """
        return self._unit_delta_per_degree_kelvin

    @property
    def absolute_zero_offset(self) -> float:
        """The temperature expressed as the unit at absolute zero.

        Equivalent to the y-intercept of the kelvin-vs-unit graph.
        """
        return self._absolute_zero_offset
