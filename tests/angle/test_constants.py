import unittest

from units import AngleUnit, angle


class ZeroTest(unittest.TestCase):
    """Unit tests for zero angle."""

    def test_zero_angle_value(self) -> None:
        self.assertAlmostEqual(0, angle.ZERO.as_unit(AngleUnit.RADIAN))
