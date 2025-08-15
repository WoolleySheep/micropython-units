import math
import unittest

from units import AngleUnit, AngularDisplacement


class AngularDisplacementTest(unittest.TestCase):
    """Unit tests for angular displacement class."""

    def test_create_displacement(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = AngularDisplacement(1, AngleUnit.RADIAN)

    def test_get_displacement_value_as_unit(self) -> None:
        displacement = AngularDisplacement(1, AngleUnit.RADIAN)

        for unit, expected_value in [
            (AngleUnit.RADIAN, 1),
            (AngleUnit.DEGREE, 180 / math.pi),
            (AngleUnit.REVOLUTION, 1 / (2 * math.pi)),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, displacement.as_unit(unit))

    def test_add_displacements_produces_displacement(self) -> None:
        displacement1 = AngularDisplacement(1, AngleUnit.RADIAN)
        displacement2 = AngularDisplacement(2, AngleUnit.RADIAN)
        new_displacement = displacement1 + displacement2
        self.assertAlmostEqual(3, new_displacement.as_unit(AngleUnit.RADIAN))

    def test_subtract_displacements_produces_displacement(self) -> None:
        displacement1 = AngularDisplacement(3, AngleUnit.RADIAN)
        displacement2 = AngularDisplacement(2, AngleUnit.RADIAN)
        new_displacement = displacement1 - displacement2
        self.assertAlmostEqual(1, new_displacement.as_unit(AngleUnit.RADIAN))

    def test_multiply_displacement_by_value(self) -> None:
        displacement = AngularDisplacement(1, AngleUnit.RADIAN)
        new_displacement_left_mult = 2 * displacement
        new_displacement_right_mult = displacement * 2
        self.assertAlmostEqual(2, new_displacement_left_mult.as_unit(AngleUnit.RADIAN))
        self.assertAlmostEqual(2, new_displacement_right_mult.as_unit(AngleUnit.RADIAN))

    def test_divide_displacement_by_value(self) -> None:
        displacement = AngularDisplacement(2, AngleUnit.RADIAN)
        new_displacement = displacement / 2
        self.assertAlmostEqual(1, new_displacement.as_unit(AngleUnit.RADIAN))

    def test_divide_displacement_by_displacement_produces_ratio(self) -> None:
        displacement1 = AngularDisplacement(2, AngleUnit.RADIAN)
        displacement2 = AngularDisplacement(1, AngleUnit.RADIAN)
        ratio = displacement1 / displacement2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_displacement(self) -> None:
        displacement = AngularDisplacement(1, AngleUnit.RADIAN)
        new_displacement = -displacement
        self.assertAlmostEqual(-1, new_displacement.as_unit(AngleUnit.RADIAN))

    def test_absolute_of_displacement(self) -> None:
        displacement = AngularDisplacement(-1, AngleUnit.RADIAN)
        new_displacement = abs(displacement)
        self.assertAlmostEqual(1, new_displacement.as_unit(AngleUnit.RADIAN))

    def test_floor_divide_displacement_by_displacement_produces_floored_ratio(
        self,
    ) -> None:
        displacement1 = AngularDisplacement(3, AngleUnit.RADIAN)
        displacement2 = AngularDisplacement(2, AngleUnit.RADIAN)
        floored_ratio = displacement1 // displacement2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_displacement_by_displacement_produces_ratio_remainder(
        self,
    ) -> None:
        displacement1 = AngularDisplacement(3, AngleUnit.RADIAN)
        displacement2 = AngularDisplacement(2, AngleUnit.RADIAN)
        remainder = displacement1 % displacement2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_displacement_by_displacement_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        displacement1 = AngularDisplacement(3, AngleUnit.RADIAN)
        displacement2 = AngularDisplacement(2, AngleUnit.RADIAN)
        floored_ratio, remainder = divmod(displacement1, displacement2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_displacements(self) -> None:
        for (
            displacement1,
            displacement2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                AngularDisplacement(0, AngleUnit.RADIAN),
                AngularDisplacement(0, AngleUnit.RADIAN),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                AngularDisplacement(0, AngleUnit.RADIAN),
                AngularDisplacement(1, AngleUnit.RADIAN),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                AngularDisplacement(1, AngleUnit.RADIAN),
                AngularDisplacement(0, AngleUnit.RADIAN),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                displacement1=displacement1,
                displacement2=displacement2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, displacement1 == displacement2)
                self.assertEqual(is_not_equal, displacement1 != displacement2)
                self.assertEqual(is_less_than, displacement1 < displacement2)
                self.assertEqual(
                    is_less_than_or_equal_to, displacement1 <= displacement2
                )
                self.assertEqual(is_greater_than, displacement1 > displacement2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    displacement1 >= displacement2,
                )
