"""Module for the temperature unit conversion parameters class."""


class UnitConversionParameters:
    """Parameters required to convert a value from kelvin to a unit.

    Not intended for public use.
    """

    def __init__(
        self, unit_delta_per_degree_kelvin: float, absolute_zero_offset: float
    ) -> None:
        self._unit_delta_per_degree_kelvin = unit_delta_per_degree_kelvin
        self._absolute_zero_offset = absolute_zero_offset

    @property
    def unit_delta_per_degree_kelvin(self) -> float:
        return self._unit_delta_per_degree_kelvin

    @property
    def absolute_zero_offset(self) -> float:
        return self._absolute_zero_offset
