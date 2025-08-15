import math
import unittest

from units import (
    AngleUnit,
    AngularVelocity,
    TimeUnit,
)


class AngularVelocityTest(unittest.TestCase):
    """Unit tests for angular velocity class."""

    def test_create_velocity(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND)

    def test_get_velocity_value_as_unit(self) -> None:
        delta = AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND)

        for distance_unit, time_unit, expected_value in [
            (AngleUnit.RADIAN, TimeUnit.SECOND, 1 * 1),
            (AngleUnit.DEGREE, TimeUnit.SECOND, (180 / math.pi) * 1),
            (AngleUnit.REVOLUTION, TimeUnit.SECOND, (1 / (2 * math.pi)) * 1),
            (AngleUnit.RADIAN, TimeUnit.MINUTE, 1 * 60),
            (AngleUnit.DEGREE, TimeUnit.MINUTE, (180 / math.pi) * 60),
            (AngleUnit.REVOLUTION, TimeUnit.MINUTE, (1 / (2 * math.pi)) * 60),
            (AngleUnit.RADIAN, TimeUnit.HOUR, 1 * 3_600),
            (AngleUnit.DEGREE, TimeUnit.HOUR, (180 / math.pi) * 3_600),
            (AngleUnit.REVOLUTION, TimeUnit.HOUR, (1 / (2 * math.pi)) * 3_600),
            (AngleUnit.RADIAN, TimeUnit.MICROSECOND, 1 * 1e-6),
            (AngleUnit.DEGREE, TimeUnit.MICROSECOND, (180 / math.pi) * 1e-6),
            (AngleUnit.REVOLUTION, TimeUnit.MICROSECOND, (1 / (2 * math.pi)) * 1e-6),
            (AngleUnit.RADIAN, TimeUnit.MILLISECOND, 1 * 1e-3),
            (AngleUnit.DEGREE, TimeUnit.MILLISECOND, (180 / math.pi) * 1e-3),
            (AngleUnit.REVOLUTION, TimeUnit.MILLISECOND, (1 / (2 * math.pi)) * 1e-3),
        ]:
            with self.subTest(
                distance_unit=distance_unit,
                time_unit=time_unit,
                expected_value=expected_value,
            ):
                self.assertAlmostEqual(
                    expected_value, delta.as_unit(distance_unit, time_unit)
                )

    def test_add_velocities_produces_velocity(self) -> None:
        velocity1 = AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        velocity2 = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_velocity = velocity1 + velocity2
        self.assertAlmostEqual(
            3, new_velocity.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_subtract_velocities_produces_velocity(self) -> None:
        velocity1 = AngularVelocity(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        velocity2 = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_velocity = velocity1 - velocity2
        self.assertAlmostEqual(
            1, new_velocity.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_multiply_velocity_by_value(self) -> None:
        velocity = AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_velocity_left_mult = 2 * velocity
        new_velocity_right_mult = velocity * 2
        self.assertAlmostEqual(
            2, new_velocity_left_mult.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_velocity_right_mult.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_divide_velocity_by_value(self) -> None:
        velocity = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        new_velocity = velocity / 2
        self.assertAlmostEqual(
            1, new_velocity.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_divide_velocity_by_velocity_produces_ratio(self) -> None:
        velocity1 = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        velocity2 = AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        ratio = velocity1 / velocity2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_velocity(self) -> None:
        velocity = AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND)
        negative_velocity = -velocity
        self.assertAlmostEqual(
            -1, negative_velocity.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_absolute_of_velocity(self) -> None:
        velocity = AngularVelocity(-1, AngleUnit.RADIAN, TimeUnit.SECOND)
        absolute_velocity = abs(velocity)
        self.assertAlmostEqual(
            1, absolute_velocity.as_unit(AngleUnit.RADIAN, TimeUnit.SECOND)
        )

    def test_floor_divide_velocity_by_velocity_produces_floored_ratio(
        self,
    ) -> None:
        velocity1 = AngularVelocity(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        velocity2 = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        floored_ratio = velocity1 // velocity2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_velocity_by_velocity_produces_ratio_remainder(
        self,
    ) -> None:
        velocity1 = AngularVelocity(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        velocity2 = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        remainder = velocity1 % velocity2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_velocity_by_velocity_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        velocity1 = AngularVelocity(3, AngleUnit.RADIAN, TimeUnit.SECOND)
        velocity2 = AngularVelocity(2, AngleUnit.RADIAN, TimeUnit.SECOND)
        floored_ratio, remainder = divmod(velocity1, velocity2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_velocities(self) -> None:
        for (
            velocity1,
            velocity2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                AngularVelocity(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularVelocity(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                AngularVelocity(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                AngularVelocity(1, AngleUnit.RADIAN, TimeUnit.SECOND),
                AngularVelocity(0, AngleUnit.RADIAN, TimeUnit.SECOND),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                volume_delta1=velocity1,
                volume_delta2=velocity2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, velocity1 == velocity2)
                self.assertEqual(is_not_equal, velocity1 != velocity2)
                self.assertEqual(is_less_than, velocity1 < velocity2)
                self.assertEqual(is_less_than_or_equal_to, velocity1 <= velocity2)
                self.assertEqual(is_greater_than, velocity1 > velocity2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    velocity1 >= velocity2,
                )
