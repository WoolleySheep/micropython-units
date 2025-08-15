import unittest

from src.units import (
    Acceleration,
    DistanceUnit,
    TimeUnit,
)


class AccelerationTest(unittest.TestCase):
    """Unit tests for acceleration class."""

    def test_create_acceleration(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND)

    def test_create_acceleration_single_time_unit(self) -> None:
        acceleration1 = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(
            1, DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND
        )
        self.assertAlmostEqual(
            acceleration1.as_unit(DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND),
            acceleration2.as_unit(DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND),
        )

    def test_get_acceleration_value_as_unit_single_time_unit(self) -> None:
        acceleration = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)
        self.assertAlmostEqual(
            acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND),
            acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND),
        )

    def test_get_acceleration_value_as_unit(self) -> None:
        delta = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)

        # Too many combinations for an exhaustive test - just doing a representative
        # sample
        for distance_unit, first_time_unit, second_time_unit, expected_value in [
            (DistanceUnit.METRE, TimeUnit.SECOND, None, 1 * 1 * 1),
            (DistanceUnit.CENTIMETRE, TimeUnit.SECOND, None, 100 * 1 * 1),
            (DistanceUnit.MILLIMETRE, TimeUnit.SECOND, None, 1_000 * 1 * 1),
            (DistanceUnit.YARD, TimeUnit.SECOND, None, 1.09361329834 * 1 * 1),
            (DistanceUnit.FOOT, TimeUnit.SECOND, None, 3.28083989501 * 1 * 1),
            (DistanceUnit.INCH, TimeUnit.SECOND, None, 39.3700787402 * 1 * 1),
            (DistanceUnit.METRE, TimeUnit.MINUTE, None, 1 * 60 * 60),
            (DistanceUnit.METRE, TimeUnit.HOUR, None, 1 * 3_600 * 3_600),
            (DistanceUnit.METRE, TimeUnit.MICROSECOND, None, 1 * 1e-6 * 1e-6),
            (DistanceUnit.METRE, TimeUnit.MILLISECOND, None, 1 * 1e-3 * 1e-3),
            (DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.SECOND, 1 * 1 * 1),
            (DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.MINUTE, 1 * 1 * 60),
            (DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.HOUR, 1 * 1 * 3_600),
            (DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.MICROSECOND, 1 * 1 * 1e-6),
            (DistanceUnit.METRE, TimeUnit.SECOND, TimeUnit.MILLISECOND, 1 * 1 * 1e-3),
        ]:
            with self.subTest(
                distance_unit=distance_unit,
                first_time_unit=first_time_unit,
                second_time_unit=second_time_unit,
                expected_value=expected_value,
            ):
                self.assertAlmostEqual(
                    expected_value,
                    delta.as_unit(distance_unit, first_time_unit, second_time_unit),
                )

    def test_add_accelerations_produces_acceleration(self) -> None:
        acceleration1 = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_acceleration = acceleration1 + acceleration2
        self.assertAlmostEqual(
            3, new_acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_subtract_accelerations_produces_acceleration(self) -> None:
        acceleration1 = Acceleration(3, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_acceleration = acceleration1 - acceleration2
        self.assertAlmostEqual(
            1, new_acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_multiply_acceleration_by_value(self) -> None:
        acceleration = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)
        new_acceleration_left_mult = 2 * acceleration
        new_acceleration_right_mult = acceleration * 2
        self.assertAlmostEqual(
            2, new_acceleration_left_mult.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )
        self.assertAlmostEqual(
            2, new_acceleration_right_mult.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_divide_acceleration_by_value(self) -> None:
        acceleration = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
        new_acceleration = acceleration / 2
        self.assertAlmostEqual(
            1, new_acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_divide_acceleration_by_acceleration_produces_ratio(self) -> None:
        acceleration1 = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)
        ratio = acceleration1 / acceleration2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_acceleration(self) -> None:
        acceleration = Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND)
        negative_acceleration = -acceleration
        self.assertAlmostEqual(
            -1, negative_acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_absolute_of_acceleration(self) -> None:
        acceleration = Acceleration(-1, DistanceUnit.METRE, TimeUnit.SECOND)
        absolute_acceleration = abs(acceleration)
        self.assertAlmostEqual(
            1, absolute_acceleration.as_unit(DistanceUnit.METRE, TimeUnit.SECOND)
        )

    def test_floor_divide_acceleration_by_acceleration_produces_floored_ratio(
        self,
    ) -> None:
        acceleration1 = Acceleration(3, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
        floored_ratio = acceleration1 // acceleration2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_acceleration_by_acceleration_produces_ratio_remainder(
        self,
    ) -> None:
        acceleration1 = Acceleration(3, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
        remainder = acceleration1 % acceleration2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_acceleration_by_acceleration_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        acceleration1 = Acceleration(3, DistanceUnit.METRE, TimeUnit.SECOND)
        acceleration2 = Acceleration(2, DistanceUnit.METRE, TimeUnit.SECOND)
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
                Acceleration(0, DistanceUnit.METRE, TimeUnit.SECOND),
                Acceleration(0, DistanceUnit.METRE, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                Acceleration(0, DistanceUnit.METRE, TimeUnit.SECOND),
                Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                Acceleration(1, DistanceUnit.METRE, TimeUnit.SECOND),
                Acceleration(0, DistanceUnit.METRE, TimeUnit.SECOND),
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
