"""Module for linear distance exceptions."""

from typing import Any


class NegativeLengthValueError(ValueError):
    """Raised when the length value is negative.

    The minimum length that can exist is 0m,
    so a length with a negative value, regardless of the unit, is impossible.
    """

    def __init__(
        self,
        value: float,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new negative-length exception."""
        self._value = value
        super().__init__(
            f"Length value [{value}] cannot be negative.",
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The length value that caused the error."""
        return self._value
