"""Module for time exceptions."""

from typing import Any


class NegativeTimeValueError(ValueError):
    """Raised when the time value is negative.

    The minimum volume that can exist is 0s,
    so a time with a negative value, regardless of the unit, is impossible.
    """

    def __init__(
        self,
        value: float,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new negative-time exception."""
        self._value = value
        super().__init__(
            f"Time value [{value}] cannot be negative.",
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The time value that caused the error."""
        return self._value
