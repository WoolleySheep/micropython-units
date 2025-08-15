import math
import unittest

from src.units import Angle, AngleUnit


class AngleTest(unittest.TestCase):
    """Unit tests for angle class."""

    def test_create_angle(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Angle(1, AngleUnit.RADIAN)

    def test_angle_maps_within_range(self) -> None:
        for value, expected_value in [
            (-2.5 * math.pi, 1.5 * math.pi),
            (-2 * math.pi, 0),
            (-1.5 * math.pi, 0.5 * math.pi),
            (-math.pi, math.pi),
            (-0.5 * math.pi, 1.5 * math.pi),
            (0, 0),
            (0.5 * math.pi, 0.5 * math.pi),
            (math.pi, math.pi),
            (1.5 * math.pi, 1.5 * math.pi),
            (2 * math.pi, 0),
            (2.5 * math.pi, 0.5 * math.pi),
            (3 * math.pi, math.pi),
            (3.5 * math.pi, 1.5 * math.pi),
            (4 * math.pi, 0),
            (4.5 * math.pi, 0.5 * math.pi),
        ]:
            with self.subTest(value=value, expected_value=expected_value):
                self.assertAlmostEqual(
                    expected_value,
                    Angle(value, AngleUnit.RADIAN).as_unit(AngleUnit.RADIAN),
                )

    def test_get_angle_value_as_unit(self) -> None:
        angle = Angle(math.pi, AngleUnit.RADIAN)

        for unit, expected_value in [
            (AngleUnit.RADIAN, math.pi),
            (AngleUnit.DEGREE, 180),
            (AngleUnit.REVOLUTION, 0.5),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, angle.as_unit(unit))

    def test_compare_angles(self) -> None:
        for (
            angle1,
            angle2,
            is_equal,
            is_not_equal,
        ) in [
            (
                Angle(0, AngleUnit.RADIAN),
                Angle(0, AngleUnit.RADIAN),
                True,
                False,
            ),
            (
                Angle(0, AngleUnit.RADIAN),
                Angle(1, AngleUnit.RADIAN),
                False,
                True,
            ),
            (
                Angle(1, AngleUnit.RADIAN),
                Angle(0, AngleUnit.RADIAN),
                False,
                True,
            ),
        ]:
            with self.subTest(
                angle1=angle1,
                angle2=angle2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
            ):
                self.assertEqual(is_equal, angle1 == angle2)
                self.assertEqual(is_not_equal, angle1 != angle2)
