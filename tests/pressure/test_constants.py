import unittest

from src.units import PressureUnit, pressure


class PerfectVacuumTest(unittest.TestCase):
    """Unit tests for perfect vacuum pressure."""

    def test_perfect_vacuum_value(self):
        self.assertAlmostEqual(0, pressure.PERFECT_VACUUM.as_unit(PressureUnit.PASCAL))


class StandardAtmosphereTest(unittest.TestCase):
    """Unit tests for standard atmospheric pressure."""

    def test_standard_atmosphere_value(self):
        """Test the standard atmosphere value."""
        self.assertAlmostEqual(
            101_325, pressure.STANDARD_ATMOSPHERE.as_unit(PressureUnit.PASCAL)
        )
