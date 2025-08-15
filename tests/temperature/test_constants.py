import unittest

from src.units import TemperatureUnit, temperature


class AbsoluteZeroTest(unittest.TestCase):
    """Unit tests for absolute zero temperature."""

    def test_absolute_zero_value(self):
        self.assertAlmostEqual(
            0, temperature.ABSOLUTE_ZERO.as_unit(TemperatureUnit.KELVIN)
        )
