import unittest

from src.units import (
    DistanceUnit,
    Jerk,
    TimeUnit,
)


class JerkTest(unittest.TestCase):
    """Unit tests for jerk class."""

    def test_create_jerk(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Jerk(
            1, DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
        )

    def test_create_jerk_single_time_unit(self) -> None:
        jerk1 = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND)
        jerk3 = Jerk(
            1, DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
        )
        self.assertAlmostEqual(
            jerk1.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
            jerk2.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
        )
        self.assertAlmostEqual(
            jerk1.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
            jerk3.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
        )

    def test_get_jerk_value_as_unit_single_time_unit(self) -> None:
        jerk = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)
        self.assertAlmostEqual(
            jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND),
            jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND),
        )
        self.assertAlmostEqual(
            jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND),
            jerk.as_unit(
                DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
        )

    def test_get_jerk_value_as_unit(self) -> None:
        delta = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)

        # Too many combinations for an exhaustive test - just doing a representative
        # sample
        for (
            distance_unit,
            first_time_unit,
            second_time_unit,
            third_time_unit,
            expected_value,
        ) in [
            (DistanceUnit.METRE, TimeUnit.SECOND, None, None, 1 * 1 * 1 * 1),
            (DistanceUnit.CENTIMETRE, TimeUnit.SECOND, None, None, 100 * 1 * 1 * 1),
            (DistanceUnit.MILLIMETRE, TimeUnit.SECOND, None, None, 1_000 * 1 * 1 * 1),
            (DistanceUnit.YARD, TimeUnit.SECOND, None, None, 1.09361329834 * 1 * 1 * 1),
            (DistanceUnit.FOOT, TimeUnit.SECOND, None, None, 3.28083989501 * 1 * 1 * 1),
            (DistanceUnit.INCH, TimeUnit.SECOND, None, None, 39.3700787402 * 1 * 1 * 1),
            (DistanceUnit.METRE, TimeUnit.MINUTE, None, None, 1 * 60 * 60 * 60),
            (DistanceUnit.METRE, TimeUnit.HOUR, None, None, 1 * 3_600 * 3_600 * 3_600),
            (
                DistanceUnit.METRE,
                TimeUnit.MICROSECOND,
                None,
                None,
                1 * 1e-6 * 1e-6 * 1e-6,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.MILLISECOND,
                None,
                None,
                1 * 1e-3 * 1e-3 * 1e-3,
            ),
            (DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, None, 1 * 1 * 1 * 1),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.MINUTE,
                None,
                1 * 1 * 60 * 60,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.HOUR,
                None,
                1 * 1 * 3_600 * 3_600,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.MICROSECOND,
                None,
                1 * 1 * 1e-6 * 1e-6,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.MILLISECOND,
                None,
                1 * 1 * 1e-3 * 1e-3,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                1 * 1 * 1 * 1,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.MINUTE,
                1 * 1 * 1 * 60,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.HOUR,
                1 * 1 * 1 * 3_600,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.MICROSECOND,
                1 * 1 * 1 * 1e-6,
            ),
            (
                DistanceUnit.METRE,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.MILLISECOND,
                1 * 1 * 1 * 1e-3,
            ),
        ]:
            with self.subTest(
                distance_unit=distance_unit,
                first_time_unit=first_time_unit,
                second_time_unit=second_time_unit,
                third_time_unit=third_time_unit,
                expected_value=expected_value,
            ):
                self.assertAlmostEqual(
                    expected_value,
                    delta.as_unit(
                        distance_unit,
                        first_time_unit,
                        second_time_unit,
                        third_time_unit,
                    ),
                )

    def test_add_jerks_produces_jerk(self) -> None:
        jerk1 = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_jerk = jerk1 + jerk2
        self.assertAlmostEqual(3, new_jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND))

    def test_subtract_jerks_produces_jerk(self) -> None:
        jerk1 = Jerk(3, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_jerk = jerk1 - jerk2
        self.assertAlmostEqual(1, new_jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND))

    def test_multiply_jerk_by_value(self) -> None:
        jerk = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)
        new_jerk_left_mult = 2 * jerk
        new_jerk_right_mult = jerk * 2
        self.assertAlmostEqual(
            2, new_jerk_left_mult.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_jerk_right_mult.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_divide_jerk_by_value(self) -> None:
        jerk = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_jerk = jerk / 2
        self.assertAlmostEqual(1, new_jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND))

    def test_divide_jerk_by_jerk_produces_ratio(self) -> None:
        jerk1 = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)
        ratio = jerk1 / jerk2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_jerk(self) -> None:
        jerk = Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND)
        negative_jerk = -jerk
        self.assertAlmostEqual(
            -1, negative_jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_absolute_of_jerk(self) -> None:
        jerk = Jerk(-1, DistanceUnit.METRE, TimeUnit.SECOND)
        absolute_jerk = abs(jerk)
        self.assertAlmostEqual(
            1, absolute_jerk.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_floor_divide_jerk_by_jerk_produces_floored_ratio(
        self,
    ) -> None:
        jerk1 = Jerk(3, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        floored_ratio = jerk1 // jerk2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_jerk_by_jerk_produces_ratio_remainder(
        self,
    ) -> None:
        jerk1 = Jerk(3, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        remainder = jerk1 % jerk2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_jerk_by_jerk_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        jerk1 = Jerk(3, DistanceUnit.METRE, TimeUnit.SECOND)
        jerk2 = Jerk(2, DistanceUnit.METRE, TimeUnit.SECOND)
        floored_ratio, remainder = divmod(jerk1, jerk2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_jerks(self) -> None:
        for (
            jerk1,
            jerk2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                Jerk(0, DistanceUnit.METRE, TimeUnit.SECOND),
                Jerk(0, DistanceUnit.METRE, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Jerk(0, DistanceUnit.METRE, TimeUnit.SECOND),
                Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Jerk(1, DistanceUnit.METRE, TimeUnit.SECOND),
                Jerk(0, DistanceUnit.METRE, TimeUnit.SECOND),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                volume_delta1=jerk1,
                volume_delta2=jerk2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, jerk1 == jerk2)
                self.assertEqual(is_not_equal, jerk1 != jerk2)
                self.assertEqual(is_less_than, jerk1 < jerk2)
                self.assertEqual(is_less_than_or_equal_to, jerk1 <= jerk2)
                self.assertEqual(is_greater_than, jerk1 > jerk2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    jerk1 >= jerk2,
                )
