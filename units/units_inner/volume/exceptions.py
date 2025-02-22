"""Module for volume exceptions."""

from typing import Any


class NegativeVolumeValueError(ValueError):
    """Raised when the volume value is negative.

    The minimum volume that can exist is 0 m^3,
    so a volume with a negative value, regardless of the unit, is impossible.
    """

    def __init__(
        self,
        value: float,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new negative-volume exception."""
        self._value = value
        super().__init__(
            f"Volume value [{value}] cannot be negative.",
            *args,
            **kwargs,
        )

    @property
    def value(self) -> float:
        """The volume value that caused the error."""
        return self._value
