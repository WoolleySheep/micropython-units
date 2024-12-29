"""Module for the negative pressure value exception."""


class NegativePressureValueError(ValueError):
    """Raised when the pressure value is negative.

    The minimum pressure that can exist is a perfect vacuum (0 Pa),
    so a pressure with a negative value, regardless of the unit, is impossible.
    """

    def __init__(self, value: float):
        self._value = value
        super().__init__(
            (
                f"Pressure value [{value}] cannot be negative, "
                "as this would produce a lower pressure than a perfect vacuum."
            )
        )

    @property
    def value(self) -> float:
        """The pressure value that caused the error."""
        return self._value
