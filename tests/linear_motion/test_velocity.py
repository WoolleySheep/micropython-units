import unittest

from src.units import (
    DistanceUnit,
    TimeUnit,
    Velocity,
)


class VelocityTest(unittest.TestCase):
    """Unit tests for velocity class."""

    def test_create_velocity(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND)

    def test_get_velocity_value_as_unit(self) -> None:
        delta = Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND)

        for distance_unit, time_unit, expected_value in [
            (DistanceUnit.METRE, TimeUnit.SECOND, 1 * 1),
            (DistanceUnit.CENTIMETRE, TimeUnit.SECOND, 100 * 1),
            (DistanceUnit.MILLIMETRE, TimeUnit.SECOND, 1_000 * 1),
            (DistanceUnit.YARD, TimeUnit.SECOND, 1.09361329834 * 1),
            (DistanceUnit.FOOT, TimeUnit.SECOND, 3.28083989501 * 1),
            (DistanceUnit.INCH, TimeUnit.SECOND, 39.3700787402 * 1),
            (DistanceUnit.METRE, TimeUnit.MINUTE, 1 * 60),
            (DistanceUnit.CENTIMETRE, TimeUnit.MINUTE, 100 * 60),
            (DistanceUnit.MILLIMETRE, TimeUnit.MINUTE, 1_000 * 60),
            (DistanceUnit.YARD, TimeUnit.MINUTE, 1.09361329834 * 60),
            (DistanceUnit.FOOT, TimeUnit.MINUTE, 3.28083989501 * 60),
            (DistanceUnit.INCH, TimeUnit.MINUTE, 39.3700787402 * 60),
            (DistanceUnit.METRE, TimeUnit.HOUR, 1 * 3_600),
            (DistanceUnit.CENTIMETRE, TimeUnit.HOUR, 100 * 3_600),
            (DistanceUnit.MILLIMETRE, TimeUnit.HOUR, 1_000 * 3_600),
            (DistanceUnit.YARD, TimeUnit.HOUR, 1.09361329834 * 3_600),
            (DistanceUnit.FOOT, TimeUnit.HOUR, 3.28083989501 * 3_600),
            (DistanceUnit.INCH, TimeUnit.HOUR, 39.3700787402 * 3_600),
            (DistanceUnit.METRE, TimeUnit.MICROSECOND, 1 * 1e-6),
            (DistanceUnit.CENTIMETRE, TimeUnit.MICROSECOND, 100 * 1e-6),
            (DistanceUnit.MILLIMETRE, TimeUnit.MICROSECOND, 1_000 * 1e-6),
            (DistanceUnit.YARD, TimeUnit.MICROSECOND, 1.09361329834 * 1e-6),
            (DistanceUnit.FOOT, TimeUnit.MICROSECOND, 3.28083989501 * 1e-6),
            (DistanceUnit.INCH, TimeUnit.MICROSECOND, 39.3700787402 * 1e-6),
            (DistanceUnit.METRE, TimeUnit.MILLISECOND, 1 * 1e-3),
            (DistanceUnit.CENTIMETRE, TimeUnit.MILLISECOND, 100 * 1e-3),
            (DistanceUnit.MILLIMETRE, TimeUnit.MILLISECOND, 1_000 * 1e-3),
            (DistanceUnit.YARD, TimeUnit.MILLISECOND, 1.09361329834 * 1e-3),
            (DistanceUnit.FOOT, TimeUnit.MILLISECOND, 3.28083989501 * 1e-3),
            (DistanceUnit.INCH, TimeUnit.MILLISECOND, 39.3700787402 * 1e-3),
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
        velocity1 = Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND)
        velocity2 = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_velocity = velocity1 + velocity2
        self.assertAlmostEqual(
            3, new_velocity.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_subtract_velocities_produces_velocity(self) -> None:
        velocity1 = Velocity(3, DistanceUnit.METRE, TimeUnit.SECOND)
        velocity2 = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_velocity = velocity1 - velocity2
        self.assertAlmostEqual(
            1, new_velocity.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_multiply_velocity_by_value(self) -> None:
        velocity = Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND)
        new_velocity_left_mult = 2 * velocity
        new_velocity_right_mult = velocity * 2
        self.assertAlmostEqual(
            2, new_velocity_left_mult.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_velocity_right_mult.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_divide_velocity_by_value(self) -> None:
        velocity = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_velocity = velocity / 2
        self.assertAlmostEqual(
            1, new_velocity.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_divide_velocity_by_velocity_produces_ratio(self) -> None:
        velocity1 = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
        velocity2 = Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND)
        ratio = velocity1 / velocity2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_velocity(self) -> None:
        velocity = Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND)
        negative_velocity = -velocity
        self.assertAlmostEqual(
            -1, negative_velocity.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_absolute_of_velocity(self) -> None:
        velocity = Velocity(-1, DistanceUnit.METRE, TimeUnit.SECOND)
        absolute_velocity = abs(velocity)
        self.assertAlmostEqual(
            1, absolute_velocity.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_floor_divide_velocity_by_velocity_produces_floored_ratio(
        self,
    ) -> None:
        velocity1 = Velocity(3, DistanceUnit.METRE, TimeUnit.SECOND)
        velocity2 = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
        floored_ratio = velocity1 // velocity2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_velocity_by_velocity_produces_ratio_remainder(
        self,
    ) -> None:
        velocity1 = Velocity(3, DistanceUnit.METRE, TimeUnit.SECOND)
        velocity2 = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
        remainder = velocity1 % velocity2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_velocity_by_velocity_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        velocity1 = Velocity(3, DistanceUnit.METRE, TimeUnit.SECOND)
        velocity2 = Velocity(2, DistanceUnit.METRE, TimeUnit.SECOND)
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
                Velocity(0, DistanceUnit.METRE, TimeUnit.SECOND),
                Velocity(0, DistanceUnit.METRE, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Velocity(0, DistanceUnit.METRE, TimeUnit.SECOND),
                Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Velocity(1, DistanceUnit.METRE, TimeUnit.SECOND),
                Velocity(0, DistanceUnit.METRE, TimeUnit.SECOND),
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
