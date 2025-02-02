import unittest

from units import TimeUnit, time


class ZeroTest(unittest.TestCase):
    """Unit tests for zero time."""

    def test_zero_time_value(self):
        self.assertAlmostEqual(0, time.ZERO.as_unit(TimeUnit.SECOND))
