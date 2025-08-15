import unittest

from src.units import TimeDelta, TimeUnit


class TimeDeltaTest(unittest.TestCase):
    """Unit tests for time delta class."""

    def test_create_time_delta(self) -> None:
        # Test passes if it simply doesn't throw an exception
        _ = TimeDelta(1, TimeUnit.SECOND)

    def test_get_time_delta_value_as_unit(self) -> None:
        delta = TimeDelta(1, TimeUnit.SECOND)

        for unit, expected_value in [
            (TimeUnit.SECOND, 1),
            (TimeUnit.MINUTE, 1 / 60),
            (TimeUnit.HOUR, 1 / (60 * 60)),
            (TimeUnit.MICROSECOND, 1e6),
            (TimeUnit.MILLISECOND, 1e3),
        ]:
            with self.subTest(unit=unit, expected_value=expected_value):
                self.assertAlmostEqual(expected_value, delta.as_unit(unit))

    def test_add_time_deltas_produces_time_delta(self) -> None:
        delta1 = TimeDelta(1, TimeUnit.SECOND)
        delta2 = TimeDelta(2, TimeUnit.SECOND)
        new_delta = delta1 + delta2
        self.assertAlmostEqual(3, new_delta.as_unit(TimeUnit.SECOND))

    def test_subtract_time_deltas_produces_time_delta(self) -> None:
        delta1 = TimeDelta(3, TimeUnit.SECOND)
        delta2 = TimeDelta(2, TimeUnit.SECOND)
        new_delta = delta1 - delta2
        self.assertAlmostEqual(1, new_delta.as_unit(TimeUnit.SECOND))

    def test_multiply_time_delta_by_value(self) -> None:
        delta = TimeDelta(1, TimeUnit.SECOND)
        new_delta_left_mult = 2 * delta
        new_delta_right_mult = delta * 2
        self.assertAlmostEqual(2, new_delta_left_mult.as_unit(TimeUnit.SECOND))
        self.assertAlmostEqual(2, new_delta_right_mult.as_unit(TimeUnit.SECOND))

    def test_divide_time_delta_by_value(self) -> None:
        delta = TimeDelta(2, TimeUnit.SECOND)
        new_delta = delta / 2
        self.assertAlmostEqual(1, new_delta.as_unit(TimeUnit.SECOND))

    def test_divide_time_delta_by_time_delta_produces_ratio(self) -> None:
        delta1 = TimeDelta(2, TimeUnit.SECOND)
        delta2 = TimeDelta(1, TimeUnit.SECOND)
        ratio = delta1 / delta2
        self.assertAlmostEqual(2, ratio)

    def test_negative_of_time_delta(self) -> None:
        delta = TimeDelta(1, TimeUnit.SECOND)
        new_delta = -delta
        self.assertAlmostEqual(-1, new_delta.as_unit(TimeUnit.SECOND))

    def test_absolute_of_time_delta(self) -> None:
        delta = TimeDelta(-1, TimeUnit.SECOND)
        new_delta = abs(delta)
        self.assertAlmostEqual(1, new_delta.as_unit(TimeUnit.SECOND))

    def test_floor_divide_time_delta_by_time_delta_produces_floored_ratio(
        self,
    ) -> None:
        delta1 = TimeDelta(3, TimeUnit.SECOND)
        delta2 = TimeDelta(2, TimeUnit.SECOND)
        floored_ratio = delta1 // delta2
        self.assertAlmostEqual(1, floored_ratio)

    def test_modulo_time_delta_by_time_delta_produces_ratio_remainder(
        self,
    ) -> None:
        delta1 = TimeDelta(3, TimeUnit.SECOND)
        delta2 = TimeDelta(2, TimeUnit.SECOND)
        remainder = delta1 % delta2
        self.assertAlmostEqual(1, remainder)

    def test_divmod_time_delta_by_time_delta_produces_floored_ratio_and_remainder(
        self,
    ) -> None:
        delta1 = TimeDelta(3, TimeUnit.SECOND)
        delta2 = TimeDelta(2, TimeUnit.SECOND)
        floored_ratio, remainder = divmod(delta1, delta2)
        self.assertAlmostEqual(1, floored_ratio)
        self.assertAlmostEqual(1, remainder)

    def test_compare_time_deltas(self) -> None:
        for (
            time_delta1,
            time_delta2,
            is_equal,
            is_not_equal,
            is_less_than,
            is_less_than_or_equal_to,
            is_greater_than,
            is_greater_than_or_equal_to,
        ) in [
            (
                TimeDelta(0, TimeUnit.SECOND),
                TimeDelta(0, TimeUnit.SECOND),
                True,
                False,
                False,
                True,
                False,
                True,
            ),
            (
                TimeDelta(0, TimeUnit.SECOND),
                TimeDelta(1, TimeUnit.SECOND),
                False,
                True,
                True,
                True,
                False,
                False,
            ),
            (
                TimeDelta(1, TimeUnit.SECOND),
                TimeDelta(0, TimeUnit.SECOND),
                False,
                True,
                False,
                False,
                True,
                True,
            ),
        ]:
            with self.subTest(
                time_delta1=time_delta1,
                time_delta2=time_delta2,
                is_equal=is_equal,
                is_not_equal=is_not_equal,
                is_less_than=is_less_than,
                is_less_than_or_equal_to=is_less_than_or_equal_to,
                is_greater_than=is_greater_than,
                is_greater_than_or_equal_to=is_greater_than_or_equal_to,
            ):
                self.assertEqual(is_equal, time_delta1 == time_delta2)
                self.assertEqual(is_not_equal, time_delta1 != time_delta2)
                self.assertEqual(is_less_than, time_delta1 < time_delta2)
                self.assertEqual(is_less_than_or_equal_to, time_delta1 <= time_delta2)
                self.assertEqual(is_greater_than, time_delta1 > time_delta2)
                self.assertEqual(
                    is_greater_than_or_equal_to,
                    time_delta1 >= time_delta2,
                )
