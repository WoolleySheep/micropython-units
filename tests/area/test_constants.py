import unittest

from src.units import AreaUnit, area


class ZeroTest(unittest.TestCase):
    """Unit tests for zero area."""

    def test_zero_area_value(self):
        self.assertAlmostEqual(0, area.ZERO.as_unit(AreaUnit.SQUARE_METRE))
