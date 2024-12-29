"""Module for the temperature difference class."""

from typing import overload

from .unit import (
    Unit,
    get_abbreviation,
    get_kelvin_to_unit_conversion_parameters,
    get_name,
)


class TemperatureDelta:
    """The difference between two temperatures."""

    def __init__(self, value: float, unit: Unit) -> None:
        self._value = value
        self._unit = unit

    def as_unit(self, unit: Unit) -> float:
        """Get the temperature difference, expressed as the unit."""
        internal_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            self._unit
        )

        value_as_kelvin = (
            self._value
            / internal_unit_conversion_parameters.unit_delta_per_degree_kelvin
        )

        external_unit_conversion_parameters = get_kelvin_to_unit_conversion_parameters(
            unit
        )
        return (
            external_unit_conversion_parameters.unit_delta_per_degree_kelvin
            * value_as_kelvin
        )

    def __mul__(self, multiplier: float) -> "TemperatureDelta":
        scaled_value = self._value * multiplier
        return TemperatureDelta(scaled_value, self._unit)

    def __rmul__(self, value: float) -> "TemperatureDelta":
        return self * value

    @overload
    def __truediv__(self, other: float) -> "TemperatureDelta": ...

    @overload
    def __truediv__(self, other: "TemperatureDelta") -> float: ...

    def __truediv__(
        self, other: "float | TemperatureDelta"
    ) -> "TemperatureDelta | float":
        if isinstance(other, TemperatureDelta):
            value_as_kelvin = self.as_unit(Unit.KELVIN)
            other_value_as_kelvin = other.as_unit(Unit.KELVIN)
            return value_as_kelvin / other_value_as_kelvin

        scaled_value = self._value / other
        return TemperatureDelta(scaled_value, self._unit)

    def __add__(self, other: "TemperatureDelta") -> "TemperatureDelta":
        # This is here because the case of a TemperatureDelta + a Temperature is
        # handled in the __radd__ method in the Temperature class, otherwise it
        # runs into problems with circular imports
        if not isinstance(other, TemperatureDelta):  # type: ignore[reportUnnecessaryIsInstance]
            return NotImplemented

        value_as_kelvin = self.as_unit(Unit.KELVIN)
        delta_value_as_kelvin = other.as_unit(Unit.KELVIN)
        added_value_as_kelvin = value_as_kelvin + delta_value_as_kelvin
        return TemperatureDelta(added_value_as_kelvin, Unit.KELVIN)

    def __sub__(self, delta: "TemperatureDelta") -> "TemperatureDelta":
        return self + (-delta)

    def __neg__(self) -> "TemperatureDelta":
        inverted_value = -self._value
        return TemperatureDelta(inverted_value, self._unit)

    def __abs__(self) -> "TemperatureDelta":
        absolute_value = abs(self._value)
        return TemperatureDelta(absolute_value, self._unit)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TemperatureDelta) and self.as_unit(
            Unit.KELVIN
        ) == other.as_unit(Unit.KELVIN)

    def __lt__(self, other: "TemperatureDelta") -> bool:
        return self.as_unit(Unit.KELVIN) < other.as_unit(Unit.KELVIN)

    def __le__(self, other: "TemperatureDelta") -> bool:
        return self.as_unit(Unit.KELVIN) <= other.as_unit(Unit.KELVIN)

    def __gt__(self, other: "TemperatureDelta") -> bool:
        return self.as_unit(Unit.KELVIN) > other.as_unit(Unit.KELVIN)

    def __ge__(self, other: "TemperatureDelta") -> bool:
        return self.as_unit(Unit.KELVIN) >= other.as_unit(Unit.KELVIN)

    def __str__(self) -> str:
        return f"{self._value} {get_abbreviation(self._unit)}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self._value}, {get_name(self._unit)})"
