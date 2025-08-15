import math
import unittest

from src.units import AngleDelta, AngleUnit


class AngleDeltaTest(unittest.TestCase):
    """Unit tests for angle delta class."""

    def test_create_angle_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = AngleDelta(1, AngleUnit.RADIAN)

    def test_angle_delta_maps_within_range(self) -> None:
        for value, expected_value in [
            (-3.5 * math.pi, 0.5 * math.pi),
            (-3 * math.pi, -math.pi),
            (-2.5 * math.pi, -0.5 * math.pi),
            (-2 * math.pi, 0),
            (-1.5 * math.pi, 0.5 * math.pi),
            (-math.pi, -math.pi),
            (-0.5 * math.pi, -0.5 * math.pi),
            (0, 0),
            (0.5 * math.pi, 0.5 * math.pi),
            (math.pi, -math.pi),
            (1.5 * math.pi, -0.5 * math.pi),
            (2 * math.pi, 0),
            (2.5 * math.pi, 0.5 * math.pi),
            (3 * math.pi, -math.pi),
            (3.5 * math.pi, -0.5 * math.pi),
        ]:
            with self.subTest(value=value, expected_value=expected_value):
                self.assertAlmostEqual(
                    expected_value,
                    AngleDelta(value, AngleUnit.RADIAN).as_unit(AngleUnit.RADIAN),
                )

    def test_get_angle_delta_value_as_unit(self) -> None:
        delta = AngleDelta(0.5 * math.pi, AngleUnit.RADIAN)

        for unit, expected_value in [
            (AngleUnit.RADIAN, 0.5 * math.pi),
            (AngleUnit.DEGREE, 90),
            (AngleUnit.REVOLUTION, 0.25),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_angle_deltas_produces_angle_delta(self) -> None:
        delta1 = AngleDelta(0.1, AngleUnit.RADIAN)
        delta2 = AngleDelta(0.2, AngleUnit.RADIAN)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(0.3, new_delta.as_unit(AngleUnit.RADIAN))

    def test_subtract_angle_deltas_produces_angle_delta(self) -> None:
        delta1 = AngleDelta(0.3, AngleUnit.RADIAN)
        delta2 = AngleDelta(0.2, AngleUnit.RADIAN)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(0.1, new_delta.as_unit(AngleUnit.RADIAN))

    def test_negative_of_angle_delta(self) -> None:
        delta = AngleDelta(1, AngleUnit.RADIAN)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(AngleUnit.RADIAN))

    def test_compare_angle_deltas(self) -> None:
        for (
            angle_delta1,
            angle_delta2,
            is_equal,
            is_not_equal,
        ) in [
            (
                AngleDelta(0, AngleUnit.RADIAN),
                AngleDelta(0, AngleUnit.RADIAN),
                True,
                False,
            ),
            (
                AngleDelta(0, AngleUnit.RADIAN),
                AngleDelta(1, AngleUnit.RADIAN),
                False,
                True,
            ),
            (
                AngleDelta(1, AngleUnit.RADIAN),
                AngleDelta(0, AngleUnit.RADIAN),
                False,
                True,
            ),
        ]:
            with self.subTest(
                angle_delta1=angle_delta1,
                angle_delta2=angle_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
            ):
                self.assertEqual(is_equal, angle_delta1 == angle_delta2)
                self.assertEqual(is_not_equal, angle_delta1 != angle_delta2)
