import unittest

from src.units import Displacement, DistanceUnit


class DisplacementTest(unittest.TestCase):
    """Unit tests for displacement class."""

    def test_create_displacement(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Displacement(1, DistanceUnit.METRE)

    def test_get_displacement_value_as_unit(self) -> None:
        displacement = Displacement(1, DistanceUnit.METRE)

        for unit, expected_value in [
            (DistanceUnit.METRE, 1),
            (DistanceUnit.CENTIMETRE, 100),
            (DistanceUnit.MILLIMETRE, 1_000),
            (DistanceUnit.YARD, 1.09361329834),
            (DistanceUnit.FOOT, 3.28083989501),
            (DistanceUnit.INCH, 39.3700787402),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, displacement.as_unit(unit))

    def test_add_displacements_produces_displacement(self) -> None:
        displacement1 = Displacement(1, DistanceUnit.METRE)
        displacement2 = Displacement(2, DistanceUnit.METRE)
        new_displacement = displacement1 + displacement2
        self.assertAlmostEqual(3, new_displacement.as_unit(DistanceUnit.METRE))

    def test_subtract_displacements_produces_displacement(self) -> None:
        displacement1 = Displacement(3, DistanceUnit.METRE)
        displacement2 = Displacement(2, DistanceUnit.METRE)
        new_displacement = displacement1 - displacement2
        self.assertAlmostEqual(1, new_displacement.as_unit(DistanceUnit.METRE))

    def test_multiply_displacement_by_value(self) -> None:
        displacement = Displacement(1, DistanceUnit.METRE)
        new_displacement_left_mult = 2 * displacement
        new_displacement_right_mult = displacement * 2
        self.assertAlmostEqual(
            2, new_displacement_left_mult.as_unit(DistanceUnit.METRE)
        )
        self.assertAlmostEqual(
            2, new_displacement_right_mult.as_unit(DistanceUnit.METRE)
        )

    def test_divide_displacement_by_value(self) -> None:
        displacement = Displacement(2, DistanceUnit.METRE)
        new_displacement = displacement / 2
        self.assertAlmostEqual(1, new_displacement.as_unit(DistanceUnit.METRE))

    def test_divide_displacement_by_displacement_produces_ratio(self) -> None:
        displacement1 = Displacement(2, DistanceUnit.METRE)
        displacement2 = Displacement(1, DistanceUnit.METRE)
        ratio = displacement1 / displacement2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_displacement(self) -> None:
        displacement = Displacement(1, DistanceUnit.METRE)
        new_displacement = -displacement
        self.assertAlmostEqual(-1, new_displacement.as_unit(DistanceUnit.METRE))

    def test_absolute_of_displacement(self) -> None:
        displacement = Displacement(-1, DistanceUnit.METRE)
        new_displacement = abs(displacement)
        self.assertAlmostEqual(1, new_displacement.as_unit(DistanceUnit.METRE))

    def test_floor_divide_displacement_by_displacement_produces_floored_ratio(
        self,
    ) -> None:
        displacement1 = Displacement(3, DistanceUnit.METRE)
        displacement2 = Displacement(2, DistanceUnit.METRE)
        floored_ratio = displacement1 // displacement2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_displacement_by_displacement_produces_ratio_remainder(
        self,
    ) -> None:
        displacement1 = Displacement(3, DistanceUnit.METRE)
        displacement2 = Displacement(2, DistanceUnit.METRE)
        remainder = displacement1 % displacement2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_displacement_by_displacement_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        displacement1 = Displacement(3, DistanceUnit.METRE)
        displacement2 = Displacement(2, DistanceUnit.METRE)
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
                Displacement(0, DistanceUnit.METRE),
                Displacement(0, DistanceUnit.METRE),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Displacement(0, DistanceUnit.METRE),
                Displacement(1, DistanceUnit.METRE),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Displacement(1, DistanceUnit.METRE),
                Displacement(0, DistanceUnit.METRE),
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
