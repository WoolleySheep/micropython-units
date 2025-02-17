"""Module for pressure exceptions."""

from typing import Any


class NegativePressureValueError(ValueError):
    """Raised when the pressure value is negative.

    The minimum pressure that can exist is a perfect vacuum (0 Pa),
    so a pressure with a negative value, regardless of the unit, is impossible.
    """

    def __init__(
        self,
        value: float,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new negative-pressure exception."""
        self._value = value
        super().__init__(
            (
                f"Pressure value [{value}] cannot be negative, "
                "as this would produce a lower pressure than a perfect vacuum."
            ),
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The pressure value that caused the error."""
        return self._value
