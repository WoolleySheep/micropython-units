import unittest

from units import DistanceUnit, length


class ZeroTest(unittest.TestCase):
    """Unit tests for zero length."""

    def test_zero_length_value(self):
        self.assertAlmostEqual(0, length.ZERO.as_unit(DistanceUnit.METRE))
