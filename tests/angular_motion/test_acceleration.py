import math
import unittest

from units import (
    AngleUnit,
    AngularAcceleration,
    TimeUnit,
)


class AngularAccelerationTest(unittest.TestCase):
    """Unit tests for acceleration class."""

    def test_create_acceleration(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND)

    def test_create_acceleration_single_time_unit(self) -> None:
        acceleration1 = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(
            1, AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND
        )
        self.assertAlmostEqual(
            acceleration1.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND),
            acceleration2.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND),
        )

    def test_get_acceleration_value_as_unit_single_time_unit(self) -> None:
        acceleration = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        self.assertAlmostEqual(
            acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND),
            acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND),
        )

    def test_get_acceleration_value_as_unit(self) -> None:
        delta = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)

        # Too many combinations for an exhaustive test - just doing a representative
        # sample
        for distance_unit, first_time_unit, second_time_unit, expected_value in [
            (AngleUnit.RADIAN, TimeUnit.SECOND, None, 1 * 1 * 1),
            (AngleUnit.DEGREE, TimeUnit.SECOND, None, (180 / math.pi) * 1 * 1),
            (AngleUnit.REVOLUTION, TimeUnit.SECOND, None, (1 / (2 * math.pi)) * 1 * 1),
            (AngleUnit.RADIAN, TimeUnit.MINUTE, None, 1 * 60 * 60),
            (AngleUnit.RADIAN, TimeUnit.HOUR, None, 1 * 3_600 * 3_600),
            (AngleUnit.RADIAN, TimeUnit.MICROSECOND, None, 1 * 1e-6 * 1e-6),
            (AngleUnit.RADIAN, TimeUnit.MILLISECOND, None, 1 * 1e-3 * 1e-3),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.SECOND, 1 * 1 * 1),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.MINUTE, 1 * 1 * 60),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.HOUR, 1 * 1 * 3_600),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.MICROSECOND, 1 * 1 * 1e-6),
            (AngleUnit.RADIAN, TimeUnit.SECOND, TimeUnit.MILLISECOND, 1 * 1 * 1e-3),
        ]:
            with self.subTest(unit=distance_unit, expected_value=expected_value):
                self.assertAlmostEqual(
                    expected_value,
                    delta.as_unit(distance_unit, first_time_unit, second_time_unit),
                )

    def test_add_accelerations_produces_acceleration(self) -> None:
        acceleration1 = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_acceleration = acceleration1 + acceleration2
        self.assertAlmostEqual(
            3, new_acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_subtract_accelerations_produces_acceleration(self) -> None:
        acceleration1 = AngularAcceleration(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_acceleration = acceleration1 - acceleration2
        self.assertAlmostEqual(
            1, new_acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_multiply_acceleration_by_value(self) -> None:
        acceleration = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_acceleration_left_mult = 2 * acceleration
        new_acceleration_right_mult = acceleration * 2
        self.assertAlmostEqual(
            2, new_acceleration_left_mult.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_acceleration_right_mult.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_divide_acceleration_by_value(self) -> None:
        acceleration = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_acceleration = acceleration / 2
        self.assertAlmostEqual(
            1, new_acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_divide_acceleration_by_acceleration_produces_ratio(self) -> None:
        acceleration1 = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        ratio = acceleration1 / acceleration2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_acceleration(self) -> None:
        acceleration = AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        negative_acceleration = -acceleration
        self.assertAlmostEqual(
            -1, negative_acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_absolute_of_acceleration(self) -> None:
        acceleration = AngularAcceleration(-1, AngleUnit.RADIAN, TimeUnit.SECOND)
        absolute_acceleration = abs(acceleration)
        self.assertAlmostEqual(
            1, absolute_acceleration.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_floor_divide_acceleration_by_acceleration_produces_floored_ratio(
        self,
    ) -> None:
        acceleration1 = AngularAcceleration(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        floored_ratio = acceleration1 // acceleration2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_acceleration_by_acceleration_produces_ratio_remainder(
        self,
    ) -> None:
        acceleration1 = AngularAcceleration(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        remainder = acceleration1 % acceleration2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_acceleration_by_acceleration_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        acceleration1 = AngularAcceleration(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        acceleration2 = AngularAcceleration(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        floored_ratio, remainder = divmod(acceleration1, acceleration2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_accelerations(self) -> None:
        for (
            acceleration1,
            acceleration2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                AngularAcceleration(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularAcceleration(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                AngularAcceleration(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                AngularAcceleration(1, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularAcceleration(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                volume_delta1=acceleration1,
                volume_delta2=acceleration2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, acceleration1 == acceleration2)
                self.assertEqual(is_not_equal, acceleration1 != acceleration2)
                self.assertEqual(is_less_than, acceleration1 < acceleration2)
                self.assertEqual(
                    is_less_than_or_equal_to, acceleration1 <= acceleration2
                )
                self.assertEqual(is_greater_than, acceleration1 > acceleration2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    acceleration1 >= acceleration2,
                )
