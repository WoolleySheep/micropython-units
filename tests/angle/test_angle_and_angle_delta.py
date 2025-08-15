import unittest

from units import Angle, AngleDelta, AngleUnit


class AngleAndAngleDeltaTest(unittest.TestCase):
    """Unit tests for interactions between angle and angle delta classes."""

    def test_add_angle_delta_to_angle_produces_angle(self) -> None:
        angle = Angle(0, AngleUnit.RADIAN)
        delta = AngleDelta(1, AngleUnit.RADIAN)
        new_angle_left_add = angle + delta
        new_angle_right_add = delta + angle
        self.assertIsInstance(new_angle_left_add, Angle)
        self.assertAlmostEqual(1, new_angle_left_add.as_unit(AngleUnit.RADIAN))
        self.assertIsInstance(new_angle_right_add, Angle)
        self.assertAlmostEqual(1, new_angle_right_add.as_unit(AngleUnit.RADIAN))

    def test_subtract_angle_delta_from_angle_produces_angle(
        self,
    ) -> None:
        angle = Angle(1, AngleUnit.RADIAN)
        delta = AngleDelta(1, AngleUnit.RADIAN)
        new_angle = angle - delta
        self.assertIsInstance(new_angle, Angle)
        self.assertAlmostEqual(0, new_angle.as_unit(AngleUnit.RADIAN))

    def test_subtract_angle_from_angle_produces_angle_delta(
        self,
    ) -> None:
        angle1 = Angle(3, AngleUnit.RADIAN)
        angle2 = Angle(2, AngleUnit.RADIAN)
        new_angle_delta = angle1 - angle2
        self.assertIsInstance(new_angle_delta, AngleDelta)
        self.assertAlmostEqual(1, new_angle_delta.as_unit(AngleUnit.RADIAN))
