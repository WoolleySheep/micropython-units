import unittest

from src.units import MassUnit, mass


class ZeroTest(unittest.TestCase):
    """Unit tests for zero mass."""

    def test_zero_mass_value(self):
        self.assertAlmostEqual(0, mass.ZERO.as_unit(MassUnit.KILOGRAM))
