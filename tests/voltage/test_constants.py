import unittest

from units import VoltageUnit, voltage


class ZeroTest(unittest.TestCase):
    """Unit tests for zero voltage."""

    def test_zero_voltage_value(self):
        self.assertAlmostEqual(0, voltage.ZERO.as_unit(VoltageUnit.VOLT))
