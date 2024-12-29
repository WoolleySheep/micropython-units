import unittest

from units import PressureUnit, pressure


class AbsoluteZeroTest(unittest.TestCase):
    """Unit tests for absolute zero pressure."""

    def test_absolute_zero_value(self):
        """Test the absolute zero value."""
        self.assertAlmostEqual(0, pressure.ABSOLUTE_ZERO.as_unit(PressureUnit.PASCAL))


class StandardAtmosphereTest(unittest.TestCase):
    """Unit tests for standard atmospheric pressure."""

    def test_standard_atmosphere_value(self):
        """Test the standard atmosphere value."""
        self.assertAlmostEqual(
            101_325, pressure.STANDARD_ATMOSPHERE.as_unit(PressureUnit.PASCAL)
        )
