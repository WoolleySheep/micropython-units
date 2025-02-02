"""Module for volumetric flow rate exceptions."""

from typing import Any


class ZeroTimeIntervalDivisionError(ValueError):
    """Raised when the time interval over which the volume changed is zero.

    A zero time interval would produce an infinite flow rate,
    which is physically impossible.
    """

    def __init__(
        self,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> None:
        """Initialise a new zero time interval exception."""
        super().__init__(
            "Time difference over which volume changes cannot be zero.",
            *args,
            **kwargs,
        )
