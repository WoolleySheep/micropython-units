import unittest

from units import CurrentUnit, current


class ZeroTest(unittest.TestCase):
    """Unit tests for zero current."""

    def test_zero_current_value(self):
        self.assertAlmostEqual(0, current.ZERO.as_unit(CurrentUnit.AMPERE))
