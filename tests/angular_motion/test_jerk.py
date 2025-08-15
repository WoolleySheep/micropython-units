import math
import unittest

from src.units import (
    AngleUnit,
    AngularJerk,
    TimeUnit,
)


class AngularJerkTest(unittest.TestCase):
    """Unit tests for angular jerk class."""

    def test_create_jerk(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = AngularJerk(
            1, AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
        )

    def test_create_jerk_single_time_unit(self) -> None:
        jerk1 = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND)
        jerk3 = AngularJerk(
            1, AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
        )
        self.assertAlmostEqual(
            jerk1.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
            jerk2.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
        )
        self.assertAlmostEqual(
            jerk1.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
            jerk3.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
        )

    def test_get_jerk_value_as_unit_single_time_unit(self) -> None:
        jerk = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        self.assertAlmostEqual(
            jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND),
            jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND),
        )
        self.assertAlmostEqual(
            jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND),
            jerk.as_unit(
                AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, TimeUnit.SECOND
            ),
        )

    def test_get_jerk_value_as_unit(self) -> None:
        jerk = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)

        # Too many combinations for an exhaustive test - just doing a representative
        # sample
        for (
            distance_unit,
            first_time_unit,
            second_time_unit,
            third_time_unit,
            expected_value,
        ) in [
            (AngleUnit.RADIAN, TimeUnit.SECOND, None, None, 1 * 1 * 1 * 1),
            (
                AngleUnit.DEGREE,
                TimeUnit.SECOND,
                None,
                None,
                (180 / math.pi) * 1 * 1 * 1,
            ),
            (
                AngleUnit.REVOLUTION,
                TimeUnit.SECOND,
                None,
                None,
                (1 / (2 * math.pi)) * 1 * 1 * 1,
            ),
            (AngleUnit.RADIAN, TimeUnit.MINUTE, None, None, 1 * 60 * 60 * 60),
            (AngleUnit.RADIAN, TimeUnit.HOUR, None, None, 1 * 3_600 * 3_600 * 3_600),
            (
                AngleUnit.RADIAN,
                TimeUnit.MICROSECOND,
                None,
                None,
                1 * 1e-6 * 1e-6 * 1e-6,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.MILLISECOND,
                None,
                None,
                1 * 1e-3 * 1e-3 * 1e-3,
            ),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, None, 1 * 1 * 1 * 1),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.MINUTE, None, 1 * 1 * 60 * 60),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.HOUR,
                None,
                1 * 1 * 3_600 * 3_600,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.MICROSECOND,
                None,
                1 * 1 * 1e-6 * 1e-6,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.MILLISECOND,
                None,
                1 * 1 * 1e-3 * 1e-3,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                1 * 1 * 1 * 1,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.MINUTE,
                1 * 1 * 1 * 60,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.HOUR,
                1 * 1 * 1 * 3_600,
            ),
            (
                AngleUnit.RADIAN,
                TimeUnit.SECOND,
                TimeUnit.SECOND,
                TimeUnit.MICROSECOND,
                1 * 1 * 1 * 1e-6,
            ),
            (
                AngleUnit.RADIAN,
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
                    jerk.as_unit(
                        distance_unit,
                        first_time_unit,
                        second_time_unit,
                        third_time_unit,
                    ),
                )

    def test_add_jerks_produces_jerk(self) -> None:
        jerk1 = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_jerk = jerk1 + jerk2
        self.assertAlmostEqual(3, new_jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND))

    def test_subtract_jerks_produces_jerk(self) -> None:
        jerk1 = AngularJerk(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_jerk = jerk1 - jerk2
        self.assertAlmostEqual(1, new_jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND))

    def test_multiply_jerk_by_value(self) -> None:
        jerk = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_jerk_left_mult = 2 * jerk
        new_jerk_right_mult = jerk * 2
        self.assertAlmostEqual(
            2, new_jerk_left_mult.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_jerk_right_mult.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_divide_jerk_by_value(self) -> None:
        jerk = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_jerk = jerk / 2
        self.assertAlmostEqual(1, new_jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND))

    def test_divide_jerk_by_jerk_produces_ratio(self) -> None:
        jerk1 = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        ratio = jerk1 / jerk2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_jerk(self) -> None:
        jerk = AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        negative_jerk = -jerk
        self.assertAlmostEqual(
            -1, negative_jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_absolute_of_jerk(self) -> None:
        jerk = AngularJerk(-1, AngleUnit.RADIAN, TimeUnit.SECOND)
        absolute_jerk = abs(jerk)
        self.assertAlmostEqual(
            1, absolute_jerk.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_floor_divide_jerk_by_jerk_produces_floored_ratio(
        self,
    ) -> None:
        jerk1 = AngularJerk(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        floored_ratio = jerk1 // jerk2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_jerk_by_jerk_produces_ratio_remainder(
        self,
    ) -> None:
        jerk1 = AngularJerk(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        remainder = jerk1 % jerk2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_jerk_by_jerk_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        jerk1 = AngularJerk(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        jerk2 = AngularJerk(2, AngleUnit.RADIAN, TimeUnit.SECOND)
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
                AngularJerk(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularJerk(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                AngularJerk(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                AngularJerk(1, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularJerk(0, AngleUnit.RADIAN, TimeUnit.SECOND),
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
