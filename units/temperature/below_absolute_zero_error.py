"""Module for the below absolute zero exception."""

from typing import Any

from units.temperature.unit import Unit, get_abbreviation


class BelowAbsoluteZeroError(ValueError):
    """Raised when the temperature would be less than absolute zero.

    The minimum temperature that can exist is absolute zero (0 K),
    so a temperature less than this is impossible.
    """

    def __init__(
        self,
        value: float,
        unit: Unit,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ):
        self._value = value
        self._unit = unit
        super().__init__(
            (
                f"Temperature [{value} {get_abbreviation(unit)}] cannot exist, "
                "as this would be less than absolute zero (0 K)."
            ),
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The temperature value that caused the error."""
        return self._value

    @property
    def unit(self) -> Unit:
        """The temperature unit that caused the error."""
        return self._unit
