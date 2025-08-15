"""Module for mass exceptions."""

from typing import Any


class NegativeMassValueError(ValueError):
    """Raised when the mass value is negative.

    The minimum mass that can exist is 0 kg,
    so a mass with a negative value, regardless of the unit, is impossible.
    """

    def __init__(
        self,
        value: float,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new negative-mass exception."""
        self._value = value
        super().__init__(
            f"Mass value [{value}] cannot be negative.",
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The mass value that caused the error."""
        return self._value
