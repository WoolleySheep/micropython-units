"""Module for area exceptions."""

from typing import Any


class NegativeAreaValueError(ValueError):
    """Raised when the area value is negative.

    The minimum area that can exist is 0 m^2,
    so an area with a negative value, regardless of the unit, is impossible.
    """

    def __init__(
        self,
        value: float,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new negative-area exception."""
        self._value = value
        super().__init__(
            f"Area value [{value}] cannot be negative.",
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The area value that caused the error."""
        return self._value
